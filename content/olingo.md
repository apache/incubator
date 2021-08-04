Title: Apache Olingo Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Olingo project graduated on 2014-03-19</span>


Apache Olingo is a generic Java language implementation of the OData 2.0 specification which will serve as a code base for the upcoming OASIS OData specification.



- 2013-07-08 Project enters incubation.

- 2013-10-16 Release 1.0.0

- 2013-10-30 New committer: V, Deepashree

- 2013-12-05 New committer: Sven Kobler

- 2014-02-10 Release 1.1.0

- 2014-02-10 New committer: Fabio Martelli

- 2014-02-10 New committer: Massimiliano Perrone

- 2014-02-10 New committer: Eduard Koller

- 2014-02-10 New committer: Challen He

- 2014-02-10 New committer: Bing Li

- 2014-02-14 New contribution: OData 3.0 Java Client Library

- 2014-02-14 New contribution: OData 3.0 JavaScript Client Library

- 2014-03-19 Apache Olingo graduates from incubator to a TLP


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://olingo.incubator.apache.org/](http://olingo.incubator.apache.org/)  |
| . | wiki |  [https://wiki.apache.org/Olingo/](https://wiki.apache.org/Olingo/)  |
| Mailing list | dev |  `dev`  `@`  `olingo.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `olingo.incubator.apache.org`  |
| Bug tracking | . |  [OLINGO](https://issues.apache.org/jira/browse/OLINGO)  |
| Source code | GIT | OData 2.0 Java: [https://gitbox.apache.org/repos/asf/incubator-olingo-odata2](https://gitbox.apache.org/repos/asf/incubator-olingo-odata2) <br></br>OData 4.0 Java: [https://gitbox.apache.org/repos/asf/incubator-olingo-odata4](https://gitbox.apache.org/repos/asf/incubator-olingo-odata4) <br></br>OData 4.0 JavaScript: [https://gitbox.apache.org/repos/asf/incubator-olingo-odata4-js](https://gitbox.apache.org/repos/asf/incubator-olingo-odata4)  |
| Mentors | fmui | Florian Müller |
| . | wave | Dave Fisher |
| . | adc | Alan Cabrera |
| Committers | sklevenz | Stephan Klevenz |
| . | ilgrosso | Francesco Chicchiriccò |
| . | jhuesken | Jens Huesken |
| . | chrisam | Christian Amend |
| . | mibo | Michael Bolz |
| . | tboehm | Tamara Boehm |
| . | chandanva | Chandan V A |
| . | anirbanroy | Anirban Roy |
| . | chitresh | Chitresh Chauhan |
| . | jobinjohn | Jobin John |
| . | jsi | Joerg Singler |
| . | deepa | V, Deepashree |
| . | koblers | Sven Kobler |
| . | fmartelli | Fabio Martelli |
| . | massi | Massimiliano Perrone |
| . | eduardk | Eduard Koller |
| . | challenh | Challen He |
| . | bingl | Bing Li |
| Extra | . | . |


-  [August 2013](http://wiki.apache.org/incubator/August2013) 

-  [September 2013](http://wiki.apache.org/incubator/September2013) 

-  [October 2013](http://wiki.apache.org/incubator/October2013) 

-  [January 2014](http://wiki.apache.org/incubator/January2014) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2013-11-06 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html) <br></br> **DONE** (see PODLINGNAMESEARCH-42) |
| 2013-07-08 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names.<br></br> **DOES NOT APPLY**  |
| 2013-07-08 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance.<br></br> **DOES NOT APPLY**  |
| 2013-07-08 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted.<br></br> **DONE**  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2013-07-16 | Ask infrastructure to create source repository modules and grant the committers karma.<br></br> **DONE**  |
| 2013-07-10 | Ask infrastructure to set up and archive mailing lists.<br></br> **DONE**  |
| 2013-07-18 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla).<br></br> **DONE**  |
| 2014-01-14 | Ask infrastructure to set up wiki (Confluence, Moin). <br></br> **DONE** |
| ....-..-.. | Migrate the project to our infrastructure.<br></br> **DOES NOT APPLY**  |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2013-07-08 | Identify all the Mentors for the incubation, by asking all that can be Mentors.<br></br> **DONE**  |
| 2013-07-10 | Subscribe all Mentors on the pmc and general lists.<br></br> **DONE**  |
| 2013-07-10 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file)<br></br> **DONE**  |
| 2013-07-08 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html'<br></br> **DONE**  |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2013-07-18 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.<br></br> **DONE**  |
| 2013-10-16 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright.<br></br> **DONE**  |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2013-10-16 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute.<br></br> **DONE**  |
| 2013-10-16 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.<br></br> **DONE**  |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2013-08-01 | Check that all active committers have submitted a contributors agreement.<br></br> **DONE**  |
| 2013-08-01 | Add all active committers in the STATUS file.<br></br> **DONE**  |
| 2013-08-01 | Ask root for the creation of committers' accounts on people.apache.org.<br></br> **DONE**  |

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
