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
          <a class="navbar-brand" href="<%if (content.rootpath) {%>${content.rootpath}<% } else { %><% }%>">Apache Incubator</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="<%if (content.rootpath) {%>${content.rootpath}<% } else { %><% }%>index.html">Home</a></li>
            <li><a href="<%if (content.rootpath) {%>${content.rootpath}<% } else { %><% }%>about.html">About</a></li>
            <li><a href="<%if (content.rootpath) {%>${content.rootpath}<% } else { %><% }%>${config.feed_file}">Subscribe</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Policies <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%policys.each {policy -> %>
                  <li><a href="${config.site_host}/${policy.uri}">${policy.title}</a></li>
                <%}%>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Guides <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <%guides.each {guide -> %>
                  <li><a href="${config.site_host}/${guide.uri}">${guide.title}</a></li>
                <%}%>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>
    <div class="container">