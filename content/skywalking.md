Title: Apache SkyWalking Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The SkyWalking project graduated on 2019-04-17</span>


Skywalking is an APM (application performance monitor), especially for microservice, Cloud Native and container-based architecture systems. Support observing and monitoring system from different sources, such as distributed tracing agents/SDKs, through Service Mesh telemetry data.



- 2019-02-17 SkyWalking officially docker repositories have transfered to Apache Docker Hub organization.

- 2019-01-29 SkyWalking 6.0.0-GA released. SkyWalking 6 core is production ready.

- 2018-12-25 SkyWalking 6.0.0-beta released. New protocols for distributed tracing are provided and recommended to update.

- 2018-11-14 SkyWalking 6.0.0-alpha released. Service mesh telemetry data format, including Istio telemetry format, are supported

- 2018-10-29 Podling name search complete. [JIRA Ticket](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-151) 

- 2018-10-17 SkyWalking 5.0.0-GA released

- 2018-09-12 SkyWalking 5.0.0-RC2 released

- 2018-07-28 New Mentor Ignasi Barrera added

- 2018-07-13 Additional git repo added: incubator-skywalking-oal-tool

- 2018-07-11 SkyWalking 5.0.0-beta2 released

- 2018-05-23 SkyWalking 5.0.0-beta released

- 2018-04-03 SkyWalking 5.0.0-alpha released

- 2018-01-14 SkyWalking website on ASF

- 2017-12-08 Project enters incubation


- SkyWalking Website - http://skywalking.incubator.apache.org


- SkyWalking Twitter - https://twitter.com/AsfSkyWalking


- The project status file is [here](https://svn.apache.org/repos/asf/incubator/public/trunk/content/projects/skywalking.xml) .

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://skywalking.incubator.apache.org/](http://skywalking.incubator.apache.org/)  |
| . | dev |  `dev`  `@`  `skywalking.incubator.apache.org`  |
| Mailing list | private |  `private`  `@`  `skywalking.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `skywalking.incubator.apache.org`  |
| . | notifications |  `notifications`  `@`  `skywalking.incubator.apache.org`  |
| Bug tracking | . | https://github.com/apache/incubator-skywalking/issues |
| Source code | . | . |
| . | incubator-skywalking | https://github.com/apache/incubator-skywalking.git |
| . | incubator-skywalking-ui | https://github.com/apache/incubator-skywalking-ui.git |
| . | incubator-skywalking-oal-tool | https://github.com/apache/incubator-skywalking-oal-tool.git |
| . | incubator-skywalking-data-collect-protocol | https://github.com/apache/incubator-skywalking-data-collect-protocol.git |
| . | incubator-skywalking-query-protocol | https://github.com/apache/incubator-skywalking-query-protocol.git |
| . | incubator-skywalking-docker | https://github.com/apache/incubator-skywalking-docker.git |
| . | incubator-skywalking-kubernetes | https://github.com/apache/incubator-skywalking-kubernetes.git |
| Roster | Whimsy |  [SkyWalking Roster](https://whimsy.apache.org/roster/ppmc/skywalking)  |
| Mentors |  | see [SkyWalking Roster Mentors](https://whimsy.apache.org/roster/ppmc/skywalking#mentors)  |
| PMC and Committers |  | see [SkyWalking Roster PMC + Committers](https://whimsy.apache.org/roster/ppmc/skywalking#ppmc)  |


-  [SkyWalking Board Reports](https://whimsy.apache.org/board/minutes/skywalking.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2017-12-08 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| 2017-12-10 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2017-12-08 | Request DNS (first step after creating podling status page). ref: INFRA-15628 |
| 2017-12-10 | Request [Mailing Lists](https://selfserve.apache.org/)  |
| 2017-12-10 | Request [gitbox repositories. ref: INFRA-15649](https://gitbox.apache.org/)  |
| 2017-12-15 | Grant the committers karma (corresponding github apache team). ref: INFRA-15649 |
| 2017-12-15 | Migrate the project to our infrastructure. ref: INFRA-15649 |
| 2018-01-18 | Migrate the website to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2017-12-08 | Subscribe all Mentors on the pmc and general lists. |
| 2018-01-18 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2018-01-18 | Tell Mentors to track progress in the file ' [incubator/contents/projects/skywalking.xml](https://svn.apache.org/repos/asf/incubator/public/trunk/content/projects/skywalking.xml) ' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2018-04-03 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2018-04-03 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2018-04-03 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2018-04-03 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2017-12-10 | Check that all active committers have submitted a contributors agreement. |
| 2017-12-08 | Add all active committers in the relevant section above. |
| 2017-12-15 | Ask root for the creation of committers' accounts in LDAP. |

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
