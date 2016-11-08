<?xml version='1.0'?>
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

<!-- 
   Process podlings.xml to produce target/project-menu.ent from current entries.

   Assumes the format is:
   
   <podling name='Name' status='current' resource='name'>

 -->
<xsl:stylesheet 
            xmlns:xsl='http://www.w3.org/1999/XSL/Transform'
            version='1.0'>
    <xsl:output 
            method='xml' 
            indent='no'
            encoding='UTF-8'/>

<xsl:param name="CELLS_PER_LINE" select="6"/>

    <xsl:template match='podlings'>
      <table>
<xsl:text>
</xsl:text>
        <xsl:apply-templates select="podling[@status = 'current']">
            <xsl:sort select='@name'/>
        </xsl:apply-templates>
        <xsl:call-template name="fill-blank-td"/>
        <xsl:text disable-output-escaping="yes">
&lt;/tr>
</xsl:text>
      </table>
    </xsl:template>
    <xsl:template name="fill-blank-td">
        <xsl:param name="num"><xsl:value-of select="count(podling[@status = 'current']) mod $CELLS_PER_LINE"/></xsl:param>
        <xsl:if test="$num &lt; $CELLS_PER_LINE and $num &gt; 0">
          <td></td>
            <xsl:call-template name="fill-blank-td">
                <xsl:with-param name="num">
                    <xsl:value-of select="$num + 1"/>
                </xsl:with-param>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>
    <xsl:template match='podling'>
        <xsl:if test="position() mod $CELLS_PER_LINE = 1">
        <xsl:if test="position() > 1">
        <xsl:text disable-output-escaping="yes">&lt;/tr>
</xsl:text>
        </xsl:if>
        <xsl:text disable-output-escaping="yes">&lt;tr>
</xsl:text>
        </xsl:if>
      <!-- copy original spacing (could be removed) -->
      <xsl:text>      </xsl:text>
        <td><xsl:element name='a'>
                <xsl:attribute name='href'><xsl:value-of select="concat('projects/', @resource, '.html')"/></xsl:attribute>
                <xsl:attribute name="title"><xsl:value-of select="description"/></xsl:attribute>
                <xsl:value-of select='@name'/>
            </xsl:element>
        </td>
<!-- Add EOL after each entry -->
<xsl:text>
</xsl:text>
    </xsl:template>
</xsl:stylesheet>
