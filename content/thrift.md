Title: Apache Thrift Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Thrift project graduated on 2010-10-20</span>


Thrift is cross-language serialization and RPC framework. It combines a powerful software stack with a code generation engine to build services that work efficiently and seamlessly between C++, Java, Python, PHP, Ruby, C#, Erlang, Perl, and several other languages. Thrift was originally developed at Facebook and open-sourced in April, 2007. Thrift entered the Apache Incubator in May, 2008.



- 2010-10-20 Thrift Graduates to a [Top Level Project](http://thrift.apache.org/) 

- 2010-08-04 Thrift 0.3 released

- 2008-05 Project enters incubation.


-  [Thrift ASF Project Official Website](http://incubator.apache.org/thrift/) 


- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Official Website | www |  [http://incubator.apache.org/thrift/](http://incubator.apache.org/thrift/)  |
| . | wiki |  [http://wiki.apache.org/thrift/](http://wiki.apache.org/thrift/)  |
| Developers Mailing List | dev |  [thrift-dev@incubator.apache.org](mailto:thrift-dev-subscribe@incubator.apache.org)  |
| Commits Mailing List | commits |  [thrift-commits@incubator.apache.org](mailto:thrift-commits-subscribe@incubator.apache.org)  |
| User Mailing List | user |  [thrift-user@incubator.apache.org](mailto:thrift-user-subscribe@incubator.apache.org)  |
| Bug tracking | Jira |  [http://issues.apache.org/jira/browse/thrift](http://issues.apache.org/jira/browse/thrift)  |
| Source code | svn |  [http://svn.apache.org/repos/asf/incubator/thrift/](http://svn.apache.org/repos/asf/incubator/thrift/)  |
| Mentors | cutting | Doug Cutting (Champion) |
| . | upayavira | Upayavira |
| Committers | aditya | Aditya Agarwal |
| . | kclark | Kevin Clark |
| . | bryanduxbury | Bryan Duxbury (PPMC) |
| . | esteve | Esteve Fernandez (PPMC) |
| . | marck | Marc Kwiatkowski |
| . | todd | Todd Lipcon |
| . | jake | Jake Luciani (PPMC) |
| . | bmaurer | Ben Maurer (PPMC) |
| . | geechorama | Andrew McGeachie |
| . | cpiro | Chris Piro |
| . | dreiss | David Reiss (PPMC) |
| . | mcslee | Mark Slee (PPMC) |
| . | jwang | James Wang (PPMC) |
| . | molinaro | Anthony Molinaro |


-  [July 2010](http://wiki.apache.org/incubator/July2010) 

- April 2010 Not Submitted

-  [January 2010](http://wiki.apache.org/incubator/January2010) 

-  [October 2009](http://wiki.apache.org/incubator/October2009) 

-  [July 2009](http://wiki.apache.org/incubator/July2009) 

-  [April 2009](http://wiki.apache.org/incubator/April2009) 

-  [January 2009](http://wiki.apache.org/incubator/January2009) 

-  [October 2008](http://wiki.apache.org/incubator/October2008) 

-  [July 2008](http://wiki.apache.org/incubator/July2008) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2007-10-23 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2008-01-12 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2008-01-12 | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-11-10 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2009-04-07<br></br>[ [THRIFT-387](https://issues.apache.org/jira/browse/THRIFT-387) ] | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2009-12-07<br></br>[ [THRIFT-622](https://issues.apache.org/jira/browse/THRIFT-622) ] | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2009-12-07<br></br>[ [THRIFT-622](https://issues.apache.org/jira/browse/THRIFT-622) ] | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

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
