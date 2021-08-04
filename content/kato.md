Title: Kato Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the official project status.


Please see the [Kato website](http://incubator.apache.org/kato) for information on the project itself.


<span class="retired">The Kato project retired on 2012-08-01</span>


JSR 326 is intended to be a Java API specification for standardising how and what can be retrieved from the contents of post-mortem artefacts -- typically process and JVM dumps. Project Kato is intended to be the place where the Specification, Reference implementation (RI) and Technology Compatibility Kit (TCK) are openly created. The intention is that the Specification and RI will be developed in tight unison, guided by a user-story-focused approach to ensure that real-world problems drive the project from the beginning.


Unusually for new APIs, this project will endeavour to encompass the old and the new. A diagnostic solution that only works when users move to the latest release does little to improve diagnosability in the short term. This project will consume existing dump artefacts as well as possible while developing an API that can address the emerging trends in JVM and application directions. The most obvious of these trends are the exploitation of very large heaps, alternative languages and, paradoxically for Java, the increased use of native memory through vehicles such as NIO.



- August 2012: Kato retired.


-  [Kato website](http://incubator.apache.org/kato) 


- TODO: link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- TODO: link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/kato/](http://incubator.apache.org/kato/)  |
| . | wiki |  [http://cwiki.apache.org/KATO/](http://cwiki.apache.org/KATO/)  |
| Mailing list | dev |  `kato-dev`  `@`  `incubator.apache.org`  |
| . | commits |  `kato-commits`  `@`  `incubator.apache.org`  |
| . | spec |  `kato-spec`  `@`  `incubator.apache.org`  |
| Bug tracking | JIRA |  [http://issues.apache.org/jira/browse/KATO/](http://issues.apache.org/jira/browse/KATO/)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/kato/](https://svn.apache.org/repos/asf/incubator/kato/)  |
| Mentors | antelder | Ant Elder |
| . | rdonkin | Robert Burrell Donkin |
| . | geirm | Geir Magnusson Jr. |
| Committers | . | . |
| . | spoole | Steve Poole |
| . | monteith | Stuart Monteith |
| . | cristal | Carmine Cristallo |
| . | riccole | Richard Cole |
| . | sgoyal | Sonal Goyal |
| Extra | . | . |


- Status reports due on March, June, September, December.
Status reports are held on the Incubators wiki:

-  [June 2009](http://wiki.apache.org/incubator/June2009) 

-  [March 2009](http://wiki.apache.org/incubator/March2009) 

-  [February 2009](http://wiki.apache.org/incubator/February2009) 

-  [January 2009](http://wiki.apache.org/incubator/January2009) 

-  [December 2008](http://wiki.apache.org/incubator/December2008) 

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

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| ....-..-.. | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-03-10 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2012-08-18 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
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
