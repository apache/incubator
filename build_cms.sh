#!/bin/sh
# caller passes $source_dir (cwd) and $target_dir as args to this script
# Called by: https://svn.apache.org/repos/infra/websites/cms/build/build_external.pl

ant "-Ddocs.dest=$2/content" docs
