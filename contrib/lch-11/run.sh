#!/bin/sh

./login.sh && ./status.sh | node parse-lch-modem-status.js
