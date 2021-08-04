Title: OpenWhisk Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The OpenWhisk project graduated on 2019-07-17</span>


Apache OpenWhisk is a serverless event-based programming platform.



- 2016-11-23 Project enters incubation.

- 2016-12-06 dev and private lists created; commits lists requested.

- 2017-01-07 Confluence Wiki created

- 2017-05-05 Moved 24/26 OpenWhisk project and ecosystem repositories from openwhisk to Apache organization within GitHub.

- 2017-05-11 Requested Infra. to move "openwhisk" (core) repo. to Apache.

- 2017-05-12 "Core" openwhisk (last source code) repo. moved under Apache GitHub.


- link to the main website:


-  [https://openwhisk.org](http://openwhisk.org) 


- link to the page(s) that tell how to participate (Website, Mailing lists, Bug tracking, Source code):


-  [https://cwiki.apache.org/confluence/display/openwhisk/OpenWhisk+Project+Wiki](https://cwiki.apache.org/confluence/display/openwhisk/OpenWhisk+Project+Wiki) 


- link to the project status file (Committers, non-incubation action items, project resources, etc.)

If the project website and code repository are not yet setup, use the following table:


<tbody>| item | type | reference |
|------|------|-----------|
| Website | www |  [http://openwhisk.apache.org](https://openwhisk.apache.org)  |
|  | Apache |  [http://openwhisk.incubator.apache.org/](http://openwhisk.incubator.apache.org/)  |
|  | wiki |  [https://cwiki.apache.org/confluence/display/openwhisk/](https://cwiki.apache.org/confluence/display/openwhisk)  |
| Mailing list | dev |  `dev`  `@`  `openwhisk.incubator.apache.org`  |
|  | commits |  `commits`  `@`  `openwhisk.incubator.apache.org`  |
| Issue (bug) tracking | GitHub Issues |  [https://github.com/apache/incubator-openwhisk/issues (core)](https://github.com/apache/incubator-openwhisk/issues) GitHub issues for other OpenWhisk repos. can be found from project listing: [](https://github.com/apache?q=openwhisk) https://github.com/apache?q=openwhisk |
|  | JIRA | N/A, using GitHub issues (per-repo.) |
| Source code | GitHub (Apache) |  [https://github.com/apache?q=openwhisk](https://github.com/apache?q=openwhisk) (Filtered link to all code repos. under Apache org.) |
|  | GitHub (OpenWhisk) |  [https://github.com/openwhisk](https://github.com/openwhisk) (Website repo. only) In-progress: Jenkins (Jekyll) build, gitpubsub. |
| Mentors |  | See [https://whimsy.apache.org/roster/ppmc/openwhisk](https://whimsy.apache.org/roster/ppmc/openwhisk)  |
| Sub-project Listing |  |  [https://cwiki.apache.org/confluence/display/openwhisk/Subproject+listing](https://cwiki.apache.org/confluence/display/OPENWHISK/Subproject+listing)  |
| PPMC list (Whimsy) |  |  [https://whimsy.apache.org/roster/ppmc/openwhisk](https://whimsy.apache.org/roster/ppmc/openwhisk)  |
</tbody>
The list of committers, PPMC members and mentors is found at [https://whimsy.apache.org/roster/ppmc/openwhisk](https://whimsy.apache.org/roster/ppmc/openwhisk) 


Incubation status reports are found at [https://whimsy.apache.org/board/minutes/Incubator](https://whimsy.apache.org/board/minutes/Incubator) 


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

<tbody>| date | item |
|------|------|
| N/A | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |
</tbody>
## Infrastructure {#Infrastructure}

<tbody>| date | item |
|------|------|
| 2016-12-06 | Ask infrastructure to set up and archive mailing lists. |
| 2017-04-26 | Ask infrastructure to create (transfer) source repository modules from openwhisk to Apache org. under GitHub. |
| N/A, Issue tracking established as part of GitHub. | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2017-01-07 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2017-05-12 | Migrate the project to our infrastructure. |
</tbody>
## Mentor-related responsibility/oversight {#Interim+responsibility}

<tbody>| date | item |
|------|------|
| 2017-02-01 | Subscribe all Mentors on the pmc and general lists. |
| 2017-01-16 | Give all Mentors access to the incubator GitHub repository. (to be done by the Incubator PPMC chair) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |
</tbody>
## Copyright {#Copyright}

<tbody>| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |
</tbody>
## Verify distribution rights {#Verify+distribution+rights}

<tbody>| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |
</tbody>
## Establish a list of active committers {#Establish+a+list+of+active+committers}

<tbody>| date | item |
|------|------|
| 2017-02-03 | Check that all active committers have submitted a contributors agreement. |
| 2017-02-06 | Add all active committers in the relevant section above. |
| 2017-02-06 | Ask root for the creation of committers' accounts in LDAP. |
</tbody>
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
