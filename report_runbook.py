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
Print out steps for a "Report Manager" to execute when preparing the
Incubator's monthly report to the ASF Board of Directors.
"""

import sys
if sys.version_info < (3, 2):
    raise Exception("Python 3.2 or above is required")

import argparse
import datetime
import calendar

from report_timeline import Timeline

def header(options):
    return strip_indent("""
        ##################################################################
        # This doc is meant to be a guide to preparing the incubator
        # report for a given month.  Each section has a heading, starting
        # with mechanical, editorial, or Chair.  If you have volunteered
        # to perform any of these actions, please pay attention to
        # those sections.
        ##################################################################
    """)

def timeline_email(options):
    timeline = Timeline(month=options['month']).to_email()
    return strip_indent("""
        ##################################################################
        # mechanical -- Send report timeline email.
        #
        # On the last Wednesday of the month, send an email to
        # general@incubator announcing the report timeline, using the
        # following content.
        ##################################################################
        {timeline}
        """).format(timeline=timeline, **options)

def assemble_release_list(options):
    month = ((options['month'] + 10) % 12) + 1
    year = options['year'] if month != 12 else options['year'] - 1
    date = datetime.date(day=1, month=month, year=year)
    found = calendar.monthrange(year, month)
    end = date + datetime.timedelta(days=found[1])
    template = "{{{date:%Y}-{date:%m}-{date:%d}}}:{{{end:%Y}-{end:%m}-{end:%d}}}"
    date_spec = template.format(date=date, end=end)
    return strip_indent("""
        ##################################################################
        # editorial  -- Assemble list of releases.
        #
        # The Board report must contain a list of releases by the
        # Incubator project during the reporting period.  This can be
        # assembled manually from the history of our dist area.
        #
        # The date of each release is the date it appeared in our dist
        # area.  We provide a list of all releases that entered
        # distribution during the previous month.
        ##################################################################

        # History of our dist area during the reporting month.
        svn log -v -r {0} https://dist.apache.org/repos/dist/release/incubator
        """.format(date_spec))

def summarize_podling_reports(options):
    return strip_indent("""
        ##################################################################
        # editorial  -- Create podling summary.
        #
        # After the podling reporting deadline has passed, group
        # podlings into the following categories (additional categories
        # may be added if appropriate):
        #
        # * Still getting started at the Incubator
        # * Not yet ready to graduate
        #   * No release
        #   * Community growth
        # * Ready to graduate
        # * Did not report, expected next month
        #
        ##################################################################

        # For any podlings that did not report, add a "monthly" attribute
        # in podlings.xml.  See http://s.apache.org/At0 for a sample commit.
        # mechanical -- Assign podlings which do not report to "monthly".
        [... edit podlings.xml with your editor of choice ...]
        svn ci -m "Assign podlings which did not report to 'monthly'."

        ##################################################################
        # editorial  -- Write narrative, misc, legal, infrastructure, etc.
        #    sections.
        #
        # After the podlings are compiled, please add the various sections
        # listed above.  To do this, visit the incubator mail archives for
        # the preceeding month and review any actions performed.  Were
        # there any code donations? Podlings renamed?  Unexpected outages?
        ##################################################################
        """)

def normalize_formatting(options):
    return strip_indent("""
        ##################################################################
        # mechanical -- Normalize report formatting
        #
        # Normalize the formatting of the podling reports and shepherd
        # reviews.  Remove any blank entries.
        #
        # The report will ultimately be published as part of the Board
        # minutes in monospaced plain text.  Here's a style guide:
        #
        # * Wrap text at 76 characters.
        # * Normalize indentation.  For all podling reports, questions are
        #   flush left, answers indented two spaces.
        * * No more than one blank line anywhere.
        # * All URLs which would cause lines to exceed 76 characters
        #   should be shortened using <http://s.apache.org>.
        ##################################################################
        """)

def send_draft_to_general(options):
    return strip_indent("""
        ##################################################################
        # mechanical -- Send "shepherding" email.
        #
        # Once the deadline has passed for the editorial and shepherding
        # tasks, a draft of the report should be sent to
        # general@incubator for review.
        #
        # It is important to send this email in a timely manner so that
        # there is an adequate window for review.  If the report is
        # incomplete, send out the draft anyway.
        # 
        # Suggested subject:
        #
        #    Draft Report {date:%B} {date:%Y} - please review
        #
        ##################################################################
        """).format(**options)

def file_report(options):
    return strip_indent("""
        ##################################################################
        # Chair      -- Deliver report to Board.
        #
        # On the day that the report is due to be submitted to the Board,
        # no action by the Report Manager is required.
        #
        # The IPMC Chair will perform a final review for completeness and
        # consistency, mark the wiki page as final, then file the report.
        ##################################################################
        """).format(**options)

def prep_next_wiki_report_template(options):
    next_month = (options['month'] % 12) + 1
    return strip_indent("""
        ##################################################################
        # mechanical -- Prepare next month's report template.
        #
        # Prepare next month's wiki report template.
        ##################################################################

        # Edit podlings.xml: remove the "monthly" attribute for podlings
        # where it has expired.  Commit any changes.
        [... edit podlings.xml with your editor of choice ...]
        svn ci -m "Remove expired 'monthly' attributes."

        # Run clutch, regenerate the website, commit and publish
        python3 clutch.py
        svn ci -m "Run clutch."
	login to CMS and publish the Incubator website.

        # Assign shepherds.
        python3 assign_shepherds.py --month={next_month}
        svn ci -m "Assign shepherds."

        # Generate report template and publish on the wiki.
        python3 clutch2report.py --month={next_month} --upload
        """).format(next_month=next_month, **options)

def strip_indent(text):
    # Fragile hack, but good enough for this simple script.
    return text.replace("\n        ", "\n")

def process_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apache-id', type=str, required=True)
    parser.add_argument('--month', type=int, required=True, help="1-12")
    options = vars(parser.parse_args())
    now = datetime.datetime.now()
    if options['month'] >= now.month:
        options['year'] = now.year
    else:
        options['year'] = now.year + 1
    for day in range(15, 22):
        date = datetime.date(day=day, month=options['month'],
                             year=options['year'])
        if date.weekday() == 2:
            options['date'] = date
            break
    return options

def main():
    options = process_cli_args()
    text = ""
    text += header(options)
    text += timeline_email(options)
    text += summarize_podling_reports(options)
    text += assemble_release_list(options)
    text += normalize_formatting(options)
    text += send_draft_to_general(options)
    text += file_report(options)
    text += prep_next_wiki_report_template(options)
    print(text)

if __name__ == '__main__':
    main()

