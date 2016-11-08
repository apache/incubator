import json
import email.utils
from pprint import pprint
import getpass
from smtplib import SMTP_SSL as SMTP
import datetime
from dateutil.parser import parse
from email.mime.text import MIMEText


template = raw_input('Path to the template: ')
fp = open(template, 'rb')
messageBody = fp.read()
fp.close()

username = raw_input('Enter your ASF Username: ')
password = getpass.getpass('Enter your ASF pw: ')

podlingsToEmail = ('hawq','htrace','iota','joshua','mnemonic','sirona','tamaya','unomi')

meFormat = '{}@apache.org'
emailFormat = "dev@{}.incubator.apache.org"

me = meFormat.format(username)

overrides = {
    'climatemodeldiagnosticanalyzer':'dev@cmda.incubator.apache.org',
    'blur':'blur-dev@incubator.apache.org',
    'wave':'wave-dev@incubator.apache.org',
    'log4cxx2':'log4cxx-dev@logging.apache.org'
}


subjectDate = 'Website Branding Issues'

emailBodyString = messageBody

s = SMTP('mail-relay.apache.org')
s.login(username, password)
print "connected"
for podling in podlingsToEmail:
    if podling in overrides:
        emailTo = overrides[podling]
    else:
        emailTo = emailFormat.format(podling)
    msgId = email.utils.make_msgid()
    msg = MIMEText(emailBodyString)
    msg['Subject'] = subjectDate
    msg['From'] = me
    msg['Date'] = email.utils.formatdate()
    msg['To'] = emailTo
    msg['Message-ID'] = msgId
    s.sendmail(me, [emailTo], msg.as_string())
    print(' sent ',msgId,' to podling ',emailTo)

s.quit()
