## Meta 深夜开源 Llama 4！首次采用 MoE，惊人千万 token 上下文，竞技场超越 DeepSeek

万万没想到。Meta 选择在周六日，发布了最新 AI 模型系列 ——Llama 4，这是其 Llama 家族的最新成员。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/NZh1Fxddxd02VSBM.webp" alt="" width="100%" />

该系列包括 Llama 4 Scout、Llama 4 Maverick 和 Llama 4 Behemoth。所有这些模型都经过了大量未标注的文本、图像和视频数据的训练，以使它们具备广泛的视觉理解能力。

Meta GenAI 负责人 Ahmad Al-Dahle 表示，Llama 4 展示了 Meta 对开源 AI、整个开源 AI 社区的长期承诺以及坚定不移的信念 —— 开放系统将产出最好的小型、中型和即将出现的前沿大模型。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/olPCqIeVLrboWERM.webp" alt="" width="100%" />

谷歌 CEO 劈查伊不禁感叹，[人工智能](https://cloud.tencent.com/product/ai-class?from_column=20065&from=20065)世界永远不无聊，恭喜 Llama 4 团队，继续前进！

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/rm0wyEVzkWCmO5GN.webp" alt="" width="100%" />

在大模型竞技场（Arena），Llama 4 Maverick 的总排名第二，成为第四个突破 1400 分的大模型。其中开放模型排名第一，超越了 DeepSeek；在困难提示词、编程、数学、创意写作等任务中排名均为第一；大幅超越了自家 Llama 3 405B，得分从 1268 提升到了 1417；风格控制排名第五。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/mbX9CddoMznCJpof.webp" alt="" width="100%" />

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/DIegOg98wou5pKdn.webp" alt="" width="100%" />

那么 Llama 4 模型系列有何特点呢？具体而言：

Llama 4 Scout 是一个拥有 170 亿激活参数和 16 个专家的模型，是同类中全球最佳的多模态模型，比前几代 Llama 模型更强大，且能适配单个 NVIDIA H100 [GPU](https://cloud.tencent.com/product/gpu?from_column=20065&from=20065)。此外，Llama 4 Scout 提供了业界领先的 10M 上下文窗口，在广泛报道的基准测试中表现优于 Gemma 3、Gemini 2.0 Flash-Lite 和 Mistral 3.1。

Llama 4 Maverick 是一个拥有 128 位专家、170 亿个激活参数模型，是同类中最好的多模态模型，在广泛报道的基准测试中击败了 GPT-4o 和 Gemini 2.0 Flash，同时在推理和编程方面取得了与新 DeepSeek v3 相当的结果 —— 激活参数不到一半。Llama 4 Maverick 提供了一流的性价比，其实验性聊天版本在 LMArena 上的 ELO 得分为 1417。

以上这两个模型是 Meta 迄今为止最好的模型，主要得益于它们是从拥有 2880 亿激活参数和 16 个专家的 Llama 4 Behemoth 模型进行知识蒸馏而来。

Llama 4 Behemoth 是 Meta 目前最强大的模型之一，也是世界上最智能的大型语言模型之一。在多项科学、技术、工程和数学（STEM）基准测试中，Llama 4 Behemoth 的表现优于 GPT-4.5、Claude 3.7 Sonnet 和 Gemini 2.0 Pro。

不过，Llama 4 Behemoth 仍在训练中，后续 Meta 会放出更多内容。

好消息是，用户现在就可以在 llama.com 和 Hugging 上下载 Llama 4 Scout 和 Llama 4 Maverick 最新模型。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/9Pbj3qr0Pugjvsui.webp" alt="" width="100%" />

所有 Llama 4 模型均采用原生多模态设计，比如上传一张图像，你可以问关于这张图像的任何问题

![转存失败，建议直接上传图片文件](<转存失败，建议直接上传图片文件 https://developer.qcloudimg.com/http-save/yehe-1754229/508a4b15681abf9d334ca0dfc15e0cb9.gif>)

Llama 4 Scout 支持长达 1000 万 token 的上下文，这是目前行业内最长的上下文长度，解锁了围绕记忆、个性化和多模态应用的新用例。

![转存失败，建议直接上传图片文件](<转存失败，建议直接上传图片文件 https://developer.qcloudimg.com/http-save/yehe-1754229/d6d6dd682331a226f683c6e7396c3a1d.gif>)

Llama 4 在图像 grounding 方面也是一流的，能够将用户提示与相关的视觉概念对齐，并将模型响应锚定到图像中的区域。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/dQLGATEior1zgFDU.webp" alt="" width="100%" />

Llama 4 还经过预训练和微调，能够理解 12 种语言的无与伦比的文本，支持全球开发和部署。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/2Xxr3oRk4SFfsGjs.webp" alt="" width="100%" />

**预训练**

Meta 在构建下一代 Llama 模型时，在预训练阶段尝试了多种新方法。

首先，**这是 Meta 首次采用混合专家（Mixture of Experts, MoE）架构**。在 MoE 模型中，单个 token 仅激活总参数的一部分。Meta 表示，MoE 架构在训练和推理时计算效率更高，在固定训练 FLOPs 预算下，相比密集模型提供更高的质量。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/ztQPiKKzKu4fvqP9.webp" alt="" width="100%" />

以 Llama 4 Maverick 模型为例，该模型拥有 170 亿激活参数和 4000 亿总参数。Meta 采用交替的密集层和混合专家（MoE）层来提高推理效率。在 MoE 层中，他们使用了 128 个路由专家和一个共享专家。每个 token 都会被发送到共享专家以及 128 个路由专家中的一个。

因此，尽管所有参数都存储在内存中，但在服务这些模型时，只有总参数的一部分被激活。这通过降低模型服务成本和延迟来提高推理效率 ——Llama 4 Maverick 可以在单个 NVIDIA H100 DGX 主机上运行，便于部署，也可以通过分布式推理实现最高效率。

Llama 4 系列模型采用原生多模态设计，通过早期融合将文本和视觉 token 无缝整合到统一的模型骨干中。早期融合是一个重大进步，因为这样能够使用大量未标记的文本、图像和视频数据对模型进行联合预训练。此外，Meta 还改进了 Llama 4 中的视觉编码器，该编码器基于 MetaCLIP，以更好地使编码器适应 LLM。

另外，Meta 还开发了一种新的训练技术，称为 MetaP，其能够可靠地设置模型超参数，例如每层的学习率和初始化规模。Meta 发现，选定的超参数在不同批量大小、模型宽度、深度和训练 token 值之间具有良好的迁移性。

Llama 4 通过在 200 种语言上进行预训练，支持开源微调工作，其中包括超过 100 种语言，每种语言都超过 10 亿 token，总体上比 Llama 3 多 10 倍的多语言 token。

此外，Meta 采用 FP8 精度进行训练，兼具质量并确保高 FLOPs 利用率。在使用 FP8 和 32K GPU 预训练 Llama 4 Behemoth 模型时，Meta 实现了每 GPU 390 TFLOPs。训练所用的数据混合总量超过 30 万亿 token，是 Llama 3 预训练数据混合量的两倍多，涵盖了多样化的文本、图像和视频数据集。

最后，Meta 还通过所谓的中期训练（mid-training）继续训练模型，提升模型核心能力，包括利用专门的数据集扩展长上下文。这使 Meta 在提升模型质量的同时，为 Llama 4 Scout 解锁了业界领先的 1000 万输入上下文长度。

**后训练**

Llama 4 Maverick 在图像和文本理解方面提供了无与伦比、行业领先的性能，能够创建跨越语言障碍的复杂人工智能应用。作为通用助手和聊天用例的产品主力模型，Llama 4 Maverick 在精确[图像理解](https://cloud.tencent.com/product/imagerecognition?from_column=20065&from=20065)和创意写作方面表现出色。

在对 Llama 4 Maverick 模型进行后训练时，最大的挑战是平衡多种输入模态、推理能力和对话能力。为了混合模态，Meta 设计了一种精心策划的课程策略，与单一模态专家模型相比，这种策略不会降低性能。

在 Llama 4 中，Meta 通过采用不同的方法对后训练流程进行了全面改进：轻量级监督微调（SFT）> 在线强化学习（RL）> 轻量级直接偏好优化（DPO）。Meta 发现，SFT 和 DPO 可能会过度约束模型，限制在线 RL 阶段的探索能力，从而导致推理、编程和数学领域的精度下降。

为了解决这一问题，Meta 使用 Llama 模型作为评判，移除了超过 50% 的标记为简单（easy）的数据，并在剩余较难的数据集上进行了轻量级监督微调（SFT）。在随后的多模态在线强化学习（RL）阶段，通过精心选择较难的提示，实现了性能的显著提升。

此外，Meta 还实施了持续在线 RL 策略，交替训练模型并使用它持续过滤并保留中等至高难度的提示。这种策略在计算和准确性权衡方面非常有益。

最后，Meta 还进行了轻量级直接偏好优化（DPO），以处理与模型响应质量相关的边缘情况，有效实现了模型智能与对话能力的良好平衡。这些改进促成了一个业界领先的通用聊天模型，具备最先进的智能和图像理解能力。

**性能**

Llama 4 Maverick 包含 170 亿激活参数、128 个专家和 4000 亿总参数，相比 Llama 3.3 70B，以更低的价格提供了更高的质量。由下表可知，Llama 4 Maverick 是同类中最佳的多模态模型，在编码、推理、多语言、长上下文和图像基准测试中，其性能超过了类似模型如 GPT-4o 和 Gemini 2.0，并且在编码和推理方面与规模更大的 DeepSeek v3.1 具有竞争力。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/Ilusha7l6FSYjYh8.webp" alt="" width="100%" />

较小模型 Llama 4 Scout 是一款通用型模型，拥有 170 亿激活参数、16 个专家和 1090 亿总参数，能够在其所属类别中提供最先进的性能。Llama 4 Scout 将支持的上下文长度从 Llama 3 的 128K 大幅提升至业界领先的 1000 万 token。这为多文档摘要、解析广泛用户活动以实现个性化任务以及推理庞大代码库等应用提供了更多可能性。

Llama 4 Scout 在预训练和后训练中均使用 256K 上下文长度，使基础模型具备强大的长上下文泛化能力。在大海捞针检索等任务中，该模型均展示了令人信服的结果。

Llama 4 架构的关键创新之一是使用无位置嵌入的交错注意力层（interleaved attention layers），并通过推理时的温度缩放来增强长上下文泛化能力。这种架构被称为 iRoPE 架构，其中 i 代表交错（interleaved）注意力层，强调其支持无限上下文长度的长期目标；RoPE 指大多数层中使用的旋转位置嵌入。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/cfCiNT5dwnYGawHq.webp" alt="" width="100%" />

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/usuVnEjcuadSu534.webp" alt="" width="100%" />

Meta 对两款模型进行了广泛的图像和视频帧静止图像训练，以赋予它们广泛的视觉理解能力，包括对时序活动及相关图像的理解。这使得模型能够在多图像输入和文本提示下轻松进行视觉推理和理解任务。这些模型在预训练时最多支持 48 张图像，并且在后训练中可以支持 8 张图像，结果良好。

Llama 4 Scout 在图像定位方面表现卓越，能够将用户提示与相关视觉概念对齐，并将模型响应锚定到图像中的特定区域。这使得大型语言模型能够更精确地进行视觉问答，更好地理解用户意图并定位感兴趣的对象。

此外，Llama 4 Scout 在编码、推理、长上下文和图像基准测试中超越了类似模型，并且比所有之前的 Llama 模型表现更强。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/nf0J197YjWF8yk7A.webp" alt="" width="100%" />

**将 Llama 推向新的尺度：2T Behemoth**

Llama 4 Behemoth 预览版是一个教师模型，也是一个多模态混合专家模型，拥有 2880 亿激活参数、16 个专家和近 2 万亿总参数。

在数学、多语言和图像基准测试中，它提供了非推理模型的最先进性能，是教授较小 Llama 4 模型的完美选择。

<img src="https://pic.code-nav.cn/post_picture/1619930914211520514/hUTxkLXhkdIsWyHW.webp" alt="" width="100%" />

对一个拥有两万亿参数的模型进行后训练是一个巨大的挑战，这要求研究者从数据规模开始，彻底重新设计和改进训练方案。为了最大化性能，Meta 不得不对监督微调（SFT）数据进行 95% 的剪枝，而较小模型的剪枝比例为 50%。这一举措是为了在质量和效率上取得必要的平衡。Meta 还发现，先进行轻量级监督微调（SFT），再进行大规模强化学习（RL），能够显著提升模型的推理和编码能力。

Meta 的强化学习（RL）方案专注于通过策略模型进行 pass@k 分析，采样难度较高的提示，并构建难度逐渐增加的训练课程。此外，在训练过程中动态过滤掉零优势的提示，并构建包含多种能力的混合提示训练批次，这些措施在数学、推理和编码方面为模型带来了显著的性能提升。最后，从多种系统指令中采样对于确保模型在推理和编码任务中保持指令遵循能力至关重要，这使得模型能够在多种任务中表现出色。

为两万亿参数的模型扩展强化学习（RL）也是一项巨大的挑战，这迫使 Meta 不得不重新设计并改进底层的强化学习基础设施，以应对前所未有的规模。

Meta 对混合专家（MoE）并行化的设计进行了优化，以提升速度，从而加快迭代过程。此外，他们还开发了一个完全异步的在线强化学习训练框架，增强了灵活性。与现有的分布式训练框架相比，后者为了将所有模型加载到内存中而牺牲了计算内存，Meta 的新基础设施能够灵活地将不同模型分配到不同的 GPU 上，并根据计算速度在多个模型之间平衡资源。这一创新使得训练效率相比上一代提升了约 10 倍。

Llama 4 Scout 和 Llama 4 Maverick 现已开放下载，地址：

- llama.com：https://www.llama.com/llama-downloads/
- Hugging Face 地址：https://huggingface.co/meta-llama

_参考链接：https://ai.meta.com/blog/llama-4-multimodal-intelligence/_

> 来源：机器之心
