#!/bin/bash
CURRENTDIR=`pwd`
SVN_CO_DIR=/tmp/incubator-site-content
SVN_BUILD_DIR=/tmp/incubator-site-build
SVN_REPO=http://svn.apache.org/repos/asf/incubator/public/trunk/
WORKDIR=/tmp/incubator-site

rm -rf $WORKDIR
mkdir -p $WORKDIR
# download the svn bits
rm -rf $SVN_CO_DIR
rm -rf $SVN_BUILD_DIR
svn co $SVN_REPO $SVN_CO_DIR
if [ $? -gt 0 ]; then
    echo ABORT: svn checkout error
    exit 4
fi
cd $SVN_CO_DIR
# build pages the old way
ant docs -Ddocs.dest=$SVN_BUILD_DIR
if [ $? -gt 0 ]; then
    echo ABORT: ant docs error
    exit 4
fi
# run clutch2 analysis
./clutch2.sh
if [ $? -gt 0 ]; then
    echo ABORT: clutch2.sh error
    exit 4
fi
# prepare the git master with updates from svn build and clutch analysis
cd "$CURRENTDIR"
pwd
# move in files built using ant in the old style
# ip clearance as assets
rm -rf assets/ip-clearance
mkdir assets/ip-clearance
cp $SVN_BUILD_DIR/ip-clearance/*.html assets/ip-clearance/.
# podling status files as assets
rm -rf assets/projects
mkdir assets/projects
cp $SVN_BUILD_DIR/projects/*.html assets/projects/.
# move in files from the clutch analysis
# these txt files are moved to assets
cp $SVN_CO_DIR/content/clutch/*.txt assets/.
cp $SVN_CO_DIR/content/clutch/*.json assets/.
# the following asciidoc clutch files go to be baked
cp $SVN_CO_DIR/content/clutch/_includes/*.ad pages/clutch/_includes/.
cp $SVN_CO_DIR/content/clutch/*.ad pages/clutch/.

# now bake the site
export WORKDIR
./bake.sh -b -s . $WORKDIR
