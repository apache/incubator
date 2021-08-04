Title: XBean Codebase Intellectual Property (IP) Clearance Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

XBean is a new set of functional modules for the Apache Geronimo project. XBean includes the following modules:



- classpath: Utilities for manipulating the class path of a server after is has been initialized

- jmx: Utilities for automated wrapping of serves with an MBean

- kernel: A light weight kernel

- osgi: Experimental bidirectional bridge between OSGi and the XBean kernel

- reflect: Simple API for build objects using reflection

- sca: SCA annotation support for service building

- server: Supporting classes to start a kernel in a standalone server

- spring: Simplified XML extensions for Spring

- telnet: Lightweight telnet server for scripting the kernel


- Geronimo module


- geronimo/xbean

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2006-01-20 | No hits at [United States Patent and Trademark Office](http://tess2.uspto.gov/bin/gate.exe?f=login&amp;p_lang=english&amp;p_d=trmk)  |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2006-01-20 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2006-01-20 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2006-01-20 | 
Check that all active committers have a signed CLA on record.

svn log https://svn.codehaus.org/xbean | grep "r[0-9][0-9]* | " | sed "s/r[0-9][0-9]* | \(.*\) | .* | .*$/\1/" | sort | uniq
All of the committers have a CLA on file at Apache. The following table maps the unix user names to real names:


 | chirino | Hiram Chirino|
 | dain | Dain Sundstrom|
 | dandiep | Daniel Diephouse|
 | dblevins | David Blevins|
 | gnt | Guillaume Nodet|
 | jstrachan | James Strachan|
 | jvanzyl | Jason van Zyl|
 | maguro | Alan Cabrera|
 | root | -service account-|
 | spullara | Sam Pullara|
 |
| 2006-01-20 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is is required to authorize their contributions under their individual CLA. |
| 2006-01-20 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2006-01-20 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- Has the receiving PMC voted to accept it? YES
<u> [http://mail-archives.apache.org/mod_mbox/geronimo-dev/200602.mbox/%3c43E282DD.8020502@hogstrom.org%3e](http://mail-archives.apache.org/mod_mbox/geronimo-dev/200602.mbox/%3c43E282DD.8020502@hogstrom.org%3e) <br></br></u><u> [http://mail-archives.apache.org/mod_mbox/geronimo-dev/200601.mbox/%3c6BA20318-F62D-4645-AF21-AE31428C7351@iq80.com%3e](http://mail-archives.apache.org/mod_mbox/geronimo-dev/200601.mbox/%3c6BA20318-F62D-4645-AF21-AE31428C7351@iq80.com%3e) <br></br></u>