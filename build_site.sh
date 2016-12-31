#!/bin/bash

rm -rf /tmp/incubator-site
ant docs -Ddocs.dest=/tmp/incubator-site
git checkout asf-site
git clean -f -d
git pull origin asf-site
cp -a /tmp/incubator-site/. output/
git add .
git commit -m "Automatic Site Publish by Buildbot"
git push origin asf-site
