<% include "header.gsp" %>

<% include "menu.gsp" %>

<div class="incubator-page-header">
    <h1>${content.title}</h1>
</div>

${content.body}

<b>Our Current Podlings:</b>
<%
    def source = new java.net.URL("http://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings.xml")
    def rootNode = new groovy.util.XmlSlurper(false, false, true).parseText(source.text)
%>
<div class="container-fluid">
    <div class="row">
        <% rootNode.children().each { podling ->
            if (podling.@status == 'current') {
        %>
        <div class="col-md-2"><a href="/projects/${podling.@resource}.html">${podling.@name}</a></div>
        <%
                    }
            } %>
    </div>
</div>
<br/><br/>
<div class="container-fluid">
    <div class="row">
        <div class="col-lg-3 text-center"><a href="/projects/#current">List of Current Podlings</a></div>
        <div class="col-lg-3 text-center"><a href="/projects/#graduated">Graduated Projects</a></div>
        <div class="col-lg-3 text-center"><a href="/projects/#retired">Retired Podlings</a></div>
        <div class="col-lg-3 text-center"><a href="/clutch/">Current Clutch Analysis</a></div>
    </div>
</div>
<br/><br/>
<% include "footer.gsp" %>
