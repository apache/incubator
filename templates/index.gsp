<%include "header.gsp"%>

	<%include "menu.gsp"%>

<div class="page-header">
    <h1>${content.title}</h1>
</div>
Days Between:
${content.body}
<br />
<br />
<ul>
<%
	def rootNode = new groovy.util.XmlSlurper().parse(new java.io.File("pages/podlings.xml"))
%>
<%rootNode.children().each {podling -> %>
<li>${podling.@name}</li>
<%}%>
</ul>
<%include "footer.gsp"%>
