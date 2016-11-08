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
from datetime import datetime
import xml.etree.ElementTree as etree

from restkit import Resource


PODLING_URI = 'http://incubator.apache.org/podlings.xml'

VALID_STATUS = set(['current', 'graduated', 'retired'])


class Podling(object):
    def __init__(self, name, description, status, mentors, resource, sponsor, start_date, end_date, reporting_group):
        self.name = name
        self.description = description
        self.status = status
        self.mentors = mentors
        self.resource = resource
        self.sponsor = sponsor
        self.start_date = start_date
        self.end_date = end_date
        self.reporting_group = reporting_group

    def as_tuple(self):
        return (self.name, self.description, self.status, tuple(sorted(self.mentors)), self.resource, self.sponsor, self.start_date, self.end_date, self.reporting_group)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __hash__(self):
        return hash(self.as_tuple())

    def __repr__(self):
        return 'Podling(%s, %s, %s, %s, %s, %s, %s, %s, %s)' % self.as_tuple()

    @classmethod
    def from_xml_element(cls, podling_element):
        name = podling_element.get('name')
        description = podling_element.find('description').text
        status = podling_element.get('status')
        resource = podling_element.get('resource')
        sponsor = podling_element.get('sponsor')
        start_date = _date_from_string(podling_element.get('startdate'))
        end_date = _date_from_string(podling_element.get('enddate')) if 'enddate' in podling_element else None

        if 'reporting' in podling_element:
            reporting_element = podling_element.find('reporting')
            reporting_group = int(reporting_element.get('group'))
        else:
            reporting_group = None

        mentors = set()
        mentors_element = podling_element.find('mentors')
        for mentor_element in mentors_element.getiterator('mentor'):
            if mentor_element.get('username'):
                mentors.add(mentor_element.get('username'))

        return cls(name, description, status, mentors, resource, sponsor, start_date, end_date, reporting_group)

    @classmethod
    def from_file_handle(cls, file_handle):
        return set([cls.from_xml_element(podling_element) for podling_element in etree.parse(file_handle).getroot()])


PODLINGS = None


def get_podlings():
    global PODLINGS
    if not PODLINGS:
        podlings = {}
        for podling in Podling.from_file_handle(Resource(PODLING_URI).get().body_stream()):
            podlings[podling.name] = podling
        PODLINGS = podlings

    return PODLINGS


def incubating(podlings):
    return set([podling for podling in podlings if podling.status == 'current'])


def graduated(podlings):
    return set([podling for podling in podlings if podling.status == 'graduated'])


def retired(podlings):
    return set([podling for podling in podlings if podling.status == 'retired'])


def _date_from_string(string):
    try:
        return datetime.strptime(string, '%Y-%m-%d').date()
    except ValueError:
        return datetime.strptime(string, '%Y-%m').date()
