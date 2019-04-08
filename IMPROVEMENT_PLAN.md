
# TL/DR

1. More Whimsy UX to manage the Podling Lifecycle
2. Consolidate podling status data
3. [`podlings.xml`][0] is still master
4. Add status checklists and Incubation watchlist to the new Cookbook
5. Whimsy podling status page will include clutch analysis
6. We need to decide how to do reporting since MOIN wikis are going away.
   No recommendation is provided.

# Podling Status Process

Here is an analysis of the many ways podling status is tracked by the Incubator.
Currently there are five components to podling status.

1. Podlings XML is directory listing ever podling and its status: current, graduated or retired.
2. Podling Status Page is an XML/HTML file that has information about the podling's resource
   requirements and various checklists for the incubation process.
3. Podling YML file which was started a few years ago as a data based approach to key resource
   and incubation process completions.
4. The monthly / reporting process. This process a manual process involving the
   MOIN Wiki and a python program for creating the report template. This will need to be changed soon
   because the MOIN Wiki is being retired.
5. Clutch analysis. This process takes the information from the Podlings XML and Status Pages and
   then looks for and confirms the Website, Issue Tracker, Wiki, Code Repositories, and Release
   Distributions. 
   
What follows is a description of each of these processes. This will be followed by some
ideas about how we should proceed.

## Podlings xml

The podling catalog is in this file: [`podling.xml`][0]

Values are stored for all Incubator podlings in a single xml file each in a `podling` node.
Not all of the data pertain to current podlings.
- Podling name. This is set when the podling is created. It can be changed later but that
  can be expensive if the resources also need to be renamed.
- Status - This is one of these three values: "current", "graduated" or "retired". Podlings
  in the Incubator are current. When the podling exits it either "graduates" or "retires"
- Resource - This is the name used for resources. It is initialized to lower case of Podling name w/o spaces.
  Once the podling's resources are created it is very expensive to change these.
- ResourceAliases - If the podling's resource and name is changed the older resource names are stored in 
  this field. Some older podlings had multiple names or short names for resources.
- Sponsor - Most often this is the "incubator", but it may also be any Apache PMC if there are directly
  sponsoring a project in the incubator.
- Start date - This is the date that the podling starts incubation. It can be the date the podling entry is created
  or the date that the incubation vote passed.
- End date - This is the date the podling leaves the incubator. It is either the date that 
  the Board votes to accept the graduation proposal, the date another PMC chooses to accept the podling
  as part of their PMC, or the date the podling retires.
- Description - a short description of the podling.
- Champion - the champion for the project.
- Mentors - a list of the podling's mentors with their Apache IDs. This is now maintained from
  Whimsy. [Whimsy roster page][1]
- Reporting group - which months is a current podling reporting to the IPMC. A new podling will be monthly.
- Resolution - when the podlings leaves the Incubator it either graduates or retires. These fields
  describe what happened, 
  - tlp attribute - If "true" the podling became a TLP 
  - link attribute - If a name change was involved to the new TLP, the podling graduates into an existing PMC,
    or retires with a new location then this is the text on a link.
  - url attribute - If there is a link then this is the url.
  - description - an optional description about retirement or graduation

A current podling:
```
    <podling name="Crail" status="current" resource="crail" sponsor="Incubator" startdate="2017-11-01">
        <description>Crail is a storage platform for sharing performance critical data in distributed data processing jobs at very high speed.</description>
        <reporting group="3"/>
        <champion availid="lresende">Luciano Resende</champion>
        <mentors>
            <mentor username="jhyde">Julian Hyde</mentor>
            <mentor username="lresende">Luciano Resende</mentor>
        </mentors>
    </podling>
```

