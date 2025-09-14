#!/usr/bin/env bash
ps -eo user,comm \  # 列出所有进程的用户和命令名
| awk 'BEGIN{IGNORECASE=1} $2 ~ /^python/ {print $1}' \  # 匹配以python开头的进程，输出用户
| sort | uniq \  # 去重
| wc -l  # 统计用户数量
