Title: XYZ Codebase Intellectual Property (IP) Clearance Status

 `-----8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;---- cut here-------8-&lt;----` 
# Preamble {#premable}

This document (or rather the source of it) is the template for recording IP clearance on new codebases. Please store the completed document in this Incubator repository using a filename that reflects your project.


One of the Incubator's roles is to ensure that proper attention is paid to intellectual property. From time to time, an external codebase is brought into the ASF that is not a separate project, but still represents a substantial contribution that was not developed within the ASF's source control system. This is a short form of the Incubation checklist, designed to allow code to be imported with alacrity while still providing for oversight.


This form is not for new projects. The intent is to simply help to ensure, and record, that due diligence (Software Grant, Individual CLA, Corporate CLA, license and dependencies) has been paid to the incoming code, so that it can be merged into an existing project/module.


Either an Individual CLA or Corporate CLA is preferred to a Software Grant. All authors must sign an Individual CLA; or all owners of IP must sign one of the three documents and send to secretary (reference [ASF Licenses](http://www.apache.org/licenses/#clas) ).


The receiving PMC is responsible for doing the work. The Incubator is simply the repository of the needed information. Once a PMC directly checks-in a filled-out short form, everything is done.


All PMCs must handle incoming code in this way. Any code that was developed outside of the ASF SVN repository must be processed like this, even if the external developer is an ASF committer.


# Process {#process}


1. IP Clearance processing must be executed either by an Officer or a Member of the ASF. _If you are not an Officer or a Member, please contact your project chair who will find an appropriate volunteer._ Incubator karma is also required. Please request karma from the incubator pmc if you do not have it.

1. (Optional) _Commit an outline [form](#form-filling) , filling those parts which can be (at this stage)_ .

1. A software grant must be provided to the ASF. This grant can either be done by the ASF Corporate CLA (via Schedule B) or the Software Grant Agreement. The completed and signed grant must be emailed to secretary@apache.org

1. Receipt of the software grant form **must** be acknowledged by an Officer of the ASF by recording in the correct file ( _grants.txt_ for a License Grant or _cclas.txt_ for a Corporate CLA). In most normal circumstances, the officer should be the ASF Secretary, who must be provided a copy of the grant or CCLA in any case (if not originally sent or Emailed to him).

1.  **Note:** the grant form **must** be acknowledged before continuing. If the source is referenced by checksum in the grant, commit the canonical tarball for the donated code into the incubator drop area (/repos/asf/incubator/donations) together with a checksum and a detached signature. This will ensure that apache has a legal record of the grant.

1. Complete and commit the [completed form](#form-filling) .

1. Post a message to general@incubator prefixed [IP CLEARANCE] asking for clearance to be checked. Sign off is by lazy consensus so wait at least 72 hours for a -1.

1. Post a [RESULT] to close the thread and let the project know that the code has been cleared for import.

# Filling The Form {#form-filling}

What to do to set it up:



- copy this file and re-name it according to incubator/public/trunk/content/ip-clearance/${project-codebase}.xml

- add a row to the table at incubator/public/trunk/content/ip-clearance/index.xml

- make a snapshot of the source code available for review

The snapshot should not last long in place before it is moved to the successful incubation area. The sole purpose is to ensure that IP is cleared so that the codebase can be merged into the ASF SVN.


For this file:



- substitute the XYZ name with the real one

- fill in the description

- fill in the work items

- remove this notice

- set a proper "title" element for the html page

When a work item is done, place the date in the supplied space.


 _On the first edit of this file, please delete this notice._ 

 `-----8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;---- cut here-------8-&lt;----` 
Describe the incoming codebase, including whether it is a large set of patches, new functional modules, etc.



- Which PMC will be responsible for the code


- Into which existing project/module


- Officer or member managing donation:

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| ....-..-.. | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

MD5 or SHA1 sum for donated software: ( _Note versioned software used to calculate sum in parentheses_ ).


## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _the name of the grant as recorded in the foundation/officers area, in either grants.txt or cclas.txt, so that the grant can be easily identified. If recorded in the grants.txt document, use the "for" or title. If recorded in the cclas.txt document, use the company name (field 2 without submitter name) and the "form on file" name (field 4, without any people's names)._ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _For individuals, use the name as recorded on the committers page_ 

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have a signed CLA on record. |
| ....-..-.. | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| ....-..-.. | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  _The VOTE thread accepting the donation may happen either before or after IP clearance. Adoption by lazy concensus is acceptable but not recommended._ 
