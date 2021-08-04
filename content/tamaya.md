Title: Tamaya Project Status Page
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The Tamaya project retired from Apache Incubation on 2020-04-30</span>


Tamaya is a highly flexible configuration solution based on an modular, extensible and injectable key/value based design, which should provide a minimal but extendible modern and functional API leveraging SE, ME and EE environments.



- 2020-04-30 Apache Tamaya has retired

- 2015-08-22 Apache Tamaya 0.1-incubating has been released.

- 2015-01-25 New committer Reinhard Sandtner.

- 2014-11-14 Project enters incubation.


- Originally, Tamaya was at https://github.com/java-config


- TODO: link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- TODO: link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www | Podling: [http://tamaya.incubator.apache.org/](http://tamaya.incubator.apache.org/)  |
| . | wiki | . |
| Mailing list | dev |  `dev`  `@`  `tamaya.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `tamaya.incubator.apache.org`  |
| . | private |  `private`  `@`  `tamaya.incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/TAMAYA](https://issues.apache.org/jira/browse/TAMAYA)  |
| Source code | Git |  [https://github.com/apache?q=tamaya](https://github.com/apache?q=tamaya)  |
| Mentors | dblevins | David Blevins |
| . | johndament | John D. Ament |
| . | gpetracek | Gerhard Petracek |
| . | struberg | Mark Struberg |
| Committers | anatole | Anatole Tresch |
| . | aalmiray | Andres Almiray |
| . | wkeil | Werner Keil |
| . | otaviojava | Otávio Santana |
| . | plexus | Oliver B. Fischer |
| . | rmannibucau | Romain Manni-Bucau |


-  [Board Reports](https://whimsy.apache.org/board/minutes/Tamaya.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2014-11-14 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |
| 2014-11-14 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names: N/A. |
| 2014-11-14 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance: N/A. |
| 2014-11-14 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. DONE |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2014-11-14 | Ask infrastructure to create source repository modules and grant the committers karma. DONE by John D. Ament in [INFRA-8635](https://issues.apache.org/jira/browse/INFRA-8635)  |
| 2014-11-14 | Ask infrastructure to set up and archive mailing lists. DONE by John D. Ament in [INFRA-8635](https://issues.apache.org/jira/browse/INFRA-8635)  |
| 2014-11-14 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). DONE by John D. Ament in [INFRA-8635](https://issues.apache.org/jira/browse/INFRA-8635)  |
| 2014-11-14 | Ask infrastructure to set up wiki (Confluence, Moin). TBD. |
| 2014-11-25 | Migrate the project to our infrastructure. Initial import vote passed. DONE by Anatole Tresch |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2014-11-14 | Subscribe all Mentors on the pmc and general lists. DONE by John D. Ament |
| 2014-11-14 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file). DONE by John D. Ament - all mentors have access already. |
| 2014-11-20 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' DONE by John D. Ament |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2014-11-20 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. ONGOING. DONE by Anatole Tresch - Anatole's original source, his ICLA is now on file. |
| 2014-11-22 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. DONE by Anatole Tresch - initial source import includes proper ASF headers. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. ONGOING |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. ONGOING |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. ONGOING. |
| ....-..-.. | Add all active committers in the STATUS file. TODO |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

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
