<div align="center">

# ✍️ LiSiH 论文降AI

**专业学术文本改写工具 · 降重 · 降AI · 双降**

[![GitHub Pages](https://img.shields.io/badge/在线访问-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://imsan3.github.io/lisi-h-ai/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📋 项目简介

LiSiH 论文降AI 是一款专注于学术文本改写的轻量级工具，支持**降重复率**、**降AI率**、**降重+降AI**三种核心模式，覆盖知网、维普、格子达、Turnitin 等 11 个主流检测平台，内置 29 个专业改写模型。

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 🔻 **降重复率** | 全网领先降重技术，一键降低查重率，保证学术表达 |
| ✨ **降AI率** | 优化文本降低AI痕迹，支持 Turnitin、GPTZero 等检测 |
| 🔄 **降重+降AI** | 同时降低重复率和AI痕迹，全面提升文章质量 |
| 📎 **文件上传** | 支持 .docx 文件拖拽上传，异步处理 |
| 💰 **自动计费** | 按字数智能计算，透明定价 |
| 🔐 **验证码系统** | 30分钟有效 + 客户绑定 + 自动补码 |

## 🛠️ 技术栈

- **前端**: 纯 HTML + CSS + JavaScript（零依赖，单文件架构）
- **字体**: 系统字体（PingFang SC / Microsoft YaHei）
- **部署**: GitHub Pages（国内可访问）

## 📁 项目结构

```
lisi-h-ai/
├── index.html          # 主页面（单文件，内联 CSS/JS）
└── README.md
```

## 🚀 快速开始

### 本地使用

```bash
# 克隆仓库
git clone https://github.com/ImSan3/lisi-h-ai.git

# 直接用浏览器打开
open lisi-h-ai/index.html
```

### 部署到 GitHub Pages

1. Fork 本仓库
2. 进入 Settings → Pages
3. Source 选择 `Deploy from a branch`
4. Branch 选择 `main`，文件夹选择 `/ (root)`
5. 点击 Save，等待 1-2 分钟即可访问

访问地址: `https://<你的用户名>.github.io/lisi-h-ai/`

## 📊 支持的模型

### 降重模型

| 模型系列 | 适用平台 | 语言 |
|---------|---------|------|
| 降重0325 系列 | 知网 | 中文 |
| 降重260206 系列 | 维普 / 格子达 | 中文 |
| 超级改写 | 多语言 | 中英 |

### 降AI模型

| 模型系列 | 特点 | 语言 |
|---------|------|------|
| 微度模式 1-5 | 改写幅度递增 | 中文 |
| AI移除 1-5 | 学术性递减·幅度递增 | 中文 |
| Turnitin 专用 | 高质量优化 | 中文 |
| 维普 / 格子达专用 | 平台专属优化 | 中文 |
| 英文降AI | 英文文本优化 | 英文 |

### 双降模型

| 模型 | 说明 |
|------|------|
| 双降 260112 系列 | 降重 + 降AI 同时进行 |

## 💳 业务流程

```
用户选择改写模式 → 自动计算费用 → 扫码付款
    → 付款截图发微信 → 管理员分配验证码
    → 用户填入验证码 → 自动开始改写
```

## 📝 更新日志

### v2.0 (2026-07-18)
- ✅ 全新 UI 设计（参考 Blomstra CRM 风格）
- ✅ 验证码系统（客户绑定 + 倒计时 + 自动补码）
- ✅ 文件上传功能（.docx 异步处理）
- ✅ 收款码迁移至 CDN（国内加速）
- ✅ 移除外部字体依赖（国内访问优化）
- ✅ 部署至 GitHub Pages

### v1.0 (2026-07-18)
- ✅ 初版上线
- ✅ 三种改写模式（降重 / 降AI / 双降）
- ✅ 11 个检测平台
- ✅ 29 个专业模型

## 🤝 致谢

- [一触即改 API](https://api.ycjg.top) - 提供文本改写 API 服务
- [幕布](https://mubu.com) - 提供图床 CDN 服务

## 📄 License

MIT License

---

<div align="center">

**Made with ❤️ by [LiSiH](https://github.com/ImSan3)**

</div>
