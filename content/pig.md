Title: Pig Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

Pig is a platform for analyzing large data sets that consists of a high-level language for expressing data analysis programs, coupled with infrastructure for evaluating these programs. The salient property of Pig programs is that their structure is amenable to substantial parallelization, which in turns enables them to handle very large data sets.


Pig has **graduated as a Hadoop subproject** , see Message-ID: &lt;f767f0600810171144w3aaff127p65766a0a2a1a9662@mail.gmail.com&gt; on general@incubator.apache.org


<span class="graduated">The Pig project graduated on 2008-10-22</span>


 **Pig** is a platform for analyzing large data sets that consists of a high-level language for expressing data analysis programs, coupled with infrastructure for evaluating these programs. The salient property of Pig programs is that their structure is amenable to substantial parallelization, which in turns enables them to handle very large data sets.


At the present time, Pig's infrastructure layer consists of a compiler that produces sequences of Map-Reduce programs, for which large-scale parallel implementations already exist (e.g., the Hadoop subproject). Pig's language layer currently consists of a textual language called Pig Latin, which has the following key properties:



-  **Ease of programming.** It is trivial to achieve parallel execution of simple, "embarrassingly parallel" data analysis tasks. Complex tasks comprised of multiple interrelated data transformations are explicitly encoded as data flow sequences, making them easy to write, understand, and maintain.

-  **Optimization opportunities.** The way in which tasks are encoded permits the system to optimize their execution automatically, allowing the user to focus on semantics rather than efficiency.

-  **Extensibility.** Users can create their own functions to do special-purpose processing.


- October 22, 2008: Pig has graduated as a Hadoop subproject.

- September 2008: Daniel Dai voted in as a Pig committer

- September 2008: Pig 0.1.0 released

- June 2008: Pi Song voted in as a Pig committer

- October 2007: [Pig formally accepted into Apache Incubator](http://www.mail-archive.com/general@incubator.apache.org/msg15348.html) 


-  [Pig website](http://incubator.apache.org/pig/) 

-  [Pig committers and mentors](http://incubator.apache.org/pig/whoweare.html) 

-  [Pig wiki](http://wiki.apache.org/pig/) 


-  [June 2008](http://wiki.apache.org/incubator/June2008) 

-  [September 2008](http://wiki.apache.org/incubator/September2008) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| October 2007 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| Existing project (Lucene) pre-approved Fall 2007 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |

 **DONE** 


## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| October 2007 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| November 2007 | Subscribe all Mentors on the pmc and general lists. |
| November 2007 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| November 2007 (re-done June 2008) | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.xml' |

 **DONE** 


## Copyright {#Copyright}

| date | item |
|------|------|
| Not applicable (I think) | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| Not applicble (new project) | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| August 2008 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| August 2008 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

 **DONE** 


## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| October 2007 (and ongoing) | Check that all active committers have submitted a contributors agreement. |
| September 2008 | Add all active committers in the STATUS file. |
| September 2008 | Ask root for the creation of committers' accounts on people.apache.org. |

 **DONE** 


Active Committers Are


| Committer | Email Address |
|-------------|-----------------|
| Daniel Dai | daijyc@gmail.com |
| Nigel Daley | nigel@apache.org |
| Alan Gates | gates@yahoo-inc.com |
| Olga Natkovich | olgan@yahoo-inc.com |
| Owen O'Malley | omalley@apache.org |
| Chris Olston | olston@yahoo-inc.com |
| Ben Reed | breed@yahoo-inc.com |
| Pi Song | pi.songs@gmail.com |
| Utkarsh Srivastava | utkarsh@yahoo-inc.com |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| October 2007 | Ask infrastructure to create source repository modules and grant the committers karma. |
| October 2007 | Ask infrastructure to set up and archive Mailing lists. |
| October 2007 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| Not applicable (project starts in Apache) | Migrate the project to our infrastructure. |

 **DONE** 


## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project? **Yes** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.) **Yes** 

- Are project decisions being made in public by the committers? **Yes** 

- Are the decision-making guidelines published and agreed to by all of the committers? **Yes** 

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers? **Yes** 

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
