#!/bin/bash

function fatal() {
    echo $* >&2
    exit 1
}

SUCCESS_FILE=$WORKDIR/.htaccess
if [ -z ${JBAKE_HOME} ]
then
  fatal "Missing JBAKE_HOME variable" >&2
fi

if [ -z ${WORKDIR} ]
then
  fatal "Missing WORKDIR variable" >&2
fi

export JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http"
${JBAKE_HOME}/bin/jbake $@ || fatal "jbake failed, exiting"

if [ ! -f $SUCCESS_FILE ]
then
    echo "Missing $SUCCESS_FILE , JBake build failed?" >&2
    exit 1
fi