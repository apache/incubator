#!/bin/bash

# Build the site locally using the JBake Docker image

function fatal() {
    echo $* >&2
    exit 1
}

# just bake the site
docker run --rm \
    -u jbake \
    -v "$PWD":/mnt/site \
    -e 'JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http,https"' \
    jbake/jbake:latest || fatal "Build failed, exiting"
