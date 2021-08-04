Title: Jackrabbit Bundle Persistence Codebase Intellectual Property (IP) Clearance Status


The contribution is a set of "bundle persistence manager" components for Apache Jackrabbit. The contribition will be included as new Java classes and packages in the existing jackrabbit-core component. The contribution also contains minor changes to existing Jackrabbit classes.


The contributed code is attached to issue [JCR-755](http://issues.apache.org/jira/browse/JCR-755) with the following description:


 _we (day software) offer our set of bundle persistence managers to the jackrabbit project. those pms combine the node and property states into a single bundle and store them together. this improves performance and reduces storage-memory overhead (no exact numbers available). The bundle pms also have a "bundle-cache" that does a memory sensitive caching of the bundles and a negative cache for non-existent bundles. small binary properties are inlined into the bundle rather than stored in the blobstore._ 



- Which PMC will be responsible for the code: Apache Jackrabbit


- Into which existing project/module: jackrabbit-core


- Officer or member managing donation: Jukka Zitting

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| NA | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

MD5 sum for donated software: a8accf17e35d1dec52f5b4fcc277bb9e (calculated using OpenSSL version 0.9.8d).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2007-03-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2007-02-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: Set of "bundle persistence manager" components for Apache Jackrabbit


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights: Day Management AG


| date | item |
|------|------|
| 2007-02-28 | Check that all active committers have a signed CLA on record. |
|  [2007-02-28](http://mail-archives.apache.org/mod_mbox/jackrabbit-dev/200702.mbox/%3c510143ac0702280624y5bcd87bn4d109dcb0ead14c7@mail.gmail.com%3e)  | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2007-02-28 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2007-02-28 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [Vote on dev@jackrabbit.apache.org](http://mail-archives.apache.org/mod_mbox/jackrabbit-dev/200702.mbox/%3c8be731880702230825v34fc0187sbd950248182a1fb3@mail.gmail.com%3e) 
