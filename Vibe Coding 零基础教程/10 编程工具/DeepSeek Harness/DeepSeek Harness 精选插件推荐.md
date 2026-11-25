# DeepSeek Harness 精选插件推荐

> 一次性鉴赏 DSH 社区热门插件，从实用工具到整活神器，量大管饱。

大家好，我是程序员鱼皮。

DeepSeek Harness 是 DeepSeek 官方最新开源的 AI Agent 运行环境，简称 DSH。

你可以把它理解成一个高度可定制的 AI 编程工具，对标 Claude Code 和 Codex，核心理念是「一切皆插件」。

![](https://pic.yupi.icu/1/image-20260814133452050-20260819135304416.png)

DSH 整套架构是建立在一个叫 Cordis 的元框架上的。模型适配器、工具注册表、会话日志、Agent 循环，甚至 Web 界面本身，全都是可以热插拔的插件。你想换模型、换工具、换交互方式，改一下配置就行，不用动源码。

虽然目前 DSH 自带的能力还不够丰富，但正因为这种彻底的插件化设计，社区补能力的速度非常快。才短短一周多，GitHub 的 `dsh-plugin` 标签下已经冒出了数千个社区插件，有给 Agent 补充能力的、有改进 UI 界面的、也有很多奇奇怪怪的抽象艺术作品……

![](https://pic.yupi.icu/1/deepseek%20ads.jpeg)

这篇文章我就来带大家鉴赏一大波 DeepSeek Harness 热门插件，有实用的、也有好看的。

![](https://pic.yupi.icu/chengfang/02.png)

鱼皮甄选，量大管饱。建议收藏，让你的鲸鱼变得更强！



## 发现优质 DSH 插件

首先，到哪里去找 DeepSeek Harness 的优质插件呢？

最直接的方法是看 GitHub 的 [dsh-plugin 主题专区](https://github.com/topics/dsh-plugin)。很多开发者发布插件后都会给仓库打上 `dsh-plugin` 这个标签，新出的插件基本都能在这里看到。

这个方法的优点是更新快、数量多；缺点就是鱼龙混杂，因为谁都可以给仓库加这个标签，不代表这些插件经过审核，也不能按照质量来排序。

![](https://pic.yupi.icu/chengfang/03DSH.png)

如果懒得一个个翻仓库，可以看看 [Awesome DSH Plugin](https://awesome-dsh-plugin.com/zh/)。它是社区整理出来的一份优质插件清单，按照用途做分类，便于你快速发现一些热门插件。不过它同样属于社区维护，适合拿来找插件、看热度，不能当做是官方推荐的。

![](https://pic.yupi.icu/chengfang/004DSH.png)

有趣的是，DSH 插件多起来以后，连「找插件」这件事本身都被做成插件了。

比如我后面会提到的 dsh-market 插件，把它装进 DeepSeek Harness 后就相当于多了一个插件市场。

在这里你不仅能够直接浏览和搜索插件，还能看到根据你当前已安装的插件继续推荐的相关项目。

举个例子，我不用提前知道 dsh-pocket 这个插件叫什么名字，只要搜索「远程」两个字，dsh-market 插件就会匹配到对应的项目。

![](https://pic.yupi.icu/chengfang/007DSH.png)

那怎么安装插件呢？

其实不用自己折腾命令，除了直接把 GitHub 仓库地址丢给 DeepSeek Harness 让 AI 自动安装外，DSH 0.2.1 及以上版本还内置了插件「发现」标签页，开启自定义插件索引后就能直接搜索安装（具体用法可以参考本目录中的《DeepSeek Harness 精选插件推荐（第二期）》）。老办法则是把仓库地址丢给 DSH，让 AI 自己读取仓库的 README 项目介绍文件、查找安装方式、执行安装命令，装完以后按照 AI 的提示重启 `dsh web` 就行。

![](https://pic.yupi.icu/1/image-20260814145412556.png)



## 优质 DSH 插件推荐

接下来正式进入插件推荐环节。我把这次测试过的插件分成了 3 类，分别是扩展 DSH 技能的、增强面板体验的，以及社区整活的。

下面先来看第一类，能直接给 DSH 补能力的插件。



### DSH 技能扩展



#### ModLens 让 DeepSeek 理解图片

这是我个人最看好的一个插件，给原本只能看文字的 AI 模型补了一双慧眼。

> 开源仓库：https://github.com/liustack/modlens

![](https://pic.yupi.icu/chengfang/033DSH1.png)

DeepSeek V4 系列模型只能处理纯文本。虽然 DeepSeek 官方 APP 里已经灰度上线了识图模式，但在 DSH 里调用的是 API 接口，如果你直接粘贴一张截图进对话，AI 根本看不懂。

> 补充一下：2026 年 9 月发布的 DeepSeek V4.1 Flash 已经是原生多模态模型了，可以直接看图，这个插件的必要性因此下降了很多。但如果你还在用其他纯文本模型，它依然有用。

ModLens 解决的就是这个问题。当你粘贴图片后，插件会自动把图片转发给一个外部的视觉模型（比如 Qwen），由视觉模型把图片内容解析成结构化的 JSON 信息，包括 OCR 识别出的文字、页面的布局区域，以及图片里的语义内容，然后再把这些信息作为上下文喂给 DeepSeek，让它能够基于图片内容继续推理。

![](https://pic.yupi.icu/chengfang/027DSH.png)

和普通的 OCR 工具不一样，ModLens 保留的不只是文字，还有元素之间的位置关系和语义。所以对于经常用 AI 做前端的朋友来说非常实用，页面做完以后直接把截图丢给 DSH，让它自己检查还原度就行了。



#### ModSearch 扩展搜索源

ModSearch 是一个搜索增强插件，可以给 DSH 接入 Firecrawl、Tavily、Exa 等不同搜索源，还能继续扩展 Twitter 搜索的能力。

> 开源仓库：https://github.com/liustack/modsearch

![](https://pic.yupi.icu/chengfang/034DSH1.png)

虽然 DSH 原生就自带联网搜索，但是搜索范围有限。

比如我让 AI 搜索当天 Twitter 上关于 DeepSeek Harness 的讨论，AI 明确告诉我当前搜索工具拿不到 Twitter 的实时原帖，只能从媒体和社区文章里找到一些转述内容。

![](https://pic.yupi.icu/chengfang/23DSH.png)

装上 ModSearch 后，我故意没有配置 API Key，又让 AI 搜索同一个问题。这一次 AI 直接搜到了一条 Twitter 上的原帖，点开链接就能验证。

![](https://pic.yupi.icu/chengfang/25DSH.png)

不过 Twitter 搜索到这一步并没有完全跑通，更完整的搜索能力还需要额外配置对应服务的 API Key 才能用。如果你平时需要在全网范围深度检索资料，配好之后会很香。



#### dsh-browser 操作浏览器

dsh-browser 可以让 DSH 直接操作你正在用的 Chrome 浏览器，比如读取网页内容、点击链接、填写表单、跳转页面等等。

> 开源仓库：https://github.com/Lum1104/dsh-browser

![](https://pic.yupi.icu/chengfang/035DSH.png)

和一般的无头浏览器方案不同，dsh-browser 连接的是你电脑上真实的 Chrome 标签页。浏览器里的 Cookie、Session、登录状态全都能直接复用，不需要给 AI 单独再登录一次。

它的技术方案是一个 DSH 桥接插件加一个 Chrome MV3 扩展，两边通过本地 WebSocket 通信。插件把网页内容转成结构化的文本描述（带编号的可交互元素列表）发给 DeepSeek，DeepSeek 不需要「看图」就能理解页面结构并执行操作。

这个插件的安装会稍微麻烦一点。除了安装 dsh-browser 插件本身，还得额外在 Chrome 里加载一个本地扩展。

![](https://pic.yupi.icu/chengfang/010DSH.png)

我直接让 DSH 按照插件的 README 文档自动安装。AI 把源码、依赖和扩展都构建好了，最后只需要我在 Chrome 的 `chrome://extensions` 页面手动加载本地扩展目录。

![](https://pic.yupi.icu/chengfang/26DSH.png)

扩展打开后，看到 `Connected` 就说明连接成功了。

![](https://pic.yupi.icu/chengfang/28DSH.png)

我先拿 GitHub 做了一轮测试，把自己的开源项目主页丢给它，让它找到页面里的置顶仓库，再点进去继续查看详情。

从读取页面、定位仓库，到点击进入并读取项目信息，整套流程全部跑通。

![](https://pic.yupi.icu/chengfang/821DSH.png)

接下来我又让 AI 通过 Twitter 页面搜索 DSH 相关内容。结果它真的在 Twitter 的搜索框里自动输入关键词、执行搜索，再切到最新结果查看刚发布的帖子。

![](https://pic.yupi.icu/chengfang/012DSH.png)

这和前面的 ModSearch 插件定位不同。ModSearch 更适合从搜索引擎渠道查找资料，而 dsh-browser 是让 AI 直接操作你已经登录的真实网站，适合填表、发帖、查询后台这种需要带登录态的操作。

不过 dsh-browser 并不会完全放任 Agent 随便操作。点击、输入、页面跳转这些动作默认都会弹确认框让你过目。手动切换标签页后，它也会停下来询问是继续控制原页面还是跟随当前页面。

实际使用时还有一个小细节值得注意。dsh-browser 默认绑定当前活动标签页，如果直接在 DSH 页面里让它打开 GitHub，当前聊天页面可能也会被跳走。后来我改成先打开目标网站的标签页，再从 Chrome 侧边栏发起对话，用起来就顺手多了。

![](https://pic.yupi.icu/chengfang/062DSH.png)



#### Agent Teams 组一支 Agent 团队

Agent Teams 是一个多 Agent 协作插件，可以让 DSH 同时拉起多个 Agent 各自干活，结果统一汇总到一个 Captain（队长）节点。

> 开源仓库：https://github.com/NanmiCoder/dsh-agent-teams

![](https://pic.yupi.icu/chengfang/036DSH.png)

Captain 负责拆分任务、分配工作并做最终汇总，下面的成员 Agent 则各自处理不同方向的问题。

我拿它检查了一个前端项目，创建了 3 个成员分别负责不同维度：

```
前端 Agent：检查页面结构、交互逻辑、响应式和明显的前端问题
代码质量 Agent：检查项目结构、依赖管理和代码可维护性
安全 Agent：检查敏感信息泄露、依赖风险和明显的安全隐患
```

任务跑起来以后，右边的活动面板能直接看到 3 个 Agent 同时在工作。等它们各自检查完成，结果会统一回到 Captain，由 Captain 汇总并给出最终报告。

![](https://pic.yupi.icu/chengfang/14DSH.png)

**更牛的是，这支 Agent 团队做完一次任务后不会马上消失，后面还能继续复用。**

![](https://pic.yupi.icu/chengfang/013DSH.png)

这一轮检查结束后，我又追问了一个 WebGL 降级的问题，并且指定只让 frontend 成员继续处理。结果活动面板里真的只有它重新进入了工作状态，另外两个成员没有被重复调度。

![](https://pic.yupi.icu/chengfang/014DSH.png)

所以它和临时开多个 Agent 还是有区别的。创建好的团队和成员会一直保留，后续可以按需指派任务。

对于代码审查、多维度调研这类能拆成多个方向的任务，用 Agent Teams 比较合适。但如果任务本身很简单，就没必要特意拉一支队伍，反而会增加调度时间和 Token 消耗。



#### DeepSeek Bot 打造你的个人助理

DeepSeek Bot 是社区开发者在 2026 年 10 月做的一个插件（并非 DeepSeek 官方出品），能把 DSH 变成一个 Personal Agent 个人智能体。

![DeepSeek Bot 安装文档](https://pic.yupi.icu/1/personalagent-26-deepseekbot-28af3921.png)

在 DSH 的插件页面里添加一下就能装好，然后就可以创建多个有名字、有人设的 Bot，接入飞书、微信等聊天软件，背后用什么模型也能随便换。它的记忆存在用 Git 管理的 Markdown 文件里，Bot 每次记住了什么、改了什么都能查得一清二楚。

不过它运行在你自己的电脑或服务器上，想让它 24 小时在线，还得自己准备一台不关机的机器。如果你想了解 Personal Agent 是什么、和 Grok Bot 这类大厂产品有什么区别，可以阅读本教程 AI 编程概念大全板块中的《Personal Agent 详解》。



### DSH 实用工具与界面

接下来是第二类，这些插件主要增强 DSH 的面板能力和使用体验，日常用起来更顺手。



#### dsh-market 给 DSH 装个插件市场

前面说过，DSH 插件越来越多以后，光靠自己翻 GitHub 找插件其实挺麻烦的。

dsh-market 相当于在 DSH 里内置了一个插件市场，不用离开 DSH 就能浏览、搜索和安装插件，还会根据你已经安装的插件推荐相关项目。

> 开源仓库：https://github.com/2BingLing/dsh-market

![](https://pic.yupi.icu/chengfang/050DSH.png)

常用的功能有 2 个，第一个是个性化推荐。插件知道你已经装了什么，推荐的东西会越来越对味儿，不用每次都自己寻找新的插件。

![](https://pic.yupi.icu/chengfang/35DSH.png)

第二个是按功能关键词搜索插件。比如我想找一个可以用手机远程控制 DSH 的插件，只要搜「远程」两个字就能匹配到相关项目，不需要提前记住插件名字。

![](https://pic.yupi.icu/chengfang/007DSH.png)



#### dsh-web-ui 网站功能增强

dsh-web-ui 是一个 Web 端增强插件，集成了任务看板、Git 管理、工作台、状态信息、皮肤主题和桌宠等一系列功能，装完以后整个页面会更像一个完整的开发工具。

> 开源仓库：https://github.com/zhu1090093659/dsh-web-ui

![](https://pic.yupi.icu/chengfang/038DSH1.png)

我一开始看到它的名字，还以为只是简单改改界面样式。结果装完才发现，这东西简直是一个超级全家桶！

![](https://pic.yupi.icu/chengfang/016DSH.png)

我最先试的功能是任务看板。你可以直接新建任务，写清楚要让 Agent 做什么，任务从开始到完成的进度都会显示在看板里，而且点进去还能找到真正执行这个任务的 DSH 会话。

![](https://pic.yupi.icu/chengfang/06DSH.png)

它把 Git 相关功能做得也很完整。可以直接搜索、切换和新建分支，还能把之前的代码提交记录画成一张 Git 图谱，把每次提交和不同分支之间的关系都清晰地展示出来。

![](https://pic.yupi.icu/chengfang/08DSH.png)

我装的是 `dsh-web-ui` 的全家桶版本，它还会一起安装 `dsh-better-sidebar`，所以右边会直接多出一套类似 VS Code 的开发工具栏。

![](https://pic.yupi.icu/chengfang/017DSH.png)

全家桶集成的 better-sidebar 里，文件列表还带了 `@文件` 按钮，看到需要的文件可以直接引用到当前对话里，不用再自己手动复制路径。

![](https://pic.yupi.icu/chengfang/019DSH.png)

怎么样，这个插件是不是挺强的？感觉官方没做的很多功能都被它实现了。



#### DSH-better-sidebar 加强侧边栏

DSH-better-sidebar 是一个侧边栏增强插件，把文件树、终端、Git 状态这些开发时常用的面板集中到 DSH 右侧，减少来回切窗口的麻烦。

> 开源仓库：https://github.com/omdsh-dev/DSH-better-sidebar

![](https://pic.yupi.icu/chengfang/039DSH.png)

和前面的 `dsh-web-ui` 相比，它没有任务看板、皮肤中心、桌宠这些额外功能，更专注于侧边栏本身，界面也更简洁。

![](https://pic.yupi.icu/chengfang/018DSH.png)

如果你觉得全家桶功能太多用不上，也可以只装这一个，单独用更轻量。



#### dsh-context 上下文增强

dsh-context 是一个上下文可视化插件，可以直接查看当前会话里上下文的组成情况、占用比例和变化记录。

> 开源仓库：https://github.com/bowenliang123/dsh-context

![](https://pic.yupi.icu/chengfang/040DSH.png)

用 AI 编程聊久了以后，经常会发现对话越来越慢、上下文越堆越大。但到底是历史消息、文件内容还是工具调用结果占了大头，平时其实很难直观看出来。

`dsh-context` 做的就是把这些原本藏在后台的数据直接摊开给你看。点一下上下文按钮，就能看到当前上下文的体检报告，每一类信息占了多少 Token 一目了然。

![](https://pic.yupi.icu/chengfang/38DSH.png)

如果你经常跑长会话或者频繁调用工具，它会很实用。至少上下文快顶满的时候，你能知道该清理什么，不用再盲目地直接开一个新会话。



#### dsh-TUI 终端操作界面

dsh-TUI 是一个终端交互界面插件，适合更习惯 Claude Code 那种终端操作风格的用户。

> 开源仓库：https://github.com/ccch1mneyyy/dsh-TUI

![](https://pic.yupi.icu/chengfang/041DSH.png)

装好运行以后，会直接进入一套全屏终端界面，底部实时显示当前模型、推理强度、上下文占用百分比等信息，简单粗暴。

![](https://pic.yupi.icu/chengfang/020DSH.png)

但是我不太建议新手直接装这个，因为 dsh-TUI 对 DSH 的界面和交互改动比较大，而 DSH 官方还在快速迭代中，后续如果新增了什么能力或者改了接口，这个插件不见得能第一时间跟上，到时候出了兼容问题排查起来会比较头疼。



#### dsh-genui 界面渲染

dsh-genui 是一个生成式 UI 插件，可以让 DSH 的回复不再局限于文字和 Markdown，而是直接在对话里渲染卡片、图表、选项按钮等交互界面。

> 开源仓库：https://github.com/omdsh-dev/dsh-genui

![](https://pic.yupi.icu/chengfang/042DSH.png)

我新开了一个对话，让它生成一个「AI 编程工具对比面板」，包含信息卡片和柱状图。结果真的直接在 DSH 的聊天窗口里渲染了出来，而且是实实在在可以交互的组件。

![](https://pic.yupi.icu/chengfang/37DSH.png)

如果你经常让 AI 做数据展示或者方案对比，觉得纯文字回答太单调，这个插件值得一试。



#### dsh-pocket 手机远程操控

dsh-pocket 可以把电脑上正在运行的 DSH 连接到手机上，扫一下二维码就能在手机浏览器里继续查看 Agent 的工作状态、发送消息。

> 开源仓库：https://github.com/shaobeichen/dsh-pocket

![](https://pic.yupi.icu/chengfang/043DSH.png)

这个插件支持局域网和公网两种模式，我都测试过了。

局域网模式很简单，手机和电脑连同一个 WiFi，扫描二维码后就能直接打开 DSH 界面。

![](https://pic.yupi.icu/chengfang/021DSH.png)

公网模式更通用，手机不需要和电脑在同一个网络里，随时随地可以访问。第一次打开会要求输入一个访问密码，每次重新开启公网访问时密码会自动更换。

![](https://pic.yupi.icu/chengfang/044DSH.png)

最关键的是，公网访问不需要你自己额外买服务器！dsh-pocket 会通过 Cloudflare Quick Tunnel 建立一个临时的公网通道，把外部请求转发到电脑本地运行的 DSH。手机端和电脑端之间的流式输出通过 WebSocket 全程透传，电脑上正在输出的内容手机上也能实时滚动。

也就是说，以后 DSH 在电脑上跑一个耗时较长的任务，出去吃饭的时候掏出手机还能继续看进度、发消息。

不过方便的同时，也要注意安全。远程二维码、公网地址和访问密码别随便分享给别人，毕竟 DSH 本身可以操作本机文件和代码，暴露的后果可想而知……



### DSH 整活玩法

前面两类插件多少还在认真地给 DSH 补充能力、优化体验。

接下来，插件的画风就开始逐渐跑偏。。。

![](https://pic.yupi.icu/1/e02764373d3605e8c6b758e546b52410500385529.jpg)



#### dsh-deep-whale 鲸鱼娘皮肤

deep-whale 是一个主题插件，装上以后，整个 Web 界面会直接换成鲸鱼娘风格。

> 开源仓库：https://github.com/Small-tailqwq/dsh-deep-whale

![](https://pic.yupi.icu/chengfang/045DSH1.png)

装上以后的效果，直接看图：

![](https://pic.yupi.icu/1/image-20260814133452050.png)

效果不错吧，是不是突然更有打开 DSH 的动力了？

虽然它并没有给 DSH 增加新功能，但不得不说，这种东西确实很适合社区传播，谁看了这个图不想装一个？



#### whale-girl 互动更强的桌宠

whale-girl 是一个桌宠插件，可以直接在 DSH 里养一只萌萌哒鲸鱼娘桌宠。

> 开源仓库：https://github.com/vlln/whale-girl

![](https://pic.yupi.icu/chengfang/046DSH.png)

前面的 dsh-web-ui 插件也带了桌宠功能，不过我实际对比下来，两边体验差别还挺明显的。

dsh-web-ui 自带的桌宠更像一个「工作状态提示器」，Agent 干活时会告诉你正在整理资料、任务完成了之类的。

而 whale-girl 更像以前的 QQ 宠物。鼠标悬浮上去可以看到等级和当前状态，点开菜单还能投喂、玩耍。

![](https://pic.yupi.icu/chengfang/41DSH.png)

它还会跟着 Agent 的工作状态做不同动作，比如思考的时候歪头、等待的时候打哈欠、完成任务后欢呼、空闲久了就开始睡觉。

虽然实际上没什么用，但是能提升使用 AI 的情绪价值，还要什么自行车？



#### dsh-liang-skin 滑动变祖器

dsh-liang-skin 是一个 DSH 皮肤插件，直接把推理强度滑块做成了「滑动变祖器」。

> 开源仓库：https://github.com/kingOfSoySauce/dsh-liang-skin

![](https://pic.yupi.icu/chengfang/047DSH.png)

来试试看，拖动推理强度的时候，你能够见证人物从梁子一路进化到梁祖的过程。

![](https://pic.yupi.icu/chengfang/%E6%B5%8B%E9%87%8F%E4%BB%AA.png)

这真的是碳基生物能想到的创意吗？？？

![](https://pic.yupi.icu/1/image-20260821101545031.png)



#### dsh-deepcel 把 DSH 伪装成 Excel

dsh-deepcel 是一个 Excel 风格的主题插件，装上以后整个页面会变成经典的表格界面。

> 开源仓库：https://github.com/Small-tailqwq/dsh-deepcel

![](https://pic.yupi.icu/chengfang/048DSH.png)

看下效果，还原度还是很高的吧？

![Excel 风格的 deepseek harness](https://pic.yupi.icu/1/Excel%20%E9%A3%8E%E6%A0%BC%E7%9A%84%20deepseek%20harness.jpeg)

感觉这玩意很适合经常用 Excel 办公的同学，当成一个摸鱼神器应该挺好的。



#### dsh-ads 把广告塞进 DSH

dsh-ads 是一个专门给 DSH 塞复古广告的整活插件。装上以后，整个页面会冒出各种 2005 年中文互联网风格的弹窗广告。

> 开源仓库：https://github.com/Nagi-ovo/dsh-ads

![](https://pic.yupi.icu/chengfang/066DSH.png)

信息流广告、弹窗、假杀毒、假游戏，还有各种花里胡哨的横幅，全都能往 DSH 里塞。

![](https://pic.yupi.icu/1/deepseek%20ads.jpeg)

抽象，太抽象了！你管这叫 AI 工具？



## 写在最后

最后，我把这次测试过的精选 DSH 插件按照使用场景整理成了一张图，供大家参考：

![](https://pic.yupi.icu/chengfang/032DSH.jpg)

多说两句，虽然 DeepSeek Harness 一切皆插件的设计给了大家无限的定制空间，但插件毕竟是第三方代码，尤其是会操作浏览器、Shell、文件和远程访问的插件，一定要注意安全，安装前最好去看一下仓库来源和它声明的权限范围。

而且 DSH 自身也还在快速迭代，很多插件不一定能做到完美兼容。像我这次测试过程中就遇到过因为插件版本不兼容导致 Web 无法正常启动的情况。所以我建议只安装有刚需的插件，而且要利用 Git 版本控制工具来管理本地的 DSH，出了问题也好回滚到之前正常的版本。

如果你想系统学习 DeepSeek Harness 的基础用法，可以阅读本教程编程工具板块 DeepSeek Harness 目录中的《DeepSeek Harness 保姆级入门教程》，从安装到实战一篇搞定；想继续看第二期实测的 12 个最新热门插件（如上下文压缩、费用账本、防删库安全网等），可以接着阅读《DeepSeek Harness 精选插件推荐（第二期）》。
