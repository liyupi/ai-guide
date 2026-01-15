## Cursor 迎来了强大的对手，Augment Code 实测

## Augment Code 介绍

根据官方介绍，Augment Agent 是首个转为大型代码库工作的专业软件工程师设计的 AI 编码助手，上下文支持 200K，也就是 20 万的 token 啊。

这对于专业的编程人员来讲，太实用了，已经达到可以做项目级别了。

除此之外，Augment Agent 还支持持久性的内存，就是它可以学习你的编码风格，记得你之前的重构，适配你的代码规范。记忆会随着时间的推移而积累。你不必在每次会话中重新教它。

除了基本的编码支持，Augment Agent 还支持多模态输入，如截图和 Figma 文件，用于修复错误和实现 UI。

另外，目前 Augment Agent 通过结合 [Anthropic](https://zhida.zhihu.com/search?content_id=256145915&content_type=Article&match_order=1&q=Anthropic&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDQ1NDcyMjEsInEiOiJBbnRocm9waWMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTYxNDU5MTUsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.s-Qlz5_gQXKB-83ew6fdNuoqCgOSZ69vCoaXwefWdcQ&zhida_source=entity) 的 [Claude Sonnet 3.7](https://zhida.zhihu.com/search?content_id=256145915&content_type=Article&match_order=1&q=Claude+Sonnet+3.7&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDQ1NDcyMjEsInEiOiJDbGF1ZGUgU29ubmV0IDMuNyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI1NjE0NTkxNSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.Ks9wyI53nxEYvxg3d-2qBm9e_IipirNvX86aSq5yKeM&zhida_source=entity) 和 [OpenAI](https://zhida.zhihu.com/search?content_id=256145915&content_type=Article&match_order=1&q=OpenAI&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDQ1NDcyMjEsInEiOiJPcGVuQUkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTYxNDU5MTUsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.dos4DrsF8bBrrMJP56gBcEBaRRvD_smBaFOX4vPO-s8&zhida_source=entity) 的 [O1 推理模型](https://zhida.zhihu.com/search?content_id=256145915&content_type=Article&match_order=1&q=O1+%E6%8E%A8%E7%90%86%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDQ1NDcyMjEsInEiOiJPMSDmjqjnkIbmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTYxNDU5MTUsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.JukcV5qUlsKbGMIXftuvbN_W1ZFODYvuca55rKQbIew&zhida_source=entity)，在 SWE-bench verified 基准测试中取得了最高分，达到第 1 名（在真实任务上达到 65.4%）。

![](https://pic4.zhimg.com/v2-853df9931204536656d9bcc20e9b6b41_1440w.jpg)

### **简介**

Augment 是一款开发者 AI 平台，它能帮助你理解代码、调试问题并快速交付，因为它理解你的代码库。使用聊天、下一编辑和代码补全功能，让你更高效地完成任务。

![](https://pic3.zhimg.com/v2-81ff73655aec503a4c5d199c65d23ab6_1440w.jpg)

核心宣传点：

1.  1\. Chat（聊天）：永远不再为开始而卡壳。聊天将帮助你快速熟悉不熟悉的代码。
2.  2\. 下一代编辑器：通过逐步引导您完成复杂或重复性的更改，帮助您持续推进任务。
3.  3\. 代码补全：智能代码建议，即可了解您的代码库。

这里我推荐一个非常好用的手指筷子，在平时玩手机、电脑工作、刷剧的时候想吃零食又不想脏手，非常实用和实惠，我买了两双，爱不释手。现在卖的很便宜

## Augment Code 试用

### 安装

目前提供了 `vscode` 扩展、`[JetBrains IDEs](https://plugins.jetbrains.com/plugin/24072-augment)` 插件、`VIM` 这三种使用方式，下面通过安装 `vscode` 扩展来使用。

![](https://pic3.zhimg.com/v2-07c20988b2528ebc2afaf0ae4e252586_1440w.jpg)

安装成功之后，需要进行登陆，登陆成功之后就可以使用了；目前测试下来 `remote` 模式的 `vscode` 登陆不上，本地的可以。

### 使用

刚好有一份 `vllm` 项目的代码，而且也不太懂，测试一下看能不能把我讲明白。

1.  1\. 先导入一个项目；导入之后它就会进行索引整个项目

![](https://pic4.zhimg.com/v2-e32ef7b78fe5e1806f8eb21a169b6877_1440w.jpg)

`vllm` 最核心的就是 `PagedAttention` 的原理，但是从之前看过一些介绍来看，只是明白了，但还不知道是如何实现的。

`PagedAttention` 的核心就是把 `Attention` 的加载从一个连续的显存空间拆分成了按显存页进行加载，使 `GPU` 的显存利用率增高。

### 问出了第一个问题：介绍`PagedAttention`

![](https://pic1.zhimg.com/v2-61eae47f81f8ff0f103bbab2460587ee_1440w.jpg)

1.  1\. 核心架构，这个我去看了代码确实是对的，在 `vllm/attention/backends` 目录下的 `abstract.py` 文件中有这个抽象类的定义。还提到了它有多个实现类，这个有点问题，真实的实现类比这个多，比如缺少 `CPUMLABackend` 等等，还有好几个。

![](https://picx.zhimg.com/v2-4a590484b0469126da5eadcc1a669f83_1440w.jpg)

1.  1\. 讲了主要实现类以及文件位置 `PagedAttention` 都是对的。

![](https://pic1.zhimg.com/v2-01b8530c85a4c9a7f6d2c51aba8198c0_1440w.jpg)

1.  1\. 突然讲到了 `KV Cache` 管理，有点奇怪。

![](https://picx.zhimg.com/v2-8b011e657689ee491bfbba7f559127fd_1440w.jpg)

1.  1\. `Attention` 的计算实现 `forward_decode` 。提到有两种模式 `Decode` 和 `Prefix` ，对应的就是 `forward_decode` 和 `forward_prefix` 这两个函数。

![](https://pic3.zhimg.com/v2-171799c5d28eac69ee4fe2a0cde2875a_1440w.jpg)

1.  1\. 后面又补充了说支持很多硬件，算是给第一点进行补充，

![](https://pic1.zhimg.com/v2-1a0b724040dbfde5dd24c931656d1e74_1440w.jpg)

这个问题问下来算是对这块的代码基本有一个了解了；比直接看确实强很多

### 第二个问题：让它帮我添加一个新模型

```text
帮我添加 Salesforce/SFR-Embedding-Code-2B_R 这个新的模型在 vllm 中运行；目前 vllm 的代码还不能运行它。你需要去 huggingface 上查看模型 https://huggingface.co/Salesforce/SFR-Embedding-Code-2B_R/blob/main/config.json 文件，获取它的 architectures 信息，之后才能添加模型注册；其它还需要参考 https://huggingface.co/Salesforce/SFR-Embedding-Code-2B_R/blob/main/modeling_gemma2.py 中的实现使其在 vllm 中能运行。
```

首先还是使用 `chat` 模式，进行了多次 输入的调整，但是依然回复的牛头不对马嘴；于是选用 `Agent` 模式进行测试一下。

还是使用上面的提示此。

1.  1\. 第一点另我意外的是它居然真的去下载文件回来进行查看了。因为它需要知道这个模型架构的类型，就需要读取 `config.json` 文件，在 `chat` 模式下都是给我乱说的。

![](https://pic1.zhimg.com/v2-d4e5a7b16ed3e52c7737d0788709a8ae_1440w.jpg)

1.  1\. 然后它列出了执行计划，涉及到四个步骤；第一步这个模型架构就描述对了。

![](https://pic1.zhimg.com/v2-2894c4649381edfa199861a5e613eb56_1440w.jpg)

1.  2\. 它给我实现出来了，我直接进行测试一下，而且它还贴心的给了测试文件。

![](https://pic1.zhimg.com/v2-f6f1d2e5dae15a48a046f1d613ae1f1e_1440w.jpg)

尝试运行之后发现还不能跑，有 bug，也可能和它训练时候的 `vllm` 版本代码有关，导入的很多包路径都有问题。

### 第三个问题：做一个微信小程序

```text
帮我设计和实现一个微信小程序的项目，同时帮我实现后端 golang web 服务和数据库 mysql 表，项目主要功能是家庭图书管理系统，记录家庭购买的书籍以及存放位置信息等；主要有三页面，第一个页面是首页，主要展示家庭图书信息，可以支持搜索图书，需要通过调用后端 API 把功能实现。第二个页面是一个图书录入页面，通过扫描图书的 ISBN，然后通过后端的 ISBN 查询接口去查询图书的基本信息，包括作者、出版时间、价格等等；第三个页面是我的页面，主要是可以邀请家庭成员进入这个图书馆，查看图书所在位置和有那些图书。
```

把提示此输入之后，大概 20 分钟给我实现了前端、后端、数据库表设计，并且最后都可以成功的执行。

1.  1\. 小程序

![](https://pic3.zhimg.com/v2-ee83116db8d8fd6d83744eea172aa012_1440w.jpg)

1.  2\. 后端自动给我启动之后调用 API 报错了，说明前端已经自动给我添加这个实现了。

![](https://pic3.zhimg.com/v2-257c1054a7de5c4540505c8285e97eaa_1440w.jpg)

1.  3\. 我本地没有数据库，让它给我用 docker 启动并且创建表

![](https://picx.zhimg.com/v2-03888823ffe6478848e3de50a2e7148f_1440w.jpg)

## 对比 Cursor

首先给我的感觉就是比 Cursor 可以执行的东西跟多了，而且执行很快，不知道是因为他们的模型快还是什么原因，总之很快，而且准确率很高。

在不久的将来，感觉像 `WEB` 程序只需要三个角色就可以做出一个系统来：

- • 一个 UI 设计，把所有的页面样式、图标设计好，给到工具。
- • 一个产品经路，把业务逻辑梳理清楚。
- • 一个架构师，把系统架构设计出来，设计出合理的数据库、接口定义等这些。

之后就可以通过工具自动化的生成、打包、部署然后就可以进行测试了。

### 引用链接

[1] abstract.py: _[http://abstract.py](https://link.zhihu.com/?target=http%3A//abstract.py)_

> 来源：知乎
