#!/bin/bash

export WORKDIR=/tmp/incubator-site
ME=`basename $0`

function fatal() {
    echo $* >&2
    exit 1
}

rm -rf $WORKDIR
mkdir -p $WORKDIR

# now bake the site
./bake.sh -b . $WORKDIR || fatal "Build failed, exiting"

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
git commit -m "git-site-role commit from $ME"
git push origin asf-site