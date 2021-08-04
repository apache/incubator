Title: PaDaF Preflight Codebase Intellectual Property (IP) Clearance Status


PaDaF provides tools to make a PDF/A preflight on a PDF document. It is highly based on Apache PDFBox. Conformance to the ISO 19005 (PDF/A) norm is checked.


The contributed code is attached to issue [PDFBOX-1056](https://issues.apache.org/jira/browse/PDFBOX-1056) with the following description:


 _We (Atos Worldline) donate our PDF/A validator to the PDFBox project. This product is based on PDFBox and a javacc parser. Before this donation, the product was already distributed under Apache Licence 2. Its current name is padaf. Padaf complies the isartor test suite. This version depends on standard PDFBox 1.5.0 version. Only one test class does not compile with current HEAD (on 27 of june), all other test cases pass. Padaf is composed of 2 modules :

- preflight : the validator

- xmpbox : an other implementation of xmp parser and writer. We make that choice because we did not have the time to propose all necessary modification in jempbox.
The attached tar ball contains :

- sources of the 2 modules

- junit tests for each one

- a parent (that will soon disappear) already depending on pdfbox-parent
_ 



- Which PMC will be responsible for the code: Apache PDFBox


- Into which existing project/module: preflight and xmpbox


- Officer or member managing donation: Andreas Lehmkühler

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2011-07-17 | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

SHA1 sum for donated software: b9bb323fa73e1416a8b282fe2a687cebf1ac2145 ( _calculated using sha1sum version 8.4_ ).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-07-08 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-07-17 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _/documents/grants/atos-worldline-padaf.pdf_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights: ATOS Worldline


| date | item |
|------|------|
| 2011-07-21 | Check that all active committers have a signed CLA on record. |
| 2011-07-21 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2011-07-13 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-07-13 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [[RESULT][VOTE] Accept the PaDaF contribution (PDFBOX-1056)](http://mail-archives.apache.org/mod_mbox/pdfbox-dev/201107.mbox/%3C4E232710.50409@lehmi.de%3E) 