A brand new podling:
```
    <podling name="DataSketches" status="current" resource="datasketches" sponsor="Incubator" startdate="2019-03-30">
        <description>DataSketches is an open source, high-performance library of stochastic streaming algorithms commonly called "sketches" in the data sciences. Sketches are small, stateful programs that process massive data as a stream and can provide approximate answers, with mathematical guarantees, to computationally difficult queries orders-of-magnitude faster than traditional, exact methods.</description>
        <reporting group="2" monthly="true">May, June, July</reporting>
        <champion availid="jbonofre">Jean-Baptiste Onofré</champion>
        <mentors>
            <mentor username="chenliang613">Liang Chen</mentor>
            <mentor username="kenn">Kenneth Knowles</mentor>
            <mentor username="kamaci">Furkan Kamaci</mentor>
        </mentors>
    </podling>
```

A podling graduated to a TLP:
```
    <podling name="CXF" status="graduated" resource="cxf" sponsor="Incubator" startdate="2006-08-15" enddate="2008-04-16">
        <description>The CXF project will create a SOA services framework by merges the ObjectWeb Celtix project and the Codehaus XFire project.</description>
        <resolution tlp="true"/>
        <mentors>
            <mentor username="jim">Jim Jagielski</mentor>
            <mentor username="jstrachan">James Strachan</mentor>
        </mentors>
    </podling>
```

A podling sponsored by a PMC that graduated into the PMC:
```
    <podling name="Derby" status="graduated" resource="derby" sponsor="DB" startdate="2004-08-15" enddate="2005-07-18">
        <description>Java relational database</description>
        <resolution link="DB Derby" url="http://db.apache.org/derby/"/>
        <mentors>
            <mentor username="coar">Ken Coar</mentor>
        </mentors>
    </podling>
```

A podling that graduated with a name change:
```
    <podling name="OpenOffice.org" status="graduated" resource="openofficeorg" resourceAliases="ooo" sponsor="Incubator" startdate="2011-06-13" enddate="2012-10-17">
        <description>OpenOffice.org is comprised of six personal productivity applications: a word processor (and its web-authoring component), spreadsheet, presentation graphics, drawing, equation editor, and database.</description>
        <resolution link="OpenOffice" url="https://openoffice.apache.org/"/>
        <mentors>
            <mentor username="jim">Jim Jagielski</mentor>
            <mentor username="rubys">Sam Ruby</mentor>
            <mentor username="danese">Danese Cooper</mentor>
            <mentor username="curcuru">Shane Curcuru</mentor>
            <mentor username="noirin">Noirin Plunkett</mentor>
            <mentor username="joes">Joe Schaefer</mentor>
            <mentor username="grobmeier">Christian Grobmeier</mentor>
            <mentor username="rgardler">Ross Gardler</mentor>
        </mentors>
    </podling>
```

A podling that retired:
```
    <podling name="Provisionr" status="retired" resource="provisionr" sponsor="Incubator" startdate="2013-03-07" enddate="2013-11-22">
        <description>Provisionr provides a service to manage pools of virtual machines on multiple clouds.</description>
        <resolution>Failed to grow a community. Retired at request of PPMC.</resolution>
        <champion availid="tomwhite">Tom White</champion>
        <mentors>
            <mentor username="rvs">Roman Shaposhnik</mentor>
            <mentor username="tomwhite">Tom White</mentor>
            <mentor username="mnour">Mohammad Nour El-Din</mentor>
        </mentors>
    </podling>
```

A podling that retired and moved development elsewhere:
```
    <podling name="Heraldry" status="retired" resource="heraldry" sponsor="Incubator" startdate="2005-07-14" enddate="2007-06-09">
        <description>Identity for the rest of us.</description>
        <resolution link="OpenID.net" url="http://openid.net/">Project retired. Some activity moved to OpenID.net</resolution>
        <mentors>
            <mentor username="ben">Ben Laurie</mentor>
            <mentor username="pquerna">Paul Querna</mentor>
            <mentor username="twl">Ted Leung</mentor>
            <mentor username="farra">J. Aaron Farr</mentor>
            <mentor username="wrowe">William Rowe</mentor>
        </mentors>
    </podling>
```

### Current format for Podling Status Files

More information is found on the project status page in xml wrapped html.
For the most part this is descriptive text which has data embedded tagged with id attributes.
There are also very descriptive check lists.

