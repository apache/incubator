Title: Isis Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Isis project graduated on 2012-10-17</span>


The Isis project will be an extensible standards-based framework to rapidly develop and enterprise level deploy domain-driven (DDD) applications.



- 2012-10-17 Isis graduates from the incubator

- 2012-09-24 New committer: Jeroen van der Wal

- 2012-02-20 Released version 0.2.0-incubating

- 2011-07-14 Released version 0.1.2-incubating

- 2010-09-07 Isis has been accepted to enter incubation

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://isis.apache.org/](http://isis.apache.org/) <br></br>previously: [http://incubator.apache.org/isis/](http://incubator.apache.org/isis/)  |
| . | wiki |  [http://cwiki.apache.org/confluence/display/Isis/](http://cwiki.apache.org/confluence/display/Isis/)  |
| Mailing list | dev |  `dev`  `@`  `isis.apache.org` <br></br>previously: `isis-dev`  `@`  `incubator.apache.org`  |
| Mailing list | users |  `users`  `@`  `isis.apache.org` <br></br>previously: `isis-users`  `@`  `incubator.apache.org`  |
| . | commits |  `commits`  `@`  `isis.apache.org` <br></br>previously: `isis-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/ISIS](https://issues.apache.org/jira/browse/ISIS)  |
| Source code | GIT |  [https://gitbox.apache.org/repos/asf/isis.git](https://gitbox.apache.org/repos/asf/isis.git) <br></br>previously: [https://svn.apache.org/repos/asf/incubator/isis/](https://svn.apache.org/repos/asf/incubator/isis/)  |
| People | . | See below |

The project team consists of:


| apache id | name | mentor? | ppmc? | committer? | alumni? |
|-----------|------|---------|-------|------------|---------|
| struberg | Mark Struberg | Y | Y | Y | . |
| bimargulies | Benson Margulies | Y | Y | Y | . |
| sgoeschl | Siegfried Goeschl | Y | Y | Y | . |
| mnour | Mohammad Nour El-Din | Y | Y | Y | . |
| danhaywood | Daniel Keir Haywood | . | Y | Y | . |
| kevin | Kevin Meyer | . | Y | Y | . |
| rmatthews | Robert Charles Matthews | . | Y | Y | . |
| dslaughter | David Slaughter | . | Y | Y | . |
| themalkolm | Alexander Krasnukhin | . | Y | Y | . |
| jcvanderwal | Jeroen van der Wal | . | Y | Y | . |
| uli | Ulrich Stärk | . | . | Y | . |


-  [September 2012](http://wiki.apache.org/incubator/September2012#Isis) 

-  [June 2012](http://wiki.apache.org/incubator/June2012#Isis) 

-  [March 2012](http://wiki.apache.org/incubator/March2012#Isis) 

-  [December 2011](http://wiki.apache.org/incubator/December2011#Isis) 

-  [September 2011](http://wiki.apache.org/incubator/September2011#Isis) 

-  [June 2011](http://wiki.apache.org/incubator/June2011#Isis) 

-  [March 2011](http://wiki.apache.org/incubator/March2011#Isis) 

-  [December 2010](http://wiki.apache.org/incubator/December2010#Isis) 

-  [November 2010](http://wiki.apache.org/incubator/November2010#Isis) 

-  [October 2010](http://wiki.apache.org/incubator/October2010#Isis) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2010-09-21 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.<br></br> **STATUS: Done** . Made sure that both **Isis** and **Apache Isis** are not used. |
| n/a | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names<br></br> **STATUS: not applicable** . |
| n/a | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance.<br></br> **STATUS: not applicable** . |
| 2010-09-07 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted.<br></br> **STATUS: not applicable** ; see [mailing list thread](http://mail-archives.apache.org/mod_mbox/incubator-general/201009.mbox/%3C4C85C4FE.4050104@gmail.com%3E)  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-09-28 | Ask infrastructure to create source repository modules and grant the committers karma.<br></br>(see [INFRA-2996](http://issues.apache.org/jira/browse/INFRA-2996) and [INFRA-3000](http://issues.apache.org/jira/browse/INFRA-3000) ) |
| 2010-09-09 | Ask infrastructure to set up and archive mailing lists.<br></br>(see [INFRA-2971](http://issues.apache.org/jira/browse/INFRA-2971) ) |
| 2010-09-21 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla).<br></br>(see [INFRA-2997](http://issues.apache.org/jira/browse/INFRA-2997) ) |
| 2010-09-21 | Ask infrastructure to set up wiki (Confluence, Moin).<br></br>(see [INFRA-3001](http://issues.apache.org/jira/browse/INFRA-3001) ) |
| 2010-10-20 | Migrate the project to our infrastructure.<br></br>(see [INFRA-2972)](https://issues.apache.org/jira/browse/INFRA-2972) umbrella ticket and in particular the [INFRA-3066](https://issues.apache.org/jira/browse/INFRA-3066) ticket to import code) |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2010-09-01 | Identify all the Mentors for the incubation, by asking all that can be Mentors.<br></br>(see [Vote thread](http://markmail.org/message/5bjv6lt64km7sgys) ) |
| 2010-09-09 | Subscribe all Mentors on the pmc and general lists.<br></br>(see [INFRA-2971](http://issues.apache.org/jira/browse/INFRA-2971) ) |
| 2010-09-28 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-09-21 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html'<br></br>(see [Notification e-mail](http://markmail.org/message/3ygombjswzmhrdwi) ) |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2010-09-26 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-03-18 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright.<br></br>(see [ISIS-1](http://issues.apache.org/jira/browse/ISIS-1) ). |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2011-03-18 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute.<br></br>Done as part of voting on first release, 0.1.2-incubating. |
| 2010-07-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.<br></br>Done as part of [voting](http://mail-archives.apache.org/mod_mbox/incubator-isis-dev/201107.mbox/%3C4E116A0F.8040606%40gmail.com%3E) on first release, 0.1.2-incubating |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-09-26 | Check that all active committers have submitted a contributors agreement.<br></br>(see [Notification e-mail](http://markmail.org/message/pzgwdwwdkpirus7x) , [Confirmation e-mail](http://markmail.org/message/ce2juvqaoodd7rou) for Alexander Krasnukhin, [Confirmation e-mail](http://markmail.org/message/3xmotalfldq63mis) for David Slaughter) |
| 2010-10-18 | Add all active committers in the STATUS file.<br></br>(see [ISIS-2](http://issues.apache.org/jira/browse/ISIS-2) ) |
| 2010-10-05 | Ask root for the creation of committers' accounts on people.apache.org.<br></br>(see [INFRA-3000](http://issues.apache.org/jira/browse/INFRA-3000) ) |

## Project specific {#Project+specific}

 _(none)_ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?<br></br> **YES** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)<br></br> **YES** 

- Are project decisions being made in public by the committers?<br></br> **YES** 

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?<br></br> **YES** 

## Project Specific {#Project+Specific}

 _(none)._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?<br></br> **n/a** 

- If graduating to a new PMC, has the board voted to accept it?<br></br> **YES** 

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?<br></br> **YES** 
