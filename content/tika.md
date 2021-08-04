Title: Apache Tika Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise.


<span class="graduated">The Tika project graduated on 2008-10-28</span>


Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries.



-  **2008-10-28:** Tika graduates into a Lucene subproject

-  **2008-10-01:** Dave Meikle added as new committer

-  **2008-04-07:** Niall Pemberton added as new committer

-  **2007-12-27:** Apache Tika 0.1-incubating released

-  **2007-10-02:** Keith Bennett added as new committer

-  **2007-03-22:** Apache Tika begins incubation

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/tika/](http://incubator.apache.org/tika/)  |
| Mailing list | dev |  `tika-dev`  `@`  `incubator.apache.org`  |
|  | commits |  `tika-commits`  `@`  `incubator.apache.org`  |
| Moderators | jukka | Jukka Zitting |
| Bug tracking | jira |  [https://issues.apache.org/jira/browse/TIKA](https://issues.apache.org/jira/browse/TIKA)  |
| Source code | svn |  [https://svn.apache.org/repos/asf/incubator/tika/](https://svn.apache.org/repos/asf/incubator/tika/)  |
| Sponsor |  |  [Apache Lucene PMC](http://lucene.apache.org/)  |
| Mentors | cutting | Doug Cutting |
|  | bdelacretaz | Bertrand Delacretaz |
|  | jukka | Jukka Zitting |
| Committers | ridabenjelloun | Rida Benjelloun |
|  | mharwood | Mark Harwood |
|  | mattmann | Chris A. Mattmann |
|  | siren | Sami Siren |
|  | jukka | Jukka Zitting |
|  | kbennett | Keith Bennett |
|  | niallp | Niall Pemberton |
|  | dmeikle | Dave Meikle |

# October 2008 {#October 2008}

Apache Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 



- Dave Meikle was just voted in as a new committer.

- Paolo Mottadelli will present Tika at ApacheCon US.

 **Development** 



- Tika 0.2 should be released soon.

- Usage documentation has been added to the website.

 **Issues before graduation** 



- The current plan is to graduate as a Lucene subproject, which could happen soon as the incubation criteria seem to be met.

# July 2008 {#July 2008}

Apache Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 



- Tika community remains relatively small, with just a handful of active members

 **Development** 



- Work towards Tika 0.2 continues, Chris Mattman has volunteered to be the release manager

 **Issues before graduation** 



- Increase the size and diversity of the community (or graduate into a Lucene subproject?)

# April 2008 {#April 2008}

Apache Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 



- Niall Pemberton joined the project as a committer and PPMC member

- The number of issues reported by external contributors is growing gradually

- There was a Fast Feather Talk on Tika in ApacheCon EU 2008

- We have good contacts especially with Apache POI and PDFBox

 **Development** 



- We are working towards Tika 0.2

- Metadata handling improvements are being discussed

 **Issues before graduation** 



- Increase the size of the community

# January 2008 {#January 2008}

Tika (http://incubator.apache.org/tika) is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser Libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 



- No new committers since the last report, activity has been moderate but steady, leading to the 0.1 release.

 **Development** 



- Tika 0.1 (incubating) has just been released.

- Chris Mattmann intends to use that release in Nutch, That's good progress towards Tika's goal of providing data extraction functionality to other projects.

- A new Tika logo was created by Google Highly Open Participation student, hasn't been integrated yet.

 **Issues before graduation** 



- Now that the first release is out, we need to work on growing the community and figuring out how to best interact with external parser projects.

# October 2007

Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 


There have been a number of positive items within Tika during the last few months. The traffic on the Tika mailing list has increased significantly (with typically 2, 3 questions, and 1 or 2 commits every day, or every other day), and there have been a lot of recent inquiries from external projects wanting to collaborate with Tika (including Aperture, PDFBox and a fellow developing a JSon library currently hosted at Google code). In addition, Tika's architecture has become a recent discussion of interest (as we'll see below).


We recently elected Keith Bennett as a new committer to Tika. Keith has been spearheading many of the new patches committed to Tika, as well as participating in discussions about the architecture, and future direction of the project.


Tika will be represented at the "Fast Feather" track at ApacheCon US by Jukka Zitting. The rest of the community is helping to create the content for the presentation. The abstract is listed below:


> Tika is a new content analysis framework borne from the desire to factor our commonality from the Apache Nutch search engine framework. Tika provides a mime detection framework, an extensible parsing framework and metadata environment for content analysis. Though in its nascent stages, progress on Tika has recently taken shape and the project is nearing a stable 0.1 release. In this talk, we'll describe the core APIs of Tika and discuss its use in several distinct domains including search engines, scientific data dissemination and an industrial setting.

 **Development** 


There have been a flurry of JIRA issues and code activity (http://issues.apache.org/jira/browse/TIKA) including 47 issues currently in JIRA, with 32 resolved issues, 14 closed issues, and 2 open major/minor issues in progress).


Tika's Parser interface (one of its key components) has just undergone a major overhaul led by Jukka Zitting, and Chris Mattmann has recently contributed a MimeType system (with help from fellow Apache Nutch committer Jerome Charron) to Tika. We also cleaned up and refactored large parts of the rest of the code (removing references to LiusLite and branding the project wherever possible with the Tika name), in preparation for an upcoming 0.1 release.


Chris Mattmann has led an effort to carve out the existing MimeType detection system in Apache Nutch (http://lucene.apache.org/nutch/) and replace it with Tika's improved MimeType detection system. There is a patch sitting in JIRA right now (http://issues.apache.org/jira/browse/NUTCH-562), and barring objections, Nutch will rely on Tika for its MimeType detection abilities.


Also active recently were committers Bertrand Delacretaz, Sami Siren and Rida Benjelloun, committing patches and improvements wherever needed.


 **Issues before graduation** 


No changes since our last report: the Tika project is still at an early stage of incubation. We need to continue bringing in the initial codebases and are targeting an initial incubating release (0.1) probably within the next month. We also need to work on growing the community and figuring out how to best interact with external parser projects.


# July 2007 {#July 2007}

Tika is a toolkit for detecting and extracting metadata and structured text content from various document formats using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 



- The Tika mailing list has seen increased activity in the last weeks, with some new people showing interest for Tika's goals.

- Grant Ingersoll brought the Aperture framework to our attention (http://aperture.sourceforge.net/), which has similar goals to Tika. We will look at possible synergies.

 **Development** 



- No code has been committed since our last report, but some initial code is ready in JIRA and should be committed soon.

 **Issues before graduation** 



- No changes since our last report: the Tika project is still at an early stage of incubation. We need to continue bringing in the initial codebases and probably target for an initial incubating release later this year. We also need to work on growing the community and figuring out how to best interact with external parser projects.

# June 2007 {#June 2007}

Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


 **Community** 


The Tika mailing lists have been relatively quiet lately, probably because with little code we don't yet have many concrete issues to talk about.


 **Development** 


We saw the first piece of Tika code when Chris A. Mattmann ported the Nutch metadata framework to Tika. Rida Benjelloun has created a version of the Lius codebase to be included in Tika, and the code is currently in the issue tracker.


 **Issues before graduation** 


The Tika project is still at an early stage of incubation. We need to continue bringing in the initial codebases and probably target for an initial incubating release later this year. We also need to work on growing the community and figuring out how to best interact with external parser projects.


# May 2007 {#May 2007}

Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries.


Incubating since: March 22nd, 2007.


 **Community** 


We had a good project bootstrap meeting as a part of the text analysis BOF at the ApacheCon EU in Amsterdam. The resulting ideas were summarized on the project mailing list, and the first design threads have started.


 **Development** 


We've started discussing the design of the Tika toolkit. It seems like we will select one of the existing codebases listed in the project proposal as the basis of an early 0.1 release, and start refactoring the code into a more generic toolkit. The Tika svn tree is still empty, but I expect us to see the first code commits before the next report.


 **Infrastructure** 


All the initial infrastructure is now in place. There is still some activity on the temporary Tika wiki on the Google Project hosting service, so we may end up requesting a Tika wiki to be set up on the ASF infrastructure.


 **Issues before graduation** 


The Tika project is still at an early stage of incubation. The most important tasks before graduation are to develop and release the Tika codebase and to grow a diverse and sustainable project community.


# April 2007 {#April 2007}

Tika is a toolkit for detecting and extracting metadata and structured text content from various documents using existing parser libraries. Tika entered incubation on March 22nd, 2007.


The Tika project has just started. The basic infrastructure (mailing lists, subversion, issue tracker, web site) is mostly in place; the only thing still missing is one committer account. We expect to get started with the actual design and code work during the next few weeks.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2007-03-07 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| NA | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| NA | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| NA | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2007-03-08 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2007-03-08 | Subscribe all Mentors on the pmc and general lists. |
| 2007-03-08 | Give all Mentors access to the incubator SVN repository. (to be done by PMC chair) |
| 2007-03-31 | Tell Mentors to track progress in the file 'incubator/projects/tika.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2008-10-17 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2008-10-17 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2008-10-17 | Check and make sure that for all code included with the distribution that is not under the Apache license, have the right to combine with Apache-licensed code and redistribute. |
| 2008-10-17 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2007-03-07 | Check that all active committers have submitted a contributors agreement. |
| 2007-03-31 | Add all active committers in the STATUS file. |
| 2008-10-17 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2007-03-31 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2007-03-31 | Ask infrastructure to set up and archive Mailing lists. |
| 2007-03-31 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2007-05-09 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

See the [issue tracker](https://issues.apache.org/jira/browse/TIKA) .


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
