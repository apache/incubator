#!/bin/sh

# convert the existing path to unix
if [ "$OSTYPE" = "cygwin32" ] || [ "$OSTYPE" = "cygwin" ] ; then
   CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# Add in your .jar files first
for i in ./lib/*.jar
do
    CLASSPATH=$CLASSPATH:"$i"
done

# convert the unix path to windows
if [ "$OSTYPE" = "cygwin32" ] || [ "$OSTYPE" = "cygwin" ] ; then
   CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
fi

BUILDFILE=build.xml

java $ANT_OPTS -classpath "$CLASSPATH" \
                org.apache.tools.ant.Main \
                -Dant.home=$ANT_HOME \
                -buildfile ${BUILDFILE} \
                 "$@"
