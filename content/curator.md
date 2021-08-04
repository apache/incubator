Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Curator project graduated on 2013-09-01</span>


Curator is a set of Java libraries that make using Apache ZooKeeper much easier. While ZooKeeper comes bundled with a Java client, using the client is non-trivial and error prone. It consists of three components that build on each other. Curator Client is a replacement for the bundled ZooKeeper class that takes care of some low-level housekeeping and provides some useful utilities. Curator Framework is a high-level API that greatly simplifies using ZooKeeper. It adds many features that build on ZooKeeper and handles the complexity of managing connections to the ZooKeeper cluster and retrying operations. Curator Recipes consists of implementations of some of the common ZooKeeper "recipes". Additionally, Curator Test is included which includes utilities to help with unit testing ZooKeeper-based applications.



- 2013-09-13 Apache Curator exits incubation.

- 2013-08-08 Apache Curator 2.2.0-incubating released.

- 2013-07-13 Iannois Canellos added as a new committer.

- 2013-07-02 Apache Curator 2.1.0-incubating released.

- 2013-06-15 Eric Tschetter added as a new committer.

- 2013-05-31 Apache Curator 2.0.1-incubating released.

- 2013-05-09 Apache Curator 2.0.0-incubating released.

- 2013-05-01 Vote on initial release commences.

- 2013-03-11 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://curator.incubator.apache.org](http://curator.incubator.apache.org)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/CURATOR](https://cwiki.apache.org/confluence/display/CURATOR)  |
| Mailing list | dev |  `dev`  `@`  `curator.incubator.apache.org`  |
| . | user |  `user`  `@`  `curator.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `curator.incubator.apache.org`  |
| Bug tracking | JIRA |  [http://issues.apache.org/jira/browse/CURATOR](http://issues.apache.org/jira/browse/CURATOR)  |
| Source code | git |  [https://gitbox.apache.org/repos/asf?p=incubator-curator.git](https://gitbox.apache.org/repos/asf?p=incubator-curator.git)  |
| Mentors | phunt | Patrick Hunt |
| . | mahadev | Mahadev Konar |
| . | lresende | Luciano Resende |
| . | enis | Enis Söztutar |
| Committers | randgalt | Jordan Zimmerman |
| . | zarfide | Jay Zarfoss |
| . | cheddar | Eric Tschetter |
| . | iocanel | Ioannis Canellos |


-  [July 2013](http://wiki.apache.org/incubator/July2013) 

-  [June 2013](http://wiki.apache.org/incubator/June2013) 

-  [May 2013](http://wiki.apache.org/incubator/May2013) 

-  [April 2013](http://wiki.apache.org/incubator/April2013) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2013-05-09 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| n/a | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2013-05-09 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2013-05-09 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2013-03-26 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2013-03-21 | Ask infrastructure to set up and archive mailing lists. |
| 2013-03-21 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2013-03-25 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2013-03-26 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2013-03-21 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2013-03-21 | Subscribe all Mentors on the pmc and general lists. |
| 2013-03-21 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2013-03-21 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2013-03-21 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2013-03-21 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2013-05-10 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2013-05-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2013-05-01 | Check that all active committers have submitted a contributors agreement. |
| 2013-05-01 | Add all active committers in the STATUS file. |
| 2013-05-01 | Ask root for the creation of committers' accounts on people.apache.org. |

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
