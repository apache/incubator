Title: Arrow Plasma Object Store Intellectual Property (IP) Clearance Status


The Plasma Object Store provides a server process, reference C++ client, and Python binding for managing a collection of binary "objects" in POSIX shared memory. Applications use a lightweight messaging protocol to create and delete memory blocks in the object store, evict objects to make room for new objects, and increment and decrement reference counts to indicate shared ownership of memory. It also provides for subscribing to notifications about object activity. The system helps simplify ownership transfer and memory lifetime of shared memory blocks, which can be much more complicated in a peer-to-peer architecture.


The object store has been used in conjunction with the Apache Arrow libraries to provide for zero-copy access to collections of large objects stored in shared memory. Incorporating this project into Apache Arrow will help the community continue to develop and innovate technology for low-overhead sharing of complex datasets across multiple processes.


The Apache Arrow PMC will be responsible for the code.


It will be integrated into the Apache Arrow project, into the C++ part of the main Arrow source tree and build system.


The following people will be managing this contribution:



- Jacques Nadeau (Apache Arrow PMC Chair)

- Julian Hyde (Apache Arrow PMC Member)

- Wes McKinney (Apache Arrow PMC Member)

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2017-07-27 | Trademark and Google Search found no use of name as software product. |


- Origin: [https://github.com/ray-project/arrow-plasma-object-store](https://github.com/ray-project/arrow-plasma-object-store) as at commit ID 11795753b0850cf5ad50d640067a8517ad8629a2.

- Download link: [11795753b0850cf5ad50d640067a8517ad8629a2.tar.gz](https://github.com/ray-project/arrow-plasma-object-store/archive/11795753b0850cf5ad50d640067a8517ad8629a2.tar.gz) 

- SHA1: 242fad7ce3a592c82865c3fe44f951b91e491b4f

- SHA256: 64353a8ce8051ec3a75804f82d1da5880fad5b43d7fffe830ed1343674c7a5f2

## Copyright {#Copyright}

| date | item |
|------|------|
| 2017-07-27 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: arrow-plasma-object-store


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



- Philipp Moritz

- Robert Nishihara

- Richard Shin

- Stephanie Wang

- Alexey Tumanov

- Ion Stoica

- Ujval Misra

- Mehrdad Niknami

| date | item |
|------|------|
| 2017-07-27 | Check that all active committers have a signed CLA on record. |
| 2017-07-27 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2017-07-27 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2017-07-27 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related votes:



-  [Vote on Apache Arrow dev list to determine whether the Arrow PMC is in favor of accepting the code contribution, passed on 2017-07-22](https://s.apache.org/arrow-plasma-object-store-pmc-vote) 

-  [Vote thread on general@incubator started on 2017-08-02](https://s.apache.org/arrow-plasma-object-store-clearance-vote) 

-  [Vote on general@incubator passed on 2017-08-07](https://s.apache.org/arrow-plasma-object-store-clearance-result) 
