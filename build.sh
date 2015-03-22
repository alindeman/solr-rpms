#!/bin/bash
set -e

dir="$1"
if [ -z "$dir" ]; then
  dir="$(cd "$(dirname "${BASH_SOURCE[0]}")"; pwd)"
fi
cd $dir

rpmdev-setuptree
# TODO
#trap rpmdev-wipetree EXIT

rpmlint solr.spec || exit 1
spectool -g -R solr.spec
rpmbuild -ba solr.spec

for ddir in RPMS SRPMS; do
  rm -rf $ddir
  cp -Rpv ~/rpmbuild/$ddir .
done
