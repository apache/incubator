Title: Apache IoTDB Project Incubation Status
<link href="http://purl.org/DC/elements/1.0/" rel="schema.DC"></link>

This page tracks the project status, incubator-wise. For more general project status, look on the project website.


<span class="graduated">The IoTDB project graduated on 2020-09-18</span>


IoTDB is a data store for managing large amounts of time series data such as timestamped data from IoT sensors in industrial applications.



- 2018-11-18 Project enters incubation.


- IoTDB Website - http://iotdb.incubator.apache.org


- link to the project status file (Committers,non-incubation action items,project resources, etc)

If the project website and code repository are not yet setup, use the following table:


| item | type | reference |
|------|------|-----------|
| Website | www |  [http://iotdb.incubator.apache.org/](http://iotdb.incubator.apache.org/)  |
| Mailing list | dev |  `dev`  `@`  `iotdb.apache.org`  |
| . | private |  `private`  `@`  `iotdb.apache.org`  |
| . | commits |  `commits`  `@`  `iotdb.incubator.apache.org`  |
| . | reviews |  `reviews`  `@`  `iotdb.apache.org`  |
| . | jira notifications |  `notifications`  `@`  `iotdb.apache.org`  |
| Source code | . | . |
| . | incubator-iotdb | https://github.com/apache/incubator-iotdb.git |
| Bug tracking | JIRA | https://issues.apache.org/jira/browse/IOTDB |
| Wiki | Confluence | https://cwiki.apache.org/confluence/display/IOTDB |
| Wiki | Documents | https://github.com/apache/incubator-iotdb/tree/master/docs |
| Twitter | twitter | https://twitter.com/ApacheIotdb/ |
| Roster | Whimsy |  [IoTDB Roster](https://whimsy.apache.org/roster/ppmc/iotdb)  |
| Champion | kmcgrail | Kevin A. McGrail |
| Mentors |  | . |
| . | jmclean | Justin Mclean |
| . | cdutz | Christofer Dutz |
| . | ningjiang | Willem Ning Jiang |
| . | kmcgrail | Kevin A. McGrail |
| Committers |  | . |
| . | caogaofei | Gaofei Cao |
| . | dope | Yi Xu |
| . | east | Dongfang Mao |
| . | geniuspig | Boris Zhu |
| . | haonan | Haonan Hou |
| . | hxd | Xiangdong Huang |
| . | jackietien | Yuan Tian |
| . | jfeinauer | Julian Feinauer |
| . | jiangtian | Tian Jiang |
| . | jimwang | Jianmin Wang |
| . | jincheng | Jincheng Sun |
| . | kangrong | Rong Kang |
| . | leirui | Lei Rui |
| . | liudw | Dawei Liu |
| . | liukun | Kun Liu |
| . | liurui | Rui Liu |
| . | lta | Tianan Li |
| . | qiaojialin | Jialin Qiao |
| . | shuozhang | Shuo Zhang |
| . | sunzesong | Zesong Sun |
| . | suyue | Yue Su |
| . | tsaitsunghan | Zonghan Cai |
| . | wangchen | Chen Wang |
| . | xingtanzjr | Jinrui Zhang |
| . | xuekaifeng | Kaifeng Xue |
| . | yuanjun | Jun Yuan |
| . | zhaoxinyi | Stefanie Zhao |


-  [IoTDB Board Reports](https://whimsy.apache.org/board/minutes/iotdb.html) 

# Project Setup {#Project+Setup}

This is the first phase on incubation, needed to start the project at Apache.


 _Item assignment is shown by the Apache id._  _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


## Identify the project to be incubated {#Identify+the+project+to+be+incubated}

| date | item |
|------|------|
| 2018-11-24 | Make sure that the requested project name does not already exist. [Please follow the guide to ensure a suitable project/product name.](http://www.apache.org/foundation/marks/naming.html)  |

## Infrastructure {#Infrastructure}

| date | item |
|------|------|
| 2018-11-24 | Request DNS (first step after creating podling status page) |
| 2018-11-24 | Request [Mailing Lists](https://whimsy.apache.org/officers/mlreq/incubator)  |
| 2018-11-24 | Request [git repositories](https://github.com/apache/incubator-iotdb)  |
| 2018-12-21 | Request [Website](https://iotdb.apache.org/)  |
| 2019-01-14 | Ask infrastructure to set up issue tracker ( [JIRA](https://issues.apache.org/jira/projects/IOTDB/issues) ). |
| 2018-12-24 | Ask infrastructure to set up wiki ( [Confluence](https://cwiki.apache.org/confluence/display/IOTDB) ). |
| 2019-01-19 | Migrate the project to our infrastructure. |
| 2019-07-25 | Ask infrastructure to add permission of ( [Nexus](https://issues.apache.org/jira/browse/INFRA-18788) ). |
| 2019-01-21 | Ask infrastructure to set up ( [Travis-CI](https://issues.apache.org/jira/browse/INFRA-17693) ). |
| 2019-12-06 | Ask infrastructure to set up ( [SonarCloud](https://issues.apache.org/jira/browse/INFRA-19507) ). |
| 2019-12-08 | Ask infrastructure to add permission of ( [DockerHub](https://issues.apache.org/jira/browse/INFRA-19459) ). |
| 2019-12-21 | Ask infrastructure to add permission of ( [Coveralls](https://issues.apache.org/jira/browse/INFRA-19612) ). |

## Mentor-related responsibility/oversight {#Interim+responsibility}

| date | item |
|------|------|
| ....-..-.. (done) | Subscribe all Mentors on the pmc and general lists. |
| ....-..-.. (done) | Give all Mentors access to the incubator Git repository. (to be done by the Incubator PMC chair or an Incubator PMC Member wih karma for the authorizations file) |
| ....-..-.. (done) | Tell Mentors to track progress in the file 'incubator/projects/iotdb.html' |

## Copyright {#Copyright}

| date | item |
|------|------|
| 2018-12-27 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2019-01-19 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

## Verify distribution rights {#Verify+distribution+rights}

| date | item |
|------|------|
| 2019-08-26 | Check and make sure that for all code included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2019-08-26 | Check and make sure that all source code distributed by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. |

## Establish a list of active committers {#Establish+a+list+of+active+committers}

| date | item |
|------|------|
| 2020-01-16 | Check that all active committers have submitted a contributors agreement. |
| 2020-01-16 | Add all active committers in the relevant section above. |
| 2018-11-24 | Ask root for the creation of committers' accounts in LDAP. |

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
