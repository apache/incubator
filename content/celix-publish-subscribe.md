Title: Celix Publish Subscribe Codebase Intellectual Property (IP) Clearance Status


A distributed service oriented implementation of the publish subscribe pattern. The design depends on 3 modules. A module for discovery, another module for serialization and transport and lastly a topology manager module which control the other modules. Multiple implementation can of the modules can be used to offer different technologies (e.g discovery using etcd or mdns). This donation contains: A PubSub Topology Manager implementation, A PubSub discovery implementation using etcd, A PubSub transport/serialization implementation using UDP multicast / JSON and an alternative PubSub transport/serialization implementation using ZeroMq / JSON.



- Which PMC will be responsible for the code


- Into which existing project/module


- Officer or member managing donation:

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2017-01-27 | https://issues.apache.org/jira/browse/CELIX-389 SHA1 sum 7a28119a6805cd82289eb41674628ea502fdccac |

MD5 or SHA1 sum for donated software: (Note versioned software used to calculate sum in parentheses).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2017-01-27 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2017-01-27 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

 _Identify name recorded for software grant: Celix publish-subscribe_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _For individuals, use the name as recorded on the committers page_ 

| date | item |
|------|------|
| 2017-01-27 | Check that all active committers have a signed CLA on record. |
| 2017-01-27 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2017-01-27 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2017-01-27 See [1] | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.A part of the donation has LGPL |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


[1]: A part of the donation depends on a library using LGPL. This part is optional and not required to use Apache Celix or use the service oriented publish subscribe implementation. This is discussed in issue https://issues.apache.org/jira/browse/LEGAL-286.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [Vote Thread](http://mail-archives.apache.org/mod_mbox/celix-dev/201701.mbox/%3CCAPhv5g-Nxbpk7vKgASRbRvmu9SRmvY8g-bvaT1hm5j58z7%2B%2Bew%40mail.gmail.com%3E) 

-  [Vote Result](http://mail-archives.apache.org/mod_mbox/celix-dev/201701.mbox/%3CCAPhv5g_toA%2Bqthos%3DGHgoRS47cKY%3DY2TxCTiEOMHzcLxK_sMBg%40mail.gmail.com%3E) 
