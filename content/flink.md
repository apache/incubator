Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Flink is an open source system for expressive, declarative, fast, and efficient data analysis. Flink combines the scalability and programming flexibility of distributed MapReduce-like platforms with the efficiency, out-of-core execution, and query optimization capabilities found in parallel databases.


<span class="graduated">The Flink project graduated on 2014-12-17</span>



- 2014-08-28 New PPMC: Gyula Fóra

- 2014-08-28 New PPMC: Márton Balassi

- 2014-08-27 Apache Flink 0.6-incubating release

- 2014-07-07 New PPMC: Till Rohrmann

- 2014-04-14 Project enters incubation.


-  [Homepage](http://flink.incubator.apache.org) 


-  [How to contribute](http://flink.incubator.apache.org/how-to-contribute.html) 


-  [Materials](http://flink.incubator.apache.org/material.html) 

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://flink.incubator.apache.org/](http://flink.incubator.apache.org/)  |
| Wiki | wiki |  [https://cwiki.apache.org/confluence/display/FLINK](https://cwiki.apache.org/confluence/display/FLINK)  |
| Mailing list | user |  `user`  `@`  `flink.incubator.apache.org`  |
| . | dev |  `dev`  `@`  `flink.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `flink.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `flink.incubator.apache.org`  |
| . | private |  `private`  `@`  `flink.incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/FLINK](https://issues.apache.org/jira/browse/FLINK)  |
| Source code | git |  [https://gitbox.apache.org/repos/asf/incubator-flink.git](https://gitbox.apache.org/repos/asf/incubator-flink.git)  |
| . | Git web |  [https://gitbox.apache.org/repos/asf?p=incubator-flink.git;a=summary](https://gitbox.apache.org/repos/asf?p=incubator-flink.git;a=summary)  |
| Mentors | gates | Alan Gates |
| . | srowen | Sean Owen |
| . | tdunning | Ted Dunning |
| . | hsaputra | Henry Saputra |
| . | hashutosh | Ashutosh Chauhan |
| . | omalley | Owen O'Malley |
| Committers | sewen | Stephan Ewen |
| . | fhueske | Fabian Hueske |
| . | warneke | Daniel Warneke |
| . | rmetzger | Robert Metzger |
| . | uce | Ufuk Celebi |
| . | aljoscha | Aljoscha Krettek |
| . | ktzoumas | Kostas Tzoumas |
| . | ssc | Sebastian Schelter |
| . | trohrmann | Till Rohrmann |
| . | gyfora | Gyula Fóra |
| . | mbalassi | Márton Balassi |


-  [May 2014](https://wiki.apache.org/incubator/May2014) 

-  [June 2014](https://wiki.apache.org/incubator/June2014) 

-  [July 2014](https://wiki.apache.org/incubator/July2014) 

-  [August 2014](http://wiki.apache.org/incubator/August2014) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2014-07-04 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html) .<br></br>Resolved via [PODLINGNAMESEARCH-49](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-49) . |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2014-06-07 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2014-04-17 | Ask infrastructure to set up and archive mailing lists. |
| 2014-05-20 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2014-07-28 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2014-07-28 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2014-04-30 | Subscribe all Mentors on the pmc and general lists. |
| 2014-06-14 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2014-08-01 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2014-06-06 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2014-07-14 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2014-07-24 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2014-07-24 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2014-04-30 | Check that all active committers have submitted a contributors agreement. |
| 2014-04-17 | Add all active committers in the STATUS file. |
| 2014-04-30 | Ask root for the creation of committers' accounts on people.apache.org. |

## Project specific {#Project+specific}


| date | item |
|------|------|
| 2014-05-14 | Stratosphere voted to change the project name to Flink |



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
