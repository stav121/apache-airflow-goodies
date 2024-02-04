#!/bin/bash

# Script that builds the wheel of the project and creates a release
#
# @author: Stavros Grigoriou <unix121@protonmail.com>

set -x
set -eo pipefail

RELEASE=${RELEASE:=false}

>&2 echo "Building wheel."

python3 setup.py sdist bdist_wheel

twine check dist/*

if [[ $RELEASE = true ]]; then
  >&2 echo "Uploading release"
  twine upload dist/*
fi