Here is [the template for new podling status pages][2]. You can see that it is a tedious
process to copy this to add a new file for each podling.

This data is available and in some cases is extracted from these files by processes
including the Clutch Analysis.
- Description - an HTML div which minimally repeats the podling description, but may include
  additional information about the podling's original location and resources.
- News - an HTML div with a list of dated events in the history of the podling.
- Project Info - an HTML table with a description and links to podling resources requested
  from infrastructure.
  - www - Website url of the podling. It should be the website within Apache, but sometimes
    is the legacy.
  - wiki - A url to the wiki. Sometimes this is blank if a Github wiki is being used.
    Not all podlings use wikis.
  - mail-dev - The mailing list in various forms.
  - mail-commits - The commits mailing list in various forms.
  - mail-private - The private mailing list in various forms.
  - tracker - a url to the issue tracker. Sometimes this is blank if Github issues are used.
  - mentors - a set of rows which duplicate podlings.xml and are only hand maintained.
    Lately this is often shortened to point to the [Whimsy roster page][1]
  - committers - a set of rows which are hand maintained.
    Lately this is often shortened to point to the [Whimsy roster page][1]
- Status reports. A list of board reports often pointing to the while incubator report.
  This is also now easily available from the [Whimsy roster page][1]
- Work Items
  - Project setup. (very outdated instructions)
  - Infrastructure. (outdated instructions)
  - Mentor setup. (outdated instructions)
  - Copyright.
  - Distribution Rights.
  - Initial Committers. (outdated instructions)
- Incubation Items - what to watch for during incubation.
  - Collaborative Development
  - Licensing Awareness
  - Project Specific
- Exit
  - Graduating into a TLP?
  - Graduating into an existing PMC?

The status pages are sporadically maintained by a majority of podlings after bootstrap.

### The Podling YML file

In the [`podling yml file`][9] the following parameters have values:

- asfCopyright - the date that the ASF copyright has been added to the donated code.
- distributionRights - the date that the code has been properly reviewed for appropriate 
  licensing.
- graduationDate - the date of graduation.
- ipClearance - the date that the code has been properly reviewed for appropriate 
  licensing.
- issueTracker - is github or jira used for issue tracking?
- jira - if jira is used provide the URL. The url can be assumed if the jira project key
  is the `podling.resource` upper cased.
- news - a new place to put podling news records.
  - date
  - note
- proposal - the url to the podling proposal.
- sga - the date the software grant was received by the Secretary.
- sourceControl - only used once for 'github'. Every project is using github.
- website - the project website url. This is always the preferred pattern.
- wiki - the Space key for a Confluence wiki.

You can see that there is quite a bit of overlap with information from the podling status page.
This is intentional since the yml files are a replacement data store.

The key values are `asfCopyright` and `distributionRights`

### Podling Report Template

The initial report template is created by [`clutch2report.py`][10].
Look for the `perproject` variable. The values `$name` and `$description` are taken indirectly from `podlings.xml`
via the `clutch2.pkl` created by `clutch2.py`. There is much more information available that can be injected into
the template.

The podling maturity section has checkboxes which parallel some of the work items and checklists on the podling status page.

```
  [ ] Initial setup
  [ ] Working towards first release
  [ ] Community building
  [ ] Nearing graduation
  [ ] Other:
```

### Clutch Analysis

Clutch analysis is performed using the [`clutch2.sh`][11] shell script. The key programs in the process
are the [`clutch2.py`][12] python script which performs analysis pulling information from the following
resources:

1. [`podlings.xml`][0]
2. [Podling status pages][18]
2. [Apache mailbox archive][14]
3. [Gitbox Catalog][15]
4. [Whimsy Project LDAP][16]
5. [Whimsy Podling Website Scan][17]

The results of the clutch analysis are published daily and appear on the [Clutch Report][19].
The shell script also runs [`clutch2status.py`][13] which produces [clutch analysis pages][20].
The data is also written as a [`clutch2.json` file][21].

