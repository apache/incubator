Title: SystemML Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


SystemML provides declarative large-scale machine learning (ML) that aims at flexible specification of ML algorithms and automatic generation of hybrid runtime plans ranging from single node, in-memory computations, to distributed computations such as Apache Hadoop MapReduce and Apache Spark.


<span class="graduated">The SystemML project graduated on 2017-05-18</span>



- 2015-11-02 Project enters incubation.

- 2015-11-02 Podling name search submitted.

- 2016-02-11 Apache SystemML 0.9.0 (incubating) released

- 2016-05-03 New committer/ppmc: Glenn Weidner

- 2016-05-16 New committer/ppmc: Faraz Makari Manshadi

- 2016-06-10 Apache SystemML 0.10.0 (incubating) released

- 2016-11-13 Apache SystemML 0.11.0 (incubating) released

- 2016-11-19 New mentor: Henry Saputra

- 2017-01-13 New committer/ppmc: Nakul Jindal

- 2017-02-08 Apache SystemML 0.12.0 (incubating) released

- 2017-03-03 Apache SystemML 0.13.0 (incubating) released

- 2017-04-19 New committer/ppmc: Felix Schuler

- 2017-05-08 Apache SystemML 0.14.0 (incubating) released

- 2017-05-18 Apache SystemML graduates as a top level project

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://systemml.apache.org/](http://systemml.apache.org/)  |
| . | wiki | . |
| Mailing list | dev |  `dev`  `@`  `systemml.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `systemml.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `systemml.incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/SYSTEMML](https://issues.apache.org/jira/browse/SYSTEMML)  |
| Source code | GIT |  [https://gitbox.apache.org/repos/asf?p=incubator-systemml.git](https://gitbox.apache.org/repos/asf?p=incubator-systemml.git)  |
| Mentors | hsaputra | Henry Saputra |
| . | lresende | Luciano Resende |
| . | pwendell | Patrick Wendell |
| . | rxin | Reynold Xin |
| . | rbowen | Rich Bowen |
| PPMC/Committers | ae2015 | Alexandre V Evfimievski |
| . | acs_s | Arvind Surve |
| . | reinwald | Berthold Reinwald |
| . | dbtsai | DB Tsai |
| . | deron | Deron Eriksson |
| . | fmakari | Faraz Makari |
| . | fschueler | Felix Schuler |
| . | freiss | Fred Reiss |
| . | gweidner | Glenn Weidner |
| . | hsaputra | Henry Saputra |
| . | holden | Holden Karau |
| . | jkbradley | Joseph Bradley |
| . | lresende | Luciano Resende |
| . | mboehm7 | Matthias Boehm |
| . | dusenberrymw | Mike Dusenberry |
| . | nakul02 | Nakul Jindal |
| . | niketanpansare | Niketan Pansare |
| . | pwendell | Patrick WendelL |
| . | prithvi | Prithviraj Sen |
| . | rxin | Reynold Xin |
| . | shirisht | Shirish Tatikonda |
| . | meng | Xiangrui Meng |


-  [2015-12 SystemML Incubator Report](https://wiki.apache.org/incubator/December2015) 

-  [2016-01 SystemML Incubator Report](https://wiki.apache.org/incubator/January2016) 

-  [2016-02 SystemML Incubator Report](https://wiki.apache.org/incubator/February2016) 

-  [2016-05 SystemML Incubator Report](https://wiki.apache.org/incubator/May2016) 

-  [2016-08 SystemML Incubator Report](https://wiki.apache.org/incubator/August2016) 

-  [2016-11 SystemML Incubator Report](https://wiki.apache.org/incubator/November2016) 

-  [2017-02 SystemML Incubator Report](https://wiki.apache.org/incubator/February2017) 

-  [2017-05 SystemML Incubator Report](https://wiki.apache.org/incubator/May2017) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2015-12-30 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| 2015-11-30 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2015-12-09 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2015-11-04 | Ask infrastructure to set up and archive mailing lists. |
| 2016-01-16 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| ....-..-.. | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2016-01-16 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2015-11-30 | Subscribe all Mentors on the pmc and general lists. |
| 2015-11-30 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2015-11-30 | Tell Mentors to track progress in the file 'incubator/projects/systemml.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2015-11-30 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2016-02-12 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2016-02-12 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2015-11-09 | Check that all active committers have submitted a contributors agreement. |
| 2015-11-09 | Add all active committers in the STATUS file. |
| 2015-11-09 | Ask root for the creation of committers' accounts on people.apache.org. |

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

## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it? Yes, on May 17, 2017, the ASF Board voted to approve Apache SystemML as a Top Level Project. See [here](http://mail-archives.apache.org/mod_mbox/incubator-systemml-dev/201705.mbox/%3CCAGU5spde-w2fwVfQp8wLpuDN_66Z3rhPLUb%2BMMy8o_nR5oDC9Q%40mail.gmail.com%3E) .

## Incubator sign-off {#Incubator+sign-off}


- SystemML received [5 +1 binding votes](https://www.mail-archive.com/general@incubator.apache.org/msg59748.html) to graduate from the Apache Incubator.
