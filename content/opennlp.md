Title: Apache OpenNLP Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

The Apache OpenNLP project completed incubation on 2012-02-15. Please go to the main project site:


 [http://opennlp.apache.org/](http://opennlp.apache.org/) 


This page was used to track the project status, incubator-wise. This page is of historical interest only.


<span class="graduated">The OpenNLP project graduated on 2012-02-15</span>


The OpenNLP is a machine learning based toolkit for the processing of natural language text. It supports the most common NLP tasks, such as tokenization, sentence segmentation, part-of-speech tagging, named entity extraction, chunking, parsing, and coreference resolution. These tasks are usually required to build more advanced text processing services. The goal of the OpenNLP project will be to create a mature toolkit for the above mentioned tasks. An additional goal is to provide a large number of pre-built models for a variety of languages, as well as the annotated text resources that those models are derived from.



- 2010-11-23 Project enters incubation

- 2011-11-29 Apache OpenNLP 1.5.2 Incubating released

- 2011-12-16 We have a new committer: Boris Galitsky

- 2011-12-16 We have a new committer: Aliaksandr Autayeu

- 2011-02-15 We have graduated from the incubator as a Top Level Project

Basic information about the Apache OpenNLP podling follows:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://opennlp.apache.org](http://opennlp.apache.org/)  |
| . | wiki |  [http://cwiki.apache.org/OPENNLP/](http://cwiki.apache.org/OPENNLP/)  |
| Mailing list | dev |  `dev`  `@`  `opennlp.apache.org`  |
| . | users |  `users`  `@`  `opennlp.apache.org`  |
| . | commits |  `commits`  `@`  `opennlp.apache.org`  |
| Bug tracking | . |  [http://issues.apache.org/jira/browse/OPENNLP](http://issues.apache.org/jira/browse/OPENNLP)  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/opennlp/](http://svn.apache.org/repos/asf/opennlp/)  |
| Mentors | gsingers | Grant Ingersoll |
| . | bimargulies | Benson Margulies |
| . | isabel | Isabel Drost |
| Committers | . | . |
| . | gsingers | Grant Ingersoll |
| . | twgoetz | Thilo Goetz |
| . | joern | Jörn Kottmann |
| . | jbaldrid | Jason Baldridge |
| . | jkosin | James Kosin |
| . | tsmorton | Thomas Morton |
| . | colen | William Silva |
| . | bgalitsky | Boris Galitsky |
| . | autayeu | Aliaksandr Autayeu |
| Extra | . | . |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2010-12-02 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| October 2010 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2010-11 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2010-11 | Ask infrastructure to set up and archive mailing lists. |
| 2010-11 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2010-11 | Ask infrastructure to set up wiki (Confluence, Moin). |
| 2010-11 | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| 2010-11 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2010-11 | Subscribe all Mentors on the pmc and general lists. |
| 2010-12-2 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2010-12-2 | Tell Mentors to track progress in the file 'incubator/projects/opennlp.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| N/A | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2010-11 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2011-03 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-03 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2010-01-27 | Check that all active committers have submitted a contributors agreement. |
| 2011-08-10 | Add all active committers in the STATUS file. |
| 2010-01-various dates | Ask root for the creation of committers' accounts on people.apache.org. |

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
