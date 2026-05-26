# 01 仓库概览

## 项目定位

- **项目类型**：VuePress v1 静态站点（知识库 / 教程站）
- **主要产物**：`.vuepress/dist/`（静态 HTML/CSS/JS）
- **内容来源**：根目录下的大量 Markdown（如 `AI/`、`Vibe Coding 零基础教程/`、`OpenClaw 保姆级教程/`、`translations/`）

## 代码与内容边界

本仓库“代码”主要用于：

- 定义站点信息架构与渲染行为（VuePress 配置、导航、侧边栏、SEO、sitemap、feed 等）
- 维护内容的索引能力（构建前自动生成侧边栏数据与目录 README）
- 自动化部署与同步（GitHub Actions）

业务内容（文章正文）本身不包含可执行逻辑，因此这里的 “关键类/函数” 主要指：

- `.vuepress/scripts/*.js` 中的 Node 脚本函数
- `.vuepress/config.ts` 及 `.vuepress/*.ts` 配置导出对象
- `.vuepress/theme/**` 的 Vue 组件（覆盖/扩展默认主题）

## 顶层目录速览

| 路径 | 类型 | 作用 |
|---|---|---|
| `.vuepress/` | 工程代码 | VuePress 站点配置、主题、自定义脚本、静态资源 |
| `.github/workflows/` | 自动化 | CI 构建部署、同步变更文件列表到后端 |
| `AI/` | 内容 | AI 知识库核心内容（会被构建脚本生成索引） |
| `Vibe Coding 零基础教程/` | 内容 | Vibe Coding 系列教程 |
| `OpenClaw 保姆级教程/` | 内容 | OpenClaw 系列教程 |
| `translations/` | 内容 | 多语言翻译（如英文、繁中） |
| `image/` | 资源 | 文章或站点引用的图片资源（非 `.vuepress/public`） |

## 关键入口文件

- 站点配置入口：[`/.vuepress/config.ts`](../../.vuepress/config.ts)
- 导航配置：[`/.vuepress/navbar.ts`](../../.vuepress/navbar.ts)
- 侧边栏挂载：[`/.vuepress/sidebar.ts`](../../.vuepress/sidebar.ts)
- AI 侧边栏数据（由脚本生成）：[`/.vuepress/sidebars/ai.ts`](../../.vuepress/sidebars/ai.ts)
- 主题扩展入口：[`/.vuepress/theme/index.js`](../../.vuepress/theme/index.js)
- 构建/开发脚本：[`/package.json`](../../package.json)
- CI（部署）：[`/.github/workflows/deploy.yml`](../../.github/workflows/deploy.yml)
- CI（同步变更）：[`/.github/workflows/sync-vibe-coding-course.yml`](../../.github/workflows/sync-vibe-coding-course.yml)

