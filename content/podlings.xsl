<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
>

<!-- basic html rendering of the podlings.xml file -->

<xsl:output method="html" indent="yes" encoding="UTF-8" omit-xml-declaration="yes"/>

<xsl:template match="/">
    <html>
    <head>
        <title>Apache Incubator Podlings</title>
        <link rel="stylesheet" href="http://incubator.apache.org/style/bootstrap-1-3-0-min.css" type="text/css" />
        <link rel="stylesheet" href="http://incubator.apache.org/style/style.css" type="text/css" />
        
        <style type="text/css">
            body { margin-left: 1em; }
            .podlings { margin-top: 1em; }
            .podling { margin-left: 1em; }
            .podling h2 { margin-left: -1em; }
            .error { color:red; }
        </style>
    </head>
    <body>
        <h1><a href="http://incubator.apache.org">Apache Incubator Podlings</a></h1>
        <div>
            Note that the source .xml file might
            contain more details that are not displayed here.
        </div>
        <div class="podlings">
            <xsl:apply-templates/>
        </div>
    </body>
    </html>
</xsl:template>

<xsl:template match="podling">
    <div class="podling">
        <a name="{@resource}"/>
        <h2>
            <a href="{concat('http://incubator.apache.org/', @resource)}">
                <xsl:value-of select="@name"/>
            </a> 
            (<xsl:value-of select="@status"/>)
        </h2>
        <p class="description"><xsl:value-of select="description"/></p>
        <p class="dates">
            Entered incubation <xsl:value-of select="@startdate"/>
            <xsl:if test="normalize-space(@enddate)">
                <xsl:text>, </xsl:text>
                <xsl:value-of select="@status"/><xsl:text> </xsl:text><xsl:value-of select="@enddate"/>
            </xsl:if> 
            <xsl:text>.</xsl:text>
        </p>

        <h3>Champion</h3>
        <xsl:apply-templates select="." mode="champion"/>

        <h3>Mentors</h3>
        <ul class="mentors">
            <xsl:apply-templates select="mentors"/>
        </ul>
        
        <xsl:if test="@status = 'current'">
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
        </xsl:if>
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