This program was recently modernized and returned to relevancy.

## An Improvement Plan

We have robust status information available for all the podlings, but have various gaps and incomplete
transformations.

1. The monthly report process must be adjusted. Two possibilities are available.
   - Switch to use a process similar to what the Board uses for TLPs.
   - Switch to Confluence process that looks like what we are doing now.
2. The Podling YML file does a good job of handling the data that is on the Podling Status page.
   What is lacking is a clean UX to edit the data at the appropriate time.
3. Editing the Podling.xml file by hand can become an issue when the DTD is not properly followed.
   Whimsy's podling roster page solves this for Mentors by handling that on its own.
4. The Podling Status page mixes data with valuable recipes that lead to success.
   They are in an svn repository in a combination of xml and html. 
5. Many of the resource choices that podlings have made are now narrowed and normalized.
   Naming patterns are used. Mailing lists, SVN, Git, Jira, Confluence, and
   Releases can all be found by inspection once they are created.
6. Many of the less usual processes like podling name changes are not well documented.
   Support for these can be improved.
   
### Podling data not in `podlings.xml`

We have to decide how best to handle the data that is in the Podlings Status page and the
Podlings YML file. We should narrow this down to what is critical to keep and then decide
where it should go.

These items seem to be the most critical:

1. SGA - the date that the SGA is received.
2. ASF Copyright - the data that the donated code has had the copyright updated to Apache
   along with the License headers updated as appropriate.
3. Distribution Rights - the date that the code and its dependencies have been confirmed
   to follow the [Legal Policy][23] on allowed 3rd party licenses.    
4. Issue Tracker - are issues tacked in JIRA or Github?
5. Wiki - does the project have a wiki, and is it a Confluence Space or a Github wiki?
6. News - while it should be able to track new committers and PPMC members automatically 
   from the Roster page it makes sense to allow the podling to track other events.
   Releases can be detected as well and automatically added.
7. Proposal - this url is not always the same as the podling name.
8. Name change information - there is [INCUBATOR-199][24] which requests adding more explicit
   information about name changes to podlings along with improvements to resolutions.

There are design choice here. Do we fold all of these additional pieces of information into
`podlings.xml`, or do we normalize the Podling YML file to only include these fields.
A third option is to replace the Podling YML with a data file in another format.

### Podling UX

Eliminating the need to hand edit files without removing the ability is a goal. Let's discuss
the actions that need to be recorded. Work was started in this direction in Whimsy and
this can be continued.

1. New Podling - begins incubation. This adds the `podling` record to `podlings.xml`
2. Podling Roster / Status - this page exists and currently handles roster changes. It could be
   expanded to cover updates:
   - News
   - IP related events
   - Reporting information
   
   Also, the page can show the clutch analysis for the podling.
3. Rename Podling - this expensive operation needs to be discouraged, but when it is needed
   appropriate guidance should be provided.
4. Exit Incubation - a page that covers the several transitions a podling may make as it
   exits the Incubator by graduating or retiring.

### Incubator Site

The Incubator site can be simplified as follows:

1. Remove the podling status pages under `/projects/`
2. Improve the [`/projects/`][6] page to be the place to find deeper status with links to
   Whimsy pages for the podling. Each podling has an anchor in the tables.
3. Change the site's `.htaccess` file to redirect project links to the anchor.
4. Remove the clutch analysis pages since the information will be on the Whimsy page.

### Incubator SVN

The Podling Status pages in [xml][3] will no longer be updated nor will they be shown.
They can remain in svn for archival purposes.

## Cookbook Checklists

The checklists should be moved into the [Cookbook][22]
   
### Bootstrap 

These tasks are done to setup infrastructure for the podling and prepare the team to develop
in The Apache Way.

- LDAP
- DNS
- Mailing lists created
- Mailing list signups
- Roster complete
  - ICLA for initial committers w/o apache accounts
  - Accounts requested for new apache committers
  - All initial committers added to the PPMC
