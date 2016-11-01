#!/bin/sh

wget \
    -U 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36' \
    -O mp3/"$*".mp3 \
    "http://translate.google.com/translate_tts?tl=en&q=$*"
