Title: xmlbeans


---------------------------------------------------------------------- ---------


 **NOTE: XMLBeans has graduated from Incubation** - please see [http://xml.apache.org/xmlbeans/](http://xml.apache.org/xmlbeans/) 


---------------------------------------------------------------------- ---------


<span class="graduated">The XMLBeans project graduated on 2004-06-23</span>



- create STATUS file in incubator-cvs

- create mailing lists

- create xml-xmlbeans CVS


- configure viewcvs

- commit mails -&gt; xml-xmlbeans-cvs@apache.org

- setup xmlbeans bugzilla

- Complete License Grant agreement

- Have all committers sign CLA's


- Cezar Andrei

- David Bau

- Patrick Calahan

- Ken Kress

- Laurence Moroney

- David Remy

- Dutta Satadip

- Cliff Schmidt

- Eric Vasilik

- David Waite

- Scott Ziegler

- Relicense XML beans files with ASL 2.0


- add ASF copyright to all files

- move all packages to org.apache.xmlbeans

- eliminate all non ASL code and library dependencies

- mailing list tasks


- lists-archived:


- mbox -&gt; xml.apache.org/mail

- Eyebrowse setup

- setup xmlbeans wiki area and refactor pages to there

- set up to sign builds


- committer PGP keys

- committer keys signed by someone in ASF (probably twl)

- build xmlbeans website

- grant some comitters access to xml-site

- Define incubation exit criteria

- configure build to match ASF style

- setup mirroring of builds

---------------------------------------------------------------------- ---------


# Identify the project to be incubated: XMLBeans {#Identify+the+project+to+be+incubated%3A+XMLBeans}

X- Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.


X- If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names.


xml-xmlbeans


xmlbeans-dev@xml.apache.org xmlbeans-user@xml.apache.org xmlbeans-cvs@xml.apache.org


X- If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance.


X- If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted.


# Interim responsibility: {#Interim+responsibility%3A}

X- Who has been identified as the shepherd for the incubation?


Ted Leung &lt;twl@apache.org&gt;


X- Are they tracking progress in the file


incubator:site/projects/xmlbeans.cwiki


# Copyright: {#Copyright%3A}

X- Have the papers that transfer rights to the ASF been received? It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.


X- Have the files been updated to reflect the new ASF copyright?


# Verify distribution rights: {#Verify+distribution+rights%3A}

X- For all code included with the distribution that is not under the Apache license, do we have the right to combine with Apache-licensed code and redistribute?


X- Is all source code distributed by the project covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms?


# Establish a list of active committers: {#Establish+a+list+of+active+committers%3A}

X- Are all active committers in the STATUS file?


X- Do they have accounts on cvs.apache.org?


X- Have they submitted a contributors agreement?


# Infrastructure: {#Infrastructure%3A}

X- CVS modules created and committers added to avail file?


X- Mailing lists set up and archived?


X- Problem tracking system (Jira)?


X- Has the project migrated to our infrastructure?


# Collaborative Development: {#Collaborative+Development%3A}

X- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?


X- Are there three or more independent committers?


X- Are project decisions being made in public by the committers?


X- Are the decision-making guidelines published and agreed to by all of the committers?


# Organizational acceptance of responsibility for the project: {#Organizational+acceptance+of+responsibility+for+the+project%3A}

N/A If graduating to an existing PMC, has the PMC voted to accept it?


X- If graduating to a new PMC, has the board voted to accept it?


# Incubator sign-off: {#Incubator+sign-off%3A}

X- Has the Incubator decided that the project has accomplished all of the above tasks?


# 2004-04-20 {#2004-04-20}

```
- Status report for the Incubator - Changes since last report in
January: * Added Dutta Satadip as a committer * Released
incubating-xmlbeans-1.0.2 after a thorough legal review ** after
review of license issues: added jaxen to distribution, removed junit,
noted W3C XML Schemas ** applied Apache License 2.0 * Formed a PPMC;
set up mailing list and designed guidelines * Moved from bugzilla to
JIRA. * Set up new wiki pages. Expectations for next three months: *
Find two more committers * Release one more distribution * Improve
web site (faq, current info, etc) * Exit incubator

```

# 2004-01-17 {#2004-01-17}

```
- Status report for the Incubator - Overall the xmlbeans project is
progressing with good committer productivity and a growing user
community. Converting over the Apache CVS systems and build process
has been accomplished along with various other Apache administrative
tasks such as setting up the Apache website. There is some movement
towards growth in the development side of the community with one
contributor (Dutta Satadip) submitting a nice enhancement and several
other contributors submitting small patches related to bugs. More on
each of the bullet points below. * is the STATUS file up to date?
(also post link) &lt;Cliff Schmidt&gt; We need to update the status file
with the latest incubator guidelines. We're mostly there, but there
are a couple things that need to be added. I also think the status
file needs to be updated in one or two other ways. For instance, the
tasks completed should now include: - build xmlbeans website - grant
some committers access to xml-site (Cliff and Remy) &lt;/Cliff Schmidt&gt;
http://incubator.apache.org/projects/xmlbeans.html * any legal,
cross-project or personal issues that still need to be addressed? In
general it appears xmlbeans is through most of the known issues that
existed getting started. The committers have been able to be
productive and there is a lot of code being created in version 2 and
fixes are being made into version 1. One issue that we have run into
is how best to accommodate commonly used api jars primarily (but not
exclusively) JCP related api's from SUN. We are not sure the
appropriate process to determine whether we can use a particular jar
and host the jar in the xmlbeans build. examples of api's that we are
unsure the appropriate/best way to deal with are: * JSR173 api and
JSR 173 RI (Streaming API for XML, a.k.a., STAX) - the JSR173 RI
dependency is temporary. Currently xmlbeans downloads it from
external server during the build process * SAAJ api - we used the
saaj-api source code in axis. * xml commons resolver (Apache jakarta)
* jaxen (jaxen.sourceforge.net - apache-style license, but not
apache) Here are some specific questions on this subject that David
Bau posted: &lt;David Bau&gt; - We currently load resolver.jar and
jaxen.jar if the user happens to put them on the classpath, and throw
a runtime exception if the user tries to use a resolver- or jaxen-
dependent feature without those JARs present. This is OK, but it
would be nicer for users if resolver and jaxen were just included in
xbean.jar, but this presents both licensing issues (for jaxen) and
possible-version-conflict issues (for commons resolver). A question
is: is there a nice way we include resolver.jar and jaxen.jar inside
xbean.jar, or should we stay away from that idea? - We need the JSR
173 API to run, and this is definitely something that we want to be
able to distribute either directly inside xbean.jar, or at least
directly inside Apache since it's so core. In other words, we can't
expect users to do anything without this API present. I've noticed
that for other APIs, such as SAAJ, Apache seems to have a "clean
room" copy of the APIs. Should we be making such a copy of the JSR
173 APIs? What is the right way to do this? &lt;/David Bau&gt; * what has
been done for incubation since the last report? &lt;David Bau&gt; The main
thing is that we've been working on the project. We're getting more
folks hanging around on the lists; we're getting some of the code
that we've talked about on the lists and on the wiki actually written
and checked in. We've been encouraging the wider community to
critique and contribute ideas and code. Community-building is a
gradual process; we don't have a mature community yet, but we've
certainly gotten started at building a little one. &lt;/David Bau&gt; *
source code checkin (was that since last status report?) * build and
test ant scripts established * website updated including docs, source
code access, etc. * established version 2 effort and modified CVS
tree accordingly * proposed (close to implementing I think) branching
strategy for version 1 (by Kevin Krouse) * gump integration (thanks
to Robert Burrell Donkin) * plans and expectations for the next
period? * development on v2 will continue incorporating community
feedback. * continued work on soliciting volunteers for contribution
and committership. * work on organizing bug tracking and follow up *
xmlbeans-1.01 distribution (minor bug fixes to v1) * improve process
of bug testing and fixing from BugZilla contributions. * any
recommendations for how incubation could run more smoothly for you?
Incubation seems to be going well with one, albeit an important one,
challenge of getting outside committers. Having a large existing
codebase in a fairly complicated area makes it challenging. The
growing user community and the excellent posts that we are getting on
the xmbleans-dev list make us optimistic we will make some
breakthroughs in the next period. * things that xmlbeans could/will
improve on (summary, contributed by Cliff Schmidt) 1. Bug management:
http://nagoya.apache.org/bugzilla/buglist.cgi?product=XMLBeans (as
has already been mentioned by one or two others) -- This is just as
much related to community as code. Of the 12 bugs entered so far, we
haven't done a very good job of keeping them updated with status. We
should encourage people to file bugs by showing that the committers
are actually responding to them (even if the response is "need more
info to repro" or simply noting the priority). 2. Web site:
http://xml.apache.org/xmlbeans/ -- We got this built and running but
we need to keep it updated. For instance, it still shows the
ApacheCon advertisement. 3. Binary download. -- We started to get
this done, but I don't think we ever finished. Actually, I'd like to
try to get this done in the next couple days. 4. PPMC -- The
incubator introduced the idea of a PPMC and we haven't responded to
this yet. I'll follow up in a separate post on what needs to be done.
5. Status file -- We need to update the status file with the latest
incubator guidelines. We're mostly there, but there are a couple
things that need to be added. I also think the status file needs to
be updated in one or two other ways. For instance, the tasks
completed should now include: - build xmlbeans website - grant some
committers access to xml-site (although I forgot who has this; I
think it is me and Remy) 6. Committer keys Bau and I were both able
to make it to ApacheCon and we both participated in the key-signing
party. We need to get other committers to make keys and get them
signed by me and Bau whenever we run into each other in person again.
7. New Committers The biggest issue of all is definitely the new
committers, as everyone seems to agree. We really need to find more
ways to encourage others to contribute. I think we are all ready and
willing to share some of the responsibility; we just need to find
people who are showing enough interest (and action) to be considered
for committership.

```
