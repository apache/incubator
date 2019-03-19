#!/bin/bash

CURRENTDIR=`pwd`
WORKDIR=/tmp/incubator-site
SVN_CO_DIR=/tmp/incubator-site-content
SVN_BUILD_DIR=/tmp/incubator-site-build
SVN_REPO=http://svn.apache.org/repos/asf/incubator/public/trunk/

# build the git bits
rm -rf $WORKDIR
mkdir -p $WORKDIR
mkdir -p $WORKDIR/clutch

echo $CURRENTDIR

# build the svn bits
rm -rf $SVN_CO_DIR
rm -rf $SVN_BUILD_DIR
svn co $SVN_REPO $SVN_CO_DIR
(
    cd $SVN_CO_DIR
    ant docs -Ddocs.dest=$SVN_BUILD_DIR
    # these files were built using ant in the old style
    mv $SVN_BUILD_DIR/ip-clearance $WORKDIR
    mv $SVN_BUILD_DIR/projects $WORKDIR
    # new clutch2 process
    ./clutch2.sh
    if [ $? -gt 0 ]; then
	echo clutch2.sh returned $? - ABORT
	exit 4
    fi
    # these txt files are moved to output
    cp $SVN_CO_DIR/content/clutch/*.txt $WORKDIR/clutch/.
    # the following files go to be baked
    cp $SVN_CO_DIR/content/clutch/_includes/*.ad $CURRENTDIR/pages/clutch/_includes/.
    cp $SVN_CO_DIR/content/clutch/*.ad $CURRENTDIR/pages/clutch/.
)

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