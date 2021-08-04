Title: httpd-cli


This page tracks the project status, incubator-wise.


<span class="graduated">The httpd-CLI project graduated on 2004-12-16</span>


The Apache 2.0 module mod_aspdotnet, and CLI implementation of Apache.Web.Host, together form a hosting environment for ASP.NET applications within Microsoft's .NET Framework for Windows, and the Apache 2.0 httpd server running on Win32.


This code was developed by William A. Rowe, Jr., Covalent Technologies, Inc., and is donated to the Apache community as a starting point for multiple avenues of CLI integration with the Apache 2.0 httpd server.


Microsoft, as part of it's .NET patents, asserts ownership of the implementation of System.Web.Hosting, the framework under which ASP.NET applications are instantiated. Note that this patent does not assert the implementation of System.Web.Host, System.Web.Request and other specific implementations of the server 'container' which forwards ASP.NET requests to the .NET Framework's implementation of System.Web.Hosting.


The initial goal of the PMC is to release this ASP.NET implementation of ASP.NET for he benefit of Apache httpd Win32 users.


The second goal of the PMC will be to refactor the Microsoft COM/.NET CLI thunks which exist in mod_aspdotnet, from the specific implementation of the ASP.NET-based Apache.Web.Host container.


Once the CLI thunk is a seperate and distinct component, the next two goals, may occur in parallel;



- Abstract the Apache httpd request model as it's own CLI implementation, allowing authors to handle native httpd requests without the Microsoft specific ASP.NET model.


- Build alternate CLI thunks to other engines such as mono, to allow CLI code to run on other platforms using the native Apache request model.

This goal allows CLI developers, to use tools such as C# to develop Apache-based solutions using alternate CLI hosting environments such as mono, without infringing on the claims of Microsoft which may inhibit ASP.NET-based solutions on non-Windows operating systems.



- The Apache httpd PMC owns this httpd CLI subproject, and this subproject follows the Apache httpd PMC's direction. Significant contributors to this sub-project (e.g. 6 months of sustained contribution) will be proposed for Apache httpd PMC membership.


- The CLI sub-project's modules will be available under seperate downloads, and are not envisioned to become part of a 'stock' httpd distribution.

# Detailed References: {#Detailed+References%3A}

| item | type | reference |
|-------|-------|------------|
| Status file | www | http://incubator.apache.org/projects/httpd-cli.html |
| Website | www | To-Do; http://httpd.apache.org/cli/ |
| Mailing list | dev | cli-dev@httpd.apache.org |
| Source code | SVN | /repos/asf/incubator/httpd/cli/trunk/ |
| Mentor | wrowe | Will Rowe (CLA on file) |
| Committers | ridruejo | Daniel Lopez (CLA on file) |
| Committers | ianh | Ian Holsman (CLA on file) |
| Committers | jimjag | Jim Jagleski (CLA on file) |
| Committers | shughes | Sterling Hughes (CLA on file) |
| Committers | wrowe | Will Rowe (CLA on file) |
| Discussion Thread | mail | Message-Id: &lt;6.0.2.0.2.20040305114405.02b4db60@pop3.rowe-clan.net&gt; |

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 



- 19 July 2004

In March '04, the httpd PMC referred the mod_aspdotnet contribution (Code Grant ack'ed in rev 1.7 of foundation/grants.txt) for incubation.


The project was recently picked back up, with Will Rowe now having the cycles to devote to the care and feeding required of incubation. Ian Holsman, also an httpd PMC member, stepped up to co-shepherd the incubation.


Invites to the interested parties were sent last week to join the mailing list cli-dev@httpd.apache.org, followed by an invitation to the dev@httpd community. The status page/ip incubation template was created, with Ian managing the site. Will has imported the initial contribution into SVN (under asf/incubator/httpd/cli/).


Next steps are documented in status, first posts will be sent to this list this week. mod_aspdotnet should have an initial release soon, followed by the refactoring of code to support an Apache.Web model that is entirely independent of the Microsoft ASP.NET technology, usable in C# with one of several CLI environments, including mono.


The cli-dev team would like to thank Noel and Sander for their advise and handholding through initial mailing list creation, SVN setup, and general guidance on the incubation process.


Will Rowe



- 30 October 2004

After soliciting a number of comments from cli-dev testers of the mod_aspdotnet, and committing their patches to solve various bugs, the subproject has extracted v2.0.0 release candidate 1 today.


The installer was migrated to InstallShield X, the only and current product for authoring .msi files from InstallShield. This, after experience with converting the Apache 1.3.33 installer, turned out to be fairly trivial, and the .ism project file did have an xml flavor that can be tracked in svn.


Next actions are creating a cli-users@httpd end-user list, declaring v2.0.0 released, adding the tracking category in bugzilla, and moving from incubator/httpd/cli to httpd/cli in svn, once graduated.


Will Rowe



- 4 February 2005

Graduation Report


December 16th is the date that the httpd-pmc vote was closed, this sub-project adopted, the repositories and first release moved into the httpd.apache.org domain, and officially kicked off. This had included the cli-users@httpd list, cli-dev@httpd list, bugzilla recordkeeping at issues.apache.org, and http://httpd.apache.org/cli/ home page.


I would like to especially thank Ian for his extraordinary help, simply navigating the particularities with the incubator's infrastructure, and all of the interested users and developers who have stepped up to this effort. A number of individuals are using this in production, for their own development, and are coming up with exciting challenges to overcome in the future.


My appologies for taking so long to close the incubator pages, and thank you to the incubation committee for helping promote this work.


Will Rowe


# Project Setup {#Project+Setup}

## Identify the codebase {#Identify+the+codebase}

| date | item |
|-------|-------|
| 2004-07-19 | If applicable, make sure that any associated name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product. |

## Copyright {#Copyright}

| date | item |
|-------|-------|
| 2004-02-19 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2004-02-26 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|-------|-------|
| 2004-07-19 | Check that all active committers have a signed CLA on record. |
| 2004-07-19 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is is required to authorize their contributions under their individual CLA. |
| 2004-07-19 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2004-07-19 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- Has the receiving PMC voted to accept it?

The Apache httpd project voted and it was adopted on 16 December, 2004.

