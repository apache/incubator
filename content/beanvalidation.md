Title: Bean Validation Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Bean Validation project graduated on 2012-02-15</span>


The Bean Validation project will create an implementation of the Java EE Bean Validation specification.



- 2010-03-01 Project enters incubation.


- link to the main website


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/bval/](http://incubator.apache.org/bval/)  |
| . | wiki |  [http://cwiki.apache.org/confluence/display/BeanValidation/](http://cwiki.apache.org/confluence/display/BeanValidation/)  |
| Mailing list | dev |  `bval-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `bval-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | . |  [https://issues.apache.org/jira/browse/BVAL](https://issues.apache.org/jira/browse/BVAL)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/bval/](https://svn.apache.org/repos/asf/incubator/bval/)  |
| Mentors | kevan | Kevan Miller |
| . | niallp | Niall Pemberton |
| . | lresende | Luciano Resende |
| . | matzew | Matthias Wessendorf |
| Committers | romanstumm | Roman Stumm |
| . | dwoods | Donald Woods |
| . | mnour | Mohammad Nour El-Din |
| . | simonetripodi | Simone Tripodi |
| . | jrbauer | Jeremy Bauer |
| . | gpetracek | Gerhard Petracek |
| . | struberg | Mark Struberg |


-  [April 2010](http://wiki.apache.org/incubator/April2010#BeanValidation)  [May 2010](http://wiki.apache.org/incubator/May2010#BeanValidation) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2012-01-08 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. DONE via trademarkia.com and others |
| 2012-01-08 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. DONE, not applicable. |
| 2012-01-08 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. DONE, not applicable. |
| 2012-01-08 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. DONE, not applicable. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-03-23 | Ask infrastructure to create source repository modules and grant the committers karma.<br></br>(see [INFRA-2528](http://issues.apache.org/jira/browse/INFRA-2528) and [INFRA-2529](http://issues.apache.org/jira/browse/INFRA-2529) ) |
| 2010-03-12 | Ask infrastructure to set up and archive mailing lists.<br></br>(see [INFRA-2527](http://issues.apache.org/jira/browse/INFRA-2527) ) |
| 2010-03-16 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla).<br></br>(see [INFRA-2530](http://issues.apache.org/jira/browse/INFRA-2530) ) |
| 2010-03-17 | Ask infrastructure to set up wiki (Confluence, Moin).<br></br>(see [INFRA-2531](http://issues.apache.org/jira/browse/INFRA-2531) ) |
| 2010-03-17 | Migrate the project to our infrastructure.<br></br>(see [r924153](http://svn.apache.org/viewvc?view=revision&amp;revision=924153) ) |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2010-02-23 | Identify all the Mentors for the incubation, by asking all that can be Mentors.<br></br>(see [Vote thread](http://markmail.org/message/37oaihbwwiuptt4q) ) |
| 2010-03-12 | Subscribe all Mentors on the pmc and general lists. |
| 2010-03-12 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-04-05 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html'<br></br>(see [here](http://markmail.org/message/ck3pwlcukfp53g4f) ) |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-10-27 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.<br></br>( _Software Grant from KEBA AG_ ) |
| 2010-03-17 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright.<br></br>(see [BVAL-3](http://issues.apache.org/jira/browse/BVAL-3) ) |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| N/A | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute.<br></br>( _all code is being distributed under AL 2.0_ ) |
| N/A | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms.<br></br>( _all code is being distributed under AL 2.0_ ) |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-03-23 | Check that all active committers have submitted a contributors agreement.<br></br>(see [INFRA-2529](http://issues.apache.org/jira/browse/INFRA-2529) ) |
| 2010-03-23 | Add all active committers in the STATUS file. |
| 2010-03-23 | Ask root for the creation of committers' accounts on people.apache.org.<br></br>(see [INFRA-2529](http://issues.apache.org/jira/browse/INFRA-2529) ) |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? (checked, DONE.)

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) (checked, DONE.)

- Are project decisions being made in public by the committers? (DONE.)

- Are the decision-making guidelines published and agreed to by all of the committers? (checked, DONE.)

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? (checked, DONE.)

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
