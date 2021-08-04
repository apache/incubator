Title: Solr Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

<span class="graduated">The Solr project graduated on 2007-01-17</span>


Solr is a search server focused on full-text search, relevancy, and performance. It builds on the Apache Lucene search library, adding features such as



- Query and update interfaces over HTTP and XML or JSON.

- Hit Highlighting

- Faceted Search

- Replication based on index snapshots and rsync.

- A schema allowing declarative specification of fields and their types, including specification of text analysis filter chains.

- External configuration for Lucene parameters, stopword lists, and synonym lists.

- A web based admin interface with statistics and debugging.

- An extensive caching framework for filters, queries, documents, and user caches.

- Plugins for customizing query handling, caching and many other server aspects.
<br></br><br></br>

- See [Solr's Website](http://incubator.apache.org/solr/) for more news

- 2007-01-17: Solr graduates from Incubator to become a Lucene sub-project!

- 2006-12-22: Solr 1.1.0 Released

- 2006-11-11: Solr PPMC votes in a new committer, Bertrand Delacretaz!

- 2006-08-14: Solr PPMC votes in a new committer, Mike Klaas!

- 2006-01-17: Incubator accepts Solr

- 2006-01-03: Lucene votes to sponsor Solr


- Project Website: [http://incubator.apache.org/solr/](http://incubator.apache.org/solr/) 

- Project Mailing Lists: [http://incubator.apache.org/solr/mailing_lists.html](http://incubator.apache.org/solr/mailing_lists.html) 

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/solr](http://incubator.apache.org/solr)  |
| Wiki | wiki |  [http://wiki.apache.org/solr](http://wiki.apache.org/solr)  |
| Mailing list | dev | solr-dev@lucene.apache.org |
|  | user | solr-user@lucene.apache.org |
|  | commits | solr-commits@lucene.apache.org |
| Bug tracking | Jira |  [http://issues.apache.org/jira/browse/SOLR](http://issues.apache.org/jira/browse/SOLR)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/solr/](https://svn.apache.org/repos/asf/incubator/solr/)  |
| Mentors | cutting | Doug Cutting |
|  | ehatcher | Erik Hatcher |
|  | ianh | Ian Holsman (retired) |
| Committers | yonik | Yonik Seeley |
|  | billa | Bill Au |
|  | hossman | Chris Hostetter |
|  | yoavs | Yoav Shapira |
|  | cutting | Doug Cutting |
|  | otis | Otis Gospodnetic |
|  | ehatcher | Erik Hatcher |
|  | klaas | Mike Klaas |
|  | bdelacretaz | Bertrand Delacretaz |


-  [April2006](http://wiki.apache.org/incubator/April2006) 

-  [August2006](http://wiki.apache.org/incubator/August2006) 

-  [November2006](http://wiki.apache.org/incubator/November2006) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| DONE | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| DONE | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| DONE | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| DONE | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| DONE | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| DONE | Subscribe all Mentors on the pmc and general lists. |
| DONE | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| DONE | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| DONE | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| DONE | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| DONE 4/18/06 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| DONE | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| DONE | Check that all active committers have submitted a contributors agreement. |
| DONE | Add all active committers in the STATUS file. |
| DONE | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| DONE | Ask infrastructure to create source repository modules and grant the committers karma. |
| DONE | Ask infrastructure to set up and archive Mailing lists. |
| DONE | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| DONE | Migrate the project to our infrastructure. |

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


- If graduating to an existing PMC, has the PMC voted to accept it? YES

- If graduating to a new PMC, has the board voted to accept it? N/A

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks? YES
