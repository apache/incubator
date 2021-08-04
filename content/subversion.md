Title: Subversion Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise.


<span class="graduated">The Subversion project graduated on 2010-02-17</span>


Subversion is an open-source version control system, with a [long and detailed list of features](http://subversion.tigris.org/features.html) .



- 2009-11-07 Project enters incubation.

 [Subversion](http://subversion.tigris.org/) is an open source project; we welcome [patches](http://subversion.tigris.org/hacking.html#patches) , and we'll help you get more [involved](http://www.red-bean.com/svnproject/contribulyzer/) if you want to be.



- 
Read the [Introduction to Subversion Development](http://subversion.tigris.org/development.html) .



- 
Read the [Hacker's Guide to Subversion](http://subversion.tigris.org/hacking.html) .



- 
Maybe browse the [API documentation](http://svn.collab.net/svn-doxygen/) .



- 
 [Browse the source tree](http://svn.collab.net/viewvc/svn/trunk/) with ViewVC.



- 
Check out the source tree:<br></br> `svn checkout http://svn.collab.net/repos/svn/trunk/` 



- 
Hack!



The following table shows the location of the main incubation resources.


| item | type | reference |
|------|------|-----------|
| Website | www |  [subversion.apache.org](http://subversion.apache.org/)  |
| Mailing list | dev |  `dev`  `@`  `subversion.apache.org`  |
|  | commits |  `commits`  `@`  `subversion.apache.org`  |
|  | private (PPMC) |  `private`  `@`  `subversion.apache.org`  |
| Bug tracking |  _see [Infrastructure section](#Infrastructure) _  |  |
| Source code | SVN |  [http://svn.apache.org/repos/asf/subversion/](http://svn.apache.org/repos/asf/subversion/)  |
| Mentors | gstein | Greg Stein |
|  | jerenkrantz | Justin Erenkrantz |
|  | dlr | Daniel Rall |
|  | striker | Sander Striker |
| Committers | bhuvan | Bhuvaneswaran A |
|  | blair | Blair Zajac |
|  | brane | Branko Čibej |
|  | cmpilato | C. Michael Pilato |
|  | danielsh | Daniel Shahaf |
|  | dlr | Daniel Rall |
|  | dongsheng | Dongsheng Song |
|  | ehu | E W H Huelsmann |
|  | fabien | Fabien Coelho |
|  | fitz | Brian Fitzpatrick |
|  | ghudson | Greg Hudson |
|  | glasser | David Samuel Glasser |
|  | gstein | Greg Stein |
|  | hwright | Hyrum Kurt Wright |
|  | ivan | Ivan Zhakov |
|  | jerenkrantz | Justin Erenkrantz |
|  | joeswatosh | Joe Swatosh |
|  | jorton | Joe Orton |
|  | josander | Jostein Chr Andersen |
|  | jrepenning | Jack Repenning |
|  | julianfoad | Julian Foad |
|  | jwhitlock | Jeremy Whitlock |
|  | kameshj | Kamesh J |
|  | kfogel | Karl Fogel |
|  | kmradke | Kevin Radke |
|  | larrys | Larry Shatzer Jr |
|  | lgo | Lieven Govaerts |
|  | markphip | Mark Phippard |
|  | martinto | Martin Tomes |
|  | mattiase | Mattias Engdegard |
|  | maxb | Max Oliver Bowsher |
|  | mbk | Mark Benedetto King |
|  | mf | Martin Furter |
|  | pburba | Paul Burba |
|  | peters | Peter Samuelson |
|  | philip | Philip Martin |
|  | pmarek | Philipp Marek |
|  | pmayweg | Patrick Mayweg |
|  | rgupta | Raman Gupta |
|  | rhuijben | Bert Huiben |
|  | rooneg | Garrett Rooney |
|  | sbutler | Stephen O'Neil Butler |
|  | steveking | Stefan Küng |
|  | striker | Sander Striker |
|  | stsp | Stefan Sperling |
|  | stylesen | Senthil Kumaran S |
|  | sussman | Ben Collins-Sussman |
|  | wein | Mathias Weinert |
|  | wsanchez | Wilfredo Sánchez |


-  [December 2009](http://wiki.apache.org/incubator/December2009#Subversion) 

-  [January 2010](http://wiki.apache.org/incubator/January2010#Subversion) 

-  [February 2010](http://wiki.apache.org/incubator/February2010#Subversion) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2009-11-07 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2009-12-.. |  **NOTE: the mailing lists and the svn repository were set up in their final locations.** <br></br>If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2009-11-07 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2009-11-12 | Subscribe all Mentors on the pmc and general lists. |
| 2009-11-13 | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| 2009-11-13 | Tell Mentors to track progress in the file 'incubator/projects/subversion.xml' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2009-11-13 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2009-12-.. |  **NOTE: the RAT tool is being used for this.** <br></br>Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2009-12-.. |  **NOTE: the RAT tool is being used for this.** <br></br>Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2009-12-.. |  **NOTE: the RAT tool is being used for this.** <br></br>Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2009-11-13 | Check that all active committers have submitted a contributors agreement. |
| 2009-11-13 | Add all active committers in the STATUS file. |
| 2009-11-13 | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2009-11-13 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2009-11-12 | Ask infrastructure to set up and archive Mailing lists. |
| 2009-12-.. |  **NOTE: decided, but not (yet) set up. We still need to figure out our migration plan from the old tracker to the new (Bugzilla).** <br></br>Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2009-12-.. | Migrate the project to our infrastructure. |

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
