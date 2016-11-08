#!/usr/bin/env python2.7

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

import json
import email.utils
from pprint import pprint
import getpass
from smtplib import SMTP_SSL as SMTP
import datetime
from dateutil.parser import parse
from email.mime.text import MIMEText

def findWednesday(d, weeks):
    days_ahead = 2 - d.weekday()
    if days_ahead <= 0:
        days_ahead += weeks * 7
    else:
        days_ahead += (weeks - 1) * 7 #we're after wednesday, give less time
    return d + datetime.timedelta(days_ahead)

fp = open('email_reminder_template.txt', 'rb')
messageBody = fp.read()
fp.close()

with open('content/shepherd_assignments.json') as data_file:    
    data = json.load(data_file)


month = raw_input('Enter month, in the format of YYYY-MM: ')
username = raw_input('Enter your ASF Username: ')
password = getpass.getpass('Enter your ASF pw: ')

podlingsToReport = data[month].keys()

meFormat = '{}@apache.org'
emailFormat = "dev@{}.incubator.apache.org"

me = meFormat.format(username)

overrides = {
    'odftoolkit':'odf-dev@incubator.apache.org',
    'climatemodeldiagnosticanalyzer':'dev@cmda.incubator.apache.org',
    'blur':'blur-dev@incubator.apache.org',
    'wave':'wave-dev@incubator.apache.org',
    'log4cxx2':'log4cxx-dev@logging.apache.org'
}


thisMonth = parse(month + "-01")

podlingReportsDue = findWednesday(thisMonth, 1)

boardMeeting = findWednesday(thisMonth, 3)

subjectDate = thisMonth.strftime("%B %Y")
wikiPage = thisMonth.strftime("%B%Y")
dueDateFormat = podlingReportsDue.strftime("%a, %B %d")
boardMeetingFormat = boardMeeting.strftime("%a, %d %B %Y")

emailBodyString = messageBody.format(boardMeetingFormat, dueDateFormat, wikiPage)

s = SMTP('mail-relay.apache.org')
s.login(username, password)
print "connected"
for podling in podlingsToReport:
    if podling in overrides:
        emailTo = overrides[podling]
    else:
        emailTo = emailFormat.format(podling)
    msgId = email.utils.make_msgid()
    msg = MIMEText(emailBodyString)
    msg['Subject'] = 'Podling Report Reminder - '+subjectDate
    msg['From'] = me
    msg['Date'] = email.utils.formatdate()
    msg['To'] = emailTo
    msg['Message-ID'] = msgId
    s.sendmail(me, [emailTo], msg.as_string())
    print(' sent ',msgId,' to podling ',emailTo)

s.quit()
