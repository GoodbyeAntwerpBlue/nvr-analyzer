# 💰 NVR 消费决策分析系统

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

一个帮助你做出理性消费决策的命令行工具。基于"需求-价值-回报"（NVR）模型，通过量化分析告诉你：**不是"它值多少钱"，而是"它对我值多少钱"。**

![Demo](https://via.placeholder.com/800x400/1a1a1a/ffffff?text=NVR+Analyzer+Demo)

## ✨ 特性

- 🎯 **七维度需求评估** - 从安全、健康、时间、自由、连接、成长、意义全方位分析
- 📊 **智能匹配度计算** - 自动计算需求与产品价值的重合度
- 💡 **性价比指数** - 一个数字告诉你值不值得买
- ⚠️ **冲动消费检测** - 识别并预警冲动购买风险
- 📈 **历史记录管理** - 追踪所有决策，形成个人消费数据库
- 📊 **统计分析** - 了解你的消费模式和需求偏好
- 🚀 **开箱即用** - 零配置，无外部依赖

## 🎬 快速演示

```bash
$ python nvr_analyzer.py

============================================================
  💰 NVR 消费决策分析工具
============================================================

📦 产品/服务名称: 小米SU7
💵 价格 (元): 300000

# ... 评估过程 ...

✨ 决策建议
============================================================

🔴 不推荐

性价比指数：0.63
决策建议：这个产品与你的需求匹配度较低，建议重新考虑。

✅ 决策记录已保存
```

## 🚀 快速开始

### 前置要求

- Python 3.6 或更高版本

### 安装

#### 方法1：克隆仓库（推荐）

```bash
git clone https://github.com/GoodbyeAntwerpBlue/nvr-analyzer.git
cd nvr-analyzer
```

#### 方法2：下载ZIP

从 [Releases](https://github.com/GoodbyeAntwerpBlue/nvr-analyzer/releases) 页面下载最新版本。

### 运行

#### Windows

```bash
# 双击运行
start.bat

# 或在命令行中
python nvr_analyzer.py
```

#### macOS / Linux

```bash
# 添加执行权限（首次）
chmod +x start.sh

# 运行
./start.sh

# 或直接运行
python3 nvr_analyzer.py
```

## 📖 使用指南

### 基本流程

1. **输入产品信息**
   ```
   产品名称：小米SU7
   价格：300000
   ```

2. **评估你的需求**（0-10分）
   - 🛡️ 安全：8
   - 💪 健康：5
   - ⏰ 时间：9
   - 🗝️ 自由：7
   - 🤝 连接：3
   - 🌱 成长：4
   - ✨ 意义：5

3. **评估产品价值**（0-10分）
   - 在相同维度上评估产品能提供的价值

4. **查看结果**
   - 匹配度、价值密度、性价比指数
   - 🟢 推荐 / 🟡 考虑 / 🔴 不推荐

### 核心概念

#### 七个维度

| 维度 | 权重 | 说明 |
|------|------|------|
| 🛡️ 安全 | 1.5× | 降低风险与焦虑 |
| 💪 健康 | 1.5× | 维持身体能量 |
| ⏰ 时间 | 1.5× | 节约或创造时间 |
| 🗝️ 自由 | 1.2× | 扩展选择与自主权 |
| 🤝 连接 | 1.0× | 建立情感联结 |
| 🌱 成长 | 1.2× | 提升能力与认知 |
| ✨ 意义 | 1.0× | 精神满足感 |

#### 决策标准

```
性价比指数 = 匹配度 × 价值密度

🟢 ≥ 1.5   强烈推荐 - 非常适合你的需求
🟡 1.0-1.5 可以考虑 - 建议对比其他方案
🔴 < 1.0   不推荐 - 可能是在为"别人的需求"买单
```

## 📊 实战案例

### 案例1：购买通勤车

**场景**：需要买车通勤，重视安全和时间效率

**候选产品**：
- A. 小米SU7（30万） - 性价比指数：0.63 🔴
- B. 比亚迪秦PLUS（10万） - 性价比指数：1.08 🟡
- C. 二手车（5万） - 性价比指数：0.89 🔴

**结论**：比亚迪最适合，既满足核心需求又性价比高。

详细分析见：[案例文档](docs/cases.md)

### 案例2：健身课程选择

- 私教课10次（5000元） - ROI：1.44 🟡
- 私教课3次（1500元） - ROI：1.60 🟢

**结论**：先买3次体验，效果好再续费。

## 📁 项目结构

```
nvr-analyzer/
├── nvr_analyzer.py          # 主程序
├── start.bat                 # Windows启动脚本
├── start.sh                  # macOS/Linux启动脚本
├── README.md                 # 本文件
├── LICENSE                   # MIT许可证
├── .gitignore               # Git忽略规则
├── docs/                    # 文档目录
│   ├── 快速入门.md
│   ├── 使用手册.md
│   ├── 需求模板参考.md
│   ├── NVR模型详解.md
│   └── 决策模板.md
└── nvr_records.json         # 历史记录（自动生成）
```

## 🎯 适用场景

### ✅ 推荐使用

- 💰 大额消费（>1000元）
- 🤔 纠结不定的购买决策
- 💸 经常后悔的消费类型
- 📊 想要了解自己的消费模式
- 🎯 建立理性消费习惯

### ⚠️ 不必使用

- ☕ 日常小额消费（<100元）
- 🚨 紧急必需品
- 🎁 情感驱动的特殊场合

## 🛠️ 技术栈

- **语言**：Python 3.6+
- **依赖**：无（仅使用标准库）
- **数据存储**：JSON格式本地文件
- **平台支持**：Windows / macOS / Linux

## 📚 文档

- [快速入门](docs/快速入门.md) - 5分钟上手指南
- [使用手册](docs/README.md) - 完整功能说明
- [需求模板参考](docs/需求模板参考.md) - 14种常见场景的评分参考
- [NVR模型详解](docs/D-20251022-NVR模型详解.md) - 理论原理和公式推导
- [决策模板](docs/D-20251022-NVR决策模板.md) - 可打印的纸质表格

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 待完成功能

- [ ] 导出分析报告（PDF/Excel）
- [ ] 多币种支持
- [ ] 图形化界面（GUI）
- [ ] Web版本
- [ ] 预算管理功能
- [ ] 数据可视化图表

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

灵感来源于：
- 马斯洛需求层次理论
- 第一性原理思维
- 理性决策理论

## 📞 联系方式

- **作者**：YourName
- **邮箱**：your.email@example.com
- **项目主页**：https://github.com/GoodbyeAntwerpBlue/nvr-analyzer

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐️

[![Star History Chart](https://api.star-history.com/svg?repos=GoodbyeAntwerpBlue/nvr-analyzer&type=Date)](https://star-history.com/#GoodbyeAntwerpBlue/nvr-analyzer&Date)

## 💡 核心理念

> **"不是它值30万，而是它对我值多少。"**  
> **"不是这车真棒，而是这车适合我吗？"**

理性消费，智慧生活。🚀

---

**如果你觉得有用，欢迎分享给朋友！** 📢
