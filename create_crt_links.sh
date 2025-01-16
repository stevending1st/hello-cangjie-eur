#!/bin/bash

# 定义函数：根据提供的文件名查找文件并创建软链接
create_symlink_for_file() {
  # 检查是否提供了文件名参数
  if [ -z "$1" ]; then
    echo "Usage: create_symlink_for_file <filename to search for>"
    return 1
  fi

  # 定义要查找的文件名
  TARGET_FILE="$1"

  # 查找文件，这里假设你在类 Unix 系统上
  # 注意：搜索可能会花费一些时间，取决于系统大小和文件位置
  SEARCH_PATH=$(find /usr/lib -name "$TARGET_FILE" | head -n 1)

  # 检查是否找到了文件
  if [ -z "$SEARCH_PATH" ]; then
    echo "$TARGET_FILE file not found"
    return 1
  else
    echo "Found $TARGET_FILE file at: $SEARCH_PATH"
  fi

  # 获取脚本所在的目录
  SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

  # 创建软链接前先检查是否已经存在同名文件或链接
  if [ -e "$SCRIPT_DIR/$TARGET_FILE" ] || [ -L "$SCRIPT_DIR/$TARGET_FILE" ]; then
    echo "Warning: $SCRIPT_DIR/$TARGET_FILE already exists, will not overwrite."
    return 1
  fi

  # 创建软链接
  ln -s "$SEARCH_PATH" "$SCRIPT_DIR/$TARGET_FILE"

  echo "Symlink created at: $SCRIPT_DIR/$TARGET_FILE"
}

# 创建 crtbeginS.o 软连接
create_symlink_for_file "crtbeginS.o"
create_symlink_for_file "crtendS.o"
