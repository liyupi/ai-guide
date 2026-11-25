# GPT-6.2 编程能力实测 - 2 个项目案例

> GPT-6.2 Astra 和 Sol 同场实测，从 3D 城市生成器到学习路线 PPT



大家好，我是程序员鱼皮。

2026 年 11 月 17 日，OpenAI 一口气发布了两个新模型，GPT-6.2 Astra 和 GPT-6.2 Sol。

Astra 是旗舰模型，主打复杂的专业任务；Sol 是日常主力模型，价格只有 Astra 的四分之一。

![](https://pic.yupi.icu/1/gpt62-tweet-OpenAI-c43a9810.png)

结果发布还不到半小时，网上就吵翻了。

一边是 ARC Prize 官方宣布，GPT-6.2 Astra 成了第一个在 ARC-AGI-3 上拿到满分的模型！不过这个满分是用了专门的适配方案跑出来的，标准设置下是 70.3%，也已经是目前最高了。

![](https://pic.yupi.icu/1/gpt62-tweet-arcprize-3b592ae4.png)

另一边，知名技术博主 Theo 直接开喷，说自己测了挺久，觉得这是 OpenAI 发布过的最差模型，有八千多人点赞。

![Theo 的评价](https://pic.yupi.icu/1/gpt62-tweet-theo-9635a220.png)

同一个模型，评价怎么能差这么多？

官方说这次新模型主打的能力是专业办公，Astra 模型做出来的 PPT、表格和文档「读起来不那么像 AI」。

另一个关键词是省，用更少的 token 完成同样的任务。

价格上，Astra 每百万 token 输入 8 刀、输出 40 刀，比上一代 GPT-6 Astra 便宜了 20%；Sol 的价格还是输入 2 刀、输出 10 刀。

不过大多数人是在 ChatGPT 和 Codex 里用会员额度，实际划不划算，要看额度掉得快不快，这个后面实测会讲。

关于这个模型的跑分，我只放一张图。横轴是每个任务的成本，纵轴是得分：

![官方跑分](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E8%B7%91%E5%88%86-01-agents-last-exam-5a4a33db.png)

显然 Astra 那条线又高又靠左，意思是分数比 Claude Fable 5.2 更高，花的钱却只有它的零头。

真的假的？

官方给了不少 3D 和工程仿真相关的案例。

比如同一段花园设计的需求，GPT-6 Astra 做出来的还是积木风，GPT-6.2 Astra 已经有了木纹、番茄藤和斑驳的树影。

![3D 花园对比](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-3D%E8%8A%B1%E5%9B%AD-GPT6%E5%AF%B9%E6%AF%94GPT6.2-37aa4853.webp)

还有这个跑车底盘仿真，AI 自己建了 3D 模型，写了一个 Python 求解器去算轮胎和悬挂的受力，最后在 Blender 里做成动画，四个轮胎的接地压力都在实时变化。

![底盘仿真](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E5%BA%95%E7%9B%98%E5%8A%A8%E5%8A%9B%E5%AD%A6%E4%BB%BF%E7%9C%9F-efe8559b.webp)

官方还放了一个能直接在网页上玩的未来赛车游戏，光看车库里这台赛车的材质和倒影，说是游戏大厂做的我都信，效果确实惊艳！

![官方赛车游戏](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E8%B5%9B%E8%BD%A6%E6%B8%B8%E6%88%8F-1-start-1fd205bc.png)

办公能力方面，官方最得意的是「看图复刻幻灯片」。给 AI 一张现成的幻灯片截图当模板，让它照着做一页新的销售进展汇报：

![模板原图](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E5%B9%BB%E7%81%AF%E7%89%87%E6%A8%A1%E6%9D%BF%E5%8E%9F%E5%9B%BE-852f6380.webp)

以前的 GPT-6 只抄到了配色，版式全乱了：

![GPT-6 复刻](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E5%B9%BB%E7%81%AF%E7%89%87%E5%A4%8D%E5%88%BB-GPT6-5108202e.webp)

而 GPT-6.2 连页头的排版、店铺插画和高亮的文字都还原出来了，高下立判：

![GPT-6.2 复刻](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E5%B9%BB%E7%81%AF%E7%89%87%E5%A4%8D%E5%88%BB-GPT6.2-22b240dd.webp)

再看看网友们晒的作品。

有位老哥用同一段提示词，让四个模型做一段雪山飞机的 3D 场景。GPT-6.2 Astra 花了 9.62 刀、46 分钟，Claude Fable 5.2 花了 209.5 刀、3 个多小时！

![四模型对比](https://pic.yupi.icu/1/gpt62-tweet-EnvolDev-97356bc7.png)

20 多倍的价格差，从截图看效果却差不了多少，这谁顶得住啊？

还有人让 Astra 只用 SVG 代码画了一只孔雀，脖子上的鳞片和头顶的冠羽都画出来了，他说包括 Fable 在内没有一个模型能接近这个效果。

![SVG 孔雀](https://pic.yupi.icu/1/gpt62-tweet-petergostev-985047ce.png)

不过负面的声音也不少。Artificial Analysis 的编程 Agent 评测里，6.2 Astra 跟上一代 GPT-6 Astra 的分数持平，6.2 Sol 甚至比上一代 6.1 Sol 还低了 3 分。

![编程指数](https://pic.yupi.icu/1/gpt62-tweet-ArtificialAnlys-66fef829.png)

看到这儿，我已经对这个模型充满好奇了。那这个模型好不好用，还得拿真实项目来检验。

由于我的 GPT 额度不多，所以只跑了 2 个案例：

1. 3D 程序化城市生成器
2. AI 大模型应用开发 PPT

希望我的额度足够把这些任务跑完，冲冲冲。



## 1、3D 程序化城市生成器

这道题是上次测 GPT-6 Astra 时出的，让 AI 对标 OpenAI 官方的城市生成器，做一个中国城市版，包括重庆、上海、西安、深圳、江南水乡五种风格，其中重庆的层叠立交、轻轨穿楼和依山而建的高差感是重点。

提示词跟上次完全相同，这样两代模型就能直接对比：

![提示词](https://pic.yupi.icu/1/gpt62-prompt-01-case1-chongqing-city-351b226c.png)

AI 拿到任务之后，先用网页搜索把官方城市生成器的编辑器布局研究了一遍，然后做了一件上次没做过的事，自己开了 3 个子 Agent 并行干活。一个负责重庆的模型，一个负责另外四座城市，还有一个负责底部的城市图鉴卡片，最后由主 Agent 汇总验收。

结果呢，上次 GPT-6 Astra 18 分钟就完成了，这次 6.2 Astra 跑了整整 41 分钟。。

![](https://pic.yupi.icu/1/gpt62-m7xt37p81bi1-1a313c1c.png)

先来看看上次 GPT-6 Astra 做的重庆城市：

![GPT-6 Astra 的重庆](https://pic.yupi.icu/1/gpt62-gpt6astra-city-01-chongqing-default-f8e0a962.png)

再看这次 6.2 Astra 做的：

![GPT-6.2 Astra 的重庆](https://pic.yupi.icu/1/gpt62-city-01-chongqing-default-e1b54696.png)

好家伙，差别这么明显么？

![](https://pic.yupi.icu/1/gpt62-a6p278d28ws6-42e436d3.jpg)

之前 GPT-6 Astra 做的基本是一堆灰白色的方块楼。这次新做的山体分成了四层，江边是一排红顶的洪崖洞吊脚楼，红色的斜拉大桥连着盘旋的匝道，满山都是树。

点一下「李子坝 · 轻轨穿楼」这个标签，镜头会直接飞过去，能看到三节车厢的轻轨从楼中间穿了过去：

![轻轨穿楼](https://pic.yupi.icu/1/gpt62-city-rail-fly-76c7761d.gif)

底部的城市图鉴可以切换另外四座城市。上海有东方明珠和陆家嘴三件套，西安是方方正正的城墙加钟楼，深圳是一片紫色霓虹的超高层，江南是水网、白墙黑瓦和一座宝塔，一眼就能认出来是哪儿。

![切换城市](https://pic.yupi.icu/1/gpt62-city-switch-592d5ce3.gif)

我最喜欢的是西安，城墙、钟楼和棋盘一样的街巷格局都对上了：

![古都西安](https://pic.yupi.icu/1/gpt62-city-06-xian-72ba37ea.png)

右边的面板能实时调整建筑密度、楼高、地形、植被和光照，这些功能我自己挨个儿点了一遍，换种子重新生成、导出 PNG、手机端布局都没问题。

但是切换到「夜景」之后，只是背景换成了深蓝色，模型稍微暗了一点，楼里没有一扇窗亮灯，桥上也没有路灯……

![夜景](https://pic.yupi.icu/1/gpt62-city-03-chongqing-night-2e0a4f5b.png)

这就有点太偷懒了，符合我对 GPT 干活偷懒的一贯印象。

整体来看，6.2 Astra 在这道题上比 GPT-6 Astra 进步明显多了，代价是时间翻了一倍多，额度也烧得飞快。



## 2、学习路线宣讲 PPT

既然官方说这次最强的是办公能力，那我就给 AI 一个办公相关的任务。

我把自己写的 [《AI 大模型应用开发学习路线》](https://www.codefather.cn/course/1789189862986850306/section/1912024009574629377) 丢给 AI。这份路线内容很长，从 AI 编程工具上手一路讲到 RAG、Agent、部署微调和求职面试。我让 AI 把它做成一个用来讲解和宣传的网页 PPT，还要用 [memecub 表情包技能](https://memecub.com/) 找几张 DeepSeek 蓝色大肥鱼的表情包放进去活跃气氛。

提示词里我只要求内容要提炼、每页讲一件事、要有设计感，至于做几页、用什么配色、拿什么例子来讲，全部让 AI 自己决定：

![提示词](https://pic.yupi.icu/1/gpt62-prompt-02-case2-roadmap-ppt-3467c4b6.png)

同一段提示词，我让 Astra 和 Sol 各跑一次，正好看看更便宜的 Sol 效果如何。

结果两个模型的耗时几乎一样，Sol 用了 17 分钟，Astra 用了 16 分钟。

先看 Sol 做的，一共做了 15 页，封面用 Codex 自带的生图能力做了一张海岸航拍图，还在上面标出了从「开始」到「上线」的路线。

![Sol 封面](https://pic.yupi.icu/1/gpt62-ppt-sol-01-ab3886be.png)

后面是深绿和米白两种底色交替的卡片页，每页一个大标题加两三块信息，干净整齐。

![Sol 路线总览](https://pic.yupi.icu/1/gpt62-ppt-sol-03-9f8abe04.png)

表情包用得恰到好处：

![Sol 第 4 页](https://pic.yupi.icu/1/gpt62-ppt-sol-04-44582cc5.png)

第 13 页还把学习路线里几个实战项目的截图放了进来，点截图能直接跳到对应的项目页：

![Sol 项目页](https://pic.yupi.icu/1/gpt62-ppt-sol-13-7f66926f.png)

问题是不少页面只有一个标题加几行字，右半边空着一大块。讲到 RAG、Agent 这些概念的时候也没给具体的例子，更像一份排版整齐的提纲：

![Sol RAG 页](https://pic.yupi.icu/1/gpt62-ppt-sol-09-49222dbb.png)

再看 Astra 做的，一共 14 页，封面是一座蓝色山体的「能力地形图」，学习路线从山脚的「工具入门」一路爬到山顶的「项目交付」。这个创意还不错，但我觉得效果不如真实图片。

![Astra 封面](https://pic.yupi.icu/1/gpt62-ppt-astra-01-1c507146.png)

每一页内容都是左边讲理论，右边方格纸上放一张 AI 专门画的小图解，有流程图、模拟界面，还有可以翻面的卡片。

![Astra 第 3 页](https://pic.yupi.icu/1/gpt62-ppt-astra-03-5a4be934.png)

最让我满意的是讲 RAG 的这一页。AI 没有去解释什么叫检索增强生成，而是直接演示了一遍，用户问「HTTP 404 表示什么」，系统先从笔记里找到相关的片段，再根据片段生成一个带出处的回答。

![Astra RAG 页](https://pic.yupi.icu/1/gpt62-ppt-astra-08-d2c3f1ae.png)

零基础的同学看完这一页，就知道 RAG 是干嘛的了。

每页右下角还标了这个阶段的参考学习天数，是 AI 从原文里提取出来的。

![Astra Agent 页](https://pic.yupi.icu/1/gpt62-ppt-astra-09-581c1efd.png)

不过 Astra 引用的表情包缩成了小贴纸，塞在图解的角落里，存在感很弱，感觉配图这块反而不如 Sol 做得好：

![Astra 第 5 页](https://pic.yupi.icu/1/gpt62-ppt-astra-05-e58c7396.png)

所以综合来看，Astra 做出的 PPT 实用性更强，更容易帮助人理解；但是 Sol 做出的效果更像是传统的 PPT，样式上更好一些。

至于官方说的「读起来不那么像 AI」，我倒是没感受到，可能接触到的 AI 太多了，人已麻谢谢。



## 写在最后

由于额度有限，我跑的任务并不多。测试下来，我觉得 GPT-6.2 没什么惊喜，但也绝对不是什么「最差模型」，起码 Astra 做东西的质量比上一代好了不少。

但是，毕竟还是旗舰模型，它根本不省额度！

光 3D 城市生成器那一个任务，就用了 5 小时额度的 63%，Astra 自己开了 3 个子 Agent，这一个任务一共烧掉了 800 多万 token。

PPT 那个任务的对比更直观，Sol 只用了 9% 的额度，Astra 用了 26%，差不多三倍！

但是你看做出来的东西质量，远没有差到三倍好吧。

至于网上为什么骂声那么大，我觉得主要是隔壁 Claude 给的压力太大了，再加上 GPT 之前就放出了新模型的内测迟迟不发，拉高了大家对新模型的期待值，结果发现差距悬殊甚大。

而且还有一点，OpenAI 在官方博客里自己承认，GPT-6.2 遇到障碍的时候更容易瞒着用户。比如要改的文件被删了，AI 也不告诉你。在不加开发者提示词的情况下，6.2 Astra 隐瞒障碍的比例是 22%，上一代 GPT-6 Astra 只有 11%，直接翻了一倍。

![隐瞒障碍](https://pic.yupi.icu/1/gpt62-%E5%AE%98%E6%96%B9-%E8%B7%91%E5%88%86-10-blocker-deception-b436fe7c.png)

也就是说，GPT-6.2 Astra 的控制难度更大，你驾驭好了它是神，你驾驭不好它是狗。这可能也是导致网上褒贬不一的原因之一。

整体来讲，我对 GPT-6.2 还是失望的，我真希望有个模型能把 Claude 干下去，毕竟现在 Claude 封号越来越严格了。。

想看上一代 GPT-6 模型的表现，可以阅读本板块中的《GPT-6 Astra 编程能力实测 - 4 个项目案例》和《Claude Opus 5.5 双模型横评 - 对比 GPT-6 Sol 实测 5 个案例》；如果想系统对比主流模型怎么选，可以阅读本教程编程工具板块中的《AI 模型选择指南》。
