Title: Stanbol Podling Status Page
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Stanbol project graduated on 2012-09-19</span>


Stanbol is a modular software stack and reusable set of components for semantic content management.



- 2010-11-15 Project enters incubation.

- 2011-07-25 Project elected Florent André as a new committer

- 2011-12-16 Project elected Reto Bachmann Gmuer as a new committer

- 2012-01-25 Project elected Ali Anil Sinaci as a new committer

- 2012-05-06 Project made its first release of Apache Stanbol 0.9.0-incubating

- 2012-07-10 Project released Apache Stanbol Entityhub 0.10.0-incubating

- 2012-09-19 Project graduated to TLP

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/stanbol/](http://incubator.apache.org/stanbol/)  |
| Mailing lists | developer |  `stanbol-dev`  `@`  `incubator.apache.org`  |
|  | private (PPMC) |  `stanbol-private`  `@`  `incubator.apache.org`  |
|  | commits |  `stanbol-commits`  `@`  `incubator.apache.org`  |
|  | user | No user mailing list at the moment |
| Bug tracking |  |  [https://issues.apache.org/jira/browse/STANBOL](https://issues.apache.org/jira/browse/STANBOL)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/incubator/stanbol](http://svn.apache.org/repos/asf/incubator/stanbol)  |
| Champion | Bertrand Delacrétaz |
| Mentors | Ted Dunning, Ross Gardler, Tommaso Teofili |
| Committers | See the [Stanbol team page](http://stanbol.apache.org/team.html)  |


-  [December 2010](http://wiki.apache.org/incubator/December2010) 
Stanbol is a modular software stack and reusable set of components for semantic content management.


Stanbol just entered incubation, on 2010-11-15.


Mailing lists, SVN and JIRA are ready, most user accounts created, pre-existing code from the IKS project has been imported under a code grant.


The Stanbol community has been invited to participate in a free workshop organized by the IKS project (*). It is a good opportunity to establish best practices for collaboration and communication between IKS (an EU-funded research project in which most current Stanbol committers are involved, http://iks-project.eu/) and the Stanbol podling.


Branding requirements checked, see https://issues.apache.org/jira/browse/STANBOL-14


Next steps:

- leanup dependencies and code as per ASF requirements

- Make an initial release

- Start establishing and growing the community



(*) Workshop URL: http://wiki.iks-project.eu/index.php/Workshops/EAworkshopAmsterdam



-  [February 2011](http://wiki.apache.org/incubator/February2011) 
Stanbol is a modular software stack and reusable set of components for semantic content management. Entered incubation on 2010-11-15.


Community development:

- Five new committers mentioned in the previous report elected, accounts requested.



Project activities:

- Java packages renamed org.apache.stanbol for enhancer and entityhub modules

- Work on removing LGPL dependencies in the Kres module ongoing

- Integration tests added to enhancer module via reusable testing tool



Next steps:

- Finish package renaming

- Finish LGPL dependencies cleanup

- Setup Hudson (Jenkins?) continuous integration

- Make a first release, possibly omitting modules with ASF-incompatible dependencies

- Grow the community



Signed off by mentor: bdelacretaz (champion)



-  [May 2011](http://wiki.apache.org/incubator/May2011) 
Stanbol is a modular software stack and reusable set of components for semantic content management. Entered incubation on 2010-11-15.


Community development:

- some new users started playing with Stanbol and asking for guidance on the mailing lists



Project activities:

- lots of package/module refactoring

- added a benchmark tool for Enhancer

- KReS module build and tests fixed

- setup continuous integration with Jenkins

- added JCR module of CMS Adapter



Next steps:

- Make a first release, possibly omitting modules with ASF-incompatible dependencies

- Grow the community



Signed off by mentor: Tommaso Teofili



-  [August 2011](http://wiki.apache.org/incubator/August2011) 
Stanbol is a modular software stack and reusable set of components for semantic content management. Entered incubation on 2010-11-15.



1. A list of the three most important issues to address in the move towards graduation.


- make a first release (depends on a first release of Apache Clerezza to eliminate SNAPSHOT dependencies)

- create demos showing the power of Stanbol to grow the community

- improve documentation and web site to lower the barrier for new users

1. Any issues that the Incubator PMC or ASF Board might wish/need to be aware of


- none

1. How has the community developed since the last report


- Florent André was elected as a new committer

- some new users showed up on the mailing list

- Potentially new users from the CMS industry were attracted in a Stanbol hands-on session during a CMS community workshop organized by the IKS project in Paris (http://www.iks-project.eu/news-and-events/events/mycms-and-web-data-iks-community-workshop)

1. How has the project developed since the last report.


- Code preparations for first release (solved incompatible license issues, license headers, release profile, etc.)

- Added new component "FactStore"

- Integration tests added to EntityHub

- CMIS module added to CMS Adapter

Signed off by mentor: rgardler



-  [November 2011](http://wiki.apache.org/incubator/November2011) 
Stanbol is a modular software stack and reusable set of components for semantic content management. Entered incubation on 2010-11-15.


There are no issues that require the Incubator PMC or ASF Board attention at this time.



1. Three most important issues to address in the move towards graduation.


- Make a first release (depends on a first release of Apache Clerezza to eliminate SNAPSHOT dependencies).<br></br>No concrete progress here.

- Create demos showing the power of Stanbol to grow the community<br></br>Demo server at http://dev.iks-project.eu, should be moved to Apache servers.

- Improve documentation and web site to lower the barrier for new users<br></br>Work in progress, docs are now available for the enhancer, entity hub, content hub, cms adapter and reasoners components, and for multi-language support.

1. How has the community developed since the last report?


- No new committers, some new users have shown up on the mailing list.

- Ali Anil Sinaci provided a number of patches which cover all current functionalities of Contenthub.

- Stanbol was presented at various events: Nuxeo Wold, ApacheCon, "Smart Content = Smart Business" workshop at the [J. Boye](http://jboye.com/conferences/aarhus11/) conference in Aarhus, Denmark.

1. How has the project developed since the last report.


- Integration with the Linked Media Framework (http://code.google.com/p/kiwi/) is in progress.

- Integration of the Semantic Search capabilities with the Stanbol ContentHub.

- New EnhancementEngine for extracting Keywords from Controlled vocabularies.

- Improved multi language support.

- Bidirectional mapping feature between JCR/CMIS content repositories and RDF data.

- Implementation of long term operations for reasoners is in progress.

Signed off by mentor: bdelacretaz



-  [February 2012](http://wiki.apache.org/incubator/February2012) 
Apache Stanbol is an open source modular software stack and reusable set of components for semantic content management. Incubating since November, 2010.



1. Three most important issues to address in the move towards graduation.


- Make a first release (depends on a first release of Apache Clerezza to eliminate SNAPSHOT dependencies)

- Auditing/clarifying multiple maven repositories and corresponding dependencies

- Make the data models downloadable independently from the ASF repositories to avoid gray copyright / licensing issues (for instance for the OpenNLP models).

1. How has the community developed since the last report?


- Reto Bachmann Gmuer and Ali Anil Sinaci has been elected as new committers.

- Alberto Musetti has contributed to the project by providing patches

- David Riccitelli provided patch that uses the Stanbol Commons Jobs to implement an Asynchronous RESTful API for the Stanbol Enhancer.

1. How has the project developed since the last report.

Features:
- LDPath (http://code.google.com/p/ldpath/) support for Entityhub and Contenthub

- Contenthub now supports multiple semantic indexes and Solr RESTful API can be directly used for search

- Enhancer now support for multiple Enhancement Chains and multi-part ContentItems. Work on extended RESTful API will be finished soon.

- Enhancement Engine for Topic Classification (STANBOL-197)

- First version of a Apache Stanbol/Apache Camel integration

- Improved Documentation (both on the Stanbol Homepage and the Web UI of Apache Stanbol)

Signed off by mentor: bdelacretaz, tommaso



-  [May 2012](http://wiki.apache.org/incubator/May2012) 
Apache Stanbol is an open source modular software stack and reusable set of components for semantic content management. Incubating since November, 2010.


Graduation:


We believe Stanbol will be ready to graduate in the next few days: the issues mentioned in our previous report have been adressed, the release is being voted on (after six iterations of release candidates) and should be out in the next few days if all goes well. Community activity is steady and slowly increasing.


Community:



  - No new committers or PPMC members since the last report, but steady activity on our lists from both existing and new members of our community.

  - Two Stanbol committers have been elected as Clerezza committers, furthering ties between both podlings.

  - A Stanbol GSoC project has been accepted, with Rupert Westenthaler as its mentor.

  - Contribution of several EnhancementEngines based on LinguaGrid (NLP framework) by Alessio Bosca (STANBOL-583).

  - Integration of DBpedia Spotlight (http://dbpedia.org/spotlight) with the Stanbol Enhancer, led by a new Stanbol contributor.

  - Stanbol was presented in the Developer Track of WWW2012 (slides: http://s.apache.org/AgK)

Project activity:



  - Reorganization of the codebase for the release, the one binary dependency left that's not available in Maven Central has been moved to a separate -deps package for the release, as discussed on the incubator general list.

  - Content hub faceted search improvements.

  - New EnhancementEngine based on Apache Tika

  - TopicEngine (STANBOL-197) is now functional

  - Full LDpath support for the Entityhub Indexing tools (STANBOL-408).

Signed off by mentor: bdelacretaz, rgardler



# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2012-08-03 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.<br></br>See [PODLINGNAMESEARCH-8](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-8)  |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2010-11-15 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2010-11-15 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2010-11-15 | Subscribe all Mentors on the pmc and general lists. |
| 2010-11-15 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-11-15 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2010-11-30 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-07-18 | The Apache RAT check was added to check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2012-05-02 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2012-05-02 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-11-30 | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| 2010-11-15 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-11-15 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2010-11-15 | Ask infrastructure to set up and archive Mailing lists. |
| 2010-11-15 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2010-11-15 | Migrate the project to our infrastructure. |

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


- If graduating to a new PMC, has the board voted to accept it?<br></br>Yes, in the board meeting at September 19, 2012.

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?<br></br>Yes, with this [vote](http://markmail.org/thread/bjijudvfiajhi2dn) .
