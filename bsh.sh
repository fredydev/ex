#!/bin/bash

for i in `find .  -type f -prune`; do
    if [ -f $i ];then
       sha1sum  $i >> beko.txt
    fi
done
