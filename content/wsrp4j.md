Title: wsrp4j


This page tracks the project status, incubator-wise.


<span class="retired">The WSRP4J project retired on 2010-04-18</span>


The WSRP4J Project is an implementation of WSRP 1.0 Producer. WSRP is an OASIS specification that describes a protocol which allows portlets to be accessed remotely using Web Services.



- 2010-04-18 Project terminated because of lack of community and interest

- 2007-05-11 New committer: Ate Douma

- 2006-05-30 New committer: Vishal Goenka

- We developed Google Summer of Code proposal for a chunk of new features we have a student ready to implement them.

- 2005-03-08 New committer: Diego Louzan

- 2004-07-09 New committer: Scott Goldstein

- We voted to move to Subversion and Maven.

- We have received contributions from outside developers, which we hope grows into more diverse participation.

- I (jmacna@apache.org) have met with constituents from higher education that are using WSRP4J and see a strong role for WSRP in their software plans, and I have encouraged them to contribute to the project publicly. We have seen increased participation from these teams already.

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://portals.apache.org/wsrp4j/](http://portals.apache.org/wsrp4j/)  |
| . | wiki |  [wsrp4j wiki](http://wiki.apache.org/portals/WSRP4J)  |
| Mailing list | dev |  [wsrp4j-dev@portals.apache.org](mailto:wsrp4j-dev@portals.apache.org)  |
| . | svn |  [wsrp4j-dev@portals.apache.org](mailto:wsrp4j-dev@portals.apache.org)  |
| Bug tracking | JIRA |  [http://issues.apache.org/jira/browse/WSRP4J](http://issues.apache.org/jira/browse/WSRP4J)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/portals/wsrp4j/](http://svn.apache.org/repos/asf/portals/wsrp4j/)  |
| Mentors |  [rubys@apache.org](mailto:rubys@apache.org)  | Sam Ruby |
| . |  [dims@apache.org](mailto:dims@apache.org)  | Davanum Srinivas |
| Committers |  [jacob@apache.org](mailto:jacob@apache.org)  | Richard Jacob |
| . |  [taylor@apache.org](mailto:taylor@apache.org)  | David Sean Taylor |
| . |  [jmacna@apache.org](mailto:jmacna@apache.org)  | Julie MacNaught |
| . |  [behl@apache.org](mailto:behl@apache.org)  | Stefan Behl |
| . |  [cziegeler@apache.org](mailto:cziegeler@apache.org)  | Carsten Ziegeler |
| . |  [pfisher@apache.org](mailto:pfisher@apache.org)  | Peter Fischer |
| . |  [sgala@apache.org](mailto:sgala@apache.org)  | Santiago Gala |
| . |  [acoliver@apache.org](mailto:acoliver@apache.org)  | Andrew C. Oliver |
| . |  [dims@apache.org](mailto:dims@apache.org)  | Davanum Srinivas |
| . |  [sgoldstein@apache.org](mailto:sgoldstein@apache.org)  | Scott Goldstein |
| . |  [dlouzan@apache.org](mailto:dlouzan@apache.org)  | Diego Louzan Martinez |
| Extra | . | . |

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2003-07-25 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| 2003-01-21 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2003-07-25 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2003-09-03 | Subscribe all Mentors on the pmc and general lists. |
| 2003-09-03 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2003-09-03 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2003-09-02 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-03-09 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2003-08-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2003-08-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| 2003-09-03 | Check that all active committers have submitted a contributors agreement. |
| 2004-01-07 | Add all active committers in the STATUS file. |
| 2003-09-03 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| 2003-09-03 | Ask infrastructure to create source repository modules and add thecommitters to the avail file. |
| 2003-09-03 | Ask infrastructure to set up and archive Mailing lists. |
| 2003-09-03 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2003-09-03 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? Yes

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) Yes.

- Are project decisions being made in public by the committers? Yes

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? Yes

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
