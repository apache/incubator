Title: Calcite Incubation Status Page
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

Calcite graduated from the Apache Incubator in October, 2015 and is now a top level project (TLP) at Apache. For the latest information about Calcite please visit [http://calcite.apache.org/](http://calcite.apache.org/) 


 **THIS WEBSITE IS NO LONGER MAINTAINED!** 


<span class="graduated">The Calcite project graduated in 2015-10</span>


Calcite is a highly customizable engine for parsing and planning queries on data in a wide variety of formats. It allows database-like access, and in particular a SQL interface and advanced query optimization, for data not residing in a traditional database.



- 2014-05-19 Project enters incubation.

- 2014-09-04 Optiq 0.9.0-incubating released.

- 2014-09-30 Optiq renamed to Calcite.

- 2014-10-02 Calcite 0.9.1-incubating released.

- 2014-11-05 Calcite 0.9.2-incubating released.

- 2015-01-31 Calcite 1.0.0-incubating released.

- 2015-03-13 Calcite 1.1.0-incubating released.

- 2015-04-07 Calcite 1.2.0-incubating released.

- 2015-05-30 Calcite 1.3.0-incubating released.

- 2015-09-02 Calcite 1.4.0-incubating released.

- 2015-10-22 Graduated.


- link to the main website


- link to the page(s) that tell how to participate (Website, Mailing lists, Bug tracking, Source code)


- link to the project status file (Committers, non-incubation action items, project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [Calcite project site](http://calcite.apache.org)  |
| . | wiki | . |
| Mailing list | dev |  `dev`  `@`  `calcite.apache.org`  |
| . | private |  `private`  `@`  `calcite.apache.org`  |
| . | commits |  `commits`  `@`  `calcite.apache.org`  |
| Bug tracking | . |  [Jira: CALCITE](https://issues.apache.org/jira/browse/CALCITE)  |
| Source code | git |  [https://gitbox.apache.org/repos/asf/calcite.git](https://gitbox.apache.org/repos/asf/calcite.git) <br></br>(mirrored at [https://github.com/apache/calcite](https://github.com/apache/calcite) ), [https://gitbox.apache.org/repos/asf/incubator-calcite-csv.git](https://gitbox.apache.org/repos/asf/incubator-calcite-csv.git) , [https://gitbox.apache.org/repos/asf/incubator-calcite-linq4j.git](https://gitbox.apache.org/repos/asf/incubator-calcite-linq4j.git) . |
| Champion | hashutosh | Ashutosh Chauhan |
| Mentors | gates | Alan Gates |
| . | tdunning | Ted Dunning |
| . | stevenn | Steven Noels |
| Committers | jhyde | Julian Hyde |
| . | jacques | Jacques Nadeau |
| . | jamestaylor | James R. Taylor |
| . | cwensel | Chris Wensel |
| . | vladimirsitnikov | Vladimir Sitnikov |
| . | amansinha | Aman Sinha |
| . | jcamacho | Jesús Camacho Rodríguez |
| . | jni | Jinfeng Ni |
| . | jpullokk | John Pullokkaran |
| . | ndimiduk | Nick Dimiduk |


-  [July](https://wiki.apache.org/incubator/July2014) , [August](https://wiki.apache.org/incubator/August2014) , [September](https://wiki.apache.org/incubator/September2014) , [October](https://wiki.apache.org/incubator/October2014) 2014; [January](https://wiki.apache.org/incubator/January2015) , [April](https://wiki.apache.org/incubator/April2015) , [September](https://wiki.apache.org/incubator/September2015) 2015

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
|  [2014-06-19](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-51) , [2014-09-26](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-56)  | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2014-04-30 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
|  [2014-06-24](https://issues.apache.org/jira/browse/INFRA-7776)  | Ask infrastructure to create source repository modules and grant the committers karma. |
|  [2014-07-09](https://issues.apache.org/jira/browse/INFRA-7981)  | Ask infrastructure to set up and archive mailing lists. |
|  [2014-06-16](https://issues.apache.org/jira/browse/INFRA-7904)  | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
|  [2014-08-03](https://issues.apache.org/jira/browse/INFRA-8133)  | Ask infrastructure to set up wiki (Confluence, Moin). |
|  [2014-07-04](https://issues.apache.org/jira/browse/INFRA-7986)  | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2015-09-01 | Subscribe all Mentors on the pmc and general lists. |
| 2015-09-01 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2015-09-01 | Tell Mentors to track progress in the file 'incubator/projects/calcite.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2015-09-01 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2015-09-01 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2015-09-01 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2015-09-01 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2015-09-01 | Check that all active committers have submitted a contributors agreement. |
| 2015-09-01 | Add all active committers in the STATUS file. |
| 2015-09-01 | Ask root for the creation of committers' accounts on people.apache.org. |

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
