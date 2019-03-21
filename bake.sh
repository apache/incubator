#!/bin/sh

#export JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http"
#jbake $@
java -Djavax.xml.accessExternalDTD=http -jar "${JBAKE_HOME}/jbake-core.jar" "$@"