- Code repository ready
- Website
- Wiki
- Issue Tracker

### IP / Copyright / Distribution Rights Checklist 

- SGA / Code transfer documents. 
- Apache copyright added to donated code.
- Apache license added to code as appropriate.
- Licenses of dependencies are reviewed.
- Podling Suitable Name Search
  - PodlingNameSearch created 
  - Research Completed by podling
  - Brand Approval

### Incubation Watch List

- Collaborative Development
  - Are long term volunteers including non-coders being identified and
	elected to be committers?
  - Are the committers independent and from at least three entities?
  - Are decisions being made in public on the dev@ mailing list?
- Licensing Awareness
  - As code is developed are new dependency's licenses properly handled?
  - Are all licensing issues being acknowledged?
  - Are any trademark issues being acknowledged?
  - Are credit issues being acknowledged?
- Releases
  - Are mentors providing enough Guidance and Votes on dev@?
  - Are source releases fully license and notice compliant?
  - Are any binary convenience releases fully license and notice compliant?
  - Are all releases distributed through required channels?
	
### Graduation Checklist

- Has the podling discussed graduation on dev@?
- Do the Mentors agree that the podling is ready?
- If graduating into an existing TLP that PMC.
  - Has Graduation been discussed and the VOTE passed dev@podling?
  - Has Graduation been discussed and the VOTE passed dev@pmc?
- If graduating to a new TLP the IPMC on general@
  - Has the PMC been properly identified?
  - Has a PMC Chair been selected?
  - Has the Graduation Resolution passed the podling on dev@?
  - Has Graduation been discussed and the VOTE passed general@incubator?
  - If to a new TLP is the resolution on the Board's agenda?
  - Did the resolution pass? (exit)

[0]: https://incubator.apache.org/podling.xml "All podlings"
[1]: https://whimsy.apache.org/roster/ppmc "All current podling roster pages"
[2]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/projects/incubation-status-template.xml "Podling status page template"
[3]: https://whimsy.apache.org/roster/ppmc/rya "Rya roster pages"
[4]: https://incubator.apache.org/projects/rya.html "Rya podling status page"
[5]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings/rya.yml "Rya yml file used on roster page"
[6]: https://incubator.apache.org/projects/#current "Current podlings table link to podling status"
[7]: https://incubator.apache.org/projects/#graduated "Graduated podlings table link to podling status and post graduate location"
[8]: https://incubator.apache.org/projects/#retired "Retired podlings table link to podling status and post retirement location, if any"
[9]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings/openwhisk.yml "Podling status YML file example"
[10]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/clutch2report.py "clutch2report.py creates the monthly report"
[11]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/clutch2.sh "clutch2.sh creates the clutch report, json and pages"
[12]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/clutch2.py "clutch2.py performs clutch analysis"
[13]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/clutch2status.py "clutch2status.py creates the podling clutch analysis page"
[14]: http://mail-archives.apache.org/mod_mbox/ "Apache mailbox archives"
[15]: https://gitbox.apache.org/repositories.json "Catalog of all Apache Git repositories on GitBox"
[16]: https://whimsy.apache.org/public/public_ldap_projects.json "Project LDAP included PMC Members and Committers"
[17]: https://whimsy.apache.org/public/pods-scan.json "Results of a scan of podling websites for Apache Branding requirements"
[18]: http://svn.apache.org/repos/asf/incubator/public/trunk/content/projects/openwhisk.xml "Podling status page example"
[19]: https://incubator.apache.org/clutch/ "Clutch Analysis"
[20]: https://incubator.apache.org/clutch/gobblin.html "Example podling clutch analysis"
[21]: https://incubator.apache.org/clutch.json "Clutch Analysis - JSON data"
[22]: https://incubator.apache.org/cookbook/ "Incubator Cookbook"
[23]: http://www.apache.org/legal/resolved.html "What can be included in an Apache project?"
[24]: https://issues.apache.org/jira/projects/INCUBATOR/issues/INCUBATOR-199 "Request to extend podlings.xml"

