Title: uimaFIT Codebase Intellectual Property (IP) Clearance Status


uimaFIT provides Java annotations for describing UIMA components which can be used to directly describe the UIMA components in Java code without the need for traditional UIMA XML descriptors. This greatly simplifies refactoring a component definition (e.g., changing a configuration parameter name). uimaFIT also makes it easy to instantiate UIMA components without using XML descriptor files by providing convenient factory methods. This makes uimaFIT an ideal library for testing UIMA components because the component can be easily instantiated and invoked without requiring a descriptor file to be created first. uimaFIT is very useful in research environments in which programmatic/dynamic instantiation of UIMA pipelines can simplify experimentation. For example, when performing 10-fold cross-validation across a number of experimental conditions, it can be quite laborious to create a different set of descriptor files for each run, or even a script which generates such descriptor files. uimaFIT is type system agnostic and does not depend on (or provide) a specific type system


uimaFIT is contributed as a multi-module Maven project.



- The UIMA PMC is responsible for the code.


- The code will be imported into https://svn.apache.org/repos/asf/uima/sandbox/uimafit as part a of the UIMA project.


- Marshal Schor and Richard Eckart de Castilho are responsible for managing the donation process.

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2012-12-10 | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

The code is available here: http://code.google.com/p/uimafit/downloads/detail?name=uimaFIT-grant-staging-rev-919.zip and SHA1 sum for donated software: 010d2f2880cd502b08a6e2659041aa025689cd20 ( _Note versioned software used to calculate sum in parentheses_ ).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2012-12-11 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2012-12-27 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _uimaFIT source code and wiki contents_ , and a Software Grant recorded with Corporate CLAs:



- Signed Corp CLA for Philip Ogren, Steven Bethard, Chris Roeder, Philipp Wetzler for uimaFIT by the Regents of the University of Colorado, CO, USA

- Signed Corp CLA for Niklas Jakob, Richard Eckart de Castilho, Shuo Yang, Torsten Zesch for uimaFIT by the Technische Universität Darmstadt, Germany

## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _Regents of the University of Colorado, CO, USA_ 

-  _Technische Universität Darmstadt, Germany_ 

-  _Steven Bethard_ 

-  _Fabio Mancinelli_ 

| date | item |
|------|------|
| 2012-12-25 | Check that all active committers have a signed CLA on record. |
| 2012-12-25 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2012-12-25 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2012-12-25 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



- http://markmail.org/message/rkru7hrwblhc6tvk

- http://mail-archives.apache.org/mod_mbox/uima-dev/201210.mbox/ajax/%3CFF46A436B80DCD43A9D7E64209F33ACB460A30C2%40FANSWORTH.ukp.informatik.tu-darmstadt.de%3E
