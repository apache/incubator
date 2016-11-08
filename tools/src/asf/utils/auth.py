#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
"""
  Deal with password loading & saving.

  To opt-in to the various key chains, please create a file: ~/.asf-tools.ini with the contents:

    [keychain]
    gnome-keychain.enable = True
    kde-keychain.enable = True
    crypted-keychain.enable = True

  Note that the OS X keychain is always available on OS X.
"""
import getpass
from logging import getLogger
import os
import subprocess
import sys

from brownie.caching import memoize
import keyring
from keyring.backend import OSXKeychain, GnomeKeyring, KDEKWallet, CryptedFileKeyring
from keyring.errors import PasswordSetError

from asf.utils.config import load_config


AUTH_SECTION = 'org.asf.auth'
KEYCHAIN_SECTION = 'keychain'

log = getLogger(__name__)

_unlocked = set()

AUTH_CONFIG_DEFAULTS = {'gnome-keychain.enable': False,
                        'kde-keychain.enable': False,
                        'crypted-keychain.enable': False}
AUTH_SECTIONS = [AUTH_SECTION, KEYCHAIN_SECTION]


class FixedOSXKeychain(OSXKeychain):
    """ OSXKeychain does not implement delete_password() yet """

    def delete_password(self, service, username):
        """Delete the password for the username of the service.
        """
        try:
            # set up the call for security.
            call = subprocess.Popen([
                                        'security',
                                        'delete-generic-password',
                                        '-a',
                                        username,
                                        '-s',
                                        service
                                    ],
                                    stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
            )
            stdoutdata, stderrdata = call.communicate()
            code = call.returncode
            # check return code.
            if code is not 0:
                raise PasswordSetError('Can\'t delete password in keychain')
        except:
            raise PasswordSetError("Can't delete password in keychain")


@memoize
def initialize_keychain():
    # NB: keyring has a config file, but it only allows a single keyring to be
    # selected, instead of reusing it's supported() method check against a list
    # of backend implementations to try.

    keyring_backends = []

    with load_config(AUTH_SECTIONS, AUTH_CONFIG_DEFAULTS) as config:

        if config.get(KEYCHAIN_SECTION, 'crypted-keychain.enable'):
            keyring_backends.insert(0, CryptedFileKeyring())

        if config.get(KEYCHAIN_SECTION, 'kde-keychain.enable'):
            keyring_backends.insert(0, KDEKWallet())

        if config.get(KEYCHAIN_SECTION, 'gnome-keychain.enable'):
            keyring_backends.insert(0, GnomeKeyring())

    keyring_backends.insert(0, FixedOSXKeychain())
    keyring_backends.sort(key=lambda x: -x.supported())

    keyring.set_keyring(keyring_backends[0])

    # Return True if there are any supported keychains.
    return not all(i.supported() == -1 for i in keyring_backends)


def clear_username_from_store():
    with load_config(AUTH_SECTIONS, AUTH_CONFIG_DEFAULTS) as config:
        config.remove(AUTH_SECTION, 'username')


def get_username(use_store=False):
    if use_store:
        with load_config(AUTH_SECTIONS, AUTH_CONFIG_DEFAULTS) as config:
            username = config.get(AUTH_SECTION, 'username')
            if not username:
                username = raw_input("Username [%s]: " % getpass.getuser())
                if not username:
                    username = getpass.getuser()
                config.set(AUTH_SECTION, 'username', username)
    else:
        username = raw_input("Username [%s]: " % getpass.getuser())
        if not username:
            username = getpass.getuser()

    return username


