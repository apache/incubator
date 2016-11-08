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
import ConfigParser
import contextlib
import inspect
from logging import getLogger
import logging
import os
import sys

import argparse

from asf.utils.auth import get_username, get_password, AUTH_SECTION, save_password, AUTH_SECTIONS, remove_password
from asf.utils.config import load_config


def entrypoint(method, depth=1, cls=None):
    """
      Run a method as your __main__ via decorator.

      Example::

        @asf.cli.entrypoint
        def main(cli):
          ...

      Shorthand for::

        def main():

          cli = asf.cli.CLI()

          ...

        if __name__ == '__main__':
          method()
    """

    current_frame = inspect.currentframe(depth).f_locals

    if '__name__' in current_frame and current_frame['__name__'] == '__main__':

        if cls is None:
            cls = CLI

        method(cls())

    return method


class CLI(object):
    """
        Initialize a command line helper instance.

        Example::

          import asf.cli

          # Adding a version variable will automatically let you use --version on the command line.
          # VERSION is also acceptable.
          version = "1.0"

          @asf.cli.entrypoint
          def main(cli):

            cli.add_argument("-p", "--podling", required=True, default="yoko", help="Podling to operate on.")
            cli.add_argument("-q", dest="quiet", action="store_true", help="An example flag")

            with cli.run():
              if not cli.args.quiet:
                cli.log.info("Operating in Incubator podling: %s", cli.args.podling)

        .. note::

          When you use asf.cli the following are available in __main__: cli, args & log.

        .. note::

          If using --log or --log-file, you can override the default FileHandler by supplying
          a log_file_handler() function that returns a valid logging.handler.

          Example::

            def log_file_handler(filename):
              return logging.handlers.TimedRotatingFileHandler(filename, when='midnight', backupCount=14)

        .. note::

          Example::
            @asf.cli.entrypoint
            def main(cli):
              ...
              cli.influx_logger.enable_reporting()
              with cli.run():
                ...

    """

    exceptions = {}

    def __init__(self, name=None):

        if name is None:
            name = os.path.basename(sys.argv[0])

        #: The name of this cli instance.
        self.name = name

        #: :mod:`argparse` replaces optparse in Python 2.7, it is installable as a stand-alone module.
        self.argparser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)

        self.argparser.add_argument(
            '--debug', action='store_true', default=False, help='Turn on debug mode / logging.'
        )

        self.argparser.add_argument(
            '--trace', action='store_true', default=False, help='Turn on trace logging. Implies --debug.'
        )

        self.argparser.add_argument(
            '--log', help='Log file destination. Defaults to stdout only.'
        )

        #: Call into a :mod:`logging` instance.
        self.log = getLogger(self.name)

        # If the user has version defined, display it.
        for name in ('version', 'VERSION'):
            if hasattr(sys.modules['__main__'], name):
                self.argparser.add_argument('--version', action='version', version='%(prog)s ' + getattr(sys.modules['__main__'], name))

        #: :class:`ConfigParser` configuration object if --config was passed on the command line.
        #: Default is None.
        self.config = None

        #: Configuration file to load. Default is None.
        self.config_file = None

        #: Description for the argument parser.
        self.description = None

        #: Epilog for the argument parser.
        self.epilog = None

        #: Parsed arguments.
        self.args = None

        #: Unrecognized arguments.
        self.unrecognized_args = None

        # Disable logging by default, programs can enable if it is wanted

        if self.log:
            # Keep the handler around, so we can change it's level later.
            self.console = logging.StreamHandler()
            self.console.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
            self.console.setLevel(logging.INFO)

            self.log.addHandler(self.console)

            # This controls the global level for loggers. Filtering will occur in handlers for levels.
            self.log.setLevel(logging.INFO)

        #: Caller can always write DEBUG level logs to a filename.
        #: Using --log on the command line will override this variable.
        self.log_file = None

        #: :class:`logging` FileHandler instance if --log was passed, or `log_file` is set.
        self.log_file_handler = None

        # Defaults to use only when there are no other arguments.
        self.argument_defaults = None

        # Flag to determine if it should attempt to send stats or not.
        self.should_send_stats = False

        # Flag to determine if we should parse the --config file.
        self.should_parse_config = False

        # Should we include standard documentation links
        self.should_use_default_wiki_location_for_docstring = False

        # Should we process the username and passwords
        self.use_username_password_store = None


    def add_argument(self, *args, **kwargs):
        """
          Add a command line argument.

          The current underlying implementation uses :mod:`argparse`.
        """

        self.argparser.add_argument(*args, **kwargs)

    def add_argument_defaults(self, **kwargs):
        """
          Set defaults to be passed to the argument parser ONLY when there are
          no other arguments on the command line. If you want regular defaults,
          use the default= setting on :meth:`add_argument`.

          Example::

            cli.add_argument_defaults(start=True, debug=True)
        """

        self.argument_defaults = kwargs

    def add_config_option(self, default=None):
        """ Add a --config option to the argument parser. """

        self.argparser.add_argument('--config', default=default, help='Config file to read. Defaults to: %(default)s')
        self.should_parse_config = True

    def add_username_password(self, use_store=False):
        """ Add --username and --password options
          :param bool use_store: Name of the section (concept, command line options, API reference)
        """
        self.argparser.add_argument('--username', default=None, help='Username')
        self.argparser.add_argument('--password', default=None, help='Password')
        self.argparser.add_argument('--clear-store', action='store_true', default=False, help='Clear password keystore')

        self.use_username_password_store = use_store

    def _add_documentation_link(self, links, section, variable_name, default=None):
        """
          :param list links: List of links to append link of the form "Section: <link>", if link available
          :param str section: Name of the section (concept, command line options, API reference)
          :param str variable_name: Variable name in main module that should hold URL to documentation
          :param str default: Default URL to documentation
        """

        url = getattr(sys.modules['__main__'], variable_name, default)

        if url:
            links.append('%s: %s' % (section, url))

    def __parse_args(self, accept_unrecognized_args=False):
        """ Invoke the argument parser. """

        # If the user provided a description, use it. Otherwise grab the doc string.
        if self.description:
            self.argparser.description = self.description
        elif getattr(sys.modules['__main__'], '__doc__', None):
            self.argparser.description = getattr(sys.modules['__main__'], '__doc__')
        else:
            self.argparser.description = 'No documentation defined. Please add a doc string to %s' % sys.modules['__main__'].__file__

        self.argparser.epilog = self.epilog

        # Only if there aren't any other command line arguments.
        if len(sys.argv) == 1 and self.argument_defaults:
            self.argparser.set_defaults(**self.argument_defaults)

        if accept_unrecognized_args:
            self.args, self.unrecognized_args = self.argparser.parse_known_args()
        else:
            self.args = self.argparser.parse_args()

    def __parse_config(self):
        """ Invoke the config file parser. """

        if self.should_parse_config and (self.args.config or self.config_file):
            self.config = ConfigParser.SafeConfigParser()
            self.config.read(self.args.config or self.config_file)

    def __process_username_password(self):
        """ If indicated, process the username and password """

        if self.use_username_password_store is not None:
            if self.args.clear_store:
                with load_config(AUTH_SECTIONS) as config:
                    config.remove_option(AUTH_SECTION, 'username')
            if not self.args.username:
                self.args.username = get_username(use_store=self.use_username_password_store)

            if self.args.clear_store:
                remove_password(AUTH_SECTION, username=self.args.username)
            if not self.args.password:
                self.args.password = get_password(AUTH_SECTION, username=self.args.username)
                if self.use_username_password_store:
                    save_password(AUTH_SECTION, self.args.password, self.args.username)

    def __finish_initializing(self):
        """ Handle any initialization after arguments & config has been parsed. """

        if self.args.debug or self.args.trace:
            # Set the console (StreamHandler) to allow debug statements.

            if self.args.debug:
                self.console.setLevel(logging.DEBUG)

            self.console.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s %(name)s - %(message)s'))

            # Set the global level to debug.
            if self.args.debug:
                self.log.setLevel(logging.DEBUG)

        if self.args.log or self.log_file:

            # Allow the user to override the default log file handler.
            try:
                self.log_file_handler = sys.modules['__main__'].log_file_handler(self.args.log or self.log_file)
            except Exception:
                self.log_file_handler = logging.FileHandler(self.args.log or self.log_file)

            self.log_file_handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s %(name)s - %(message)s'))
            self.log_file_handler.setLevel(logging.DEBUG)

            self.log.addHandler(self.log_file_handler)

        # Allow cli.log, args & self to be accessed from __main__
        if not hasattr(sys.modules['__main__'], 'log'):
            sys.modules['__main__'].log = self.log

        if not hasattr(sys.modules['__main__'], 'cli'):
            sys.modules['__main__'].cli = self

        if not hasattr(sys.modules['__main__'], 'args'):
            sys.modules['__main__'].args = self.args

    @classmethod
    def register_exception(cls, exception, func):
        """
          Allow callers to register a function to be run when the given
          exception is raised while inside a cli.run() context manager.
        """

        cls.exceptions[exception] = func

    @contextlib.contextmanager
    def run(self, accept_unrecognized_args=False):
        """
          Called via the `with` statement to invoke the :func:`contextlib.contextmanager`.

          Control is then yielded back to the caller.

          All exceptions are caught & a stack trace emitted, except in the case of `asf.cli.ExitedCleanly`.
        """

        self.__parse_args(accept_unrecognized_args)
        self.__parse_config()
        self.__process_username_password()
        self.__finish_initializing()

        exit_status = 0

        try:
            yield self
        except ExitedCleanly:
            pass
        except (Exception, KeyboardInterrupt) as e:
            # Run any method a library or caller might have registered.
            for base in type(e).mro():
                if base in self.exceptions:
                    self.exceptions[base](e)
                    break
            else:
                self.log.exception(e)

            exit_status = os.EX_SOFTWARE
        finally:
            logging.shutdown()

        sys.exit(exit_status)


class ExitedCleanly(StandardError):
    """ Use instead of sys.exit() to throw an exception but not log an error. """
    pass


def prompt_options(text, options):
    for idx, value in enumerate(options):
        print '%s: %s' % (idx + 1, value)
    text += ' [1 to %s, enter to skip] ' % len(options)
    while True:
        answer = raw_input(text)
        if not answer:
            return None
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= len(options):
                return answer - 1


def prompt_yes_no(text, default=None):
    if default is None:
        text += ' (y/n) '
    elif default:
        text += ' (Y/n) '
    else:
        text += ' (y/N) '
    while True:
        answer = raw_input(text)
        if not answer and default is not None:
            return default
        if answer.lower() == 'y':
            return True
        if answer.lower() == 'n':
            return False
