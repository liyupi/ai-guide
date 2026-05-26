# Code Wiki（ai-guide）

本目录是一套面向维护者的代码/工程 Wiki，聚焦“站点如何构建与发布”，而非内容本身的写作指南。

## 快速导航

- [01 仓库概览](./01-repo-overview.md)
- [02 整体架构](./02-architecture.md)
- [03 VuePress 配置详解](./03-vuepress-config.md)
- [04 导航与侧边栏](./04-navigation-and-sidebar.md)
- [05 脚本工具](./05-scripts.md)
- [06 依赖与插件](./06-dependencies.md)
- [07 CI/CD 与自动化](./07-ci-cd.md)
- [08 本地运行与构建](./08-how-to-run.md)
- [09 内容组织约定](./09-content-conventions.md)
- [10 常见问题排查](./10-troubleshooting.md)

## 一句话理解这个仓库

这是一个基于 **VuePress v1** 的静态文档站点仓库：内容以 Markdown 为主；少量工程代码集中在 `.vuepress/`（站点配置 + 自定义主题组件 + 构建辅助脚本）以及 `.github/workflows/`（CI 构建部署与同步）。

