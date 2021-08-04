Title: Apache JDO Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status related to incubation. For more general project status, look on the project website.


<span class="graduated">The JDO project graduated on 2005-12-09</span>


The Apache JDO Project plan is to migrate the existing JDO 1.0 code base, including the API, RI, and TCK to Apache. Subsequently, development on JDO 2.0 will commence, using the JDO 1.0 code as a starting point. The API and TCK will be implemented entirely as Apache sub-projects. The licenses will be changed to be Apache licenses.<br></br>


If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/jdo/](http://incubator.apache.org/jdo/)  |
| . | wiki |  [http://wiki.apache.org/jdo/](http://wiki.apache.org/jdo/) <br></br> |
| Mailing list | dev | jdo-dev@db.apache.org |
| . | svn | jdo-commits@db.apache.org |
| Bug tracking | JIRA<br></br> | http://issues.apache.org/jira/browse/JDO<br></br> |
| Source code | svn<br></br> | incubator/jdo<br></br> |
| Mentors | <br></br> | Geir Magnusson Jr.<br></br> |
| Committers<br></br> | <br></br> | Craig Russell<br></br> |
| <br></br> | <br></br> | Dain Sundstrom<br></br> |
| <br></br> | <br></br> | Erik Bengston<br></br> |
| <br></br> | <br></br> | Geir Magnusson Jr.<br></br> |
| <br></br> | <br></br> | Brian McCallister<br></br> |
| <br></br> | <br></br> | Michael Bouschen<br></br> |
| <br></br> | <br></br> | Martin Zaun<br></br> |
| <br></br> | <br></br> | Matthew Adams<br></br> |
| <br></br> | <br></br> | Michael Watzek<br></br> |
| <br></br> | <br></br> | Michelle Caisse<br></br> |
| <br></br> | <br></br> | Patrick Linskey<br></br> |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-12-02 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A<br></br> | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| 2004-12-02<br></br> | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-12-06 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2005-01-05<br></br> | Subscribe all Mentors on the pmc and general lists. |
| 2005-01-05<br></br> | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2005-01-05<br></br> | Tell Mentors to track progress in the file 'site-author/projects/jdo.html' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2005-03-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-12-10 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2004-12-10 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2004-12-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2005-03-16 | Check that all active committers have submitted a contributors agreement. |
| 2005-03-16 | Add all active committers in the STATUS file. |
| 2005-03-16 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| 2005-01-03<br></br> | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2005-01-03<br></br> | Ask infrastructure to set up and archive Mailing lists. |
| 2005-01-03<br></br> | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2005-03-18<br></br> | Migrate the project to our infrastructure. |

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

## Licensing awareness  {#Licensing+awareness%C2%A0}


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
