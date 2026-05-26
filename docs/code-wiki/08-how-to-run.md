# 08 本地运行与构建

## 前置条件

- Node.js（建议与 CI 对齐：16.x）
- npm

补充：

- 如果你的本地 Node 版本较新（>= 17），可能在 `vuepress build` 阶段遇到 OpenSSL 相关报错（典型报错 `error:0308010C:digital envelope routines::unsupported`）。此时可临时加上环境变量绕过：

```bash
NODE_OPTIONS=--openssl-legacy-provider npm run docs:build
```

## 安装依赖

在仓库根目录执行：

```bash
npm install
```

## 本地开发（热更新）

```bash
npm run docs:dev
```

说明：

- 等价于 `vuepress dev .`（见 [`package.json`](../../package.json)）
- 配置了 `extraWatchFiles`，修改 `.vuepress/*.ts` 与 `.vuepress/sidebars/*.ts` 会触发热更新（见 [`config.ts`](../../.vuepress/config.ts)）

## 生产构建（生成静态站点）

```bash
npm run docs:build
```

构建前置动作：

- 会自动执行 `pre-docs:build`：
  - `npm run generate:sidebar ./AI`
  - `npm run generate:readme ./AI`

构建产物：

- `.vuepress/dist/`

## 构建后本地预览

仓库内提供脚本：

```bash
npm run serve
```

但该脚本依赖 `serve` 命令，而仓库未声明该依赖。建议用：

```bash
npx serve ./.vuepress/dist
```

## 常见问题

### 1）构建后侧边栏不符合预期

可能原因：

- 侧边栏由脚本按文件系统 `birthtime` 排序生成，跨平台/同步后时间可能变化
- 目录存在手写 README，但被 `genReadme.js` 覆盖

建议排查：

- 先单独运行 `npm run generate:sidebar ./AI`，检查输出的 [`ai.ts`](../../.vuepress/sidebars/ai.ts)
- 若排序需要稳定性，考虑改为“显式排序规则”（例如文件名前缀、frontmatter date）

### 2）本地能跑、CI 失败

建议对齐：

- Node 版本（CI 使用 16）
- `package-lock.json` 是否与 `npm install` 输出一致
