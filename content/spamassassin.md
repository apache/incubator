Title: spamassassin


This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The SpamAssassin project graduated on 2004-06-23</span>


SpamAssassin(tm) is a mail filter to identify spam.


Using its rule base, it uses a wide range of heuristic tests on mail headers and body text to identify "spam", also known as unsolicited commercial email.



- none yet

| item | type | reference |
|-------|-------|------------|
| Website | www |  [http://spamassassin.org/](http://spamassassin.org/)  |
| . | wiki |  [http://wiki.apache.org/spamassassin/](http://wiki.apache.org/spamassassin/)  |
| Mailing list | dev | spamassassin-dev@incubator.apache.org |
| . | cvs | spamassassin-cvs@incubator.apache.org |
| . | ppmc | spamassassin-ppmc@incubator.apache.org |
| . | users | spamassassin-users@incubator.apache.org |
| . | devel-br | spamassassin-devel-br@incubator.apache.org |
| . | devel-de | spamassassin-devel-de@incubator.apache.org |
| . | announce | spamassassin-announce@lists.sourceforge.net |
| . | . | (replacement spamassassin-announce exists on incubator, but will not be used until graduation) |
| Bug tracking | . |  [http://bugzilla.spamassassin.org/](http://bugzilla.spamassassin.org/)  |
| Source code | SVN | incubator/spamassassin/ |
| Mentors | striker | Sander Striker |
| PPMC | felicity | Theo Van Dinter |
| . | jm | Justin Mason |
| . | quinlan | Daniel Quinlan |
| Committers | duncf | Duncan A. Findlay |
| . | felicity | Theo Van Dinter |
| . | jm | Justin Mason |
| . | mss | Malte Sebastian Stretz |
| . | parker | Michael Parker |
| . | quinlan | Daniel Quinlan |
| . | sidney | Sidney Markowitz |
| Extra | DNS | spamassassin.org |

# 2004-04-22 {#2004-04-22}

```
* is the Incubation Status file up to date? (also post link) Yep --
http://cvs.apache.org/viewcvs.cgi/*checkout*/incubator/site/projects/s
amassassin.cwiki * any legal, cross-project or personal issues that
still need to be addressed? Copyright and distribution rights still
remain to be verified by ASF. The trademark issue on the
"SpamAssassin" name is still in progress. * what has been done for
incubation since the last report? news.spamassassin.org has been shut
down; it was becoming just a dumping-ground for third-party press
releases, and Wiki pages were more appropriate. We're still waiting
for trademark assignment to be taken care of. Also unsure if the ASF
have vetted the CLA coverage of the current codebase. Mostly, the
ball is in the ASF's court ;) Have received agreement from current
domain holder of "spamassassin.org" that it will be transferred to
the ASF. * plans and expectations for the next period? Hopefully
we'll get the TM assignment taken care of, and the CLAs vetted; then
we'll be ready (at least in terms of ASF procedures) to issue a 3.0.0
release of SpamAssassin as an ASF project. * any recommendations for
how incubation could run more smoothly for you? * etc (your own
thoughts on what is important would be helpful!)

```

# 2004-03-?? {#2004-03-%3F%3F}

```
* STATUS is up to date
http://cvs.apache.org/viewcvs.cgi/*checkout*/incubator/site/projects/s
amassassin.cwiki is now the canonical STATUS file and it is now
up-to-date. The trunk copy points at it now. * 3.0.0 tree under
development at ASF * 2.6x not under development at ASF

```

# 2004-01-21 {#2004-01-21}

```
* is the STATUS file up to date? (also post link)
http://cvs.apache.org/viewcvs.cgi/*checkout*/incubator/site/projects/s
amassass in.cwiki Not quite -- the two 'Establish a list of active
committers' items are not up to date. All active committers are now
signed up, so that can be closed off. The second item is 'Add all
active committers in the STATUS file.' However, I'm now confused.
Which is the canonical STATUS file --
/incubator/spamassassin/trunk/STATUS, or
/incubator/site/projects/spamassassin.cwiki? Some signs seem to be
pointing to the latter... so, if the latter, some cut and paste from
the former to the latter is then required (and note, I don't think I
or anyone else on the SpamAssassin PPMC have write access to it). I'm
kind of taking the approach that the latter is the incubation
checklist, and the former is tracking our assets and people. That may
be wrong though BTW the former is here:
http://svn.apache.org/repos/asf/incubator/spamassassin/trunk/STATUS
Also, the two tasks under 'Verify distribution rights', should be
complete. All code in the trunk is covered by CLAs, and the
non-covered branches have README files noting their non-Apache status
and presence for historical purposes only. However, perhaps this may
need to be verified by the ASF before the task can be marked as
complete, I'm not sure. * any legal, cross-project or personal issues
that still need to be addressed? Copyright and distribution rights
still remain to be verified, although all CLAs should now be in. --
so it's up to ASF legal now. The trademark issue on the
"SpamAssassin" name is still in progress; as far as I know, NAI legal
still need to provide some documentation to DW, Jim Jagielski et al.
* what has been done for incubation since the last report? Lots! - -
all committer accounts are set up; - - source code is now running
from the Apache Incubator SVN repository; - - all of the
developer-oriented mailing lists are now at the Incubator - although
some user-oriented lists are still external, to avoid user confusion;
- - all code has been vetted for CLA coverage, and removed or
clean-roomed if a CLA could not be provided, and this is now awaiting
verification by the ASF; - - and all major code or rules files in SVN
are tagged with the ASL 1.1. - - The Wiki has been moved to
wiki.apache.org. * plans and expectations for the next period? We
need to transition more infrastructure, including our main website,
Wiki and Bugzilla. Bugzilla uses some custom code to track CLAs,
which would be nice to bring over. We also plan to finish up the
legal situation, by getting the CLA coverage verified by the ASF,
then the trademark. Also we have several cron scripts that are used
to perform distributed rule QA, and a very large rsync server contain
2.7Gb of data, which will need to be migrated. What to do with these
is still a topic of discussion, since they're *big* in terms of disk
space usage, and there may not be room at the ASF infrastructure for
this! There's also a spamtrap server which almost definitely should
*not* come along -- it handles approx 1 Gbit of traffic per day (in
spam reports) and would be a waste of ASF hardware and bandwidth,
IMO. * any recommendations for how incubation could run more smoothly
for you? A little more introductory doco would be nice; I hadn't
heard of http://www.apache.org/dev/ until quite late in the process,
and there were a few other issues where I had to hop around the
apache.org website to figure out what things meant or what a given
procedure was. Also, one thing I'm concerned about is how many
aspects of our infrastructure will wind up with "incubator" in their
URL or hostname; as a mature project, it'd be much easier to
transition with the minimum of changes for the existing community,
and this scoping of URLs and hostnames as in incubation means an
additional change once we leave the incubator. As a result, it gives
us a bit of an incentive to *not* set things up (lists, etc.) until
we leave.

```

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|-------|-------|
| 2004-02-16 | Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |
| DONE | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

 _NOTE_ 


```
There is a trademark

```

## Interim responsibility {#Interim+responsibility}

| date | item |
|-------|-------|
| 2003-12-20 | Identify all the Mentors for the incubation, by asking all that can be Mentors. |
| N/A | Subscribe all Mentors on the pmc and general lists. |
| N/A | Give all Mentors access to all incubator CVS modules. (to be done by PMC chair) |
| 2003-12-29 | Tell Mentors to track progress in the file 'incubator/projects/spamassassin.cwiki' |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2004-02-16 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-02-16 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| DONE | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| DONE | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|-------|-------|
| 2004-01-21 | Check that all active committers have submitted a contributors agreement. |
| 2004-01-21 | Add all active committers in the STATUS file. |

## Infrastructure {#Infrastructure}

| date | item |
|-------|-------|
| 2003-12-23 | Ask root for the creation of committers' accounts on svn.apache.org. |
| 2004-01-07 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2003-12-25 | Ask infrastructure to set up and archive Mailing lists. |
| ....-..-.. | Decide about and then ask infrastructure to setup an issuetracking system (Bugzilla, Scarab, Jira). |
| ....-..-.. | Migrate the project to our infrastructure. |

 _NOTES_ 


```
Discussion is underway to whether SA wants to use Jira, or wants to
import their BZ database into the existing ASF installation.

```

```
The moving to the ASF infrastructure is partly delayed by the limited
resources available in the ASF Infrastructure team (time). Also, this
mature project has quite a lot of infrastructure to move. I suggest
we don't let this be one of the points to keep SA in the Incubator;
the intent to move to the ASF infrastructure is there.

```

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

Yes.



- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

Yes.



- Are project decisions being made in public by the committers?

Yes.



- Are the decision-making guidelines published and agreed to by all of the committers?

Yes.


## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

Two trademarks are being assigned to the ASF:


SpamAssassin: http://assignments.uspto.gov/assignments/q?db=tm&amp;sno=78148991


Powered by SpamAssassin: http://assignments.uspto.gov/assignments/q?db=tm&amp;sno=78213077


## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