def unlock_keychain(username):
    """ If the user is running via SSH, their Keychain must be unlocked first. """

    if 'SSH_TTY' not in os.environ:
        return

    # Don't unlock if we've already seen this user.
    if username in _unlocked:
        return

    _unlocked.add(username)

    if sys.platform == 'darwin':
        sys.stderr.write("You are running under SSH. Please unlock your local OS X KeyChain:\n")
        subprocess.call(['security', 'unlock-keychain'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def save_password(entry, password, username=None):
    """
      Saves the given password in the user's keychain.

      :param entry: The entry in the keychain. This is a caller specific key.
      :param password: The password to save in the keychain.
      :param username: The username to get the password for. Default is the current user.
    """

    if username is None:
        username = get_username()

    has_keychain = initialize_keychain()

    if has_keychain:
        try:
            keyring.set_password(entry, username, password)
        except Exception as e:
            log.warn("Unable to set password in keyring. Continuing..")
            log.debug(e)


def remove_password(entry, username=None):
    """
      Removes the password for the specific user in the user's keychain.

      :param entry: The entry in the keychain. This is a caller specific key.
      :param username: The username whose password is to be removed. Default is the current user.
    """

    if username is None:
        username = get_username()

    has_keychain = initialize_keychain()

    if has_keychain:
        try:
            keyring.delete_password(entry, username)
        except Exception as e:
            print e
            log.warn("Unable to delete password in keyring. Continuing..")
            log.debug(e)


def get_password(entry=None, username=None, prompt=None, always_ask=False):
    """
      Prompt the user for a password on stdin.

      :param username: The username to get the password for. Default is the current user.
      :param entry: The entry in the keychain. This is a caller specific key.
      :param prompt: The entry in the keychain. This is a caller specific key.
      :param always_ask: Force the user to enter the password every time.
    """

    password = None

    if username is None:
        username = get_username()

    has_keychain = initialize_keychain()

    # Unlock the user's keychain otherwise, if running under SSH, 'security(1)' will thrown an error.
    unlock_keychain(username)

    if prompt is None:
        prompt = "Enter %s's password: " % username

    if has_keychain and entry is not None and always_ask is False:
        password = get_password_from_keyring(entry, username)

    if password is None:
        password = getpass.getpass(prompt=prompt)

    return password


def get_password_from_keyring(entry=None, username=None):
    """
      :param entry: The entry in the keychain. This is a caller specific key.
      :param username: The username to get the password for. Default is the current user.
    """

    password = None

    if username is None:
        username = get_username()

    has_keychain = initialize_keychain()

    # Unlock the user's keychain otherwise, if running under SSH, 'security(1)' will thrown an error.
    unlock_keychain(username)

    if has_keychain and entry is not None:
        try:
            return keyring.get_password(entry, username)
        except Exception as e:
            log.warn("Unable to get password from keyring. Continuing..")
            log.debug(e)

    return None


def validate_password(entry, username, check_function, password=None, retries=1, save_on_success=True, prompt=None, **check_args):
    """
      Validate a password with a check function & retry if the password is incorrect.

      Useful for after a user has changed their password in LDAP, but their local keychain entry is then out of sync.

      :param str entry: The keychain entry to fetch a password from.
      :param str username: The username to authenticate
      :param func check_function: Check function to use. Should take (username, password, **check_args)
      :param str password: The password to validate. If `None`, the user will be prompted.
      :param int retries: Number of retries to prompt the user for.
      :param bool save_on_success: Save the password if the validation was successful.
      :param str prompt: Alternate prompt to use when asking for the user's password.

      :returns: `True` on successful authentication. `False` otherwise.
      :rtype: bool
    """

    if password is None:
        password = get_password(entry, username, prompt)

    for _ in xrange(retries + 1):

        if check_function(username, password, **check_args):
            if save_on_success:
                save_password(entry, password, username)

            return True

        log.error("Couldn't successfully authenticate your username & password..")

        password = get_password(entry, username, prompt, always_ask=True)

    return False


def get_stored_credentials():
    """
        Gets the credentials, username and password, that have been stored in
        ~/.asf-tools.ini and the secure keychain respectively without bothering
        to prompt the user if either credential cannot be found.

        :returns: username and password
        :rtype: tuple of str
    """
    with load_config(AUTH_SECTIONS, AUTH_CONFIG_DEFAULTS) as config:
        username = config.get(AUTH_SECTION, 'username')
        if not username:
            # if we don't have a username then we cannot lookup the password
            return None, None

    has_keychain = initialize_keychain()
    # Unlock the user's keychain otherwise, if running under SSH, 'security(1)' will thrown an error.
    unlock_keychain(username)

    if has_keychain:
        try:
            password = keyring.get_password(AUTH_SECTION, username)
            return username, password
        except Exception as e:
            log.warn("Unable to get password from keyring. Continuing..")
            log.debug(e)

    return username, None
