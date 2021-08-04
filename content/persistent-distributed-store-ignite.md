Title: Ignite Persistent Store Codebase Intellectual Property (IP) Clearance Status


The donated persistent store is a distributed and transactional disk storage that seamlessly integrates with Apache Ignite 2.0 page memory architecture. One of the main advantages of the store is that Apache Ignite becomes a fully operational from disk (SSD or Flash) without any need to preload the data in memory. Plus, with full SQL support already available in Apache Ignite, this feature will allow Apache Ignite serve as a distributed transactional database, both in memory and on disk, while continuing to support all the existing use cases.<br></br>Refer to these wiki pages for more details:

-  [Persistent Store Design](https://cwiki.apache.org/confluence/display/IGNITE/Persistent+Store+Overview) 

-  [Persistent Store Architecture](https://cwiki.apache.org/confluence/display/IGNITE/Persistent+Store+Architecture) 




- Apache Ignite PMC will be responsible for the code.


- The persistent store will be added under "pds" and "core" modules.


- Officer or member managing donation: Denis Magda (Apache Ignite PMC Chair)

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2017-05-12 | Branch: https://github.com/agoncharuk/ignite/tree/pds-donate<br></br>Commit: https://github.com/agoncharuk/ignite/commit/1cce2fcc960c5098cc684b6138ed306daf5dd5e4<br></br>MD5 or SHA1 sum for donated software: MD5 (ignite-pds-donate.zip) = 10c87c969cd836deb94172db384039f6 ( _md5 tool from Mac OS_ ). |
| 2017-05-22 | The persistent store code base was committed to Apache Ignite repository's branch:<br></br>https://github.com/apache/ignite/tree/ignite-5267 |
| 2017-06-16 | The persistent store code base was moved to the different branch due to a variety of changes. The "pds" module is discontinued - all the codebase merged to "ignite-core" component:<br></br>https://github.com/apache/ignite/tree/ignite-5267-1 |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2017-05-13 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2017-05-16 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: Ignite Persistent Store


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



- GridGain Systems, Inc.

| date | item |
|------|------|
| 2017-05-12 | Check that all active committers have a signed CLA on record. |
| 2017-05-12 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2017-05-12 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2017-05-12 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [IP Clearance vote on general@incubator.](http://apache-incubator-general.996316.n3.nabble.com/RESULT-IP-CLEARANCE-Apache-Ignite-Persistent-Store-td55050.html) 

-  [Donation acceptance vote on Apache Ignite dev list.](http://apache-ignite-developers.2346864.n4.nabble.com/RESULT-VOTE-Accept-Contribution-of-Ignite-Persistent-Store-td18096.html) 
