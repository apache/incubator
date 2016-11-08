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
Provides access to https://id.apache.org/info/MailAlias.txt.
"""
from collections import defaultdict
from restkit import BasicAuth, Resource

from brownie.caching import memoize


MAIL_ALIAS_URL = 'https://id.apache.org/info/MailAlias.txt'


@memoize
def canonical_email_address(email):
    if '@' in email:
        local, domain = email.split('@')
        return '%s@%s' % (local, domain.lower())
    else:
        return email


@memoize
def is_apache_email_address(email):
    return canonical_email_address(email).endswith('@apache.org')


@memoize
def username_from_apache_email(email):
    if not is_apache_email_address(email):
        raise ValueError('%s is not a valid Apache Software Foundation email' % email)

    return email.split('@')[0]


def aliases_for(apache_email, mail_aliases):
    apache_email = canonical_email_address(apache_email)
    if apache_email in mail_aliases:
        return mail_aliases[apache_email]['aliases']
    else:
        raise ValueError('%s is not in the mail aliases file' % apache_email)


def email_from_alias(alias_email, mail_aliases):
    alias_email = canonical_email_address(alias_email)
    for apache_email_address, data in mail_aliases.iteritems():
        if alias_email in data['aliases']:
            return apache_email_address
    return None


def get_mail_aliases(username, password):
    mail_aliases = defaultdict(dict)
    for line in Resource(MAIL_ALIAS_URL, filters=[BasicAuth(username, password)], timeout=10).get().body_stream():
        apache_email, alias_email, member = [canonical_email_address(field.strip()) for field in line.split(',')]
        mail_aliases[apache_email]['member'] = bool(member)
        if 'aliases' not in mail_aliases[apache_email]:
            mail_aliases[apache_email]['aliases'] = set()
        mail_aliases[apache_email]['aliases'].add(alias_email)

    return mail_aliases
