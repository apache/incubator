Title: Apache Chemistry Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Chemistry project graduated on 2010-02-16</span>


Apache Chemistry is an implementation of the OASIS CMIS specification in Java, Python and PHP.



- 2011-02-16 Project graduates to [TLP](http://chemistry.apache.org/) !

- 2011-01-21 Second release of the OpenCMIS Java client and server, OpenCMIS 0.2.0-incubating

- 2011-01-18 CMIS.net implementation in .Net started

- 2010-09-17 First release of the OpenCMIS Java client and server, OpenCMIS 0.1.0-incubating

- 2010-06-08 php-cmis-lib contribution accepted, and Richard McKnight added as a new committer

- 2010-02-15 OpenCMIS contribution accepted and David Ward, Florian Müller, Jens Hübel, Martin Hermes, Paul Goetz and Stephan Klevenz added as new committers (6)

- 2010-02-10 Nick Burch joins the project as a new mentor

- 2010-02-10 cmislib contribution accepted and Jeff Potts added as a new committer

- 2009-05-15 David Caruana added as a new committer

- 2009-04-30 Project enters incubation

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/chemistry/](http://incubator.apache.org/chemistry/)  |
| . | wiki | . |
| Mailing list | dev | chemistry-dev@incubator.apache.org |
| . | commits | chemistry-commits@incubator.apache.org |
| Bug tracking | jira |  [CMIS](https://issues.apache.org/jira/browse/CMIS)  |
| Source code | svn |  [https://svn.apache.org/repos/asf/incubator/chemistry/](https://svn.apache.org/repos/asf/incubator/chemistry/)  |
| Mentors | gianugo | Gianugo Rabellino |
| . | jukka | Jukka Zitting |
| . | nick | Nick Burch |
| Committers | bs | Bogdan Stefanescu |
| . | dcaruana | David Caruana |
| . | dpfister | Dominique Pfister |
| . | fguillaume | Florent Guillaume |
| . | gabriele | Gabriele Columbro |
| . | paolo | Paolo Mottadelli |
| . | sfermigier | Stéfane Fermigier |
| . | slacoin | Stéphane Lacoin |
| . | stan | Sun Seng David Tan |
| . | uncled | David Nuescheler |
| . | jpotts | Jeff Potts |
| . | dward | David Ward |
| . | fmui | Florian Müller |
| . | jens | Jens Hübel |
| . | hermesm | Martin Hermes |
| . | pgoetz | Paul Goetz |
| . | sklevenz | Stephan Klevenz |
| . | richardm | Richard McKnight |
| Extra | . | . |

The Chemistry PPMC consists of all the committers and mentors listed above.




January 2011

Apache Chemistry is an effort to provide an implementation of the CMIS (Content Management Interoperability Services) specification in Java, Python, PHP, JavaScript (and possibly other languages). Chemistry entered incubation on April 30th, 2009.


Issues to address in the move towards graduation:



- First non-Java release (PHP, Python)

Issues for Incubator PMC or ASF Board:



- None.

Community development since the last report:



- We have 8 active committers working on three sub projects. No new committer has been added last quarter. There are a few regular contributors of bug reports, suggestions and patches.

- Traffic on the dev list is steady.

Project development since the last report:



- A second release of the Java subproject (OpenCMIS 0.2) is under way. A release candidate is available.

- The Java APIs have been refined and should now be stable.

- Continued work on the draft browser binding (JSON protocol) in the sandbox.

- The Python subproject (cmislib) is preparing for its first release since joining the project.

- The PHP subproject (phpclient) increased coverage of the spec, refined some of the existing functionality and updated documentation. Next steps are to begin preparations for the first release.


October 2010

Apache Chemistry is an effort to provide an implementation of the CMIS (Content Management Interoperability Services) specification in Java, Python, PHP, JavaScript (and possibly other languages). Chemistry entered incubation on April 30th, 2009.


Issues to address in the move towards graduation:



- First non-Java release (PHP, Python)

Issues for Incubator PMC or ASF Board:



- None.

Community development since the last report:



- None.

Project development since the last report:



- A first release of the Java subproject (OpenCMIS 0.1) was done.

- Work to refine the Java APIs continues.

- Continued work on the draft browser binding (JSON protocol) in the sandbox.


July 2010

Apache Chemistry is an effort to provide an implementation of the CMIS (Content Management Interoperability Services) specification in Java, Python, PHP, JavaScript (and possibly other languages). Chemistry entered incubation on April 30th, 2009.


Issues to address in the move towards graduation:



- First Java release (an attempt has been made but there were issues).

- First non-Java release

Issues for Incubator PMC or ASF Board:



- None.

Community development since the last report:



- PHP library added, with Richard McKnight as new committer.

Project development since the last report:



- Oasis CMIS 1.0 spec is final.

- Code merge OpenCMIS / Chemistry completed, only one Java code base now.

- Improvement / stabilization of the client API.

- Improvement of the online documentation in the wiki.

- Enhanced query integration in OpenCMIS.

- First prototyping around the proposed browser binding (JSON protocol) in the sandbox.

- More license documentations to make release candidate ASF compliant.

- Preparations for a first release 0.1.


April 2010

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS (Content Management Interoperability Services) specification. Chemistry entered incubation on April 30th, 2009.


A list of the three most important issues to address in the move towards graduation:



- First formal incubator release. Although this is planned, there are several tasks to complete (e.g. documentation) and a learning curve to climb.

Any issues that the Incubator PMC or ASF Board might wish/need to be aware of:


There are currently no issues requiring board or Incubator PMC attention.


How has the community developed since the last report



- The OpenCMIS project (originally proposed to the Incubator which also targets a Java implementation of CMIS) has joined Apache Chemistry, with the following new committers - David Ward, Florian Müller, Jens Hübel, Martin Hermes, Paul Goetz and Stephan Klevenz

- Jeff Potts has contributed his Python CMIS client library and became a committer
.
- Nick Burch has joined as a new mentor
.
- Mailing list traffic has increased 2.5 times since last quarter.

How has the project developed since the last report



- Development continues at a steady pace, and Chemistry now targets CMIS 1.0 CD07, the version of the specification submitted to OASIS.

- Command-line Shell has been contributed (from Nuxeo).

- Hudson builds have been setup and stabilized.

- An agreement has been been met on how to merge the Chemistry and OpenCMIS codebases. The merge will take place in a branch, until stabilized (which should take no longer than 2 weeks).

- A first formal incubator release of the merged Chemistry/OpenCMIS codebases is planned shortly after the merge is complete.


January 2010

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS specification. Chemistry entered incubation on April 30th, 2009.


There are currently no issues requiring board or Incubator PMC attention.


Community



- Another project (OpenCMIS) targetting a Java implementation of CMIS, like Chemistry, has been proposed to the Incubator. Discussions between OpenCMIS and Chemistry developers have identified areas of possible collaboration but the OpenCMIS incubation status has not moved forward.

- Chemistry is now being used by companies or individuals outside the initial developers.

Development



- Development continues at a steady pace, mostly driven by Florent Guillaume.

- Chemistry now targets CMIS 1.0 CD 05 draft, soon to be 06.

- Nuxeo will contribute a command-line shell for CMIS in a few days.

- SOAP bindings are planned in the coming days as well.

Issues before graduation



- Stabilize the general interest into a sustainable development community

- Set up Hudson builds.

- Create an Apache release of the Chemistry codebase


October 2009

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS specification. Chemistry entered incubation on April 30th, 2009.


There are currently no issues requiring board or Incubator PMC attention.


Community



- No notable community changes.

Development



- Development continues at a steady pace, mostly driven by Florent Guillaume and Gabriele Columbro.

- A full 0.62/0.70 CMIS AtomPub binding TCK contributed and maintained against the spec by David Caruana

- The codebase is currently split to two branches, targeting different draft versions of CMIS.

Infrastructure



- Chemistry is planning to use repository.apache.org as a Maven deployment target

Issues before graduation



- Stabilize the general interest into a sustainable development community

- Make sure that all licensing details conform with Apache policies

- Create an Apache release of the Chemistry codebase


July 2009

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS specification. Chemistry entered incubation on April 30th, 2009.


There are currently no issues requiring board or Incubator PMC attention.


Community



- David Caruana has been voted in as committer and member of the PPMC.

Software



- David Caruana offered contribution of Client Test Harness

Licensing and other issues



- None at the moment.

Issues before graduation:



- Stabilize the general interest and energy into a sustainable development community

- Make sure that all licensing details conform with Apache policies

- Create an Apache release of the Chemistry codebase


June 2009

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS specification. Chemistry entered incubation on April 30th, 2009.


The incubation process has started well. All the project infrastructure is in place and all initial committers have their Apache accounts. We even increased the headcount of the initial team as David Caruana joined the project as a new committer.


Development of the Chemistry codebase has moved to Apache svn and there's been a number or related discussions on the mailing list. Overall the project is still in a startup phase as people are getting oriented with the scope and structure of the project. A number of license headers were updated to match Apache policies.


Issues before graduation:



- Stabilize the general interest and energy into a sustainable development community

- Make sure that all licensing details conform with Apache policies

- Create an Apache release of the Chemistry codebase


May 2009

Apache Chemistry is an effort to provide a Java (and possibly others, like JavaScript) implementation of the upcoming CMIS specification. Chemistry entered incubation on April 30th, 2009.


The Chemistry project has just entered incubation and we've been busy getting started with everything. Most of the project infrastructure is already in place, all the CLAs have been received, and the initial codebases are now in Apache svn.


Many Chemistry developers had a chance to meet in person in the CMIS PlugFest at the end of April, and the resulting energy has been visible also on the new Chemistry mailing lists. Among the results are updates to the core Chemistry codebase, a new JavaScript-based CMIS client codebase, and a proposal to contribute a Flex/Air -based CMIS explorer.


Issues before graduation:



- Stabilize the general interest and energy into a sustainable development community

- Make sure that license headers and other details conform with Apache policies

- Create an Apache release of the Chemistry codebase

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2009-04-30 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| 2009-04-30 | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| 2009-04-30 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2009-04-30 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2009-04-30 | Subscribe all Mentors on the pmc and general lists. |
| 2009-04-30 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2009-04-30 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-04-30 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2009-08-16 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2010-09-17 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2010-09-17 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2009-08-16 | Check that all active committers have submitted a contributors agreement. |
| 2009-08-16 | Add all active committers in the STATUS file. |
| 2009-08-16 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2009-04-30 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2009-04-30 | Ask infrastructure to set up and archive Mailing lists. |
| 2009-04-30 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2009-08-16 | Migrate the project to our infrastructure. |

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
