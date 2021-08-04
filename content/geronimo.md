Title: geronimo


# Apache Geronimo Now A Top Level Project {#Apache+Geronimo+Now+A+Top+Level+Project}

The Apache Geronimo project has completed incubation. Please go to the main project site :


 [http://geronimo.apache.org/](http://geronimo.apache.org/) 


This page tracked the project status, incubator-wise. Items marked **DONE** have been completed.


<span class="graduated">The Geronimo project graduated on 2004-05-26</span>


This page is of historical interest only.


# 2003-11-11 {#2003-11-11}

We have recieved a mail [a letter on behalf of the JBoss Group, LCC dated October 31, 2003](geronimo/20031031_jboss.pdf) that asks for clarifications regarding similarity between parts of the Geronimo codebase and the JBoss codebase.


We are thus in the process of actively reviewing not only the specific claims but also the code base in general.


A small info page for Geronimo can be found [here](geronimo/index.html) .


The wiki for Geronimo is at [http://wiki.apache.org/geronimo/](http://wiki.apache.org/geronimo/) 


 **DONE** Make sure that the requested project name does not already exist and check www.nameprotect.com to be sure that the name is not already trademarked for an existing software product.


 **DONE** If request from an existing Apache project to adopt an external package, then ask the Apache project for the cvs module and mail address names.


 **DONE** If request from outside Apache to enter an existing Apache project, then post a message to that project for them to decide on acceptance.


 **DONE** If request from anywhere to become a stand-alone PMC, then assess the fit with the ASF, and create the lists and modules under the incubator address/module names if accepted.


 **DONE** Who has been identified as the Mentor for the incubation?


Geir Magnusson Jr. Jim Jagielski


 **DONE** Are they tracking progress in the file


incubator/projects/{project_name}/status


 **DONE** Have the papers that transfer rights to the ASF been received? It is only necessary to transfer rights for the package, the core code, and any new code produced by the project.


 **(new codebase)** 


 **DONE** Have the files been updated to reflect the new ASF copyright?


Verify distribution rights:



- For all code included with the distribution that is not under the Apache license, do we have the right to combine with Apache-licensed code and redistribute?

done except for questions about the Sun j2ee schemas. We are waiting for information from Geir on the Sun and Apache position on this question.


 **DONE** Is all source code distributed by the project covered by one or more of the following approved licenses: Apache, BSD, Artistic, MIT/X, MIT/W3C, MPL 1.1, or something with essentially the same terms?



- Check all clarification requests from the JBoss group, and in particular check that [this letter dated 2003-10-31](geronimo/20031031_jboss.pdf) has been properly addressed. These claims were extensively researched by many Apache contributors and Geronimo committers. The official conclusions are ???


- Are all active committers in the STATUS file? **DONE** Do they have accounts on cvs.apache.org? **DONE** Have they submitted a contributors agreement?

 **DONE** CVS modules created and committers added to avail file? **DONE** Mailing lists set up and archived? **DONE** Problem tracking system (JIRA)? **DONE** Has the project migrated to our infrastructure?


 **DONE** Have all of the active long-term volunteers been identified and acknowledged as committers on the project?


 **DONE** Are there three or more independent committers?


(The legal definition of independent is long and boring, but basically it means that there is no binding relationship between the individuals, such as a shared employer, that is capable of overriding their free will as individuals, directly or indirectly.)


 **DONE** Are project decisions being made in public by the committers?



- Are the decision-making guidelines published and agreed to by all of the committers?

# 2004-01-20 {#2004-01-20}

```
Status report for the Incubator Geronimo Project * is the STATUS file
up to date? (also post link) Yes
/home/cvs/incubator/site/projects/geronimo.cwiki * any legal,
cross-project or personal issues that still need to be addressed? A
serious legal issue was raised by JBoss Group LLC in a letter dated
10/31/2003. This issue has been thoroughly investigated and the
conclusion of the community is that the issues raised in the letter
are unfounded. A question has arisen whether it is permissible to
include XML Schema documents for J2EE deployment descriptors in CVS.
We have raised the issue with Sun and are awaiting a response. * what
has been done for incubation since the last report? The establishment
of a PPMC has aided the organization of the project. Added Gianny
D'Amour as committer. The community voted to keep the name "Geronimo"
The ASF has become a J2EE licensee, allowing us to start the
certification process. * plans and expectations for the next period?
To start testing with the J2EE TCK. To work with the Incubator PMC to
provide an interim release allowing people to use Geronimo without
building from source making it available to a larger community. To
address any remaining issues before applying to leave the Incubator.
* any recommendations for how incubation could run more smoothly for
you? The establishment of the PPMC has been a great help.

```

If graduating to an existing PMC, has the PMC voted to accept it? (Not applicable)



- If graduating to a new PMC, has the board voted to accept it?


- Has the Incubator decided that the project has accomplished all of the above tasks?

Other issues: 2003/12/21 vote on keeping the name Geronimo +1 jboynes, dblevins, adc, gstein, jdillon, djencks, dims, chirino, dain, janb, gregwilkins, bsnyder, rmonson, jules, geir -1 jstrachan Decision made on 2003/12/24 to keep the name Geronimo


List of active committers: (see also the root project.xml maven control file)


Jan Bartel Jeremy Boynes Alan Cabrera Hiram Chinirio Gianni Damour Jason Dillon Jules Gosnell David Jencks Richard Monson-Haefel Aaron Mulder Bruce Snyder James Strachan Dain Sundstrom Greg Wilkins

