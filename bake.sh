#!/bin/sh

export JBAKE_OPTS="-Djavax.xml.accessExternalDTD=http"
jbake $@
