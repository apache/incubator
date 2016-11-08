<?xml version='1.0'?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  
  http://www.apache.org/licenses/LICENSE-2.0
  
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method='text' encoding='iso-8859-1' />

  <xsl:template match='changes'>
Audit Report: <xsl:value-of select='@from' /> -> <xsl:value-of select='@to' />
======================================
<xsl:choose>
  <xsl:when test='count(descendant::added/document) + count(descendant::modified/document) + count(descendant::missing/document) > 0 '>
 * <xsl:value-of select='count(descendant::added/document)'/> files were added
 * <xsl:value-of select='count(descendant::modified/document)'/> files were modified
 * <xsl:value-of select='count(descendant::missing/document)'/> files were deleted
 
For details see http://incubator.apache.org/audit/changes-<xsl:value-of select='@to' />.html
 </xsl:when>
  <xsl:otherwise>
Move along! Nothing to see here!
  </xsl:otherwise>
</xsl:choose>
  </xsl:template>
</xsl:stylesheet>
