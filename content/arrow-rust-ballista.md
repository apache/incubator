Title: Apache Arrow Rust Ballista Codebase Intellectual Property (IP) Clearance Status


Arrow Rust Ballista is a distributed scheduler and query engine that depends on components in the existing Rust Arrow project.



- The Apache Arrow PMC will be responsible for the code


- It will be integrated into the Apache Arrow project


- Officer or member managing donation: Andy Grove (Apache Arrow PMC Member)

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2021-04-01 | Trademark search found two active trademarks for software products named Ballista; an [operating system for drones from Dreamhammer, Inc](https://tmsearch.uspto.gov%2Fbin%2Fshowfield%3Ff%3Ddoc%26state%3D4802%3Aoty9vz.2.11) and a [VR game from High Voltage Software](https://tmsearch.uspto.gov%2Fbin%2Fshowfield%3Ff%3Ddoc%26state%3D4802%3Aoty9vz.2.3) . A Google search found a [software testing product named Ballista from Carnegie Mellon University](http://users.ece.cmu.edu%2F~koopman%2Fballista/) where they state that Ballista is a registered trademark. |

Origin: [https://github.com/ballista-compute/ballista](https://github.com/ballista-compute/ballista) , which is being contributed in reduced form in the following Apache Arrow PR: [https://github.com/apache/arrow/pull/9723](https://github.com/apache/arrow/pull/9723) 


## Copyright {#Copyright}

| date | item |
|------|------|
| 2021-04-01 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _the name of the grant as recorded in the foundation/officers area, in either grants.txt or cclas.txt, so that the grant can be easily identified. If recorded in the grants.txt document, use the "for" or title. If recorded in the cclas.txt document, use the company name (field 2 without submitter name) and the "form on file" name (field 4, without any people's names)._ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _Andy Grove_ 

| date | item |
|------|------|
| 2021-04-05 | Check that all active committers have a signed CLA on record. **There are 22 commits from 11 contributors that do have CLAs on file and have not responded to requests to submit one. See the [audit spreadsheet](https://docs.google.com/spreadsheets/d/19rIp24Jvi9KEEq3f8_fxqrThdH0dAaoTKiB0jNapDcY/edit?usp=sharing) for full details but most of these commits are implementing serde code to translate between protobuf data structures and Ballista data structures. There are also trivial code cleanup commits, and one small feature, one bug fix, and two performance optimizations. If any of the authors later object to their code being included, it will be trivial to remove the commits and then re-implement the changes without referencing their original work.**  |
| 2021-04-05 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2021-04-05 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2021-04-05 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [The VOTE thread on the Apache Arrow dev@ mailing list accepting the donation](https://lists.apache.org/thread.html/rb4746aabbfa5a9d7f987db59375315235a78a7ef11dec0bd2a928eb6%40%3Cdev.arrow.apache.org%3E) 
