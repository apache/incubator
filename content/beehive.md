Title: Apache Beehive Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the [project website](http://incubator.apache.org/beehive) .


<span class="graduated">The Beehive project graduated on 2005-07-18</span>


The Beehive project is an extensible Java application framework with an integrated metadata-driven programming model for web services, web applications, and resource access. The framework leverages the latest innovations in the forthcoming JDK 1.5, particularly JSR 175 metadata annotations. It currently builds on key Apache projects such as Tomcat, Struts, MyFaces, and Axis.


While this proposal focuses on a framework consisting of these three subprojects, it is expected that the Apache community will come up with additional innovative ideas that will evolve into future subprojects. The currently planned components include:



- Controls: The Control architecture is a lightweight component framework based upon annotated JavaBeans, exposing a simple and consistent client model for accessing a variety of J2EE resource types. The framework provides a variety of functions including: JavaBean-based client access, configuration through JSR-175 metadata and external configuration data, automatic resource management, context services, and an extensible authoring model for creating new Control types.

- NetUI: NetUI Page Flow is a web application framework based on Apache Struts with an easy to use, single-file programming model based on JSR-175 metadata. It builds on the core Struts separation of model/view/controller elements, and adds features such as automatic state management and first-class integration with Controls, XMLBeans, and Java Server Faces.

- Metadata for Java Web Services: This component is an implementation of the JSR-181 specification and is a key piece of the Beehive framework. JSR 181 uses JSR-175 metadata annotations in Java methods and classes to easily build Web services.


- 2005-06-06: Beehive releases 1.0 milestone 1

- 2005-05-09: Beehive starts building a nightly release available from http://cvs.apache.org

- 2005-05-09: Beehive completes the addition of the core J2EE system controls to Apache SVN

- 2005-03-28: Beehive reaches a beta milestone and releases pre-1.0 beta version

- 2005-02-07: Beehive adds Bryan Che as a committer

- 2004-12-17: Beehive adds Fumitada Hatori as a committer

- 2004-11-12: Beehive reaches an alpha milestone and releases pre-1.0 alpha version for ApacheCon

- 2004-07-16: Beehive source code for NetUI and Controls are now available. Web Services code will begin with the Axis 181 codebase


- Project Web Site: [http://incubator.apache.org/beehive](http://incubator.apache.org/beehive) 

- Mailing List Info: [http://incubator.apache.org/beehive/mailinglists.html](http://incubator.apache.org/beehive/mailinglists.html) 

# Detailed References: {#Detailed+References%3A}

| Item | Type | Reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/beehive/](http://incubator.apache.org/beehive/)  |
| . | wiki |  [http://wiki.apache.org/beehive](http://wiki.apache.org/beehive)  |
| Mailing list | dev | beehive-dev@incubator.apache.org |
| . | user | beehive-user@incubator.apache.org |
| . | commits | beehive-commits@incubator.apache.org |
| . | ppmc | beehive-ppmc@incubator.apache.org |
| Bug tracking | . | JIRA: Beehive (BEEHIVE), Admin: Heather Stephens (heathers) |
| Source code | SVN |  [http://svn.apache.org/repos/asf/incubator/beehive](http://svn.apache.org/viewcvs.cgi/incubator/beehive/)  |
| Proposal | wiki |  [http://wiki.apache.org/incubator/BeehiveProposal](http://wiki.apache.org/incubator/BeehiveProposal)  |
| Mentor | craigmcc | Craig R. McClanahan |
| Committers | ias | Changshin Lee |
| Committers | cjudson | Chris Judson |
| Committers | cliffs | Cliff Schmidt |
| Committers | craigc | Craig Crutcher |
| Committers | dolander | Daryl Olander |
| Committers | dims | Davanum Srinivas |
| Committers | davidbau | David Bau |
| Committers | dmkarr | David M. Karr |
| Committers | daveread | David Read |
| Committers | ekoneil | Eddie O'Neil |
| Committers | heathers | Heather Stephens |
| Committers | jongjinchoi | Jongjin Choi |
| Committers | kylem | Kyle Marvin |
| Committers | jsong | James Song |
| Committers | kentam | Ken Tam |
| Committers | mclark | Michael Clark |
| Committers | rich | Richard Feit |
| Committers | rotan | Rotan Hanrahan |
| Committers | scottryan | Scott Ryan |
| Committers | steveh | Steve Hanson |
| Committers | stocco | Steven Tocco |
| Committers | vsalvato | Vince Salvato |
| Committers | mmerz | Mike Merz |
| Committers | hattori | Fumitada Hattori |
| Committers | bryanche | Brian Che |

 **2005-04-26** <br></br><br></br>Beehive is in the home stretch of its 1.0-level release; we declared a beta release in March, and are on track to deliver a 1.0 in the late May timeframe. Posting automated daily builds continues to be an challenge, but otherwise infrastructure is well in place. At this point we are largely focused on fit'n'finish issues in the code, as well as a polished set of samples and documentation.<br></br><br></br>The Beehive community added Bryan Che as a new committer in February, 2005. With the beta release and open planning on features for the next version, we are seeing increased dev/user list activity -- we anticipate that the 1.0 release will be even more significant in building the community, and hope to graduate from the Incubator sometime soon after the 1.0 release. Certain Beehive components have a very clear affinity with the Apache Struts and AXIS projects, and those projects may play a role in graduation (pending further discussion).<br></br><br></br> **2004-10-18** <br></br><br></br> **Code &amp; Infrastructure** 



- initial code drop was made in mid-July. Ongoing development is very active.

- over the last three months, we've set up SVN, JIRA, a website, and a wiki.

- docs and tutorials contributions continue - a better Beehive build system has been proposed by a contributor. It is currently under review by committers.

- Beehive jars were added to java-repository in order to support control builders who prefer to use Maven.
 **Legal** <br></br>

- all code shows ASF copyright notice.

- software grant, individual CLAs, and corporate CLAs, are in place for all active committers (one initial committer has no account while we wait for his employer to complete review of CLA and CCLA)
 **Community** <br></br>

- Web services metadata subproject has participation from key members of Axis community; We've accepted Wolfgang (Fumitada Hattori) as a new committer on the project in the Web services area

- NetUI and Controls subprojects are still primarily driven by BEA employees. We expect this to begin to change after getting out an initial release for the community to experiment with and digest.

- We've seen a growth in interest/use on both the user and dev mailing lists

- Amazon, XFire and Hibernate pre-1.0 controls built on Beehive have been released at Controlhaus.
 **Release Plans** <br></br>

- The community cut a pre-1.0 release for ApacheCon. This release followed the incubation release rules requiring a) incubator disclaimer in README and from any download links, b) filename to include 'incubating', and c) ppmc vote (providing the incubator pmc approval since all interested incubator pmc members should be on the beehive ppmc mailing list.

- A generic release plan proposed and discussed but needs a final vote. Roadmap documents have been posted to make it easier for new developers to get the big picture and figure out where they can help.
<br></br><br></br><br></br><br></br>
# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| Date | Item |
|-------|-------|
| DONE - ....-..-.. | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| DONE - 2004-07-15 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| Date | Item |
|-------|-------|
| DONE - 2004-05-09 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| DONE - 2004-06-15 | Subscribe all Mentors on the pmc and general lists. |
| DONE - 2004-07-16 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| DONE - 2004-07-18 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| Date | Item |
|-------|-------|
| DONE - 2004-07-16 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| DONE - 2004-10-18 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |
| DONE - 2005-05-09 | Migrated the "system controls" from [ControlHaus](http://www.controlhaus.org) to Apache SVN with ASF 2.0 License and Apache copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| Date | Item |
|-------|-------|
| DONE - 2004-10-18 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| DONE - 2004-10-18 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |
| DONE - 2005-05-04 | BEA completes code grant for the "system control" source code from [ControlHaus](http://www.controlhaus.org) to be added to the Beehive SVN repository and released with our distributions. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| Date | Item |
|-------|-------|
| DONE ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| DONE - 2004-07-14 | Add all active committers in the STATUS file. |
| DONE - 2004-07-18 | Ask root for the creation of committers' accounts on cvs.apache.org. |
| 2004-12-17 | Added Fumitada Hatori (Wolfgang) as a committer. |
| 2005-02-07 | Added Bryan Che a committer. |

## Infrastructure {#Infrastructure}

| Date | Item |
|-------|-------|
| DONE - 2004-07-15 | Ask infrastructure to set up and archive Mailing lists. |
| DONE - 2004-07-16 | Ask infrastructure to create source repository modules and grant the committers karma. |
| DONE - 2004-07-16 | Decide about and then ask infrastructure to setup an issuetracking system (JIRA). |
| DONE - 2004-07-16 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- DONE - Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

- DONE - Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- DONE - Are project decisions being made in public by the committers?

- DONE - Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- DONE - Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific Tasks {#Project+Specific+Tasks}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
