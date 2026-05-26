# 07 CI/CD 与自动化

本仓库的自动化主要通过 GitHub Actions 实现，配置位于：[`/.github/workflows/`](../../.github/workflows/)

## 1）构建并部署到腾讯云 COS

工作流：[`deploy.yml`](../../.github/workflows/deploy.yml)

### 触发条件

- `push` 到 `main`
- `workflow_dispatch` 手动触发

### 关键步骤

- Node 16 + `npm install`
- `npm run docs:build` 构建静态站点（产物 `.vuepress/dist/`）
- Python 3.10 + `pip install coscmd`
- `coscmd upload -r .vuepress/dist/ /` 上传到 COS
- 成功后安装 `nodemailer` 并执行 `send-email.js` 发送邮件通知

### Secrets（必须在仓库设置中配置）

COS 上传相关：

- `TENCENT_SECRET_ID`
- `TENCENT_SECRET_KEY`
- `COS_BUCKET`
- `COS_REGION`

邮件通知相关：

- `EMAIL_USER`
- `EMAIL_PASS`
- `EMAIL_TO`

安全注意：

- `EMAIL_PASS` 对 QQ 邮箱通常是“授权码”，不是登录密码
- 工作流中会执行 `npm install nodemailer`，这是运行时临时安装；若希望更可控，可考虑将 `nodemailer` 固定为项目依赖

## 2）同步 Vibe 教程变动内容到后端服务

工作流：[`sync-vibe-coding-course.yml`](../../.github/workflows/sync-vibe-coding-course.yml)

### 目标

在 push 发生时，把本次提交相对上一提交的文件变更列表（新增/修改/删除）POST 到一个后端接口，用于触发站外系统的内容同步或索引刷新。

### 核心逻辑

- `fetch-depth: 0` 拉取完整 git 历史（便于 diff）
- 兼容首次 push：`github.event.before` 为空树时，降级为父提交或空树 diff
- `git diff --name-only --diff-filter=<A|M|D>` 获取文件列表
- `jq` 把列表转成 JSON 数组，并构造 payload：
  - `repository`
  - `addedFileList`
  - `modifiedFileList`
  - `deletedFileList`
- `curl -X POST`，并使用 `Authorization: Bearer $AUTH_TOKEN`

### Secrets

- `SYNC_AI_GUIDE_URL`：后端接口地址（脚本中映射为 `POST_URL`）
- `SYNC_AI_COURSE_TOKEN`：Bearer token（脚本中映射为 `AUTH_TOKEN`）

可靠性注意：

- 工作流依赖 `jq`；`ubuntu-latest` 通常自带，但如果 runner 镜像变化，可在脚本中显式安装
- 该工作流只同步“文件列表”，不上传内容正文；后端需要自行根据 repo + 文件路径拉取/处理

