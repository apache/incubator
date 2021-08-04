Title: Pinot Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Pinot is a distributed columnar storage engine that can ingest data in real-time and serve analytical queries at low latency. There are two modes of data ingestion - batch and/or realtime. Batch mode allows users to generate pinot segments externally using systems such as Hadoop. These segments can be uploaded into Pinot via simple curl calls. Pinot can ingest data in near real-time from streaming sources such as Kafka. Data ingested into Pinot is stored in a columnar format. Pinot provides a SQL like interface (PQL) that supports filters, aggregations, and group by operations.



- 2018-10-21 Project enters incubation.

- 2020-04-09 New committer added - Haibo Wang.

- 2020-07-22 New committer added - Kartik Khare.

- 2020-07-22 New committer added - Ting Chen.

- 2020-09-20 New committer added - Harley Jackson.

- 2021-02-01 New committer added - Yupeng Fu.

- 2021-02-01 New committer added - Chinmay Soman.


- Pinot Website - https://pinot.incubator.apache.org


-  [Current Documentation](https://docs.pinot.apache.org/) 

-  [Releases](https://dist.apache.org/repos/dist/release/incubator/pinot/) 

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://pinot.incubator.apache.org/](http://pinot.incubator.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/PINOT/](https://cwiki.apache.org/confluence/display/PINOT/)  |  |
| Mailing list | dev |  `dev`  `@`  `pinot.incubator.apache.org`  |
| . | user |  `user`  `@`  `pinot.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `pinot.incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/PINOT](https://issues.apache.org/jira/browse/PINOT)  |
| Source code | git checkout | git clone https://gitbox.apache.org/repos/asf/incubator-pinot.git |
| Source code | Browse | git clone https://gitbox.apache.org/repos/asf/incubator-pinot.git |
| Source code | Github mirror | https://github.com/apache/incubator-pinot |
| Mentors | jim | Jim Jagielski |
| . | kishoreg | Kishore G |
| . | olamy | Olivier Lamy |
| . | felixcheung | Felix Cheung |
| Committers | apache id | name |
| . | akshayrai09 | Akshay Rai |
| . | apucher | Alexander Pucher |
| . | cpsoman | Chinmay Soman |
| . | haibow | Haibo Wang |
| . | jackie | Jackie Jiang |
| . | jamesshao | James Shao |
| . | jfim | Jean-Francois Im |
| . | jenniferdai | Jennifer Dai |
| . | jlli | Jialiang Li |
| . | jihao | Jihao Zhang |
| . | kharekartik | Kartik Khare |
| . | mayanks | Mayank Shrivastava |
| . | nehapawar | Neha Pawar |
| . | aaronucsd | Long Huynh |
| . | siddteotia | Siddharth Teotia |
| . | snlee | Seunghyun Lee |
| . | mcvsubbu | Subbu Subramaniam |
| . | sunithabeeram | Sunitha Beeram |
| . | tingchen | Ting Chen |
| . | xhsun | Xiaohui Sun |
| . | xiangfu | Xiang Fu |
| . | yupeng | Yupeng Fu |


-  [Board Reports](https://whimsy.apache.org/board/minutes/pinot.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2018-10-18 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| NA | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| NA | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| NA | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2018-10-20 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2018-10-18 | Ask infrastructure to set up and archive mailing lists. |
| 2018-10-16 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2019-03-08 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2018-10-01 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2018-10-24 | Subscribe all Mentors on the pmc and general lists. |
| 2018-10-24 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2018-10-24 | Tell Mentors to track progress in the file 'incubator/projects/pinot.xml' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2019-01-31 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2019-01-31 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2019-01-31 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2019-01-31 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2019-01-31 | Check that all active committers have submitted a contributors agreement. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? - YES

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) - YES

- Are project decisions being made in public by the committers? - YES

- Are the decision-making guidelines published and agreed to by all of the committers? - YES

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? - YES

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
