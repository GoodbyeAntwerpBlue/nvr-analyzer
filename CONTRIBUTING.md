# 贡献指南

感谢你考虑为 NVR Analyzer 做出贡献！🎉

## 🌟 我们欢迎什么样的贡献

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📝 改进文档
- 🔧 修复 Bug
- ✨ 实现新功能
- 🌍 翻译文档

## 🚀 如何开始

### 1. Fork 并 Clone 仓库

```bash
# Fork 本仓库（在GitHub网页上点击Fork按钮）

# Clone 你的 fork
git clone https://github.com/GoodbyeAntwerpBlue/nvr-analyzer.git
cd nvr-analyzer

# 添加上游仓库
git remote add upstream https://github.com/原作者/nvr-analyzer.git
```

### 2. 创建分支

```bash
# 更新主分支
git checkout main
git pull upstream main

# 创建新分支
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/bug-description
```

### 3. 进行修改

按照代码规范进行修改（见下文）。

### 4. 提交修改

```bash
git add .
git commit -m "feat: 添加某某功能"
```

### 5. 推送到你的 Fork

```bash
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

在 GitHub 上创建 Pull Request，描述你的修改。

## 📜 代码规范

### Python 代码风格

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范：

```python
# 好的示例
def calculate_match(weighted_needs: Dict[str, float], 
                   values: Dict[str, float]) -> float:
    """计算匹配度
    
    Args:
        weighted_needs: 加权需求字典
        values: 价值字典
        
    Returns:
        匹配度百分比
    """
    matches = {}
    for dim in DIMENSIONS.keys():
        matches[dim] = weighted_needs[dim] * values[dim]
    return sum(matches.values())
```

### 提交信息规范

使用 [约定式提交](https://www.conventionalcommits.org/zh-hans/)：

```
<类型>: <描述>

[可选的正文]

[可选的脚注]
```

**类型**：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

**示例**：
```
feat: 添加导出Excel功能

- 支持导出历史记录到Excel
- 包含详细的分析数据
- 添加单元测试

Closes #42
```

## 🐛 报告 Bug

### 在提交 Issue 前

1. 搜索现有 Issues，避免重复
2. 确认使用的是最新版本
3. 准备好详细的信息

### Bug 报告模板

```markdown
**Bug 描述**
简洁清晰的描述问题。

**复现步骤**
1. 运行 '...'
2. 输入 '...'
3. 看到错误

**预期行为**
描述你期望发生什么。

**实际行为**
描述实际发生了什么。

**截图**
如果可能，添加截图。

**环境信息**
- 操作系统: [如 Windows 11]
- Python 版本: [如 3.9.7]
- 程序版本: [如 v1.0]

**额外信息**
任何其他相关信息。
```

## 💡 建议新功能

### 功能建议模板

```markdown
**功能描述**
清晰描述你想要的功能。

**动机**
解释为什么需要这个功能。

**方案建议**
描述你希望如何实现。

**替代方案**
是否有其他可行的方案？

**额外信息**
任何其他相关信息。
```

## 📝 改进文档

文档同样重要！欢迎：

- 修正拼写/语法错误
- 改进表述清晰度
- 添加使用示例
- 翻译成其他语言
- 完善注释

## 🧪 测试

### 运行测试

```bash
# 运行程序，手动测试核心功能
python nvr_analyzer.py

# 测试各个功能：
# 1. 新建分析
# 2. 查看历史
# 3. 统计信息
# 4. 边界情况（极大值、极小值、空输入）
```

### 编写测试

如果添加新功能，请考虑添加测试用例。

## 🎨 代码审查

所有 Pull Request 都会经过审查。审查关注：

- ✅ 功能是否正确实现
- ✅ 代码是否清晰易懂
- ✅ 是否遵循代码规范
- ✅ 是否有充足的注释
- ✅ 是否更新了文档
- ✅ 是否有测试覆盖

## 📦 发布流程

由维护者负责：

1. 更新版本号
2. 更新 CHANGELOG
3. 创建 Git Tag
4. 发布 GitHub Release

## 👥 社区准则

### 行为准则

- 🤝 尊重他人
- 💬 保持专业和友好
- 🎯 专注于建设性讨论
- 🚫 不容忍骚扰和攻击

### 沟通渠道

- **Issues**: 报告Bug、建议功能
- **Pull Requests**: 提交代码
- **Discussions**: 一般性讨论

## ❓ 需要帮助？

如果有任何问题：

1. 查看 [使用文档](docs/README.md)
2. 搜索现有 Issues
3. 创建新 Issue 提问
4. 联系维护者

## 🎖️ 贡献者

感谢所有贡献者！

<!-- 贡献者列表将自动更新 -->

## 📄 许可证

通过贡献代码，你同意你的贡献将在 [MIT License](LICENSE) 下发布。

---

再次感谢你的贡献！🙏

让我们一起把 NVR Analyzer 做得更好！💪
