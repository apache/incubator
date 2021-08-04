Title: Buildr Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Buildr project graduated on 2009-02-23</span>


Buildr is a build system for Java applications written in Ruby. We wanted something that’s simple and intuitive to use, so we only need to tell it what to do, and it takes care of the rest. But also something we can easily extend for those one-off tasks, with a language that’s a joy to use. And of course, we wanted it to be fast, reliable and have outstanding dependency management.



- 2008-10-16 Buildr 1.3.3 release.

- 2008-08-20 Antoine Contal has been voted in the Buildr PPMC.

- 2008-08-20 Antoine Contal has been accepted as a new committer.

- 2008-07-24 Buildr 1.3.2 release.

- 2008-05-28 Buildr 1.3.1 release.

- 2008-04-30 Buildr 1.3 release.

- 2008-04-25 Victor Hugo Borja has been accepted in the Buildr PPMC.

- 2008-01-30 Victor Hugo Borja is a new committer.

- 2007-11-01 Buildr enters the Incubator.


- Web site: [http://incubator.apache.org/buildr](http://incubator.apache.org/buildr) 


- User mailing-list: [buildr-user@incubator.apache.org](mailto:buildr-user-subscribe@incubator.apache.org) 


- Dev mailing-list: [buildr-dev@incubator.apache.org](mailto:buildr-dev-subscribe@incubator.apache.org) 


- Jira: [https://issues.apache.org/jira/browse/BUILDR](https://issues.apache.org/jira/browse/BUILDR) 

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/buildr/](http://incubator.apache.org/buildr/)  |
| Mailing List | dev |  [buildr-dev@incubator.apache.org](mailto:buildr-dev-subscribe@incubator.apache.org)  |
| . | commits |  [buildr-commits@incubator.apache.org](mailto:buildr-commits-subscribe@incubator.apache.org)  |
| Bug tracking | Jira |  [https://issues.apache.org/jira/browse/BUILDR](https://issues.apache.org/jira/browse/BUILDR)  |
| Source code | svn |  [http://svn.apache.org/repos/asf/incubator/buildr/](http://svn.apache.org/repos/asf/incubator/buildr/)  |
| Mentors | jim | Jim Jagielski |
| . | yoavs | Yoav Shapira |
| . | mriou | Matthieu Riou |
| Committers | assaf | Assaf Arkin |
| . | boisvert | Alex Boisvert |
| . | lacton | Antoine Contal |
| . | mriou | Matthieu Riou |
| . | vborja | Victor Hugo Borja |


-  [November 2007](http://wiki.apache.org/incubator/November2007) 

-  [December 2007](http://wiki.apache.org/incubator/December2007) 

-  [January 2008](http://wiki.apache.org/incubator/January2008) 

-  [April 2008](http://wiki.apache.org/incubator/April2008) 

-  [August 2008](http://wiki.apache.org/incubator/August2008) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2007-11-15 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2007-11-01 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2007-11-13 | Subscribe all Mentors on the pmc and general lists. |
| 2007-11-13 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2007-11-13 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2007-11-10 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2008-10-17 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2008-04 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2008-04 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2007-11-01 | Check that all active committers have submitted a contributors agreement. |
| 2007-11-01 | Add all active committers in the STATUS file. |
| 2007-11-01 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2007-11-02 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2007-11-01 | Ask infrastructure to set up and archive Mailing lists. |
| 2007-11-01 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2007-11-13 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

| date | item |
|------|------|
| 2008-03-22 | Clarify policy regarding Gem dependencies and the Ruby license. |

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

# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to a new PMC, has the board voted to accept it? Yes.

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?

- Yes. The resolution to make Buildr a TLP has been approved in Dec. 2008.
