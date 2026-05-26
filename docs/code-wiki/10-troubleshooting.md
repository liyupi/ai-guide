# 10 常见问题排查

## 1）`npm run serve` 报错：找不到 `serve`

原因：

- `package.json` 提供了 `serve: "serve ./.vuepress/dist"`，但没有声明 `serve` 依赖

解决：

- 推荐直接使用：`npx serve ./.vuepress/dist`
- 或将 `serve` 加入 `devDependencies` 后再使用 `npm run serve`

## 2）批量格式化 Markdown 后标题异常

相关脚本：[`formatMdContent.js`](../../.vuepress/scripts/formatMdContent.js)

现状：

- `firstLine` 的计算方式会得到“第一个字符”而不是第一行，导致判断与替换逻辑不正确

建议：

- 修复脚本后再执行批处理
- 在小范围目录试运行并做 git diff 复核，避免内容被批量污染

## 3）侧边栏顺序在不同机器上不一致

相关脚本：[`generateSidebar.js`](../../.vuepress/scripts/generateSidebar.js)

原因：

- 使用文件系统 `birthtime` 排序，跨平台/解压/同步后可能变化

建议：

- 若需要稳定顺序：采用“显式顺序约定”
  - 文件名前缀序号（如 `01-xxx.md`）
  - frontmatter date + 自定义排序逻辑

## 4）CI 同步工作流失败（curl/jq/git diff）

相关工作流：[`sync-vibe-coding-course.yml`](../../.github/workflows/sync-vibe-coding-course.yml)

排查要点：

- 是否配置了 secrets：`SYNC_AI_GUIDE_URL` / `SYNC_AI_COURSE_TOKEN`
- 后端接口是否返回非 2xx（工作流使用 `--fail-with-body` 会使 job 失败）
- runner 环境是否具备 `jq`（如镜像调整导致缺失）

## 5）构建报错：`error:0308010C:digital envelope routines::unsupported`

现象：

- 运行 `npm run docs:build` 时在 terser/webpack 阶段失败

原因：

- VuePress v1 的构建链路依赖的部分 webpack/terser 逻辑与新版本 Node(OpenSSL 3+) 不兼容

解决：

- 优先选择与 CI 一致的 Node 16
- 或临时使用：

```bash
NODE_OPTIONS=--openssl-legacy-provider npm run docs:build
```
