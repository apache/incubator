Title: Metron Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


The Metron project graduated on 2017-04-19, by Board resolution.


<span class="graduated">The Metron project graduated on 2017-04-19</span>


Metron integrates a variety of open source big data technologies in order to offer a centralized tool for security monitoring and analysis. Metron provides capabilities for log aggregation, full packet capture indexing, storage, advanced behavioral analytics and data enrichment, while applying the most current threat-intelligence information to security telemetry within a single platform.


Metron can be divided into 4 areas:

1. A mechanism to capture, store, and normalize any type of security telemetry at extremely high rates. Because security telemetry is constantly being generated, it requires a method for ingesting the data at high speeds and pushing it to various processing units for advanced computation and analytics.

1. Real time processing and application of enrichments such as threat intelligence, geolocation, and DNS information to telemetry being collected. The immediate application of this information to incoming telemetry provides the context and situational awareness, as well as the “who” and “where” information that is critical for investigation.

1. Efficient information storage based on how the information will be used:

   1. Logs and telemetry are stored such that they can be efficiently mined and analyzed for concise security visibility

   1. The ability to extract and reconstruct full packets helps an analyst answer questions such as who the true attacker was, what data was leaked, and where that data was sent

   1. Long-term storage not only increases visibility over time, but also enables advanced analytics such as machine learning techniques to be used to create models on the information. Incoming data can then be scored against these stored models for advanced anomaly detection.


1. An interface that gives a security investigator a centralized view of data and alerts passed through the system. Metron’s interface presents alert summaries with threat intelligence and enrichment data specific to that alert on one single page. Furthermore, advanced search capabilities and full packet extraction tools are presented to the analyst for investigation without the need to pivot into additional tools.



Big data is a natural fit for powerful security analytics. The Metron framework integrates a number of elements from the Hadoop ecosystem to provide a scalable platform for security analytics, incorporating such functionality as full-packet capture, stream processing, batch processing, real-time search, and telemetry aggregation. With Metron, our goal is to tie big data into security analytics and drive towards an extensible centralized platform to effectively enable rapid detection and rapid response for advanced security threats.



- 2017-04-19 Board approves graduation resolution.

- 2017-03-14 New Committer: Matt Foley

- 2017-03-14 New Committer: Jon Zeolla

- 2016-11-04 New Committer: Kyle Richardson

- 2016-10-14 New Committer: Otto Fowler

- 2016-09-29 New Committer: Michael Miklavcic.

- 2016-09-29 New Committer: Justin Leet.

- 2016-09-28 New PPMC Member: David Lyle.

- 2016-09-28 New PPMC Member: Nick Allen.

- 2016-03-22 New Committer: David Lyle

- 2016-02-11 New Committer: Nick Allen

- 2016-01-08 New Committer: Debo Dutta.

- 2015-12-06 Project enters incubation.

URIs and email addresses below refer to locations used by the project while in incubation. Now that the project has graduated, please remove "incubator" (and associated delimiters) from all structured names.


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://metron.incubator.apache.org/](http://metron.incubator.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/METRON/Metron+Wiki](https://cwiki.apache.org/confluence/display/METRON/Metron+Wiki)  |
| Mailing list | commits |  `commits`  `@`  `metron.incubator.apache.org`  |
| . | dev |  `dev`  `@`  `metron.incubator.apache.org`  |
| . | issues |  `issues`  `@`  `metron.incubator.apache.org`  |
| . | security |  `security`  `@`  `metron.incubator.apache.org`  |
| . | user |  `user`  `@`  `metron.incubator.apache.org`  |
| Bug tracking | . |  [Metron jira](https://issues.apache.org/jira/browse/METRON)  |
| Source code | Git |  [https://gitbox.apache.org/repos/asf/incubator-metron.git](https://gitbox.apache.org/repos/asf/incubator-metron.git)  |
| Mentors | ptgoetz | P. Taylor Goetz |
| . | mattmann | Chris Mattmann |
| . | omalley | Owen O'Malley |
| . | billie | Billie Rinaldi |
| . | vinodkv | Vinod Kumar Vavilapalli |
| PPMC | jimbaker | Jim Baker |
| . | mbittmann | Mark Bittmann |
| . | sheetal_dolas | Sheetal Dolas |
| . | ddutta | Debo Dutta |
| . | discovery | Discovery Gerdes |
| . | ptgoetz | P. Taylor Goetz |
| . | dev_warlord | Andrew Hartnett |
| . | dbhirko | Dave Hirko |
| . | reaperhulk | Paul Kehrer |
| . | bjkolly | Brad Kolarov |
| . | kirankom | Kiran Komaravolu |
| . | lmccay | Larry McCay |
| . | rmerriman | Ryan Merriman |
| . | . | Michael Perez |
| . | cporter | Charles Porter |
| . | prhodes | Phillip Rhodes |
| . | sirsean | Sean Schulte |
| . | jsirota | James Sirota |
| . | cestella | Casey Stella |
| . | . | Bryan Taylor |
| . | . | Ray Urciuoli |
| . | vinodkv | Vinod Kumar Vavilapalli |
| . | gvetticaden | George Vetticaden |
| . | smogg | Oskar Zabik |
| . | lyle | David Lyle |
| . | nallen | Nick Allen |
| Committers | Otto Fowler | otto |
| . | kylerichardson | Kyle Richardson |
| . | leet | Justin Leet |
| . | mmiklavcic | Michael Miklavcic |
| . | jonzeolla | Jon Zeolla |
| . | mattf | Matt Foley |


-  [https://whimsy.apache.org/board/minutes/Metron.html](https://whimsy.apache.org/board/minutes/Metron.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2015-10-24 | Make sure that the requested project name does not already exist. |
| 2015-10-24 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. Done [here](https://groups.google.com/d/msg/opensoc-support/rFlW2uSSvmU/Sw_cO-T2AAAJ) . |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2015-12-07 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2015-12-07 | Ask infrastructure to set up and archive mailing lists. |
| 2015-12-15 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2015-12-15 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2015-12-15 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2016-01-08 | Subscribe all Mentors on the pmc and general lists. |
| 2015-12-07 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2015-12-10 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2016-01-08 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2016-01-09 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2016-11-10 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2016-11-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2015-12-10 | Check that all active committers have submitted a contributors agreement. |
| 2015-12-10 | Add all active committers in the STATUS file. |
| 2015-12-10 | Ask root for the creation of committers' accounts on people.apache.org. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? YES

- Are there three or more independent committers? YES (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- Are project decisions being made in public by the committers? YES

- Are the decision-making guidelines published and agreed to by all of the committers? YES

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? YES

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
