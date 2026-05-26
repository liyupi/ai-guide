# 04 导航与侧边栏

本仓库的信息架构主要由两类配置驱动：

- 顶部导航（Navbar）：定义站点顶部入口与下拉菜单
- 侧边栏（Sidebar）：定义左侧目录树（按路径匹配不同的 sidebar 配置）

## 顶部导航（Navbar）

配置文件：[`/.vuepress/navbar.ts`](../../.vuepress/navbar.ts)

结构为 `NavItem[]`，目前包含：

- `AI 项目`：下拉菜单，链接到若干项目教程页面（如海龟汤、亲戚计算器、模拟面试等）
- `Deepseek`：下拉菜单，链接到不同章节锚点（如“关于DeepSeek”“使用指南”等）
- 站外入口：`编程学习`、`AI 面试题库`
- 站内入口：`作者`

维护建议：

- 站内 `link` 建议统一以 `/` 开头，避免相对路径在不同页面上下文产生偏差
- 含中文与特殊字符的 slug（例如 emoji）依赖 VuePress 的编码/解码，新增页面时建议本地跑一遍构建确认最终 URL

## 侧边栏（Sidebar）挂载规则

配置文件：[`/.vuepress/sidebar.ts`](../../.vuepress/sidebar.ts)

当前为“多侧边栏配置”（`SidebarConfig4Multiple`），规则为：

- `"/AI/"` 与 `"/AI项目教程/"`：都使用同一份 AI 侧边栏数据 `AI`
- `"/"`：兜底使用 `"auto"`，让 VuePress 根据页面标题自动生成侧边栏（实际由主题 util 的 `resolveHeaders` 生成）

AI 侧边栏数据来源：

- 数据文件：[`/.vuepress/sidebars/ai.ts`](../../.vuepress/sidebars/ai.ts)
- 该文件由构建前脚本自动生成（见 05 脚本工具）

## AI 侧边栏数据结构（ai.ts）

`ai.ts` 导出一个数组（`export default [...]`），元素可能是：

- `""`：表示当前目录 `README.md`（VuePress 侧边栏约定）
- `{ title, collapsable, children }`：分组节点；`children` 可继续嵌套 group 或页面路径字符串

示例（节选）见：[`ai.ts`](../../.vuepress/sidebars/ai.ts)

## 自动生成逻辑要点

生成侧边栏脚本：[`generateSidebar.js`](../../.vuepress/scripts/generateSidebar.js)

核心策略：

- 递归扫描目标目录（默认传参为 `./AI`）
- 忽略以 `.` 开头的隐藏目录
- 收集 Markdown（排除 `README.md`）与子目录
- 使用 **文件/目录创建时间 `birthtime`** 做降序排序（新的在前）
- 对包含 `🔥DeepSeek 小白快速上手指南` 的文件做特殊处理：插到当前层级最前
- 生成结果写入：`.vuepress/sidebars/ai.ts`

风险提示：

- `birthtime` 在不同文件系统/跨平台同步时不一定稳定；如果遇到排序异常，更可靠的方式是改为显式排序字段（如文件名前缀数字、frontmatter date 等）

