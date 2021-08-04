Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Hivemall is a library for machine learning implemented as Hive UDFs/UDAFs/UDTFs. Hivemall runs on Hadoop-based data processing frameworks, specifically on Apache Hive, Apache Spark, and Apache Pig, that support Hive UDFs as an extension mechanism.



- 2016-09-13 Project enters incubation.


-  [Apache Hivemall (incubating) website](http://hivemall.incubator.apache.org) 


-  [How to contribute to Apache Hivemall (incubating)](https://cwiki.apache.org/confluence/display/HIVEMALL/) 

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://hivemall.incubator.apache.org/](http://hivemall.incubator.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/HIVEMALL](https://cwiki.apache.org/confluence/display/HIVEMALL)  |
| Mailing list | dev |  `dev`  `@`  `hivemall.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `hivemall.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `hivemall.incubator.apache.org`  |
| . | user |  `user`  `@`  `hivemall.incubator.apache.org`  |
| . | private |  `private`  `@`  `hivemall.incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/HIVEMALL](https://issues.apache.org/jira/browse/HIVEMALL)  |
| Source code | GIT |  [https://gitbox.apache.org/repos/asf/incubator-hivemall.git](https://gitbox.apache.org/repos/asf/incubator-hivemall.git)  |
| . | GitHub mirror |  [http://github.com/apache/incubator-hivemall](http://github.com/apache/incubator-hivemall)  |
| . | Website content and docs |  [https://gitbox.apache.org/repos/asf/incubator-hivemall-site.git](https://gitbox.apache.org/repos/asf/incubator-hivemall-site.git)  |
| Mentors | rxin | Reynold Xin |
| . | weimer | Markus Weimer |
| . | meng | Xiangrui Meng |
| . | daijy | Daniel Dai |
| Committers | myui | Makoto Yui |
| . | yamamuro | Takeshi Yamamuro |
| . | daijy | Daniel Dai |
| . | ozawa | Tsuyoshi Ozawa |
| . | lewuathe | Kai Sasaki |
| . | takuti | Takuya Kitazawa |
| . | ri | Ryu-ichi Ito |


-  [September 2016](http://wiki.apache.org/incubator/September2016) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2016-09-14 | Ask infrastructure to create source repository modules and grant the committers karma. Tracking via [INFRA-12608](https://issues.apache.org/jira/browse/INFRA-12608)  |
| 2016-09-14 | Ask infrastructure to set up and archive mailing lists. |
| 2016-09-14 | Ask infrastructure to set up issue tracker (JIRA). |
| 2016-09-14 | Ask infrastructure to set up wiki (Confluence). |
| 2016-09-14 | Ask infrastructure to set up svn pubsub website. |
| 2016-12-01 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator Git repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/hivemall.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |
| ....-..-.. | The Apache RAT check was added to check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the podling description file. |
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
