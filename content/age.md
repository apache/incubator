Title: Apache AGE Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page track the project status incubator-wise. For more general project status, look on the project website.


AGE is a multi-model database that enables graph and relational models built on PostgreSQL.This project is a new generation of a multi-model graph database for the modern complex data environment.



- 2020-04-30 Project enters incubation.

- 2021/03/19 New Committer, Dehowe Feng

- 2021-02-19 First Apache AGE release v0.3.0.

- 2021-05-03 First Apache AGE release v0.4.0.


- AGE Website - http://age.incubator.apache.org


-  [Current Documentation](https://age.apache.org/docs/Apache_AGE_Guide.pdf) 

-  [Releases](https://dist.apache.org/repos/dist/release/incubator/age/) 

-  [Wiki](https://cwiki.apache.org/confluence/display/INCUBATOR/AGE) 


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://age.incubator.apache.org](http://age.incubator.apache.org)  |
| . | wiki |  [Wiki](https://cwiki.apache.org/confluence/display/age)  |
| Mailing list | dev |  `dev`  `@`  `age.incubator.apache.org`  |
| . | user |  `user`  `@`  `age.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `age.incubator.apache.org`  |
| . | private |  `private`  `@`  `age.incubator.apache.org`  |
| Bug tracking | . | https://issues.apache.org/jira/browse/ageold |
| Source code | incubator-age | https://github.com/apache/incubator-age |
| . | incubator-age-website | https://github.com/apache/incubator-age-website |
| . | incubator-age | https://gitbox.apache.org/repos/asf?p=incubator-age.git |
| . | incubator-age-website | https://gitbox.apache.org/repos/asf?p=incubator-age-website.git |
| Mentors |  | . |
| . | jim | Jim Jagielski |
| . | djkevincr | Kevin Ratnasekera |
| . | vongosling | Von Gosling |
| . | rbircher | Raphael Bircher |
| . | felixcheung | Felix Cheung |
| Committers |  |
| . | jgemignani | John Gemignani |
| . | jinnis | Josh Innis |
| . | eyab | Eya Badal |
| . | dehowef | Dehowe Feng |


-  [Board Reports](https://whimsy.apache.org/board/minutes/age.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2020-07-21 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2020-06-25 | Request DNS (first step after creating podling status page) |
| 2020-06-25 | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator)  |
| 2020-06-25 | Request [git repositories](https://reporeq.apache.org/)  |
| 2020-06-25 | Ask infrastructure to create source repository modules and grant the committers karma (if using SVN) |
| 2020-02-20 | Ask infrastructure to set up issue tracker ( [JIRA](https://selfserve.apache.org/jira.html) , Bugzilla). |
| 2020-06-25 | Ask infrastructure to set up wiki ( [Confluence](https://selfserve.apache.org/confluence.html) ). |
| 2020-07-29 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2020-08-05 | Subscribe all Mentors on the pmc and general lists. |
| 2020-08-05 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member with karma for the authorizations file) |
| 2020-08-05 | Tell Mentors to track progress in the file 'incubator/projects/age.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2020-07-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2020-07-07 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2020-03-20 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2020-03-20 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2020-05-17 | Check that all active committers have submitted a contributors agreement. |
| 2020-09-02 | Add all active committers in the STATUS file. |
| N/A | Ask root for the creation of committers' accounts on home.apache.org. |

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
