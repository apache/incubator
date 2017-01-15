<%include "header.gsp"%>

	<%include "menu.gsp"%>

<h1>About the Apache Incubator</h1>
The Incubator project is the entry path into The Apache Software Foundation (ASF) for projects and codebases wishing to become part of the Foundation's efforts. All code donations from external organisations and existing external projects wishing to join Apache enter through the Incubator.

The Apache Incubator has two primary goals:
<ul>
    <li>Ensure all donations are in accordance with the ASF <a href="http://www.apache.org/licenses/">legal standards</a></li>
    <li>Develop new communities that adhere to our <a href="http://www.apache.org/foundation/how-it-works.html">guiding principles</a></li>
</ul>
See also the <a href="http://www.youtube.com/watch?v=KopPbWS87fw">Life In The Apache Incubator video</a>, where former Incubator PMC chair Jukka Zitting presents the Incubator, at ApacheCon EU 2012.

<h2>About The Apache Software Foundation</h2>
The Apache Software Foundation provides organizational, legal, and financial support for a broad range of open source software projects. The Foundation provides an established framework for intellectual property and financial contributions that simultaneously limits the potential legal exposure for the contributors. Through a collaborative and meritocratic development process, Apache projects deliver enterprise-grade, freely available software products that attract large communities of users. The pragmatic Apache License makes it easy for all users, commercial and individual, to deploy Apache products.

<br/><br/>
You can find out <a href="http://www.apache.org/foundation/">more about the ASF</a>.
<br/><br/>
<ul>
<%
	def rootNode = new groovy.util.XmlSlurper().parse(new java.io.File("pages/podlings.xml"))
%>
<%rootNode.children().each {podling -> %>
<li>${podling.@name}</li>
<%}%>
</ul>
<%include "footer.gsp"%>
