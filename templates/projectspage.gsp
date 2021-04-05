<% include "header.gsp" %>

<% include "menu.gsp" %>

<div class="incubator-page-header">
    <h2>${content.title}</h2>
    <p>These tables are generated from the <span class="code">podlings.xml</span> file.
       Please keep your project metadata up-to-date
       (see <a href="https://incubator.apache.org/guides/mentor.html#initialize_podling_status_page">here</a> and
       <a href="https://incubator.apache.org/guides/website.html#maintaining_status_files">here</a>).
</div>

<div class="container-fluid">
    <div class="row">
        <div class="col-lg-3 text-center"><a href="#current">List of Current Podlings</a></div>
        <div class="col-lg-3 text-center"><a href="#graduated">Graduated Projects</a></div>
        <div class="col-lg-3 text-center"><a href="#retired">Retired Podlings</a></div>
        <div class="col-lg-3 text-center"><a href="/clutch/">Current Clutch Analysis</a></div>
    </div>
</div>
<br/><br/>
<%
    def source = new java.net.URL("http://svn.apache.org/repos/asf/incubator/public/trunk/content/podlings.xml")
    def podlings = new groovy.util.XmlSlurper(false, false, true).parseText(source.text).children()
    def sortedName = { it.@name.text().toLowerCase() } 
%>
<h3 id="current"><img src="/images/redarrow.gif">Current Podlings</h3>
<div class="container-fluid">
    <div class="row">
      <table class="colortable">
	<tr>
	   <th>Project</th>
	   <th>Description</th>
	   <th>Sponsor (Champion)</th>
	   <th>Mentors</th>
	   <th>Aliases</th>
	   <th>Start&nbsp;Date&nbsp;</th>
	</tr>
        <% podlings.toSorted(sortedName).each { podling ->
            if (podling.@status == 'current') {
        %>
        <tr id="${podling.@resource}">
	   <td><a href="/projects/${podling.@resource}.html">${podling.@name}</a></td>
	   <td>${podling.description}</td>
	   <td>${podling.@sponsor}
		<% if ( podling.champion != "" ) { %>
		<br/>(${podling.champion})
		<% } %> 
	   </td>
	   <td><%
		def sep=""
		podling.mentors.children().each { mentor ->
		%>${sep}${mentor}<%
		     	sep=", "
		} %>
	   </td>
	   <td><%
	   	aliases=podling.resourceAliases.replaceAll(",",", ")
		%>${aliases}
	   </td>
	   <td>${podling.@startdate}</td>
	</tr>
        <%
           }
      } %>
      </table>
    </div>
</div>
<h3 id="graduated"><img src="/images/redarrow.gif">Graduated Projects</h3>
<div class="container-fluid">
    <div class="row">
      <table class="colortable">
	<tr>
	   <th>Project</th>
	   <th>Description</th>
	   <th>Apache Sponsor</th>
	   <th>Mentors</th>
	   <th>Aliases</th>
	   <th>Start&nbsp;Date&nbsp;</th>
	   <th>End&nbsp;Date&nbsp;&nbsp;&nbsp;</th>
	</tr>
        <% podlings.toSorted(sortedName).each { podling ->
            if (podling.@status == 'graduated') {
        %>
        <tr id="${podling.@resource}">
	   <td><a href=/projects/${podling.@resource}.html>${podling.@name}</a>
		<% if ( podling.resolution.@tlp == "true" ) { %>
		   <hr>
		   <img src="/images/redarrow.gif"><a href="https://${podling.@resource}.apache.org/">${podling.@name}</a>
		<% } else if ( podling.resolution.@url != "" ) { %>
		   <hr>
		   <img src="/images/redarrow.gif"><a href="${podling.resolution.@url}"><%
		   	if ( podling.resolution.@link != "" ) {
			%>${podling.resolution.@link}</a><% } else { %>${podling.@name} <% }
		} %>
	   </td>
	   <td>${podling.description}
		<% if ( podling.resolution != "" ) { %>
		<hr>
		${podling.resolution}
		<% } %> 
	   </td>
	   <td>${podling.@sponsor}
		<% if ( podling.champion != "" ) { %>
		<br/>(${podling.champion})
		<% } %> 
	   </td>
	   <td><%
		sep=""
		podling.mentors.children().each { mentor ->
		%>${sep}${mentor}<%
		     	sep=", "
		} %>
	   </td>
	   <td><%
	   	aliases=podling.resourceAliases.replaceAll(",",", ")
		%>${aliases}
	   </td>
	   <td>${podling.@startdate}</td>
	   <td>${podling.@enddate}</td>
	</tr>
        <%
           }
      } %>
      </table>
    </div>
</div>
<h3 id="retired"><img src="/images/redarrow.gif">Retired Podlings</h3>
<div class="container-fluid">
    <div class="row">
      <table class="colortable">
	<tr>
	   <th>Project</th>
	   <th>Description</th>
	   <th>Apache Sponsor</th>
	   <th>Mentors</th>
	   <th>Aliases</th>
	   <th>Start&nbsp;Date&nbsp;</th>
	   <th>End&nbsp;Date&nbsp;&nbsp;&nbsp;</th>
	</tr>
        <% podlings.toSorted(sortedName).each { podling ->
            if (podling.@status == 'retired') {
        %>
        <tr id="${podling.@resource}">
	   <td><a href=/projects/${podling.@resource}.html>${podling.@name}</a>
		<% if ( podling.resolution.@url != "" ) { %>
		   <hr>
		   <img src="/images/redarrow.gif"><a href="${podling.resolution.@url}"><%
		   	if ( podling.resolution.@link != "" ) {
			%>${podling.resolution.@link}</a><% } else { %>${podling.@name} <% }
		} %>
	   </td>
	   <td>${podling.description}
		<% if ( podling.resolution != "" ) { %>
		<hr>
		${podling.resolution}
		<% } %> 
	   </td>
	   <td>${podling.@sponsor}
		<% if ( podling.champion != "" ) { %>
		<br/>(${podling.champion})
		<% } %> 
	   </td>
	   <td><%
		sep=""
		podling.mentors.children().each { mentor ->
		%>${sep}${mentor}<%
		     	sep=", "
		} %>
	   </td>
	   <td><%
	   	aliases=podling.resourceAliases.replaceAll(",",", ")
		%>${aliases}
	   </td>
	   <td>${podling.@startdate}</td>
	   <td>${podling.@enddate}</td>
	</tr>
        <%
           }
      } %>
      </table>
    </div>
</div>
<br/><br/>
<% include "footer.gsp" %>
