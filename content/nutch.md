Title: Nutch Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

On 2005-06-01, the Nutch project has been voted in by the Lucene PMC to become part of the Lucene project.


<span class="graduated">The Nutch project graduated on 2005-06-01</span>


Nutch is web search software. It builds on the Apache Lucene search library, adding a crawler, web database (including full link graph), plugins for various document formats, user interface, etc. It is currently used by sites such as [The Creative Commons](http://search.creativecommons.org/) , [Oregon State University](http://oregonstate.edu/) , and The Internet Archive.



- Project Website: [http://www.nutch.org/](http://www.nutch.org/) 


- Project Mailing Lists: [http://incubator.apache.org/nutch/mailing_lists.html](http://incubator.apache.org/nutch/mailing_lists.html) 

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/nutch/](http://incubator.apache.org/nutch/)  |
|  | wiki | http://wiki.apache.org/nutch/ |
| Mailing list | dev | nutch-dev@incubator.apache.org |
|  | commits | nutch-commits@incubator.apache.org |
|  | user | nutch-user@incubator.apache.org |
|  | agent | nutch-agent@incubator.apache.org |
|  |  | nutch-general@incubator.apache.org |
| Bug tracking | Jira |  [http://issues.apache.org/jira/](http://issues.apache.org/jira)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/nutch](https://svn.apache.org/repos/asf/incubator/nutch)  |
| Mentors | cutting | Doug Cutting |
|  | ehatcher | Erik Hatcher |
| Committers | cutting | Doug Cutting |
|  | cafarella | Michael Cafarella |
|  | abial | Andrzej Bialecki |
|  | johnx | John Xing |
|  | ziren | Sami Siren |


- none yet

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| status | item |
|---------|-------|
| DONE | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| DONE | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| DONE | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| DONE | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| status | item |
|---------|-------|
| DONE | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| DONE | Subscribe all Mentors on the pmc and general lists. |
| DONE | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| DONE | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| status | item |
|---------|-------|
| DONE | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| DONE | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| status | item |
|---------|-------|
| DONE | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| DONE | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| status | item |
|---------|-------|
| DONE | Check that all active committers have submitted a contributors agreement. |
| DONE | Add all active committers in the STATUS file. |
| DONE | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| status | item |
|---------|-------|
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

Yes. All existing committers have migrated to Apache.



- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

Yes. Nutch has five committers. No two committers share an employer. Yahoo! at times contracts with two of the five committers (Mike &amp; Doug) to work on Nutch.



- Are project decisions being made in public by the committers?

Yes. Project discussions are on public mailing lists.



- Are the decision-making guidelines published and agreed to by all of the committers?

Yes. Committers are using Apache decision-making guidelines.

<div style="margin-left: 2em">
### Licensing awareness


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?
</div>
Yes. Several Nutch plugins were disabled when Nutch entered incubation, since they required libraries with incompatible licenses. Nearly all of these have since been re-written and re-enabled. Two plugins remain disabled (parse-mp3 and parse-rtf) but these are not critical. Through this process, all comitters have become familiar with the legal issues related to Apache software.

<div style="margin-left: 2em">
### Project Specific

 _Add project specific tasks here._ 

<h2>Exit</h2>
 _Things to check for before voting the project out._ 


### Organizational acceptance of responsibility for the project


- If graduating to an existing PMC, has the PMC voted to accept it?

Yes. It has on 2005-06-01.


### Incubator sign-off


- Has the Incubator decided that the project has accomplished all of the above tasks?

Yes. It has on 2005-06-01.

</div>