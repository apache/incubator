<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0"
                xmlns:Atom="http://www.w3.org/2005/Atom"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
                xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" 
                xmlns:doap="http://usefulinc.com/ns/doap#"
                xmlns:asfext="http://projects.apache.org/ns/asfext#"
                >

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="document"/>
  </xsl:template>

  <xsl:template match="document">
<rdf:RDF>
  <Project>
    <license rdf:resource="http://usefulinc.com/doap/licenses/asl20" />
    <asfext:pmc rdf:resource="http://incubator.apache.org" />
    <shortdesc>This project is under incubation.</shortdesc>
    <xsl:apply-templates select="body"/>
  </Project>
</rdf:RDF>
  </xsl:template>

  <xsl:template match="body">
    <xsl:apply-templates select="section"/>
  </xsl:template>

  <xsl:template match="section">
    <xsl:choose>
      <xsl:when test="@id = 'Description'">
    <description><xsl:value-of select="p"/></description>
      </xsl:when>
      <xsl:when test="contains(@id, 'Project+Incubation')">
    <name>
      <xsl:text>Apache </xsl:text>
      <xsl:value-of select="substring-before(title, ' Project')"/>
    </name>
      </xsl:when>
      <xsl:when test="contains(@id, 'Project+info')">
        <xsl:apply-templates select="table"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="table">
    <xsl:apply-templates select="tr"/>
  </xsl:template>

  <xsl:template match="tr">
    <xsl:param name="type">
      <xsl:apply-templates select="." mode="findType"/>
    </xsl:param>

    <xsl:choose>
      <xsl:when test="contains($type, 'Website')">
        <xsl:if test="contains(td[2], 'www')">
    <homepage><xsl:value-of select="td[3]"/></homepage>
        </xsl:if>
      </xsl:when>
      <xsl:when test="contains($type, 'Source code')">
    <repository>
      <SVNRepository>
        <location>
          <xsl:attribute name="rdf:resource">
            <xsl:value-of select="td[3]"/>
          </xsl:attribute>
        </location>
      </SVNRepository>
    </repository>
      </xsl:when>
      <xsl:when test="contains($type, 'Mailing list')">
    <mailing-list>
      <xsl:attribute name="rdf:resource">
        <xsl:value-of select="td[3]"/>
      </xsl:attribute>
    </mailing-list>
      </xsl:when>
      <xsl:when test="contains($type, 'Bug tracking')">
    <bug-database>
      <xsl:attribute name="rdf:resource">
        <xsl:value-of select="td[3]"/>
      </xsl:attribute>
    </bug-database>
      </xsl:when>
    </xsl:choose>
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

  <xsl:template select="*|text()"/>
</xsl:stylesheet>
