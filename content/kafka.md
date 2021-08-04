Title: Kafka Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Kafka project graduated on 2012-10-23</span>


Kafka provides an extremely high throughput distributed publish/subscribe messaging system. Additionally, it supports relatively long term persistence of messages to support a wide variety of consumers, partitioning of the message stream across servers and consumers, and functionality for loading data into Apache Hadoop for offline, batch processing.



- 2011-07-04 Project enters incubation.

- 2012-05-07 New committer Joel Koshy

- 2012-05-07 New committer Prashanth Menon

- 2012-05-07 New committer Joe Stein


- link to the main website


- link to the page(s) that tell how to participate (Website, Mailing lists, Bug tracking, Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/kafka/](http://incubator.apache.org/kafka/)  |
| . | wiki | . |
| Mailing list | dev |  `kafka-dev`  `@`  `incubator.apache.org`  |
| . | users |  `kafka-users`  `@`  `incubator.apache.org`  |
| . | commits |  `kafka-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | . | https://issues.apache.org/jira/browse/KAFKA |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/kafka/](https://svn.apache.org/repos/asf/incubator/kafka/)  |
| Mentors | adc | Alan D. Cabrera |
| . | cdouglas | Chris Douglas |
| . | geirm | Geir Magnusson Jr. |
| . | omalley | Owen O'Malley |
| Committers | jkreps | Jay Kreps |
| . | junrao | Jun Rao |
| . | nehanarkhede | Neha Narkhede |
| . | jghoman | Jakob Homan |
| . | cburroughs | Chris Burroughs |
| . | jjkoshy | Joel Koshy |
| . | prashanthmenon | Prashanth Menon |
| . | joestein | Joe Stein |
| Extra | . | . |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2011-08-01 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2011-07-04 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2011-07-04 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2011-07-04 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2011-07-04 | Ask infrastructure to set up and archive mailing lists. |
| 2011-07-04 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2011-07-04 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2011-08-03 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2011-07-04 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2011-07-04 | Subscribe all Mentors on the pmc and general lists. |
| 2011-07-04 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2011-07-04 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-08-03 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-07-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2011-07-28 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-07-28 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2011-07-07 | Check that all active committers have submitted a contributors agreement. |
| 2011-07-04 | Add all active committers in the STATUS file. |
| 2011-07-07 | Ask root for the creation of committers' accounts on people.apache.org. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- Are project decisions being made in public by the committers?

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
