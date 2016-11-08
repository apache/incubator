<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                >

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="document"/>
  </xsl:template>

  <xsl:template match="document">
<incubatorNews>
    <xsl:apply-templates select="body"/>
</incubatorNews>
  </xsl:template>

  <xsl:template match="body">
    <xsl:apply-templates select="section"/>
  </xsl:template>

  <xsl:template match="section">
    <xsl:if test="contains(@id, 'News')">
      <xsl:apply-templates select="ul"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul">
    <xsl:apply-templates select="li"/>
  </xsl:template>

  <xsl:template match="li">
    <xsl:if test="not(contains(., 'none yet'))">
  <newsItem>
    <date><xsl:value-of select="substring-before(., ' - ')"/></date>
    <text><xsl:value-of select="substring-after(., ' - ')"/></text>
  </newsItem>
    </xsl:if>
  </xsl:template>

  <xsl:template select="*|text()" />
</xsl:stylesheet>
