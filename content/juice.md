Title: juice


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The JuiCE project retired on 2007-10-18</span>


JuiCE is an implementation of a JCE provider based on OpenSSL.



- 2007-10-18 JuiCE is going into Retired Status due to lack of community interest.


- link to the main website

- link to the page(s) that tell how to participate (Website,Mailing lists,Bug tracking,Source code)

- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://xml.apache.org/security/](http://xml.apache.org/security/)  |
| . | wiki | . |
| Mailing list | dev | juice-dev@xml.apache.org |
| . | svn | juice-cvs@xml.apache.org |
| Bug tracking | Jira |  [http://issues.apache.org/jira/browse/JUICE](http://issues.apache.org/jira/browse/JUICE)  |
| Source code | SVN | xml/juice |
| Mentors | id1 | Berin Lautenbach |
| Committers | wassa | Walter Hoehn &lt;wassa@memphis.edu&gt; |
| . | nlevitt | Noah Levitt &lt;nlevitt@columbia.edu&gt; |
| . | kwouters | Karel Wouters &lt;Karel.Wouters@esat.kuleuven.ac.be&gt; |
| . | amattheu | Axl Mattheus &lt;Axl.Mattheus@Sun.COM&gt; |
| . | vdkoogh | Erwin van der Koogh &lt;vdkoogh@apache.org&gt; |
| . | blautenb | Berin Lautenbach &lt;berin@wingsofhermes.org&gt; |
| . | dims | Davanum Srinivas (dims@yahoo.com) |
| . | werner | Werner Dittman (werner.dittman@t-online.de) |
| Extra | . | . |

# 2004-04-20 {#2004-04-20}

```
Status report for JuiCE for the Incubator JuiCE is just entering
incubation, and is currently in the process of starting up. We are
currently waiting on CLAs from core developers to enable us to get
started. * is the STATUS file up to date? (also post link) Yes -
http://incubator.apache.org/projects/juice.html * any legal,
cross-project or personal issues that still need to be addressed? No.
* what has been done for incubation since the last report? JuiCE has
only just entered the Incubator. We are currently in the process of
getting infrastructure up and running, accounts set up and code
imported. * plans and expectations for the next period? Getting code
imported, web site setup and development started.

```

 **April 2006** 


Good activity in the previous quarter. Werner Dittman was voted in as a committer and has been refactoring the initial code into a more long term format. A test build has also been created on a Win32 platform.


The team involved in this are all committers on the xml-security project. Over the next quarter we will be looking to promote this from the Incubator into the xml project as a part of xml-security.


# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-04-02 | Project name is used by some other open source software products, but none of them in the cryptography space. These projects were approached and indicated no problems with us using the name JuiCE. |
| 2004-04-02 | Project has been accepted by the XML projects, and will use xml based names - i.e. juice-dev@xml.apache.org and SVN /xml/juice |

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2004-04-02 | Mentor identified as Berin Lautenbach |
| 2004-04-02 | Berin subscribed on pmc and juice-dev lists |
| 2004-04-02 | Mentor already subscribed to incubator CVS modules |
| 2004-04-19 | Mentor tracking status in 'incubator/projects/juice.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2004-04-02 | Software grant has been received for NativeJCE (the original code base) from Internet2. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|-------|-------|
| 2005-04-27 | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| 2005-04-27 | Ask root for the creation of committers' accounts on cvs.apache.org. |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|-------|-------|
| 2004-04-18 | SVN repository set up, with access to all developers with submitted CLAs. |
| 2004-04-02 | All mailing lists set up and archived. |
| 2004-04-09 | Jira project tracking setup. |
| 2004-04-09 | Migrate the project to our infrastructure. |

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
