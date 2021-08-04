Title: Cayenne Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Cayenne project graduated on 2006-12-20</span>


Cayenne is an open source component-oriented persistence framework licensed under the Apache License, providing object-relational mapping (ORM) and remoting services. With a wealth of unique and powerful features, Cayenne can address a wide range of persistence needs. Cayenne seamlessly binds one or more database schemas directly to Java objects, managing atomic commit and rollbacks, SQL generation, joins, sequences, and more. With Cayenne's Remote Object Persistence, those Java objects can even be persisted out to clients via Web Services. Or, with native XML serialization, objects can be even further persisted to non-Java clients - such as an Ajax-capable browser. In addition to this existing functionality, Cayenne is currently building a JPA-compatible persistence provider (JSR-220). In 2001, Cayenne was started as an open source collaborative environment, modeled after ASF. Thus, proposing Cayenne as an ASF project is the logical next step to further expand the community and increase participation.



- 2006-03-06: [DB PMC sponsors Cayenne incubation](http://mail-archives.apache.org/mod_mbox/incubator-general/200603.mbox/%3c224f32340603060804wc46a5acn3d898ae03c2dce7c@mail.gmail.com%3e) 

- 2006-10-07: [Version 2.0.1 released](http://mail-archives.apache.org/mod_mbox/incubator-cayenne-dev/200610.mbox/%3cF97DE912-AF6B-442F-8028-AEF07093A3BE@objectstyle.org%3e) 

- 2006-11-05: [Added new committer: Malcom Edgar](http://objectstyle.org/cayenne/lists/cayenne-devel/2006/11/0009.html) 

- 2006-12-5: [Incubator graduation vote passes.](http://mail-archives.apache.org/mod_mbox/incubator-general/200612.mbox/%3c3F81E767-B20F-471A-8428-58496DADF941@objectstyle.org%3e) 

- 2006-12-20: Board passes proposal to make Cayenne a top level project.

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/cayenne/](http://incubator.apache.org/cayenne/)  |
| Cayenne WIKI | wiki |  [http://cwiki.apache.org/CAY/](http://cwiki.apache.org/CAY/) <br></br> |
| Mailing List | dev | cayenne-dev@incubator.apache.org |
| commits | SCM | cayenne-commits@incubator.apache.org |
| Project Management Committe | PMC | cayenne-private@incubator.apache.org |
| User Mailing List | user | cayenne-user@incubator.apache.org |
| Bug tracking | JIRA<br></br> |  [JIRA at Apache](http://issues.apache.org/cayenne/) <br></br> |
| Source code | svn<br></br> | https://svn.apache.org/repos/asf/incubator/cayenne/ |
| Mentor | <br></br> | Jean T. Anderson<br></br> |
| Mentor | <br></br> | Brian McCallister<br></br> |
| Mentor | <br></br> | Bill Dudney<br></br> |
| Mentor | <br></br> | Jim Jagielski (Retired: 2006-10-20)<br></br> |
| Committers<br></br> | aadamchik | Andrus Adamchik (PPMC May 2006)<br></br> |
| <br></br> | cdaniluk | Cris Daniluk<br></br> |
| <br></br> | bdudney | Bill Dudney (PPMC Mar 2006)<br></br> |
| <br></br> | medgar | Malcolm Edgar<br></br> |
| <br></br> | mgentry | Michael Gentry (PPMC Nov 2006)<br></br> |
| <br></br> | torehalset | Tore Halset (PPMC Oct 2006)<br></br> |
| <br></br> | mkienenb | Mike Kienenberger (PPMC May 2006)<br></br> |
| <br></br> | kmenard | Kevin Menard<br></br> |


-  [March 2006](http://wiki.apache.org/incubator/March2006) 

-  [April 2006](http://wiki.apache.org/incubator/April2006) 

-  [May 2006](http://wiki.apache.org/incubator/May2006) 

-  [June 2006](http://wiki.apache.org/incubator/June2006) 

-  [September 2006](http://wiki.apache.org/incubator/September2006) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated&amp;#xD; {#Identify+the+project+to+be+incubated%26%23xD%3B}

| date | item |
|-------|-------|
| Done - 2006-03-13 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| Done 2006-02-25 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| Done 2006-03-13 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| Done - 2006-02-28 | Subscribe all Mentors on the pmc and general lists. |
| Done - 2006-03-13 | Give all Mentors access to the incubator SVN repository. (to be done by PMC chair) |
| Done - 2006-04-24 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| Done - 2006-09-15 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| Done - 2006-04-14 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| Done 2006-10-05 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| Done 2006-10-05 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| Done 2006-04-14 | Check that all active committers have submitted a contributors agreement. |
| Done 2006-05-08 | Add all active committers in the STATUS file. |
| Done 2006-04-19 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| Done 2006-04-14 | Ask infrastructure to create source repository modules and grant the committers karma. |
| Done 2006-03-16 | Ask infrastructure to set up and archive Mailing lists. |
| Done 2006-04-15 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| Done 2006-07-22 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? **YES.** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) **YES. All eight committers are independent of each other -- the Cayenne project originally began as an open source project before coming into the Incubator, so the committers have been independent from the beginning.** 

- Are project decisions being made in public by the committers? **YES.** 

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? **YES.** 

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it? **N/A** 

- If graduating to a new PMC, has the board voted to accept it? **2006-12-20** 

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? ** [2006-12-05](http://mail-archives.apache.org/mod_mbox/incubator-general/200612.mbox/%3c3F81E767-B20F-471A-8428-58496DADF941@objectstyle.org%3e) ** 
