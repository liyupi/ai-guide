# 09 内容组织约定

本仓库的内容以 Markdown 为主，工程侧的约定主要服务于“可索引、可导航、可稳定构建”。

## 目录与信息架构

- `AI/` 是构建链路中被“索引生成脚本”重点处理的目录：
  - 构建前会生成 `/.vuepress/sidebars/ai.ts`
  - 构建前会覆盖写入 `AI/README.md`（以及其子目录 README，取决于脚本运行范围）
- 其他内容目录（如 `Vibe Coding 零基础教程/`、`OpenClaw 保姆级教程/`、`translations/`）主要由 VuePress 默认解析与侧边栏 auto 模式呈现

## 文件命名建议

由于侧边栏与 README 生成脚本会把文件名直接作为标题/链接文本的一部分：

- 文件名建议避免过长（可读性与 URL 可用性）
- 中文与空格可用，但注意 URL 编码：
  - `genReadme.js` 会把空格替换为 `%20`
- emoji / 特殊符号（如 `🔥`）在 URL 中会被编码，建议新增内容后本地跑一遍构建确认最终链接可访问

## README 生成与维护策略

当前构建链路会执行：

- `node ./.vuepress/scripts/genReadme.js ./AI`

这意味着：

- `AI/README.md` 会在每次构建前自动生成/覆盖
- 如果希望在 `AI/README.md` 中保留手工内容，需要调整构建脚本（例如拆分“机器生成区块”和“手写区块”）

## Frontmatter（可选但推荐）

虽然仓库目前以内容为主，但对于 SEO/Feed/文章排序更可控的做法是：

- 给文章增加 frontmatter，如 `title`、`description`、`tags`、`date`、`image`
- SEO 插件会读取 `frontmatter.description/tags/date/image`（见 [`config.ts`](../../.vuepress/config.ts) 的 seo 插件配置）

