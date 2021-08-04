Title: Eagle Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


Eagle is a Monitoring solution for Hadoop to instantly identify access to sensitive data, recognize attacks, malicious activities and take actions in real time. Eagle supports a wide variety of policies on HDFS data and Apache Hive. Eagle also provides machine learning models for detecting anomalous user behavior in Apache Hadoop.


<span class="graduated">The Eagle project graduated on 2016-12-21</span>



- 2016-12-21 Graduated to Apache TLP.

- 2016-11-15 Add one new committer: Jijun Tang.

- 2016-10-12 start graduation discussion and steps.

- 2016-09-05 Add one new committer: Jinhu Wu.

- 2016-07-21 Apache Eagle 0.4.0-incubating released.

- 2016-06-17 Add one new committer: Michael Wu.

- 2016-06-13 Add one new committer: Daniel Zhou.

- 2016-04-11 Apache Eagle 0.3.0-incubating released.

- 2016-02-01 Add one new committer: Ralph Su.

- 2015-11-19 Mailing list, wiki, jira, git repo and website initialized.

- 2015-10-26 Project entered incubation.


- Project Website: http://eagle.incubator.apache.org/


- Community and how to contribute: https://cwiki.apache.org/confluence/display/EAG/Community

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://eagle.incubator.apache.org/](http://eagle.incubator.apache.org/)  |
| . | wiki |  [http://cwiki.apache.org/confluence/display/EAG](http://cwiki.apache.org/confluence/display/EAG)  |
| Mailing list | user |  `user`  `@`  `eagle.incubator.apache.org`  |
| . | dev |  `dev`  `@`  `eagle.incubator.apache.org`  |
| . | commits |  `commits`  `@`  `eagle.incubator.apache.org`  |
| Bug tracking | jira |  [https://issues.apache.org/jira/browse/EAGLE](https://issues.apache.org/jira/browse/EAGLE)  |
| Source code | Git |  [https://gitbox.apache.org/repos/asf/incubator-eagle.git](https://gitbox.apache.org/repos/asf/incubator-eagle.git)  |
| . | GitHub |  [https://github.com/apache/incubator-eagle](https://github.com/apache/incubator-eagle)  |
| Mentors | hsaputra | Henry Saputra |
| . | omalley | Owen O'Malley |
| . | jhyde | Julian Hyde |
| . | ptgoetz | P. Taylor Goetz |
| . | amareshwari | Amareshwari Sriramadasu |
| Committers | yonzhang2012 | Edward Zhang |
| . | hao | Hao Chen |
| . | arunmanoharan | Arun Manoharan |
| . | libsun | Libin Sun |
| . | jilin | Jilin Jiang |
| . | qingwzhao | Qingwen Zhao |
| . | cgupta | Chaitali Gupta |
| . | ralphsu | Ralph Su |
| . | senthilec566 | Senthil Kumar |
| . | hdendukuri | Hemanth Dendukuri |
| . | dazhou | Daniel Zhou |
| . | mw | Michael Wu |
| . | jinhuwu | Jinhu Wu |
| . | jjtang | Jijun Tang |


-  [November 2016](https://wiki.apache.org/incubator/November2016) 

-  [August 2016](https://wiki.apache.org/incubator/August2016) 

-  [May 2016](https://wiki.apache.org/incubator/May2016) 

-  [February 2016](https://wiki.apache.org/incubator/February2016) 

-  [January 2016](https://wiki.apache.org/incubator/January2016) 

-  [December 2015](https://wiki.apache.org/incubator/December2015) 

-  [November 2015](https://wiki.apache.org/incubator/November2015) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2015-10-21 | Make sure that the requested project name does not already exist. We've completed the [podling name search for Apache Eagle](https://issues.apache.org/jira/browse/PODLINGNAMESEARCH-85)  |
| ....-..-.. | If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance. |
| ....-..-.. | If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted. |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2015-10-28 | Ask infrastructure to create source repository modules and grant the committers karma. |
| 2015-10-28 | Ask infrastructure to set up and archive mailing lists. |
| 2015-10-28 | Ask infrastructure to set up issue tracker (JIRA, Bugzilla). |
| 2015-10-28 | Ask infrastructure to set up wiki (Confluence, Moin). |
| ....-..-.. | Migrate the project to our infrastructure. |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| ....-..-.. | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. | Give all Mentors access to the incubator SVN repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. | Tell Mentors to track progress in the file 'incubator/projects/{project.name}.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| ....-..-.. | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| ....-..-.. | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| ....-..-.. | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| ....-..-.. | Check that all active committers have submitted a contributors agreement. |
| ....-..-.. | Add all active committers in the STATUS file. |
| ....-..-.. | Ask root for the creation of committers' accounts on people.apache.org. |

## Project specific {#Project+specific}

 _Add project specific tasks here._ 


# Incubation {#Incubation}

These action items have to be checked for during the whole incubation process.


 _These items are not to be signed as done during incubation, as they may change during incubation._  _They are to be looked into and described in the status reports and completed in the request for incubation signoff._ 


## Collaborative Development {#Collaborative+Development}


- Have all of the active long-term volunteers been identified and acknowledged as committers on the project?

- Are there three or more independent committers? (The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)

- Are project decisions being made in public by the committers?

- Are the decision-making guidelines published and agreed to by all of the committers?

## Licensing awareness {#Licensing+awareness}


- Are all licensing, trademark, credit issues being taken care of and acknowleged by all committers?

## Project Specific {#Project+Specific}

 _Add project specific tasks here._ 


# Exit {#Exit}

 _Things to check for before voting the project out._ 


## Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}


- If graduating to an existing PMC, has the PMC voted to accept it?

- If graduating to a new PMC, has the board voted to accept it?

## Incubator sign-off {#Incubator+sign-off}


- Has the Incubator decided that the project has accomplished all of the above tasks?
