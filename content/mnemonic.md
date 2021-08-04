Title: Mnemonic Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Mnemonic is an advanced hybrid memory storage oriented library, we've proposed a non-volatile/durable Java object model and durable computing service that bring several advantages to significantly improve the performance of massive real-time data processing/analytics. developers are able to use this library to design their cache-less and SerDe-less high performance applications.


<span class="graduated">The Mnemonic project graduated on 2017-11-15</span>



- 2016-03-03 Project enters incubation.

- 2016-05-24 the first official release.

- 2016-08-02 the second official release.

- 2016-10-21 the third official release.

- 2017-01-24 the fourth official release.

- 2017-03-13 the fifth official release.

- 2017-04-13 the sixth official release.

- 2017-05-04 the seventh official release.

- 2017-06-23 the eighth official release.

- 2017-09-13 the ninth official release.

- 2017-11-15 the tenth official release.


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://mnemonic.incubator.apache.org/](http://mnemonic.incubator.apache.org/)  |
| . | wiki |  [https://cwiki.apache.org/confluence/display/MNEMONIC/Apache+Mnemonic+Home](https://cwiki.apache.org/confluence/display/MNEMONIC/Apache+Mnemonic+Home)  |
| Mailing list | dev |  `dev`  `@`  `mnemonic.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `mnemonic.incubator.apache.org`  |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/MNEMONIC](https://issues.apache.org/jira/browse/MNEMONIC)  |
| Source code | Git |  [https://github.com/apache/incubator-mnemonic](https://github.com/apache/incubator-mnemonic)  |
| Champion | phunt | Patrick Hunt |
| Mentors | phunt | Patrick Hunt |
| . | apurtell | Andrew Purtell |
| . | jamestaylor | James Taylor |
| . | hsaputra | Henry Saputra |
| Committers | yanpingw | Yanping Wang |
| . | garyw | Gang(Gary) Wang |
| . | umamahesh | Uma Maheswara Rao G |
| . | drankye | Kai Zheng |
| . | rakeshr | Rakesh Radhakrishnan Potty |
| . | seanzhong | Sean Zhong |
| . | hsaputra | Henry Saputra |
| . | chhao01 | Hao Cheng |
| . | ddutta | Debojyoti Dutta |
| . | johnu | Johnu George |
| . | yzhao | Yanhui Zhao |
| . | peili | PeiLi Shen |


-  [April, 2016](https://wiki.apache.org/incubator/April2016) 

-  [September, 2016](https://wiki.apache.org/incubator/September2016) 

-  [December, 2016](https://wiki.apache.org/incubator/December2016) 

-  [March, 2017](https://wiki.apache.org/incubator/March2017) 

-  [June, 2017](https://wiki.apache.org/incubator/June2017) 

-  [September, 2017](https://wiki.apache.org/incubator/September2017) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2016-03-17 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html) Name Search jira [PODLINGNAMESEARCH-95](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-95)  |
| NA | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2016-03-24 | SGA was assigned by Intel, and the project was moved into ASF GIT https://gitbox.apache.org/repos/asf?p=incubator-mnemonic.git |
| 2016-03-11 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2016-03-11 | Ask infrastructure to set up and archive mailing lists. |
| 2016-03-31 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2016-03-12 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2016-04-18 | cwiki site setup is completed |
| 2016-04-04 | Completely migrated the project to Mnemonic infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2016-04-12 | Subscribe all Mentors on the pmc and general lists. |
| 2016-03-12 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2016-03-11 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2016-03-23 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2016-04-05 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2016-04-26 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2016-05-09 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2016-03-31 | Check that all active committers have submitted a contributors agreement. |
| 2016-03-11 | Add all active committers in the relevant section above. |
| 2016-03-12 | Ask root for the creation of committers' accounts in LDAP. |

## Project specific {#Project+specific}

 _NA_ 


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

 _NA_ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
