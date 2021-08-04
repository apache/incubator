Title: Gora Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise.


<span class="graduated">The Gora project graduated on 2012-01-15</span>


Gora is an ORM framework for column stores such as Apache HBase and Apache Cassandra with a specific focus on Hadoop.


Although there are various excellent ORM frameworks for relational databases, data modeling in NoSQL data stores differ profoundly from their relational cousins. Moreover, data-model agnostic frameworks such as JDO are not sufficient for use cases, where one needs to use the full power of the data models in column stores. Gora fills this gap by giving the user an easy-to-use ORM framework with data store specific mappings and built in Apache Hadoop support.



-  **2012-01-15 Apache Gora has been accepted by the Board and has now graduated to a Top Level Project within the Apache Software Foundation.** 

- 2010-10-10 Mailing lists, issue tracker, accounts, etc. created

- 2010-09-26 Project enters incubation.


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/gora/](http://incubator.apache.org/gora/)  |
| . | wiki |  [http://cwiki.apache.org/confluence/display/GORA](http://cwiki.apache.org/confluence/display/GORA)  |
| Mailing list | dev |  `gora-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `gora-commits`  `@`  `incubator.apache.org`  |
| . | private (PPMC) |  `gora-private`  `@`  `incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/GORA](https://issues.apache.org/jira/browse/GORA)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/gora/](https://svn.apache.org/repos/asf/incubator/gora/)  |
| Mentors | mattmann | Chris Mattmann |
| . | ab | Andrzej Bialecki |
| . | tomwhite | Tom White |
| Committers | . | . |
| . | ahart | Andrew F. Hart |
| . | dogacan | Doğacan Güney |
| . | enis | Enis Söztutar |
| . | hsaputra | Henry Saputra |
| . | jnioche | Julien Nioche |
| . | sertan | Sertan Alkan |
| . | woollard | David Woollard |
| Extra | Proposal |  [GORA Proposal](http://wiki.apache.org/incubator/GoraProposal)  |


- All are linked from our wiki, [here](https://cwiki.apache.org/confluence/display/GORA/Home) .

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2010-11-10 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product (searched and found closest match to be [@GORA](http://s.apache.org/Ilp) .). |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2010-09-26 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2010-09-26 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2010-09-26 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2010-09-26 | Subscribe all Mentors on the pmc and general lists. |
| 2010-09-26 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-09-26 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2010-10-05 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2010-10-11 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2010-10-11 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2010-10-11 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-09-26 | Check that all active committers have submitted a contributors agreement. |
| 2010-09-26 | Add all active committers in the STATUS file. |
| 2010-10-04 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-09-27 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2010-09-27 | Ask infrastructure to set up and archive Mailing lists. ( [INFRA-3017](https://issues.apache.org/jira/browse/INFRA-3017) ) |
| 2010-09-27 | Ask infrastructure to set up JIRA ( [INFRA-3019](https://issues.apache.org/jira/browse/INFRA-3019) ) |
| 2010-09-27 | Ask infrastructure to set up Confluence ( [INFRA-3020](https://issues.apache.org/jira/browse/INFRA-3020) ) |
| 2010-10-11 | Migrate the project to our infrastructure. |

## Initial Goals {#Project+specific}


1. Iron out the remaining issues with HBase, Cassandra and SQL support. **DONE** 

1. Make the first release before the end of the year. **DONE** 

1. Improve documentation. **DONE** 

1. Support for Cascading. Not done, but not currently required by the community.

# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? **YES** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) **YES** 

- Are project decisions being made in public by the committers? **YES** 

- Are the decision-making guidelines published and agreed to by all of the committers? **YES** 

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? **YES** 

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it? **SEE BELOW** 

- If graduating to a new PMC, has the board voted to accept it? **YES SEE TOP OF PAGE** 

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? **YES** 
