# DeepSeek官方整理的模型应用和工具

今天给大家介绍一个由 DeepSeek 团队维护的项目 Awesome DeepSeek Integration，该项目整理了与 DeepSeek 模型相关的各种应用和工具。

DeepSeek 本身做的是基础的模型，很少涉及应用，只对外提供 API 接口，我们可以通过 API 将 DeepSeek 大模型能力轻松接入各类软件。

另外 DeepSeek 大模型本身是开源的，我们自己也可以搭建一个本地的大模型应用。

Awesome DeepSeek Integration 刚好提供了一些用于与 DeepSeek 等 AI 平台集成的资源、工具和库的集合。

**开源地址：https://github.com/deepseek-ai/awesome-deepseek-integration**

目前该项目已经收获了 15k+ 的 Star:

![图片](https://pic.yupi.icu/yuyi/640-20250220181106646)

DeepSeek 火了之后，该 Star 数是直线上升：

![图片](https://pic.yupi.icu/yuyi/640-20250220181106711)

Awesome DeepSeek Integration 是一个精选列表，包含了多种与 DeepSeek 模型集成的应用程序、工具和插件，涵盖了日常对话、AI 编程、大模型开发、知识库等多个领域。

通过这些工具和应用可以帮助开发者和用户更方便地使用 DeepSeek 模型，提升生产力和效率。

------

**1. 桌面客户端**



**QuantaLogic：**一个用于打造高级 AI 助手的框架，帮助开发者设计能思考和行动的智能体，提升 AI 解决问题的能力。

**Chatbox：**电脑端的 AI 聊天软件，支持 Windows、Mac 和 Linux，可接入多种 AI 模型，方便随时与 AI 交流。

**ChatGPT-Next-Web：**网页版工具，支持跨设备无缝切换，快速使用 DeepSeek，随时随地与 AI 聊天。

**留白记事：**微信上的智能助手，通过 DeepSeek 功能管理笔记、任务、日程和待办清单。

**Pal：**iPhone 和 iPad 上的 AI 助手应用，随时随地解答问题、处理任务。

**LibreChat：**开源的 AI 聊天工具，可定制性强，能与 DeepSeek 无缝结合，提供个性化交互体验。

![图片](https://pic.yupi.icu/yuyi/640-20250220181106893)

------

**2. AI Agent 框架**

**Anda：**一个用 Rust 语言开发的 AI 智能体框架，能让智能体自主运行、记住事情，并通过 DeepSeek 等模型变得更聪明，适合构建高效、安全的智能体网络。

**YoMo：**一个支持强类型语言的“有状态无服务器”框架，方便开发者快速构建和管理复杂的 AI 应用，特别适合需要记住用户操作的场景。

**Alice：**基于区块链的 AI 代理，利用 DeepSeek 等模型进行决策，能管理代币、挖矿和参与生态治理，是区块链和 AI 结合的智能助手。

**ATTPs：**一个智能体之间的通信协议框架，让不同平台的智能体可以安全、可信地交流，支持注册、发送和接收可验证数据，实现高效协作。

![图片](https://pic.yupi.icu/yuyi/640-20250220181106957)

------

**3. RAG 框架**

**RAGFlow：**RAGFlow 是一款开源的 RAG（检索增强生成）引擎，基于深度文档理解技术。它支持多种复杂格式的数据，结合大语言模型（LLM），提供可靠的问答和有理有据的引用。

**AutoFlow：**AutoFlow 是一个开源的知识库工具，基于 GraphRAG 构建，支持 TiDB Vector、LlamaIndex 和 DSPy。它提供类 Perplexity 的搜索页面，可轻松集成到网站中。

**DeepSearcher：**DeepSearcher 结合了强大的 LLM（如 DeepSeek 和 OpenAI）和向量数据库（如 Milvus），基于私有数据进行搜索、评估和推理，提供高度准确的答案和全面的报告。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107016)

------

**4. Solana 框架**

Solana Agent Kit：一个开源工具包，用于将 AI 智能体连接到 Solana 区块链协议。它支持任意 AI 模型的代理自主执行 60 多种 Solana 操作，包括代币交易、NFT 创建与管理、借贷、空投等。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107100)

------

**5. 即时通讯插件**

**茴香豆：**一个集成到个人微信群或飞书群的领域知识助手，专注于解答问题，不闲聊。

**LangBot：**一个大模型原生即时通信机器人平台，适配 QQ、企微、飞书等多种消息平台。

**NoneBot：**基于 NoneBot 框架的智能对话工具，支持 QQ、飞书、Discord、TG 等多种消息平台。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107190)

------

**6. 浏览器插件**

**沉浸式翻译：**一款双语对照网页翻译插件，简洁高效。

**沉浸式导读：**一款无侧边栏的沉浸式 AI 网页摘要插件。

**ChatGPT Box：**将 LLM 作为私人助手整合到浏览器中的插件。

**划词翻译：**整合多家翻译 API 和 LLM API 的浏览器翻译插件。

**欧路翻译：**提供划词搜索、逐段对照翻译、PDF 翻译等功能，支持 DeepSeek、Bing、GPT、Google 等多种翻译引擎。

**流畅阅读：**一款革新性的浏览器开源翻译插件，提供母语般的阅读体验。

**馆长：**知识库 AI 问答助手，帮助整理与分析知识。

**RssFlow：**一款智能 RSS 阅读器浏览器扩展，支持 AI 驱动的 RSS 摘要和多维度订阅视图。

**Typral：**超快的 AI 写作助手，帮助优化日报、文章等文本。

**Trancy：**沉浸式双语对照翻译、视频双语字幕、划句/划词翻译插件。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107315)

