Title: UIMA-AS Codebase Intellectual Property (IP) Clearance Status


(Note: the original name of the donation was UIMA-EE; this name was changed while in the incubator to UIMA-AS)


The contribution is a set of components that extend the Apache UIMA framework to support fine-grained "scale-out" to multiple independent processes (potentially running in a LAN/WAN), using techniques that make use of JMS (Java Messaging Service) standards. It includes components that use Apache ActiveMQ as the messaging infrastructure. Also included are Eclipse plugin components for editing a new XML descriptor, used to describe the deployment of a UIMA service using this new kind of scale-out.


The contributed code is in the "sandbox" area of the UIMA SVN: [http://svn.apache.org/viewvc/incubator/uima/sandbox/trunk/uima-as/](http://svn.apache.org/viewvc/incubator/uima/sandbox/trunk/uima-as/) , where it is being cleaned up and otherwise worked on. The original donation is in a zip file attached to a JIRA issue: [http://issues.apache.org/jira/browse/UIMA-689](http://issues.apache.org/jira/browse/UIMA-689) .


The donation codebase is a set of new modules and documentation and does not contain patches for other components.



- PMC responsible for the code: Apache UIMA (currently an Incubator project, so officially, the Incubator PMC)


- This donation is being initially imported into the Apache UIMA project in the "sandbox" under the top level directory "uima-as".


- Officer or member managing donation: Ken Coar

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2008-04-22 | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

The MD5 sum for the donated software: d1ae83965d28d55a2d8ddf1671b7b21c donatedFiles.zip ( _md5 calculated using Windows Explorer extension digestIt 2004_ ).


## Copyright {#Copyright}

| date | item |
|------|------|
| 2008-04-03 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2008-04-22 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _UIMA-EE and its associated tooling_ .


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



- IBM Corporation

| date | item |
|------|------|
| 2008-04-22 | Check that all active committers have a signed CLA on record. |
| 2008-04-23 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| N/A | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2008-04-22 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



- Unanimously accepted; `uima-dev@incubator.apache.org` message ID `&lt;480DFFEF.4060502@schor.com&gt;` .
