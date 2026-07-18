<div align="center">

# ✍️ LiSiH 论文降AI

**专业学术文本改写工具 · 降重 · 降AI · 双降**

[![GitHub Pages](https://img.shields.io/badge/在线访问-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://sannottired.github.io/lisi-h-ai/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📋 项目简介

LiSiH 论文降AI 是一款基于一触即改 API 的学术文本改写工具，支持**降重复率**、**降AI率**、**降重+降AI**三种模式，覆盖知网、维普、格子达、Turnitin 等 11 个检测平台，内置 29 个专业改写模型。

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 🔻 **降重复率** | 全网领先降重技术，一键降低查重率，保证学术表达 |
| ✨ **降AI率** | 优化文本降低AI痕迹，支持 Turnitin、GPTZero 等检测 |
| 🔄 **降重+降AI** | 同时降低重复率和AI痕迹，全面提升文章质量 |
| 📎 **文件上传** | 支持 .docx 文件拖拽上传，异步处理 |
| 💰 **自动计费** | 按字数 × ¥3.5/千字 自动计算费用 |
| 🔐 **验证码系统** | 30分钟有效 + 客户绑定 + 自动补码 + 撤销功能 |

## 🛠️ 技术栈

- **前端**: 纯 HTML + CSS + JavaScript（零依赖，单文件）
- **API**: [一触即改 API](https://api.ycjg.top)（文本改写 + 文件改写）
- **字体**: 系统字体（PingFang SC / Microsoft YaHei）
- **部署**: GitHub Pages

## 📁 项目结构

```
lisi-h-ai/
├── index.html          # 主页面（单文件，内联 CSS/JS）
├── pay-wechat.jpg      # 微信收款码（已迁移至幕布CDN）
├── pay-alipay.jpg      # 支付宝收款码（已迁移至幕布CDN）
└── README.md
```

## 🚀 快速开始

### 本地使用

```bash
# 克隆仓库
git clone https://github.com/SannotTired/lisi-h-ai.git

# 直接用浏览器打开
open lisi-h-ai/index.html
```

### 部署到 GitHub Pages

```bash
# 1. Fork 本仓库

# 2. 进入 Settings → Pages

# 3. Source 选择 Deploy from a branch

# 4. Branch 选择 main，文件夹选择 / (root)

# 5. 点击 Save，等待 1-2 分钟即可访问
```

访问地址: `https://<你的用户名>.github.io/lisi-h-ai/`

## 🔑 API Key 获取

1. 注册 [一触即改 API 平台](https://api.ycjg.top)
2. 进入「开发者中心」获取 API Key
3. 在页面隐藏输入框中输入暗号 `San3013` 打开管理后台

## 📊 支持的模型

### 降重模型（中文）

| 模型 | 适用平台 | 价格 |
|------|---------|------|
| 降重0325-2 ⭐ | 知网 | ¥0.44/千字 |
| 降重0325-1 | 知网 | ¥0.44/千字 |
| 降重260206_中文 | 维普/格子达 | ¥0.44/千字 |
| 超级改写(多语言) | 英文 | ¥0.44/千字 |

### 降AI模型（中文）

| 模型 | 特点 | 价格 |
|------|------|------|
| 微度模式1-5 | 改写幅度递增 | ¥0.44/千字 |
| AI移除_1-5 | 学术性递减·幅度递增 | ¥0.44/千字 |
| Turnitin专用 | 质量高 | ¥0.44/千字 |
| 维普/格子达专用 | 平台专属优化 | ¥0.44/千字 |

### 双降模型

| 模型 | 说明 | 价格 |
|------|------|------|
| 双降260112_1 ⭐ | 降重+降AI同时进行 | ¥0.44/千字 |
| 双降260112_2-3 | 不同改写强度 | ¥0.44/千字 |

## 💳 支付流程

```
用户选择改写模式 → 自动计算费用 → 扫码付款
    → 付款截图发微信 → 管理员分配验证码
    → 用户填入验证码 → 自动开始改写
```

### 管理后台

在页面任意位置输入暗号 `San3013` 打开管理后台：

- 🔢 **自动生成 3 个并行验证码**
- ⏱ **每个验证码 30 分钟有效期**
- 👤 **绑定客户昵称**（分配时填写）
- 📋 **一键复制**（标记已发送状态）
- ❌ **撤销功能**（发错立即作废）
- 🔄 **自动补码**（客户用掉一个自动补新码）

## 📸 功能预览

<div align="center">

| 降重模式 | 支付弹窗 | 管理后台 |
|---------|---------|---------|
| ![模式选择](https://via.placeholder.com/300x200?text=Mode+Selection) | ![支付](https://via.placeholder.com/300x200?text=Payment+Modal) | ![Admin](https://via.placeholder.com/300x200?text=Admin+Panel) |

</div>

## ⚙️ 配置说明

### 修改 API Key

在 `index.html` 中找到隐藏的 API Key 输入框，替换为你的 Key：

```html
<input type="password" id="apiKey" value="sk-你的Key" ...>
```

### 修改定价

```javascript
const PRICE_PER_1000 = 3.5; // ¥3.5/千字
```

### 修改验证码有效期

```javascript
const CODE_EXPIRE_MS = 30 * 60 * 1000; // 30分钟
```

### 修改暗号

```javascript
function checkSecret() {
  const v = document.getElementById('secretInput').value;
  if (v.includes('你的暗号')) { ... }
}
```

## 📝 更新日志

### v2.0 (2026-07-18)
- ✅ 全新 UI 设计（参考 Blomstra CRM 风格）
- ✅ 验证码系统（客户绑定 + 倒计时 + 自动补码）
- ✅ 文件上传功能（.docx 异步处理）
- ✅ 收款码迁移至幕布 CDN（国内加速）
- ✅ 移除 Google Fonts（国内访问优化）
- ✅ 部署至 GitHub Pages

### v1.0 (2026-07-18)
- ✅ 初版上线
- ✅ 三种改写模式（降重/降AI/双降）
- ✅ 11 个检测平台
- ✅ 29 个专业模型
- ✅ 文本输入 + 文件上传

## 🤝 致谢

- [一触即改 API](https://api.ycjg.top) - 提供文本改写 API 服务
- [幕布](https://mubu.com) - 提供图床 CDN 服务

## 📄 License

MIT License

---

<div align="center">

**Made with ❤️ by [LiSiH](https://github.com/SannotTired)**

</div>
