<%include "header.gsp"%>

<%include "menu.gsp"%>

<div class="page-header">
    <h1>${content.title}</h1>
</div>

<div class="article-body">

Estimated Reading Time: <span class="eta"></span>

<p>${content.body}</p>

<div class="cookbookIndex">
<% 
all_content.sort({p -> p.sort_order}).each { p -> 
    if(p.type == "cookbook") {
      %> 
        <div class="item">
          <!-- no link on purpose <h2><a href="${p.docname}.html">${p.title}</a></h2> -->
          <h2>${p.title}</h2>
          <div class="text">
            ${p.body}
          </div>
          <!-- debug <blockquote>${p}</blockquote> -->
        </div>
      <%
    }
}%>
</div>

<pre>${content.bottom_note}</pre>

</div>

<%include "footer.gsp"%>
