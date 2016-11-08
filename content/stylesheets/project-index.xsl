<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform' version='1.0'
                xmlns:redirect="http://xml.apache.org/xalan/redirect"
                extension-element-prefixes="redirect">
    <xsl:output method='xml' indent='yes' encoding='utf-8'/>
            
<!-- 
   Process podlings.xml to produce tables for the podlings in each state.
   Output is written to the files {$outputdir}{$status}.ent, e.g.
   target/current.ent
   target/graduated.ent
   target/retired.ent
   
   TODO: remove output spacing, probably no longer necessary
 -->

<!-- where to store the output files (usually target/) -->
<xsl:param name="outputdir"/>

<xsl:template match='podlings'>
    <xsl:call-template name="section">
        <xsl:with-param name="status" select="'current'"/>
    </xsl:call-template>
    <xsl:call-template name="section">
        <xsl:with-param name="status" select="'graduated'"/>
        <xsl:with-param name="enddate" select="'true'"/>
    </xsl:call-template>
    <xsl:call-template name="section">
        <xsl:with-param name="status" select="'retired'"/>
        <xsl:with-param name="enddate" select="'true'"/>
    </xsl:call-template>
</xsl:template>

<xsl:template name="section">
    <xsl:param name='status'/>
    <xsl:param name='enddate'/>
      <redirect:write file="{$outputdir}{$status}.ent">
      <xsl:element name="table">
        <tr>
          <th>Project</th>
          <th>Description</th>
          <xsl:choose>
            <xsl:when test="$status = 'current'"><th>Sponsor (Champion)</th></xsl:when>
            <xsl:otherwise><th>Apache Sponsor</th></xsl:otherwise>
          </xsl:choose>
          <th>Mentors</th>
          <th>Start Date</th>
          <xsl:if test="$enddate = 'true'"><th>End Date</th></xsl:if>
        </tr>
        <xsl:apply-templates select="podling[@status = $status]">
            <xsl:sort select='@name'/>
            <xsl:with-param name="enddate" select="$enddate"/>
            <xsl:with-param name="status" select="$status"/>
        </xsl:apply-templates>
<xsl:text>
      </xsl:text>
      </xsl:element>
<xsl:text>
    </xsl:text>
    </redirect:write>
    </xsl:template>    

    <xsl:template match='podling'>
        <xsl:param name='enddate'/>
        <xsl:param name='status'/>
<xsl:text>
        </xsl:text>
        <tr>
          <xsl:attribute name="id">
            <xsl:value-of select="translate(translate(normalize-space(@name), ' ', ''), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"/>
          </xsl:attribute>
<xsl:text>
          </xsl:text>
          <td>
<xsl:text>
            </xsl:text>
            <xsl:element name="a">
                <xsl:attribute name="href">
                    <xsl:value-of select="concat('../projects/', @resource, '.html')"/>
                </xsl:attribute>
                <xsl:choose>
                    <xsl:when test="@longname"><xsl:value-of select="@longname"/></xsl:when>
                    <xsl:otherwise><xsl:value-of select="@name"/></xsl:otherwise>
                </xsl:choose>
            </xsl:element>
            <!-- Shorthand for TLP target -->
            <xsl:if test="resolution/@tlp = 'true'">
<xsl:text>
            </xsl:text>
            <hr/>
<xsl:text>
            </xsl:text>
            <xsl:element name="a">
              <xsl:attribute name="href">
                <xsl:value-of select="concat('http://',@resource,'.apache.org/')"/>
              </xsl:attribute>
<xsl:text>
            </xsl:text>
              <img src="../images/redarrow.gif" />
              <xsl:value-of select="@name"/>
<xsl:text>
            </xsl:text>
            </xsl:element>
            </xsl:if>
            <xsl:if test="resolution/@url">
<xsl:text>
            </xsl:text>
            <hr/>
<xsl:text>
            </xsl:text>
            <xsl:element name="a">
              <xsl:attribute name="href">
                <xsl:value-of select="resolution/@url"/>
              </xsl:attribute>
<xsl:text>
            </xsl:text>
              <img src="../images/redarrow.gif" />
              <xsl:value-of select="resolution/@link | @name"/>
<xsl:text>
            </xsl:text>
            </xsl:element>
            </xsl:if>
<xsl:text>
          </xsl:text>
          </td>
<xsl:text>
          </xsl:text>
          <td>
          <xsl:value-of select="description"/>
          <xsl:if test="resolution != ''">
            <hr/>
            <xsl:value-of select="resolution"/>
          </xsl:if>
          </td>
<xsl:text>
          </xsl:text>
          <td><xsl:value-of select="@sponsor"/>
          <xsl:if test="$status = 'current' and champion != ''">
          <xsl:element name="br"/>
          <xsl:text>(</xsl:text>
          <xsl:value-of select="champion"/>
          <xsl:text>)</xsl:text>
          </xsl:if>
          </td>
<xsl:text>
          </xsl:text>
          <td>
          <xsl:call-template name="mentor-list"/>
          </td>
<xsl:text>
          </xsl:text>
          <td><xsl:value-of select="@startdate"/></td>
          <xsl:if test="$enddate = 'true'">
<xsl:text>
          </xsl:text>
              <td>
              <xsl:choose>
                  <xsl:when test="@enddate"><xsl:value-of select="@enddate"/></xsl:when>
                  <xsl:otherwise>?</xsl:otherwise>
              </xsl:choose>
              </td>
          </xsl:if>
<xsl:text>
        </xsl:text>
        </tr>
<!-- Add EOL after each entry -->
<xsl:text>
</xsl:text>
    </xsl:template>

  <xsl:template name="mentor-list">
    <xsl:for-each select="mentors/mentor">
      <xsl:value-of select="." />
      <xsl:if test="position() != last()">
        <xsl:value-of select="', '"/>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
