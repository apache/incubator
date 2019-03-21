# Apache Incubator Website

## Prerequisites

The website is built using JBake and a Groovy template.
The builds for the website do require internet access.

- Install JBake from http://jbake.org/download.html
- Create an environment variable `JBAKE_HOME` pointing to your JBake installation
- Ensure that you have a JVM locally, e.g. [OpenJDK](http://openjdk.java.net/install/)

## Clone the Source code

You can fork from github https://github.com/apache/incubator and raise a pull request.

## Building & Running the site

There is a custom `bake.sh` file that is used to build the website.
You can call it with any of the [arguments you would pass to jbake](http://jbake.org/docs/2.5.1/#bake_command).
The easiest way to use it is to run `./bake.sh -b -s`.
This will start up JBake in a watching mode as you make changes it will refresh after a short period of time.
(If you download JBake 2.6.4 then you may want to do `which jbake` and edit bake.sh. See commented lines.)
While working with it locally, you'll notice that the site URLs redirect to `incubator.apache.org`;
to change this edit `jbake.properties` and uncomment the line referencing `localhost`

If you want to run the full site build locally including the clutch analysis and any other other content
remaining in SVN then you can use `./build_local.sh`. Instead of publishing the site it finishes with JBake
in watching mode.

## Automatic build and publishing - Jenkins Setup

Commits to the `master` branch are automatically checked out and built using `build_site.sh`.

The corresponding jenkins job can be found at [https://builds.apache.org/view/H-L/view/Incubator/job/Incubator%20Site/](https://builds.apache.org/view/H-L/view/Incubator/job/Incubator%20Site/)

The result of the website build are pushed to the `asf-site` branch which are then published automatically using `gitwcsub`

## Asciidoctor

Most of the pages in the site are written using Asciidoctor.
While it is a form of asciidoc it does have some [syntax differences that are worth reviewing](http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)

## Groovy Templates

The site templates are written in groovy scripts.
Even though the files end with `.gsp` they are not GSP files and do not have access to tag libraries.
You can run custom code in them, similar to what is done in [homepage.gsp](templates/homepage.gsp) and [projectspage.gsp](templates/projectspage.gsp).
