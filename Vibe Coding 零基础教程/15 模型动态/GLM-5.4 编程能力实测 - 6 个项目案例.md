# GLM-5.4 编程能力实测 - 6 个项目案例

> 智谱首款 Loop Transformer 旗舰模型，用 6 个项目实测编程和 3D 能力



大家好，我是程序员鱼皮。

2026 年 11 月，智谱发布了 GLM-5.4，这是他们第一个用上 Loop Transformer 架构的旗舰模型。

![](https://pic.yupi.icu/1/glm54-%E5%AE%98%E6%96%B9-hero-754abe7f.jpeg)

简单来说，就是让模型中间的 28 层循环跑两遍，参数量不变，相当于每个字都多想了一轮。

官方说这样一来，750B 的模型能达到 2T 到 3T 级别的智能水平。

此外，这次的 GLM-5.4 还新增了视觉理解能力，主打用写代码的方式去做视频、游戏和 3D，官方管这个叫「泛 Coding」。

奇怪的是，官方没有公布正式版的任何跑分。目前最有参考价值的是 AICodeKing 的 KingBench 4 榜单，GLM-5.4 排第 7，是开源模型第一，跟 GPT-6.2 Astra 只差 0.4 分！

![](https://pic.yupi.icu/1/glm54-tweet-pair-official-9e77a713.png)

但网上吐槽最多的是慢。有网友让 Gemini 4 Neon 和 GLM-5.4 做同一个篮球场场景，一个用了 11 分钟，一个用了 108 分钟……

![](https://pic.yupi.icu/1/glm54-tweet-pair-slow-682cbff2.png)

那 GLM-5.4 到底怎么样呢？

目前它的 API 还没开放，只能通过 GLM Coding Plan 套餐使用。为了测试时速度能快点，我专门开了 Max 会员，一个月 1078 块，然后在智谱官方的 ZCode 里把模型切换到了 GLM-5.4 的最高档。

![](https://pic.yupi.icu/1/glm54-zcode-glm54-ui-f997b24d.png)

本来我是想再专门多跑一些跟我以前文章中的测评类似的案例，比如以撒的结合、赛车游戏、复杂的后端工程，好跟往期的 Claude、Gemini、DeepSeek 直接对比。

但是，一开跑我就傻眼了。。

我先是同时开了 6 个任务，结果账号直接被限流。

改成一个一个跑之后，又赶上工作日下午的高峰期，满屏都是 529「该模型当前访问量过大」。可能是模型刚发布、用的人太多，我实测高峰期带工具调用的请求差不多一半会被拒掉，同样的请求换成 GLM-5.3 就正常。

再加上 GLM-5.4 祖传的「雷霆大思考」，就更慢了。。

我翻了下日志，有一次 AI 光思考就输出了 13 万字符，花了整整 12 分钟，最后只回了一句话、调用了一次工具。。。

![](https://pic.yupi.icu/1/glm54-glm%E5%A8%98-%E5%B0%8F%E6%86%A9-8a075d8c.jpg)

其中有个跑得最久的 3D 动画短片任务，前后一个半小时，请求失败了 97 次，代码才刚写完。

**而且一个案例都没跑完，5 小时额度就从 6% 涨到了 45%！**

![](https://pic.yupi.icu/1/glm54-kimi%E5%A8%98-%E8%B4%B5%E8%B4%B5-2f9c4958.png)

不过没事，在 GLM-5.4 刚发布的时候，我就在另一台电脑上给自己的 [VibeFather 网站](https://vibefather.ai) 新增了很多套 GLM-5.4 生成的作品。

VibeFather 是我做的 AI 编程模板网站，每个模板都有一份上万字符的详细提示词，同一份提示词会交给不同的模型去做，正好能横向对比。目前用 GLM-5.4 做的作品已经有近 20 个了，全部是在 ZCode 里用原提示词生成的，在 [GLM-5.4 模型页](https://vibefather.ai/models/glm-5-4) 能一次看全。

![](https://pic.yupi.icu/1/glm54-vibefather-glm54-v2-e940ba24.png)

我从里面挑了 6 个不同类型的案例，从网页到 3D 由浅入深：

1. 水族馆官网
2. 精密加工厂官网
3. 插画师作品集
4. 邮箱客户端
5. 3D 飞行模拟游戏
6. 3D 太阳系比例模型

原始提示词都是又臭又长的英文，下面每个案例我都提炼成了中文简化版，方便大家理解。



## GLM-5.4 项目实测

### 1、水族馆官网

先来个热身，给一家城市水族馆做官网，要有展区楼层图、动物卡片、喂食时间表和分时段预约。

![](https://pic.yupi.icu/1/glm54-prompt-01-case1-aquarium-b496c7f5.png)

看看效果，首屏是深夜蓝的海水配一只发光的水母，背景的水波光纹会缓缓漂动，氛围感拉满。

![](https://pic.yupi.icu/1/glm54-aquarium-glm-5.4-01-40549d87.png)

这个模板我用 GLM-5.3 也做过，两代模型的首屏几乎一样，毕竟提示词连文案和素材都定死了。

真正的差距在需要 AI 自己画的地方。GLM-5.4 画的楼层图，每个展区都标了名字和水深，点哪个区就跳到哪张卡片：

![](https://pic.yupi.icu/1/glm54-aquarium-glm-5.4-02-map-a903ff28.png)

而 GLM-5.3 只摆了 5 个写着数字的方块，还是能感受到模型能力升级的：

![GLM-5.3 的楼层图](https://pic.yupi.icu/1/glm54-aquarium-glm-5.3-02-map-5d2721bc.png)



### 2、精密加工厂官网

接下来换成更讲究信息密度的 B 端官网，给一家机械加工厂做门面，核心是一个能估算工期和价格的计算器。

![](https://pic.yupi.icu/1/glm54-prompt-02-case2-factory-ff0abdc1.png)

看看效果，钢灰加电光蓝的工业风，大标题「TOLERANCES OTHERS DECLINE」的意思是别人不敢接的公差我们接，很有气势！

![](https://pic.yupi.icu/1/glm54-factory-glm-5.4-01-f3efac9a.png)

这个案例的高光是估价器。选完工艺、材料、表面处理和数量，右边立刻算出 16 个工作日和每件的价格，下面还把每一项是怎么算出来的都列了出来，跟提示词要求的「规则公开」完全对上。

![](https://pic.yupi.icu/1/glm54-factory-glm-5.4-02-estimator-10dde625.png)

之前我也用 Kimi K3.1 Pro 和 GLM-5.3 做过这个模板，三个版本的结构几乎一致，没有明显的高下之分：

![Kimi K3.1 Pro 的版本](https://pic.yupi.icu/1/glm54-factory-kimi-k3.1-pro-01-fbc3dfb1.png)

看来只要提示词写得够细，做官网这种简单的任务，国产模型的水平已经卷到差不多了。



### 3、插画师作品集

第三个案例带上了电商功能，是一位绘本插画师的作品集，能看创作过程，还能买签名版画。

![](https://pic.yupi.icu/1/glm54-prompt-03-case3-illustrator-b0300866.png)

打开首页，看到手写体大标题配一张水粉风的灯塔插画，「gouache」下面那条手绘下划线位置刚好。

![](https://pic.yupi.icu/1/glm54-illustrator-glm-5.4-01-6102a823.png)

对比 Kimi K3.1 Pro 做的，下划线的位置明显跑偏了，横在「drawn in」底下，还超出去一截。

![Kimi K3.1 Pro 的首页](https://pic.yupi.icu/1/glm54-illustrator-kimi-k3.1-pro-01-c51e9b64.png)

最让我意外的是创作过程弹窗。GLM-5.4 用代码画了 6 格构图草稿，还用红圈圈出了最终选中的那一格，很有插画师工作台的感觉！

![](https://pic.yupi.icu/1/glm54-illustrator-glm-5.4-03-process-4e564cd3.png)

对比同一个弹窗，Kimi 只放了几个房子和山的占位图标。。高下立判了。

![Kimi K3.1 Pro 的创作过程弹窗](https://pic.yupi.icu/1/glm54-illustrator-kimi-k3.1-pro-03-process-29e4d354.png)

商店功能也是可以正常使用的，加入购物车之后，底部还有一条「再买 75 刀包邮」的进度条。

![](https://pic.yupi.icu/1/glm54-illustrator-glm-5.4-04-cart-7f44a9af.png)

这一局 GLM-5.4 赢了，细节明显做的更好。



### 4、邮箱客户端

前面都是展示型网站，第四个项目我要做一个能真正操作的 Web 应用，一个三栏布局的邮箱客户端。

![](https://pic.yupi.icu/1/glm54-prompt-04-case4-mail-2d576cf6.png)

看看效果，分类收件箱、标签、按会话展开的邮件都有，是个比较成熟的邮箱页面了：

![](https://pic.yupi.icu/1/glm54-mail-glm-5.4-01-00f8095f.png)

搜索功能也做得很顺手，按 `/` 输入关键词，会话列表能实时过滤，顶部还显示一共搜到了几封。

![](https://pic.yupi.icu/1/glm54-mail-glm-5.4-04-search-d009991c.png)

不过我按快捷键 `C` 打开写信窗口，收件人一栏里会多出一个「c」，用来打开窗口的那个按键也被打了进去，我反复试了几次都是这样。

![](https://pic.yupi.icu/1/glm54-mail-glm-5.4-02-compose-d2116d3e.png)

这算是一个小 Bug 吧，虽然问题不大，但会影响使用体验。Kimi K3.1 Pro 做的版本没有这个毛病，打开的邮件里还多了附件卡片。

![Kimi K3.1 Pro 的版本](https://pic.yupi.icu/1/glm54-mail-kimi-k3.1-pro-01-8c68bb81.png)

这一局，GLM-5.4 惜败。



### 5、3D 飞行模拟游戏

传统网页这块 GLM-5.4 已经做的很稳了，接下来进入官方主打的游戏和 3D 项目。

第五个案例是低多边形风格的飞行模拟游戏，提示词如下：

![](https://pic.yupi.icu/1/glm54-prompt-05-case5-flight-b1c3e002.png)

先看看 GLM-5.4 做的版本，一打开飞机就在海岛上空飞着，从黄昏切换到白天的光照过渡很丝滑，海浪、云层、穿越圈和左下角的雷达都有。

![](https://pic.yupi.icu/1/glm54-flight-glm-5.4-highlight-0277309a.gif)

但接管操控之后，仔细看这架水上飞机，机翼和支架的结构有点乱：

![](https://pic.yupi.icu/1/glm54-flight-glm-5.4-02-control-3f170364.png)

再看看 GPT-6.2 Sol 做的，高单翼加双浮筒的飞机造型一眼就能认出来，海岛的山峰、沙滩和树林层次也丰富得多：

![GPT-6.2 Sol 的版本](https://pic.yupi.icu/1/glm54-flight-gpt-6.2-sol-02-control-cc94aed0.png)

再看看 Gemini 4 Neon 做的，光影氛围很不错，夕阳把整片天空都染红了：

![Gemini 4 Neon 的版本](https://pic.yupi.icu/1/glm54-flight-gemini-4-neon-02-control-49a156ce.png)

三家放在一起对比，GLM-5.4 的 3D 建模精细度明显差了一截。



### 6、3D 太阳系比例模型

最后一个案例直接对标国外顶级模型。这个模板我让 Claude Opus 5.5、Sonnet 5.5、Gemini 4 Carbon 和 GPT-6 Astra 都做过，要做一个可交互的 3D 太阳系比例模型。

![](https://pic.yupi.icu/1/glm54-prompt-06-case6-solar-83521aeb.png)

这个模板的灵魂是「切换比例」。GLM-5.4 一切换到真实比例，行星全部缩成了小点，尽量还原真实的间距：

![](https://pic.yupi.icu/1/glm54-solar-glm-5.4-highlight-f7be05e6.gif)

导览模式做的很好看，镜头飞到水星跟前，表面的陨石坑都是用代码生成的：

![](https://pic.yupi.icu/1/glm54-solar-glm-5.4-04-tour-b083c649.png)

导览最后，AI 还按要求做了一张「自己走一遍」的距离表。如果把太阳当成一个 12 英寸的沙滩球，地球就是一粒胡椒，要放在 107 英尺之外，海王星得走出去半英里多。

![](https://pic.yupi.icu/1/glm54-solar-glm-5.4-05-walk-d381c7ae.png)

拿 Claude Opus 5.5 做的版本对比，真实比例的效果几乎一模一样：

![Claude Opus 5.5 的真实比例](https://pic.yupi.icu/1/glm54-solar-opus-5.5-02-true-scale-7fcb7eb9.png)

没想到，在这种需求写得非常精确的 3D 页面上，GLM-5.4 已经能跟顶级模型打平了。



## 写在最后

6 个案例看下来，我觉得 GLM-5.4 配得上目前国产第一梯队的编程模型，比 GLM-5.3 有看得见的进步。

只要需求写得足够清楚，不管是官网、作品集、Web 应用，还是太阳系这种 3D 交互页面，它都能做得很到位，有些细节比 Kimi K3.1 Pro 还用心。

但到了需要 AI 自己发挥的地方，差距就出来了，比如飞行游戏里的飞机建模，跟 GPT-6.2 Sol 还差一截。所谓「2T 级智能」，我在这几个案例里没看出来。

但 GLM-5.4 的缺点也非常明显，用过的朋友都知道 —— 速度太慢！

雷霆大思考本身就慢，再赶上刚发布用的人多、高峰期一半请求被拒，我在 ZCode 里跑长任务的体验很糟糕。一个月一千多的 Max 会员，高峰期还按全价扣额度，确实有点难绷。

所以我的建议是，如果你已经是 Coding Plan 用户，可以切换到 GLM-5.4 写页面，但尽量避开工作日下午 2 点到 6 点；如果还没买，先别急着冲 Max，等过了这波发布高峰、算力跟上了再说。

其实除了本文介绍的这些案例之外，我还有很多用 GLM-5.4 跑的案例没有介绍，比如动效设计师作品集、品牌规范文档站、学术个人主页等。每个都有在线 Demo 和完整提示词，还能跟 Kimi K3.1 Pro、Claude Opus 5.5、GPT-6.2 Sol 等模型的作品对比，感兴趣的话可以到我的 [VibeFather](https://vibefather.ai/models/glm-5-4) 上看看。

![](https://pic.yupi.icu/1/glm54-vibefather-glm54-2-v2-bd12f958.png)

想看智谱上一代模型的表现，可以阅读本板块中的《GLM-5.3 三模型横评 - DeepSeek Harness 统一评测》和《GLM-5.3-Flash 编程能力实测 - 3 个项目案例》；如果想系统了解不同模型的特点和选型建议，可以阅读本教程编程工具板块中的《AI 模型选择指南》。
