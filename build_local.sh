#!/bin/bash

CURRENTDIR=`pwd`
export WORKDIR=/tmp/incubator-site

function fatal() {
    echo $* >&2
    exit 1
}

rm -rf $WORKDIR
mkdir -p $WORKDIR

# just bake and serve the site
export WORKDIR
./bake.sh -b -s . $WORKDIR || fatal "Build failed, exiting"

