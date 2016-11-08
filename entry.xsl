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
    <xsl:text># podlings entered incubation
</xsl:text>
    <xsl:variable name="total">
        <xsl:value-of select="count(podling)+1"/>
    </xsl:variable>
    <xsl:for-each select="podling">
        <xsl:sort select="@startdate" order="descending"/>
        <xsl:sort select="@name" order="descending"/>
        <xsl:value-of select="@startdate"/>
        <!-- If day is missing, assume 01 -->
        <xsl:if test="string-length(@startdate)=7"><xsl:text>-01</xsl:text></xsl:if>
        <xsl:text>,"</xsl:text><xsl:value-of select="@name"/><xsl:text>",</xsl:text>
        <xsl:value-of select="$total - position()"/>
        <xsl:text>
</xsl:text>
    </xsl:for-each>

</xsl:template>

</xsl:stylesheet>
