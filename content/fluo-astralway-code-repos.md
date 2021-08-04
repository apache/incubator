Title: Fluo contributions from Astralway Codebase Intellectual Property (IP) Clearance Status


Astralway is the name of the project on GitHub (github.com/astralway) where Fluo originated. Since Fluo graduated incubation, the Astralway maintainers (who are also Fluo PMC members) have separately maintained two developer tools and three example projects for use with Fluo. They now wish to contribute those projects directly to the Apache Fluo PMC.


The incoming code base is three git repositories ( [uno](https://github.com/astralway/uno) , [muchos](https://github.com/astralway/muchos) , and [examples](https://github.com/examples) ). Uno contains developer tools for running a single-node Accumulo/Fluo cluster for testing and development. Muchos is the same, but for running a multi-node cluster using Ansible. The examples project contains the three examples, phrasecount, webindex, and stresso, which are useful for testing Fluo, and as documentation for demonstrating example uses.



- The Apache Fluo PMC will be responsible for the code.


- The Astralway admins will coordinate with ASF Infra to transfer the existing GitHub repos to ASF and to configure ASF Gitbox dual-hosting for them, just as Fluo's current repositories are configured.


- Christopher Tubbs (Apache Fluo PMC member, ASF member, and Astralway project maintainer) will manage the contribution.

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2018-04-17 | If applicable, make sure that any associated name does not already exist and is not already trademarked for an existing software product. |

Donated software is identified as:



- https://github.com/astralway/uno (git commit: 8fbe10a9cd9e12f5eca67ee09cfad62aef141eb5)

- https://github.com/astralway/muchos (git commit: 65be99caa4968fec1219f36b599533b40f4755e5)

- https://github.com/astralway/examples (git commit: 4bd6a004c8dc37e2996314fd8b0de554562c5d38)

The above repos are currently locked (archived), to prevent changes. The intention is that the full repositories will be transferred to ASF, and renamed with the "fluo-" prefix.


## Copyright {#Copyright}

| date | item |
|------|------|
| 2018-04-17 | Check and make sure that the papers that transfer rights to the ASF been received. Entire donation is already ALv2 and all authors are ASF committers with ICLAs on file. ASF already has all rights necessary. |

## Verify distribution rights {#Verify+distribution+rights}

Individuals holding existing distribution rights (technically, everybody in the world has distribution rights; the project is licensed under ALv2):



- ctubbsii - Christopher Tubbs

- dhutchis - Dylan Hutchison

- drew - Drew Farris

- ecn - Eric Newton

- elserj - Josh Elser

- kennethmcfarland - Kenneth McFarland

- kturner - Keith Turner

- jmark99 - Mark Owens

- mmiller - Mike Miller

- mwalch - Mike Walch

| date | item |
|------|------|
| 2018-04-17 | Check that all active committers have a signed CLA on record. |
| Not applicable - ICLAs were already on file | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2018-04-17 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2018-04-17 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

Notes: Ansible (GPL3) is a dependency of Muchos. However, since Muchos is targeted specifically for use with Ansible and does not include Ansible code, it is covered by the platform exception (See discussion on https://issues.apache.org/jira/browse/LEGAL-282). All Muchos code itself is under the Apache License, Version 2.0


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  [Donation acceptance vote on Apache Fluo dev list](https://lists.apache.org/thread.html/921012ad4be72642e81e1f06aee1bdb6c973e85f76f91bc12c180a84@%3Cdev.fluo.apache.org%3E) 

-  [IP Clearance (lazy) vote on Apache Incubator general list](https://lists.apache.org/thread.html/a9a7ddcca6289edc3f756a085f37409f56da3029048e85d06d04427a@%3Cgeneral.incubator.apache.org%3E) 
