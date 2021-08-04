Title: Accumulo Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Accumulo project graduated on 2012-03-21</span>


Accumulo is a sorted, distributed key/value store based on Google's BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It features a few novel improvements on the BigTable design in the form of cell-level access labels and a server-side programming mechanism that can modify key/value pairs at various points in the data management process.



- 2012-03-21 Apache Accumulo graduated to a top-level project.

- 2012-03-20 Jason Trost added as a new committer.

- 2012-02-14 David Medinets added as a new committer.

- 2011-12-17 Version 1.3.5-incubating released.

- 2011-09-12 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/accumulo/](http://incubator.apache.org/accumulo/)  |
| . | wiki | N/A |
| Mailing list | dev |  `accumulo-dev`  `@`  `incubator.apache.org`  |
| . | user |  `accumulo-user`  `@`  `incubator.apache.org`  |
| . | commits |  `accumulo-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | JIRA | https://issues.apache.org/jira/browse/ACCUMULO |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/accumulo/](https://svn.apache.org/repos/asf/incubator/accumulo/)  |
| Mentors | bimargulies | Benson Margulies |
| . | adc | Alan D. Cabrera |
| . | berndf | Bernd Fondermann |
| Committers | acordova | Aaron Cordova |
| . | afuchs | Adam Fuchs |
| . | medined | David Medinets |
| . | ecn | Eric Newton |
| . | billie | Billie Rinaldi |
| . | jtrost | Jason Trost |
| . | kturner | Keith Turner |
| . | vines | John Vines |
| . | cawaring | Chris Waring |
| Extra | . | . |


-  [October 2011](http://wiki.apache.org/incubator/October2011) 

-  [November 2011](http://wiki.apache.org/incubator/November2011) 

-  [December 2011](http://wiki.apache.org/incubator/December2011) 

-  [March 2012](http://wiki.apache.org/incubator/March2012) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2012-02-28 |  [Suitable Name Search](http://incubator.apache.org/guides/names.html) - see [PODLINGNAMESEARCH-3](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-3) . |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2011-09-12 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2011-10-03 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2011-09-12 | Ask infrastructure to set up and archive mailing lists. |
| 2011-09-12 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| N/A | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2011-10-04 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2011-09-12 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2011-09-13 | Subscribe all Mentors on the pmc and general lists. |
| 2011-10-14 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member with karma for the authorizations file) |
| 2011-09-12 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-10-13 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-11-18 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2012-01-06 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2012-01-06 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2011-09-13 | Check that all active committers have submitted a contributors agreement. |
| 2011-09-13 | Add all active committers in the STATUS file. |
| 2011-09-13 | Ask root for the creation of committers' accounts on people.apache.org. |

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


- Are all licensing, trademark, credit issues being taken care of and acknowledged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
