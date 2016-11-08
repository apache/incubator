<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform' version='1.0'
                xmlns:redirect="http://xml.apache.org/xalan/redirect"
                extension-element-prefixes="redirect">
    <xsl:output method='text' indent='no' encoding='utf-8'/>
            
<!-- 
   Process podlings.xml to produce CSV lists for the podlings in each state.
   Output is written to the files {$status}.txt, e.g.
   current.txt
   graduated.txt
   retired.txt
   Also creates a summary of all podlings in
   podling.txt
-->

<!-- where to store the output files (usually target/) -->
<xsl:param name="outputdir"/>

<xsl:template match='podlings'>
    <xsl:call-template name="summary">
        <xsl:with-param name="status" select="'graduated'"/>
    </xsl:call-template>
    <xsl:call-template name="summary">
        <xsl:with-param name="status" select="'retired'"/>
    </xsl:call-template>
    <xsl:call-template name="summary">
        <xsl:with-param name="status" select="'current'"/>
    </xsl:call-template>
    <xsl:call-template name="summary">
        <xsl:with-param name="status" select="'*'"/>
        <xsl:with-param name="filename" select="'podlings'"/>
    </xsl:call-template>
</xsl:template>

<xsl:template name="summary">
    <xsl:param name='status'/>
    <xsl:param name='filename' select="$status"/>
    <redirect:write file="{$outputdir}{$filename}.txt">
        <xsl:choose>
            <xsl:when test="$status='*'">
                <xsl:apply-templates select="podling">
                    <xsl:sort select='@resource'/>
                </xsl:apply-templates>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="podling[@status=$status]">
                    <xsl:sort select='@resource'/>
                </xsl:apply-templates>
            </xsl:otherwise>
        </xsl:choose>
    </redirect:write>
</xsl:template>

<xsl:template match='podling'>
    <xsl:value-of select="@resource"/>
    <xsl:text>,</xsl:text>
    <xsl:value-of select="@status"/>
    <xsl:text>,</xsl:text>
    <xsl:value-of select="@enddate"/>
    <xsl:text>,</xsl:text>
    <xsl:choose>
        <xsl:when test="@longname"><xsl:value-of select="@longname"/></xsl:when>
        <xsl:otherwise><xsl:value-of select="@name"/></xsl:otherwise>
    </xsl:choose>
<xsl:text>
</xsl:text>
</xsl:template>

</xsl:stylesheet>
