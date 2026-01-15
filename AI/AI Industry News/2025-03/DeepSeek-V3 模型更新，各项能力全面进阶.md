# DeepSeek-V3 模型更新，各项能力全面进阶

DeepSeek V3 模型已完成小版本升级，目前版本号 DeepSeek-V3-0324，用户登录官方网页、APP、小程序进入对话界面后， **关闭深度思考** 即可体验。API 接口和使用方式保持不变。

如非复杂推理任务，建议使用新版本 V3 模型，即刻享受速度更加流畅、效果全面提升的对话体验。

---

## 模型能力提升一览

### 推理任务表现提高

新版 V3 模型借鉴 DeepSeek-R1 模型训练过程中所使用的强化学习技术，大幅提高了在推理类任务上的表现水平，在数学、代码类相关评测集上取得了超过 GPT-4.5 的得分成绩。

![](https://cdn.deepseek.com/api-docs/v3_0324_benchmark.webp)

### 前端开发能力增强

在 HTML 等代码前端任务上，新版 V3 模型生成的代码可用性更高，视觉效果也更加美观、富有设计感。

![](https://cdn.deepseek.com/api-docs/v3_0324_gif.gif)

### 中文写作升级

在中文写作任务方面，新版 V3 模型基于 R1 的写作水平进行了进一步优化，同时特别提升了中长篇文本创作的内容质量。

![](https://cdn.deepseek.com/api-docs/v3_0324_example_1.webp)

![](https://cdn.deepseek.com/api-docs/v3_0324_example_2.webp)

### 中文搜索能力优化

新版 V3 模型可以在联网搜索场景下，对于报告生成类指令输出内容更为详实准确、排版更加清晰美观的结果。

![](https://cdn.deepseek.com/api-docs/v3_0324_example_3.webp)

此外，新版 V3 模型在 **工具调用、角色扮演、问答闲聊** 等方面也得到了一定幅度的能力提升。

---

## 模型开源

DeepSeek-V3-0324 与之前的 DeepSeek-V3 使用同样的 base 模型，仅改进了后训练方法。私有化部署时只需要更新 checkpoint 和 tokenizer_config.json（tool calls 相关变动）。模型参数约 660B，开源版本上下文长度为 128K（网页端、App 和 API 提供 64K 上下文）。V3-0324 模型权重下载请参考：

- Model Scope: [https://modelscope.cn/models/deepseek-ai/DeepSeek-V3-0324](https://modelscope.cn/models/deepseek-ai/DeepSeek-V3-0324)
- Huggingface: [https://huggingface.co/deepseek-ai/DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324)

与 DeepSeek-R1 保持一致，此次我们的开源仓库（包括模型权重）统一采用 MIT License，并允许用户利用模型输出、通过模型蒸馏等方式训练其他模型。

- [模型能力提升一览](https://api-docs.deepseek.com/zh-cn/news/news250325#%E6%A8%A1%E5%9E%8B%E8%83%BD%E5%8A%9B%E6%8F%90%E5%8D%87%E4%B8%80%E8%A7%88)
  - [推理任务表现提高](https://api-docs.deepseek.com/zh-cn/news/news250325#%E6%8E%A8%E7%90%86%E4%BB%BB%E5%8A%A1%E8%A1%A8%E7%8E%B0%E6%8F%90%E9%AB%98)
  - [前端开发能力增强](https://api-docs.deepseek.com/zh-cn/news/news250325#%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E8%83%BD%E5%8A%9B%E5%A2%9E%E5%BC%BA)
  - [中文写作升级](https://api-docs.deepseek.com/zh-cn/news/news250325#%E4%B8%AD%E6%96%87%E5%86%99%E4%BD%9C%E5%8D%87%E7%BA%A7)
  - [中文搜索能力优化](https://api-docs.deepseek.com/zh-cn/news/news250325#%E4%B8%AD%E6%96%87%E6%90%9C%E7%B4%A2%E8%83%BD%E5%8A%9B%E4%BC%98%E5%8C%96)
- [模型开源](https://api-docs.deepseek.com/zh-cn/news/news250325#%E6%A8%A1%E5%9E%8B%E5%BC%80%E6%BA%90)

> 来源：deepseek 官方
