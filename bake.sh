#!/bin/sh

export JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http"
${JBAKE_HOME}/bin/jbake $@
