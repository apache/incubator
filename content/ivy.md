Title: Ivy Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

The Apache Ivy project has completed incubation, more information is available from the Ant website.


<span class="graduated">The Ivy project graduated on 2007-10-11</span>


Ivy is a tool for managing (recording, tracking, resolving and reporting) project dependencies. It is characterized by the following:


1. flexibility and configurability - Ivy is essentially process agnostic and is not tied to any methodology or structure. Instead it provides the necessary flexibility and configurability to be adapted to a broad range of dependency management and build processes.


2. tight integration with Apache Ant - while available as a standalone tool, Ivy works particularly well with Apache Ant providing a number of powerful Ant tasks ranging from dependency resolution to dependency reporting and publication.



- 2007-10-11 Ivy graduated as a subproject of Ant

- 2007-10-08 Ant accepted Ivy as a subproject once graduated

- 2007-09-26 The Ivy community voted to graduate as a subproject of Ant

- 2007-04-26 Ivy 2.0.0-alpha1-incubating Released

- 2007-01-05 Web site created

- 2006-11-07 Software grant received by the ASF

- 2006-10-23 Project proposal [announced](http://marc.theaimsgroup.com/?l=incubator-general&amp;m=116163023627073&amp;w=2) publicly.

| Item | Type | Reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/ivy/](http://incubator.apache.org/ivy/)  |
| Website | wiki |  [http://wiki.apache.org/ivy/](http://wiki.apache.org/ivy/)  |
| Mailing list | private (for the members of the ppmc) |  [ivy-private@incubator.apache.org](mailto:ivy-private@incubator.apache.org)  |
| Mailing list | dev |  [ivy-dev@incubator.apache.org](mailto:ivy-dev@incubator.apache.org) [ [Subscribe](mailto:ivy-dev-subscribe@incubator.apache.org) | [Unsubscribe](mailto:ivy-dev-unsubscribe@incubator.apache.org) ] |
| Mailing list | user |  [ivy-user@incubator.apache.org](mailto:ivy-user@incubator.apache.org) [ [Subscribe](mailto:ivy-user-subscribe@incubator.apache.org) | [Unsubscribe](mailto:ivy-user-unsubscribe@incubator.apache.org) ] |
| Mailing list | commits |  [ivy-commits@incubator.apache.org](mailto:ivy-commits@incubator.apache.org) [ [Subscribe](mailto:ivy-commits-subscribe@incubator.apache.org) | [Unsubscribe](mailto:ivy-commits-unsubscribe@incubator.apache.org) ] |
| Bug tracking | JIRA |  [https://issues.apache.org/jira/browse/IVY](https://issues.apache.org/jira/browse/IVY)  |
| Source code | svn |  [https://svn.apache.org/repos/asf/incubator/ivy/](https://svn.apache.org/repos/asf/incubator/ivy/)  |




| Role | Apache Id | Name (Given Surname) |
|------|-----------|----------------------|
| Champion | antoine | Antoine Levy-Lambert |
| Champion | sylvain | Sylvain Wallez |
| Mentor | antoine | Antoine Levy-Lambert |
| Mentor | sbailliez | Stephane Bailliez |
| Mentor | stevel | Steve Loughran |
| Mentor | bodewig | Stefan Bodewig |
| Committer | xavier | Xavier Hanin |
| Committer | maartenc | Maarten Coene |
| Committer | gscokart | Gilles Scokart |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache. **DONE.** 


## Interim responsibility {#Interim+responsibility}

| Date | Item |
|------|------|
| 2006-10-26 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2006-10-26 | Subscribe all Mentors on the pmc and general lists. |
| 2006-10-26 | Give all Mentors access to all incubator SVN modules. (to be done by PMC chair) |
| 2006-10-26 | Tell Mentors to track progress in the file 'incubator/projects/ivy.html' which is generated from the XML status file. |

## Copyright {#Copyright}

| Date | Item |
|------|------|
| 2006-11-22 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2007-04-20 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| Date | Item |
|------|------|
| 2007-04-20 | Check and make sure that for all code included with the distribution that is not under the Apache license have the right to combine with Apache-licensed code and redistribute. |
| 2007-04-20 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| Date | Item |
|------|------|
| 2006-11-22 | Check that all active committers have submitted a contributors agreement. |
| 2006-11-27 | Add all active committers in the STATUS file. |
| 2006-11-22 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| Date | Item |
|------|------|
| 2006-11-09 | Create source repository modules and grant the committers karma. **Done.**  |
| 2006-10-31 | Ask infrastructure to set up and archive Mailing lists. **Done.**  |
| 2006-10-31 | Ask infrastructure to setup an issue tracking system (Jira). **Done.**  |
| 2006-12-08 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?<br></br> **Yes** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)<br></br> **Ivy started with two committers and added the most active contributor rather quickly. The three of them work for different entities. Upon graduation all Ant committers will become Ivy committers as well since Ant uses a single ACL for all subprojects.** <br></br> **Yes** 

- Are project decisions being made in public by the committers?<br></br> **Yes** 

- Are the decision-making guidelines published and agreed to by all of the committers?<br></br> **Yes** 

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?<br></br> **Yes** 

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?<br></br> **Yes** 

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?<br></br> **Yes** 
