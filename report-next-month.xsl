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
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:datetime="http://exslt.org/dates-and-times">

<!-- basic html rendering of the podlings.xml file showing podling reporting next month 
     use exslt datetime function to determine the current month -->

<xsl:output method="html" indent="yes" encoding="UTF-8" omit-xml-declaration="yes"/>

<xsl:template match="/">
  <xsl:variable name="thisMonth" select="datetime:monthName()"/>
  <xsl:variable name="nextMonthGroup">
    <xsl:choose>
      <xsl:when test="$thisMonth = 'January' or $thisMonth = 'April' or $thisMonth = 'July' or $thisMonth = 'October'">2</xsl:when>
      <xsl:when test="$thisMonth = 'February' or $thisMonth = 'May' or $thisMonth = 'August' or $thisMonth = 'November'">3</xsl:when>
      <xsl:when test="$thisMonth = 'March' or $thisMonth = 'June' or $thisMonth = 'September' or $thisMonth = 'December'">1</xsl:when>
    </xsl:choose>
  </xsl:variable>
  <xsl:variable name="nextMonth">
    <xsl:choose>
      <xsl:when test="$thisMonth = 'January'">February</xsl:when>
      <xsl:when test="$thisMonth = 'February'">March</xsl:when>
      <xsl:when test="$thisMonth = 'March'">April</xsl:when>
      <xsl:when test="$thisMonth = 'April'">May</xsl:when>
      <xsl:when test="$thisMonth = 'May'">June</xsl:when>
      <xsl:when test="$thisMonth = 'June'">July</xsl:when>
      <xsl:when test="$thisMonth = 'July'">August</xsl:when>
      <xsl:when test="$thisMonth = 'August'">September</xsl:when>
      <xsl:when test="$thisMonth = 'September'">October</xsl:when>
      <xsl:when test="$thisMonth = 'October'">November</xsl:when>
      <xsl:when test="$thisMonth = 'November'">December</xsl:when>
      <xsl:when test="$thisMonth = 'December'">January</xsl:when>
    </xsl:choose>
  </xsl:variable>

  <html>
    <head>
      <title>Apache Incubator Podlings needing to prepare report for <xsl:value-of select="$nextMonth"/></title>
      <link rel="stylesheet" href="http://incubator.apache.org/style/bootstrap-1-3-0-min.css" type="text/css" />
      <link rel="stylesheet" href="http://incubator.apache.org/style/style.css" type="text/css" />
      
      <style type="text/css">
	body { 
	margin-left: 1em;
	}
	.podlings { 
	margin-top: 1em; 
	display:block;
	float:none;
	text-align:left;
	margin-left:200px;
	}
	.podling { 
	margin-left: 1em; 
	}
	.podling h2 { 
	margin-left: -1em; 
	}
	.error { 
	color:red; 
	}

	nav {
	background-color: #FFFFFF;
	border: 1px solid #1178C2;
	box-shadow: 5px 5px 2px #888;
	border-radius: 0.8em 0.8em 0.8em 0.8em;
	padding: 5px 5px 10px;
	margin-bottom: 10px;
	float: left;
	text-align: left;
	width: 150px;
	margin-left:1%;
	background-color: #D1C7C7;
	position: fixed;
	}

	nav ul {
	border-top: 1px solid #E7E2D7;
	list-style: none outside none;
	margin: 14px 0;
	padding: 0;
	}
	nav li {
	list-style: none outside none;
	margin: 0;
	padding: 0;
	}
	nav li a:link, nav li a:visited {
	border-bottom: 1px solid #E7E2D7;
	float: left;
	padding: 3px 1%;
	width: 96%;
	color: black;
	}
	nav li a:hover {
	background: none repeat scroll 0 0 #F2F1EC;
	}
      </style>
    </head>
    <body>
      <h1><a href="http://incubator.apache.org">Apache Incubator</a> Podlings needing to prepare report for <xsl:value-of select="$nextMonth"/></h1>
      <div style="text-align:right;"><i>Generated on <xsl:value-of select="datetime:date-time()"/></i></div>
      <nav>
	<ul>
	<xsl:for-each select="podlings/podling[@status = 'current']">
	  <xsl:if test="reporting/@group = $nextMonthGroup or reporting/@monthly = 'true'">
	    <li>
	      <a href="#{@resource}"><xsl:value-of select="@name"/><xsl:if test="reporting/@monthly = 'true'"> (starting)</xsl:if></a>
	    </li>
	  </xsl:if>
	</xsl:for-each>
	</ul>
      </nav>
      <div class="podlings">
	<xsl:for-each select="podlings/podling[@status = 'current']">
	  <xsl:if test="reporting/@group = $nextMonthGroup or reporting/@monthly = 'true'">
	    <xsl:apply-templates select="."/>
	  </xsl:if>
	</xsl:for-each>
      </div>
    </body>
  </html>
</xsl:template>

<xsl:template match="podling">
  <div class="podling">
    <a name="{@resource}"/>
    <h2>
      <a href="{concat('http://incubator.apache.org/projects/', @resource, '.html')}">
	<xsl:value-of select="@name"/>
      </a> 
      <xsl:if test="reporting/@monthly = 'true'"> (starting)</xsl:if>
    </h2>
    <p class="description"><xsl:value-of select="description"/></p>
    <p class="dates">
      Entered incubation <xsl:value-of select="@startdate"/>
      <xsl:if test="normalize-space(@enddate)">
	, graduated <xsl:value-of select="@enddate"/>
      </xsl:if> 
      .
    </p>

    <h3>Champion</h3>
    <xsl:apply-templates select="." mode="champion"/>

    <h3>Mentors</h3>
    <ul class="mentors">
      <xsl:apply-templates select="mentors"/>
    </ul>
    
    <h3>Reporting Schedule</h3>
    <p>
      Group <xsl:value-of select="reporting/@group"/><xsl:text> = </xsl:text>
      <xsl:choose>
	<xsl:when test="reporting/@group = '1'">January, April, July, October</xsl:when>
	<xsl:when test="reporting/@group = '2'">February, May, August, November</xsl:when>
	<xsl:when test="reporting/@group = '3'">March, June, September, December</xsl:when>
	<xsl:otherwise>Unknown group</xsl:otherwise>
      </xsl:choose>
      <xsl:if test="reporting/@monthly = 'true'"> (Currently monthly: <xsl:value-of select="reporting"/>)</xsl:if>
    </p>
  </div>
</xsl:template>

<xsl:template match="podling[champion]" mode="champion">
  <p><xsl:value-of select="champion"/></p>
</xsl:template>

<xsl:template match="podling" mode="champion">
  <xsl:if test="@status='current'">
    <p class="error">MISSING</p>
  </xsl:if>
</xsl:template>

<xsl:template match="mentor">
  <li><xsl:value-of select="."/></li>
</xsl:template>

</xsl:stylesheet>
