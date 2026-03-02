# SkillBoss - AI Agent 工具商店

> AI Agent 的一站式服务平台，100+ AI 服务，一个 API Key 搞定

## 简介

SkillBoss 是专为 AI Agent 设计的工具商店，提供 100+ AI 服务的统一 API 接口。无需管理多个 API Key，无需学习不同 SDK，30 秒即可接入使用。

## 核心优势

| 传统方式 | SkillBoss |
|---------|-----------|
| 10+ API Key 管理 | **1 个 API Key** |
| 多种 SDK 学习成本 | **OpenAI 兼容** |
| 多平台账单管理 | **统一账单** |
| 数小时配置时间 | **30 秒接入** |

## 支持的服务

### AI 模型（50+）
- **Anthropic**: Claude 4.5 Sonnet, Claude 3.7 Sonnet
- **OpenAI**: GPT-5, GPT-4o, o3, o4-mini
- **Google**: Gemini 2.5 Pro/Flash（100万上下文）
- **DeepSeek**: V3, R1
- **更多**: Qwen, Llama 4, Mistral, Cohere

### 图像/视频/音频
- **图像生成**: DALL-E 3, Flux, Stable Diffusion, Midjourney
- **视频生成**: Veo 3.1, MiniMax, Runway, Kling
- **语音**: ElevenLabs, OpenAI TTS, Whisper STT

### 数据与服务
- **数据采集**: LinkedIn, Instagram, Twitter, Google Maps
- **支付**: Stripe, PayPal
- **邮件/短信**: SendGrid, Resend, Twilio
- **托管**: Vercel, Netlify, CloudFlare

## 快速接入

### 通用安装（一行命令）

```bash
curl -fsSL https://skillboss.co/install.sh | bash
```

支持：Claude Code, Cursor, Windsurf, Gemini CLI, Kiro, Codex, Amp, Trae

### Claude Code

```bash
claude mcp add skillboss -- npx -y @skillboss/mcp-server
```

### Cursor / Windsurf / Cline

添加到 MCP 配置：

```json
{
  "mcpServers": {
    "skillboss": {
      "command": "npx",
      "args": ["-y", "@skillboss/mcp-server"],
      "env": { "SKILLBOSS_API_KEY": "sk-sb-your-key" }
    }
  }
}
```

### 直接 API 调用（OpenAI 兼容）

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.heybossai.com/v1",
    api_key="sk-sb-your-key"
)

response = client.chat.completions.create(
    model="claude-4-5-sonnet",
    messages=[{"role": "user", "content": "你好！"}]
)
```

## 相关链接

- 官网：https://skillboss.co
- 文档：https://skillboss.co/docs
- API 目录：https://skillboss.co/docs/api-catalog
- NPM：https://www.npmjs.com/package/@skillboss/mcp-server
