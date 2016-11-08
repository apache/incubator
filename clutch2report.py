import sys
if sys.version_info < (3, 2):
    raise Exception("Python 3.2 or above is required")

import pickle
import pprint
from string import Template
import datetime
import getpass
import argparse
import textwrap
import calendar
import xmlrpc
import xmlrpc.client
import json
import os

from report_timeline import Timeline

'''
'clutch2report' reads the pickle file which was created by 'clutch' and generates
a shell for a monthly report for the incubator.
'''

months2groups = [ 'group-1', 'group-2', 'group-3', 
                  'group-1', 'group-2', 'group-3',
                  'group-1', 'group-2', 'group-3',
                  'group-1', 'group-2', 'group-3']

boilerplate = """
= Incubator PMC report for {month} {year} =

=== Timeline ===
{timeline}

=== Shepherd Assignments ===
{shepherds}

=== Report content ===
{{{{{{
Incubator PMC report for {month} {year}

The Apache Incubator is the entry path into the ASF for projects and
codebases wishing to become part of the Foundation's efforts.

< narrative >

* Community

  New IPMC members:



  People who left the IPMC:



* New Podlings



* Graduations

  The board has motions for the following:



* Releases

  The following releases entered distribution during the month of
  {last_month}:


* IP Clearance



* Legal / Trademarks



* Infrastructure



* Miscellaneous



* Credits

  - Report Manager:

-------------------- Summary of podling reports --------------------

* Still getting started at the Incubator



* Not yet ready to graduate

  No release:



  Community growth:



* Ready to graduate

  The Board has motions for the following:



* Did not report, expected next month



----------------------------------------------------------------------
                       Table of Contents
{toc}
----------------------------------------------------------------------
"""

perproject = """
--------------------
$name

$description

$name has been incubating since $start.

Three most important issues to address in the move towards graduation:

  1.
  2.
  3.

Any issues that the Incubator PMC (IPMC) or ASF Board wish/need to be
aware of?



How has the community developed since the last report?



How has the project developed since the last report?



Date of last release:

  XXXX-XX-XX

When were the last committers or PMC members elected?



Signed-off-by:

  $mentorlist

Shepherd/Mentor notes:


"""

def push(pagename, reportFile):
    print("Publishing " + pagename)
    name = input("Username for wiki.apache.org/incubator: ")
    password = getpass.getpass("Password for wiki.apache.org/incubator: ")
    report = open(reportFile, 'r')
    reportcontent = report.read(-1)
    report.close()
    srcwiki = xmlrpc.client.ServerProxy("http://wiki.apache.org/incubator/?action=xmlrpc2")
    token =  srcwiki.getAuthToken(name, password)
    
    pushresults = srcwiki.system.multicall([{'methodName':'applyAuthToken', 'params': [token]}, 
                                            {'methodName':'putPage', 'params': [pagename, reportcontent]}])
    print(pushresults)

def cliargs():
    parser = argparse.ArgumentParser(description='Create (and optionally push) a template for an incubator report.')
    parser.add_argument('--upload', action='store_true',
                        help='whether to upload the report template.')
    parser.add_argument('--month', type=int, help='the month to report for, defaults to current month.', default=0)
    return parser.parse_args()  # note that this exits on errors.

def gen_shepherd_assignments(projects, month, year):
    # Load the shepherd assignments data for this month's report.
    now = datetime.datetime.now()
    date = "{0:04d}-{1:02d}".format(year, month)
    assignments_path = os.path.join("content", "shepherd_assignments.json")
    with open(assignments_path, "r") as f:
        assignments_data = json.load(f)
    if date not in assignments_data:
        print("Shepherds have not yet been assigned for {}.".format(date))
        print("Please run `assign_shepherds.py --month={}`".format(month))
        sys.exit(1)
    report = assignments_data[date]

    # Load the roster of active shepherds, which we'll use to get full names.
    shepherds_path = os.path.join("content", "shepherds.json")
    with open(shepherds_path, "r") as f:
        shepherds_data = json.load(f)
    shepherds = {}
    for shepherd in shepherds_data:
        shepherds[shepherd['apache_id']] = shepherd

    # Generate and return the wikified list of assignments.
    lines = []
    for podling_id, shepherd_id in report.items():
        podling_name = projects[podling_id]['fullName']
        shepherd_name = '[none]'
        if shepherd_id in shepherds:
            shepherd_name = shepherds[shepherd_id]['name']
        lines.append("||{} ||{} ||".format(shepherd_name, podling_name))
    lines.sort()
    return "\n".join(lines)

def main():
    options = cliargs()
    now = datetime.datetime.now()
    if options.month == 0:
        month = now.month + 1
    else:
        month = options.month
    last_month = ((now.month + 11) % 12) + 1
    year = now.year if month >= now.month else now.year + 1
    curGroup = months2groups[month - 1]
    inputFile = open('clutch.pkl', 'rb')
    projects = pickle.load(inputFile)
    inputFile.close()

    timeline  = Timeline(month).to_moin()
    shepherds = gen_shepherd_assignments(projects, month, year)

    output = open('report.txt', 'w')

    toc = ""
    for project in sorted(projects.keys()):
        pdata = projects[project]
        if pdata['rawReportingGroup'] == curGroup or pdata['reportingMonthly']:
            toc = toc + projects[project]['fullName'] + "\n"
         
    output.write(boilerplate.format(month=calendar.month_name[month],
                                    last_month=calendar.month_name[last_month],
                                    year=year, toc=toc, shepherds=shepherds,
                                    timeline=timeline))
    
    ptemplate = Template(perproject)
    
    for project in sorted(projects.keys()):
        pdata = projects[project]
        
        if pdata['rawReportingGroup'] == curGroup or pdata['reportingMonthly']:
            mentor_boxes = []
            for mentor in pdata['mentors']:
                mentor_box = "[ ]({0}) {1}".format(project, mentor)
                mentor_boxes.append(mentor_box)
            mentorlist = "\n  ".join(mentor_boxes)
            description = textwrap.fill(pdata['description'], 78)
            pdict = { 'name': pdata['fullName'], 
                      'description': description,
                      'start': pdata['startDate'],
                      'mentorlist' : mentorlist}
            output.write(ptemplate.substitute(pdict))

    # Close `Report Content` section.
    output.write("\n}}}\n")

    output.close()
    if options.upload:
        push("{0}{1}".format(calendar.month_name[month], year), 'report.txt')
    
if __name__ == "__main__":
    main()
