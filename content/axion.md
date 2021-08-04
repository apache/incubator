Title: Axion Project Incubation Status
<version>$Revision: 1.4 $ $Date: 2014-03-27 23:51:21 +0000 (Thu, 27 Mar 2014) $</version>

Axion is a Java-based relational database engine.


This page tracks Axion's incubation status. For general project status, see the Axion project website.


<span class="retired">The Axion project retired on 2006-01-23</span>


# Incubation Related {#Incubation+Related}



2006-01-23
 [Cancelled at request of Sponsoring TLP. The axion project never moved to the ASF from tigris.org.](http://mail-archives.apache.org/mod_mbox/incubator-general/200601.mbox/%3cB94F91F8-4E42-4336-B9C6-B06D63BC8BF0@apache.org%3e) 


2003-12-19
The [Apache Incubator Project](http://incubator.apache.org/) has acknowledged Axion's acceptance by the [Apache Database Project](http://db.apache.org/) . Incubation is officially underway.

2003-12-02
The [Apache Database Project](http://db.apache.org/) has accepted Axion's proposal. Send message to [general-thread.243@db.apache.org](mailto:general-thread.243@db.apache.org) to retrieve the VOTE thread, and to [general-thread.257@db.apache.org](mailto:general-thread.247@db.apache.org) to retrieve the RESULT thread. Morgan Delegrange has [volunteered](http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=720) to act as "mentor".

2003-11-04
Axion team [has voted](http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=697) to move the [Apache Database Project](http://db.apache.org/) .
# Project Related {#Project+Related}

Currently, see [http://axion.tigris.org/news.html](http://axion.tigris.org/news.html) for project related news.


| item | type | reference |
|-------|-------|------------|
| Website | www | Currently [http://axion.tigris.org/](http://axion.tigris.org/) . Eventually [http://db.apache.org/axion/](http://db.apache.org/axion/) . |
| Mailing List | dev | axion-dev@db.apache.org (deprecated: dev@axion.tigris.org) |
|   | user | axion-user@db.apache.org (deprecated: users@axion.tigris.org) |
|   | cvs | axion-dev@db.apache.org (deprecated: cvs@axion.tigris.org) |
| Issue Database |   | Currently [http://axion.tigris.org/servlets/ProjectIssues](http://axion.tigris.org/servlets/ProjectIssues) . Soon Bugzilla? Jira? To be determined. |
| Source Repository | CVS | Currently [http://axion.tigris.org/source/browse/axion/](http://axion.tigris.org/source/browse/axion/) . Soon [db-axion](http://cvs.apache.org/viewcvs/db-axion) . |
| Mentors |   | Morgan Delegrange (morgand@apache) |
| Committers |   | For now, see [http://axion.tigris.org/servlets/ProjectMemberList](http://axion.tigris.org/servlets/ProjectMemberList)  |

ToDo: Add links here.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date completed | item |
|-----------------|-------|
| 2003-12-19 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.<br></br> **Done.**  _As of 19 December 2003, nothing seems relevant ( [try it yourself](http://nameprotect.com/cgi-bin/FREESearch/search.cgi?action=SEARCH&amp;db=PTO&amp;ss=axion) ). Note that "axion" is [a scientific term](http://www.m-w.com/cgi-bin/dictionary?axion) ._  |
| 2003-12-02 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names.<br></br> **Done.**  _Send a message to [general-thread.243@db.apache.org](mailto:general-thread.243@db.apache.org) to retrieve the VOTE thread, and to [general-thread.257@db.apache.org](mailto:general-thread.247@db.apache.org) to retrieve the RESULT thread._  |
| 2003-11-04 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance.<br></br> **Done.**  _See [http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=697](http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=697) ._  |

## Interim responsibility {#Interim+responsibility}

| date completed | item |
|-----------------|-------|
| 2003-12-03 | Identify all the Mentors for the incubation, by asking all that can be Mentors.<br></br> **Done.**  _See [http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=720](http://axion.tigris.org/servlets/ReadMsg?list=dev&amp;msgNo=720) ._  |
| 2003-12-19 | Subscribe all Mentors on the pmc and general lists.<br></br> **Done.**  |
| 2003-12-19 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair)<br></br> **Done.**  |
| 2003-12-19 | Tell Mentors to track progress in the file `incubator/projects/{project.name}.cwiki
` <br></br> **Done.**  _Using `incubator/projects/axion.xml
` instead, since Forrest's cwiki parser seems to be broken._  |

## Copyright {#Copyright}

| date completed | item |
|-----------------|-------|
| Submitted 16-July-2004 | Check that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.<br></br>(Fax submitted 16-July-2004. Not yet acknowledged.) |
|   | Check that the files that have been donated have been updated to reflect the new ASF copyright.<br></br> |

## Verify distribution rights {#Verify+distribution+rights}

| date completed | item |
|-----------------|-------|
| 2003-12-19 | Check that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute.<br></br> **Done.**  _All code currently distributed by the project is already available under an ASF-like license. See [Axion's original license](http://axion.tigris.org/unbranded-source/browse/*checkout*/axion/LICENSE.txt?rev=HEAD) . This will be changed to the ASF license when the copyright is transfered (see [above](#copyright) )._  |
| 2003-12-19 | Check that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.<br></br> **Done.**  _All code currently distributed by the project is already available under an ASF-like license. See [Axion's original license](http://axion.tigris.org/unbranded-source/browse/*checkout*/axion/LICENSE.txt?rev=HEAD) . This will be changed to the ASF license when the copyright is transfered (see [above](#copyright) )._  |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date completed | item |
|-----------------|-------|
|   | Check that all active committers have submitted a contributors agreement. |
|   | Add all active committers in the STATUS file. |
|   | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure {#Infrastructure}

| date completed | item |
|-----------------|-------|
| 2004-06-14 | Ask infrastructure to create source repository modules and add the committers to the avail file.<br></br> **Done.**  |
| 2004-06-14 | Ask infrastructure to set up and archive Mailing lists.<br></br> **Done.**  |
|   | Decide about and then ask infrastructure to setup an issue tracking system (Bugzilla, Scarab, Jira). |
|   | Migrate the project to our infrastructure.<br></br> _As previously discussed, waiting on final Milestone 3 release from Tigris._  |

# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


> These items are not to be signed as done during incubation, as they may change during incubation. They are to be looked into and described in the status reports and completed in the request for incubation signoff.

## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- Are project decisions being made in public by the committers?

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

# Exit {#Exit}

Things to check for before voting the project out.


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}



If graduating to an existing PMC, has the PMC voted to accept it?
 _Yes. Send a message to [general-thread.243@db.apache.org](mailto:general-thread.243@db.apache.org) to retrieve the VOTE thread, and to [general-thread.257@db.apache.org](mailto:general-thread.247@db.apache.org) to retrieve the RESULT thread._ 
## Incubator sign-off {#Incubator+sign-off}



Has the Incubator decided that the project has accomplished all of the above tasks?
 