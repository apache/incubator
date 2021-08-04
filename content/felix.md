Title: Felix Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Felix project graduated on 2007-04-01</span>


The Felix Project has graduated from the Incubator at the Apache Software Project and is an implementation of the OSGi R4 specification.



- March 2007 - Felix graduated from the Incubator.


- Main site: http://incubator.apache.org/felix/


- Wiki site: http://cwiki.apache.org/FELIX/


- Status: http://incubator.apache.org/projects/felix.html

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Mailing list | dev | felix-dev@incubator.apache.org |
| Bug tracking | Jira | http://issues.apache.org/jira/browse/Felix |
| Source code | Subversion | https://svn.apache.org/repos/asf/incubator/felix |
| Mentors | akarasulu | Alex Karasulu |
| . | upayavira | Upayavira |
| Committers | akarasulu | Alex Karasulu |
| . | bloritsch | Berin Loritsch |
| . | cziegeler | Carsten Ziegeler |
| . | demuru | Matteo Demuru |
| . | erodriguez | Enrique Rodriguez |
| . | furfari | Francesco Furfari |
| . | humberto | Humberto Cervantes |
| . | lenzi | Stefano Lenzi |
| . | marrs | Marcel Offermans |
| . | noel | Noel Bergman |
| . | pauls | Karl Pauls |
| . | rickhall | Richard Hall |
| . | sylvain | Sylvain Wallez |
| . | tbennett | Timothy Bennett |
| . | trustin | Trustin Lee |
| . | walkerr | Rob Walker |
| . | sfrenot | Stephane Frenot |
| . | donsez | Didier Donsez |
| . | santillan | Manuel Santillan |
| . | jlruiz | Jose L. Ruiz |
| . | jcduenas | Juan C. Duenas |
| . | fmeschbe | Felix Meschberger |
| Extra | . | . |


-  [Q4 2005](http://wiki.apache.org/incubator/IncubatorBoardReport2005Q4) 

-  [Q1 2006](http://wiki.apache.org/incubator/IncubatorBoardReport2006Q1) 

-  [April 2006](http://wiki.apache.org/incubator/April2006) 

-  [July 2006](http://wiki.apache.org/incubator/July2006) 

-  [October 2006](http://wiki.apache.org/incubator/October2006) 

-  [January 2007](http://wiki.apache.org/incubator/January2007) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2005-08-08 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.
 _After the name 'Felix' was proposed for the project, and before we actually voted on it, a search on the US PTO for "Felix" was done. That search produced about 50 hits of live trademarks. As far as could be determined, only one was definitely related to computers (clusters). Further research from showed that the owning company (MPI software technology) was acquired by another company and no references on the new combined website could be found regarding "Felix". References (message ID's on the oscar-dev mailing list):

- &lt;200508081556.33891.niclas@hedhman.org&gt;

- &lt;200508090231.58289.niclas@hedhman.org&gt;
_ 

 |
| n/a | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| n/a | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| 2005-07-19 | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2006-02-17 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2006-02-17 | Subscribe all Mentors on the pmc and general lists. |
| 2006-02-17 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2006-05-04 | Tell Mentors to track progress in the file 'incubator/projects/felix.xml' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2006-05-04 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2006-06-06 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2006-06-01 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. _For the source code, we have made sure that every file has an ASL license. On the private mailing list there was a long thread about "Status page" which eventually led to a message (message id: &lt;487a994c0606010455q6ff8caf3g3e451c9e79817f42@mail.gmail.com&gt;) confirming that all sources were checked and contain the ASL copyright message._  |
| 2006-07-10 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. _See table below for complete list of dependencies with their licenses._  |

| Library | Version | License |
|---------|---------|---------|
| org.apache.maven maven-plugin-api | 2.0 | ASL |
| org.apache.maven maven-archiver | 2.0 | ASL |
| org.apache.maven maven-artifact | 2.0 | ASL |
| org.apache.directory.daemon daemon-bootstrappers | 1.0-RC2-SNAPSHOT | ASL |
| org.codehaus.plexus plexus-utils | 1.1 | ASL |
| org.slf4j nlog4j | 1.2.19 | SLF4J license, claims to be compatible with ASL |
| commons-daemon commons-daemon | 1.0.1 | ASL |
| kxml2 kxml2 | 2.2.2 | BSD |
| junit junit | 3.8.2 | CPL |
| tomcat servlet | 4.0.6 | APL |
| xerces xercesImpl | 2.4.0 | ASL |
| org-cybergarage cyberlink-upnp-patched | 1.7.0 | BSD |
| easymock easymock | 1.2_Java1.3 | MIT |
| jetty org.mortbay.jetty-jdk1.2 | 4.2.25 | Jetty License, derived from Artistic License |
| asm | 2.2.1 | INRIA, France Telecom License, http://asm.objectweb.org/license.html |
| BND | 0.0.106 | ASL, http://www.aqute.biz/Code/Bnd |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2006-05-04 | Check that all active committers have submitted a contributors agreement. |
| 2006-05-04 | Add all active committers in the STATUS file. |
| &lt;2006-05-04 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| 2005-07-19 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2005-07-18 | Ask infrastructure to set up and archive Mailing lists. |
| &lt;2006-05-04 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| &lt;2006-05-04 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

 _No project specific tasks._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?<br></br> **yes** 

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)<br></br> **yes** 

- Are project decisions being made in public by the committers?<br></br> **yes** 

- Are the decision-making guidelines published and agreed to by all of the committers?<br></br> **yes:**  [http://cwiki.apache.org/FELIX/felix-community-roles-and-processes.html](http://cwiki.apache.org/FELIX/felix-community-roles-and-processes.html) 

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?<br></br> **yes** 

## Project Specific {#Project+Specific}

None.


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
