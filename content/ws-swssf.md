Title: Streaming-WebService-Security-Framework (swssf) Codebase Intellectual Property (IP) Clearance Status


In order to be able to use WS-Security, typically the DOM processing model will be applied. For further processing, the XML document must be fully read into an object-tree by the DOM parser. The whole object-tree is hold in the computer memory during the processing. This requires a lot of processor and memory resources. Now, if an attacker sends over-sized SOAP documents, it can lead to a Denial-of-Service (DoS) attack. For encrypted documents the memory consumption is even higher. Firstly, the entire SOAP Message must be read into memory, then the decryption can be performed. The decrypted XML part must be read in an object-tree again. At this time, both the encrypted and decrypted XML part is present in the memory. Afterwards the encrypted XML part can be replaced with the decrypted one.


WS-Security provides integrity, authenticity and confidentiality at the message level. But which parts of the SOAP message must be secured and how is not defined in the WS-Security standard. What are the requirements for a SOAP client to access a Web Service successfully? Must the entire SOAP body to be encrypted? Is a timestamp expected? Must the message be signed? Which keys must be used and in which format are they expected? In order to express such requirements, the WS-SecurityPolicy standard was introduced.


If WS-SecurityPolicy is applied in an DOM environment and the client sends a message which does not correspond to the policy, a lot of computer resources are unnecessarily wasted again. The DOM parser fully reads the message into memory, the WS-Security framework processes the document using the security header and as last the WS-SecurityPolicy framework notes that the document was not protected as the policy it demanded.


This work presents a streaming-based WebService-Security-Framework with the ability to process large SOAP documents efficiently. The streaming-based processing of the messages is done via the StAX-API. With the streaming-oriented approach it is possible to gradually read and process the messages without keeping the entire message in the memory. If it is not possible to process the message, for example because the used keys are not known, the process can be aborted immediately.


The integration of WS-SecurityPolicy makes it possible to achieve the wished "fail-fast" behavior. This is, because policy relevant events can and will be evaluated immediately.


Me, Marc Giger &lt;gigerstyle@gmx.ch&gt; contributes/donates my Streaming-WebService-Security-Framework (swssf) to the WSS4J project. A part of this work (encryption, decryption and policy-verification) was developed for my master-thesis in Applied IT Security. The swssf codebase consists of about 26396 lines java code and additionally about 9263 lines of test code (526 Tests).


The contributed code is attached to issue WSS-311



- Which PMC will be responsible for the code: Apache Web Services


- Into which existing project/module: WSS4J


- Officer or member managing donation: Daniel Kulp

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2011-08-23 | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product.<br></br>The framework will be integrated into WSS4J-2 and most probably renamed accordingly |

MD5 or SHA1 sum for donated software: The svn dump is attached to https://issues.apache.org/jira/browse/WSS-311 and has an md5 of 9cd87d1ae47029f37fc4e30f7c185ebd and is digitally signed by the original author with a signature of: `
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2.0.17 (GNU/Linux)

iQEcBAABAgAGBQJOUQOgAAoJEF8Zt+R9dfyulyoIAKCQKQVvqNPC45j/MufbKs67
J+7vK8hooJ8A3IaxRx0b5iIZwbWN1rX367yKniEMulkW9mNeu+VKj8d6JZcZuLkF
I9IqNUrNG8o+u1LKD+84jdni8NVha584UXWJELG3I7000zX2AnTe6M3ePlOltj1G
G7luUoMBLmsxTt4LIST+W1AAGlbwslRCe98CnWeYSrVDp+MFqd4z084ZkPTYLEJH
bGFMWPIRtJpAp1mBUkykBHSp94g1blmYEZsqAQWivOZWRibYCEMMZ+bNqdt6QBrP
imgQXercKOaXWbc2x37/1bSouGoBLel/l/PWeRzxjGF4Ol/OUKeqkHp1YBdzQcE=
=6WD3
-----END PGP SIGNATURE-----
` 


## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-08-29 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-08-24 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _the name of the grant as record in the grants.txt document so that the grant can be easily identified_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights: Marc Giger



-  _For individuals, use the name as recorded on the committers page_ 

| date | item |
|------|------|
| 2011-08-23 | Check that all active committers have a signed CLA on record. |
| 2011-08-23 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2011-08-23 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-08-23 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [Vote thread on the WebServices PMC](https://mail-search.apache.org/members/private-arch/ws-private/201108.mbox/%3C8221192.ACzd2zs93s@dilbert.dankulp.com%3E) (private list, ASF members only)
