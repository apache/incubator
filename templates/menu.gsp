	<!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/"><i class="icon-home"></i>Apache Incubator</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Policies <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%policys.each {policy -> %>
                  <li><a href="/${policy.uri}">${policy.title}</a></li>
                <%}%>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Proposals <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%proposalGuides.each {guide -> %>
                <li><a href="/${guide.uri}">${guide.title}</a></li>
                <%}%>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Podling Guides <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%guides.each {guide -> %>
                  <li><a href="/${guide.uri}">${guide.title}</a></li>
                <%}%>
                <li><hr/><a href="/projects/#current">Current Podlings</a></li>
                <li><a href="/clutch/">Clutch Report</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">PMC Guides <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%pmcGuides.each {guide -> %>
                <li><a href="/${guide.uri}">${guide.title}</a></li>
                <%}%>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">ASF <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="https://www.apache.org/foundation/how-it-works.html">How Apache Works</a></li>
                <li><a href="https://www.apache.org/dev/">Developer Documentation</a></li>
                <li><a href="https://www.apache.org/foundation/">Foundation</a></li>
                <li><a href="https://www.apache.org/legal/">Legal</a></li>
		<li><hr/><a href="https://www.apache.org/licenses/">License</a></li>
		<li><a href="https://www.apache.org/security/">Security</a></li>
                <li><a href="https://www.apache.org/foundation/sponsorship.html">Sponsorship</a></li>
                <li><a href="https://www.apache.org/foundation/thanks.html">Thanks</a></li>
		<li><a href="https://www.apache.org/events/current-event">Current Events</a></li>
              </ul>
            </li>
            <li><a href="/faq.html">FAQs</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-4 vcenter"><a href="https://www.apache.org/"><img src="https://www.apache.org/img/asf_logo.png" alt="The Apache Software Foundation" border="0" style="margin-top: 2px" width="200"></a></div>
          <div class="col-md-4 vcenter"><a href="/"><img src="https://incubator.apache.org/images/incubator_feather_egg_logo_sm.png" alt="The Apache Software Foundation Incubator" border="0" style="margin-top: 2px" width="256"></a></div>
          <div class="col-md-4 vcenter"><a href="https://www.apache.org/foundation/contributing.html"><img src="https://www.apache.org/images/SupportApache-small.png" style="margin-left: 92px" height="64" width="64"></a></div>
      </div>
    </div>
    <div class="top-container container">