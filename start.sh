#!/bin/bash

echo "========================================"
echo "  💰 NVR 消费决策分析工具"
echo "========================================"
echo ""
echo "正在启动程序..."
echo ""

# 检测Python命令
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ 错误：未找到Python！"
    echo ""
    echo "请先安装Python 3.6或更高版本"
    echo "访问：https://www.python.org/downloads/"
    exit 1
fi

# 运行程序
$PYTHON_CMD nvr_analyzer.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ 程序运行出错！"
    echo ""
    echo "可能的原因："
    echo "1. Python版本过低（需要3.6+）"
    echo "2. 缺少必要的库"
    echo ""
fi
