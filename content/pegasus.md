Title: Apache Pegasus Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Pegasus is a distributed key-value storage system which is designed to be simple, horizontally scalable, strongly consistent and high-performance.



- 2020-06-22 Project enters incubation.


- Pegasus Website - http://pegasus.incubator.apache.org


-  [Community Pages](http://pegasus.incubator.apache.org/community/) 

-  [Current Documentation](http://pegasus.incubator.apache.org/docs/) 

-  [Releases](http://pegasus.incubator.apache.org/releases/) 

-  [Wiki](https://cwiki.apache.org/confluence/display/pegasus) 


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://pegasus.incubator.apache.org](http://pegasus.incubator.apache.org)  |
| . | wiki |  [Wiki](https://cwiki.apache.org/confluence/display/pegasus)  |
| Mailing list | dev |  `dev`  `@`  `pegasus.incubator.apache.org`  |
| . | user(not request) |  `user`  `@`  `pegasus.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `pegasus.incubator.apache.org`  |
| . | private |  `private`  `@`  `pegasus.incubator.apache.org`  |
| Bug tracking | . | https://issues.apache.org/jira/projects/PEGASUS |
| Source code | . | . |
| . | incubator-pegasus | https://gitbox.apache.org/repos/asf?p=incubator-pegasus.git |
| . | incubator-pegasus-website | https://gitbox.apache.org/repos/asf?p=incubator-pegasus-website.git |
| Mentors |  | . |
| . | vongosling | Von Gosling |
| . | kmcgrail | Kevin A. McGrail |
| . | zhangduo | Duo zhang |
| . | chenliang613 | Liang Chen |
| Committers | . | . |
| . | cailiuyang | Cai Liuyang |
| . | yuchenhe | He Yuchen |
| . | huangwei | Huang Wei |
| . | jiashuo | Jia Shuo |
| . | sunweijie | Sun Weijie |
| . | wutao | Wu Tao |
| . | laiyingchun | Yingchun Lai |
| . | zhaoliwei | Zhao Liwei |
| . | qinzuoyan | Zuoyan Qin |


-  [Board Reports](https://whimsy.apache.org/board/minutes/pegasus.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2020-06-28 | Request DNS (first step after creating podling status page) |
| 2020-07-01 | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator)  |
| 2020-07-20 | Request git repositories after SGAs are filed |
| N/A | Ask infrastructure to create source repository modules and grant the committers karma (if using SVN) |
| 2020-06-28 | Ask infrastructure to set up issue tracker ( [JIRA](https://selfserve.apache.org/jira.html) , Bugzilla). |
| 2020-06-28 | Ask infrastructure to set up wiki ( [Confluence](https://selfserve.apache.org/confluence.html) ). |
| 2020-08-21 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2020-07-08 | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member with karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/pegasus.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2020-07-14 | Check that all active committers have submitted a contributors agreement. |
| 2020-07-14 | Add all active committers in the STATUS file. |
| 2020-07-14 | Ask root for the creation of committers' accounts on home.apache.org. |

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
