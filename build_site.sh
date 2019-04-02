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
rm -rf content
mkdir content
cp -a $WORKDIR/* content
cp -a $WORKDIR/.htaccess content
cp -a reserve/*.txt content/.
cp -a reserve/*.json content/.
cp -a reserve/clutch content/.
cp -a reserve/projects content/.
cp -a reserve/ip-clearance content/.
git add content
git commit -m "Automatic Site Publish by git-site-role"
git push origin asf-site