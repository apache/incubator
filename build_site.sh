#!/bin/bash

WORKDIR=/tmp/incubator-site
rm -rf $WORKDIR
mkdir -p $WORKDIR
$JBAKE_HOME/bin/jbake -b . $WORKDIR
git checkout asf-site
git clean -f -d
git pull origin asf-site
rm -rf *
cp -a $WORKDIR/* .
git add .
git commit -m "Automatic Site Publish by Buildbot"
git push origin asf-site