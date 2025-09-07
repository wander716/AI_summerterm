#!/usr/bin/env bash
ps -eo user,comm \
| awk 'BEGIN{IGNORECASE=1} $2 ~ /^python/ {print $1}' \
| sort | uniq \
| wc -l
