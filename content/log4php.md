Title: log4php


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Log4php project graduated on 2010-03-07</span>


The Log4php project restarted on 2007-07-04 with a new development team. It implements a logging API similar to log4j but in PHP.



- 2010-03-07 - Log4PHP graduated to a sub-project of Logging PMC

- 2009-10-08 - New Committer: Christian Hammers

- 2009-04-28 - New Committer: Christian Grobmeier

- 2009-04-28 - New Committer: Gavin McDonald

- 2009-04-28 - New Mentor: Niclas Hedhman

- 2009-04-28 - New Mentor: Gavin McDonald

- 2007-07-04 - The Log4php project reentered incubation with a new development team.

- 2007-02-17 - The Log4php project was retired from incubation due to lack of community momentum.

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://logging.apache.org/log4php/](http://logging.apache.org/log4php/)  |
| Mailing list | dev |  [log4php-dev@logging.apache.org](mailto:log4php-dev@logging.apache.org) [ [Subscribe](log4php-dev-subscribe@logging.apache.org) | [Unsubscribe](log4php-dev-unsubscribe@logging.apache.org) ] |
| Mailing list | commits |  `log4php-dev`  `@`  `logging.apache.org`  |
| Mailing list | user |  [log4php-user@logging.apache.org](mailto:log4php-user@logging.apache.org) [ [Subscribe](log4php-user-subscribe@logging.apache.org) | [Unsubscribe](log4php-user-unsubscribe@logging.apache.org) ] |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/LOG4PHP](https://issues.apache.org/jira/browse/LOG4PHP)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/logging/log4php/trunk](https://svn.apache.org/repos/asf/logging/log4php/trunk)  |
| Mentor | gmcdonald | Gavin McDonald |
| Mentor | niclas | Niclas Hedhman |
| Mentor | jim | Jim Jagielski |
| Committer | alvero | Alvero Carrasco |
| Committer | kurdalen | Knut Urdalen |
| Committer | grobmeier | Christian Grobmeier |
| Committer | gmcdonald | Gavin McDonald |
| Committer | chammers | Christian Hammers |


- Status Reports due March, June, September, December

Status reports are held on the Incubator Wiki site:



-  [June 2009](http://wiki.apache.org/incubator/June2009) 

-  [September 2009](http://wiki.apache.org/incubator/September2009) 

-  [December 2009](http://wiki.apache.org/incubator/December2009) 

-  [March 2010](http://wiki.apache.org/incubator/March2010) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated [done] {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-01-15 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| 2004-01-15 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| 2004-01-06 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility [done] {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-01-22 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2004-01-22 | Subscribe all Mentors on the pmc and general lists. |
| 2004-01-22 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2004-01-22 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright [done] {#Copyright}

| date | item |
|-------|-------|
| 2004-02-05 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-02-05 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights [done] {#Verify+distribution+rights}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2004-06-14 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers [done] {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| 2004-01-22 | Check that all active committers have submitted a contributors agreement. |
| 2004-01-22 | Add all active committers in the STATUS file. |
| 2004-01-22 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure [done] {#Infrastructure}

| date | item |
|-------|-------|
| 2004-01-22 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2004-01-22 | Ask infrastructure to set up and archive Mailing lists. |
| ....-..-.. | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2004-01-22 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation [done] {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._ 


 _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?


- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)


- Are project decisions being made in public by the committers?


- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit [done] {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
