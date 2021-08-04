Title: Apache YuniKorn Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


YuniKorn is a standalone resource scheduler responsible for scheduling batch jobs and long-running services on large scale distributed systems running in on-premises environments as well as different public clouds.



- 2021-07-07 New Committer, Manikandan R

- 2021-07-07 New PPMC member, Kinga Marton

- 2021-04-09 Apache YuniKorn v0.10.0 released.

- 2021-02-03 New Committer, TingYao Huang

- 2020-09-22 New Committer, Kinga Marton

- 2020-08-26 Apache YuniKorn v0.9.0 released.

- 2020-06-16 New Committer, Li Gao

- 2020-05-04 First Apache YuniKorn release v0.8.0.

- 2020-04-01 Published yunikorn website.

- 2020-03-27 Changed JIRA and GitHub email notification lists.

- 2020-01-21 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://yunikorn.apache.org/](http://yunikorn.apache.org/)  |
| Mailing list | dev |  `dev`  `@`  `yunikorn.apache.org`  |
| . | private |  `private`  `@`  `yunikorn.apache.org`  |
| . | issues |  `issues`  `@`  `yunikorn.apache.org`  |
| . | reviews |  `reviews`  `@`  `yunikorn.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/projects/YUNIKORN/issues](https://issues.apache.org/jira/projects/YUNIKORN/issues)  |
| Source code | incubator-yunikorn-core | https://github.com/apache/incubator-yunikorn-core.git |
| . | incubator-yunikorn-k8shim | https://github.com/apache/incubator-yunikorn-k8shim.git |
| . | incubator-yunikorn-scheduler-interface | https://github.com/apache/incubator-yunikorn-scheduler-interface.git |
| . | incubator-yunikorn-web | https://github.com/apache/incubator-yunikorn-web.git |
| . | incubator-yunikorn-site | https://github.com/apache/incubator-yunikorn-site.git |
| Roster | people.apache |  [YUNIKORN Roster](http://people.apache.org/phonebook.html?podling=yunikorn)  |
| Mentors | junping_du | Junping Du |
| . | felixcheung | Felix Cheung |
| . | jlowe | Jason Lowe |
| . | holden | Holden Karau |
| Committers | akhilpb | Akhil PB |
| . | asuresh | Arun Suresh |
| . | curino | Carlo Curino |
| . | dbtsai | DB Tsai |
| . | jhung | Jonathan Hung |
| . | kingamarton | Kinga Marton |
| . | kkaranasos | Konstantinos Karanasos |
| . | ligao | Li Gao |
| . | mani | Manikandan R |
| . | subru | Subramaniam Krishnan |
| . | sunilg | Sunil G |
| . | taoyang | Tao Yang |
| . | tingyao | TingYao Huang |
| . | vinodkv | Vinod Kumar Vavilapalli |
| . | wangda | Wangda Tan |
| . | wwei | Weiwei Yang |
| . | wilfreds | Wilfred Spiegelenburg |


-  [YuniKorn Board Reports](https://whimsy.apache.org/board/minutes/yunikorn.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2020-01-29 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2020-01-29 | Request DNS (first step after creating podling status page) |
| 2020-01-29 | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator) Completed |
| 2020-02-01 | Request [git repositories](https://reporeq.apache.org/) Completed |
| 2020-01-29 | Ask infrastructure to set up issue tracker ( [JIRA](https://selfserve.apache.org/jira.html) , Bugzilla). Completed |
| N/A | Ask infrastructure to set up wiki ( [Confluence](https://selfserve.apache.org/confluence.html) ). Not Required |
| 2020-02-04 | Migrate the project to our infrastructure. Completed |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2020-03-28 | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator Git repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/yunikorn.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2020-02-04 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2020-05-04 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2020-02-04 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2020-02-04 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2020-02-15 | Check that all active committers have submitted a contributors agreement. |
| 2020-03-12 | Add all active committers in the relevant section above. |
| 2020-02-15 | Ask root for the creation of committers' accounts in LDAP. |

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
