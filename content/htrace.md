Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


HTrace is a tracing framework intended for use with distributed systems written in java.


<span class="retired">The HTrace podling retired on 2018-04-11</span>



- 2018-04-11 The HTrace podling retired on 2018-04-11

- 2016-10-05 PPMC: Mike Drob

- 2016-03-08 GSoC Mentor: Colin McCabe

- 2016-03-04 Apache HTrace 4.1.0 release

- 2015-09-26 Apache HTrace 4.0.1 release

- 2015-09-14 Apache HTrace 4.0.0 release

- 2015-06-03 Apache HTrace 3.2.0 release

- 2015-02-11 PPMC: Abraham Elmahrek

- 2014-11-11 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www | Original: [http://htrace.org/](http://htrace.org/) Podling: [http://htrace.incubator.apache.org/](http://htrace.incubator.apache.org/)  |
| . | wiki | . |
| Mailing list | dev |  `dev`  `@`  `htrace.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `htrace.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `htrace.incubator.apache.org`  |
| . | private |  `private`  `@`  `htrace.incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/HTRACE](https://issues.apache.org/jira/browse/HTRACE)  |
| Source code | Git |  [https://gitbox.apache.org/repos/asf?p=incubator-htrace.git](https://gitbox.apache.org/repos/asf?p=incubator-htrace.git)  |
| Mentors | rvs | Roman Shaposhnik |
| . | jfarrell | Jake Farrell |
| . | todd | Todd Lipcon |
| . | lewismc | Lewis John McGibbney |
| . | billie | Billie Rinaldi |
| . | stack | Michael Stack |
| Committers | . | . |
| . | cmccabe | Colin McCabe |
| . | eclark | Elliott Clark |
| . | leavitt | Jonathan Leavitt |
| . | iwasakims | Masatake Iwasaki |
| . | stack | Michael Stack |
| . | ndimiduk | Nick Dimiduk |
| . | todd | Todd Lipcon |
| Extra | . | . |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2014-11-11 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html) DONE |
| 2014-11-11 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names: N/A. |
| 2014-11-11 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance: N/A. |
| 2014-11-11 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. DONE |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2014-11-11 | Ask infrastructure to create source repository modules and grant the committers karma. DONE by Jake Farrell in [INFRA-8608](https://issues.apache.org/jira/browse/INFRA-8608)  |
| 2014-11-11 | Ask infrastructure to set up and archive mailing lists. DONE by Jake Farrell in [INFRA-8608](https://issues.apache.org/jira/browse/INFRA-8608)  |
| 2014-11-11 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). DONE by Jake Farrell in [INFRA-8608](https://issues.apache.org/jira/browse/INFRA-8608)  |
| 2014-11-11 | Ask infrastructure to set up wiki (Confluence, Moin). NONE asked for. |
| 2014-12-10 | Project src migrated to Apache. Software grant email, [[IP CLEARANCE] Software grant for htrace (incubating), a tracing framework for use with distributed systems written in java](https://mail-archives.apache.org/mod_mbox/incubator-general/201412.mbox/%3CCADcMMgFEWeSS9PdaNh94ahgZaW%2BrtK19EX4rNqSagSj%3DmuzaBQ%40mail.gmail.com%3E) . |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2014-11-11 | Subscribe all Mentors on the pmc and general lists. DONE by Jake Farrell |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' DONE by Jake Farrell |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2014-12-02 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. DONE: See [[IP CLEARANCE] Software grant for htrace (incubating), a tracing framework for use with distributed systems written in java](https://mail-archives.apache.org/mod_mbox/incubator-general/201412.mbox/%3CCADcMMgFEWeSS9PdaNh94ahgZaW%2BrtK19EX4rNqSagSj%3DmuzaBQ%40mail.gmail.com%3E)  |
| 2014-12-02 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. DONE. Migraged src runs RAT check as part of build. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. ONGOING |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. ONGOING |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. ONGOING. All but Mastake have filed icla or already have an apache id. |
| ....-..-.. | Add all active committers in the STATUS file. TODO |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. DONE except for Masatake. Waiting on icla. |

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
