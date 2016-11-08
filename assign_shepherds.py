#!/usr/bin/env python3

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

"""
Assign shepherds to podlings for an upcoming report cycle.

This script can only be run from a checkout of the Incubator's Subversion
repository.  Assignments are written out to
`content/shepherd_assignments.json`; once this script has been run, the
modified file must be committed.

The roster of active shepherds is maintained in the file
`content/shepherds.json`.

Rules by which shepherds are assigned:

*   Shepherds must not be Mentors for the podling.
*   Shepherds will be assigned a maximum of 3 podlings per cycle, or fewer if
    they choose.  If there are not enough shepherds to meet demand, some
    podlings will not receive shepherd assignments.
*   If possible, no shepherd should be assigned the same podling multiple
    times over the course of incubation.
*   Shepherds may specify a whitelist of podlings which they will accept.

"""

import sys
if sys.version_info < (3, 2):
    raise Exception("Python 3.2 or above is required")

import os
import re
import json
import pickle
import random
import datetime
import argparse
import xml.dom.minidom
from pprint import pprint

class Shepherd(object):
    """An Incubator Shepherd."""

    def __init__(self, apache_id, name=None, max_podlings=3, whitelist=None):
        """
        Return a Shepherd instance.

        *   apache_id -- The Shepherd's apache id.
        *   max_podlings -- Maximum podlings to review per month.
        *   whitelist -- An optional list of acceptable podling IDs.
        """
        self._apache_id = apache_id
        self._max_podlings = int(max_podlings)
        self._name = name
        self._whitelist = set(whitelist) if whitelist else None
        self._assignments = {}

    def accept(self, date, podling_id):
        """Indicate whether the proposed assignment is acceptable."""
        return self._do_accept(date, podling_id, throw=False)

    def _do_accept(self, date, podling_id, throw):
        # If this shepherd has a whitelist, ensure that the podling is in it.
        if self._whitelist:
            if podling_id not in self._whitelist:
                if throw:
                    raise ValueError("Podling not in whitelist")
                return False

        # Ensure that the shepherd has capacity to accept an assignment.
        count = 0
        if date in self._assignments:
            count = len(self._assignments[date])
        if count >= self._max_podlings:
            if throw:
                raise ValueError("Too many podling assignments this month")
            return False
        return True

    def assign(self, date, podling_id):
        """
        Attempt to assign a podling to the Shepherd for a specific report
        date.  Throw an exception if the assignment is not acceptable.
        """
        self._do_accept(date=date, podling_id=podling_id, throw=True)
        self.force_assign(date, podling_id)

    def force_assign(self, date, podling_id):
        """Assign a podling to the shepherd.  Always succeeds."""
        if date not in self._assignments:
            self._assignments[date] = set()
        self._assignments[date].add(podling_id)

    def podling_count(self, date):
        """
        Return the number of podlings that the Shepherd has been assigned
        for the given report date.
        """
        if date in self._assignments:
            return len(self._assignments[date])
        return 0

    def has_tended(self, podling_id):
        """
        Indicate whether the shepherd has ever been assigned the specified
        podling.
        """
        for past in self._assignments:
            if podling_id in past:
                return True
        return False

    def whitelisted(self, podling_id):
        """
        Indicate whether the shepherd is willing to accept the specified
        podling.
        """
        return self._whitelist and podling_id in self._whitelist

    def get_apache_id(self):
        return self._apache_id

    def get_max_podlings(self):
        return self._max_podlings

    @staticmethod
    def bulk_load(f):
        """
        Parse a JSON file stream and returns a dict of (apache_id: Shepherd)
        pairs.
        """
        data = json.load(f)
        shepherds = {}
        for args in data:
            shepherd = Shepherd(**args)
            shepherds[shepherd.get_apache_id()] = shepherd
        return shepherds

