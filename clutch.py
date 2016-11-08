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
Purpose: Clutch gathers details about projects currently in incubation.

The core resource is the SITE_CONTENT/podlings.xml file. As soon as a project is
accepted into incubation, please add its entry. 
This script reads the SITE_CONTENT/podlings.xml table, and each podling status page, and
other resources. The assembled metadata is stored in various data files.

See further explanation at http://incubator.apache.org/clutch.html

Note: Please keep the dependencies as minimal as possible, so this script can
be operated by any Incubator committer. It uses only standard modules.

Note: The 'svn log' queries might only run on UNIX, YMMV.
'''

'''
External input data files used:
- SITE_CONTENT/podlings.xml

URLs
http://people.apache.org/~crossley/incubator-keys.txt

Created on minotaur using:
find /www/www.apache.org/dist/incubator \
  -iname "*KEYS*" | grep -v "\.svn\/" > ~/public_html/incubator-keys.txt

http://people.apache.org/~crossley/incubator-releases.txt

Created on minotaur using:
find /www/www.apache.org/dist/incubator \
  -iname "*incubat*gz.asc" -o -iname "*incubat*gz.sig" \
  -o -iname "*incubat*bz2.asc" -o -iname "*incubat*bz2.sig" \
  -o -iname "*incubat*zip.asc" -o -iname "*incubat*zip.sig" \
  > ~/public_html/incubator-releases.txt

http://people.apache.org/~crossley/incubator-releases-bad-filename.txt

Created on minotaur using:
find /www/www.apache.org/dist/incubator \
  -iname "*gz.asc" -o -iname "*gz.sig" \
  -o -iname "*bz2.asc" -o -iname "*bz2.sig" \
  -o -iname "*zip.asc" -o -iname "*zip.sig" \
  | sed 's/.*\/incubator\///' \
  | grep -v incubat \
  > ~/public_html/incubator-releases-bad-filename.txt

The above has now been replaced by parsing the output of
'svn', 'ls', '-R', 'https://dist.apache.org/repos/dist/release/incubator'

asf-authorization-template from Git deployment branch
http://mail-archives.apache.org/mod_mbox/
http://www.apache.org/dist/incubator/<resource>
http://svn.apache.org/repos/asf/incubator

SVN commands 
'svn', 'ls', '-R', 'https://dist.apache.org/repos/dist/release/incubator'
'svn', 'ls', '--xml', 'http://svn.apache.org/repos/asf/incubator/'
'svn', 'log', '--xml', 'SITE_CONTENT/projects/{0}.xml' {status file}

Output data files created:
SITE_CONTENT/clutch.txt
SITE_CONTENT/clutcho1.ent
SITE_CONTENT/clutcht.ent
SITE_CONTENT/clutchr1.ent
SITE_CONTENT/clutchr2.ent
SITE_CONTENT/clutcho2.ent
SITE_CONTENT/clutchm.ent
SITE_CONTENT/clutchmy.ent
SITE_CONTENT/report_due_1.txt
SITE_CONTENT/report_due_2.txt
SITE_CONTENT/report_due_3.txt

