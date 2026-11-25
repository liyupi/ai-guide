# Vibe Coding 网站美化技巧

> 7 个方法，让你的网站告别 AI 味儿



你好，我是鱼皮。

先做个小测试，下面这几个网站，你能看出哪些是 AI 做的吗？

![](https://pic.yupi.icu/1/1769600749428-08e8524c-c71c-4ef0-b72f-feec296f5684.png)

![](https://pic.yupi.icu/1/1769600766773-a2f0782c-704f-4b17-a91a-bce1f3ee4b49.png)

![](https://pic.yupi.icu/1/1769600778173-2c16a9e4-4b3b-4d5e-9bfa-2c3f1450ab04.png)



公布答案：**全都是 AI 做的！**

![](https://pic.yupi.icu/1/1769600732342-59517bbf-7b63-4a3c-9979-76529d846259.png)

是不是觉得有点意外？

“为啥我用 AI 搓出来的网站一股子 AI 味儿？而这些网站看起来干净很多呢？”

这就是接下来我要分享的：

- 什么是 AI 编程的 AI 味儿？
- 为什么网站会有 AI 味儿？
- 怎么去除网站的 AI 味儿？

学会这些技巧后，你也能让 AI 做出更精美的网站。

⭐️ 推荐观看本文对应视频版，效果更明显：
https://bilibili.com/video/BV1QF6EBiErM


## 什么是 AI 味儿？

所谓的 AI 味儿，就是那种一眼就能看出是 AI 生成的网站，界面样式和内容风格都千篇一律。

![](https://pic.yupi.icu/1/1769600840225-3990db3e-7527-436e-a5bc-2a716fd287ab.png)

1）配色死板：蓝紫渐变色用到吐。

2）布局死板：首屏放个大标题，下面三个卡片并排。

3）字体死板：基本上就是 Inter、Roboto 等几种固定的字体。

4）Emoji 泛滥：什么 🐟4️⃣🐶 之类的，满屏幕都是表情图标。

5）内容空洞：基本没有真实图片，文字风格也比较刻板。

用户看这些网站时就一个感觉：我在跟机器人聊天。

![](https://pic.yupi.icu/1/1769600858180-10f1ed0d-f92d-47bd-b88d-9f708c3d1b09.png)



## 为什么网站会有 AI 味儿？

说了这么多问题，到底为啥会这样？

核心原因就俩字：**求稳**。

举个例子，为啥 AI 那么爱用蓝紫渐变色？

因为 AI 的训练数据里，很多现代网站采用 Tailwind 样式库，而这个库的默认主色调就是蓝紫色。AI 在学习数亿行代码时，这些颜色出现的频率是最高的，于是 AI 就认为 “现代化网站 ≈ 蓝紫色渐变”。

![](https://pic.yupi.icu/1/1769600882890-89e4170f-00bf-44b5-9f17-1ebde2d3351f.png)

并且 AI 学会了一个生存法则：**用最常见的 = 最不容易出错**。

所以当你让 AI “开发一个现代化的网站” 时，AI 为了求稳，就会选择使用蓝紫渐变色。

**那怎么破局？**

很简单，从 “请求者” 变成 “指挥官”。

不要只说需求：给我做个网站

而是要明确要求：用深灰色背景、手绘图标、不对称布局、拒绝蓝紫色。

用强有力的约束条件，逼着 AI 偏离它的舒适区。

![](https://pic.yupi.icu/1/1769600923212-e36b1723-7a7d-4772-a757-3f513a96407c.jpeg)



## 怎么去除网站的 AI 味儿？

下面分享我总结的 7 个方法，保证让你的网站摆脱 AI 味儿。

### 方法 1、让 AI 参考真实网站

最简单粗暴的一招，你看到好看的网站，直接让 AI 学。

有 4 种具体的做法：

1）如果你使用 Cursor 或者 Claude Code 等 AI 编程工具，或者利用 [Firecrawl MCP](https://www.firecrawl.dev/)，让 AI 能够直接读取网页。

![](https://pic.yupi.icu/1/1769600968915-1e80b6a6-53d2-40dd-9458-b5f8b11459c4.png)

你只需要跟 AI 说：

```markdown
请访问 ai.codefather.cn，提取它的配色方案、字体选择和布局结构，然后生成类似风格的网站。
```

AI 会自己去看那个网站，然后学着做。

![](https://pic.yupi.icu/1/1769601048258-79c99e12-f960-460d-b66f-b0420bc4619a.png)



2）如果 AI 大模型支持图片理解，你还可以把网页截图提供给 AI，搭配文字能让 AI 还原网站更准确。

![](https://pic.yupi.icu/1/1769601076313-ac8b9644-1dc1-484a-b9ea-94d0828bb8a3.png)

效果如图：

![](https://pic.yupi.icu/1/1769601123122-81bd55a5-5408-4472-b70a-e0b98fa68547.png)



3）如果你用的 AI 大模型不支持图片理解、纯文本理解又不到位，可以先利用 **截图转代码** 工具，比如 [Screenshot to Code](https://github.com/abi/screenshot-to-code)。

![](https://pic.yupi.icu/1/1769601172971-c6d47b5d-49c9-4b8e-86f2-55b2c3267e75.png)

把喜欢的网站截个图，上传上去，它直接给你转成代码。

![](https://pic.yupi.icu/1/1769601152959-ac25b585-b1e0-4b95-94a3-07acc9a2eb4e.png)

然后你再把代码喂给 AI，让它参考着做。

![](https://pic.yupi.icu/1/1769601184992-01d76651-b0c7-4987-bf51-fc3f515bd917.png)

准确度会高很多，抄样式肯定不如抄代码来的直接。

![](https://pic.yupi.icu/1/1769601222476-2dcde723-c897-4c6c-9d56-1e3ab50ac05f.png)



4）此外，还可以直接套用现成的网站模板或者 GitHub 上的开源项目。

推荐几个不错的网站模板资源：

- [VibeFather](https://vibefather.ai)（[开源提示词库](https://github.com/liyupi/awesome-vibe-coding-websites)）：鱼皮专门为 Vibe Coding 打造的 AI 网站模板库，收录了 500 多个 AI 从零生成的真实网站，涵盖各行业官网、网页版 PPT、互动科普和 3D 小游戏，每个模板都附带完整提示词、设计规范文档和在线 Demo，可以直接复制设计规范给 AI 改界面风格，或者下载源码二次开发
- [HTML5 UP](https://html5up.net/)：免费的响应式网站合集，极简风格
- [WordPress 官方主题库](https://cn.wordpress.org/themes/)：1 万多个免费主题，啥类型都有
- [Start Bootstrap](https://startbootstrap.com/)：Bootstrap 生态的免费网站模板库
- [Colorlib](https://colorlib.com/wp/free-wordpress-themes/)：提供不少免费的网站模板，设计精美

这些网站模板都有源代码，你选个不错的下载下来，把代码丢给 AI 让它去改改内容就好了，样式基本准确还原。

![](https://pic.yupi.icu/1/1769601317176-fc548cbf-fecb-4ae7-aa9e-6f573a20d59a.png)



### 方法 2、设计优先开发

这个方法特别适合做大项目。

简单来说，就是 **不要上来就让 AI 梭哈整个项目**。

比如传统做法是这样的：帮我做一个包含用户系统、后台管理的完整 SaaS 平台。

然后 AI 哗啦哗啦给你生成几十个文件，结果做完后发现页面风格不对，重新返工，浪费 Tokens。

![](https://pic.yupi.icu/1/1769601339363-dcbc5190-fdfe-4a1c-b231-885545a855bc.png)

推荐的做法是 **拆分步骤**，先让 AI 做个前端网站 Demo，纯静态页面就好。对设计满意了之后，再让 AI 基于 Demo 代码，用同样的风格开发完整项目。

你像我生成出下面这种破玩意，肯定是不能让 AI 继续开发的！

![](https://pic.yupi.icu/1/1769601353690-2df4bbca-7140-446c-af0e-f7111bc9ea98.png)



这里推荐一个很强大的 AI 设计工具 [Google Stitch](https://stitch.withgoogle.com/)。

你只需要输入一段描述，它就能生成专业的界面原型。

![](https://pic.yupi.icu/1/1769601399879-e2a70816-4e5a-4da3-b5a5-397e9c9f596f.png)

甚至你在纸上画个草图，拍照上传，它都能识别出来转成代码。

![](https://pic.yupi.icu/1/1769601433733-0fa47423-cb67-4860-993d-17fb4a463d69.png)

你还可以人工修改设计的主题风格，或者人工标注要修改的部分，让 AI 帮你快速调整。

![](https://pic.yupi.icu/1/1769601453928-09f4b942-4cb6-4df6-a2f8-047008f6011d.png)

设计完成后，导出文件或下载代码，再喂给 Cursor 等 AI 编程工具继续开发。这样风格就定下来了，不会跑偏。

![](https://pic.yupi.icu/1/1769601475052-01de6924-0e89-4ad2-b0bc-cd45e778509e.png)

当然，如果你会用 [Figma](https://www.figma.com/) 这种更专业的设计工具，你可以先在 Figma 里把网站设计得清清楚楚。

![](https://pic.yupi.icu/1/1769601491432-a98ef003-f613-43e8-9333-b709df447703.png)

然后搭配 [Figma MCP](https://github.com/GLips/Figma-Context-MCP) 扩展，让 AI 直接读取你的 Figma 设计文件，按照设计生成代码。

![](https://pic.yupi.icu/1/1769601504433-d43ef9b4-ca40-49c0-977c-170ab43af4f8.png)

此外，还有个工具叫 [Onlook](https://www.onlook.ai/)，号称为设计师准备的 Cursor，可以让设计师直接可视化编辑网页代码，设计和开发无缝衔接。

![](https://pic.yupi.icu/1/1769518652135-ad6e4342-4a01-483e-8d42-bd5e38c53550.png)



### 方法 3、丰富网站图片

一般 AI 生成的网站是没有图片的，我们可以通过添加图片让网站更个性化。

没必要让 AI 从 0 开始生图，只要告诉 AI 去主动找图、到哪里找图就好。

图片资源主要包括插画、图标、真实照片和占位图这几类。

1）插画库 [unDraw](https://undraw.co/)：有非常多免费的 SVG 插画，而且可以自定义颜色。

![](https://pic.yupi.icu/1/1769601537109-69845405-15c2-49c8-be61-ab07d9dd60ab.png)

2）图标库 [Iconify](https://iconify.design/)：20 多万个免费矢量图标

![](https://pic.yupi.icu/1/1769601552661-0984adc0-a931-434f-bf6b-bebdcfcf7585.png)

3）真实照片 [Pexels](https://www.pexels.com/)：免费高质量图库，还提供了 API 快速搜索图片

![](https://pic.yupi.icu/1/1769601563667-0d0ee4ec-6b47-403c-ae3b-fef23771b47a.png)

4）占位图 [Picsum Photos](https://picsum.photos/)：直接用 URL 指定图片尺寸，每次刷新都是不同的真实照片

![](https://pic.yupi.icu/1/1769601577827-353e909f-344c-4807-aae4-4a5d075953c9.png)



如果你的 AI 编程工具支持网页读取，可以直接让 AI 从这些网站搜索图片：

```markdown
我要开发一个摄影作品集网站
请根据需要，为网站搜索并集成图片资源：
1. 插画：使用 undraw.co，搜索与网站内容相关的插画
2. 图标：使用 Iconify 图标库
3. 真实照片：使用 Pexels 搜索真实照片
4. 占位图：使用 Picsum Photos 作为临时占位图
```



这下，生成的网站看起来成熟多了吧？

![](https://pic.yupi.icu/1/1769601635196-ea757546-bd01-4b6d-a0c7-382b315f564a.png)



### 方法 4、提示词约束

就算不搞那些花里胡哨的工具，只要跟 AI 对话时，把你的要求说清楚，一样能让网站变专业。

Claude 官方的 Cookbook 中有篇文章 [Frontend Aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics)（前端美学），专门讲怎么避免让 AI 生成具有 AI 味儿的通用设计。

![](https://pic.yupi.icu/1/1769601710440-6f8ffae7-3a7c-4b7f-afb9-2b0bca8008d5.png)

下面讲几个我自己常用的提示词技巧。

#### 1）反向提示

不要只说 “要什么”，更要说 “不要什么”。

```plain
设计禁止清单：
❌ 紫色/靛蓝色渐变
❌ 纯平背景色（必须有噪点或渐变）
❌ Hero + 三卡片布局
❌ 完美居中对齐
❌ 高深的专业名词和无意义的空话
❌ Emoji 作为功能图标
❌ 线性动画 ease-in-out
```

你把这些禁止项写清楚，AI 就不敢乱来了。



#### 2）角色设定

给 AI 定个人设，比如：

```markdown
你是一位资深独立设计师，专注于《反主流》的网页美学。
你鄙视千篇一律的 SaaS 模板，认为软件界面应该有触感和灵魂。
你的创意边界：
- "现代但不要紫色" → 可以试试深灰+橙色
- "极简但要有温度" → 用大留白+手绘插画
- "科技感但不要冰冷" → 用深色+暖色点缀
```

这样 AI 就知道，它不是在做标准答案，而是在做有个性的设计。



#### 3）拒绝空洞文案

AI 特别喜欢写那些 “听起来很厉害但啥也没说” 的文案。

你得明确告诉它文案的要求：

```plain
网站的文字内容必须做到：
- 具体化："每天节省 2 小时重复劳动"（不要说"提升生产力"）
- 口语化："用起来就像呼吸一样自然"（不要说"卓越的用户体验"）
- 带情绪："再也不用在 10 个群里找文件了"（不要说"高效协作"）
- 甚至可以挑衅："别再假装你会看完那些 PPT 了"
```

这样文案就会更有人味儿了。



#### 4）语境注入

AI 老是生成通用设计，是因为它不知道你要传达什么 “感觉”。

所以我们可以尝试 **先给 AI 喂情绪，再提设计**。

比如你要做个具有科技感的博客网站，可以这么说：

```markdown
先阅读这段话：《黑客与画家》 - 编程语言是用来思考的

现在根据这种冷静、理性的情绪设计博客首页：
- 配色：深灰+冷蓝
- 布局：理性、有序
- 感觉：沉思的、专注的
```

AI 会把视觉参数（颜色、间距、字体）和文本的情感特征（冷静、理性）对齐，生成有特定氛围的设计。

![](https://pic.yupi.icu/1/1769601745340-d621e29c-76f7-4a8f-af01-7271d88c5272-20260128202014218.png)

就像给演员说戏，不是告诉他演得开心一点，而是让他回忆一段开心的记忆，情绪自然就出来了。



#### 5）复用提示词

前面讲了这么多约束条件，你不能每次都重复人工编写一遍吧？

所以要保存提示词为项目规则文件 [AGENTS.md](https://agents.md/)，便于多次复用。

[AGENTS.md](https://agents.md/) 是一个开放标准，让不同的 AI 工具都能读取同一份规则文件，主流的 AI 编程工具（Cursor、Claude Code、Windsurf 等）都支持。

![](https://pic.yupi.icu/1/1769601770744-9db9fb73-1210-4807-8c41-3e1248a88455.png)

比如这里我给大家准备了一套提示词模板，包含了前面讲的所有技巧：

```markdown
# 项目设计规则（AGENTS.md）

## 角色设定
你是一位资深独立设计师，专注于 "反主流" 的网页美学。
你鄙视千篇一律的 SaaS 模板，追求每个像素都有温度。

## ❌ 绝对禁止项

### 配色禁止
- 紫色/靛蓝色/蓝紫渐变（#6366F1、#8B5CF6）
- 纯平背景色（必须有噪点纹理或渐变）
- Tailwind 默认色板

### 布局禁止
- Hero + 三卡片布局
- 完美居中对齐
- 等宽多栏（必须不对称）

### 文案禁止
- 高深的专业名词和无意义的空话
- Lorem Ipsum 占位文本
- 被动语态和长句

### 组件禁止
- Shadcn/Material UI 默认组件（必须深度定制）
- Emoji 作为功能图标
- 线性动画（ease-in-out）

## ✅ 必须遵守项

### 文案风格
- 口语化，像朋友聊天
- 具体化，有数字和场景
- 可以幽默、自嘲、甚至挑衅
- 每句话不超过 15 个字

### 图片系统
- 图标：使用 Iconify 图标库（https://iconify.design）
- 占位图：使用 Picsum Photos（https://picsum.photos）
- 真实图片：使用 Pexels 搜索（https://www.pexels.com）
- 插画：使用 unDraw（https://undraw.co）
```

保存这个文件为 `AGENTS.md`，放在项目根目录，以后每次跟 AI 对话，它都会自动读取这个文件，按照你的要求来工作。

![](https://pic.yupi.icu/1/1769601809476-e38cc355-3b1d-4b5c-af19-733829e0628c.png)

举个例子，输入跟之前一毛一样的需求 “帮我做个动漫视频网站”，有了规则文件后，效果立竿见影！

![](https://pic.yupi.icu/1/1769601868173-f9e1ff80-8bd6-468a-bdf3-4d1ebbea7552.png)



### 方法 5、Agent Skills

如果你觉得自己写提示词太麻烦，还有个更省事的办法 —— **Agent Skills**。

简单来说，Agent Skills 就是别人封装好的专业技能包，你直接在 AI 编程工具中安装就能用，让 AI 学会各种专业技能，比如制作 PPT、整理 Excel 表格等等。

![](https://pic.yupi.icu/1/1769601927834-226e857f-9dbb-4eca-a1d3-255fd1e0638d.jpeg)

如果想让 AI 开发的网站更精美独特，可以用下面 2 个 Skills。

#### Frontend-design

这是 Anthropic 官方出品的 [前端设计技能](https://github.com/anthropics/skills/tree/main/skills/frontend-design)，可以教 AI 生成专业设计感网站。

用法很简单，以 Claude Code 为例。

首先打开 Claude Code 并输入命令，添加官方技能市场：

```plain
/plugin marketplace add anthropics/skills
```

![](https://pic.yupi.icu/1/1769307009465-4e04d585-3f68-4fcb-a3b0-ba43ad70139a-20260127164823520-20260128201603535.png)

这就像是在你的 AI 助手里开通了一个技能商店，接下来你就可以从商店中获取技能了。

![](https://pic.yupi.icu/1/1769307026089-70a117da-b18e-4c7d-992b-1d08e30a7a0b-20260127164823553-20260128201603572.png)

在 Claude Code 中输入命令，安装官方提供的技能包：

```plain
/plugin install example-skills@anthropic-agent-skills
```

![](https://pic.yupi.icu/1/1769307063576-10e2ce68-b5cd-41c7-8d6c-da0781298929-20260127164823605-20260128201603607.png)

这个 example-skills 包含了一堆官方示例技能，包括前端设计、网页测试、动图制作等等。

![](https://pic.yupi.icu/1/1769307079120-6aaf2999-fee5-4fdb-a5e3-2ba66824b4de-20260127164823637-20260128201603651.png)

装完之后，你就可以直接让 AI 使用这些技能了。

比如你输入：帮我开发个人作品集网站。

AI 会主动问你：我发现你安装了前端设计技能，需要用它来生成更具设计感的页面吗？

![](https://pic.yupi.icu/1/1769307135496-aa2a1e4e-4e8a-43e5-a138-9a148410b52e-20260127164911476-20260128201603748.png)

确认之后，AI 会利用技能生成代码，告别蓝紫渐变、生成独特风格的精美页面。

![](https://pic.yupi.icu/1/1769307161745-c81ca221-9902-49dd-96de-a99d50a17684-20260127164929260-20260128201603790.png)

不用每次都给 AI 输入一大堆相同的提示词，装一次技能就行了。



#### UI UX Pro Max

[UI UX Pro MAX](https://ui-ux-pro-max-skill.nextlevelbuilder.io/) 是我现在用下来最顺手的去 AI 味儿技能了，专门用于提升 AI 的设计能力。

![](https://pic.yupi.icu/1/1769601961428-9c2501f0-1d85-4911-932f-714396b5e06a.png)

它支持几乎目前所有主流的 AI 编程工具，比如 Claude Code、Cursor、VS Code、Codex 等等。

用法很简单，首先按照 [开源仓库文档](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 的指引，安装官方提供的命令行工具：

```bash
npm install -g uipro-cli
```

![](https://pic.yupi.icu/1/1769307627168-c682f14b-4517-4325-ad4a-33e88661e714-20260127165342236-20260128201604037.png)

然后进入到你的项目目录下，根据使用的 AI 工具执行对应的命令。比如我这里用 Cursor：

```bash
uipro init --ai cursor
```

![](https://pic.yupi.icu/1/1769307641070-2138ef02-8f26-460a-8cdd-979c59b725de-20260127165352453-20260128201604091.png)

它会自动把技能安装到 Cursor 的配置目录里。

接下来，当你让 AI 开发一个网站时，可以使用斜杠命令手动触发技能，或者让 AI 自动识别技能。

![](https://pic.yupi.icu/1/1769307707968-1545cef4-b8e2-4bf9-b0a7-98130afc78ba-20260127165405230-20260128201604126.png)

1）AI 会根据你的需求识别出产品类型和需要的页面类型

![](https://pic.yupi.icu/1/1769307720984-a6afcae8-a5e8-4577-be7c-8356b42832ee-20260127165431384-20260128201604166.png)

2）然后调用 `search.py` 搜索脚本，在 data 目录里进行多维度搜索，找到适合的配色、字体、布局风格

![](https://pic.yupi.icu/1/1769307768048-ef58645a-6188-4af7-9865-8033602126f7-20260127165431494-20260128201604217.png)

3）综合搜索结果，生成完整的设计方案（主色调、字体组合、间距规范等）

![](https://pic.yupi.icu/1/1769307782038-59ea2231-b43d-45e3-a39f-6c36b0c7f645-20260127165431536-20260128201604239.png)

4）最后，再按照设计方案生成代码

![](https://pic.yupi.icu/1/1769307794443-ffc76a7e-24e9-4e4d-b973-ef97285fd32b-20260127165431613-20260128201604303.png)

这样一来，生成的界面既专业又有设计感。

![](https://pic.yupi.icu/1/1769307819333-fef63881-90b7-4248-8ca7-35354f8a7a7a-20260127165431745-20260128201604458.png)

AI 不需要把所有规则都背下来，而是用到哪个查哪个，这就是 Agent Skills 的精髓。

另外，如果你想让 AI 在动手写页面前直接搜索成熟的高颜值网站模板，也可以装上我开源的 **VibeFather Skill**（执行 `npx skills add liyupi/awesome-vibe-coding-websites`），这样 AI 会自动从 [VibeFather](https://vibefather.ai) 的 500 多个真实案例里挑选合适的模板、读取对应的设计文档并照着生成同款网站，既省 tokens 又能稳定摆脱 AI 味儿。



### 方法 6、反 AI 味儿组件库

前面提到，AI 为了保险，默认会选最主流的组件库，比如 Tailwind CSS、Shadcn UI 等。

这些库虽然专业，但也最容易产生 AI 味儿。

所以我们可以反其道而行之，明确告诉 AI 用一些 **小众但有特色** 的组件库。

比如 [Aceternity UI](https://ui.aceternity.com/) 这个库专门做那种炫酷效果，什么闪光粒子（Sparkles）、极光背景（Aurora Background）、流星效果（Meteors），都是高计算量的视觉组件。

![](https://pic.yupi.icu/1/1769601991258-c39a8b17-c707-4fb5-ab92-73abe8eb6d35.png)

AI 很难从零写出这么复杂的效果，但你直接让 AI 用这个库，几行代码就能搞定。

要注意，对于这些相对小众的组件库，AI 可能不太熟悉用法。建议安装 Context7 插件，可以实时查询最新文档。

![](https://pic.yupi.icu/1/1769602022954-c4712a60-e6e3-4818-b599-ca83fa41fdd3.png)

或者直接把官方文档地址发给 AI 让它参考：

```plain
必须使用 Aceternity UI 设计网站
你需要阅读官方文档来了解最新的使用方法：https://ui.aceternity.com/components
```

网站的逼格立刻就上去了，完全不像 AI 生成的。

![](https://pic.yupi.icu/1/1769602042077-97940429-7324-4ba9-938a-5897095115c8.png)

还有很多我觉得有特点的 UI 组件库：

- [Magic UI](https://magicui.design/)：150+ 动画组件，专门做微交互、流光边框、文字渐变
- [DaisyUI](https://daisyui.com/)：30+ 主题，有 cyberpunk、retro、cupcake 等风格
- [Brutalist UI](https://brutalistui.site/)：粗野主义风格，粗边框、硬阴影、高对比
- [CSS Glass](https://css.glass/)：玻璃拟态效果，半透明、模糊背景
- [ikun-ui](https://github.com/ikun-svelte/ikun-ui)：基于 Svelte.js 和 UnoCSS 的组件库
- [Radix UI](https://www.radix-ui.com/)：无样式原语组件，完全自定义
- [Mantine](https://mantine.dev/)：100+ 组件，功能丰富

像我练习时长两年半，最喜欢 [ikun-ui](https://github.com/ikun-svelte/ikun-ui) 了~

![](https://pic.yupi.icu/1/1769602061209-92ee57f0-76aa-412e-a4bb-c700094688b2.png)



### 方法 7、自主配色（扩展知识）

如果你想让网站更独特，完全走自己的路，那就得人工设计配色方案了。

这个方法适合有设计基础的朋友，可以用一些快速生成个性化配色的工具，比如：

- [Coolors](https://coolors.co/)：主流的配色生成器，按空格键随机生成，支持导出多种格式
- [Adobe Color](https://color.adobe.com/)：Adobe 官方的专业配色工具

![](https://pic.yupi.icu/1/1769602205633-22850346-ee55-4ab3-916d-c54e0f66fae2.png)

生成好配色后，把色值告诉 AI，让它严格按照你的配色方案来设计。这样出来的网站，配色绝对独特。



## 实战案例

前面我讲的这些方法是可以结合使用的。下面分享几个实战例子，大家可以感受下效果。

### 案例 1、个人技术博客

#### 优化前

直接输入提示词：

```markdown
开发个人技术博客网站首页
```

效果是这样的，一眼 AI……

![](https://pic.yupi.icu/1/1769602233437-c2df5654-4dc2-407d-86f8-c95888c446fd.png)



#### 优化后

使用 `AGENTS.md` 提示词规则 + UI UX Pro Max 技能：

```markdown
开发个人技术博客网站首页
```

得到的网站更有极客范儿，内容更充实。

![](https://pic.yupi.icu/1/1769602249372-66ac1c3f-7aaa-4890-be04-5a3615226d49.png)

![](https://pic.yupi.icu/1/1769602300430-f710cad3-dedb-4035-869c-42ef76467e95.png)



### 案例 2、SaaS 产品落地页

#### 优化前

直接输入提示词：

```markdown
开发 SaaS 产品《服务器运维监控平台》的落地页
```

效果是这样的，又是蓝紫配色，一眼 AI……

![](https://pic.yupi.icu/1/1769602314736-88e9b6e7-a14a-4ea3-99f4-5a2626c0d880.png)



#### 优化后

使用 `AGENTS.md` 提示词规则 + UI UX Pro Max 技能 + 语境注入 + 反 AI 味儿组件库：

```markdown
开发 SaaS 产品《服务器运维监控平台》的落地页

先阅读这段话感受氛围：《黑客帝国》你选择蓝色药丸还是红色药丸？
必须使用 Aceternity UI 设计网站
你需要阅读官方文档来了解最新的使用方法：https://ui.aceternity.com/components
```

网站背景变成了代码雨，也更像一个专业产品介绍页：

![](https://pic.yupi.icu/1/1769602346623-9d0988bb-5904-4328-9e87-9698bd9476f0.png)

![](https://pic.yupi.icu/1/1769602360859-110bfa1e-e0e5-4276-8074-883f7c7ddae9.png)



### 案例 3、健身 APP 落地页（移动端）

#### 优化前

直接输入提示词：

```markdown
开发健身 APP 落地页（移动端）
```

效果…… 这啥玩意，不评价了……

![](https://pic.yupi.icu/1/1769602385367-1a74cdeb-7452-471d-b13b-3afdddb6fb81.png)



#### 优化后

使用 `AGENTS.md` 提示词规则 + UI UX Pro Max 技能 + 反 AI 味儿组件库：

```markdown
开发健身 APP 落地页（移动端）

必须使用 IKun UI 设计网站
你需要阅读官方文档来了解最新的使用方法：https://ikun-ui.netlify.app
```



这下得到的页面更真实可用了，对比还是非常明显的吧！

![](https://pic.yupi.icu/1/1769602473561-48f4ba99-d41a-462d-a7d3-6ea8613c43ba.png)



## 写在最后

看到这里你应该意识到，现在 AI 开发网站的能力已经非常强了。

有朋友觉得 AI 生成的效果不理想，可能只是因为没给它足够明确的指令。

就像一个厨师，你只说做个好吃的，他为了保险只能做最大众化的家常菜。但你说 “多放辣椒、不要花椒、多放豆瓣酱”，他就能做出你想要的味道。

**记住，AI 是工具，你才是主导者。**

学会了或者学废了的朋友们，点个赞吧~ 



## 推荐资源

1）鱼皮 AI 导航网站：[AI 资源大全、最新 AI 资讯、免费 AI 教程](https://ai.codefather.cn)

2）编程导航学习圈：[学习路线、编程教程、实战项目、求职宝典、交流答疑](https://www.codefather.cn)

3）程序员面试八股文：[实习/校招/社招高频考点、企业真题解析](https://www.mianshiya.com)

4）程序员写简历神器：[专业模板、丰富例句、直通面试](https://www.laoyujianli.com)

5）1 对 1 模拟面试：[实习/校招/社招面试拿 Offer 必备](https://ai.mianshiya.com)
