# 03 VuePress 配置详解

配置入口为 [`/.vuepress/config.ts`](../../.vuepress/config.ts)。

## 顶层字段速览

| 字段 | 作用 | 备注 |
|---|---|---|
| `title` / `description` | 站点标题与描述 | 影响 HTML head、SEO 插件 |
| `head` | 额外注入 `<head>` 内容 | 包含 favicon、meta keywords、百度统计脚本 |
| `permalink` | URL 规则 | `/:slug` |
| `extraWatchFiles` | 监听额外文件变更 | 便于侧边栏/配置变更后热更新 |
| `markdown` | Markdown 渲染参数 | 行号、提取标题层级等 |
| `plugins` | VuePress 插件列表 | SEO、sitemap、feed、lazyload 等 |
| `themeConfig` | 主题配置 | nav/sidebar、repo/editLinks、footer/extraSideBar |

## 关键配置点

### 1）Head 注入

`head` 数组用于追加 favicon、meta、script 等。当前包含：

- favicon：`/favicon.ico`
- `meta keywords`
- 百度统计脚本（hm.baidu.com）

### 2）Permalink 规则

`permalink: "/:slug"` 会基于页面 slug 生成更短的 URL。维护者需要注意：

- slug 与文件路径/标题的对应关系由 VuePress 内部规则决定
- 对文章标题或 frontmatter 的变更可能影响最终 URL，进而影响外链与 SEO

### 3）Markdown 渲染策略

`markdown` 配置包括：

- `lineNumbers: true`：代码块显示行号
- `extractHeaders: ["h2","h3","h4","h5","h6"]`：侧边栏/目录可使用更深的标题层级

### 4）插件清单与配置意图

插件配置位于 `plugins`，核心包括：

- `@vuepress/back-to-top`：回到顶部按钮
- `@vuepress/google-analytics`：GA/Tag Manager（`ga` 字段）
- `@vuepress/medium-zoom`：图片点击缩放
- `seo`（vuepress-plugin-seo）：为页面生成 meta（title/description/tags/url/publishedAt/modifiedAt）
- `sitemap`：生成 sitemap.xml（`hostname` 固定为站点域名）
- `vuepress-plugin-baidu-autopush`：百度链接推送
- `vuepress-plugin-tags`：标签页能力
- `vuepress-plugin-code-copy`：代码块复制按钮（成功提示文案）
- `feed`（vuepress-plugin-feed）：RSS/Atom feed（`canonical_base`、`count` 等）
- `img-lazy`（vuepress-plugin-img-lazy）：图片懒加载

### 5）ThemeConfig 与主题扩展点

`themeConfig` 的关键字段：

- `nav`：来自 [`/.vuepress/navbar.ts`](../../.vuepress/navbar.ts)
- `sidebar`：来自 [`/.vuepress/sidebar.ts`](../../.vuepress/sidebar.ts)
- `repo` / `docsBranch` / `editLinks` / `editLinkText`：用于 GitHub 仓库跳转与“编辑此页”
- `footer`：来自 [`/.vuepress/footer.ts`](../../.vuepress/footer.ts)，由主题组件 [`Footer.vue`](../../.vuepress/theme/components/Footer.vue) 渲染
- `extraSideBar`：来自 [`/.vuepress/extraSideBar.ts`](../../.vuepress/extraSideBar.ts)，由主题组件 [`ExtraSidebar.vue`](../../.vuepress/theme/components/ExtraSidebar.vue) 渲染

## 配置与主题代码的绑定关系

主题布局中会读取 `this.$site.themeConfig.footer` 与 `this.$site.themeConfig.extraSideBar`：

- 布局入口：[`Layout.vue`](../../.vuepress/theme/layouts/Layout.vue)
- 右侧工具条：[`ExtraSidebar.vue`](../../.vuepress/theme/components/ExtraSidebar.vue)
- 页脚：[`Footer.vue`](../../.vuepress/theme/components/Footer.vue)

