#!/bin/bash

export WORKDIR=/tmp/incubator-site

function fatal() {
    echo $* >&2
    exit 1
}

rm -rf $WORKDIR
mkdir -p $WORKDIR

# just bake and serve the site
./bake.sh -b -s . $WORKDIR || fatal "Build failed, exiting"
