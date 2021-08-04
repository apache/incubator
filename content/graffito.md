Title: Graffito
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="retired">The Graffito project retired on 2007-07-11</span>


Graffito (formerly JCMS) is dedicated to build a complete CMS solution on top of existing content management frameworks (like Slide or Jackrabbit). One of the design goals of Graffito is to be easily integrated in a JSR-168 portal environment like Pluto or Jetspeed 2.




2007 April

The JCR Mapping component was transferred into the Apache Jackrabbit project.



2006 January

1 new committer joins the team (Alexandru Popescu).


Jetspeed 2 integration is almost finished. We plan to build a Graffito implementation for the Jetspeed 2 Page Manager.


Version 1.0-a1-dev is almost finished.


The JCR mapping tools support basic mapping strategies. Now, we are working on more advance strategy like inheritance,interface, ...



2005 June

Graffito is still under incubation. See on the Graffito incubation page to get more information.


2 new committers join the team (Oliver and Sandro). They are mainly focus on the JCR Mapping tools.


Version 1.0-a1-dev is on good way, some portlets are availables, see the maven report to follow the developement process.



2004 December

Graffito developement is just incubating in the ASF. The code is not 100% stable and not all Graffito features are implemented.


Obviously, you are welcome to send your comments and to contribute!


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://incubator.apache.org/graffito/](http://incubator.apache.org/graffito/)  |
| . | wiki | . |
| Mailing list | dev | graffito-dev@incubator.apache.org |
| . | svn | graffito-commits@incubator.apache.org |
| Bug tracking | jira |  [http://issues.apache.org/jira/secure/BrowseProject.jspa?id=10661](http://issues.apache.org/jira/secure/BrowseProject.jspa?id=10661)  |
| Source code | SVN |  [https://svn.apache.org/repos/asf/incubator/graffito/](https://svn.apache.org/repos/asf/incubator/graffito/)  |
| Mentors | raphael | Raphael Luta |
| . | jukka | Jukka Zitting |
| Committers | taylor | David S. Taylor |
| . | raphael | Raphael Luta |
| . | clombart | Christophe Lombart |
| . | okiessler | Oliver Kiessler |
| . | sboehme | Sandro Boehme |
| . | apopescu | Alexandru Popescu |

# April 2007 {#April 2007}

Graffito is a framework for content-based applications, especially in portlet environments. Graffito entered incubation on September 20, 2004.


Despite recent efforts the level of activity within the Graffito project remains low. The only part of the project that enjoys continued interest and commit activity is the JCR Mapping component, whose transfer into a subproject of Apache Jackrabbit is being prepared.


There is little indication that the level of activity within other parts of the Graffito project would increase in future, so we will most likely request termination of the project as retired as soon as the JCR Mapping component has been moved to Apache Jackrabbit.


# February 2007 {#February 2007}

(This is the extra followup report requested by the board last month.)


Graffito is a framework for content-based applications, especially in portlet environments. Graffito entered incubation on September 20, 2004.


The recent discussion on the status of the Graffito project has concluded with some concrete action items (see [the thread](http://mail-archives.apache.org/mod_mbox/incubator-graffito-dev/200702.mbox/%3c3b728ee90702140445i5d21bd22j95fb5b67c58abc70@mail.gmail.com%3e) ). The plan is to realign Graffito to be more a content management framework instead of a complete CMS product and to better leverage the features of JCR content repositories.


The effect of these plans on commit activity remains to be seen, but as of now the general feeling around the project is positive. Hopefully we'll have some concrete results to show by the time of the next report.


# January 2007 {#January 2007}

Graffito is a framework for content-based applications, especially in portlet environments. Graffito entered incubation on September 20, 2004.


Top three items to resolve before graduation:



1. Build a self-sustaining community

1. Create an incubating Graffito release

1. Move the JCR mapping component to the Jackrabbit project

There hasn't been much activity in the Graffito project since the last report. A discussion on what to do with the project that still hasn't reached "critical mass" after over two years of incubation is currently taking place. The perceived complexity of the project is seen by many as a barrier to start using or contributing to Graffito. Splitting the project into more manageable component projects was raised as one potential approach to reviving the codebase and project community.


# October 2006 {#October 2006}

Graffito is a framework for content-based applications, especially in portlet environments. Graffito entered incubation on September 20, 2004.


Top three items to resolve before graduation:



- Upgrade to the latest license header and copyright notice policy

- Create an incubating Graffito release

- Move the JCR mapping component to the Jackrabbit project

Graffito activity has increased noticeably since the last report, especially due to interest from within the Jackrabbit community. New bug reports and patches are also being contributed.



- Jukka Zitting was voted in as a new mentor for the project. He will accompany Raphael Luta in that role.

- Given positive feedback from both communities, we are evaluating options for moving the JCR mapping component from Graffito into the Jackrabbit project. This would expose the component to a wider JCR developer community and a larger audience of potential users.

- There has been renewed discussion on producing incubating releases of the Graffito components.

- Edgar Poce has been working on a related JCR-based wysiwyg portlet prototype, using the Graffito mailing list for design discussions, but the implementation approach differs from the Graffito portlet model, so at least for now the tool is not being integrated into Graffito

# June 2006 {#June 2006}

There was not so much commits on the project due to the current commiters activities. The company Sword Technologies donates new Graffito services (worfklow, news management , mail and scheduler services). Christophe will try to review and commit this code asap.


The Spring support is finished for the OCM Tools. Now the OCM tools will be used in the complete Graffito stack. By this way, the Graffito persistence service can access to JCR repositories.


Graffito is working with Jetspeed 2 head.


# April 2006 {#April 2006}


- We are still working on our JCR support. This support is mainly done with an object/Content mapping. We hope to finalize the first release of this subproject for the ASF Europe Conf. This tools could be use in other open source project.

- Sword Technologies is working on the workflow service and the first Graffito module (personalized news management with syndication). The code will be donate in May to the ASF.

- Still working with the Jetspeed team to see how to build a common release for the ASF Europe Conf.

- We want to promote and make some "marketing" to increase the community size.

# 2006Q1 {#2006Q1}

Graffito has nicely grown recently with activity encouraged by the final release of Jetspeed 2.0 and good progress made on the JCR support though Jackrabbit.


We've just added a new committer:



- Alexandru Popescu

and some existing Portals committers also actively contributing to the integration of Graffito with Portals.


# 2005Q4 {#2005Q4}

Lot of work underway:



- working on JCR mapping for Graffito objects

- port under way for using Graffito for storing Jetspeed page descriptions in a Graffito managed repository (effort lead by Jetspeed team)

- several new names have appeared on mailing-list and start contributing patches and join the design discussions

We plan to have a Graffito binary bundled with upcoming Jetspeed 2 M4 release (required if PSML integration is complete for M4) If community development continues its progress as expected, I think we'll add couple of new committers this quarter and probably ask for exiting Incubator early next year.


# 2005Q3 {#2005Q3}


- The main news in this quarter is that we have expanded the committer base beyond the original contributors with the addition of Oliver Kiessler and Sandro Boehme.

- Both are busily working on building support for JCR (through Jackrabbit).

- Work is also underway to use Graffito as a native CMS engine in Jetspeed 2.

# 2005-4-25 {#2005-4-25}
 `1) Is the STATUS file up to date? Yes 2) Any legal, cross-project or
personal issues that still need to be addressed? no 3) What has been
done for incubation since the last report? * The most important work
was made on the Jetspeed 2 integration &amp; building some JSR-168
portlets. There is a content tree view, a document viewer and an
admin browser portlet. Futhermore, we have integrate an HTML editor
(Kupu). * Some work has been done for the security management (fine
grain access control, permission management, JAAS support, ...). * We
have started raising awareness and promoting the project on some
other Apache and non-Apache lists in order build further the
community. * New developers have started collaborating with the core
team on Graffito work, especially JCR mapping tools. 4) Plans and
expectations for the next period? * Implementing our JCR mapping
framework with Jackrabbit. * XML editor integration. * A Graffito
implementation for the Jetspeed 2 page manager. * Continue our work
on the JSR-168 portlets (search &amp; version management). * Start a site
demo with a Jetspeed integration * We expect the committer base to
expand during next period given the current developer participation
on the dev mailing-lists. 5) Any recommendations for how incubation
could run more smoothly for you? None so far.
` 
# 2005-1-14 {#2005-1-14}
 `1) Is the STATUS file up to date? Yes 2) Any legal, cross-project or
personal issues that still need to be addressed? * Software grant has
been recieved by the ASF. * All trademark issues with project name
have been resolved. * We have renamed the JCMS project as Graffito to
avoid naming confusion with Jalios JCMS, another Java based CMS
system. 3) What has been done for incubation since the last report? *
We cleaned up repository, site, build process, site deployment and
publishing to help new users and developers jump into the project. *
Christophe Lombart account has been created and karma granted * ASF
Infrastructure has been set up for Graffito * We are working on the
Jetspeed 2 integration &amp; building JSR 168 portlets. 4) Plans and
expectations for the next period? * Add more info in the Graffito
site * WEBDAV integration * More work on Jetspeed 2 integration,
building portlets. * Introduce Graffito to some important to related
projects: Slide, JackRabbit, Jetspeed ... in order to grow the
development community 5) Any recommendations for how incubation could
run more smoothly for you? None so far. All is well.
` 
# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2004-09-20 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. (raphael) |
| ....-..-.. | If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names. |
| 2004-09-13 | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. (raphael) |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Interim responsibility {#Interim+responsibility}

| date | item |
|------|------|
| 2004-09-13 | Identify all the Mentors for the incubation, by asking all that can be Mentors. (raphael) |
| 2004-09-20 | Subscribe all Mentors on the pmc and general lists. (raphael) |
| 2004-11-06 | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) (raphael) |
| 2004-11-06 | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.cwiki' (raphael) |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2004-11-27 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. (raphael) |
| 2004-11-27 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. (raphael) |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2004-11-29 | Check and make sure that for all code included with the distribution that is not under the Apache license, e have the right to combine with Apache-licensed code and redistribute. (raphael) |
| 2004-11-29 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. (raphael) |

## Establish a list of active committers ! {#Establish+a+list+of+active+committers+%21}

| date | item |
|------|------|
| 2004-11-27 | Check that all active committers have submitted a contributors agreement. (raphael) |
| 2004-12-12 | Add all active committers in the STATUS file. (raphael) |
| 2004-12-23 | Ask root for the creation of committers' accounts on cvs.apache.org. (raphal) |

## Infrastructure ! {#Infrastructure+%21}

| date | item |
|------|------|
| 2005-01-03 | Ask infrastructure to create source repository modules and grant the committers karma. (raphael) |
| 2004-12-28 | Ask infrastructure to set up and archive Mailing lists. (raphael) |
| 2005-01-07 | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| 2005-01-08 | Migrate the project to our infrastructure. |

## Project specific {#Project+specific}

| date | item |
|------|------|
| 2004-12-27 | Renamed JCMS to Graffito to avoid naming conflict with Jalios JCMS, another Java CMS package |

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
