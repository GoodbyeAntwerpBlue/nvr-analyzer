@echo off
chcp 65001 > nul
echo ========================================
echo   💰 NVR 消费决策分析工具
echo ========================================
echo.
echo 正在启动程序...
echo.

python nvr_analyzer.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ 程序运行出错！
    echo.
    echo 可能的原因：
    echo 1. 未安装Python
    echo 2. Python版本过低（需要3.6+）
    echo.
    echo 请安装Python后重试
    echo 下载地址：https://www.python.org/downloads/
    pause
)
