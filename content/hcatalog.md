Title: HCatalog Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The HCatalog project graduated on 2013-02-13</span>


HCatalog is a table and storage management service for data created using Apache Hadoop.



- 2011-03-14 HCatalog enters incubation.

- 2013-02-13 HCatalog graduates from incubation to become part of Apache Hive.

| item | type | reference |
|------|------|-----------|
| Website | www |  [HCatalog](http://incubator.apache.org/hcatalog/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/HCATALOG](https://cwiki.apache.org/confluence/display/HCATALOG)  |
| Mailing list | dev |  `hcatalog-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `hcatalog-commits`  `@`  `incubator.apache.org`  |
| . | user |  `hcatalog-user`  `@`  `incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/HCATALOG](https://issues.apache.org/jira/browse/HCATALOG)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/hcatalog/](https://svn.apache.org/repos/asf/incubator/hcatalog/)  |
| Mentors | gates | Alan Gates |
| . | akarasulu | Alex Karasulu |
| . | omalley | Owen O'Malley |
| PPMC Members | hashutosh | Ashutosh Chauhan |
| . | ddas | Devaraj Das |
| . | macyang | Mac Yang |
| . | pauly | Paul Yang |
| . | khorgath | Sushanth Sowmyan |
| . | toffer | Francis Liu |
| . | avandana | Vandana Ayyalasomayajula |
| Committers | daijy | Daniel Dai |
| . | travis | Travis Crawford |
| . | mithun | Mithun Radhakrishnan |


-  [December 2012 Report](http://wiki.apache.org/incubator/December2012) 

-  [September 2012 Report](http://wiki.apache.org/incubator/September2012) 

-  [June 2012 Report](http://wiki.apache.org/incubator/June2012) 

-  [March 2012 Report](http://wiki.apache.org/incubator/March2012) 

-  [December 2011 Report](http://wiki.apache.org/incubator/December2011) 

-  [September 2011 Report](http://wiki.apache.org/incubator/September2011) 

-  [June 2011 Report](http://wiki.apache.org/incubator/June2011) 

-  [May 2011 Report](http://wiki.apache.org/incubator/May2011) 

-  [April 2011 Report](http://wiki.apache.org/incubator/April2011) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2011-03-15 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. (nameprotect.com no longer offers free services (see [LUCY-121](https://issues.apache.org/jira/browse/LUCY-121)) ) but I worked through the steps located on this [this page](http://www.apache.org/dev/project-names.html) and did not find any name issues.) |
| Not Applicable | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| Not Applicable | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| Not Applicable | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2011-03-15 | Ask infrastructure to create source repository modules and grant the committers karma. I created the initial repository area and Owen added the trunk, branches, and tags directories. Karma was granted for mentors and committers who are current Apache committers. Accounts have been requested for committers who are not current committers (Mac Yang and Sushanth Sowmyan). |
| 2011-03-16 | Ask infrastructure to set up and archive mailing lists. [INFRA-3522](https://issues.apache.org/jira/browse/INFRA-3522)  |
| 2011-03-16 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). [INFRA-3523](https://issues.apache.org/jira/browse/INFRA-3523)  |
| 2011-03-16 | Ask infrastructure to set up wiki (Confluence, Moin). I asked for a confluence page since it has access controls. [INFRA_3524](https://issues.apache.org/jira/browse/INFRA-3524)  |
| 2011-04-12 | Migrate the project to our infrastructure. [HCATALOG-1](https://issues.apache.org/jira/browse/HCATALOG-1)  |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2011-03-15 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2011-03-15 | Subscribe all Mentors on the pmc and general lists. |
| 2011-03-15 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2011-03-16 | Tell Mentors to track progress in the file 'incubator/projects/hcatalog.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-03-21 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-03-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2011-08-09 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-08-09 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2011-03-21 | Check that all active committers have submitted a contributors agreement. |
| 2011-03-28 | Add all active committers in the STATUS file. |
| 2011-03-21 | Ask root for the creation of committers' accounts on people.apache.org. |

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


- If graduating to an existing PMC, has the PMC voted to accept it? The Hive PMC voted to accept Hive on Feb 4 2013 ( [vote summary](http://mail-archives.apache.org/mod_mbox/hive-dev/201302.mbox/%3CCACf6Rrz-2vQ%2BT3KcDrt9gjxvf8%2B_OOvbxzQRT9iveiknOWxRWQ%40mail.gmail.com%3E) ). The IPMC ratified the decision on Feb 13 2013 ( [vote summary](http://mail-archives.apache.org/mod_mbox/incubator-general/201302.mbox/%3CAA3D16B0-F542-4E17-89E8-9220443158B2%40hortonworks.com%3E) ).

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
