Title: Incubation Status Template
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The DirectMemory project graduated on 2012-08-15</span>


DirectMemory's main purpose is to to act as a second level cache able to store large amounts of data without filling up the Java heap and thus avoiding long garbage collection cycles.



- 2011-10-05 Project enters incubation.

| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/directmemory](http://incubator.apache.org/directmemory/)  |
| . | wiki |  [http://wiki.apache.org/directmemory/](http://wiki.apache.org/directmemory/)  |
| Mailing list | dev |  `directmemory-dev`  `@`  `incubator.apache.org`  |
| . | user |  `directmemory-user`  `@`  `incubator.apache.org`  |
| . | commits |  `directmemory-commits`  `@`  `incubator.apache.org`  |
| Bug tracking | JIRA | https://issues.apache.org/jira/browse/DIRECTMEMORY |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/directmemory/](https://svn.apache.org/repos/asf/incubator/directmemory/)  |
| Mentors | antelder | Anthony Elder |
| . | olamy | Olivier Lamy |
| . | sylvain | Sylvain Wallez |
| . | twilliams | Tim Williams |
| Committers | Ioannis Canellos | iocanel |
| . | Maurizio Cucchiara | mcucchiara |
| . | grobmeier | Christian Grobmeier |
| . | Olivier Lamy | olamy |
| . | Raffaele P. Guidi | raffaeleguidi |
| . | Simone Gianni | simoneg |
| . | Simone Tripodi | simonetripodi |
| . | Tommaso Teofili | tommaso |
| . | Benoit Perroud | bperroud |


-  [January 2012](http://wiki.apache.org/incubator/January2012) 

-  [December 2011](http://wiki.apache.org/incubator/December2011) 

-  [November 2011](http://wiki.apache.org/incubator/November2011) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| ....-..-.. | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| n/a | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| Done. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| Done. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| Done. | Ask infrastructure to create source repository modules and grant the committers karma. |
| Done. | [simonetripodi] - Ask infrastructure to set up and archive mailing lists. Done - [INFRA-3999](https://issues.apache.org/jira/browse/INFRA-3999)  |
| Done. | [simonetripodi] - Ask infrastructure to set up issue tracker (JIRA, Bugzilla). In flight, [INFRA-4001](http://issues.apache.org/jira/browse/INFRA-4001)  |
| 2011-10-06 | [simonetripodi] - Ask infrastructure to set up wiki (Confluence, Moin). [INFRA-4003](http://issues.apache.org/jira/browse/INFRA-4003) . Wiki created [here.](http://wiki.apache.org/directmemory/)  |
| Done. | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| Done. | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| Done. | Subscribe all Mentors on the pmc and general lists. |
| 2011-10-07 | [twilliams] - Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file). Done. |
| 2011-10-05 | [grobmeier] - Tell Mentors to track progress in the file 'incubator/projects/directmemory.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2011-10-07 | [twilliams] - Check that all active committers have submitted a contributors agreement. Verified. |
| 2011-10-07 | [twilliams] - Add all active committers in the STATUS file. Done. |
| 2011-10-07 | [twilliams] - Ask root for the creation of committers' accounts on people.apache.org. Created, thanks root! |

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
