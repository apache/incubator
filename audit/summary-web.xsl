<?xml version='1.0'?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  
  http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method='xml' indent='yes' encoding='UTF-8' />

  <xsl:template match='changes'>
    <xsl:comment>
      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing,
      software distributed under the License is distributed on an "AS
      IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
      express or implied. See the License for the specific language
      governing permissions and limitations under the License.
    </xsl:comment>
    <document>
      <properties>
        <title>
          Audit Report For
          <xsl:value-of select='@to' />
        </title>
        <atom
          url="http://mail-archives.apache.org/mod_mbox/incubator-general/?format=atom">
          general@incubator.apache.org Archives
        </atom>
        <link href="http://purl.org/DC/elements/1.0/" rel="schema.DC" />
      </properties>
      <body>
        <section id='Overview'>
          <title>Overview</title>
          <p>
            This report audits the changes made from
            <xsl:value-of select='@from' />
            till
            <xsl:value-of select='@to' />
            in:
          </p>
          <ul>
            <li>
              <a href='http://www.apache.org/dist/incubator'>
                www.apache.org/dist/incubator
              </a>
            </li>
            <li>
              <a href='http://archive.apache.org/dist/incubator'>
                archive.apache.org/dist/incubator
              </a>
            </li>
          </ul>
        </section>
        <section id='summary'><title>Summary</title>
          <ul>
          <li><xsl:value-of select='count(descendant::added/document)'/> files were <a href='#added'>added</a></li>
          <li><xsl:value-of select='count(descendant::modified/document)'/> files were <a href='#modified'>modified</a></li>
          <li><xsl:value-of select='count(descendant::missing/document)'/> files were <a href='#deleted'>deleted</a></li>
          </ul>
        </section>
        <section id='details'><title>Details</title>
          <section id='added'><title>Modified</title>
            <ul>
              <xsl:for-each select='modified/document'>
                <xsl:sort
                  select="@dir"
                  data-type = "text"
                  order = "ascending"
                  case-order = "lower-first"/>
                <xsl:sort
                  select="@name"
                  data-type = "text"
                  order = "ascending"
                  case-order = "lower-first"/>
                <li>
                <strong><xsl:value-of select="@name"/></strong> in <xsl:value-of select="@dir"/>
                </li>
              </xsl:for-each>
            </ul>
          </section>
          <section id='added'><title>Added</title>
            <ul>
              <xsl:for-each select='added/document'>
                <xsl:sort
                  select="@dir"
                  data-type = "text"
                  order = "ascending"
                    case-order = "lower-first"/>
                <xsl:sort
                  select="@name"
                  data-type = "text"
                  order = "ascending"
                  case-order = "lower-first"/>
                <li>
                <strong><xsl:value-of select="@name"/></strong> in <xsl:value-of select="@dir"/>
                </li>
              </xsl:for-each>
            </ul>
          </section>
          <section id='deleted'><title>Deleted</title>
            <ul>
              <xsl:for-each select='missing/document'>
              <xsl:sort
                  select="@dir"
                  data-type = "text"
                  order = "ascending"
                  case-order = "lower-first"/>
             <xsl:sort
                  select="@name"
                  data-type = "text"
                  order = "ascending"
                  case-order = "lower-first"/>
                <li>
                <strong><xsl:value-of select="@name"/></strong> in <xsl:value-of select="@dir"/>
                </li>
              </xsl:for-each>
            </ul>
          </section>
        </section>
      </body>
    </document>
  </xsl:template>
</xsl:stylesheet>
