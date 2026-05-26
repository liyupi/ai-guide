# 06 依赖与插件

依赖清单：[`/package.json`](../../package.json)

## 运行环境

- Node.js：CI 中使用 Node 16（见 [`deploy.yml`](../../.github/workflows/deploy.yml)）
- 包管理：npm（存在 `package-lock.json`）

## 依赖分层

### devDependencies（构建时依赖）

这些依赖主要由 `vuepress dev/build` 在本地与 CI 中使用：

- `vuepress@^1.9.10`：静态站点生成器
- `@vuepress/plugin-back-to-top`：返回顶部
- `@vuepress/plugin-google-analytics`：统计
- `@vuepress/plugin-medium-zoom`：图片缩放
- `vuepress-plugin-seo`：SEO meta 生成（见 [`config.ts`](../../.vuepress/config.ts)）
- `vuepress-plugin-sitemap`：站点地图 sitemap.xml
- `vuepress-plugin-feed`：RSS/Atom feed
- `vuepress-plugin-baidu-autopush`：百度推送
- `vuepress-plugin-tags`：标签页能力

### dependencies（站点运行时依赖 / 插件）

这些依赖同样会在构建产物中体现或影响运行时体验：

- `vuepress-plugin-code-copy`：代码块一键复制
- `vuepress-plugin-img-lazy`：图片懒加载

## 插件与配置的对应关系

插件声明在 `package.json`，实际启用与参数在 [`/.vuepress/config.ts`](../../.vuepress/config.ts) 的 `plugins` 字段。

维护建议：

- 新增插件：先安装依赖，再在 `config.ts` 中配置；同时确认是否与当前主题覆盖组件存在冲突
- 升级 VuePress v1 插件：优先在本地跑 `npm run docs:dev` 与 `npm run docs:build` 验证，避免在 CI 才暴露问题

## 非声明依赖提示

`package.json` 中的 `serve` script 使用 `serve ./.vuepress/dist`，但仓库未声明 `serve` 依赖。更稳妥的本地预览方式：

- `npx serve ./.vuepress/dist`

