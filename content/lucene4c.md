Title: Lucene4c Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The Lucene4c project retired on 2006-10-15</span>


Lucene4c is a port of the [Lucene](http://lucene.apache.org/java/) search engine from Java to C, built on top of the [Apache Portable Runtime](http://apr.apache.org/) .


Unlike other Lucene ports, Lucene4c does not simply stick to the API used in the original Java based Lucene, instead it attempts to build an idiomatic APR/C based API that will be familiar to C programmers while making use of the file formats and algorithms created by the original Lucene project.



- 2006-10-15 - Project closed due to lack of activity


- Project Website: [http://electricjellyfish.net/garrett/lucene4c/](http://electricjellyfish.net/garrett/lucene4c/) 


- Project Mailing Lists: None yet.

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/lucene4c/](http://incubator.apache.org/lucene4c/)  |
|  | wiki | None, will use Lucene wiki for the time being |
| Mailing list | dev | lucene4c-dev@incubator.apache.org |
|  | commits | lucene4c-commits@incubator.apache.org |
| Bug tracking | Jira |  [http://issues.apache.org/jira/](http://issues.apache.org/jira)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/lucene4c](https://svn.apache.org/repos/asf/incubator/lucene4c)  |
| Mentors | ehatcher | Erik Hatcher |
| Committers | rooneg | Garrett Rooney |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| ....-..-.. | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| ....-..-.. | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| ....-..-.. | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| ....-..-.. | Ask infrastructure to create source repository modules and grant the committers karma. |
| ....-..-.. | Ask infrastructure to set up and archive Mailing lists. |
| ....-..-.. | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| ....-..-.. | Migrate the project to our infrastructure. |

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
