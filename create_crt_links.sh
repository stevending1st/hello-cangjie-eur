#!/bin/bash

# 确保脚本以 root 权限运行
# if [ "$EUID" -ne 0 ]; then
#   echo "请以 root 用户或使用 sudo 运行此脚本"
#   exit 1
# fi

# 查找 crtbeginS.o 并创建符号链接
CRTBEGIN=$(find /usr/lib -name "crtbeginS.o" | head -n 1)
if [ -n "$CRTBEGIN" ]; then
    if [ -e "/usr/lib/crtbeginS.o" ]; then
        echo "警告: /usr/lib/crtbeginS.o 已存在，不会覆盖"
    else
        ln -s $CRTBEGIN /usr/lib/crtbeginS.o
        echo "已创建符号链接: /usr/lib/crtbeginS.o -> $CRTBEGIN"
    fi
else
    echo "未能找到 crtbeginS.o 文件"
fi

# 查找 crtendS.o 并创建符号链接
CRTEND=$(find /usr/lib -name "crtendS.o" | head -n 1)
if [ -n "$CRTEND" ]; then
    if [ -e "/usr/lib/crtendS.o" ]; then
        echo "警告: /usr/lib/crtendS.o 已存在，不会覆盖"
    else
        ln -s $CRTEND /usr/lib/crtendS.o
        echo "已创建符号链接: /usr/lib/crtendS.o -> $CRTEND"
    fi
else
    echo "未能找到 crtendS.o 文件"
fi

echo "完成所有操作"