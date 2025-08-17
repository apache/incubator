#!/bin/bash

# Build and/or serve the site locally using the JBake Docker image

function fatal() {
    echo $* >&2
    exit 1
}

# N.B. jbake-docker.properties defines server.hostname=0.0.0.0
# This is necessary to ensure the server accepts external requests
# (The documentation says to use localhost, but that does not work)

OPT=$1
shift

case "$OPT" in
    -s)
    # just serve the site
    docker run --rm \
        -u jbake \
        -v "$PWD":/mnt/site \
        -e 'JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http,https"' \
        -p '8820:8820' \
        jbake/jbake:latest -c jbake-docker.properties -s || fatal "Build failed, exiting"
    ;;
    -bs)
    # bake and serve the site
    docker run --rm \
        -u jbake \
        -v "$PWD":/mnt/site \
        -e 'JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http,https"' \
        -p '8820:8820' \
        jbake/jbake:latest -c jbake-docker.properties -b -s || fatal "Build failed, exiting"
    ;;
    -b)
    # just bake the site
    docker run --rm \
        -u jbake \
        -v "$PWD":/mnt/site \
        -e 'JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http,https"' \
        jbake/jbake:latest "$@" || fatal "Build failed, exiting"
    ;;
    *) echo "Valid options are: -b (bake), -s (serve), -bs (bake and serve)"
    ;;
esac
