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
from nose.plugins.attrib import attr

from asf.utils.emails import aliases_for, email_from_alias, canonical_email_address, is_apache_email_address, get_mail_aliases
from asf.utils.test import ensure_credentials_stored


def test_canonical_email_address():
    assert 'jim@jagunet.com' == canonical_email_address('jim@jaguNET.com')

    try:
        canonical_email_address('a@B.com,c@D.com')
        assert False, 'malformed email addresses should generate a value error'
    except ValueError:
        pass


def test_is_apache_email_address():
    assert is_apache_email_address('adc@ApAcHe.org')


@attr('integration')
@ensure_credentials_stored
def test_aliases_for(username, password):
    aliases = aliases_for('adc@ApAcHe.org', get_mail_aliases(username, password))
    assert 'adc@toolazydogs.com' in aliases
    assert 'list@toolazydogs.com' in aliases
    assert 'alan.cabrera@gmail.com' in aliases


@attr('integration')
@ensure_credentials_stored
def test_email_from_alias(username, password):
    assert email_from_alias('list@toolazydogs.com', get_mail_aliases(username, password)) == 'adc@apache.org'
