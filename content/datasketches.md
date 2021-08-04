Title: DataSketches Incubation Status
<link href="https://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The DataSketches project graduated on 2020-12-16</span>


DataSketches is an open source, high-performance library of streaming algorithms commonly called "sketches" in the data sciences. Sketches are small, stateful programs that process massive data as a stream and can provide approximate answers, with mathematical guarantees, to computationally difficult queries orders-of-magnitude faster than traditional, exact methods.



- 2019-03-30 Datasketches enters incubation.

- Current Releases: [](https://datasketches.apache.org/docs/Community/Downloads.html) https://datasketches.apache.org/docs/Community/Downloads.html

- History of Apache Releases by component:

  - datasketches-java: [https://github.com/apache/incubator-datasketches-java/releases](https://github.com/apache/incubator-datasketches-java/releases) 

  - datasketches-cpp: [https://github.com/apache/incubator-datasketches-cpp/releases](https://github.com/apache/incubator-datasketches-cpp/releases) 

  - datasketches-hive: [https://github.com/apache/incubator-datasketches-hive/releases](https://github.com/apache/incubator-datasketches-hive/releases) 

  - datasketches-pig: [https://github.com/apache/incubator-datasketches-pig/releases](https://github.com/apache/incubator-datasketches-pig/releases) 

  - datasketches-postgresql: [https://github.com/apache/incubator-datasketches-postgresql/releases](https://github.com/apache/incubator-datasketches-postgresql/releases) 

  - datasketches-memory: [https://github.com/apache/incubator-datasketches-memory/releases](https://github.com/apache/incubator-datasketches-memory/releases) 


- Integration efforts have started with Apache Impala.

- Added new committers:

  - David Cromberge, August 17, 2020.

  - Pavel Veselý, November 23, 2020.


- Board approved graduation: December 16, 2020.

- Transition to TLP in process.

| item | type | reference |
|------|------|-----------|
| Website | www |  [https://datasketches.apache.org/](https://datasketches.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/DATASKETCHES/Home](https://cwiki.apache.org/confluence/display/DATASKETCHES/Home)  |
| Mailing lists | dev |  `dev`  `@`  `datasketches.apache.org`  |
| . | users |  `users`  `@`  `datasketches.apache.org`  |
| . | commits |  `commits`  `@`  `datasketches.apache.org`  |
| . | issues |  `issues`  `@`  `datasketches.apache.org`  |
| . | notifications |  `notifications`  `@`  `datasketches.apache.org`  |
| . | private |  `private`  `@`  `datasketches.apache.org`  |
| Bug tracking | Java Core |  [https://github.com/apache/incubator-datasketches-java/issues](https://github.com/apache/incubator-datasketches-java/issues)  |
| . | CPP Core |  [https://github.com/apache/incubator-datasketches-cpp/issues](https://github.com/apache/incubator-datasketches-cpp/issues)  |
| . | Java Hive |  [https://github.com/apache/incubator-datasketches-hive/issues](https://github.com/apache/incubator-datasketches-hive/issues)  |
| . | Java Pig |  [https://github.com/apache/incubator-datasketches-pig/issues](https://github.com/apache/incubator-datasketches-pig/issues)  |
| . | CPP PostreSQL |  [https://github.com/apache/incubator-datasketches-postgresql/issues](https://github.com/apache/incubator-datasketches-postgresql/issues)  |
| . | Java Memory |  [https://github.com/apache/incubator-datasketches-memory/issues](https://github.com/apache/incubator-datasketches-memory/issues)  |
| . | GitHub | Use _issues_ on any of our GitHub sites (below). |
| Source code | GitHub |  [https://github.com/apache?q=datasketches](https://github.com/apache?q=datasketches)  |
| . | Zip Archive |  [https://archive.apache.org/dist/incubator/datasketches/](https://archive.apache.org/dist/incubator/datasketches/)  |
| . | Nexus (Java) |  [https://repository.apache.org/content/repositories/releases/org/apache/datasketches/](https://repository.apache.org/content/repositories/releases/org/apache/datasketches)  |
| Mentors | kamaci | Furkan Kamaci |
| . | kenn | Kenneth Knowles |
| . | chenliang613 | Liang Chen |
| . | wave | Dave Fisher |
| . | evansye | Evans Ye |
| Roster | Whimsy |  [Datasketches Roster](https://whimsy.apache.org/roster/ppmc/datasketches)  |


-  [Datasketches Board Reports](https://whimsy.apache.org/board/minutes/datasketches.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2019-04-09 |  [Datasketches Name Approved by Mark Thomas](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-168)  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2019-04-10 | Request DNS (first step after creating podling status page) https://issues.apache.org/jira/browse/INFRA-18197. Completed. |
| 2019-04-10 | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator) Completed. |
| 2019-05-10 | Request [git repositories](https://reporeq.apache.org/) https://issues.apache.org/jira/browse/INFRA-18362. Completed |
| N/A (using GitHub) | Ask infrastructure to set up issue tracker ( [JIRA](https://selfserve.apache.org/jira.html) , Bugzilla). [DataSketches JIRA](https://issues.apache.org/jira/projects/DATASKETCHES) Not used. |
| N/A (not using wiki) | Ask infrastructure to set up wiki ( [Confluence](https://selfserve.apache.org/confluence.html) ). Not used. |
| 2020-01-24 (website was the final item) | Migrate the project to our infrastructure. ( [INFRA-18362](https://issues.apache.org/jira/browse/INFRA-18362) and [INFRA-19259](https://issues.apache.org/jira/browse/INFRA-19259) ) |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2019-05-10 | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file). Completed. |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright and IP {#Copyright}

| date | item |
|------|------|
| 2019-05-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2019-10-25 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |
| 2019-05-07 | Matt Sicker (secretary@apache.org) acknowledged receipt of Software Grant |
| 2019-05-07 | Matt Sicker (secretary@apache.org) acknowledged receipt of SGA and Logo source file. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2019-10-25 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. Completed. |
| 2019-10-25 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. Completed. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| Committer | ICLA? |
|-----------|-------|
| Alexander Saydakov | YES |
| David Cromberge | YES |
| Edo Liberty | YES |
| Eshcar Hillel | YES |
| Jon Malkin | YES |
| Justin Thaler | YES |
| Lee Rhodes | YES |
| Pavel Veselý | YES |
| Roman Leventov | YES |

| date | item |
|------|------|
| 2019-04-10 | Check that all active committers have submitted a contributors agreement. YES. |
| 2019-04-10 | Add all active committers in the relevant section above. Done. |
| 2019-04-10 | Ask root for the creation of committers' accounts in LDAP. Done. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? YES.

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)
YES.
- Are project decisions being made in public by the committers? YES.

- Are the decision-making guidelines published and agreed to by all of the committers? YES.

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? YES.

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it? YES.

- If graduating to a new PMC, has the board voted to accept it? YES.

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? YES.
