Title: ServiceMix Codebase Intellectual Property (IP) Clearance Status


Apache ServiceMix is an open source distributed Enterprise Service Bus (ESB) and SOA toolkit built from the ground up on the semantics and APIs of the Java Business Integration (JBI) specification JSR 208.



- Which PMC will be responsible for the code: Apache Geronimo PMC


- Into which existing project/module: ServiceMix will go into its own project


- Officer or member managing donation: James Strachan

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2006-02-18 | Trademark, ServiceMix, assigned to ASF |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2006-02-04 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2005-12-26 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

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


 | bsnyder | Bruce Snyder|
 | chirino | Hiram Chirino|
 | dandiep | Daniel Diephouse|
 | foconer | Frederick OConer|
 | gastaldi | George Gastaldi|
 | gnt | Guillaume Nodet|
 | gregw | Gregory Wilkins|
 | janb | Jan Bartel|
 | jgapuz | Joseph Gapuz|
 | jlim | Jonas Lim|
 | jstrachan | James Strachan|
 | maguro | Alan Cabrera|
 | myap | Merwin Yap|
 | pdodds | Philip Dodds|
 | rajdavies | Robert Davies|
 |
| ....-..-.. | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| ....-..-.. | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  _The VOTE thread accepting the donation may happen either before or after IP clearance. Adoption by lazy concensus is acceptable but not recommended._ 
