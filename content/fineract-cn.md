Title: Fineract CN Codebase Intellectual Property (IP) Clearance Status


Fineract CN is a cloud-native, microservice-based rewrite of Fineract. It also includes a UI. The microservices and their libraries and integration tests are Spring-based Java code spread across 33 code repositories. The UI is a single repository containing Angular-based JavaScript and Typescript. There is also a Selenium based test-suite for the UI in its own repository. The code was developed at the Mifos Initiative starting at the beginning of 2016, and at Kuelap since March 2017. Kuelap donated the code developed there to the Mifos Initiative. This rearchitecture was originally called Mifos I/O.



- The Fineract project will be responsible for managing this code.


- New gitbox repos have been created for each repository.


- The following people will be managing this contribution:

  - Myrle Krantz (Apache Fineract PMC Chair, and former employee of both the Mifos Initiative and Kuelap.)

  - Ed Cable (Apache Fineract PMC Member, and CEO of the Mifos Initiative which donated the code.)


 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2018-04-09 | The name Fineract already belongs to Apache. |

These repositories were originally under https://github.com/mifosio. They have been deleted there and are now available as a snapshot under https://github.com/mifosio-04-04-2018. The repositories and commit ids there are:
| repository | commit id |
|------------|-----------|
| demo-server | ba85aa29bffcccf4d6c6d39e82a6196f51d2d68c |
| default-setup | 109e641787d06edad3d8147fcee8af86f6a1eb0b |
| accounting | 2e4730ce2e66f469ea409223a34b1133ca71e8ce |
| fims-e2e | 8821edd800a28f06bae8260e1fe7ebe49238095c |
| fims-web-app | c97119c5e63c038eed11ad32e16b490189f66049 |
| portfolio | d4fb74c2e94d95f02f51c51d534d03b6fc88be89 |
| deposit-account-management | 9f00a397e08d46f553816910b503e7283ba3bd21 |
| customer | 3962e1885372803d9af814376e8fd905b9ba98a8 |
| teller | b67978315835b8c90c8e6dafaea6580d808a1734 |
| cheques | 6efef67d3f49bdc258cf5265c292ced72ee21c15 |
| payroll | 8405db37c70093c36b0ddffc744b6cf54f4853cc |
| reporting | de1fa388c9935299c8e35a009647c9e8065a455c |
| office | 12e26137ad24b94c1e6504d2de37022040ddae5e |
| rhythm | 0abeb5819a1f67c1aac403d3a632bb0f6f25b18a |
| provisioner | d5e8876d902bcb0f6e7041a2e6454c351e5fef6b |
| permitted-feign-client | 5dae48798f97d52833de59a241ef2ecce9abdbc7 |
| mariadb | 496703ce8bf876002a482a1d9d06300cc6572e2f |
| api | b00a37ea9849a0db285ede50847e7c8c7031d192 |
| lang | 9cc432c2869bf882545a4052a823b28b9fad5eb8 |
| test-accounting-portfolio | 9e034f7bb6e7fd6e80c98b9f754f14c5ff63df34 |
| identity | 2b8d42744cf451221aefbd98e30b8d0da7e8b890 |
| test-provisioner-identity-rhythm-portfolio-accounting | 4e72a7fa8f4a59d93a6849f35daafb6575aebb57 |
| anubis | 5f919f4c1f03d06ed36d3adf5dbe17e950e048a6 |
| template | 08f84198fe12b8b7547ef6c104a3be23558278be |
| test | 3f53d9d01df04791da51a46cb3460971dcb58d7a |
| cassandra | 9b07e76645a89222986c8038afeb68a9b720d4ac |
| command | 31e95658a7487c31eacd839480b32677581f8912 |
| async | a28cd1ed14b3a70d0a5f3ccfba2710c6623bf0bf |
| service-starter | 008380d4b14540c2833b3eaecda42f5e0db95eab |
| crypto | 09e3e610fbf62f3a782331423c03aec3b969092c |
| test-provisioner-identity-organization | 330aee5649d8176e10f78795344fe23eb21a3e8f |
| group | c759a24270439822653b38ce01937c7899e3de32 |
| data-jpa | b78dadec2e481c3eb51184e85eeac0270d4a979e |



## Copyright {#Copyright}

| date | item |
|------|------|
| 2017-11-06 | The software grant agreement was filed by the Mifos Initiative and acknowledged by the secretary. https://lists.apache.org/thread.html/5ea4cc5f15e003238ce7d72094c694545ee9f2621b4a499d4aeb1e4e@%3Cprivate.fineract.apache.org%3E |
| 2018-03-16 | The last of the changes to reflect the new ASF copyright were completed. https://lists.apache.org/thread.html/df158fe2bcfb08db24bc3b97b3e863dcc2907063c342445680b29a5c@%3Cdev.fineract.apache.org%3E |

Name recorded for software grant: _https://github.com/mifosio from the Mifos Initiative_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



-  _Mifos Initiative_ 

| date | item |
|------|------|
| 2018-02-19 | Active committers have signed an ICLA. Last one was here: https://lists.apache.org/thread.html/79a0274f1f2749160480d257b344e6681db80ba3d7a5cee6e5453355@%3Cprivate.fineract.apache.org%3E |
| 2018-04-09 | Committers have been reminded that they are responsible for ensuring that a Corporate CLA is recorded if such is required. https://lists.apache.org/thread.html/4e64b77adab29d4238883342a985cf8bbb454b4dd0dbc75ab1002fb8@%3Cdev.fineract.apache.org%3E |
| 2018-04-18 | Five files in service-starter (in package org.apache.fineract.cn.test.servicestarter.aether) are copied from an eclipse-licensed sample project. All other code is original code submitted to the Mifos Initiative by its original authors. |
| 2018-04-18 | There are currently three dependencies with Category X licenses (embedded MariaDB for testing, MariaDB JDBC driver for accessing MySQL database, Hibernate JPA). 'Blocker' JIRA tickets have been written to describe the replacement of those dependencies with alternatives: FINCN-26, FINCN-27, FINCN-2. |

# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



-  _Two thirds of the committers at the time voted to accept the code donation: https://lists.apache.org/thread.html/8a791e91aa1295c84cd51f0429af2fcdada7db57fdb65b4185ea5fc0@%3Cdev.fineract.apache.org%3E_ 
