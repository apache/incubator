Title: apollo


This page tracks the project status, incubator-wise. For more general project status, look on the [project website](http://incubator.apache.org/apollo/) .


<span class="graduated">The Apollo project graduated on 2005-06-03</span>


A Web Services WS-FX subproject that provides an implementation of the Web Services Resource Framework (WSRF) family of specifications.



- 2005-06-03 - Incubator PMC voted to graduate WSRF (formerly named Apollo)

- 2004-11-08 - Proposal sent to incubator general mailing list

- 2004-10-14 - Proposal accepted by WS PMC

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/apollo/](http://incubator.apache.org/apollo/)  |
| Proposal | wiki |  [http://wiki.apache.org/incubator/ApolloProposal](http://wiki.apache.org/incubator/ApolloProposal)  |
| Mailing Lists | dev |  [apollo-dev@ws.apache.org](mailto:apollo-dev@ws.apache.org)  |
| . | svn |  [apollo-cvs@incubator.apache.org](mailto:apollo-cvs@incubator.apache.org)  |
| Bug Tracking | jira |  [http://nagoya.apache.org/jira/secure/project/ViewProject.jspa?pid=1061](http://nagoya.apache.org/jira/secure/project/ViewProject.jspa?pid=10612)  |
| Source Code | svn |  [https://svn.apache.org/repos/asf/incubator/apollo/](https://svn.apache.org/repos/asf/incubator/apollo/)  |
| Mentors | dims | Davanum Srinivas |
| Committers | gawor | Jarek Gawor |
| . | ips | Ian Springer |
| . | kidz | Kinga Dziembowski |
| . | meder | Sam Meder |
| . | scamp | Sal Campana |
| . | wire | Bill Reichardt |
| Extra | . | . |


- 2005-06-03 - Incubator PMC voted to graduate WSRF

- 2005-05-25 - A 1.0 beta release of Apollo was released today. For a description of the features included in this release, see the [release announcement](http://marc.theaimsgroup.com/?l=apollo-dev&amp;m=111705792026831&amp;w=2) . This release contains all of the features that are planned for v1.0. The plan is to spend the next 6-8 weeks bolstering documentation and unit test coverage, i18nizing all messages, and fixing any bugs that are reported.

- 2005-04-21 - Kinga Dziembowski was voted in as a committer.

- 2005-03-17 - Due to trademark concerns with using the name Apollo, we voted to change the project name to WSRF.

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2005-04-18 | Make sure that the requested project name does not already exist and check http://www.nameprotect.com/ to be sure that the name is not already trademarked for an existing software product. NOTE: The new name will be WSRF, since the name Apollo has trademark issues. |
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
| 2005-01-04 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
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
| 2004-11-08 | Ask root for the creation of committers' accounts on minotaur.apache.org. |

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
| 2005-12-15 | Carry over the interfaces used in the Globus WSRF/WSN impl (Resource, ResourceHome, ResourceProperty, etc.). |
| 2005-03-01 | Participate in the OASIS WSRF interop. |

# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? ... Yes, though we expect to add new committers in the future. For example. Hitachi will be contributing a couple developers in the near future, and a company called Gestalt has expressed interest in contributing some manpower.

- Are there three or more independent committers? ... Yes - HP (4), Globus (2), CA (1) and Stefan Lischke (individual).

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