------

**7. VS Code 插件**

**Continue：**开源 IDE 插件，使用 LLM 作为编程助手。

**Cline：**一款能够与 CLI 和编辑器配合使用的 AI 助手。

**AI Commit：**使用 AI 生成 Git commit message 的 VS Code 插件。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107397)

------

**8. neovim 插件**

**avante.nvim：**开源 IDE 插件，使用 LLM 作为编程助手。

**llm.nvim：**支持任意大模型（如 Deepseek、GPT）的 Neovim 插件。

**minuet-ai.nvim：**支持多个主流大模型的实时代码补全插件。

**codecompanion.nvim：**AI 驱动的编码插件，无缝集成到 Neovim。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107448)

------

**9. JetBrains 插件**

**Chinese-English Translate：**集成多家翻译和 AI 厂商的 JetBrains 插件，支持中英文翻译。

**AI Git Commit：**使用 AI 生成 Git commit message 的 JetBrains 插件。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107501)

------

**10. AI Code编辑器**

**Cursor：**基于 VS Code 扩展的 AI Code 编辑器。

**WindSurf：**基于 VS Code 的 AI Code 编辑器。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107589)

------

**11. 其他**

**Abso：**TypeScript SDK，支持 OpenAI 格式与任何 LLM 提供商交互。

**ShellOracle：**用于智能 Shell 命令生成的终端工具。

**深度求索（快捷指令）：**使用 DeepSeek API 增强 Siri 能力的快捷指令。

**n8n-nodes-deepseek：**支持将 DeepSeek API 集成到 n8n 工作流的社区节点。

**promptfoo：**用于测试和评估 LLM 提示的工具，支持比较不同 LLM 提供商的响应。

**deepseek-tokenizer：**一个轻量级的 tokenization 库，仅依赖 tokenizers。

**deepseek-review：**使用 Deepseek 进行代码审核的工具，支持 GitHub Action 和本地使用。

**WordPress AI 助手：**对接 Deepseek API，用于 WordPress 站点的 AI 对话、文章生成和总结插件。

![图片](https://pic.yupi.icu/yuyi/640-20250220181107651)