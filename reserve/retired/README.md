Retired podlings markers for website redirects
---

This directory is used to enable website redirects for retired podlings (see also [INFRA-21451](https://issues.apache.org/jira/browse/INFRA-21451)).

When a podling retires, create a directory with the host name of the podling.
e.g. if the podling website is abcd.apache.org, then create directory abcd/

Empty directories are ignored when checking out Git repos, so there needs to be a file in it,
so create a bare index.html file. (There's nothing to see, so no point in generating a listing)

Once the Incubator website has been deployed, the website
http://abcd.apache.org/
will redirect to 
https://incubator.apache.org/projects/abcd.html which is the standard status page for podling "abcd" and
should mention the "retired" status of the podling.

Note: older podlings with websites of the form 
http://abcd.incubator.apache.org/
or
http://incubator.apache.org/abcd/
are handled by the .htaccess file here:
https://github.com/apache/incubator/blob/master/assets/.htaccess
