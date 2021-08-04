Title: WADI Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The WADI project retired on 2005-12-05</span>


Achieving software infrastructure scalability is a tenet of Return on Investment (ROI) for any IT infrastructure and usually takes place in two forms: vertical scalability and horizontal scalability. Vertical addresses the scalability within the software itself whereas horizontal deals with it from the amount of hardware that can be utilized. Clustering, load balancing and failover is a necessity for any application server to be taken seriously in the enterprise in terms of scalability. Without the ability to cluster the application server, vertical scalability cannot take place. Without such vertical scalability, applications built on top of it can only be scaled horizontally. In order to make Geronimo more enterprise ready, it needs to provide such vertical scalability.


WADI is a clustering, load balancing and failover solution for the web application container tier. It currently supports both Jetty and Tomcat and plans are currently afoot to add full J2EE clustering functionality. WADI will help Geronimo to achieve vertical scalability.



- [none yet]

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/wadi](http://incubator.apache.org/wadi)  |
| WADI WIKI | wiki |  [http://wiki.apache.org/wadi/](http://wiki.apache.org/wadi/) <br></br> |
| Mailing List | dev | wadi-dev@incubator.apache.org |
| commits | SCM | wadi-commits@incubator.apache.org |
| Project Management Committe | PMC | wadi-ppmc@incubator.apache.org |
| User Mailing List | user | wadi-user@incubator.apache.org |
| Bug tracking | JIRA<br></br> | http://issues.apache.org/jira/browse/WADI<br></br> |
| Source code | svn<br></br> | incubator/wadi<br></br> |
| Mentor | <br></br> | Geir Magnusson Jr.<br></br> |
| Mentor | <br></br> | James Strachan<br></br> |
| Committers<br></br> | <br></br> | Bill Dudeny<br></br> |
| <br></br> | <br></br> | Bruce Snyder<br></br> |
| <br></br> | <br></br> | Jan Bartel<br></br> |
| <br></br> | <br></br> | Greg Wilkins<br></br> |
| <br></br> | <br></br> | James Strachan<br></br> |
| <br></br> | <br></br> | Jeff Genender<br></br> |
| <br></br> | <br></br> | Jules Gosnell<br></br> |
| <br></br> | <br></br> | Gianni Scenini<br></br> |
| <br></br> | <br></br> | James Goodwill<br></br> |


- [none yet]

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated&amp;#xD; {#Identify+the+project+to+be+incubated%26%23xD%3B}

| date | item |
|-------|-------|
| ....-..-.. | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the SVN module and mail address names. |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| ....-..-.. | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
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
