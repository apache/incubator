#!/bin/bash

function fatal() {
    echo $* >&2
    exit 1
}

if [ -z ${JBAKE_HOME} ]
then
  fatal "Missing JBAKE_HOME variable"
fi

if [ -z ${WORKDIR} ]
then
  fatal "Missing WORKDIR variable"
fi
SUCCESS_FILE=$WORKDIR/.htaccess

export JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http"
${JBAKE_HOME}/bin/jbake $@ || fatal "jbake failed, exiting"

if [ ! -f $SUCCESS_FILE ]
then
    fatal "Missing $SUCCESS_FILE , JBake build failed?"
fi