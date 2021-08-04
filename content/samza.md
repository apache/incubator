Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Samza project graduated on 2015-01-21</span>


Samza provides a system for processing stream data from publish-subscribe systems such as Apache Kafka. The developer writes a stream processing task, and executes it as a Samza job. Samza then routes messages between stream processing tasks and the publish-subscribe systems that the messages are addressed to.



- 2013-07-30 Project enters incubation.

- 2014-07-11 Samza 0.7 [released](https://blogs.apache.org/samza/entry/announcing_the_release_of_apache) 

- 2014-12-09 Samza 0.8 [released](https://blogs.apache.org/samza/entry/announcing_the_release_of_apache1) 

- 2014-01-02 Samza graduates to Top Level Project status.


-  [link to the main website](http://samza.incubator.apache.org/) 


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://samza.incubator.apache.org/](http://samza.incubator.apache.org/)  |
| . | wiki |  [http://wiki.apache.org/samza/](http://wiki.apache.org/samza/)  |
| Mailing list | dev |  `dev`  `@`  `samza.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `samza.incubator.apache.org`  |
| . | private |  `private`  `@`  `samza.incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/SAMZA](https://issues.apache.org/jira/browse/SAMZA)  |
| Source code | Git |  [http://gitbox.apache.org/repos/asf/incubator-samza.git](http://gitbox.apache.org/repos/asf/incubator-samza.git)  |
| Mentors | acmurthy | Arun Murthy |
| . | cdouglas | Chris Douglas |
| . | jghoman | Jakob Homan |
| . | rvs | Roman Shaposhnik |
| Committers | cpsoman | Chinmay Soman |
| . | criccomini | Chris Riccomini |
| . | jkreps | Jay Kreps |
| . | jghoman | Jakob Homan |
| . | sriramsub | Sriram Subramanian |
| . | garryturk | Garry Turkington |
| . | martinkl | Martin Kleppmann |
| . | yanfang | Yan Fang |
| . | zjshen | Zhijie Shen |


-  [October 2014](http://wiki.apache.org/incubator/October2014) 

-  [July 2014](http://wiki.apache.org/incubator/July2014) 

-  [April 2014](http://wiki.apache.org/incubator/April2014) 

-  [January 2014](http://wiki.apache.org/incubator/January2014) 

-  [October 2013](http://wiki.apache.org/incubator/October2013) 

-  [September 2013](http://wiki.apache.org/incubator/September2013) 

-  [August 2013](http://wiki.apache.org/incubator/August2013) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2014-04-29 | Make sure that the requested project name does not already exist: [PODLINGNAMESEARCH-46](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-46) . |
| 2013-07-13 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2013-07-13 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2013-08-06 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2013-08-06 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2013-08-06 | Ask infrastructure to set up and archive mailing lists. |
| 2013-08-06 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2013-08-10 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2013-08-06 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2013-08 | Subscribe all Mentors on the pmc and general lists. |
| 2013-08 | Give all Mentors access to the incubator git repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2013-08 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2014-04-13 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2014-04-13 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2014-04-13 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2014-04-13 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2014-04-13 | Check that all active committers have submitted a contributors agreement. |
| 2014-04-13 | Add all active committers in the STATUS file. |
| 2014-04-13 | Ask root for the creation of committers' accounts on people.apache.org. |

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
