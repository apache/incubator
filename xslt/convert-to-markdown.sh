#/usr/bin/bash

export CLASSPATH=xalan-j_2_7_2/xalan.jar

for f in ${1}/*.xml
do
    echo $f
    fn="$(basename $f .xml)"
    echo $fn
    java org.apache.xalan.xslt.Process -IN $f -XSL stylesheets/anakia-to-markdown.xsl -OUT ${2}/${fn}.md
done

