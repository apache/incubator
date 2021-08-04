Title: PDFBox Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The PDFBox project graduated on 2009-10-21</span>


PDFBox is an open source Java library for working with PDF documents.



- 2009-10-21: Board passed resolution to establish Apache PDFBox as a TLP

- 2009-09-23: First release of Apache PDFBox

- 2009-05-05: First release of Apache FontBox

- 2009-04-07: First release of Apache JempBox

- 2008-12-15: New committer: Brian Carrier

- 2008-12-15: New committer: Andreas Lehmkühler


-  [PDFBox website](http://incubator.apache.org/pdfbox/) 

-  [Old PDFBox website](http://www.pdfbox.org/) 

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/pdfbox/](http://incubator.apache.org/pdfbox/)  |
|  | wiki | . |
| Mailing list | dev |  [pdfbox-dev@incubator.apache.org](mailto:pdfbox-dev-subscribe@incubator.apache.org)  |
|  | users |  [pdfbox-users@incubator.apache.org](mailto:pdfbox-users-subscribe@incubator.apache.org)  |
|  | commits |  [pdfbox-commits@incubator.apache.org](mailto:pdfbox-commits-subscribe@incubator.apache.org)  |
| Bug tracking | Jira |  [https://issues.apache.org/jira/browse/PDFBOX](https://issues.apache.org/jira/browse/PDFBOX)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/incubator/pdfbox/](http://svn.apache.org/repos/asf/incubator/pdfbox/)  |
| Mentors | jukka | Jukka Zitting |
|  | jeremias | Jeremias Märki |
| Committers | blitchfield | Ben Litchfield |
|  | danielwilson | Daniel Wilson |
|  | pkoch | Philipp Koch |
|  | lehmi | Andreas Lehmkühler |
|  | carrier | Brian Carrier |
| Extra | . | . |



November 2008

Apache PDFBox is an open source Java library for working with PDF documents. PDFBox entered incubation on February 7th, 2008.


The website has been set up. The license review is underway and has already progressed quite far. The export control notification has been set up. These tasks and most other tasks were all performed by PDFBox mentors (mostly by Jukka Zitting). Sadly, there has been almost no participation by the initial committers, yet, except for handling the license grants and CLAs.


On the user side, some questions don't seem to get answered. Not many patches have reached us, either.


Issues before graduation:



- Increase community size and activity

- Finish license review

- First Apache release


August 2008

Apache PDFBox is an open source Java library for working with PDF documents. PDFBox entered incubation on February 7th, 2008.


We have finally migrated all sources to Apache svn and set up the project website at http://incubator.apache.org/pdfbox/. We also set up a CI build using Hudson. Traffic is picking up on the user and developer mailing lists, new issues are being reported through Jira, and there is initial discussion about an incubating 0.8.0 release.


Software Grants have been received from Ben Litchfield and Daniel Wilson who are the primary authors of the PDFBox, FontBox and JempBox software. There have been a lot of small contributions (under the BSD license) by a number of other people to the project and it was asked (see http://markmail.org/message/zy6oweihmenqt6o4) on the legal-discuss list whether the primary authors have "sufficient rights" to grant a license for all of the code, or if we have to contact all the other contributors for separate grants. Having received no response to the question on legal-discuss we assumed that software grants from the primary authors was sufficient.


We're discussing about what to do with the FontBox and JempBox codebases that are included as subprojects of PDFBox. We might decide to merge them with similar efforts in other Apache projects, most notably XML Graphics.


Issues before graduation:



- Increase community size and activity

- License review

- Export control notifications

- First Apache release


April 2008

PDFBox is an open source Java PDF library for working with PDF documents. PDFBox entered incubation on February 7th, 2008.


The contents of the issue trackers at SourceForge have been migrated to Jira. We've also created a pdfbox-users mailing list and plan to point people from the SourceForge support forums to that list. The project sources have not yet been migrated to Apache svn.


Issues before graduation:



- Bring the sources to Apache

- Increase community size and activity

- Release once all licensing and export issues are resolved


March 2008

PDFBox is an open source Java PDF library for working with PDF documents. PDFBox entered incubation on February 7th, 2008.


The basic project infrastructure (lists, svn, jira, etc.) is already in place, and we are currently working on migrating the source code and existing issues from SourceForge. We have also requested a user mailing list to replace the current help forums on SourceForge.


PDFBox uses the Bouncy Castle crypto libraries for handling encrypted PDF files. We will take care of export control issues as we proceed with importing the PDFBox sources to Apache.



February 2008

PDFBox is an open source Java PDF library for working with PDF documents. PDFBox entered incubation on February 7th, 2008.


The PDFBox project has just entered incubation, and we're currently setting up the project infrastructure. A question about the licensing of the JAI dependency was voiced on the mailing list.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2009-01-16 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| NA | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| NA | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2009-01-16 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2008-02-07 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2008-02-10 | Subscribe all Mentors on the pmc and general lists. |
| 2008-02-10 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2009-01-16 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-01-16 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2009-01-16 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2009-08-23 | Check and make sure that for all code included with the distribution that is not under the Apache license, have the right to combine with Apache-licensed code and redistribute. (see [LEGAL-36](https://issues.apache.org/jira/browse/LEGAL-36) and [LEGAL-55](https://issues.apache.org/jira/browse/LEGAL-36) for further details) |
| 2009-01-16 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2009-01-16 | Check that all active committers have submitted a contributors agreement. |
| 2008-04-14 | Add all active committers in the STATUS file. |
| 2008-04-14 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2008-04-14 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2008-02-10 | Ask infrastructure to set up and archive Mailing lists. |
| 2008-04-14 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| ....-..-.. | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- Are project decisions being made in public by the committers?

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
