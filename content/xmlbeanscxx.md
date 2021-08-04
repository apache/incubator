Title: Apache XML Beans C++ Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>
<div class="section">
This page tracks the incubation status of the Apache XML Beans C++ project.


<span class="retired">The XMLBeans/C++ project retired in 2007-05-16</span>

</div><div class="section">
The Apache XML Beans C++ project will produce a C++ equivalent to Apache's XMLBeans project for Java.


XMLBeans provides the developer with an 'object' representation of structured XML data conforming to Schema language. Additionally, XMLBeans enables the developer to handle XML documents directly, achieving increased performance and flexibility in a single framework. The C++ version will provide a similar user experience to the popular Java version, but will be optimized to take advantage of the powerful, high-performance features of C++.

</div><div class="section">

- 2005-06-06 Project accepted by the Web services PMC.

- 2005-05-15 Project proposed on general@incubator mailing.

- 2005-02-09 xmlbeanscxx [project page](http://incubator.apache.org/xmlbeanscxx) and [status page](http://incubator.apache.org/projects/xmlbeanscxx.html) committed to subversion.
</div><div class="section">
| item | id | reference |
|------|----|-----------|
| Web site | www |  [http://incubator.apache.org/xmlbeanscxx/](http://incubator.apache.org/xmlbeanscxx/)  |
|  | wiki |  [http://wiki.apache.org/xmlbeanscxx/](http://wiki.apache.org/xmlbeanscxx/)  |
| Mailing lists | dev |  [cxx-dev@xmlbeans.apache.org](mailto:cxx-dev@xmlbeans.apache.org)  |
|  | svn |  [cxx-commits@xmlbeans.apache.org](mailto:cxx-commits@xmlbeans.apache.org)  |
|  | ppmc |  [TBD](mailto:)  |
| Moderators | abrookes |  [Allen Brookes](mailto:abrookes_at_apache.org)  |
|  | dhaney |  [David Haney](mailto:dhaney_at_apache.org)  |
| Bug tracking | TBD |  [TBD]()  |
| Source code | svn |  []( )  |
| Sponsor |  |  [Incubator PMC](mailto:pmc_at_incubator.apache.org)  |
| Mentors | Cliff Schmidt |  [Cliff Schmidt](mailto:) (See this [post](http://www.mail-archive.com/general@incubator.apache.org/msg04836.html) .) |
| Committers | abrookes |  [Allen Brookes](mailto:abrookes_at_roguewave_dot_com)  |
| hbuelow |  [Heidi Buelow](mailto:heidi.buelow_at_apache.org)  |
|  | dhaney |  [David Haney](mailto:dhaney_at_apache.org)  |
|  | myoder |  [Michael Yoder](mailto:yoder_at_roguewave.com)  |
|  | ttriemstra |  [Tim Triemstral](mailto:ttriemstra_at_apache_dot_org)  |
|  |  |  [TBD](mailto:tbd)  |

Committers in _italics_ do not have a signed [Contributor License Agreement](http://incubator.apache.org/forms/ASF_Contributor_License_2_form.pdf) on file.

</div><div class="section">
| file | note |
|------|------|
| TBD | TBD |
</div>



# Project Setup {#Project+Setup}




## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| TBD | Make sure that the requested project name does not already exist and check [NameProtect](http://www.nameprotect.com) to be sure that the name is not already trademarked for an existing software product. |
| N/A | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| N/A | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| N/A | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| TBD | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| TBD | Subscribe all Mentors on the pmc and general lists. |
| TBD | Give all Mentors access to all incubator SVN modules (to be done by PMC chair). |
| TBD | Tell Mentors to track progress in the status file. |

## Copyright {#Copyright}

| date | item |
|------|------|
| TBD | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| TBD | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| TBD | Check and make sure that for all code included with the distribution that is not under the Apache license, has the right to combine with Apache-licensed code and redistribute. |
| TBD | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| TBD | Check that all active committers have submitted a contributors agreement (see the list of [committers](#committers) above for any exceptions). |
| TBD | Add all active committers to the status page. |
| TBD | Ask root to create committers' accounts on cvs.apache.org ( [INFRA-440](http://issues.apache.org/jira/browse/INFRA-440) ). |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| TBD | Ask infrastructure to create source repository modules and grant the committers karma ( [INFRA-441](http://issues.apache.org/jira/browse/INFRA-441) ). |
| TBD | Ask infrastructure to set up and archive mailing lists ( [INFRA-339](http://issues.apache.org/jira/browse/INFRA-339) ). |
| TBD | Decide about and then ask infrastructure to setup an issue tracking system ( [INFRA-438](http://issues.apache.org/jira/browse/INFRA-438) ). |
| TBD | Migrate the project to our infrastructure. |

## Project-specific {#Project-specific}

| date | item |
|------|------|
| TBD | Publish a [page](http://incubator.apache.org/xmlbeanscxx/bugs.html) on how to file issues against the project and how to submit patches ( [XMLBEANSCXX-9](http://issues.apache.org/jira/browse/XMLBEANSCXX-9) ). |
| TBD | Improve the [project page](http://incubator.apache.org/xmlbeanscxx/) ( [XMLBEANSCXX-6](http://issues.apache.org/jira/browse/XMLBEANSCXX-6) ). |
| TBD | Make the [Class Reference](http://svn.apache.org/repos/asf/incubator/xmlbeanscxx/trunk/doc/stdlibref/) and [Users Guide](http://svn.apache.org/repos/asf/incubator/xmlbeanscxx/trunk/doc/stdlibug/) available online, from the project page ( [XMLBEANSCXX-12](http://issues.apache.org/jira/browse/XMLBEANSCXX-12) ). |
| TBD | Make a tarball of stable project sources available for download from the project site. |
| TBD | Document the design and development practices and publish them on the project site. |
| TBD | Put together a list of things to do and publish it on the project site. |
| TBD | Check in the test driver. |
| TBD | Check in the project test suite. |

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

## Project-specific {#Project-specific-N10439}

 _No project-specific tasks._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
