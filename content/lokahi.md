Title: Lokahi Project Incubation Status

<div class="section">
This page tracks the project status, incubator-wise. For broader project information, review the project website [http://incubator.apache.org/lokahi/](http://incubator.apache.org/lokahi/) .


<span class="retired">The Lokahi project retired on 2009-08-16</span>

</div><div class="section">
The Apache Lokahi project presents a web based modular framework written in Java to manage both Apache HTTP Server and Apache Tomcat, scaling to both horizontal and vertical buildout of these services across an enterprise.


The project originated as TMCg2 at Merck, and was donated to the ASF to benefit the broader Apache HTTP Server and Apache Tomcat communities. The name Lokahi (Loh-kah-hee) was chosen as it is the Hawaiian word for "harmony and unity"; one primary goal of the project is to invite ASF technologies to participate in a harmonious configuration framework, unifying configuration and deployment of our projects.

</div><div class="section">

- Aug 16 2000; Incubator PMC decided to retire the project as inactive.

- Oct 2 2006; Milestone 1 released.

- Mar 1 2005; the project has just begun provisioning resources.

- See more news in Incubation Work Items section below.
</div><div class="section">
| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/lokahi/](http://incubator.apache.org/lokahi/)  |
| . | wiki |  [http://wiki.apache.org/lokahi/](http://wiki.apache.org/lokahi/)  |
| Mailing Lists | dev |  `lokahi-dev`  `incubator.apache.org`  |
| . | commits |  `lokahi-commits`  `incubator.apache.org`  |
| . | private |  `lokahi-private`  `incubator.apache.org`  |
| Bug tracking | jira |  [http://issues.apache.org/jira/browse/lokahi](http://issues.apache.org/jira/browse/lokahi)  |
| Source Code | svn |  [http://svn.apache.org/repos/asf/incubator/lokahi/](http://svn.apache.org/repos/asf/incubator/lokahi/)  |
| Sponsor | incubator | Incubator PMC |
| Mentors | wrowe | William A. Rowe, Jr. |
| . | yoavs | Yoav Shapira |
| . | stoddard | Bill Stoddard |
| Committers | neils | Neil Stein |
| . | toback | Steve Toback |
| . | kailass | Kailas Simha |
</div>

-  [November 2006](http://wiki.apache.org/incubator/November2006) : Top items to resolve before graduation, MySQL support.

-  [August 2006](http://wiki.apache.org/incubator/August2006) : Preparing for a first milestone release.

-  [May 2006](http://wiki.apache.org/incubator/May2006) : After a fairly active April, May was a bit slower.

-  [April 2006](http://wiki.apache.org/incubator/April2006) : The Lokahi project is still setting up its infrastructure: Subversion has been set up with proper commit privileges, and the initial code import just took place a couple of days ago. The Lokahi name has been cleared as far as trademark usage goes.

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated&amp;#xD; {#Identify+the+project+to+be+incubated%26%23xD%3B}

| date | item |
|------|------|
| 2005-12-06 | Submit propsal to general(at)incubator to consider for adoption as a new ASF project.<br></br>Message ID: &lt;FF5CC930B20F6047A645F97065DFED00CB09CE@usctmx1110.merck.com&gt; |
<td>2006-01-07</td><td>Tally votes to accepted project into incubator;<br></br>+1: mads, jerenkrantz, jimjag, wrowe, geirm<br></br>0: [none]<br></br>-1: [none]</td>| 2006-02-17 | Make sure that the requested project name does not already exist or is trademarked for an existing software product.<br></br>Reservations about TMCg2 inspired a name change, initial choice of Ohana proved troublesome with trademarks.<br></br>Final name, Lokahi acceptable to all. Checked google.com, verified Echo did not adopt, checked uspto.gov's TESS database, no apparent conflicts (wrowe). |
| 2006-03-17 | Establish SVN repository layout and commit privileges. (wrowe). |
| 2006-04-16 | Bill Stoddard joined the project as a mentor. |
| [WIP] | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module name. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|---------------------|---------------------|
| February 2006 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| February 2006 | Subscribe all Mentors on the pmc and general lists. |
| March 2006 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/lokahi.html' |

## Copyright {#Copyright}

| date | item |
|---------------------|---------------------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|---------------------|---------------------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|---------------------|---------------------|
| 2006-02-17 | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|---------------------|---------------------|
| ....-..-.. | Ask infrastructure to create source repository modules and grant the committers karma. |
| ....-..-.. | Ask infrastructure to set up and archive Mailing lists. |
| ....-..-.. | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| ....-..-.. | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _Put together a list of things to do and publish it on the project site._ 


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
