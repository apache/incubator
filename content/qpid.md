Title: Qpid Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Qpid project graduated on 2008-12-18</span>


The Qpid Project provides an open and interoperable, multiple language implementations of the Advanced Messaged Queuing Protocol (AMQP) specification and related technologies including PGM, transaction management, queuing, distribution, security, management and heterogeneous multi-platform support for messaging.



- Nov 08 - Jonathan Robie was voted in as new committer. He contributed the XML exchange and has done a lot of work improving examples/documentation around Qpid

- Oct 08 - M3 release

- Sep 08 - Lahiru Gunathilake was voted in as a new committer. He contributed a CLI management tool as part of the GSoC project

- Sep 08 - Manuel Teira was voted in as a new committer. He is working on a solaris port for the c++ broker

- Sep 08 - Steve Huston was voted in as a new committer. He is working on a windows port for the c++ broker

- June 08 - Apache Axis2/C have AMQP support via Qpid

- June 08 - Apache Synapse and Apache Axis2/Java have AMQP support via Qpid

- May 08 - M2.1 release

- May 08 - Addition of new committer (Ted Ross)

- Feb 08 - Karma clean up, done by community process

- Jan 08 - Addition of new committer (Aidan Skinner)

- Jan 08 - Vote of Qpid community to request graduation as TLP

- Dec 07 - Set scope and dates for M2.1

- Dec 07 - Moving of build system back to Ant

- Jan 07 - Addition of new committer (Nuno Santos)

- Oct 07 - M2 release of Qpid

- July 07 - Closing of legal questions on TCK and passing all JMS TCK tests

- June 08 - Addition of new committer (Arnaud Simon)

- June 07 - Added Ruby client

- June 07 - Addition of .NET client

- June 07 - M1 release of Qpid

- Apr 07 - Addition of new committer (Tomas Restrepo)

- Apr 07 - Addition of new committer (Kevin Smith)

- Apr 07 - Addition of new committer (Rupert Smith)

- Jan 07 - Addition of new committer (Jim Meyering)

- Jan 07 - Addition of new committer (Robert Godfrey)

- Jan 07 - Addition of new committer (Andrew Stitcher)

- Jan 07 - New C++ build/ make system

- Dec 06 - Migration of build system to Maven

- Nov 06 - IP Clearance for code grant

- Nov 06 - Creation of committer accounts

- Sept 06 - Project setup

- Aug 06 - Acceptance into Incubator

| item | type | reference |
|--------|--------|-------------|
| Website | www |  [http://qpid.apache.org](http://qpid.apache.org)  |
| . | wiki |  [http://cwiki.apache.org/confluence/display/qpid/Index](http://cwiki.apache.org/confluence/display/qpid/Index)  |
| Mailing list | dev |  `dev`  `@`  `qpid.apache.org`  |
| . | svn |  `commits`  `@`  `qpid.apache.org`  |
| . | private |  `private`  `@`  `qpid.apache.org`  |
| Bug tracking | . |  [http://issues.apache.org/jira/browse/QPID](http://issues.apache.org/jira/browse/QPID)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/qpid/trunk/](https://svn.apache.org/repos/asf/qpid/trunk/)  |
| Mentors | cliffs | Cliff Schmidt |
| . | pzf | Paul Fremantle |
| . | yoavs | Yoav Shapira |
| . |  | Scott Deboy |
| . |  | Craig L Russell |
| Committers | . | . |
| . | . | Aidan Skinner |
| . | . | Alan Conway |
| . | . | Arnaud Simon |
| . | . | Andrew Stitcher |
| . | . | Carl Trieloff |
| . | . | Gordon Sim |
| . | . | Jim Meyering |
| . | . | John O'Hara |
| . | . | Jonathan Robie |
| . | . | Kim van der Riet |
| . | . | Lahiru Gunathilake |
| . | . | Marnie McCormack |
| . | . | Martin Ritchie |
| . | . | Manuel Teira |
| . | . | Kim van der Riet |
| . | . | Paul Fremantle |
| . | . | Nuno Santos |
| . | . | Rafael Schloming |
| . | . | Rajith Attapattu |
| . |  | Robert Godfrey. |
| . | . | Robert Greig. |
| . | . | Rupert Smith |
| . | . | Steve Huston |
| . | . | Yoav Shapira |


- Latest available at http://wiki.apache.org/incubator/April2007

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated&amp;#xD; {#Identify+the+project+to+be+incubated%26%23xD%3B}

| date | item |
|--------|--------|
| 2006-08-27 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2006-08-27 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2006-08-27 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|--------|--------|
| 2006-08-27 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2006-11-02 | Subscribe all Mentors on the pmc and general lists. |
| 2006-08-27 | Give all Mentors access to the incubator SVN repository. (to be done by PMC chair) |
| 2007-04-17 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|--------|--------|
| 2006-11-02 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2006-11-02 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|--------|--------|
| 2006-11-01 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2006-11-01 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|--------|--------|
| 2006-09-01 | Check that all active committers have submitted a contributors agreement. |
| 2006-09-01 | Add all active committers in the STATUS file. |
| 2006-09-01 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|--------|--------|
| 2006-09-01 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2006-09-01 | Ask infrastructure to set up and archive Mailing lists. |
| 2006-09-30 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2006-09-01 | Migrate the project to our infrastructure. |

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



- Understanding the details between JCP and announce compliance

- Making sure we are comfortable with the working relationship between Qpid and the AMQP Working Group.



# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
