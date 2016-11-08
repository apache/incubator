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
import os
import datetime

from nose.plugins.attrib import attr

from asf.incubator.podlings import Podling, retired, graduated, incubating, VALID_STATUS
from asf.utils.committers import get_committer
from asf.utils.test import ensure_credentials_stored


DATA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


@attr('integration')
@ensure_credentials_stored
def test_from_xml(username, password):
    with open(os.path.join(DATA_ROOT, 'podlings.xml'), 'r') as fh:
        podlings = Podling.from_file_handle(fh)
        assert podlings
        assert len(podlings) == 184

        for podling in podlings:
            assert podling.name
            assert podling.description
            assert podling.resource
            assert podling.sponsor
            assert podling.start_date and isinstance(podling.start_date, datetime.date)
            assert not podling.end_date or isinstance(podling.end_date, datetime.date)
            assert podling.status in VALID_STATUS
            assert not podling.reporting_group or isinstance(podling.reporting_group, int)
            for mentor in podling.mentors:
                try:
                    committer = get_committer(mentor, username, password)
                    print committer.fullname, 'is a committer'
                except KeyError:
                    print mentor, 'is not a committer'

        assert len(incubating(podlings)) == 34
        assert len(graduated(podlings)) == 118
        assert len(retired(podlings)) == 32
