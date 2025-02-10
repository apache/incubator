# Apache Incubator Website

This is the content and build scripts for http://incubator.apache.org/

## Contributing to the website content

You can fork from https://github.com/apache/incubator, test your changes as described below
and raise a pull request.

Use the [general@incubator.apache.org](https://lists.apache.org/list.html?general@incubator.apache.org) mailing list to contact
the Incubator PMC which manages this website.

## Automated publishing - Website and Clutch data

Commits to the `master` branch are automatically checked out and built using `build_site.sh` by the 
[Incubator GIT Site - part 2](https://ci-builds.apache.org/job/Incubator/job/Incubator-GIT-Site-part-2/)
Jenkins job. The results are pushed to the [`content` folder of the `asf-site` branch](https://github.com/apache/incubator/tree/asf-site/content)
which is in turn published automatically to http://incubator.apache.org/ by the ASF's `gitwcsub` mechanism.

The data for http://incubator.apache.org/clutch/ takes longer to build so it is handled by a separate
[SVN Clutch Analysis - part 1](https://ci-builds.apache.org/job/Incubator/job/Incubator-SVN-Clutch-Analysis-part-1/)
Jenkins job that runs the `build_clutch.sh` script that's scheduled to run daily and is also triggered by svn changes using
the [Trigger-Clutch-Analysis-on-SVN-Change](https://ci-builds.apache.org/job/Incubator/job/Trigger-Clutch-Analysis-on-SVN-Change/)
Jenkins job. The results are stored in the [`reserve` folder of the `asf-site` branch](https://github.com/apache/incubator/tree/asf-site/reserve)

For now that Clutch data is still managed in svn, at http://svn.apache.org/repos/asf/incubator/public/trunk/ , see
the build scripts for more info. The projects folder (podling status pages) and the ip-clearance folders are also still in svn
and the html is built using `ant docs` in the `build_clutch.sh` script.

Any build failures are reported to *[cvs@incubator.apache.org](https://lists.apache.org/list.html?cvs@incubator.apache.org)*
mailing list.

## Prerequisites for building the website locally

The website is built using [JBake](https://jbake.org/) and Groovy templates.
The builds for the website do require internet access.

- Install JBake from http://jbake.org/download.html
  - Currently it looks like version 2.6.0 or greater is required.
- Create an environment variable `JBAKE_HOME` pointing to your JBake installation, e.g.
  - `export JBAKE_HOME=/usr/local/Cellar/jbake/2.6.4`
- Ensure that you have a JVM locally, e.g. [OpenJDK](http://openjdk.java.net/install/)

## Building & testing the site locally

To test the site locally, use 

    ./build_local.sh -b -s
    
This builds the site, serves it locally at  http://localhost:8820/ and rebuilds the content fairly
quickly if any changes are made.

That script can be called with any of the [arguments you would pass to jbake](https://jbake.org/docs/2.6.4/#bake_command).

### Building the Clutch and Legacy SVN Content (if you know what you're doing)

**Warning** do not run the clutch build scripts unless you are sure you understand them, and please be careful not to commit any of the resulting assets and pages to the git master branch. That content and data is only committed to the `asf-site` 
branch's `reserve`folder as mentioned below.

The `build_local_clutch.sh` script can be used to build the Clutch data, but that's updated automatically by the Jenkins 
builds as `build_clutch.sh` mentioned below so it's not required unless you want to test that.

## Asciidoctor

Most of the pages in the site are written using Asciidoctor (those with file extension .ad).
While it is a form of asciidoc it does have some [syntax differences that are worth reviewing](http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)

Note that Asciidoctor automatically generates links for text that looks like an email address or a web address.
Also, it can have problems with URLs that contain certain special characters.
In such cases, the URL should be prefixed and suffixed with '++'.
For example:
- `++https://lists.apache.org/list.html?general@incubator.apache.org++[Incubator community]`

## Groovy Templates

The site templates are written in groovy scripts.
Even though the files end with `.gsp` they are not GSP files and do not have access to tag libraries.
You can run custom code in them, similar to what is done in [homepage.gsp](templates/homepage.gsp) and [projectspage.gsp](templates/projectspage.gsp).

## Clutch data files

In addition to the [clutch pages](https://incubator.apache.org/clutch/) several data files are provided:

* [clutch.json](https://incubator.apache.org/clutch.json) contains the latest clutch analysis for all current podlings.
* [clutch.txt](https://incubator.apache.org/clutch.txt) contains a list of current podlings,
* [report_due_1.txt](https://incubator.apache.org/report_due_1.txt) dev mailing lists for podlings reporting in group 1.
* [report_due_2.txt](https://incubator.apache.org/report_due_2.txt) dev mailing lists for podlings reporting in group 2.
* [report_due_3.txt](https://incubator.apache.org/report_due_3.txt) dev mailing lists for podlings reporting in group 3.
