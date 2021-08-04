Title: ActiveMQ Codebase Intellectual Property (IP) Clearance Status


ActiveMQ is a fast open source JMS 1.1 provider and Message Fabric supporting clustering, peer networks, discovery, TCP, SSL, multicast, persistence, XA and integrates seamlessly into J2EE 1.4 containers, light weight containers and any Java application.



- Which PMC will be responsible for the code: Apache Geronimo PMC


- Into which existing project/module: ActiveMQ will go into its own project


- Officer or member managing donation: James Strachan

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2006-02-18 | Trademark, ActiveMQ, assigned to ASF |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2006-02-04 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2005-12-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _the name of the grant as record in the grants.txt document so that the grant can be easily identified_  **DONE** 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _For individuals, use the name as recorded on the committers page_ 

| date | item |
|------|------|
| 2006-01-20 | 
Check that all active committers have a signed CLA on record.

svn log https://svn.codehaus.org/activemq/branches/activemq-4-0 | grep "r[0-9][0-9]* | " | sed "s/r[0-9][0-9]* | \(.*\) | .* | .*$/\1/" | sort | uniq
All of the committers have a CLA on file at Apache. The following table maps the unix user names to real names:


 | aco | Adrian Co|
 | ammulder | Aaron Mulder|
 | brianm | Brian McCallister|
 | chirino | Hiram Chirino|
 | djcook | Dennis Cook|
 | foconer | Frederick OConer|
 | gnt | Guillaume Nodet|
 | gregw | Gregory Wilkins|
 | jgapuz | Joseph Gapuz|
 | jlim | Jonas Lim|
 | jstrachan | James Strachan|
 | maguro | Alan Cabrera|
 | pbrooke | TO BE DISCOVERED|
 | pvillacorta | Patrick Villacorta|
 | rajdavies | Robert Davies|
 | rsaba | Ramzi Saba|
 |
| ....-..-.. | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| ....-..-.. | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  _The VOTE thread accepting the donation may happen either before or after IP clearance. Adoption by lazy concensus is acceptable but not recommended._ 
