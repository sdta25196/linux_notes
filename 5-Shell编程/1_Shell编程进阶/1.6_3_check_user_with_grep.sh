#!/bin/bash

read -p "Please input you wanna check user: " key_word

if [ `grep -q "^$key_word:" /etc/passwd` ]; then
    echo "The user $key_word is exist."
else
    echo "The user $key_word is NOT exist."
fi
