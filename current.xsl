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
<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform'
                xmlns:exsl="http://exslt.org/common"
                version='1.0'>

<xsl:output method='text' indent='no' encoding='utf-8'/>

<xsl:template match='podlings'>
    <xsl:text># total in active incubation
</xsl:text>

    <!-- Generate document containing list of start and end dates -->
    <xsl:variable name="workDoc">
        <!-- Generate start date entries -->
        <xsl:for-each select="podling">
            <xsl:element name="entry">
                <xsl:attribute name="type">1</xsl:attribute>
                <xsl:attribute name="date">
                    <xsl:value-of select="@startdate"/>
                    <xsl:if test="string-length(@startdate)=7"><xsl:text>-01</xsl:text></xsl:if>
                </xsl:attribute>
                <xsl:attribute name="name">
                    <xsl:value-of select="@name"/>
                </xsl:attribute>
            </xsl:element>
        </xsl:for-each>
        <!-- Generate end date entries -->
        <xsl:for-each select="podling[@enddate]">
            <xsl:element name="entry">
                <xsl:attribute name="type">2</xsl:attribute>
                <xsl:attribute name="date">
                    <xsl:value-of select="@enddate"/>
                    <!-- If day is missing, assume 01 -->
                    <xsl:if test="string-length(@enddate)=7"><xsl:text>-01</xsl:text></xsl:if>
                </xsl:attribute>
                <xsl:attribute name="name">
                    <xsl:value-of select="@name"/>
                </xsl:attribute>
             </xsl:element>
        </xsl:for-each>
    </xsl:variable>

    <!-- Sort the list by date then type -->
    <xsl:variable name="sortedDoc">
        <xsl:for-each select="exsl:node-set($workDoc)/entry">
            <xsl:sort select="@date"/>
            <xsl:sort select="@type"/>
            <xsl:copy-of select="."/>
        </xsl:for-each>
    </xsl:variable>

    <!-- extract the sorted data -->
    <xsl:for-each select="exsl:node-set($sortedDoc)/entry">
        <!-- don't process if there is a following entry with the same date -->
        <xsl:if test="not(following-sibling::entry/@date = @date)">
            <xsl:value-of select="@date"/>
            <xsl:text>,</xsl:text>
            <!-- 
                total active = entries - exits
                In theory, entries and exits should be available using:
                    xsl:number count="entry[@type = 1|2]
                However, xsl:number does not return anything unless the preceeding entry elements have the same type.
                [This may be a bug?]
                So we use the fact that entries + exits = position, i.e.
                total = entries - (position - entries) = entries * 2 - position
                total = (position - exits) - exits = position - exits * 2 
            -->
            <xsl:if test="@type = 1">
                <xsl:variable name="entries">
                    <xsl:number count="entry[@type = 1]"/>
                </xsl:variable>
                <xsl:value-of select="$entries * 2 - position()"/>
            </xsl:if>
            <xsl:if test="@type = 2">
                <xsl:variable name="exits">
                    <xsl:number count="entry[@type = 2]"/>
                </xsl:variable>
                <xsl:value-of select="position() - $exits * 2"/>
            </xsl:if>
            <xsl:text>
</xsl:text>
        </xsl:if>
    </xsl:for-each>
</xsl:template>

</xsl:stylesheet>
