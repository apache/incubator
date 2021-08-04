Title: log4cxx


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The log4cxx project graduated on 2005-01-11</span>However it has now re-entered the Incubator as [log4cxx2](log4cxx2.html) 


On 2004-11-27, the log4cxx project has been voted in by the Logging Services PMC to become part of the Logging Services project. It implements a logging API similar to log4j but in the C++ language.



- 2013-12-09: Log4cxx returns to the incubator with a new group of committers as [log4cxx2](log4cxx2.html) 

Curt Arnold currently leads the log4cxx effort. He took over from Michael Catanzariti, project founder, who is temporarily absent on a year long trip around the world. The Logging Services PMC found this smooth transition particularly reassuring.


Moreover, log4cxx has decided to base its upcoming 0.9.8 "snapshot" on APR which constitutes yet another excellent sign of its integration within the ASF.


| item | type | reference |
|-------|-------|------------|
| Website | www | http://logging.apache.org/log4cxx |
| . | wiki | . |
| Mailing list | dev | log4cxx-dev@logging.apache.org (to be created) |
| . | cvs | log4cxx-cvs@logging.apache.org (to be created) |
| Bug tracking | . | http://nagoya.apache.org/jira/secure/BrowseProject.jspa?id=10550 |
| Source code | CVS | logging-log4cxx |
| Mentors | id1 | Ceki Gulcu |
| Committers | . | Curt Arnorld, Michael Catanzariti, Christophe de Vienne |
| Extra | . | . |


- none

Reports were sent to the Board instead.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-01-21 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-01-15 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2004-01-15 | Subscribe all Mentors on the pmc and general lists. |
| 2004-01-15 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2004-01-15 | Tell Mentors to track progress in the file 'incubator/projects/log4cxx.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2004-02-12 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-06-14 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2004-11-27 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2004-11-27 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

C. Arnold writes: log4cxx currently depends on libxml2 (LGPL) or MSXML for XML configuration. Migration to Apache Portable Runtime in progress.


## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2004-02-12 | Check that all active committers have submitted a contributors agreement. |
| 2004-03-04 | Ask root for the creation of committers' accounts on cvs.apache.org. |

3 current committers: carnold, cdevienne, mcatan. There are mutually independent and without any known relationship with a single commercial entitiy.


## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| 2004-03 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2004-01-15 | Ask infrastructure to set up and archive Mailing lists. |
| 2004-05-21 | A decision has been made to chose JIRA. |
| 2004-03 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


The project has decided rely on Apache APR. Migration is in progress.


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._ 


 _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

Curt Arnold currently leads the log4cxx effort. He took over from Michael Catanzariti, project founder, who is temporarily absent on a year long trip around the world. The Logging Services PMC found this smooth transition particularly reassuring.



- Are there three or more independent committers? (The legaldefinition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

See previous comments.



- Are project decisions being made in public by the committers?

Voting examples APR: http://nagoya.apache.org/eyebrowse/ReadMsg?listName=log4cxx-dev@loggin .apache.org&amp;msgNo=331



- Are the decision-making guidelines published and agreed to by all of the committers?

0.9.6 and 0.9.7 appeared to be released with no public discussion. 0.9.8 discussion: http://nagoya.apache.org/eyebrowse/ReadMsg?listName=log4cxx-dev@loggin .apache.org&amp;msgNo=338


## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

Yes. It has on 2004-11-27.



- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?

Yes, it has voted so on 2005-01-11.

