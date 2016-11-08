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

import sys
if sys.version_info < (3, 2): 
        raise Exception("Python 3.2 or above is required")

import datetime
import argparse

class Timeline(object):
    """Timeline of events associated with an Incubator Board report."""

    def __init__(self, month):
        self._month = month
        now = datetime.datetime.now()
        self._year = now.year if month >= now.month else now.year + 1
        for day in range(1, 8):
            first_wed = datetime.date(day=day, month=self._month,
                                      year=self._year)
            if first_wed.weekday() == 2:
                break
        self._events = []
        self._date = first_wed.replace(day=first_wed.day + 14)
        self._add_event(desc="Podling reports due by end of day",
                        date=first_wed)
        self._add_event(desc="Shepherd reviews due by end of day",
                        date=first_wed.replace(day=first_wed.day + 4))
        self._add_event(desc="Summary due by end of day",
                        date=first_wed.replace(day=first_wed.day + 4))
        self._add_event(desc="Mentor signoff due by end of day",
                        date=first_wed.replace(day=first_wed.day + 6))
        self._add_event(desc="Report submitted to Board",
                        date=first_wed.replace(day=first_wed.day + 7))
        self._add_event(desc="Board meeting",
                        date=first_wed.replace(day=first_wed.day + 14))

    def _add_event(self, desc, date):
        self._events.append({"desc": desc, "date": date})

    def to_moin(self):
        """Represent the timeline as a table in MoinMoin wiki syntax."""
        moin = ""
        for event in self._events:
            moin += '||{0:%a} {0:%B} {0:%d} ||{1} ||\n'.format(event['date'],
                                                               event['desc'])
        return moin

    def to_email(self):
        """Represent the timeline as plain text email content."""
        template = """
            {date:%B} {date:%Y} Incubator report timeline:

                http://wiki.apache.org/incubator/{date:%B}{date:%Y}

            """.replace("\n            ", "\n")
        text = template.format(date=self._date)
        for event in self._events:
            text += '    {0:%a} {0:%B} {0:%d} -- {1}\n'.format(event['date'],
                                                               event['desc'])
        return text

def process_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--month', type=int, default=0,
                        help="month number (1-12)")
    options = parser.parse_args()
    if options.month == 0:
        now = datetime.datetime.now()
        options.month = (now.month % 12) + 1
    return options

def main():
    options = process_cli_args()
    timeline = Timeline(month=options.month)
    print(timeline.to_email())

if __name__ == '__main__':
    main()

