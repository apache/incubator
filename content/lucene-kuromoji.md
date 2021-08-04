Title: Kuromoji Codebase Intellectual Property (IP) Clearance Status


The project was started in 2010 since we couldn't find any high-quality, actively maintained and easy-to-use Java-based Japanese morphological analyzers, and these become many of our design goals for Kuromoji. Kuromoji also has a segmentation mode that is particularly useful for search, which we hope will interest Apache Lucene and Solr users. Compound-nouns, such as 関西国際空港 (Kansai International Airport) and 日本経済新聞 (Nikkei Newspaper), are segmented as one token with most analyzers. As a result, a search for 空港 (airport) or 新聞 (newspaper) will not give you a for in these words. Kuromoji can segment these words into 関西 国際 空港 and 日本 経済 新聞, which is generally what you would want for search and you'll get a hit. The target was to make sure the technology has a license that makes it compatible with other Apache Software Foundation software to maximize its usefulness. Kuromoji has an Apache License 2.0 and all code is currently owned by Atilika Inc. The software has been developed by Masaru Hasegawa and Christian Moen.



- Which PMC will be responsible for the code: Apache Lucene


- Into which existing project/module: Apache Lucene Java


- Officer or member managing donation: Simon Willnauer

 _Completed tasks are shown by the completion date (YYYY-MM-dd)._ 


# Identify the codebase {#Identify+the+codebase}

| date | item |
|------|------|
| 2011-07-12 | Chistian Moen created https://issues.apache.org/jira/browse/LUCENE-3305, packaged the source with appropriate Apache Headers and uplaoded them to the referenced issue ( kuromoji-solr-0.5.3-asf.tar.gz &amp; kuromoji-0.7.6-asf.tar.gz) |

MD5 sum for donated software:
MD5 (kuromoji-0.7.6-asf.tar.gz) = a84f016bd5162e57423a1da181c25f36


MD5 (kuromoji-solr-0.5.3-asf.tar.gz) = a3e7d5afba64ec0843be6d4dbb95be1c




## Copyright {#Copyright}

| date | item |
|------|------|
| 2011-08-08 | Check and make sure that the papers that transfer rights to the ASF been received. It is only necessary to transfer rights for the package, the core code, and any new code produced by the project. |
| 2011-09-26 | Check and make sure that the files that have been donated have been updated to reflect the new ASF copyright. |

Identify name recorded for software grant: _Kuromoji_ 


## Verify distribution rights {#Verify+distribution+rights}

Corporations and individuals holding existing distribution rights:



- Masaru Hasegawa (original developer)

- Christian Moen (original developer)

| date | item |
|------|------|
| 2011-08-02 | Check that all active committers have a signed CLA on record. |
| 2011-08-02 | Remind active committers that they are responsible for ensuring that a Corporate CLA is recorded if such is required to authorize their contributions under their individual CLA. |
| 2011-08-08 | Check and make sure that for all items included with the distribution that is not under the Apache license, we have the right to combine with Apache-licensed code and redistribute. |
| 2011-09-20 | Check and make sure that all items depended upon by the project is covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms. | The terms of the included IPADIC license has been discussed on LEGAL-97. Apache Lucene is free to use the IPADIC Licensed dictionary files by following the terms and conditions in the license. |

Generally, the result of checking off these items will be a Software Grant, CLA, and Corporate CLA for ASF licensed code, which must have no dependencies upon items whose licenses that are incompatible with the Apache License.


# Organizational acceptance of responsibility for the project {#Organizational+acceptance+of+responsibility+for+the+project}

Related VOTEs:



- The vote on the dev@lucene.apache.org mailing list to accept Kuromoji into the Apache Lucene project passed on 2011-08-11.
