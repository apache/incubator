Title: Apache Imperius Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The Imperius project retired on 2011-05-14</span>


Imperius (Simple Policy Language) or SPL - Is a simple standards based object-oriented policy language that allows expression of management policies using condition-action rules. Imperius provides an extensible set of over 100 operations for expressing conditions and actions. Imperius is a generalization of the CIM-SPL language. Conversely, CIM-SPL can be thought of as Imperius with CIM binding. Imperius can be extended to create similar bindings for other environments. JavaSPL (Imperius with Java binding) is another such example.



- 2011-05-14 Retired

- 2008-01-18 New committer: Erik Bengtson

- 2007-12-22 First code drop


-  [link to the main website](http://incubator.apache.org/imperius) 


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/imperius/](http://incubator.apache.org/imperius/)  |
| . | wiki | . |
| Mailing list | dev |  `imperius-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `imperius-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | Jira |  [http://issues.apache.org/jira/browse/imperius](http://issues.apache.org/jira/browse/imperius)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/incubator/imperius](http://svn.apache.org/repos/asf/incubator/imperius)  |
| Mentors | stoddard | Bill Stoddard |
| . | clr | Craig Russell |
| . | fhanik | Filip Hanik |
| . | kevan | Kevan Miller |
| Committers | . | . |
|  | jneeraj | Neeraj Joshi |
|  |  | Prashant Baliga |
|  | macsun | Mark Carlson |
|  | michaelknunez | Mike Nunez |
|  | ebengston | Erik Bengston |
| Extra | . | . |


-  [December 2007](http://svn.apache.org/viewvc/incubator/imperius/board/2007-12.txt?view=markup) 

-  [January 2008](http://svn.apache.org/viewvc/incubator/imperius/board/2008-01.txt?view=markup) 

-  [April 2008](http://svn.apache.org/viewvc/incubator/imperius/board/2008-04.txt?view=markup) 

-  [July 2008](http://svn.apache.org/viewvc/incubator/imperius/board/2008-07.txt?view=markup) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date(YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2007-11-10 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2007-11-10 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2007-11-10 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2007-11-10 | Subscribe all Mentors on the pmc and general lists. |
| 2007-11-10 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2007-11-10 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2007-10-01 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2007-12-08 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2007-12-08 | Check and make sure that for all code included with the distribution that is not under the Apache license have the right to combine with Apache-licensed code and redistribute. |
| 2007-12-08 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2007-12-08 | Check that all active committers have submitted a contributors agreement. |
| 2007-12-08 | Add all active committers in the STATUS file. |
| 2007-11-08 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2007-12-08 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2007-12-08 | Ask infrastructure to set up and archive Mailing lists. |
| 2007-12-08 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| N/A | Migrate the project to our infrastructure. |

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
