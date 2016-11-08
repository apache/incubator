<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                >

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="document"/>
  </xsl:template>

  <xsl:template match="document">
<incubatorPeople>
    <xsl:apply-templates select="body"/>
</incubatorPeople>
  </xsl:template>

  <xsl:template match="body">
    <xsl:apply-templates select="section"/>
  </xsl:template>

  <xsl:template match="section">
    <xsl:if test="contains(@id, 'Project+info')">
      <xsl:apply-templates select="table"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="table">
  <Mentors>
    <xsl:apply-templates select="tr" mode="Mentors"/>
  </Mentors>
  <Committers>
    <xsl:apply-templates select="tr" mode="Committers"/>
  </Committers>
  </xsl:template>

  <xsl:template match="tr" mode="Mentors">
    <xsl:param name="type">
      <xsl:apply-templates select="." mode="findType"/>
    </xsl:param>

    <xsl:if test="contains($type, 'Mentors')">
      <xsl:apply-templates select="." mode="addPerson"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="tr" mode="Committers">
    <xsl:param name="type">
      <xsl:apply-templates select="." mode="findType"/>
    </xsl:param>

    <xsl:if test="contains($type, 'Committers')">
      <xsl:apply-templates select="." mode="addPerson"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="tr" mode="addPerson">
    <person>
    <xsl:if test="not(contains(td[2], '.'))">
      <availId><xsl:value-of select="td[2]"/></availId>
    </xsl:if>
      <name><xsl:value-of select="td[3]"/></name>
    </person>
  </xsl:template>

  <xsl:template match="tr" mode="findType">
    <xsl:choose>
      <xsl:when test="contains(td[1], '.')">
        <xsl:apply-templates select="preceding-sibling::tr[1]" mode="findType"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="td[1]"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template select="*|text()" />
</xsl:stylesheet>
