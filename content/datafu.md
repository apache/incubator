Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The DataFu project graduated on 2018-02-21</span>


DataFu provides a collection of Hadoop MapReduce jobs and functions in higher level languages based on it to perform data analysis. It provides functions for common statistics tasks (e.g. quantiles, sampling), PageRank, stream sessionization, and set and bag operations. DataFu also provides Hadoop jobs for incremental data processing in MapReduce.



- 2014-01-05 Project enters incubation.

- 2014-01-15 Project fully transitions to ASF infrastructure.

- 2014-02-25 Jian Wang voted in as a new committer and PPMC member.

- 2014-05-13 PODLINGNAMESEARCH-48 completed.

- 2014-07-23 Casey Stella voted in as a new committer and PPMC member.

- 2014-11-13 Russell Jurney voted in as a new committer and PPMC member.

- 2015-11-14 1.3.0-incubating release created.

- 2016-07-05 Eyal Allweil voted in as a new committer and PPMC member.

- 2016-08-10 1.3.1-incubating release created.

- 2017-03-10 1.3.2-incubating release created.

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://datafu.incubator.apache.org](http://datafu.incubator.apache.org)  |
| . | wiki |  [http://wiki.apache.org/datafu](http://wiki.apache.org/datafu)  |
| Mailing list | dev |  `dev`  `@`  `datafu.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `datafu.incubator.apache.org`  |
| Bug tracking | . | https://issues.apache.org/jira/browse/DATAFU |
| Source code | SVN |  [git://git.apache.org/incubator-datafu.git](git://git.apache.org/incubator-datafu.git)  |
| Mentors | jghoman | Jakob Homan |
| . | hashutosh | Ashutosh Chauhan |
| . | rvs | Roman Shaposhnik |
| . | tdunning | Ted Dunning |
| Committers | mhayes | Matt Hayes |
| . | cestella | Casey Stella |
| . | eyal | Eyal Allweil |
| . | jianwang | Jian Wang |
| . | rjurney | Russell Jurney |
| . | wvaughan | William Vaughan |
| . | evion | Evion Kim |
| . | samshah | Sam Shah |
| . | meng | Xiangrui Meng |
| . | clloyd | Christopher Lloyd |
| . | mbastian | Mathieu Bastian |
| . | mitultiwari | Mitul Tiwari |
| . | jwills | Josh Wills |
| . | jarcec | Jarek Jarcec Cecho |


-  [April 2017](https://wiki.apache.org/incubator/April2017) 

-  [February 2017](https://wiki.apache.org/incubator/February2017) 

-  [November 2016](https://wiki.apache.org/incubator/November2016) 

-  [July 2016](https://wiki.apache.org/incubator/July2016) 

-  [April 2016](https://wiki.apache.org/incubator/April2016) 

-  [January 2016](https://wiki.apache.org/incubator/January2016) 

-  [November 2015](https://wiki.apache.org/incubator/November2015) 

-  [August 2015](https://wiki.apache.org/incubator/August2015) 

-  [January 2015](https://wiki.apache.org/incubator/January2015) 

-  [October 2014](https://wiki.apache.org/incubator/October2014) 

-  [July 2014](https://wiki.apache.org/incubator/July2014) 

-  [April 2014](https://wiki.apache.org/incubator/April2014) 

-  [March 2014](https://wiki.apache.org/incubator/March2014) 

-  [February 2014](https://wiki.apache.org/incubator/February2014) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2014-05-13 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| 2014-05-13 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2014-05-13 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2014-05-13 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2014-01-15 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2014-01-15 | Ask infrastructure to set up and archive mailing lists. |
| 2014-01-15 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2014-01-15 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2014-01-15 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2014-01-15 | Subscribe all Mentors on the pmc and general lists. |
| 2014-01-15 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2014-01-15 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2015-11-14 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2015-11-14 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2015-11-14 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2015-11-14 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2014-01-15 | Check that all active committers have submitted a contributors agreement. |
| 2014-01-15 | Add all active committers in the STATUS file. |
| 2014-01-15 | Ask root for the creation of committers' accounts on people.apache.org. |

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
