<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License. 
-->
<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform' version='1.0'>

<xsl:output method='text' indent='no' encoding='utf-8'/>

<!--
 -->

<xsl:template match="text()"/>

<xsl:template match='podlings'>
    <xsl:text>(Generated file. Do not edit. See http://incubator.apache.org/guides/mentor.html#Overview)
</xsl:text>
    <xsl:text>
* Monthly (normally for the first three months)
</xsl:text>
    <xsl:apply-templates select='podling[@status="current"]/reporting[@monthly = "true"]'>
        <xsl:with-param name="monthly" select="'true'"/>
    </xsl:apply-templates>

    <xsl:text>* January, April, July, October
</xsl:text>
    <xsl:apply-templates select='podling[@status="current"]/reporting[@group = "1"]'/>

    <xsl:text>* February, May, August, November
</xsl:text>
    <xsl:apply-templates select='podling[@status="current"]/reporting[@group = "2"]'/>

    <xsl:text>* March, June, September, December
</xsl:text>
    <xsl:apply-templates select='podling[@status="current"]/reporting[@group = "3"]'/>

</xsl:template>

<xsl:template match='reporting'>
    <xsl:param name='monthly'/>
    <xsl:text>   </xsl:text>
    <xsl:value-of select="../@name"></xsl:value-of>
    <xsl:if test="$monthly = 'true'">
        <xsl:text> (</xsl:text>
        <xsl:value-of select="text()"/>
        <xsl:text>)</xsl:text>
    </xsl:if>
    <xsl:text>
</xsl:text>
</xsl:template>

</xsl:stylesheet>