Pickle file:
- clutch.pkl (I/O)
'''

# FIXME: Mail list detection could be improved.
# FIXME: Mail list detection. See svn comments with 2009-11-13 rush bug fix.
# FIXME: Occasional trailing slash issue in Clutch cache.
# FIXME: Some projects use different names in different contexts, and cannot
#        be automatically handled, e.g. Lucene.Net, log4php (some of their stats
#        are missing).
#        See beginning attempt to handle this with "resourceNames".
# FIXME: Perhaps send some error reporting to a log file:
#        - validate the dates.
#        - detect short description, e.g. Hama = Hama
# FIXME: Better/more exception handling, e.g. url open
# FIXME: Need various output formats:
#        - source docs xml file in clutch*.ent (now happening)
#        - simple text list of project names and basic data clutch.txt (now happening)
#        - Notation3 or DOAP or RDFa or some such? (not yet)
#        - python pickle (now happening)
# FIXME: Parse Robert's "audit" stuff.
# FIXME: Detect if they have SVN repo yet.
#        - http://svn.apache.org/repos/asf/incubator/* ensure more than ".."
# FIXME: Similarly with website. Ensure that there is some content length.
# FIXME: Get better hints from Status pages, e.g. sometimes they don't link
#        to their "tracker" etc. they just use text.
# FIXME: News parser gets extra committer if source has commented xml template.
# FIXME: Use fragments via other files for the sets of html notes.
# FIXME: See some other suggestions on the general@ list.
# FIXME: See some other suggestions in clutch.html#notes-2
# FIXME: Better deal with input/output/unicode.
# FIXME: See some other suggestions in issue INCUBATOR-78.

import sys
if sys.version_info < (3, 2):
    raise Exception("Python 3.2 or above is required")

import subprocess
from subprocess import Popen, PIPE
import datetime
from html.parser import HTMLParser
import os.path
import pickle
import pprint
import re
import urllib.request
import urllib.error
import urllib.parse
import xml.dom.minidom
import argparse
import io

# constants for external data ---
GIT = 'https://git-wip-us.apache.org/repos/asf?p=infrastructure-puppet.git;hb=refs/heads/deployment;a=blob_plain;f=modules/subversion_server/files/authorization/%s'
ASF = 'asf-authorization-template'
# PIT='pit-authorization-template'

MAIL_LIST_URL = "http://mail-archives.apache.org/mod_mbox/"

# Constant for site content location ---

SITE_CONTENT_DIR = 'content/'

parser = argparse.ArgumentParser(
    description='Gather details about projects currently in incubation.')
parser.add_argument('--ignoreState',    action='store_true',
                    default='False', help='Ignore state (default false)')
parser.add_argument('-v', '--verbose',  action='store_true',
                    default='False', help='verbose mode (default false)')
parser.add_argument('-q', '--quiet',    action='store_true',
                    default='False', help='quiet mode (default false)')
parser.add_argument('-x', '--external', action='store_true', default='False',
                    help='log external requests (e.g. svn, http) (default false)')
args = parser.parse_args()

# Normal level of info
optionInfo = args.quiet != True

# Issue some extra debug information.
optionVerbose = args.verbose == True
if optionVerbose:
    optionInfo = True

# Use the persistent data to speed operations.
# Occasionally bad data is cached (e.g. experimenting with developing new code).
# So need to ignore the cached data and perform all resource availability
# tests.
optionUseClutchState = args.ignoreState != True

# Should we log external requests?
optionExternal = args.external == True

# Utility functions ----


def logexternal(string):
    if optionExternal:
        print("External: " + string)


def getUrl(url, encoding=None, errors=None):
    logexternal(url)
    # ensure invalid URLs don't cause long wait
    resp = urllib.request.urlopen(url, timeout=5)
    if encoding:
        return io.TextIOWrapper(resp, encoding=encoding, errors=errors)
    else:
        return resp


def osExec(list):
    logexternal(" ".join(list))
    return subprocess.Popen(list, stdout=subprocess.PIPE).communicate()[0]


def osPopen(list):
    logexternal(" ".join(list))
    return subprocess.Popen(list, stdout=subprocess.PIPE, universal_newlines=True)


def getText(nodelist):
    """http://www.python.org/doc/2.5.2/lib/minidom-example.txt"""
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc


def normaliseSVNurl(url):
    rc = url.replace('https://', 'http://')
    if not rc[-1] == '/':
        rc = rc + '/'
    return rc

def checkStatus(k, projectList, status):
    statusFile = SITE_CONTENT_DIR + "projects/{0}.xml".format(k)
    e = projectList[k]
    if os.path.exists(statusFile):
        try:
            dom = xml.dom.minidom.parse(statusFile)
            span = dom.getElementsByTagName("span")
            if (len(span) < 1):
                print("INFO: Missing from status file: "+statusFile)
                print("      <p><span class='{2}'>The {0} project {2} on {1}</span></p>".format(e['name'], e['enddate'], status))
        except (Exception) as e:
            print("Exception processing " + statusFile + " : " + str(e))
            raise
    else:
        print("WARN: Cannot find {0}".format(statusFile))

projects = {}  # internal data, derived from podlings.xml
otherIssues = []
persist = {}  # persistent data to be utilised by other tools
mentorsProjects = {}  # internal data

gatherDate = datetime.datetime.utcnow()
gatherDateString = datetime.datetime.utcnow().ctime()
delta = datetime.timedelta(days=61)
statusTallyDate1 = gatherDate - delta
delta = datetime.timedelta(days=122)
statusTallyDate2 = gatherDate - delta
delta = datetime.timedelta(days=273)
statusTallyDate3 = gatherDate - delta

# Regualar expressions ---
# These expressions are used often, so compile them early.
startDateRE = re.compile("([0-9]+)-0?([0-9]+)-?0?([0-9]+)?")
statusLogRE = re.compile("^([0-9]+)-0?([0-9]+)-0?([0-9]+)")
svnRevisionSkipRE = re.compile(
    "707389|708087|708420|708791|709356|709648|711153|744365|761864|788239|796085|804825|894972|940767|959869|1065888|1153764|1159079|1373730|1479744|1494479|1515212")
mailListRE = re.compile("^([-a-z0-9]+)@([a-z]+)\.apache\.org")
mailListNameRE = re.compile("^([a-z]+)-([-a-z0-9]+)")
mailListNameUrlRE = re.compile("/([a-z]+)-([-a-z0-9]+)/$")
urlHttpRE = re.compile("^http")
newCommitterRE = re.compile("[nN]ew [cC]omm?itt?ers? ?\(?([0-9]+)?")
distMirrorRE = re.compile("cgi/incubator/([-a-z0-9]+)/")

# Import the persistent data ---
# This enables us to skip detection of website etc. if already detected.
inputFile = open('clutch.pkl', 'rb')
state = pickle.load(inputFile)
inputFile.close()

# Parse the podlings data file ---
dom = xml.dom.minidom.parse(SITE_CONTENT_DIR + "podlings.xml")

graduatedProjects = {}
graduatingOrRetiring = []
retiredProjects = {}

print("Gather data from podlings.xml ...")
for row in dom.getElementsByTagName("podling"):
    name = row.getAttribute("name").strip()
    id = name.lower()
    id = id.replace(' ', '')  # strip spaces from project ID
    startDate = row.getAttribute("startdate")
    endDate = row.getAttribute("enddate")

    if row.getAttribute("status") == 'graduated':
        resource = row.getAttribute("resource")
        graduatedProjects[resource.lower()] = {'name': name, 'enddate': endDate}

    if row.getAttribute("status") == 'retired':
        resource = row.getAttribute("resource")
        retiredProjects[resource.lower()] = {'name': name, 'enddate': endDate}

    if row.getAttribute("status") == 'current':
        #print("Name: " + name)

        if id in projects:
            print("ERROR: {0}: row exists".format(id))
        else:
            projects[id] = {}
            # strip spaces from project name (as per original ReportingSchedule)
            # TODO is this still needed? Or should the @name attribute not
            # contain spaces?
            projects[id]['fullName'] = name
            projects[id]['name'] = name.replace(' ', '')
            # Set some defaults
            needMetadata = False
            projects[id]['reportingMonthly'] = False
            projects[id]['reportingComments'] = ""
            projects[id]['hasReportingGroup'] = True
            # currently needed for reporting phase
            projects[id]['reportingGroup'] = 'month'
            projects[id]['hasStatusEntry'] = True
            projects[id]['statusFileName'] = id
            projects[id]['statusLastUpdated'] = ""
            projects[id]['statusAge'] = 0
            projects[id]['statusUpdateCounts'] = ""
            projects[id]['urlSvn'] = ""
            projects[id]['urlTracker'] = ""
            projects[id]['urlWww'] = ""
            projects[id]['urlDist'] = ""
            projects[id]['urlKeys'] = ""
            projects[id]['hasEntryIssues'] = False
            projects[id]['resourceNames'] = [id]
            # Some projects use an alternate short resource name
            # rather than their project name
            alias = row.getAttribute("resource")
            if (alias != '' and alias != id):
                projects[id]['resourceNames'].append(alias)
            for alias in row.getAttribute("resourceAliases").split(','):
                if alias != '':
                    projects[id]['resourceNames'].append(alias)
            projects[id]['entryDate'] = None
            projects[id]['committersSvn'] = None
            projects[id]['hintMailListDev'] = ""
            projects[id]['hasMailListDev'] = ""
            projects[id]['hintMailListCommits'] = ""
            projects[id]['hasMailListCommits'] = ""
            projects[id]['numberCommitters'] = 0
            projects[id]['numberCommittersNew'] = 0

            projects[id]['hasClutchState'] = id in state
            descElements = row.getElementsByTagName("description")
            projects[id]['description'] = getText(descElements[0].childNodes)
            if 'FIXME' in projects[id]['description']:
                needMetadata = True
            projects[id]['sponsor'] = row.getAttribute("sponsor")
            projects[id]['startDate'] = startDate
            projects[id]['statusFileName'] = row.getAttribute("resource")
            mentors = [mentor.firstChild.data.strip()
                       for mentor in row.getElementsByTagName("mentor")]
            projects[id]['mentors'] = mentors
            if 'FIXME' in mentors:
                needMetadata = True
            if needMetadata:
                errorMsg = "{0}: Need to add incubation metadata.".format(id)
                print('ERROR:', errorMsg)
                errorMsg += " Please maintain your records in the content/podlings.xml file. See <a href=\"#h-hasStatusEntry\">help</a>."
                otherIssues.append(errorMsg)

            # determine projects for each mentor
            for mentor in mentors:
                try:
                    mentorsProjects[mentor]
                except KeyError:
                    mentorsProjects[mentor] = []
                mentorsProjects[mentor].append(name)

            isGraduating = row.getElementsByTagName("graduating").length > 0
            if isGraduating:
                graduatingOrRetiring.append(id)
                if not row.getAttribute("endDate"):
                    errorMsg = "{0}: Has graduated, but still needs to follow the graduation steps.".format(
                        id)
                    print('ERROR:', errorMsg)
                    errorMsg += " See <a href=\"#h-Graduate\">help</a>."
                    otherIssues.append(errorMsg)

            isRetiring = row.getElementsByTagName("retiring").length > 0
            if isRetiring:
                graduatingOrRetiring.append(id)
                if not row.getAttribute("endDate"):
                    errorMsg = "{0}: Has retired, but still needs to follow the retirement steps.".format(
                        id)
                    print('ERROR:', errorMsg)
                    errorMsg += " See <a href=\"#h-Retire\">help</a>."
                    otherIssues.append(errorMsg)

            # Is it reporting monthly?
            reporting = row.getElementsByTagName("reporting")
            if reporting.length != 1:
                projects[id]['hasReportingGroup'] = False
                if not isGraduating:
                    print(
                        "ERROR: {0}: expecting a single reportgroup".format(name))
            else:
                if reporting[0].getAttribute("monthly") == 'true':
                    projects[id]['reportingMonthly'] = True
                    projects[id]['reportingComments'] = getText(reporting)
                    projects[id]['hasEntryIssues'] = True
                group = reporting[0].getAttribute("group")
                if group == None:
                    print("ERROR: {0}: missing group attribute".format(name))
                    projects[id]['hasReportingGroup'] = False
                else:
                    projects[id]['reportingGroup'] = 'group-' + group

dom.unlink()

for k in sorted(graduatedProjects):
    checkStatus(k, graduatedProjects, 'graduated')
for k in sorted(retiredProjects):
    checkStatus(k, retiredProjects, 'retired')

# Process the incubation table data, detect some potential issues. ---

print("Gather details from project status files ...")
projectNames = list(projects.keys())
for k in sorted(projectNames, key=str.lower):
    if optionVerbose:
        print("DEBUG: Processing status file for {0}".format(k))

    # Append more potential alternate names for a project
    if projects[k]['statusFileName'] not in projects[k]['resourceNames']:
        projects[k]['resourceNames'].append(projects[k]['statusFileName'])
    if optionVerbose and len(projects[k]['resourceNames']) > 1:
        print("DEBUG: Will try alternate names: {0}".format(
            projects[k]['resourceNames']))

    # parse their project status file to extract specific information
    statusFile = SITE_CONTENT_DIR + \
        "projects/{0}.xml".format(projects[k]['statusFileName'])
    if os.path.exists(statusFile):
        try:
            dom = xml.dom.minidom.parse(statusFile)
        except (Exception) as e:
            print("Exception processing " + statusFile + " : " + str(e))
            raise
        # get the project info hints
        if optionVerbose:
            print("DEBUG: Gather hints from project Status page")
        table = dom.getElementsByTagName("table")[0]
        for row in table.getElementsByTagName("tr")[1:]:
            if (len(row.getElementsByTagName("td")) < 3):
                continue
            cell = row.getElementsByTagName("td")[2]
            if 'id' in cell.attributes:
                values = [getText(item.childNodes) for item in cell.childNodes]
                value = " ".join(values).strip()
                if value == "":
                    value = getText(cell.childNodes).strip()
                if optionVerbose:
                    print("DEBUG: Hint: {0}={1}".format(
                        cell.getAttribute('id'), value))
                if cell.getAttribute('id') == "mail-dev":
                    value = value.replace('  at  ', '@')
                    value = value.replace('  Subscribe  Unsubscribe', '')
                    value = value.replace('  Archive', '')
                    value = value.replace(' ', '@', 1)
                    value = value.replace(' ', '')
                    value = value.replace('@@', '@')
                    matchMail = re.search(mailListRE, value)
                    if matchMail:
                        projects[k][
                            'hintMailListDev'] = "{0}-{1}".format(matchMail.group(2), matchMail.group(1))
                    continue
                if cell.getAttribute('id') == "mail-commits":
                    value = value.replace('  at  ', '@')
                    value = value.replace('  Subscribe  Unsubscribe', '')
                    value = value.replace('  Archive', '')
                    value = value.replace(' ', '@', 1)
                    value = value.replace(' ', '')
                    value = value.replace('@@', '@')
                    matchMail = re.search(mailListRE, value)
                    if matchMail:
                        projects[k][
                            'hintMailListCommits'] = "{0}-{1}".format(matchMail.group(2), matchMail.group(1))
                    continue
                # Get hints for various url-based resources
                matchUrl = re.search(urlHttpRE, value)
                if not matchUrl:
                    for item in cell.getElementsByTagName('a'):
                        if 'href' in item.attributes:
                            value = item.getAttribute('href')
                            break
                hasUrl = re.search(urlHttpRE, value)
                if cell.getAttribute('id') == "svn" and hasUrl:
                    projects[k]['urlSvn'] = value
                    continue
                if cell.getAttribute('id') == "tracker" and hasUrl:
                    projects[k]['urlTracker'] = value
                    continue
                if cell.getAttribute('id') == "www" and hasUrl:
                    projects[k]['urlWww'] = value
                    continue
        # Scan the project News section and count new commiters.
        for section in dom.getElementsByTagName("section"):
            if 'id' in section.attributes and section.getAttribute('id') == "News":
                for line in section.toxml().splitlines():
                    if ('<!--' in line):
                        continue
                    matchNewCommitter = re.search(newCommitterRE, line)
                    if matchNewCommitter:
                        if matchNewCommitter.group(1):
                            projects[k][
                                'numberCommittersNew'] += int(matchNewCommitter.group(1))
                        else:
                            projects[k]['numberCommittersNew'] += 1
        dom.unlink()
    # end of if status file exists

# end of processing incubation table data

# Gather committers data ---

print("Gather committers data ...")
# Parse the locally defined groups directly
committers_projects = {}
with getUrl(GIT % ASF, encoding='UTF-8') as f:
    for line in f:  # skip the header
        if line.startswith('[groups]'):
            break

    for line in f:  # read the defs section
        line = line.rstrip()
        if re.match(r"^(#|\s*$)", line):  # comment or blanks
            continue
        if re.match(r"^\[/\]", line):  # end of definition section
            break
        m = re.match(r"^\s*(\w\S+?)\s*=\s*(\S+)?$", line)
        if m:
            entry = m.group(1)
            value = m.group(2)
            if value:  # ignore empty groups
                if value.startswith('{'):
                    continue
                committers_projects[entry] = value.split(',')
# pprint.pprint(committers_projects)

# Gather incubator group mail list data ---

print("Gather incubator group mail list data ...")


class IncubatorMailListNamesParser(HTMLParser):

    def __init__(self):
        self.strict = True
        self.names = []
        self.newStyle = []
        self.convert_charrefs = False
        self.reset()

    def handle_starttag(self, tag, attrs):
        # Get the newStyle projects
        if tag == "option":
            for key, value in attrs:
                if (key == "value" and ".incubator" in value):
                    value = value.replace('.incubator', '')
                    self.newStyle.append(value)

        # Get all Incubator lists
        if tag == "a":
            for key, value in attrs:
                if (key == "href" and "incubator" in value):
                    value = value.replace('incubator-', '')
                    value = value.replace('/', '')
                    self.names.append(value)
                    break

mailLists = IncubatorMailListNamesParser()
mailLists.feed(getUrl(MAIL_LIST_URL).read().decode('utf-8'))
mailLists.close()
if optionVerbose:
    pprint.pprint(mailLists.names)
    pprint.pprint(mailLists.newStyle)

projectMailLists = {}
mailListNamesRE = re.compile("(.*)-([^-]+)")
mailListNamesUsualRE = re.compile(
    "announce|commits|cvs|dev|issues|notifications|user|users|spec")
for listName in mailLists.names:
    if listName in ["announce", "cvs", "general", "projects"]:
        continue
    if optionVerbose:
        print("DEBUG: listName=" + listName)
    if ('-' in listName):
        matchList = re.search(mailListNamesRE, listName)
        try:
            projectMailLists[matchList.group(1)]
        except KeyError:
            projectMailLists[matchList.group(1)] = {}
        listName = listName.replace('/', '')
        projectMailLists[matchList.group(1)][matchList.group(2)] = listName
        if optionVerbose:
            print("DEBUG: Found list: {0} {1}".format(
                matchList.group(1), matchList.group(2)))
            if (matchList.group(1) not in mailLists.newStyle):
                print("DEBUG: Uses oldStyle list set-up")
        # FIXME: We assume that mail lists are always named like this
        # with "-dev" or "-commits" etc.
        matchListUsual = re.search(mailListNamesUsualRE, matchList.group(2))
        if optionVerbose and not matchListUsual:
            print("WARN: Unusual mail list name '{0}'".format(listName))
    else:
        listName = listName.replace('/', '')
        try:
            projectMailLists[listName]
        except KeyError:
            projectMailLists[listName] = {}
        projectMailLists[listName]['dev'] = listName
        print("WARN: {0}: unusual mail list name '{1}', assuming it is their dev list".format(
            listName, projectMailLists[listName]['dev']))
if optionVerbose:
    print("DEBUG: projectMailLists")
    pprint.pprint(projectMailLists)

# Gather incubator PGP keys data ---

print("Gather incubator PGP keys data and releases ...")

keysList = {}
releases = {}
releasesBadName = {}
distareas = {}  # podlings with dist areas

with osPopen(['svn', 'ls', '-R', 'https://dist.apache.org/repos/dist/release/incubator']) as s:
    for line in s.stdout:
        line = line.rstrip()
        fields = line.split('/')
        podling = fields[0]
        distareas[podling] = True
        file = fields[-1]
        if file:
            if re.search('KEYS(\.txt)?$', file):
                keysList[
                    podling] = "{0}/{1}".format("http://www.apache.org/dist/incubator", line)
            if re.search('(bz2|gz|zip)\.(asc|sig)$', file, flags=re.IGNORECASE):
                if re.search('incubat(ing|or)', file, flags=re.IGNORECASE):
                    releases[podling] = True
                else:
                    releasesBadName[podling] = True

for k in releases:
    # FIXME: need to handle projects[k]['resourceNames']
    if not k in projects:
        if k in graduatedProjects:
            errorMsg = "{0}: Has graduated, but still has remains on Incubator distribution mirrors".format(
                k)
            print('ERROR:', errorMsg)
            errorMsg += ". See <a href=\"#h-Graduate\">help</a>."
            otherIssues.append(errorMsg)
            continue
        if k in retiredProjects:
            print(
                "INFO: {0}: retired project has remains on Incubator mirrors".format(k))

for k in releasesBadName:
    errorMsg = '{0}: Has a distribution filename missing the word "incubating/incubator"'.format(
        k)
    print('ERROR:', errorMsg)
    errorMsg += ". See <a href=\"#h-hasRelease\">help</a>."
    otherIssues.append(errorMsg)
    if k in graduatedProjects:
        errorMsg = "{0}: Has graduated, but still has remains on Incubator distribution mirrors".format(
            k)
        print('ERROR:', errorMsg)
        errorMsg += ". See <a href=\"#h-Graduate\">help</a>."
        otherIssues.append(errorMsg)

# Processing the gathered sata ---

print("Processing ...")
# Process the reporting schedule data, correlate and ensure each exists in the
# incubation projects summary table, add more details to the data store.
projectNames = list(projects.keys())
for k in sorted(projectNames, key=str.lower):
    print(k)

    statusFile = SITE_CONTENT_DIR + \
        "projects/{0}.xml".format(projects[k]['statusFileName'])
    if not os.path.exists(statusFile):
        errorMsg = "{0}: Missing status file".format(k)
        print('ERROR:', errorMsg)
        errorMsg += ". See <a href=\"#h-hasStatusEntry\">help</a>."
        otherIssues.append(errorMsg)
        projects[k]['hasStatusEntry'] = False
        continue

    startDate = projects[k]['startDate']
    match = re.search(startDateRE, startDate)
    if match:
        if match.group(3) != None:
            entryDateDay = int(match.group(3))
        else:
            entryDateDay = 1
        try:
            entryDate = datetime.datetime(
                int(match.group(1)), int(match.group(2)), entryDateDay)
        except ValueError:
            print("ERROR: {0}: ValueError with date".format(k))
        else:
            projects[k]['entryDate'] = entryDate

    # Gather recent updates to their status page.
    inputFile = SITE_CONTENT_DIR + \
        "projects/{0}.xml".format(projects[k]['statusFileName'])
    if optionVerbose:
        print("DEBUG: Parsing svn log for {0} ...".format(inputFile))
    outputString = osExec(['svn', 'log', '--xml', inputFile])
    dom = xml.dom.minidom.parseString(outputString)
    rowCounter = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for row in dom.getElementsByTagName("logentry"):
        # Skip counting various commits which were to standardise the status
        # files.
        matchSvnSkip = re.search(
            svnRevisionSkipRE, row.getAttribute('revision'))
        if matchSvnSkip:
            continue
        rowCounter += 1
        date = getText(row.getElementsByTagName("date")[0].childNodes)
        matchSvn = re.search(statusLogRE, date)
        thisDate = datetime.datetime(
            int(matchSvn.group(1)), int(matchSvn.group(2)), int(matchSvn.group(3)))
        if rowCounter == 1:
            projects[k]['statusLastUpdated'] = "{0:4d}-{1:02d}-{2:02d}".format(
                int(matchSvn.group(1)), int(matchSvn.group(2)), int(matchSvn.group(3)))
        if thisDate >= statusTallyDate1:
            count1 += 1
        if thisDate >= statusTallyDate2:
            count2 += 1
        if thisDate >= statusTallyDate3:
            count3 += 1
    if projects[k]['entryDate'] >= statusTallyDate1:
        count2 = "-"
    if projects[k]['entryDate'] >= statusTallyDate2:
        count3 = "-"
    projects[k]['statusUpdateCounts'] = "{0},{1},{2}".format(
        count1, count2, count3)

    dom.unlink()

# end of processing

# Collect SVN directory names ---

print("Collect SVN directory names")
incubatorSvnDirs = {}  # top-level SVN incubator dirs
outputString = osExec(
    ['svn', 'ls', '--xml', 'http://svn.apache.org/repos/asf/incubator/'])
dom = xml.dom.minidom.parseString(outputString)
"""
Sample output
<lists>
  <list path="http://svn.apache.org/repos/asf/incubator">
    <entry kind="file">
    <name>REPO-ORGANISATION.txt</name>
    ...
    </entry>
    <entry kind="dir">
    <name>accumulo</name>
    ...
"""
for entry in dom.getElementsByTagName("entry"):
    if entry.getAttribute("kind") == 'dir':
        name = entry.getElementsByTagName("name")[0].firstChild.data
        if name not in ('trunk', 'public'):  # skip non-podling entries
            incubatorSvnDirs[
                "http://svn.apache.org/repos/asf/incubator/{0}/".format(name)] = True

# Detect certain resources ---

print("Detect certain resources ...")
for k in sorted(projectNames, key=str.lower):
    print(k)

    # Add the number of committers
    # Sometimes the committer SVN group name contains the sponsor TLP,
    # e.g. portals-wsrp4j
    svnGroups = projects[k]['resourceNames'][:]
    sponsor = projects[k]['sponsor'].lower()
    if '?' in sponsor:
        sponsor = "incubator"
    if not 'incubator' in sponsor:
        tlpSvn = "{0}-{1}".format(sponsor, k)
        svnGroups.append(tlpSvn)
    for svnGroup in svnGroups:
        if optionVerbose:
            print("DEBUG: Trying committers group '{0}'".format(svnGroup))
        if svnGroup in committers_projects:
            projects[k]['numberCommitters'] = len(
                committers_projects[svnGroup])
            projects[k]['committersSvn'] = svnGroup
            break
        else:
            continue
    if projects[k]['committersSvn'] == None and optionInfo:
        print("INFO: {0}: Does not yet have committers accounts".format(k))

    # Detect if they have SVN yet.
    # First, try the URL from their status page
    # then, try URLs based on their resourceNames.
    if optionUseClutchState and projects[k]['hasClutchState'] and state[k]['urlSvn']:
        projects[k]['urlSvn'] = state[k]['urlSvn']
        incubatorSvnDirs[normaliseSVNurl(state[k]['urlSvn'])] = 'used'
    else:
        urls = []
        try:
            projects[k]['urlSvn']
        except:
            pass
        else:
            if projects[k]['urlSvn'] != '':
                urls.append(projects[k]['urlSvn'])
        for name in projects[k]['resourceNames']:
            urls.append(
                "https://svn.apache.org/repos/asf/incubator/{0}/".format(name))
        for url in urls:
            if optionVerbose:
                print("DEBUG: Trying SVN URL " + url)
            if normaliseSVNurl(url) in incubatorSvnDirs:
                projects[k]['urlSvn'] = url
                incubatorSvnDirs[url] = name  # mark used
                break
            try:
                getUrl(url)
            except IOError:
                projects[k]['urlSvn'] = ''
            else:
                projects[k]['urlSvn'] = url
                break
        if not projects[k]['urlSvn'] and optionInfo:
            print("INFO: {0}: Does not yet have SVN".format(k))

    # Detect if they have Tracker yet.
    # First, try the url from their status page
    # then, try a standard url.
    if optionUseClutchState and projects[k]['hasClutchState'] and state[k]['urlTracker']:
        projects[k]['urlTracker'] = state[k]['urlTracker']
    else:
        urlTrackerDefault = "https://issues.apache.org/jira/browse/" + \
            projects[k]['statusFileName'].upper()
        if urlTrackerDefault == projects[k]['urlTracker']:
            urlTrackerDefault = ""
        for url in [projects[k]['urlTracker'], urlTrackerDefault]:
            if url == "":
                continue
            if optionVerbose:
                print("DEBUG: Trying Tracker URL: " + url)
            try:
                getUrl(url)
            except IOError:
                projects[k]['urlTracker'] = ""
            else:
                projects[k]['urlTracker'] = url
                break
        if not projects[k]['urlTracker'] and optionInfo:
            print("INFO: {0}: Does not yet have an Issue Tracker".format(k))

    # Detect if they have a website yet.
    # First, try the url from their status page
    # then, try a standard url.
    if optionUseClutchState and projects[k]['hasClutchState'] and state[k]['urlWww']:
        projects[k]['urlWww'] = state[k]['urlWww']
    else:
        urlWwwDefault = "http://{0}.incubator.apache.org/".format(
            projects[k]['statusFileName'])
        urlWwwDefault2 = "http://incubator.apache.org/{0}/".format(
            projects[k]['statusFileName'])
        if urlWwwDefault == projects[k]['urlWww']:
            urlWwwDefault = ""
        if urlWwwDefault2 == projects[k]['urlWww']:
            urlWwwDefault2 = ""
        for url in [projects[k]['urlWww'], urlWwwDefault, urlWwwDefault2]:
            if url == "":
                continue
            try:
                getUrl(url)
            except IOError:
                projects[k]['urlWww'] = ""
            else:
                projects[k]['urlWww'] = url
                break
        if not projects[k]['urlWww'] and optionInfo:
            print("INFO: {0}: Does not yet have a website".format(k))

    # See if they have a distribution area yet.
    if optionUseClutchState and projects[k]['hasClutchState'] and state[k]['urlDist']:
        projects[k]['urlDist'] = state[k]['urlDist']
    else:
        for nameDist in projects[k]['resourceNames']:
            urlDist = "http://www.apache.org/dist/incubator/{0}/".format(
                nameDist)
            urlMirror = "http://www.apache.org/dyn/closer.cgi/incubator/{0}/".format(
                nameDist)
            if nameDist in distareas:
                projects[k]['urlDist'] = urlMirror
                break
    if not projects[k]['urlDist']:
        if optionInfo:
            print("INFO: {0}: Does not yet have a distribution area".format(k))
    elif optionVerbose:
        print("DEBUG: dist=" + projects[k]['urlDist'])

    # Detect if they have a PGP KEYS file
    if projects[k]['urlDist']:
        match = re.search("/incubator/([^/]+)/", projects[k]['urlDist'])
        if match:
            nameDistArea = match.group(1)
            if nameDistArea in keysList:
                projects[k]['urlKeys'] = keysList[nameDistArea]
            else:
                if optionInfo:
                    print(
                        "INFO: {0}: Does not yet have a PGP KEYS file".format(k))
    if optionVerbose:
        print("DEBUG: KEYS=" + projects[k]['urlKeys'])

    # Detect mail lists established:
    # For each alternate resourceName:
    # First, try the list names from their status page
    # then, try a standard list name under incubator.
    # To reduce network queries, if it is an incubator-hosted list then look up in
    # the list of mail-lists already gathered, otherwise it is a TLP-hosted list,
    # so try getting the archives URL.
    foundMailLists = False
    for projectName in projects[k]['resourceNames']:
        for listType in ['dev', 'commits']:
            if listType == "dev":
                mailListHintKey = "hintMailListDev"
                mailListKey = "hasMailListDev"
            else:
                mailListHintKey = "hintMailListCommits"
                mailListKey = "hasMailListCommits"
            if optionVerbose:
                print("DEBUG: Looking for mailList: " +
                      projects[k][mailListHintKey])
            matchMail = re.search(mailListNameRE, projects[k][mailListHintKey])
            if matchMail:
                mailListGroup = matchMail.group(1)
                mailListNameHint = matchMail.group(2)
            else:
                mailListGroup = "incubator"
                mailListNameHint = ""
            if optionVerbose:
                print("DEBUG: Trying mailListGroup={0} mailListNameHint={1}".format(
                    mailListGroup, mailListNameHint))
            if mailListGroup == "incubator":
                mailListNameDefault = "{0}-{1}".format(projectName, listType)
                if mailListNameDefault == mailListNameHint:
                    mailListNameDefault = ""
                for listName in [mailListNameHint, mailListNameDefault]:
                    if listName == "":
                        continue
                    if optionVerbose:
                        print("DEBUG: Trying listName=" + listName)
                    if not projectName in projectMailLists:
                        if optionVerbose:
                            print("DEBUG: {0}: No incubator group mail lists using '{1}'".format(
                                k, projectName))
                        break
                    if listType in projectMailLists[projectName]:
                        leader = 'incubator-' if (
                            k not in mailLists.newStyle) else ''
                        projects[k][mailListKey] = MAIL_LIST_URL + \
                            "{0}{1}/".format(leader,
                                             projectMailLists[projectName][listType])
                        if optionVerbose:
                            print("DEBUG: Successful Incubator mail url: " +
                                  projects[k][mailListKey])
                        foundMailLists = True
                        break
                    else:
                        if optionInfo:
                            print("INFO: {0}: Does not yet have hinted incubator mail list '{1}-{2}'".format(
                                k, projectName, listType))
                        projects[k][mailListKey] = ""
            # End of processing incubator group mail list.
            else:
                listName = projects[k][mailListHintKey]
                url = "http://mail-archives.apache.org/mod_mbox/{0}/".format(
                    listName)
                if optionVerbose:
                    print("DEBUG: Trying mail url: " + url)
                try:
                    getUrl(url)
                except IOError:
                    projects[k][mailListKey] = ""
                else:
                    projects[k][mailListKey] = url
                    if optionVerbose:
                        print("DEBUG: Successful TLP mail url: " + url)
                    foundMailLists = True
        if foundMailLists:
            break
    # End of processing project mail lists.
    if not projects[k]['hasMailListDev'] and optionInfo:
        print("INFO: {0}: Does not yet have 'dev' mail list".format(k))
    if not projects[k]['hasMailListCommits'] and optionInfo:
        print("INFO: {0}: Does not yet have 'commits' mail list".format(k))

# end of processing each podling to detect resource availability

if optionInfo:
    for entry in sorted(incubatorSvnDirs):
        if incubatorSvnDirs[entry] == True and entry in graduatedProjects:
            print("INFO: graduated project has SVN directory " + entry)

# Output data files ---

print("Output the data ...")
reportingGroups = {'month': 'Monthly',
                   'group-1': 'January,April,July,October',
                   'group-2': 'February,May,August,November',
                   'group-3': 'March,June,September,December'}
monthsLong = 'January February March April May June July August September October November December'.split()
nameCurrentReport = "{0}{1}".format(
    monthsLong[gatherDate.month - 1], gatherDate.year)
urlCurrentReport = "".join(
    ["http://wiki.apache.org/incubator/", nameCurrentReport])

fileXmlMY = open(SITE_CONTENT_DIR + 'clutchmy.ent', encoding='utf-8', mode='w')
fileXmlMY.write(
    '<a href="{0}">{1}</a>\n'.format(urlCurrentReport, nameCurrentReport))
fileXmlMY.close()

fileList = open(SITE_CONTENT_DIR + 'clutch.txt', 'w')

fileXmlo1 = open(SITE_CONTENT_DIR + 'clutcho1.ent', encoding='utf-8', mode='w')
fileXmlo1.write("<!-- generated by clutch; do not edit -->\n")
if len(otherIssues):
    otherXml = """<li>other issues <a href="#other">listed</a> below for: """
    otherIssuesRE = re.compile("^([^:]+):.*$")
    otherIssues.sort()
    for issue in otherIssues:
        matchOtherIssues = re.search(otherIssuesRE, issue)
        otherXml += '\n <span class="care">{0}</span> '.format(
            matchOtherIssues.group(1))
    otherXml += "\n</li>\n"
    fileXmlo1.write(otherXml)
fileXmlo1.close()

fileXmlt = open(SITE_CONTENT_DIR + 'clutcht.ent', encoding='utf-8', mode='w')
fileXmlt.write("<!-- generated by clutch; do not edit -->\n")
tableTopXml = """
        Clutch last gathered: {0} UTC.<br />
        Number of podlings in incubation: {1}
""".format(gatherDateString, len(projects))
fileXmlt.write(tableTopXml)
fileXmlt.close()

fileList.write('#identifier,name,sponsor\n')
reportList1 = ""
reportList2 = ""
reportList3 = ""
tableRowCount = 0
tableRowCountMid = int(len(projects) / 2)
fileXml = open(SITE_CONTENT_DIR + 'clutchr1.ent', encoding='utf-8', mode='w')
fileXml.write("<!-- generated by clutch; do not edit -->\n")
for k in sorted(projectNames, key=str.lower):
    tableRowCount += 1
    if tableRowCount == tableRowCountMid:
        fileXml.close()
        fileXml = open(SITE_CONTENT_DIR + 'clutchr2.ent',
                       encoding='utf-8', mode='w')
        fileXml.write("<!-- generated by clutch; do not edit -->\n")
    fileXml.write('        <tr id="{0}">\n'.format(k))
    fileXml.write('          <td')
    if k in graduatingOrRetiring:
        fileXml.write(' class="grad"')
    fileXml.write('>{0}</td>\n'.format(projects[k]['fullName']))
    persist[k] = {}
    persist[k]['podlingName'] = projects[k]['name']
    persist[k]['fullName'] = projects[k]['fullName']

    if '?' in projects[k]['sponsor']:
        fileXml.write(
            '          <td class="issue">{0}</td>\n'.format(projects[k]['sponsor']))
    else:
        fileXml.write(
            '          <td>{0}</td>\n'.format(projects[k]['sponsor']))
    persist[k]['sponsor'] = projects[k]['sponsor']
    persist[k]['description'] = projects[k]['description']
    persist[k]['mentors'] = projects[k]['mentors']

    fileXml.write('          <td>{0}</td>\n'.format(projects[k]['startDate']))
    persist[k]['startDate'] = projects[k]['startDate']

    # elapsedDays column
    fileXml.write('          <td></td>\n')

    if not projects[k]['reportingMonthly']:
        fileXml.write(
            '          <td>{0}</td>\n'.format(projects[k]['reportingMonthly']))
    else:
        fileXml.write(
            '          <td class="care">{0}</td>\n'.format(projects[k]['reportingMonthly']))
    persist[k]['reportingMonthly'] = projects[k]['reportingMonthly']

    fileXml.write(
        '          <td>{0}</td>\n'.format(projects[k]['reportingGroup']))
    # save the simple group number for programs that have their own ideas.
    persist[k]['rawReportingGroup'] = projects[k]['reportingGroup']
    persist[k]['reportingGroup'] = reportingGroups[
        projects[k]['reportingGroup']]
    reportDevList = '"{0} Developers"'.format(projects[k]['fullName'])
    if projects[k]['hasMailListDev']:
        matchDevMail = re.search(mailListNameUrlRE, projects[
                                 k]['hasMailListDev'])
        if matchDevMail:
            mailListGroup = None
            for alias in projects[k]['resourceNames']:
                if (alias in mailLists.newStyle):
                    mailListGroup = alias
            if (mailListGroup != None):
                reportDevList += " <dev@{0}.incubator.apache.org>".format(
                    mailListGroup)
            else:
                reportDevList += " <{0}@{1}.apache.org>".format(
                    matchDevMail.group(2), matchDevMail.group(1))
        else:
            reportDevList += " <general@incubator.apache.org>"
    else:
        reportDevList += " <general@incubator.apache.org>"
    if optionVerbose:
        print("DEBUG: {0}: reportDevList={1}".format(k, reportDevList))
    reportDevList += "\n"
    if projects[k]['reportingMonthly']:
        reportList1 += reportDevList
        reportList2 += reportDevList
        reportList3 += reportDevList
    else:
        if (projects[k]['reportingGroup'] == "group-1"):
            reportList1 += reportDevList
        elif (projects[k]['reportingGroup'] == "group-2"):
            reportList2 += reportDevList
        elif (projects[k]['reportingGroup'] == "group-3"):
            reportList3 += reportDevList

    if projects[k]['hasReportingGroup']:
        fileXml.write(
            '          <td class="cool1">{0}</td>\n'.format(projects[k]['hasReportingGroup']))
    else:
        fileXml.write(
            '          <td class="issue">{0}</td>\n'.format(projects[k]['hasReportingGroup']))

    if projects[k]['hasStatusEntry']:
        fileXml.write('          <td class="cool1"><a href="projects/{0}.html">{1}</a></td>\n'.format(
            projects[k]['statusFileName'], projects[k]['hasStatusEntry']))
    else:
        fileXml.write(
            '          <td class="issue">{0}</td>\n'.format(projects[k]['hasStatusEntry']))

    fileXml.write(
        '          <td>{0}</td>\n'.format(projects[k]['statusLastUpdated']))

    # statusAge column
    fileXml.write('          <td></td>\n')

    fileXml.write(
        '          <td>{0}</td>\n'.format(projects[k]['statusUpdateCounts']))

    if projects[k]['numberCommitters'] > 0:
        if projects[k]['numberCommitters'] > 2:
            fileXml.write('          <td class="cool1 number"><a href="http://people.apache.org/committers-by-project.html#{0}">{1}</a></td>\n'.format(
                projects[k]['committersSvn'], projects[k]['numberCommitters']))
        else:
            fileXml.write('          <td class="care number"><a href="http://people.apache.org/committers-by-project.html#{0}">{1}</a></td>\n'.format(
                projects[k]['committersSvn'], projects[k]['numberCommitters']))
    else:
        fileXml.write('          <td class="care">-</td>\n')

    if projects[k]['numberCommittersNew'] > 0:
        if projects[k]['numberCommittersNew'] > 1:
            fileXml.write(
                '          <td class="cool1 number">{0}</td>\n'.format(projects[k]['numberCommittersNew']))
        else:
            fileXml.write(
                '          <td class="cool2 number">{0}</td>\n'.format(projects[k]['numberCommittersNew']))
    else:
        fileXml.write('          <td class="care number">0</td>\n')

    if projects[k]['urlSvn']:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlSvn']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['urlSvn'] = projects[k]['urlSvn']

    if projects[k]['urlTracker']:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlTracker']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['urlTracker'] = projects[k]['urlTracker']

    hasUrl = re.search(urlHttpRE, projects[k]['hasMailListDev'])
    if hasUrl:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['hasMailListDev']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['hasMailListDev'] = projects[k]['hasMailListDev']

    hasUrl = re.search(urlHttpRE, projects[k]['hasMailListCommits'])
    if hasUrl:
        fileXml.write('          <td class="cool1"><a href="{0}">True</a></td>\n'.format(
            projects[k]['hasMailListCommits']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['hasMailListCommits'] = projects[k]['hasMailListCommits']

    if projects[k]['urlWww']:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlWww']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['urlWww'] = projects[k]['urlWww']

    if projects[k]['urlDist']:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlDist']))
    else:
        fileXml.write('          <td class="care">False</td>\n')
    persist[k]['urlDist'] = projects[k]['urlDist']

    if projects[k]['urlKeys']:
        fileXml.write(
            '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlKeys']))
    else:
        fileXml.write('          <td class="care">False</td>\n')

    match = re.search(distMirrorRE, projects[k]['urlDist'])
    if match:
        if match.group(1) in releases:
            fileXml.write(
                '          <td class="cool1"><a href="{0}">True</a></td>\n'.format(projects[k]['urlDist']))
        else:
            fileXml.write('          <td class="care">False</td>\n')
    else:
        fileXml.write('          <td class="care">False</td>\n')

    fileXml.write('        </tr>\n')

    fileList.write('{0},"{1}","{2}"\n'.format(
        k, projects[k]['name'], projects[k]['sponsor']))

fileXml.close()
# End of rows

# Other issues
fileXmlo2 = open(SITE_CONTENT_DIR + 'clutcho2.ent', encoding='utf-8', mode='w')
fileXmlo2.write("<!-- generated by clutch; do not edit -->\n")
if len(otherIssues):
    otherIssues.sort()
    for issue in otherIssues:
        fileXmlo2.write("        <li>{0}</li>\n".format(issue))
else:
    fileXmlo2.write("        <li>No known issues.</li>\n")
fileXmlo2.close()


mentors = list(mentorsProjects.keys())
mentors.sort()
fileXmlm = open(SITE_CONTENT_DIR + 'clutchm.ent', encoding='utf-8', mode='w')
fileXmlm.write("<!-- generated by clutch; do not edit -->\n")
for mentor in mentors:
    fileXmlm.write("        <li><strong>{0}</strong>: {1}</li>\n".format(
        mentor, ', '.join(mentorsProjects[mentor])))
fileXmlm.close()

fileList.close()

fileReport1 = open(SITE_CONTENT_DIR + 'report_due_1.txt', 'w')
fileReport1.write(reportList1)
fileReport1.close()
fileReport2 = open(SITE_CONTENT_DIR + 'report_due_2.txt', 'w')
fileReport2.write(reportList2)
fileReport2.close()
fileReport3 = open(SITE_CONTENT_DIR + 'report_due_3.txt', 'w')
fileReport3.write(reportList3)
fileReport3.close()

# Create the persistent data file.
outputFile = open('clutch.pkl', 'wb')
pickle.dump(persist, outputFile, protocol=3)
outputFile.close()

print("Done. Generated clutch*.ent files.")
print("Now you need to re-build the site, as usual.")
