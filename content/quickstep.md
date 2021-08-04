Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Quickstep is a high-performance database engine. It is designed to (1) convert data to insights at bare-metal speed, (2) support multiple query surfaces including SQL (the first, and current, version only supports SQL), and (3) deliver bare-metal performance on any hardware (including running on a laptop, running on a high-end (single node) server, and running on a distributed cluster). Since its inception, the project has been planned to deliver a high-performance single node system first, followed by a distributed system.


<span class="retired">The Quickstep podling retired on 2018-12-01</span>

.

- 2016-03-29 Project enters incubation.


-  [Apache Quickstep (incubating) website](http://quickstep.incubator.apache.org) 


-  [How to contribute to Apache Quickstep (incubating)](https://cwiki.apache.org/confluence/display/QUICKSTEP/) 

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://quickstep.incubator.apache.org/](http://quickstep.incubator.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/QUICKSTEP](https://cwiki.apache.org/confluence/display/QUICKSTEP)  |
| Mailing list | dev |  `dev`  `@`  `quickstep.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `quickstep.incubator.apache.org`  |
| . | user |  `user`  `@`  `quickstep.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `quickstep.incubator.apache.org`  |
| . | private |  `private`  `@`  `quickstep.incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/QUICKSTEP](https://issues.apache.org/jira/browse/QUICKSTEP)  |
| Source code | GIT |  [https://gitbox.apache.org/repos/asf/incubator-quickstep.git](https://gitbox.apache.org/repos/asf/incubator-quickstep.git)  |
| . | GitHub mirror |  [http://github.com/apache/incubator-quickstep](http://github.com/apache/incubator-quickstep)  |
| . | Website content and docs |  [https://svn.apache.org/repos/asf/incubator/quickstep](https://svn.apache.org/repos/asf/incubator/quickstep)  |
| Mentors | cos | Konstantin Boudnik |
| . | jhyde | Julian Hyde |
| . | rvs | Roman Shaposhnik |
| Committers | . | Jignesh M. Patel |
| . | cos | Konstantin Boudnik |
| . | . | Harshad Deshmukh |
| . | . | Jianqiao Zhu |
| . | . | Zuyu Zhang |
| . | . | Marc Spehlmann |
| . | . | Saket Saurabh |
| . | . | Hakan Memisoglu |
| . | . | Rogers Jeffrey |
| . | . | Leo John |
| . | . | Adalbert Gerald |
| . | . | Soosai Raj |
| . | . | Udip Pant |
| . | . | Siddharth Suresh |
| . | . | Rathijit Sen |
| . | . | Craig Chasseur |
| . | . | Qiang Zeng |
| . | . | Shoban Chandrabose |
| . | . | Navneet Potti |
| . | . | Yinan Li |
| . | . | Sangmin Shin |
| . | . | James Paton |
| . | . | Shixuan Fan |
| . | rvs | Roman Shaposhnik |
| . | jhyde | Julian Hyde |
| . | dhruba | Dhruba Borthakur |


-  [May 2016](http://wiki.apache.org/incubator/May2016) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2016-04-11 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2016-04-11 | Ask infrastructure to create source repository modules and grant the committers karma. Tracking via [INFRA-11645](https://issues.apache.org/jira/browse/INFRA-11645)  |
| 2015-04-11 | Ask infrastructure to set up and archive mailing lists. |
| 2015-04-11 | Ask infrastructure to set up issue tracker (JIRA). |
| 2015-04-11 | Ask infrastructure to set up wiki (Confluence). |
| 2015-04-11 | Ask infrastructure to set up svn pubsub website. |
| ....-..-.. | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2016-04-11 | Subscribe all Mentors on the pmc and general lists. |
| 2016-04-11 | Give all Mentors access to the incubator Git repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2016-04-11 | Tell Mentors to track progress in the file 'incubator/projects/quickstep.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2015-04-12 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2015-04-12 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |
| ....-..-.. | The Apache RAT check was added to check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2016-04-12 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2016-04-12 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| 2016-04-11 | Add all active committers in the podling description file. |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

## Project specific {#Project+specific}

| date | item |
|------|------|
| ....-..-.. | Produce first Apache Incubating release. |

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

| date | item |
|------|------|
| ....-..-.. | Figure out how to publish project documentation. |

# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