class Report(object):
    """An Incubator report to the ASF Board of Directors for a given date."""

    def __init__(self, date):
        """
        Return a Report instance.

        *   date -- A string of the format `YYYY-MM`.
        """
        if not re.match("\\d{4}-\\d{2}", date):
            raise ValueError("Invalid date")
        self._date = date
        self._month = int(date[5:])
        self._assignments = {}

    def get_date(self):
        return self._date

    def assign(self, podling_id, shepherd):
        """Attempt to assign a podling to the specified shepherd."""
        if shepherd is not None and not isinstance(shepherd, Shepherd):
            raise TypeError("Not a Shepherd")
        if podling_id in self._assignments:
            raise ValueError("Podling " + podling_id + " already assigned")
        self._assignments[podling_id] = shepherd
        
    def shepherd(self, podling_id):
        """Return the Shepherd assigned to `podling_id`, if any."""
        if podling_id in self._assignments:
            return self._assignments[podling_id]
        return None

    def podlings(self):
        """Return the podlings reporting this cycle as a `set` of IDs"""
        return set(self._assignments.keys())

    def _select_shepherd(self, podling, shepherds):
        # Exclude mentors and inactive shepherds.
        shep_list = []
        for shep in shepherds.values():
            if shep.get_max_podlings():
                if not podling.has_mentor(shep.get_apache_id()):
                    shep_list.append(shep)

        # Try to distribute podlings evenly amongst the shepherds.
        random.shuffle(shep_list)
        shep_list.sort(key = lambda shep: shep.podling_count(self._date))

        # First, try to assign the podling to someone who's got it whitelisted.
        for shep in shep_list:
            if shep.whitelisted(podling.get_id()):
                if shep.accept(podling_id=podling.get_id(), date=self._date):
                    return shep

        # Try to assign the podling to someone who hasn't shepherded it before.
        for shep in shep_list:
            if shep.has_tended(podling.get_id()):
                continue
            if shep.accept(podling_id=podling.get_id(), date=self._date):
                return shep

        # Find someone who's got the time.
        for shep in shep_list:
            if shep.accept(podling_id=podling.get_id(), date=self._date):
                return shep

        # Nobody's available.
        return None

    def assign_shepherds(self, podlings, shepherds, reports):
        """
        Assign shepherds to this report.

        *   podlings -- a dict of (podling_id: Podling) pairs.
        *   shepherds -- a dict of (apache_id: Shepherd) pairs.
        *   reports -- a dict of ("YYYY-MM": Report) pairs.
        """
        shuffled = list(podlings.values())
        random.shuffle(shuffled)
        for podling in shuffled:
            if podling.report_due(self._month):
                shep = self._select_shepherd(podling, shepherds)
                if shep is not None:
                    shep.assign(date=self._date, podling_id=podling.get_id())
                self.assign(podling_id=podling.get_id(), shepherd=shep)

    @staticmethod
    def bulk_load(shepherds, f):
        """
        Parse a JSON file stream and return a dict of ("YYYY-MM": Report)
        pairs.

        As a side effect, update `shepherds` by assigning podlings from past
        reports.

        *   shepherds: A dict of (apache_id: Shepherd) pairs.
        *   f: A readable file stream.
        """
        data = json.load(f)
        reports = {}
        for date in data:
            report = reports[date] = Report(date=date)
            for podling_id, shepherd_id in data[date].items():
                if shepherd_id and shepherd_id not in shepherds:
                    # Add past shepherds to roster, but indicate that they are
                    # inactive by giving them max_podlings=0.
                    shep = Shepherd(apache_id=shepherd_id, max_podlings=0)
                    shepherds[shepherd_id] = shep
                shepherd = shepherds[shepherd_id] if shepherd_id else None
                report.assign(podling_id=podling_id, shepherd=shepherd)
                if shepherd:
                    shepherd.force_assign(date=date, podling_id=podling_id)
        return reports

    @staticmethod
    def bulk_dump(reports, f):
        """
        Write out a dict of ("YYYY-MM": Report) pairs to a JSON file stream,
        capturing shepherd assignments.
        """
        data = {}
        for date, report in reports.items():
            assigned = {}
            data[report.get_date()] = assigned
            for podling_id in report.podlings():
                shepherd = report.shepherd(podling_id)
                apache_id = shepherd.get_apache_id() if shepherd else None
                assigned[podling_id] = apache_id
        json.dump(data, f, indent=4, sort_keys=True, separators=(",", ": "))

