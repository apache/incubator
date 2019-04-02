#!/bin/bash

CURRENTDIR=`pwd`
WORKDIR=/tmp/incubator-site

rm -rf $WORKDIR
mkdir -p $WORKDIR

# now bake the site
./bake.sh -b . $WORKDIR

# push all of the results to asf-site
git checkout asf-site
git clean -f -d
git pull origin asf-site
rm -rf *
mkdir content
cp -a $WORKDIR/* content
cp -a $WORKDIR/.htaccess content
git add .
git commit -m "Automatic Site Publish by git-site-role"
git push origin asf-site