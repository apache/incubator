Title: OODT Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise.


<span class="graduated">The OODT project graduated on 2010-11-17</span>


OODT is a grid middleware framework for science data processing, information integration, and retrieval.


OODT is used on a number of successful projects at [NASA's Jet Propulsion Laboratory/ California Institute of Technology](http://jpl.nasa.gov) , and many other research institutions and universities, specifically those part of the:



-  [National Cancer Institute's (NCI's) Early Detection Research Network (EDRN)](http://cancer.gov/edrn) project - over 40+ institutions all performing research into discovering biomarkers which are early indicators of disease.

-  [NASA's Planetary Data System (PDS)](http://pds.nasa.gov) - NASA's planetary data archive, a repository and registry for all planetary data collected over the past 30+ years.

- various Earth Science data processing missions, including [Seawinds/QuickSCAT](http://seawinds.jpl.nasa.gov) , the [Orbiting Carbon Observatory](http://oco.jpl.nasa.gov) , the [NPP Sounder PEATE project](http://jointmission.gsfc.nasa.gov/) , and the [Soil Moisture Active Passive (SMAP)](http://smap.jpl.nasa.gov) mission.

OODT is middleware for metadata:



- Transparent access to distributed resources

- Data discovery and query optimization

- Distributed processing and virtual archives

OODT is a software architecture:



- Models for information representation

- Solutions to knowledge capture problems

- Unification of technology, data, and metadata


- 2010-11-17 Project graduates to [TLP](http://oodt.apache.org) !

- 2010-09-26 New committer: David Kale

- 2010-08-13 New committer: Cameron Goodale

- 2010-02-08 Mailing lists, issue tracker, accounts, etc. created

- 2010-01-21 Project enters incubation.


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/oodt/](http://incubator.apache.org/oodt/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/OODT/Home](https://cwiki.apache.org/confluence/display/OODT/Home)  |
| Mailing list | dev |  `oodt-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `oodt-commits`  `@`  `incubator.apache.org`  |
| . | private (PPMC) |  `oodt-private`  `@`  `incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/OODT](https://issues.apache.org/jira/browse/OODT)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/oodt/](https://svn.apache.org/repos/asf/incubator/oodt/)  |
| Mentors | jerenkrantz | Justin Erenkrantz |
| . | rgardler | Ross Gardler |
| . | ianh | Ian Holsman |
| . | jfclere | Jean-Frederic Clere |
| Committers | . | . |
| . | ahart | Andrew F. Hart |
| . | bfoster | Brian Foster |
| . | cgoodale | Cameron Goodale |
| . | crichton | Daniel J. Crichton |
| . | davekale | David Kale |
| . | joshuaga | Joshua Garcia |
| . | kelly | Sean Kelly |
| . | mattmann | Chris A. Mattmann |
| . | pramirez | Paul Ramirez |
| . | shardman | Sean Hardman |
| . | smcclees | Sean McCleese |
| . | woollard | David Woollard |
| Extra | Proposal |  [OODT Proposal](http://wiki.apache.org/incubator/OODTProposal)  |


- All are linked from our wiki, [here](https://cwiki.apache.org/confluence/display/OODT/Home) .

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2010-01-25 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2010-01-21 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2010-01-21 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2010-01-25 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2010-02-11 | Subscribe all Mentors on the pmc and general lists. |
| 2010-02-11 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-01-25 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2010-02-11 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2010-09-29 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2010-09-29 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2010-11-06 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-02-11 | Check that all active committers have submitted a contributors agreement. |
| 2010-02-11 | Add all active committers in the STATUS file. |
| 2010-02-11 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-01-25 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2010-01-25 | Ask infrastructure to set up and archive Mailing lists. ( [INFRA-2463](https://issues.apache.org/jira/browse/INFRA-2463) ) |
| 2010-01-25 | Ask infrastructure to set up JIRA ( [INFRA-2464](https://issues.apache.org/jira/browse/INFRA-2464) ) |
| 2010-01-25 | Ask infrastructure to set up Confluence ( [INFRA-2465](https://issues.apache.org/jira/browse/INFRA-2465) ) |
| 2010-02-23 | Migrate the project to our infrastructure. |

## Three blocking issues prior to graduation {#Project+specific}


1. Port OODT code and license headers into ASF license headers

1. OODT contributors from at least 2 other organizations besides JPL

1. At least one OODT incubating release, hopefully in the first few months

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
