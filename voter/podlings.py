# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
Purpose: Parses the Incubator podling status files to find the list of
         development mailing list archive files.

Status: Alpha
'''

from __future__ import absolute_import

import os, sys
import collections
import traceback
import xml.etree.ElementTree

sys.path.insert(0, os.path.dirname(__file__))
from utility import Issue, SiteStructure, UTC

Podling = collections.namedtuple('Podling', ('name', 'mbox_relpath'))

class Issues(object):
    ERROR = 'ERROR'
    WARNING = 'WARNING'

    def __init__(self):
        self.__issues = []

    def __exfmt(self):
        return ''.join(traceback.format_exception_only(*sys.exc_info()[:2]))

    def __writelast(self):
        issue = self.__issues[-1]
        if issue.kind:
            sys.stderr.write('%s: %s\n' % issue)
        else:
            sys.stderr.write(issue.message)

    @property
    def issues(self):
        return self.__issues[:]

    def record_warning(self, message):
        self.__issues.append(Issue(self.WARNING, message))
        self.__writelast()

    def record_error(self, message):
        self.__issues.append(Issue(self.ERROR, message))
        self.__writelast()

    def record_exception(self, message):
        self.record_error(message)
        self.__issues.append(Issue(None, self.__exfmt()))
        self.__writelast()
__issues = Issues()


def __parse_xml_file(path):
    """
    Parse an XML file and suppress any encountered errors.
    """

    try:
        return xml.etree.ElementTree.parse(path)
    except:
        __issues.record_exception('Could not parse ' + path)
        return None

def __find_podling_names():
    """
    Find names of currently active podlings.
    """

    doc = __parse_xml_file(SiteStructure.podlings())
    if not doc:
        return None

    names = []
    for info in doc.iterfind('podling'):
        if info.get('status') != 'current':
            continue
        name = info.get('resource')
        if name is None:
            continue
        names.append(name)
    return names

__incubator = 'incubator.apache.org'
def __relpath_from_email(email):
    """
    Convert a list email address to an archive relative path.
    """

    email = email.strip()

    # Some podlings are silly and add crud to the mailing list address
    offset = email.find(__incubator)
    if offset < 0:
        __issues.record_warning('Not an Incubator address: ' + email)
        return None
    if email[offset + len(__incubator):]:
        __issues.record_warning('Ignoring crud following address: ' + email)
    email = email[:offset + len(__incubator)]

    # Split the email into list name and host name
    list_name, atsign, host = email.partition('@')
    if not atsign or not host:
        __issues.record_warning('Invalid mail address: ' + email)
        return None

    # Old-style podling lists are inside the incubator archives.
    # The mailing list address is podling-list@incubator.apache.org
    if host == __incubator:
        return os.path.join(__incubator, list_name)

    # New-style podling lists have their own archive directory.
    # The mailing list address is list@podling.incubator.apache.org
    basedir = host[:len(host) - len(__incubator)] + 'apache.org'
    return os.path.join(basedir, list_name)

def podling_archives():
    try:
        podlings = []
        for name in __find_podling_names():
            doc = __parse_xml_file(SiteStructure.project_path(name + '.xml'))
            if not doc:
                continue
            info = doc.find('.//*[@id="mail-dev"]')
            if info is None:
                __issues.record_warning(name + ' has no dev list?')
                continue
            email = ''
            for el in info.iter():
                email += (el.text or '')
            podlings.append(Podling(name, __relpath_from_email(email)))
        return podlings, __issues
    except:
        __issues.record_exception('Could not find any podlings')
        return [], __issues


def test():
    podlings, issues = podling_archives()
    for p in podlings:
        print('%25s %s' % (p.name + ' dev list:', p.mbox_relpath))
