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
import json
from logging import getLogger

from restkit import Resource, BasicAuth, ResourceNotFound

from asf.utils.emails import canonical_email_address


COMMITTERS_URL = 'https://whimsy.apache.org/roster/committer'

log = getLogger(__name__)


class Committer(object):
    def __init__(self, username, member, fullname, emails, urls, committees, projects, mentoring):
        self.username = username
        self.member = member
        self.fullname = fullname
        self.emails = set(emails)
        self.urls = set(urls)
        self.committees = set(committees)
        self.projects = set(projects)
        self.mentoring = set(mentoring)

    def as_tuple(self):
        return (self.username, self.member, self.fullname, tuple(sorted(self.emails)), tuple(sorted(self.urls)), tuple(sorted(self.committees)), tuple(sorted(self.projects)), tuple(sorted(self.mentoring)))

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __hash__(self):
        return hash(self.as_tuple())

    def __repr__(self):
        return 'Committer(%s, %s, %s, %s, %s, %s, %s, %s)' % self.as_tuple()


COMMITTERS = {}


def get_committer(committer, username, password):
    global COMMITTERS
    if committer not in COMMITTERS:
        try:
            committer_json = json.loads(Resource('%s/%s' % (COMMITTERS_URL, committer),
                                                 filters=[BasicAuth(username, password)],
                                                 timeout=10).get(headers={'Accept': 'application/json'}).body_string())
        except ResourceNotFound:
            log.warning('Unable to find committer %s' % committer)
        else:
            availid = committer_json['availid']
            member = bool(committer_json['member'])
            fullname = committer_json['name']

            emails = set()
            for email in committer_json['emails']:
                try:
                    emails.add(canonical_email_address(email))
                except ValueError:
                    log.warning('Malformed email address %s not added to committer %s', email, committer)

            urls = committer_json['urls']
            committees = committer_json['committees']
            projects = set(committer_json['groups'])
            if 'apsite' in projects: projects.remove('apsite')
            if 'committers' in projects: projects.remove('committers')
            if 'member' in projects: projects.remove('member')
            mentoring = committer_json['auth']

            COMMITTERS[committer] = Committer(availid, member, fullname, emails, urls, committees, projects, mentoring)

    return COMMITTERS[committer]
