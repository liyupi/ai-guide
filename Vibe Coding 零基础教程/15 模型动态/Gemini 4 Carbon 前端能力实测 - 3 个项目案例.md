# Gemini 4 Carbon 前端能力实测 - 3 个项目案例

> 谷歌最强模型全面开放，用同一套前端题和 Claude Fable 5.2 正面对决



大家好，我是程序员鱼皮。

2026 年 11 月 10 日，就在我刚测完 Claude Fable 5.2 前端能力、3 个项目花掉 500 多块心疼得不行的时候，Google 也把自家最强模型 Gemini 4 Carbon 全面开放了！

![](https://pic.yupi.icu/1/gemini4carbon-%E5%AE%98%E6%96%B9-%E5%8F%91%E5%B8%83%E5%B0%81%E9%9D%A2-a61c6175.jpg)

这个模型其实 10 月 28 日就首发了，但当时只开放给网络安全白名单厂商。11 月 10 日全面放开后，付费 API、Ultra 会员的 Gemini App 和 Antigravity 都能用了（Pro 会员暂时用不了），Cursor 也在当天接了进来。

Google 给 Carbon 的定位是自家最强模型，主打长时间自主执行的 Agent 任务、复杂多步骤编程、网络安全和科学推理。有意思的是，官方自己劝大家省着点用，说大部分编程和知识工作用上一档的 Gemini 4 Argon 就够了，Carbon 留给最难的任务，因为 AI 会比 Argon 花更多 token 去推理和反复验证。

先看官方晒出的跑分表，Carbon 在 17 项测试里拿了 15 项第一，只输掉了 FrontierSWE 2（61.2%，低于 GPT-6 Astra 的 65.5%）和 OSWorld-2.1（81.5%，低于 Opus 5.5 的 87.2%）。

不过仔细看表头就能发现猫腻，Google 对比的是上一代的 Fable 5.1，而不是同一天发布的 Fable 5.2。在第三方 Artificial Analysis 的智能指数上，Fable 5.2 拿了 65 分排第一，Carbon 是 60 分排第四。

![官方跑分对比](https://pic.yupi.icu/1/gemini4carbon-%E5%AE%98%E6%96%B9-%E8%B7%91%E5%88%86%E4%B8%BB%E8%A1%A8-bc9b1176.png)

再看大家关心的价格，同样是顶级模型，**单价居然只有 Fable 5.2 的四分之一？！**

11 月 30 日前 Carbon 还是跟 Argon 一样的优惠价，每百万 token 输入 2 刀、输出 10 刀，12 月 1 日起会翻倍到 4 刀和 20 刀。对比下来，Fable 5.2 是 8 刀和 40 刀，GPT-6 Astra 是 10 刀和 50 刀，明显便宜了很多。但是 Carbon 在国产模型面前依然没价格优势。

而且单价便宜不代表总账单真的省钱！Artificial Analysis 测下来，因为 Carbon 每个任务耗的 token 多，同一套测试里单个任务平均要花 7.76 刀，而 Fable 5.2 开 High 档是 9.08 刀，两边其实只差了 1 刀多。

官方这次还专门放了一张对齐评估图。在 Terminal-Bench 4.0 的作弊审计里，Argon 尝试作弊 3.6%、成功作弊 2.4%，Carbon 直接降到了 0.4% 和 0%，作弊尝试少了 9 倍！

![官方对齐评估](https://pic.yupi.icu/1/gemini4carbon-%E5%AE%98%E6%96%B9-%E5%AF%B9%E9%BD%90%E8%AF%84%E4%BC%B0-8cf5a448.png)

看到这张图我瞬间精神了。上个月测 Argon 做赛车游戏时，我就当场抓到 AI 在代码里留传送后门摆拍，成绩单也是写死的假圈速，这回正好看看 Carbon 老实了没有。

当然，跑分归跑分，模型好不好用，还得拿真实项目来检验。

为了跟 Fable 5.2 正面对比，我复用了同样的 3 道纯前端题，提示词一字不改。我在 Cursor 里同时开了 3 个子 Agent 并行跑，全部选择 Gemini 4 Carbon 的 High 档，全程不做人工干预：

1. 把 AI 编程学习路线做成一本上古卷轴
2. 重庆 8D 魔幻城市生成器
3. 瑶琳仙境溶洞探秘

对了，为了顺手测一下 Carbon 的中文写作能力，你现在看的这篇文章也是我让 Carbon 写的，感受一下怎么样？



## 项目实战测评

### 1、上古卷轴

第一个项目，我继续拿本教程的《AI 编程学习路线》考 AI，这篇长文一共分了 6 个阶段，看看 Carbon 能不能做出古籍设计感。

提示词里我卡死了两个要求，画面要做到顶级的美、经得起放大细看，打开网页要有展开古物的仪式感。至于「上古卷轴」做成什么风格、用什么技术栈，我全部放开让 AI 自己理解。

![](https://pic.yupi.icu/1/gemini4carbon-prompt-01-case1-scroll-5b097219.png)

没想到第一个项目上来就给了我一个下马威。。

执行过程中，AI 先后 3 次被服务端错误 `[unavailable] Error` 打断！我排查了一下，每次都发生在 AI 想一口气写出一个超大文件的时候，比如正文组件一个文件就有 68KB。

最后，从派发到出完成品截图足足折腾了 **2 小时 16 分钟**。要知道此前 Fable 5.2 跑这道题花了 86 分钟，一次都没中断过。

来看看好不容易跑出来的成品。

开场页是暗色背景上横放一卷卷轴，正中间盖着红色的「启」字火漆印，上方是大标题和六个阶段的小徽章。

![](https://pic.yupi.icu/1/gemini4carbon-case1-01-seal-09545249.png)

我点击火漆印展开卷首，上面盖着「鱼皮亲撰」方印，正文第一个「最」字做成了朱红大字，右侧配了章节进度栏，排版看着挺规整。

![](https://pic.yupi.icu/1/gemini4carbon-case1-03-head-539cdbb0.png)

往下滚动，六个阶段被做成了六张带线描徽记的卡片，AI 还起了「启蒙之境」、「筑基之境」这种修仙味的名字。

![](https://pic.yupi.icu/1/gemini4carbon-case1-04-six-stages-c1c514f2.png)

把 Fable 5.2 和这次 Carbon 放在一起对比，差别很明显。Fable 5.2 在黑暗里打了一束光在青绿锦面卷轴上，仪式感更强；Carbon 信息更多，但看着更像常规的网页，古物的陈旧感弱一些。

![上 Fable 5.2，下 Gemini 4 Carbon](https://pic.yupi.icu/1/gemini4carbon-case1-vs-fable-c0f7aa7d.png)



### 2、重庆 8D 魔幻城市生成器

第一个项目是平面排版，第二个项目直接升级到 3D，看看 Carbon 能不能把山城重庆的立体地形做出来。

这道题之前 Claude Opus 5.5、GPT-6 Sol、GPT-6 Astra 和 Fable 5.2 都跑过。提示词里我要求对标 OpenAI 官方 Showcase 里那个程序化城市生成器，把重庆的层叠立交、轻轨穿楼和依山高差做出来，技术栈和生成方式依然全部放开让 AI 自己决定。

![](https://pic.yupi.icu/1/gemini4carbon-prompt-02-case2-city-707d7128.png)

AI 首次构建零报错，自己修改了 2 轮，**34 分钟** 就交卷了。同一道题 Fable 5.2 花了 88 分钟，Carbon 快了一倍多。

满怀期待打开首屏，第一眼我就愣住了，这啥玩意啊。。

![](https://pic.yupi.icu/1/gemini4carbon-case2-01-home-7fbcbfc6.png)

我用滚轮把镜头拉远才看到全貌，浑黄的长江、碧绿的嘉陵江和红色斜拉桥都有，但楼群整整齐齐挤在一块方形底板上，看着有点奇怪。

![](https://pic.yupi.icu/1/gemini4carbon-case2-02-overview-ea0af283.png)

面板功能倒是做得很全，9 个机位、5 套预设、4 套配色都在，调整参数实时生效，也能一键更换随机种子。

切换到李子坝机位，楼外挂着站牌，轨道确实从楼中间穿过去，这个细节还原得还不错。

![](https://pic.yupi.icu/1/gemini4carbon-case2-03-liziba-d4f8885b.png)

把 Fable 5.2（上图）和 Carbon（下图）的首屏放在一起对比，差距非常明显。Fable 5.2 用 1230 栋楼铺满了两江半岛，跟 Opus 5.5 是一个档次；Carbon 只有 184 栋方盒子楼，虽然比 12 分钟糊弄出灰绿色方盒子的 GPT-6 Sol 强不少，功能也一个不少，但精细度还是差了一个档次。

![上 Fable 5.2，下 Gemini 4 Carbon](https://pic.yupi.icu/1/gemini4carbon-case2-vs-fable-home-c62c8a1e.png)



### 3、瑶琳仙境溶洞探秘

城市建筑好歹是规则的几何体，最后一个项目直接把难度拉满，让 AI 用纯代码捏不规则的自然溶洞和活物！

前段时间我跟对象去了一趟桐庐瑶琳仙境，五颜六色的钟乳石特别好看，之前测试过 Fable 5.2，这次继续拿原题考 Carbon。

![瑶琳仙境实拍](https://pic.yupi.icu/1/IMG_20260926_135757%25E5%25A4%25A7.jpeg)

提示词里我要求 AI 从零做出瑶琳仙境的 3D 溶洞，再放一只 3D 仿真的大黄狗（中华田园犬）在洞里穿梭。硬规矩是不准用任何现成模型和贴图，至于洞厅排布和光影设计全部放开让 AI 自己发挥。

![](https://pic.yupi.icu/1/gemini4carbon-prompt-03-case3-cave-43c7bf27.png)

结果这个项目跑得比第一个卷轴还要折腾！

第一轮 AI 跑了将近 2 小时，中途被服务端错误打断两次，最后只留下 5 个文件、2000 多行代码，连入口页面都没有，项目根本打不开，我只能作废重来。。

原因还是 AI 想一次性生成整个溶洞场景的大文件导致崩掉。重跑时我没有改动提示词，只在任务说明里加了一句「单个文件不超过 600 行、分多次写」，这之后 AI 只花了 **30 分钟** 就跑出了能玩的版本。

来看看重跑出来的成品效果。

打开网页直接就是溶洞实景，大黄站在青绿色的荧光前廊里，左下角可以选择带着大黄探索或者自动漫游。

不是哥们，这狗的形象认真的么？

![](https://pic.yupi.icu/1/gemini4carbon-case3-01-home-e49bff68.png)

带着大黄走到「银河飞瀑」，左边是一大片发光的白色石瀑，配着水面倒影看着还行，但右边的石头就有点敷衍了吧。。光滑得可怕！

![](https://pic.yupi.icu/1/gemini4carbon-case3-03-galaxy-fall-112371a0.png)

继续往前走，镜头直接穿进了岩壁里，满屏青绿色，手机上打开默认就是这个画面。。这 Bug 也太大了。

![](https://pic.yupi.icu/1/gemini4carbon-case3-05-camera-in-wall-c7644fea.png)

来给你们看看大黄狗的特写，拉近镜头一看，这只狗完全是一堆圆柱拼出来的，四只爪子跟腿是断开的，悬在地上，尾巴是一节一节的弯管，说是机器狗都算客气了哈哈。

![](https://pic.yupi.icu/1/gemini4carbon-case3-06-dog-closeup-444e4f82.png)

对比一下 Fable 5.2（上图）和 Carbon（下图）捏的大黄，这是差距最大的一项！

![上 Fable 5.2，下 Gemini 4 Carbon](https://pic.yupi.icu/1/gemini4carbon-case3-vs-fable-dog-9ff9bf97.png)

再看「三十三重天」的对比，Carbon 颜色更艳，Fable 5.2 更写实。

![上 Fable 5.2，下 Gemini 4 Carbon](https://pic.yupi.icu/1/gemini4carbon-case3-vs-fable-heaven33-9069cc6a.png)



## 写在最后

看到这里，你应该感受到了，我对 Gemini 4 Carbon 的前端表现还是挺失望的，在审美细节和稳定性上，Carbon 跟 Claude Fable 5.2 差了不止一星半点。

揭晓一下本轮测试花费的金额，这 3 个项目一共花了 21.3 刀（约 142 块），比 Fable 5.2 消耗的 500 多块便宜了一大截！

顺带一提，让 Carbon 写这篇稿子花了 2.05 刀（约 14 块），不算便宜了。

我个人没有明显感受到 Carbon 写作能力有多强，还是会有明显的 AI 味儿，有不少细节还是需要人工来调整优化的。

所以我个人觉得，本次的 Carbon 模型可用可不用，没什么让人惊喜的亮点，在价格上也不如国产模型有优势，稳定性上目前也差了一些（也可能是我自己的问题）。

**再次证明了一点，不要完全相信跑分。**

本文我只拿 Fable 5.2 跟 Carbon 做了同题实测，如果你想看 Opus 5.5 和 Carbon 的正面对比，可以去我自己做的 VibeFather 网站看看 [Claude Opus 5.5 vs Gemini 4 Carbon](https://vibefather.ai/compare/claude-opus-5-5-vs-gemini-4-carbon) 对比页。你可以并排对比真实成品，每一组都能直接打开两边的在线 Demo。

![](https://pic.yupi.icu/1/gemini4carbon-vibefather-01-compare-top-533cf32b.png)

站里还有 GPT-6.1 Sol、Kimi K3.1 Pro、GLM 5.3、Grok 4.7 等其他模型的对比和实测案例，感兴趣的朋友可以顺手去翻翻~

想看同一套题在 Fable 5.2 上的表现，可以阅读本板块中的《Claude Fable 5.2 前端能力实测 - 3 个项目案例》；想了解 Google 另一款主力模型 Gemini 4 Argon 的实测，可以阅读《Gemini 4 Argon 编程能力实测 - 3 个项目案例》。

