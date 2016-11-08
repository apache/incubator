<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                >

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="document"/>
  </xsl:template>

  <xsl:template match="document">
<incubatorProgress>
    <xsl:apply-templates select="body"/>
</incubatorProgress>
  </xsl:template>

  <xsl:template match="body">
    <xsl:apply-templates select="section"/>
  </xsl:template>

  <xsl:template match="body/section">
    <xsl:if test="contains(@id, 'Incubation+work+items')">
      <xsl:apply-templates select="section"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="section/section">
  <incubationStage>
    <title><xsl:value-of select="title"/></title>
    <xsl:apply-templates select="section"/>
  </incubationStage>
  </xsl:template>

  <xsl:template match="section/section/section">
    <workSection>
      <title><xsl:value-of select="title"/></title>
      <xsl:apply-templates select="table|ul"/>
    </workSection>
  </xsl:template>

  <xsl:template match="table">
    <xsl:choose>
      <xsl:when test="contains(tr[1]/th[1], 'status')">
        <xsl:apply-templates select="tr" mode="status"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates select="tr" mode="dates"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="tr" mode="dates">
    <xsl:if test="td">
      <workItem>
        <desc><xsl:value-of select="td[2]"/></desc>
      <xsl:if test="contains(td[1], '-')">
        <date>
          <xsl:if test="not(contains(td[1], '..'))">
            <xsl:value-of select="td[1]"/>
          </xsl:if>
        </date>
      </xsl:if>
      </workItem>
    </xsl:if>
  </xsl:template>

  <xsl:template match="tr" mode="status">
    <xsl:if test="td">
      <workItem>
        <desc><xsl:value-of select="td[2]"/></desc>
        <status>
          <xsl:if test="contains(td[1], 'DONE')">
            DONE
          </xsl:if>
        </status>
      </workItem>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul">
    <xsl:apply-templates select="li"/>
  </xsl:template>

  <xsl:template match="li">
      <verificationItem><xsl:value-of select="."/></verificationItem>
  </xsl:template>

  <xsl:template select="*|text()" />
</xsl:stylesheet>
