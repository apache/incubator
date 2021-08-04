Title: Calcite-Avatica-Go Codebase Intellectual Property (IP) Clearance Status


Calcite-Avatica-Go is a client for Apache Phoenix and Apache Calcite Avatica written in the Go programming language and contributed by Boostport. It describes itself as "Apache Phoenix/Avatica SQL Driver". It is self-contained module, and a medium-sized code base (30 files, 8,000 lines of code). Because it is a different language from current Avatica (Go versus Java) it will probably become a new module in a new git repo and separate releases. It remains to be decided whether we keep the Phoenix-specific customizations in this module or apply those directly in Phoenix.



- PMC that will be responsible for the code: Apache Calcite PMC

- Into which existing project/module: Apache Calcite Avatica

- Officer or member managing donation: Julian Hyde (jhyde)

- Tracking case: [ [CALCITE-1240](https://issues.apache.org/jira/browse/CALCITE-1240) ]

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2017-07-27 |  [https://github.com/Boostport/avatica/commit/77207918cf826662cb4ea40cfffbfb5cb64bf4a0](https://github.com/Boostport/avatica/commit/77207918cf826662cb4ea40cfffbfb5cb64bf4a0) or [http://people.apache.org/~jhyde/boostport-avatica.patch](http://people.apache.org/~jhyde/boostport-avatica.patch) . |

 `$ sha1sum boostport-avatica.patch 
ba7441f20261409a2d5b38a88e5d8d6b0d826b86  boostport-avatica.patch
$ sha1sum --version 
sha1sum (GNU coreutils) 8.21
$ md5sum boostport-avatica.patch
6f66ce5756b67ecddb35bf1030c49a0b  boostport-avatica.patch
$ md5sum --version 
md5sum (GNU coreutils) 8.21` 


## Copyright {#Copyright}

| date | item |
|------|------|
| 2017-07-27 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.<br></br><br></br>Corporate CLA for "Boostport Pty Ltd" is already on file in cclas.txt. |
| 2017-07-27 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright<br></br><br></br>There are no copyright notices or other file headers in the code, therefore nothing to change. Code already includes an Apache License. |

Identify name recorded for software grant: calcite-avatica-go


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



- Francis Chuang (francischuang)

- Boostport Pty Ltd

| date | item |
|------|------|
| 2017-07-27 | Check that all active committers have a signed CLA on record. |
| 2017-07-27 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2017-07-27 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute.<br></br><br></br>Not applicable. The code is 100% Apache Licensed. |
| 2017-07-27 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.<br></br><br></br>The project has one category B dependency (go-cleanhttp is MPL), and we intend to address this before release; others are category A. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [[DISCUSS] Accept Boostport's Avatica Go client into Calcite/Avatica](http://mail-archives.apache.org/mod_mbox/calcite-dev/201707.mbox/%3CCAPSgeESfUwzKHudgH%3D1Lunvn4WJk29iR3mpxfay5KshQESoe0A%40mail.gmail.com%3E) thread on dev@calcite

-  [Vote thread on general@incubator started on 2017-07-28](https://s.apache.org/calcite-avatica-go-clearance-vote) 

-  [Vote on general@incubator passed on 2017-08-03](https://s.apache.org/calcite-avatica-go-clearance-result) 

-  [Vote on Calcite PMC passed on 2017-08-07](https://s.apache.org/calcite-avatica-go-pmc-result) 
