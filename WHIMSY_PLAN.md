# Incubator Podling Lifecycle from Whimsy

We would like to finish the data migration and UX work to manage the podling lifecycle and
related data from Whimsy. What follows is a description of the data currently in `podlings.xml`,
the data needed that is not in the `podlings.xml`, an initial plan for the Podling Lifecycle UX
to be discussed, and then examples of podlings in various states from `podlings.xml`

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


## Podling data currently not in `podlings.xml`

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
7. Proposal - this url is not always the same as the podling name. For example the Tuweni
   is proposed as Cava.
8. Podling Name Search issue.
9. Name change information - there is [INCUBATOR-199][24] which requests adding more explicit
   information about name changes to podlings along with improvements to resolutions.

There are design choice here. Do we fold all of these additional pieces of information into
`podlings.xml`, or do we normalize the Podling YML file to only include these fields.
A third option is to replace the Podling YML with a data file in another format.

## Podling UX for Whimsy

Eliminating the need to hand edit files without removing the ability is a goal. Let's discuss
the actions that need to be recorded. Work was started in this direction in Whimsy and
this can be continued.

1. New Podling - begins incubation. This adds the `podling` record to `podlings.xml`.
   We should discuss if this a first time only page or can be combined with Rename and Exit.
   If so then this could be termed the Podling Lifecycle Page.
   - Podling name.
   - Resource.
   - Sponsor.
   - Start date.
   - Description.
   - Champion.
   - Reporting group. This can be computed from the Start date.
   - Proposal.
   - News. The start of the podling.
   - Issue Tracker. (is this choice best deferred to later?)
   - Wiki. (is this choice best deferred to later?)
   
2. Podling Roster / Status - this page exists and currently handles roster changes. It could be
   expanded to cover updates:
   - Roster (as now)
     - Mentors
     - PPMC Members
     - Committers
   - News
     - News about adding Committers, PPMC members, and Mentors can be automatic.
     - Manual news should addable.
     - PPMC members should be able to remove news.
   - IP related events
     - SGA
     - ASF Copyright
     - Distribution Rights
     - Podling Name Search (does the current automated procedure work in all cases?)
   - Reporting group.
     - IPMC Chair removes the monthly checkbox or removes it depending on reporting.
   
   Also, the page can show the [clutch analysis][20] for the podling.
   The [current generated JSON file][21] which can be abbreviated to remove redundant information like "LDAP".
   
3. Rename Podling - this expensive operation needs to be discouraged, but when it is needed
   appropriate guidance should be provided.
   - Podling name
   - Description
   - Podling Name Search (does the current automated procedure work in all cases?)
   - Resource (expensive) - leads to explanation / checklist.
   - News entry about renaming.
   
4. Exit Incubation - a page that covers the several transitions a podling may make as it
   exits the Incubator by graduating or retiring.
   - End Date
   - Graduation?
     - New TLP?
     - To an existing PMC?
       - Which PMC?
       - Subproject link?
   - Retirement?
     - Development going to be elsewhere?
       - 3rd Party link?
   - Description of the change 
   - Resolution (automatically filled in with the answers)
     - tlp attribute
     - link attribute
     - url attribute
     - description


#### Example Podlings from `podlings.xml`

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

A podling that changed its name (highlights the [INCUBATOR-199 issue][24]):
```
    <podling name="Flagon" status="current" resource="flagon" resourceAliases="senssoft" sponsor="Incubator" startdate="2016-07-13">
        <description>Flagon is a software tool usability testing platform</description>
        <reporting group="1"/>
	<champion availid="lewismc">Lewis John McGibbney</champion>
        <mentors>
            <mentor username="lewismc">Lewis John McGibbney</mentor>
            <mentor username="dmeikle">David Meikle</mentor>
            <mentor username="atri">Atri Sharma</mentor>
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


[0]: https://incubator.apache.org/podling.xml "All podlings"
[1]: https://whimsy.apache.org/roster/ppmc "All current podling roster pages"
[20]: https://incubator.apache.org/clutch/gobblin.html "Example podling clutch analysis"
[21]: https://incubator.apache.org/clutch.json "Clutch Analysis - JSON data"
[23]: http://www.apache.org/legal/resolved.html "What can be included in an Apache project?"
[24]: https://issues.apache.org/jira/projects/INCUBATOR/issues/INCUBATOR-199 "Request to extend podlings.xml"

