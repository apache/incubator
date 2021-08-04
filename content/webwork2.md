Title: WebWork 2 Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The WebWork 2 project graduated on 2006-05</span>


The Apache Struts project and the members of the OpenSymphony WebWork 2 project are working together on a next-generation web application framework utilizing an action/request architecture. WebWork was initially created by Rickard Oberg to improve on the ideas and functionality of the Jakarta Struts framework. (Now known as the Apache Struts Action framework.) Since then, the WebWork community has continued to extend and refine the framework's capabilities through a long series of releases, the latest of which, 2.2, brings advanced Ajax, templating, and Java 5 capabilities to its solid WebWork 2 foundation. While, to date, the WebWork and Struts Action codebases have overlapped, recent movements to bring consolidation to the web framework landscape have inspired both communities to work together. Apache Struts has recently reorganized our codebase into multiple subprojects, two of which, Shale and Action, represent two separate but equal web frameworks. Struts Shale serves the nascent JSF community, while Struts Action serves the established JSP community. The WebWork 2 code will be brought into the Action subproject as the 2.x branch.



- 2006-01-30 - [Proposal](http://wiki.apache.org/incubator/WebWork2Proposal) accepted by the Struts PMC

- 2006-05-06 - Graduation! ( [vote result](http://mail-archives.apache.org/mod_mbox/incubator-general/200605.mbox/ajax/%3c1c661f2f0605061132x18dbaac1m4fdfea5706348a27@mail.gmail.com%3e) )


- OpenSymphony's WebWork 2 site - [http://www.opensymphony.com/webwork/](http://www.opensymphony.com/webwork/) 


- Apache Struts site - [http://struts.apache.org](http://struts.apache.org) 


- Incubation status page - [http://incubator.apache.org/projects/webwork2](http://incubator.apache.org/projects/webwork2) 

| Item | Type | Reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/projects/webwork2/](http://incubator.apache.org/projects/webwork2/)  _Not needed, will use Struts site_  |
| Website | wiki |  [http://wiki.apache.org/struts"](http://wiki.apache.org/struts)  _Using the Struts site_  |
| Mailing list | dev | dev@struts.apache.org |
| Bug tracking | JIRA |  [http://issues.apache.org/struts](http://issues.apache.org/struts)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/webwork2](https://svn.apache.org/repos/asf/incubator/webwork2)  |

 


| Role | Apache ID | Name |
|-------|------------|-------|
| Champion | mrdon | Don Brown |
| Mentor | martinc | Martin Cooper |
| Mentor | husted | Ted Husted |
| Committer | jcarreira | Jason Carreira |
| Committer | plightbo | Patrick Lightbody |
| Committer | jmitchell | James Mitchell |
| Committer | germuska | Joe Germuska |
| Committer | apopescu | Alexandru Popescu |
| Committer | rgielen | Rene Gielen |
| Committer | hermanns | Rainer Hermanns |
| Committer | tmjee | Toby Jee |
| Committer | roughley | Ian Roughley |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated&amp;#xD; {#Identify+the+project+to+be+incubated%26%23xD%3B}

| date | item |
|-------|-------|
| 2006-02-21 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2006-02-21 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2006-02-21 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2006-02-21 | Subscribe all Mentors on the pmc and general lists. |
| 2006-02-22 | Give all Mentors access to all incubator SVN directory. (to be done by PMC chair) |
| 2006-02-22 | Tell Mentors to track progress in the file 'incubator/projects/webwork2.html' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2006-04-28 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2006-04-28 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2006-04-28 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2006-04-28 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| 2006-03-22 | Check that all active committers have submitted a contributors agreement. |
| 2006-03-22 | Add all active committers in the STATUS file. |
| 2006-03-22 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| 2006-02-22 | Ask infrastructure to create source repository modules and grant the committers karma. |
| N/A | Ask infrastructure to set up and archive Mailing lists. |
| 2006-02-28 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2006-04-28 | Migrate the project to our infrastructure. |

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


- <strike>Replace LGPL calendar with Dojo version</strike>

- <strike>Replace LGPL tooltip with Dojo version</strike>

- <strike>Replace LGPL editor with Dojo version</strike>

- <strike>Change Opensymphony copyrights</strike>

- <strike>Replace incompatibly option select Javascript library</strike>

- <strike>Add Apache copyrights to dtree files</strike>

- <strike>Add Apache copyrights to PicoContainer copyrighted files</strike>

- <strike>Remove erronously added copyrights</strike>

# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
