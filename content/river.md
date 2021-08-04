Title: Apache River
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The River project graduated on 2011-01-19</span>


The River Project is a Jini technology implementation community.



- 2011-01-19: Project graduated into a TLP

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/river/](http://incubator.apache.org/river/)  |
| Mailing list | dev |  `river-dev`  `@`  `incubator.apache.org`  |
|  | user |  `river-user`  `@`  `incubator.apache.org`  |
|  | commits |  `river-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | jira |  [https://issues.apache.org/jira/browse/RIVER](https://issues.apache.org/jira/browse/RIVER)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/incubator/river/](http://svn.apache.org/repos/asf/incubator/river/)  |
| Mentors | niclas | Niclas Hedhman |
|  | jukka | Jukka Zitting |
|  | bimargulies | Benson Margulies |
| Former Mentors | gianugo | Gianugo Rabellino |
|  | geirm | Geir Magnusson Jr |
|  | psteitz | Phil Steitz |
| Committers | bvenners | Bill Venners |
|  | marbro | Mark Brouwer |
|  | waldo | Jim Waldo |
|  | pdp8 | John McClain |
|  | btmurphy | Brian Murphy |
|  | peter_jones | Peter Jones |
|  | fbarnaby | Frank Barnaby |
|  | resendes | Robert Resendes |
|  | vinod | Vinod Johnson |
|  | rjmann | Ron Mann |
|  | jhurley | Jim Hurley |
|  | jcosters | Jonathan Costers |
|  | peter_firmstone | Peter Firmstone |
|  | thobbs | Tom Hobbs |
|  | sijskes | Sim IJskes |
|  | pats | Patricia Shanahan |
| Emeriti | rscheifler | Bob Scheifler |
|  | dancres | Dan Creswell |
|  | foliver | Fred Oliver |
|  | geirm | Geir Magnusson Jr |
|  | nigel | Nigel Daley |
|  | psteitz | Phil Steitz |
|  | ramirjf | Juan Ramirez |

# March 2007

River is aimed at the development and advancement of the Jini technology core infrastructure. Jini technology is a service oriented architecture that defines a programming model which both exploits and extends Java technology to enable the construction of secure, distributed systems which are adaptive to change.



- Apache River incubator project proposal approved on Dec 26, 2006

- Basic project structures created (mailing lists, web pages, jira, wiki, etc)

- Much and varied discussions on direction and particulars on the river-dev list

- ServiceUI contribution submitted and waiting PPMC formation and vote.

Next steps include:



- complete requirements and setup of initial committer list and PPMC

- hold PPMC vote to accept ServiceUI contribution

- Sun to submit Starter Kit contribution

- hold PPMC vote to accept contribution

- finalize jira categories and migrate pre-existing Sun bug reports

- come to agreement on initial set of work leading to first Apache River release

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2006-12-26 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2006-12-26 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2006-12-26 | Subscribe all Mentors on the pmc and general lists. |
| 2007-05-16 | Give all Mentors access to the incubator SVN repository. (to be done by PMC chair) |
| 2006-12-26 | Tell Mentors to track progress in the file 'incubator/projects/river.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2010-12-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2010-12-07 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2010-12-07 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2010-12-07 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2007-05-15 | Check that all active committers have submitted a contributors agreement. |
| 2007-05-15 | Add all active committers in the STATUS file. |
| 2007-05-15 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2007-05-15 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2007-05-15 | Ask infrastructure to set up and archive Mailing lists. |
| 2007-05-15 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2010-12-07 | Migrate the project to our infrastructure. |

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
