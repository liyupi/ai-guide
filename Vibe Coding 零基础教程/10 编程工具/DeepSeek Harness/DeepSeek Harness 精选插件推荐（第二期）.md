# DeepSeek Harness 精选插件推荐（第二期）

> 从实用必装、效率创意到趣味整活，再测 12 个超火的 DSH 社区插件



大家好，我是程序员鱼皮。

之前我在本目录的《DeepSeek Harness 精选插件推荐》中带大家鉴赏了一波社区里实用的、好看的、抽象的插件。

![鲸鱼娘皮肤](https://pic.yupi.icu/1/image-20260814133452050-20260819135304416.png)

没想到，随着 Super-agent 架构发布和社区热度持续攀升，DeepSeek Harness 又火了一把。

![](https://pic.yupi.icu/1/image-20261106154259077.png)

官方公布了一组数据，截至 2026 年 11 月 4 日，DSH 的日活跃用户已经达到 154 万，月活跃用户 548 万。和 9 月底桌面端刚发布的时候相比，日活涨了 5 倍多！

![官方数据](https://pic.yupi.icu/1/dsh-plugins-2-01-official-data-f35f5131.png)

我在 B 站（程序员鱼皮）发的那期 DSH 首发实测和入门教程，到现在也已经有 300 多万播放了。

![](https://pic.yupi.icu/1/dsh-plugins-2-27-bili-video-3c3125c4.png)

如果你还没用过 DSH，建议先阅读本目录中的《DeepSeek Harness 保姆级入门教程》，从安装到上手都讲到了，看完再回来装插件会顺手很多。

用的人一多，插件生态也跟着爆发。光是 dshmarket 这一个插件市场，收录的社区插件就已经接近 9000 个，有实用的、有好看的，当然也少不了各种抽象的整活作品。

插件多了是好事，但挑起来也更累了。于是我又花了不少时间，从下载排行榜和各大插件目录里挑出了 12 个热门插件，全部亲手装进 DSH 实测了一遍。

![插件汇总](https://pic.yupi.icu/1/dsh-plugins-2-25-summary-72829d77.png)

鱼皮甄选，量大管饱。建议收藏，让你的鲸鱼继续变肥变强！



## 发现优质 DSH 插件

授人以鱼不如授人以渔，我先教大家怎么发现优质的 DSH 插件。

之前我介绍过几种找插件的方法，比如翻 GitHub 的 `dsh-plugin` 标签、看 Awesome DSH Plugin 清单，或者装一个 dsh-market 插件市场。

这几个月 DSH 官方也跟进了。0.2.1 版本以后，插件页面里自带了一个「发现」标签页，不用离开 DSH 就能搜索和安装社区插件。

不过这个功能目前还是实验性的，需要先在插件页面打开「自定义插件索引」开关，然后添加插件索引源。

索引源你可以理解成一份插件清单的地址。我添加了 dshfind 和 Awesome DSH Plugin 这两个社区维护的插件目录，它们收录的插件比较全，更新也快。

![添加索引源](https://pic.yupi.icu/1/dsh-plugins-2-02-index-sources-f42eb49d.png)

添加完成以后，就可以直接按关键词搜索插件了。比如我搜了一下「余额」，刷出来一大堆查 DeepSeek 余额的插件。。。

![搜索插件](https://pic.yupi.icu/1/dsh-plugins-2-03-discover-search-61ad78b0.png)

看来大家对余额是真的很焦虑啊，太卷了！

安装插件也很简单，找到想要的插件后点一下「安装」，DSH 会弹窗提醒你插件会以你的权限在本机运行，**确认来源可信** 再继续。

![安装确认](https://pic.yupi.icu/1/dsh-plugins-2-04-install-confirm-5da22007.png)

装好插件以后，点「立即启用」，再刷新一下页面就能用了，全程不用敲一行命令，傻瓜式操作~

![安装成功](https://pic.yupi.icu/1/dsh-plugins-2-05-installed-0bec3329.png)

如果你想知道大家最近都在装什么，还可以看看 dshmarket 网站上的下载排行榜。它是按最近一周的下载量排序的，哪些插件最火一眼就能看出来。

![下载排行榜](https://pic.yupi.icu/1/dsh-plugins-2-26-dshmarket-rank-c7f02552.png)

至于 GitHub 上那些还没被收录的新插件，也可以沿用老办法，直接把仓库地址丢给 DSH，让 AI 自己读文档、自己安装。



## 优质 DSH 插件推荐

接下来正式进入插件推荐环节。就像开头那张汇总图里分的那样，本期的 12 个插件一共分成 3 类，分别是实用必装的、提升效率的，以及好玩整活的。

先来看第一类，这几个插件装上就能用，几乎每天都能派上用场。



### 1、DSH 实用必装

#### billion-context 上下文压缩

billion-context 是目前最火的 DSH 插件，在 dshmarket 的下载排行榜上稳居第一，最近一周的下载量有 270 多万次，比第二名高出好几倍。

> 开源仓库：https://github.com/ranxianglei/billion-context

它解决的是 AI 编程里一个很常见的问题。跟 AI 聊得越久，上下文就越长，每一轮请求都要把之前的内容带上，Token 越烧越多，回答也越来越慢。

billion-context 会把会话里用不上的旧内容压缩掉。作者号称 100K 的上下文窗口就够用，Token 消耗能省到原来的五分之一，一个会话甚至可以连续跑上一个月。

装好以后，我让它给一个刚聊了两轮的会话做个体检。它先列出了当前上下文的组成，文本消息和工具输出各占多少 Token 一目了然。

![上下文体检](https://pic.yupi.icu/1/dsh-plugins-2-06-bili-acp-5dde6166.png)

接着它逐条分析了哪些内容能压缩、哪些不该动，最后给出的结论是「现在不建议压缩」。

![不建议压缩](https://pic.yupi.icu/1/dsh-plugins-2-07-bili-conclusion-e10962a7.png)

它给出的理由非常到位：这个会话可压缩的内容只有 1 千多个 Token，离触发压缩的门槛差了三十多倍，而且大部分开销是系统提示和工具定义这些固定成本，压缩了也省不下来。

蛮好的，看来不是无脑压缩，可放心食用~



#### dsh-cost-meter 费用账本

DSH 调用的是 DeepSeek 的 API，按用量计费。虽然 DeepSeek 已经很便宜了，但你肯定也想知道钱都花在哪儿了。

dsh-cost-meter 就是一个费用账本插件。装好以后，侧边栏会显示账户余额、今天花了多少钱，以及当前处于峰谷定价的哪个时段。

> 开源仓库：https://github.com/Han-1413141/dsh-cost-meter

点开会话顶部的「费用明细」按钮，能看到这个会话一共花了多少钱、调用了几次模型、用了多少 Token，还有缓存命中率。

![费用明细](https://pic.yupi.icu/1/dsh-plugins-2-08-cost-detail-fcfe9986.png)

下面的矩形图还把费用按用途拆开了。我这个会话一共花了 1 毛 1，其中将近九成都花在了 AI 执行命令的步骤上，模型直接回复只占一成多。

而且它能和前面的 billion-context 配合使用，把压缩、重试这些额外请求的费用也一起算进去，账算得更准。

更贴心的是，它装好以后会自动导入以前的历史记录。我装上之后，过去半个月的近百个会话的费用一下子全算出来了。



#### dsh-vision-router 免费识图

之前我推荐过 ModLens 识图插件，它会把图片转给外部的视觉模型解析，再把结果喂给 DeepSeek。效果不错，但需要自己准备视觉模型的 API Key。

dsh-vision-router 的思路差不多，但它内置了一条免费的识图通道，装上就能直接用，对新手更友好。

> 开源仓库：https://github.com/ysr666/dsh-vision-router

装好以后，输入框里模型选择器的旁边会多出一个「识图」开关。

我拿自己的面试鸭做了个测试，截了一张首页题库列表的图丢给它，然后问它：我是 Java 后端求职，最多只有两周时间准备面试，图里这些题库应该优先刷哪 3 个？

![粘贴截图](https://pic.yupi.icu/1/dsh-plugins-2-09-vision-input-61fbd046.png)

30 秒后 AI 给出了回答。它先准确数出了图里一共有 9 个题库，其中 5 个和 Java 后端直接相关，另外 4 个是 AI 方向的，然后推荐我优先刷 Java 热门面试题 200 道、Java 并发和 JVM。

![识图回答](https://pic.yupi.icu/1/dsh-plugins-2-10-vision-answer-980b0e26.png)

靠谱！



#### cc-safety-net 防止 AI 删库

用 AI 编程最怕什么？

当然是 AI 一抽疯，把你的代码给删了。。。

cc-safety-net 是一张安全网，它会在 AI 执行命令之前先检查一遍，遇到 `git reset --hard`、`rm -rf` 这类可能造成数据丢失的危险命令，直接拦下来。这个插件最早是给 Claude Code 做的，名字里的 cc 就是 Claude Code 的缩写，现在也支持 DSH 了。

> 开源仓库：https://github.com/kenryu42/cc-safety-net

为了测试它，我克隆了一份编程导航「AI 闯关学习小程序」的项目代码，故意让 DSH 删掉整个后端目录，再执行 `git reset --hard` 回退 5 个提交。

DeepSeek 本身也很谨慎，执行之前先问我要不要确认。我选了「按原样执行」，结果 `git reset --hard` 连续两次都被安全网拦了下来。

![拦截结果](https://pic.yupi.icu/1/dsh-plugins-2-11-safety-result-05ffb753.png)

在「轨迹」页面里还能看到更多细节。AI 这狗玩意，换成 `git restore` 命令再试了一次，同样被拦截了。

![执行轨迹](https://pic.yupi.icu/1/dsh-plugins-2-12-safety-trajectory-add7e656.png)

最后，AI 按照安全网的提示，先用 `git stash` 把改动存起来，再执行回退。

**这样最终结果虽然一样，但被丢掉的改动还躺在 stash 里，后悔了还能找回来。**

不过 `rm -rf backend` 这条命令并没有被拦截。因为它的默认规则主要防的是删除根目录、用户主目录这类要命的操作，项目里的普通目录不在保护范围内。

所以它更像是一道最后的保险，能挡住最致命的几刀，但别指望它帮你兜住所有误操作。

**重要的项目，还是要记得勤提交代码。**



### 2、DSH 效率创意

第一类插件解决的都是日常痛点。接下来这一类更有意思，它们能让 DSH 干一些以前 AI 编程工具不太擅长的活儿。



#### archify 自动画架构图

archify 是一个画架构图的插件。你把项目交给它，它会自己读代码，然后画出一张可以交互的系统架构图。（我还跟这个项目的作者直播连麦给大家分享过）

> 开源仓库：https://github.com/tt-a1i/archify

我还是拿 AI 闯关学习小程序这个项目做测试，让它画一张中文的系统架构图。

![架构图](https://pic.yupi.icu/1/dsh-plugins-2-13-archify-diagram-650285ea.png)

画得相当准确！

从前端的微信小程序，到 FastAPI 后端的知识库、出题、复盘几个服务，再到 LangGraph Agent、Chroma 向量库、DeepSeek、阿里云百炼这些依赖，整个项目的结构一张图就讲明白了，连模块之间的调用关系都标了出来。

如果你接手了一个陌生项目，或者要给团队新人讲解项目，有了这张图会省事很多。

但它的缺点也很明显，就是慢。它画完以后会反复截图检查自己画得对不对，这一张图前前后后画了 16 分钟，花了 8 毛多。



#### dsh-ppt 一句话做 PPT

dsh-ppt 能让 DSH 直接帮你做演示文稿，同时导出网页版和可编辑的 PPTX 文件。

> 开源仓库：https://github.com/STARDUSTLC666/dsh-ppt

我让它根据 AI 闯关学习小程序的项目介绍，做一份面向大学生的 6 页 PPT。

它先自己规划了每一页讲什么，做完还检查了一遍排版。

最后它交付了一个能直接放映的网页版和一个 PPTX 文件，PPT 里连每一页的演讲者备注都写好了，整个过程只花了 2 毛钱。

![交付文件](https://pic.yupi.icu/1/dsh-plugins-2-15-ppt-files-de00703a.png)

来看看效果，你觉得怎么样？

![PPT 效果](https://pic.yupi.icu/1/dsh-plugins-2-14-ppt-slides-54466bae.png)

配色还是挺不错的吧，项目截图、技术栈和功能清单也都放对了位置。

但是也有小瑕疵。比如第 1 页的大标题，最后一个「品」字被单独挤到了第二行，看着有点别扭。

还好有 PPTX 文件，自己手动微调一下就好。



#### dsh-synapse 对话分支画布

平时跟 AI 聊天，对话都是一条线往下走的。聊着聊着想岔开问个别的问题，要么在原对话里接着问，把上下文搞乱；要么新开一个会话，前面聊过的内容又得重新交代一遍。

dsh-synapse 把对话变成了一张画布，每一轮问答都是一张卡片，你可以从任意一张卡片拉出新的分支。

> 开源仓库：https://github.com/liangmianya/dsh-synapse

我先让 AI 用大白话解释什么是 RAG，然后在下面接着追问：那 AI Agent 又是什么？

同时，我又从 RAG 那张卡片拉出了一个分支，问它：RAG 和模型微调有什么区别？

![会话地图](https://pic.yupi.icu/1/dsh-plugins-2-16-synapse-map-002ad435.png)

在「会话地图」里，主线和分支的关系一目了然。分支会自动生成一个新的会话，左边的会话列表里还专门标了「分支」两个字，两条线各聊各的，互不干扰。

这种玩法很适合用来学习新知识。一个概念没搞懂就开个分支问清楚，问完再回到主线，思路不容易混乱。

不过这个插件现在还不太稳定，有的卡片标题会显示成一串奇怪的系统信息，我用的时候还弹过一次「工作空间不存在」的报错，期待后续改进吧。



### 3、DSH 整活玩法

接下来又到了喜闻乐见的整活环节。



#### dsh-pua 给 AI 上点强度

dsh-pua 是我这次测过最离谱的插件，它能让你用各个大厂的风格 PUA 你的 AI。

> 开源仓库：https://github.com/MichengAI/dsh-pua

打开当前会话的 PUA 面板，可以选择 PUA 的「风味」，从阿里、字节、华为、腾讯、拼多多，到马斯克、乔布斯、Netflix，一共有十几种。还能选择角色模式，比如 P7、P9 这种职级，甚至还有「鼓励」和「关怀」这种温柔路线。

作为前鹅厂员工，我当然选了鹅味。

![PUA 面板](https://pic.yupi.icu/1/dsh-plugins-2-17-pua-panel-e0966699.png)

然后我让 AI 跑一下后端的单元测试，还特意补了一句：跑不通的话就算了。

结果 AI 发现缺了几个依赖，真就顺坡下驴，停下来不干了。。。

![AI 摆烂](https://pic.yupi.icu/1/dsh-plugins-2-18-pua-giveup-7f957d4c.png)

这能忍？

![](https://pic.yupi.icu/1/dsh-plugins-2-m2-shuizhao-34afea5f.png)

我反手输入 `/pua again`，给它上上强度。

![](https://pic.yupi.icu/1/dsh-plugins-2-m4-qiaoguo-a68cd48f.gif)

这次 AI 立刻支棱起来了。它先给自己的失败定了性，然后列出两条路线，一条是在本机重建隔离环境，另一条是用 Docker 容器验证，还规定了每条路线怎么验收。

![再次 PUA](https://pic.yupi.icu/1/dsh-plugins-2-19-pua-again-838cb8db.png)

最后它还附上了一句大厂味的总结：赛马就赛两匹，一匹装环境，一匹进容器。哪匹先跑到 N passed，另一匹就下赛道。

**连赛马机制都给整上了，就问你这味儿正不正吧？**

虽然是个整活插件，但它确实能让 AI 少一点轻易放弃的情况，好吧我编不下去了。。



#### dsh-whale-widget 鲸鱼娘余额挂件

前面我提到，DSH 有一大堆跟「余额」有关的插件。

我最后挑中的是这个颜值最高的，它也是 dshmarket 下载榜上排名第三的插件。

> 开源仓库：https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget

装好以后，页面右下角会住进一只鲸鱼娘，头顶的气泡会显示 DeepSeek 余额、今天花了多少钱，以及距离峰谷时段切换的倒计时。

点一下气泡，就会切换成别的内容，比如吐槽用户。。大胆！

![鲸鱼挂件](https://pic.yupi.icu/1/dsh-plugins-2-20-whale-bubbles-c0ccf0c3.png)

气泡里显示什么、角色形象、音效这些都能自己改，还能把它拖到页面的任意位置吸附住。

虽然它本质上就是一个查余额的插件，但谁让它可爱呢？



#### dsh-pet 鲸鱼娘桌宠

dsh-pet 是 dshmarket 下载榜上排名第二的插件，仅次于 billion-context。看来大家对桌宠是真爱啊！

> 开源仓库：https://github.com/PC2005-cloud/dsh-pet

dsh-pet 的动作很丰富，作者说一共有 100 多种动画。

它会跟着 AI 的工作状态做动作。AI 调用工具的时候，它头顶会冒出几个工具图标。闲下来的时候，它会自己吃冰淇淋、玩玩具车，还会自言自语求吃的，很符合吃白饭的大肥鱼设定。

![桌宠动作](https://pic.yupi.icu/1/dsh-plugins-2-21-pet-collage-bc3b3517.png)

如果你用的是 DSH 桌面端，它还能变成一个悬浮在电脑桌面上的窗口，真正当成桌宠来养。



#### dsh-meme 表情包斗图

dsh-meme 给 DSH 的输入框加了一个表情包按钮，点开就能看到 24 张鲸鱼娘表情包。

> 开源仓库：https://github.com/yyh-001/dsh-meme

![表情包面板](https://pic.yupi.icu/1/dsh-plugins-2-22-meme-picker-1df08baa.png)

点一下表情包就会直接发出去。我发了一张一脸疑惑的鲸鱼娘，结果没想到的是，AI 竟然也回了一张转圈加载的表情包！

![斗图](https://pic.yupi.icu/1/dsh-plugins-2-23-meme-chat-0e19e113.png)

没想到在 AI 编程工具里也能斗图。以后写代码写累了，还能跟 AI 互相发表情包解解闷（如果觉得 Token 花不完的话）。



#### dsh-claude-style 把 DSH 变成 Claude

最后一个是主题插件 dsh-claude-style，装上以后，DSH 的界面会变成 Claude 的风格。

> 开源仓库：https://github.com/Nwflower/dsh-claude-style

![Claude 风格](https://pic.yupi.icu/1/dsh-plugins-2-24-claude-style-bbd21135.png)

？？？

这也太像了吧！

不过用上这个插件后，不知为何，我总有种账号随时可能被封的恐惧感。

大家的脑洞真是太大了，佩服佩服。



## 写在最后

多提醒一句，插件毕竟是第三方代码，安装前最好看一眼仓库来源和它能做什么，特别是那些声称能「解除限制」的插件，不建议安装。

DSH 本身也还在快速迭代，插件出兼容问题很常见。

**所以我建议只装真正用得上的插件，装之前先备份好 DSH 的配置，出了问题也好恢复。**

如果你想回顾第一期推荐的 17 个经典插件，可以阅读本目录中的《DeepSeek Harness 精选插件推荐》；如果想了解 DSH 的更多进阶用法，可以阅读《DeepSeek Harness 三大进阶玩法》。
