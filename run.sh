#!/usr/bin/env bash

TIME=`whereis -b time|cut -d' ' -f2`

if [[ -z $TIME ]]; then
    echo "time binary not found. Check your system."
    exit 1
fi

stack install 2>/dev/null
$TIME -v ./aeson-shits-its-pants
