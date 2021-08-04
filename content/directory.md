Title: directory


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The Directory project graduated on 2005-02-23</span>


The Directory Project is an attempt to centralize all naming and directory needs in one place at the ASF. This incubator project is language independent with the current components:



- Apache Directory Server: an embeddable LDAP server written in Java

- Kerberos: a Kerberos server 'module' for the directory server

- Networking: a combination of networking code based on SEDA and ACE

- LDAP: common client and server code for LDAP

- AuthX: Authentication, Authorization and Accounting Framework

- Naming: set of core functionality common to all JNDI providers

- ASN1: Codecs for ASN.1


- ApacheDS 0.8 and Naming 0.8 Released!

- Kerberos server plugin added using common ASN.1 basis and snapping into the directory server's network layer

- More committers on board, Trustin, Enrique, and Berin

- Community is growing very rapidly with a good user community following especially after the 0.8 releases

- All IP issues vetted in code base

- All trademark issues with project names resolved

- Voting for Incubator Exit

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://incubator.apache.org/directory/](http://incubator.apache.org/directory/)  |
| . | wiki |  [http://wiki.apache.org/directory](http://wiki.apache.org/directory)  |
| Mailing list | dev | directory-dev@incubator.apache.org |
| . | cvs | directory-cvs@apache.org |
| Bug tracking | . |  [http://issues.apache.org/jira/secure/BrowseProject.jspa?id=10400](http://issues.apache.org/jira/secure/BrowseProject.jspa?id=10400)  |
| Source code | SVN | incubator-directory |
| Mentors | noel | Noel Bergman |
| . | nicolaken | Nicola Ken Barozzi |
| Committers | . |  [http://incubator.apache.org/directory/community/who/index.html](http://incubator.apache.org/directory/community/who/index.html)  |
| . | noel | Noel Bergman |
| . | nicolaken | Nicola Ken Barozzi |
| . | erodriguez | Enrique Rodriguez |
| . | jmachols | Jeff Machols |
| . | akarasulu | Alex Karasulu |
| . | trustin | Trustin Lee |
| . | psteitz | Phil Steitz |
| . | brett | Brett Porter |
| . | bayard | Henri Yandell |
| . | wesmckean | Wes McKean |
| . | rpenoyer | Rob Penoyer |
| . | bloritsch | Berin Loritsch |
| . | adc | Alan Cabrera |
| . | mcconnell | Stephan McConnell |
| . | niclas | Niclas Hedman |
| . | vtence | Vincent Tence |
| Extra | . | . |

# 2005-02-07 {#2005-02-07}

```
1). Is the STATUS file up to date? Yes 2). Any legal, cross-project
or personal issues that still need to be addressed? * All IP issues
in the code have been resolved. * All trademark issues with project
names have been resolved. 3). What has been done for incubation since
the last report? * Prepared to exit incubator this month: ran survay
- ready to kick off vote * Released 0.8 ApacheDS and Naming from
incubator * Significantly grew the community with more committers and
users * Gump integration completed with usual hickups 4). Plans and
expectations for the next period? * Graduate the incubator * Handle
infrastructure setup to get us situated 5). Any recommendations for
how incubation could run more smoothly for you? None. All is well.

```

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2003-12-01 | The requested project name does not already exist. No software trademarks exist for the names Eve, Janus or Snickers. |
| 2003-12-01 | The request was made to become a stand-alone PMC and the assessment was made to wrt the fit with the ASF. It was accepted that the directory project upon graduating the incubator would become a TLP. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2003-12-01 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| 2003-12-01 | Subscribe all Mentors on the pmc and general lists. |
| 2003-12-01 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2003-12-01 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2005-02-07 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2005-02-07 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2005-02-07 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| 2005-02-07 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2005-02-07 | Check that all active committers have submitted a contributors agreement. |
| 2005-02-07 | Add all active committers in the STATUS file. |
| COMPLETED | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| COMPLETED | Ask infrastructure to create source repository modules and add thecommitters to the avail file. |
| COMPLETED | Ask infrastructure to set up and archive Mailing lists. |
| COMPLETED | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| COMPLETED | Migrate the project to our infrastructure. |

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
