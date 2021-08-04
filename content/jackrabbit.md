Title: jackrabbit


Jackrabbit has graduated incubation. For more information, please see the [Apache Jackrabbit](http://jackrabbit.apache.org/) project.


<span class="graduated">The Jackrabbit project graduated on 2006-03-15</span>


The Jackrabbit podling has been formed to develop an open source implementation of the Content Repository for Java Technology API (JCR), as specified within the Java Community Process as [JSR 170](http://www.jcp.org/en/jsr/detail?id=170) and [JSR 283](http://www.jcp.org/en/jsr/detail?id=283) . [Day Software](http://www.day.com/) , the JCR specification lead, has licensed an initial implementation of the JCR reference implementation for use as seed code for this project. JCR specifies an API for application developers (and application frameworks) to use for interaction with modern content repositories -- content management systems that provide content services such as versioning, transactions, indexing, workflow, etc.


Jackrabbit's implementation began as a proposal within the [Jakarta Slide](http://jakarta.apache.org/slide/index.html) project, but has since attracted interest from multiple projects with the [Apache Software Foundation](http://www.apache.org/) , including Slide, Cocoon, Lenya, Graffito, XML Indexing, and Derby. We are also looking at integration with projects such as Maven and Beehive.


The purpose of this incubation period is to attract additional contributors from other Apache projects and from the various JSR 170 and 283 expert group companies, learn the Apache way of doing things, and allow the developers to focus on this interface/implementation rather than all of the existing projects that might want to use it. We hope to improve collaboration on the code base by moving all of the active developers and authors to Apache, bring in as many of the Apache veterans as wish to get involved, and open it up to all of the 22 expert group companies. Development of the JCR RI and TCK will occur in this project -- Day Software plans to continue participation in Jackrabbit and use the code in the official RI and TCK releases, allowing developers to beta test against the open source versions as well as the official versions.



- 2006 Mar 15: Incubator PMC approves graduation to new TLP

- 2006 Mar 15: ASF Board approves new Apache Jackrabbit project

- 2006 Mar 11: Committers vote to request incubator graduation

- 2006 Feb 14: Apache Jackrabbit 0.9 released

- 2004 Aug 28: Proposal accepted by Incubator PMC

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://jackrabbit.apache.org/jackrabbit/](http://jackrabbit.apache.org/jackrabbit/)  |
|  | wiki |  [http://wiki.apache.org/jackrabbit/](http://wiki.apache.org/jackrabbit/)  |
| Mailing list | dev | dev jackrabbit.apache.org |
|  | cvs | commits jackrabbit.apache.org |
|  | pmc | private jackrabbit.apache.org |
| Bug tracking | Jira | JCR-* |
| Source code | Subversion | jackrabbit/ |
| Committers | tripod | Tobias Bocanegra |
|  | fielding |  [Roy T. Fielding](http://roy.gbiv.com/) (mentor) |
|  | stefan | Stefan Guggisberg |
|  | shuber | Serge Huber |
|  | fmeschbe | Felix Meschberger |
|  | bcm | Brian Moseley |
|  | uncled | David Nuescheler |
|  | dpfister | Dominique Pfister |
|  | ppiegaze | Peeter Piegaze |
|  | edgarpoce | Edgar Poce |
|  | mreutegg | Marcel Reutegger |
|  | angela | Angela Schreiber |
|  | sylvain | Sylvain Wallez |
|  | jukka | Jukka Zitting |
| Emeritus | stefano | Stefano Mazzocchi (mentor) |
|  | gianugo | Gianugo Rabellino |
|  | prussell | Paul Russell |
|  | treilly | Tim Reilly |
|  | asavory | Andrew Savory |

# 2006/03/13 {#Status20060313}

Jackrabbit accomplished its first official incubating release with version 0.9 of the Apache Jackrabbit reference implementation and JCR-RMI tools. Day Software has confirmed that the version 0.9 jars have passed the JCR 1.0 TCK with the current exclude list.


We are now getting reorganized for graduation from the Incubator to our own top-level project at the Apache Software Foundation. The Jackrabbit committers voted on March 11, 2006, to request graduation. In addition, we made a call to refresh the list of active committers for an accurate presentation to the board; Stefano Mazzocchi, Gianugo Rabellino, Paul Russell, Tim Reilly, and Andrew Savory have requested emeritus status, meaning that they won't be listed on the initial project management committee but are welcome to come back if they choose to rejoin the project at a later time.


# 2006/01/18 {#Status20060118}

Jackrabbit added four new committers to the project this quarter:



- Serge Huber

- Felix Meschberger

- Brian Moseley

- Angela Schreiber

in recognition of their outstanding and sustained contributions to the project. Jukka Zitting has volunteered to be the RM for our first set of incubating releases. We plan to seek graduation from incubator as soon as we have a track record for a successful release vote.


# 2005/10/26 {#Status20051026}

The Apache Jackrabbit podling is slowly recovering from the impact of finalizing JSR 170, initializing JSR 283 (the next JCR specification revision EG), and the summer holiday schedule. We are in the process of reconfiguring our source directories for an eventual 1.0 release and Maven 2 support. No new committers were added this quarter, though we expect more to be added soon.


# 2005/07/15 {#Status20050715}

Jackrabbit has attracted public interest from many different projects, both open source and commercial in nature, and has over 250 people reading the developer list. During the past quarter we added one new committer, Edgar Poce, and cleared the minimum threshold of three independent committers.


The big news is that JCR, the Content Repository for Java Technology 1.0 API, has been completed by the JSR 170 expert group and received final approval from the J2SE/EE executive committee at the end of May. We are currently working on restructuring the Jackrabbit project directories in preparation of an eagerly anticipated first release candidate and passing the official TCK, at which point we are hoping to graduate from Incubator to TLP status for the 1.0 release.


# 2005/04/25 {#Status20050425}

Jackrabbit is doing well as a project and is attracting interest both within other Apache projects (Lenya and Graffito in particular) as well as from new folks in the Java community. We added two new committers, Jukka Zitting and Dominique Pfister, and have received sustained contributions from Serge Huber, Edgar Poce, Angela Schreiber, Felix Meschberger, and others.


Jackrabbit's only problem right now is continued reliance on JCP EG private discussions due to the unfinished nature of the JSR 170 Content Repository for Java Technology API. JSR 170 is expected to be submitted for final draft status in early May, after which all of the discussion can be moved to Apache lists. We anticipate graduating from Incubator sometime soon after that.


# 2004/11/17 {#Status20041117}

The Jackrabbit project has completed all of the Incubator checklist items in terms of moving to Apache and getting the IP transfer done. With the help of Maven, we have a full website set up at


 [http://incubator.apache.org/jackrabbit/](http://incubator.apache.org/jackrabbit/) 


with a few link bugs due to the svn/viewcvs integration. Our big task from now to graduation is to get the community more involved in development, planning features, integrating with some of the DB projects, and scoping out interesting applications to build on top of the interface.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2004-09-06 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. (fielding) |
| 2004-08-28 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. (fielding) |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2004-08-28 | Identify all the Mentors for the incubation, by asking all that can be Mentors. (fielding) |
| 2004-08-28 | Subscribe all Mentors on the pmc and general lists. (fielding) |
| 2004-08-28 | Give all Mentors access to all incubator CVS modules. (fielding) |
| 2004-08-28 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' (fielding) |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2004-09-03 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. (fielding) |
| 2004-09-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. (fielding) |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2004-09-28 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. (fielding) |
| 2004-09-28 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.(fielding) |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|------|------|
| 2004-09-13 | Check that all active committers have submitted a contributors agreement. (fielding) |
| 2004-09-13 | Add all active committers in the STATUS file. (fielding) |
| 2004-09-13 | Ask root for the creation of committers' accounts on cvs.apache.org. (fielding) |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|------|------|
| 2004-09-14 | Ask infrastructure to create source repository modules and grant the committers karma. (fielding) |
| 2004-09-08 | Ask infrastructure to set up and archive Mailing lists. (fielding) |
| 2004-09-14 | Decide about and then ask infrastructure to setup an issuetracking system (Jira). (fielding) |
| 2004-09-28 | Migrate the project to our infrastructure. (stefan) |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? **Yes** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) **Yes** 

- Are project decisions being made in public by the committers? **Yes** 

- Are the decision-making guidelines published and agreed to by all of the committers? **Yes** 

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? **Yes** 

## Project Specific {#Project+Specific}

 _Add project specific tasks here. **None** _ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#acceptance}


- If graduating to an existing PMC, has the PMC voted to accept it? **n/a** 

- If graduating to a new PMC, has the board voted to accept it? **Yes** 

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? **Yes** 
