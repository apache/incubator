Title: muse


This page tracks the project status, incubator-wise.


<span class="graduated">The Muse project graduated on 2005-06-03</span>


A Web Services subproject that provides an implementation of the OASIS Web Services Distributed Management (WSDM) family of specifications.



- 2005-06-03 - Incubator PMC voted to graduate Muse

- 2004-11-08 - Proposal sent to incubator general mailing list

- 2004-10-14 - Proposal accepted by WS PMC

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/muse/](http://incubator.apache.org/muse/)  |
| Proposal | wiki |  [http://wiki.apache.org/incubator/MuseProposal](http://wiki.apache.org/incubator/MuseProposal)  |
| Mailing Lists | dev |  [muse-dev@ws.apache.org](mailto:muse-dev@ws.apache.org)  |
| . | svn |  [muse-cvs@incubator.apache.org](mailto:muse-cvs@incubator.apache.org)  |
| Bug Tracking | jira |  [http://nagoya.apache.org/jira/secure/project/ViewProject.jspa?pid=1061](http://nagoya.apache.org/jira/secure/project/ViewProject.jspa?pid=10614)  |
| Source Code | svn |  [https://svn.apache.org/repos/asf/incubator/muse/](https://svn.apache.org/repos/asf/incubator/muse/)  |
| Mentors | dims | Davanum Srinivas |
| Committers | gawor | Jarek Gawor |
| . | ips | Ian Springer |
| . | kidz | Kinga Dziembowski |
| . | meder | Sam Meder |
| . | scamp | Sal Campana |
| . | wire | Bill Reichardt |


- 2005-06-03 - Incubator PMC voted to graduate Muse

- 2005-05-25 - A 1.0 beta release of Muse was released today. For a description of the features included in this release, see the [release announcement](http://marc.theaimsgroup.com/?l=muse-dev&amp;m=111711591011814&amp;w=2) . This release contains all of the features that are planned for v1.0. The plan is to spend the next 6-8 weeks bolstering documentation and unit test coverage, i18nizing all messages, and fixing any bugs that are reported.

- 2005-04-21 - Kinga Dziembowski was voted in as a committer.

- 2004-12-01 - The community has decided to cut a 0.5 beta release. The release will follow the incubation release rules, which require:


1. incubator disclaimer in README and from any download links

1. dist filename to include "incubating"

1. ppmc vote (providing the incubator pmc approval, since all interested incubator pmc members should be on the webservices ppmc mailing list)

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2005-04-18 | Make sure that the requested project name does not already exist and check http://www.nameprotect.com/ to be sure that the name is not already trademarked for an existing software product. |
| 2004-11-04 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-11-04 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2004-11-04 | Subscribe all Mentors on the pmc and general lists. |
| 2004-11-04 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2004-11-04 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2005-01-05 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-11-04 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2005-04-26 | Check and make sure that all code included with the distribution that is not under the Apache license has the right to combine with Apache-licensed code and redistribute. |
| 2005-04-21 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2004-11-08 | Check that all active committers have submitted a contributors agreement. |
| 2004-11-08 | Add all active committers in the STATUS file. |
| 2004-11-08 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| 2004-11-15 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2004-11-15 | Ask infrastructure to set up and archive Mailing lists. |
| 2004-11-15 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2004-11-15 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

| date | item |
|-------|-------|
| 2005-12-15 | Carry over the interfaces used in the Globus WSRF/WSN impl (Subscription, Topic, etc.). |
| 2005-04-23 | Participate in the OASIS WSDM 1.0 interop. |

# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? ... Yes, though we expect to add new committers in the future. For example. Hitachi will be contributing a couple developers in the near future, and a company called Gestalt has expressed interest in contributing some manpower.

- Are there three or more independent committers? ... Yes - HP (4), Globus (2), and CA (1).

- Are project decisions being made in public by the committers? ... Yes, we vote on all important decisions (for example, cutting a release or changing the project name).

- Are the decision-making guidelines published and agreed to by all of the committers? ... Yes, we use the standard ASF voting procedure.

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? ... Yes, we are only using 3rd-party libs with ASF-compatible licenses, and we are not using any trademarked names without proper acknowledgement.

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- Has the PMC voted to accept it? ... Yes, the WebServices PMC has accepted responsibility for the project.

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? ... A VOTE was intitiated by dims on 2005-05-27 and incubation was successfully completed on 2005-06-03.
