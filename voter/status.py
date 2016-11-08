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
Purpose: generates an HTML with the status of current incubator
         votes, using data from the votes database.

Status: Alpha
'''

from __future__ import absolute_import

import os, sys
import cgi
import datetime

sys.path.insert(0, os.path.dirname(__file__))
from utility import SiteStructure, UTC
from voter import VoteDatabase


class __Template(object):
    def __init__(self, page,
                 current_table, current_row,
                 closed_table, closed_row,
                 issues_table, issues_row):
        self.page = page
        self.current_table = current_table
        self.current_row = current_row
        self.closed_table = closed_table
        self.closed_row = closed_row
        self.issues_table = issues_table
        self.issues_row = issues_row


__standalone = __Template(
    page = """\
<!DOCTYPE html>
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Apache Incubator Voting Status</title>
  <style type="text/css">
  <!--
  .normal {}
  .nudge  { background-color: #f0e442; }
  .nag    { background-color: #e69f00; }
  .yell   { background-color: #d55e00; font-weight: bold; }

  body    { color: black;
            background-color: white;
            font-family: Helvetica, Arial, sans-serif; }
  table   { white-space: pre;
            border: 1px solid #707070;
            border-collapse: collapse; }
  th      { background-color: #cccccc; }
  th, td  { padding: 4pt 0.5em 4pt 0.5em;
            border: 1px solid #333333; }
  -->
  </style>
</head>
<body>
  <h1>Apache Incubator Voting Status</h1>
  <p style="whitespace: pre">Last recorded change: %(lastchange)s</p>
  <p>
    Legend:
    The <span class="nag">orange</span> items indicate where more care
    and attention is needed. Anything <span class="yell">vermilion</span>
    is an issue that should be addressed ASAP.
    The <span class="nudge">yellow</span> items are in process.
    Please precede email Subject with a "[VOTE]" label,
    and prepend "[RESULT]" for the final tally (as
    <a href="http://incubator.apache.org/facilities.html#voting-status">explained</a>).
  </p>
%(current)s
%(closed)s
%(issues)s
</body>
</html>
""",
    current_table = """\
  <h2>Current Votes</h2>
  <table>
    <tr>
     <th>Subject</th>
     <th>Activity</th>
     <th>Started</th>
     <th>Age</th>
    </tr>
%s
  </table>""",
    current_row = """\
    <tr class="%(klass)s">
      <td>%(subject)s</td>
      <td>%(updated)s</td>
      <td>%(noticed)s</td>
      <td>%(duration)s</td>
    </tr>""",
    closed_table = """\
  <h2>Recently Closed Votes</h2>
  <table>
    <tr>
     <th>Status</th>
     <th>Subject</th>
     <th>Started</th>
     <th>Closed</th>
    </tr>
%s
  </table>""",
    closed_row = """\
    <tr class="%(klass)s">
      <td>%(status)s</td>
      <td>%(subject)s</td>
      <td>%(noticed)s</td>
      <td>%(closed)s</td>
    </tr>""",
    issues_table = """\
  <h2>Issues</h2>
  <p>Problems encountered during vote status page generation:</p>
  <table>
    <tr>
      <th>Severity</th>
      <th>Description</th>
    </tr>
%s
  </table>""",
    issues_row = """\
  <tr class="%(klass)s">
    <td>%(kind)s</td>
    <td>%(message)s</td>
  </tr>""")

__embedded = __Template(
    page = """\
<!DOCTYPE html>
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.
-->
<html lang="en">
<body>
  <div id="voter" class="section-content">
    <p style="whitespace: pre">Last recorded change: %(lastchange)s</p>
%(current)s
%(closed)s
%(issues)s
  </div>
</body>
</html>
""",
    current_table = """\
    <h3 id="Current+Votes">Current Votes</h3>
    <div class="section-content">
      <table class="colortable" width="100%%">
        <tr>
          <th>Subject</th>
          <th>Activity</th>
          <th>Started</th>
          <th>Age</th>
        </tr>
%s
      </table>
    </div>""",
    current_row = """\
        <tr class="%(klass)s">
          <td>%(subject)s</td>
          <td>%(updated)s</td>
          <td>%(noticed)s</td>
          <td>%(duration)s</td>
        </tr>""",
    closed_table = """\
    <h3 id="Recently+Closed+Votes">Recently Closed Votes</h3>
    <div class="section-content">
      <table class="colortable" width="100%%">
        <tr>
          <th>Status</th>
          <th>Subject</th>
          <th>Started</th>
          <th>Closed</th>
        </tr>
%s
      </table>
    </div>""",
    closed_row = """\
        <tr class="%(klass)s">
          <td>%(status)s</td>
          <td>%(subject)s</td>
          <td>%(noticed)s</td>
          <td>%(closed)s</td>
        </tr>""",
    issues_table = """\
    <h3 id="Problems+Found">Issues</h3>
    <div class="section-content">
      <p>Problems encountered during vote status page generation:</p>
      <table class="colortable" width="100%%">
        <tr>
          <th>Severity</th>
          <th>Description</th>
        </tr>
%s
      </table>
    </div>""",
    issues_row = """\
        <tr class="%(klass)s">
          <td>%(kind)s</td>
          <td>%(message)s</td>
        </tr>""")


def escape_date(dateobject):
  return cgi.escape(UTC.timedate(dateobject)).replace('-', '&ndash;')

def refresh_page(template, target, database):
    current = []
    now = datetime.datetime.utcnow()
    for vote in database.list_open_votes():
        age = now - vote.noticed
        if age < datetime.timedelta(hours = 49):
            klass = 'normal'
        elif age < datetime.timedelta(hours = 73):
            klass = 'nudge'
        elif age < datetime.timedelta(days = 7):
            klass = 'nag'
        else:
            klass = 'yell'

        if age < datetime.timedelta(hours = 72):
           hours = int((age.total_seconds() + 1800) // 3600)
           if hours == 1:
               duration = 'one hour'
           else:
               duration = '%d hours' % hours
        else:
           days = int((age.total_seconds() + 43200) // 86400)
           duration = '%d days' % days


        current.append(template.current_row
                       % dict(klass = klass,
                              duration = duration,
                              subject = cgi.escape(vote.subject),
                              updated = escape_date(vote.updated),
                              noticed = escape_date(vote.noticed)))
    if current:
        current = template.current_table % '\n'.join(current)
    else:
        current = ''

    resolved = []
    for vote in database.list_resolved_votes():
        klass = vote.cancelled and 'nudge' or 'normal'
        status = vote.cancelled and 'Cancelled' or 'Resolved'
        resolved.append(template.closed_row
                        % dict(klass = klass,
                               status = status,
                               subject = cgi.escape(vote.subject),
                               noticed = escape_date(vote.noticed),
                               closed = escape_date(vote.closed)))
    if resolved:
        resolved = template.closed_table % '\n'.join(resolved)
    else:
        resolved = ''

    issues = []
    for kind, message in database.list_issues():
      if kind is None:
        kind = '&nbsp;'
        klass = 'normal'
      elif kind == 'WARNING':
        klass = 'nag'
      else:
        klass = 'yell'
      issues.append(template.issues_row
                    % dict(klass = klass,
                           kind = kind,
                           message = cgi.escape(message)))
    if issues:
      issues = template.issues_table % '\n'.join(issues)
    else:
      issues = ''

    updated = cgi.escape(UTC.timestring(database.updated)).replace('-', '&ndash;')
    temp = target + '.temp'
    with open(temp, 'wt') as page:
        page.write(template.page % dict(lastchange = updated,
                                        current = current,
                                        closed = resolved,
                                        issues = issues))
    os.rename(temp, target)


def main():
    votes_path = SiteStructure.votes_database()
    status_page = SiteStructure.standalone_status_page()
    status_template = SiteStructure.status_page_template()
    refresh_page(__standalone, status_page, VoteDatabase(votes_path))
    refresh_page(__embedded, status_template, VoteDatabase(votes_path))

if __name__ == '__main__':
    main()
