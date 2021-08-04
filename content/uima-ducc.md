Title: UIMA-DUCC Codebase Intellectual Property (IP) Clearance Status


Distributed UIMA Cluster Computing (DUCC) is a cluster management system providing tooling, management, and scheduling facilities to automate the scale-out of applications using the UIMA framework.


Core UIMA provides a generalized framework for applications that process unstructured information such as human language, but does not provide a scale-out mechanism. UIMA-AS provides a scale-out mechanism to distribute UIMA pipelines over a cluster of computing resources, but does not provide job or cluster management of the resources. DUCC completes the set by providing job support, cluster management, and life-cycle automation for the scale-out of UIMA applications, using UIMA-AS, on large computing clusters


The contribution includes components that use Apache ActiveMQ and Apache Camel as a messaging infrastructure. It also includes Jetty to display DUCC's cluster information in web browsers, as well as enabling cluster control.


The contributed code is in the "sandbox" area of the UIMA SVN: http://svn.apache.org/viewvc/uima/sandbox/uima-ducc/ , where it is being cleaned up and otherwise worked on. The original donation is in a zip file attached to a JIRA issue: https://issues.apache.org/jira/browse/UIMA-2491.


The donation codebase is a set of new modules and documentation and does not contain patches for other components.



- Which PMC will be responsible for the code: Apache UIMA


- This donation is being initially imported into the Apache UIMA project in the "sandbox" under the top level directory "uima-ducc"


- Officer or member managing donation: Marshall Schor.

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2013-11-15 | A trademark search for DUCC acronym using http://www.uspto.gov/trademarks/ turned up some possible concerns. We reviewed this with Trademarks at Apache who said it was OK to proceed. |

The MD5 sum for donated software: f8cbb2dde7f1b868d3ed50f895145902 ( _md5 calculated using Microsoft File Checksum Integrity Verifier (FCIV)_ ).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2012-12-17 | ASF received a Software Grant for all the code. |
| 2012-12-28 | All donated source files were updated or checked to make sure each includes ASF copyright, with the exception of some test/configuration data. |

Identify name recorded for software grant: _file: ibm-ducc.pdf; for: DUCC source code, documentation, and test cases_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _IBM Corporation_ 

| date | item |
|------|------|
| 2012-12-05 | Discussed with active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2012-12-10 | All active committers have a signed CLA on record. |
| 2012-12-11 | Checked all items included with the distribution not under the Apache license, that we have the right to combine with Apache-licensed code and redistribute. |
| 2012-12-11 | Checked Licenses for compatibility with the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1. |

# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  _Unanimously accepted; http://mail-archives.apache.org/mod_mbox/uima-dev/201210.mbox/%3CCAO329yBSD-zqh-znOzSyBBxt5r3-a6ocTmXznmwR5bC3d_Mfdg%40mail.gmail.com%3E_ 
