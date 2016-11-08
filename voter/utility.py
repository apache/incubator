#!/usr/bin/env python

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
Purpose: Utilities for Voter & friends.

Status: Alpha
'''

from __future__ import absolute_import

import os.path
import collections
import datetime


Issue = collections.namedtuple('Issue', ('kind', 'message'))

class __UTC(datetime.tzinfo):
    """
    A datetime.tzinfo object representing Universal Coordinated Time
    and providing a set of parsing and formatting utilities.
    """

    def utcoffset(self, dt):
        return 0;
    def dst(self, dt):
        return timedelta(0)
    def tzname(self,dt):
        return 'UTC'

    def adjust(self, dateobject):
        if dateobject.tzinfo:
            dateobject = dateobject.astimezone(self)
        return dateobject

    def timestring(self, dateobject):
        if dateobject is not None:
            return self.adjust(dateobject).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def timedate(self, dateobject):
        if dateobject is not None:
            return self.adjust(dateobject).strftime('%Y-%m-%d')
        return None

    def timeparse(self, datestring):
        if datestring is not None:
            return datetime.datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
        return None
UTC = __UTC()


class SiteStructure(object):
    """
    This class describes the structure of the Incubator site and tells
    other modules where to find information and/or store results.
    """

    INCUVOTER_DIR = os.path.abspath(os.path.dirname(__file__))
    CONTENT_DIR = os.path.join(os.path.dirname(INCUVOTER_DIR), 'content')
    PROJECTS_DIR = os.path.join(CONTENT_DIR, 'projects')

    @classmethod
    def incuvoter_path(cls, *relpath):
        return os.path.join(cls.INCUVOTER_DIR, *relpath)

    @classmethod
    def content_path(cls, *relpath):
        return os.path.join(cls.CONTENT_DIR, *relpath)

    @classmethod
    def project_path(cls, *relpath):
        return os.path.join(cls.PROJECTS_DIR, *relpath)

    @classmethod
    def votes_database(cls):
        return cls.incuvoter_path('votes.sqlite')

    @classmethod
    def standalone_status_page(cls):
        return cls.incuvoter_path('votes.html')

    @classmethod
    def status_page_template(cls):
        return cls.incuvoter_path('embedded-votes.html')

    @classmethod
    def podlings(cls):
        return cls.content_path('podlings.xml')

