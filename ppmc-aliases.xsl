<?xml version="1.0" encoding="UTF-8"?>

<!--
    Transform podlings.xml into a list of current podlings' 
    private lists addresses.
    
    Please set Reply-To: general@incubator.apache.org when
    writing to all PMCs, if your message can be public.
 -->

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fo="http://www.w3.org/1999/XSL/Format"
>

<xsl:template name="newline"><xsl:text>
</xsl:text></xsl:template>

    <xsl:output method="text"/>

    <xsl:template match="text()"/>
    
    <xsl:template match="/">
        <xsl:apply-templates/>
        <xsl:call-template name="newline"/>
    </xsl:template>
    
    <xsl:template match="podling[@status='current']">
        <xsl:value-of select="concat(@resource, '-private@incubator.apache.org,')"/>
    </xsl:template>

</xsl:stylesheet>
