# 05 脚本工具

脚本目录：[`/.vuepress/scripts/`](../../.vuepress/scripts/)

这些脚本主要用于“内容索引生成”和“CI 辅助动作”。入口一般通过 `package.json` 的 scripts 调用。

## generateSidebar.js（生成侧边栏）

- 文件：[`generateSidebar.js`](../../.vuepress/scripts/generateSidebar.js)
- npm 脚本：`npm run generate:sidebar <dir>`（见 [`package.json`](../../package.json)）
- 输出：写入 `/.vuepress/sidebars/ai.ts`

### 关键函数

- `generateSidebarConfig(dirPath)`：生成 sidebar 数组
- `processDirectory(currentPath, relativePath, config)`：递归扫描目录并填充配置

### 输入/输出约定

- CLI 参数 `process.argv[2]`：目标目录（默认 `.`），构建流程中传 `./AI`
- 若目标目录下存在 `README.md`：会先 `sidebarItems.push("")`，以便 README 作为分组首页

## genReadme.js（生成目录 README 索引页）

- 文件：[`genReadme.js`](../../.vuepress/scripts/genReadme.js)
- npm 脚本：`npm run generate:readme <dir>`
- 输出：在指定目录内写入/覆盖 `README.md`

### 关键函数

- `genReadme(directory)`：主入口，校验目录存在并写入 README
- `generateContent(directory, dirName)`：生成 README Markdown 内容
- `getSubDirectories(directory)`：获取一级子目录
- `getFilesInDirectory(directory)`：递归获取所有 `.md`

### 生成策略要点

- README 顶部固定文案（站点链接）
- 一级子目录按 `birthtime` 新→旧排序
- 子目录内收集 `.md` 文件（递归），最多列出 100 条链接
- 对包含 `🔥DeepSeek 小白快速上手指南` 的文件做置顶
- 链接路径会把空格替换为 `%20`

风险提示：

- 该脚本会覆盖现有 README；如果目录 README 需要手工维护，请避免在构建链路中对该目录运行此脚本

## getMdNumber.js（统计 Markdown 数量）

- 文件：[`getMdNumber.js`](../../.vuepress/scripts/getMdNumber.js)
- npm 脚本：`npm run getMdNumber <dir>`

### 关键函数

- `countMarkdownFiles(dirPath)`：递归统计 `.md` 数量

## formatMdContent.js（批量补标题/规范化标题）

- 文件：[`formatMdContent.js`](../../.vuepress/scripts/formatMdContent.js)
- 入口约定：`node scripts/formatMdContent.js <dir>`（脚本文件顶部说明）
- 行为：递归处理目录内所有 `.md`，如果开头没有 `# ` 或 `## ` 标题则补 `## 文件名`

### 已知问题（建议修复后再使用）

当前实现使用：

- `const firstLine = content.trim().split("")[0];`

这会得到“第一个字符”而不是第一行，导致标题识别和 `replace` 基本不可用。正确做法应当按换行切分首行（例如 `split("\n")[0]`）。

如果你计划在仓库中实际启用该脚本，建议先修正后再运行，避免批量污染内容文件。

## send-email.js（CI 部署成功邮件通知）

- 文件：[`send-email.js`](../../.vuepress/scripts/send-email.js)
- 触发位置：CI 部署工作流 [`deploy.yml`](../../.github/workflows/deploy.yml)

### 输入约定

脚本读取：

- CLI 参数：`emailUser`、`emailPass`、`toEmail`
- GitHub Actions 环境变量：`GITHUB_REPOSITORY`、`GITHUB_RUN_ID`、`GITHUB_REF_NAME`

### 关键函数

- `sendEmail()`：使用 `nodemailer.createTransport` 发送 HTML 邮件；成功返回 `true` 并以进程退出码表达执行结果（0/1）

