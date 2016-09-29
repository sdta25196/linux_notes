#!/bin/bash

if [ -d /tmp/ ] && [ -f READ.me ]; then
    echo okay
fi

if [ -d /tmp/ -o -f /tmp/ ]; then
    echo '/tmp/ is a directory and /tmp/ is not a directory is okay'
elif [ -d /tmp/ -a -f READ.me ]; then 
    echo '/tmp/ is a directory and READ.me is a file'
else
    echo 'do nothing.'
fi
