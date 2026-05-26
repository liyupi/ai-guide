# 02 整体架构

## 运行时架构（访问者视角）

该项目最终被构建为静态站点：

- 浏览器访问静态资源（HTML/CSS/JS/图片）
- 客户端侧由 VuePress（Vue）完成页面渲染与导航交互
- 不包含后端运行时（除非外部系统为站点提供 CDN/对象存储托管）

## 构建时架构（维护者视角）

构建链路由 npm scripts 串联，核心由三段组成：

1. **索引生成（构建前）**：扫描 `AI/` 内容树，生成侧边栏数据与目录 README
2. **VuePress 构建**：将 Markdown 编译为静态站点
3. **部署/同步（CI）**：将构建产物发布到对象存储，并按需通知或同步变更

### 构建主链路（本地/CI 通用）

入口脚本见 [`package.json`](../../package.json)。

```mermaid
flowchart TD
  A[npm run docs:build] --> B[pre-docs:build]
  B --> C[node .vuepress/scripts/generateSidebar.js ./AI]
  B --> D[node .vuepress/scripts/genReadme.js ./AI]
  A --> E[vuepress build .]
  E --> F[.vuepress/dist 生成静态站点]
```

### 部署链路（GitHub Actions）

部署工作流见 [`deploy.yml`](../../.github/workflows/deploy.yml)：

```mermaid
flowchart TD
  A[push main / 手动触发] --> B[checkout]
  B --> C[setup node@16]
  C --> D[npm install]
  D --> E[npm run docs:build]
  E --> F[setup python@3.10]
  F --> G[pip install coscmd]
  G --> H[coscmd config（secrets）]
  H --> I[coscmd upload .vuepress/dist -> COS]
  I --> J[安装 nodemailer]
  J --> K[send-email.js 发送部署成功邮件]
```

### 同步链路（变更文件列表 -> 后端）

同步工作流见 [`sync-vibe-coding-course.yml`](../../.github/workflows/sync-vibe-coding-course.yml)：

- 用 `git diff` 计算 A/M/D 三类文件列表
- 用 `jq` 构造 JSON payload
- 用 `curl` 携带 Bearer token POST 到后端

## 模块划分（代码侧）

| 模块 | 位置 | 职责 |
|---|---|---|
| 站点配置 | `.vuepress/*.ts` | title/SEO/head、插件、导航/侧边栏、主题配置 |
| 主题覆盖 | `.vuepress/theme/**` | 覆盖默认主题组件（Layout/Footer/ExtraSidebar 等） |
| 内容索引脚本 | `.vuepress/scripts/**` | 自动生成侧边栏与目录 README、统计/格式化等 |
| CI/CD | `.github/workflows/**` | 构建部署、同步变更 |

## 关键依赖关系（工程视角）

```mermaid
graph LR
  subgraph Content[内容目录]
    AI[AI/]
    Vibe[Vibe Coding 零基础教程/]
    OpenClaw[OpenClaw 保姆级教程/]
    Trans[translations/]
  end

  subgraph Build[构建层]
    Scripts[.vuepress/scripts]
    Config[.vuepress/config.ts]
    Theme[.vuepress/theme]
    Sidebar[.vuepress/sidebars/ai.ts]
  end

  subgraph CI[自动化]
    Deploy[deploy.yml]
    Sync[sync-vibe-coding-course.yml]
  end

  AI --> Scripts --> Sidebar --> Config --> Theme
  Vibe --> Config
  OpenClaw --> Config
  Trans --> Config
  Config --> Dist[.vuepress/dist]
  Dist --> Deploy
  Content --> Sync
```