class Podling(object):
    """An Incubator podling."""

    def __init__(self, podling_id, group, monthly):
        """
        Return a Podling instance.

        *   podling_id -- The resource identifier for the podling.
        *   group -- Reporting group (1, 2 or 3).
        *   monthly -- Whether podling currently reports monthly.
        """
        self._id = podling_id 
        self._monthly = monthly
        self._group = group
        self._mentors = set()

    def add_mentor(self, mentor):
        """Add a mentor to the podling."""
        self._mentors.add(mentor)

    def has_mentor(self, apache_id):
        """Indicate whether `apache_id` mentors the podling."""
        return apache_id in self._mentors

    def get_id(self):
        """Return the podlings string resource identifier."""
        return self._id

    def report_due(self, month):
        """
        Indicate whether the podling will have a report due during the
        specified month.
        """
        if self._monthly:
            return True
        if (((month - 1) % 3) + 1) == self._group:
            return True
        return False

    @staticmethod
    def bulk_load(f):
        """
        Parse a podlings.xml file stream and return a dict of
        (podling_id: Podling) pairs.
        """
        podlings = {}
        dom = xml.dom.minidom.parse(f)
        for row in dom.getElementsByTagName("podling"):
            if row.getAttribute("status") != 'current':
                continue
            podling_id = row.getAttribute("name").strip()
            podling_id = podling_id.lower()
            podling_id = podling_id.replace(' ', '')
            reporting = row.getElementsByTagName("reporting")
            if not reporting:
                raise Exception(
                    "podlings.xml is missing 'reporting' for " + podling_id
                )
            monthly = True if reporting[0].getAttribute("monthly") else False
            group = int(reporting[0].getAttribute("group"))
            podling = Podling(podling_id=podling_id, monthly=monthly,
                              group=group)
            podlings[podling_id] = podling
            for mentor_data in row.getElementsByTagName("mentor"):
                mentor_name = mentor_data.getAttribute("username").strip()
                podling.add_mentor(mentor_name)
        return podlings

def repos_root():
    """Return the root dir of the Incubator version control checkout."""
    return os.path.dirname(os.path.abspath(__file__))

def main():
    # Process arguments and load data.
    options = process_cli_args()
    content_dir = os.path.join(repos_root(), 'content')
    podlings_xml_path = os.path.join(content_dir, 'podlings.xml')
    shepherds_path = os.path.join(content_dir, 'shepherds.json')
    assignments_path = os.path.join(content_dir, 'shepherd_assignments.json')
    with open(podlings_xml_path, 'r') as f:
        podlings = Podling.bulk_load(f=f)
    with open(shepherds_path, 'r') as f:
        shepherds = Shepherd.bulk_load(f=f)
    with open(assignments_path, 'r') as f:
        reports = Report.bulk_load(shepherds=shepherds, f=f)

    # See whether the assignments have already been made for the given month.
    if options.date in reports:
        print("Assignments for {} already complete.".format(options.date))
        sys.exit(0)

    # Perform assignments and dump to `content/shepherds_assignments.json`.
    report = reports[options.date] = Report(date=options.date)
    report.assign_shepherds(podlings=podlings,
                            shepherds=shepherds,
                            reports=reports)
    os.remove(assignments_path)
    with open(assignments_path, 'w') as f:
        Report.bulk_dump(reports=reports, f=f)
    print("Updated {}".format(assignments_path))

def process_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', type=int, default=0,
                        help="month number (1-12)")
    options = parser.parse_args()
    now = datetime.datetime.now()
    if options.month == 0:
        options.month = (now.month % 12) + 1
    if options.month < now.month:
        options.year = now.year + 1
    else:
        options.year = now.year
    options.date = "{0:04d}-{1:02d}".format(options.year, options.month)
    return options

if __name__ == '__main__':
    main()
