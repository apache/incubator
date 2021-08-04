Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>
 `-----8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;----` 
This document is the template for project incubation status.


What to do to set it up:



- copy this file and name it &lt;projectname&gt;.xml

- add a section in incubator/content/podlings.xml

For this file:



- substitute the XYZ project name with the real one

- fill in the "Description". See [Project Naming And Descriptions](http://www.apache.org/foundation/marks/pmcs.html#markdesc) 

- edit "Project info" to contain only effective resources

- start doing "Incubation work items"

When an "Incubation work item" is done, place the date in the supplied space, and if necessary update "Project info" to reflect changes in resources.


There are also sections where to place project news and incubation status reports.


 _On the first edit of this file, please delete this entire section._ 

 `-----8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;---- cut here -------8-&lt;----` 
This page tracks the project status, incubator-wise. For more general project status, look on the project website.


The XYZ Project is a wonderful project that does things and goes places.



- YYYY-MM-DD Project enters incubation.


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://XYZ.incubator.apache.org/](http://XYZ.incubator.apache.org/)  |
| . | wiki | . |
| Mailing list | dev |  `dev`  `@`  `PROJECT.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `PROJECT.incubator.apache.org`  |
| Bug tracking | . | [ provide expected link ] |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/XYZ/](https://svn.apache.org/repos/asf/incubator/XYZ/)  |
| Roster | Whimsy |  [XYZ Roster](https://whimsy.apache.org/roster/ppmc/XYZ)  |


-  [XYZ Board Reports](https://whimsy.apache.org/board/minutes/XYZ.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| ....-..-.. | Request DNS (first step after creating podling status page) |
| ....-..-.. | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator)  |
| ....-..-.. | Request [git repositories](https://reporeq.apache.org/)  |
| ....-..-.. | Ask infrastructure to create source repository modules and grant the committers karma (if using SVN) |
| ....-..-.. | Ask infrastructure to set up issue tracker ( [JIRA](https://selfserve.apache.org/jira.html) , Bugzilla). |
| ....-..-.. | Ask infrastructure to set up wiki ( [Confluence](https://selfserve.apache.org/confluence.html) ). |
| ....-..-.. | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the relevant section above. |
| ....-..-.. | Ask root for the creation of committers' accounts in LDAP. |

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
