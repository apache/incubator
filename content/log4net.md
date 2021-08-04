Title: log4net


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The log4net project graduated on 2007-02</span>


The Log4net project graduated the incubator on 2007-02-17 and is now part of the Logging Services project. It implements a logging API similar to log4j but in the C# language.



- The Log4net project graduated the incubator on 2007-02-17 and is now part of the Logging Services project.

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://logging.apache.org/log4net](http://logging.apache.org/log4net)  |
| . | wiki | . |
| Mailing list | dev | log4net-dev@logging.apache.org |
| . | user | log4net-user@logging.apache.org |
| . | cvs | log4net-cvs@logging.apache.org |
| Bug tracking | JIRA |  [http://issues.apache.org/jira/browse/LOG4NET](http://issues.apache.org/jira/browse/LOG4NET)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/logging/log4net/trunk](https://svn.apache.org/repos/asf/logging/log4net/trunk)  |
| Mentors | id1 | Mark Womack |
| Committers | nicko | Nicko Cadell |
| . | niall | Niall Daley |
| . | drieseng | Gert Driesen |
| . | rgrabowski | Rob Grabowski |
| Extra | . | . |

| Date | Status |
|------|--------|
| 2004-05 | Log4net now supports building under the Mono Beta 1 runtime. |
| 2005-02 | The Logging Services PMC would like to see the log4net project graduate in the coming few months. A new log4net development release is in preparation which the LS PMC has approved. We intend to seek the approval of the Incubator PMC in the coming days. The finalised log4net version 1.2 should be released within the next quarter.<br></br><br></br>log4net is now using a JIRA issue tracker. |
| 2005-05 | The incubator approved the release of log4net 1.2.9 beta which is the first release of log4net under Apache. The upcoming release goals are to ensure consistent code quality and improve the available end user documentation.<br></br><br></br>The project's ongoing goal is to increase the number of active committers and to graduate from incubation. |
| 2005-08 | The log4net project is still in incubation, but it is active. The Logging Services PMC is currently voting on a new committer, Rob Grabowski (rgrabowski@apache.org), and the vote seems likely to pass. This would bring the number of active committers to 4, helping meet incubator exit criteria.<br></br><br></br>The log4net committers are working towards the next maintenance release with a focus on code quality and improving the available end user documentation. |
| 2005-10 | Log4net has elected Rob Grabowski (rgrabowski at apache dot org) as a new committer. This brings the number of active committers to 4, helping meet incubator exit criteria.<br></br><br></br>We have recently migrated from CVS to SVN.<br></br><br></br>We are working towards the next maintenance release with a focus on code quality and improving the available end user documentation. |
| 2006-01 | The log4net committers are working on compatibility with the .NET 2.0 releases from Microsoft and Mono. |
| 2007-02-17 | Graduation from Incubator to Logging Services. |

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-01-15 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| 2004-01-15 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| 2004-01-06 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-01-15 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2004-01-15 | Subscribe all Mentors on the pmc and general lists. |
| 2004-01-15 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2004-01-15 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2004-01-26 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2005-03-10 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2005-03-10 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2005-03-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| 2004-01-23 | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| 2004-01-23 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| 2004-01-15 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2004-01-15 | Ask infrastructure to set up and archive Mailing lists. |
| 2005-02-23 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2004-01-15 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._ 


 _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?


- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)


- Are project decisions being made in public by the committers?

From the discussions on log4net-dev@logging.apache.org that appears to be the case.



- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

Nicko Cadell has promtly responded to IP related concerns raised on the general@incubator and log4net-dev mailing lists.


## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
