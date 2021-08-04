Title: Apache ODF Toolkit Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The ODF Toolkit project retired from Apache Incubation on 2018-11-27</span>


<span class="retired">The ODF Toolkit project moved to The Document Foundation at [http://odftoolkit.org/](http://odftoolkit.org/) </span>


The ODF Toolkit is a set of Java modules that allow programmatic creation, scanning and manipulation of OpenDocument Format (ISO/IEC 26300 == ODF) documents. Unlike other approaches which rely on runtime manipulation of heavy-weight editors via an automation interface, the ODF Toolkit is lightweight and ideal for server use.



- 2018-11-27 Project removed from incubation.

- 2017-04-10 ODF Toolkit 0.6.2-incubating available

- 2017-03-07 We have a new mentor: Tom Barber.

- 2015-10-05 We have a new committer/PPMC: Damjan Jovanovic.

- 2014-06-02 ODF Toolkit 0.6.1-incubating available

- 2013-06-22 ODF Toolkit 0.6-incubating available

- ...

- 2011-11-16 We have a new committer: Oliver Rau.

- 2011-09-13 Website and Source Code migration complete.

- 2011-08-01 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www |  [Is now at http://odftoolkit.org/](http://odftoolkit.org/)  |
| . | wiki |  _To be migrated_  |
| Mailing list | dev |  `odf-dev`  `@`  `incubator.apache.org`  |
| . | users |  `odf-users`  `@`  `incubator.apache.org`  |
| . | commits |  `odf-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | . |  _ [https://issues.apache.org/jira/browse/ODFTOOLKIT/](https://issues.apache.org/jira/browse/ODFTOOLKIT/) _  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/odf/](https://svn.apache.org/repos/asf/incubator/odf/)  |
| Source code at the TDF | GIT |  [https://github.com/tdf/odftoolkit](https://github.com/tdf/odftoolkit)  |
| Mentors | magicaltrout | Tom Barber |
| . | nick | Nick Burch |
| . | yegor | Yegor Kozlov |
| . | robweir | Rob Weir |
| Committers | robweir | Rob Weir |
| . | damjan | Damjan Jovanovic |
| . | devinhan | Biao Han (Devin) |
| . | svanteschubert | Svante Schubert |
| . | daisyguo | Ying Chun Guo (Daisy) |
| . | dpharbison | Don Harbison |
| . | therabi | Andy Brown |
| . | wave | Dave Fisher |
| . | jsc | Juergen Schmidt |
| . | liudali | Da Li Liu |
| . | olira | Oliver Rau |
| . | fhopf | Florian Hopf |
| Extra | . | . |

The ODF Toolkit PPMC consists of all the committers and mentors listed above.




October 2013


- Three most important issues to address in the move towards graduation:

1. Grow the community, especially attracting new developers.

1. Address issues of too much code development happening outside of Apache

1. Hold an informal graduation readiness vote


- Any issues that the Incubator PMC (IPMC) or ASF Board wish/need to be aware of:<br></br>It has recently been pointed out that the project status page on the Incubator project site is out of date, we hope to update that shortly.

- How has the community developed since the last report?<br></br>Higher feed-back from the users mailing list, but no new developers.<br></br><br></br>Discussion has started, but without much conclusion, of whether we should aim for TLP status, or merge into an existing TLP with similar alignment, such as POI or OpenOffice.

- How has the project developed since the last report?<br></br>Clear unnecessary dependency from the Clarizza project.

- Date of last release:<br></br>2017-04-10

- When were the last committers or PMC members elected:<br></br>Not for a long while...


August 2011

The ODF Toolkit is a set of Java modules that allow programmatic creation, scanning and manipulation of OpenDocument Format (ISO/IEC 26300 == ODF) documents. Unlike other approaches which rely on runtime manipulation of heavy-weight editors via an automation interface, the ODF Toolkit is lightweight and ideal for server use.


ODF Toolkit entered incubation on Aug 1st, 2011.



- Most important issues to address.

1. Moving the community from the ODF Toolkit Union to Apache and learning the Apache Way

1. Growing the community, increasing diversity of committers

1. Grants for the transfer of existing code, documentation etc to Apache

1. Migration of existing things to Apache infrastructure, including code repository, website, mailing list, bugzilla and wiki.

1. Successful podling release.


- Any issues that the Incubator PMC or ASF Board might wish/need to be aware of:<br></br>None at this time.

- How has the community developed since the last report<br></br>Just getting started. After mailing lists are ready (INFRA-3809), we will start to discuss migration and new release. At the same time, we will invite the existing users to this new community and try to attract more new people join us.

- How has the project developed since the last report.<br></br>None at this time. Just getting started.

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2011-09-01 | Ask infrastructure to create source repository modules and grant the committers karma. Completed 2011-09-13 |
| 2011-08-01 | Ask infrastructure to set up and archive mailing lists. Completed 2011-08-15. |
| 2011-08-24 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla), and migrate in existing issues. _Pending_  |
| ....-..-.. | Ask infrastructure to set up wiki (Confluence, Moin). |
| ....-..-.. | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2011-08-01 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2011-08-01 | Subscribe all Mentors on the pmc and general lists. |
| 2011-09-13 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2011-08-01 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

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
| 2011-08-15 | Check that all active committers have submitted a contributors agreement. |
| 2011-08-15 | Add all active committers in the STATUS file. |
| 2011-08-15 | Ask root for the creation of committers' accounts on people.apache.org. |

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
