## DeepSeek接入Python，一般电脑也能飞速跑，确实可以封神了！


今天这篇教程介绍：DeepSeep最新推理模型R1接入Python编程，在本地电脑从零搭建方法。

![img](https://pic.yupi.icu/yuyi/1739502610400-71691d00-4e2b-403d-a683-eb4f67fb9ce8.webp)

### 1 这样做有哪些好处？ 

1) 大模型在本地搭建，除了能够方便个人知识库管理，详见上一篇介绍，还能提效编程学习，比如Python，Java等，学编程就像学做事的思路和逻辑，挺重要也很有意思。
2) DeepSeek最近开源了推理模型R1，开源免费，性能强劲，本文接入的正是DeepSeek的R1；Python的开发环境本文使用的是PyCharm社区版，完全免费，本人使用社区版已超过10年；推荐的插件CodeGPT免费、UI好用。总结来说本文搭建方法：零成本，不需花一分钱。

3）为了照顾到关注我的大部分朋友，本文推荐的搭建方法已将电脑配置要求降低最小，我会第二节详细介绍，按照此方法，普通电脑也能飞速跑。

### 2 框架选择 

一句话描述框架选择：DeepSeek-r1:1.5b + PyCharm社区版 + CodeGPT插件

DeepSeek-r1 一共有7个不同版本，随着尺寸参数变大对电脑要求也会变高，相应的本地回复延时也会变长（因为大参数尺寸推理时间会更长）：

![img](https://pic.yupi.icu/yuyi/1739502610402-4520f4d1-738f-430f-8d55-8cd9235890d6.webp)

电脑没有大显存GPU的朋友，推荐安装1.5b尺寸，这版尺寸普通电脑无GPU的都能流畅运行，延时几乎在1-2秒，更为关键的是，DeepSeek-r1之所以爆出圈有一个重要原因，小尺寸模型回答质量也很高，即便1.5b如此小的参数尺寸亦如此。

简单再介绍下DeepSeek-R1。它回复问题主要包括两部分：思考(Thinking)和 Answer（正式回答），在每次正式回答前，会有一个很长的思考链。之前的大模型在小尺寸参数（如1.5b）回复Token有些简短，质量一般，但是这次DeepSeek-r1:1.5b解决了回复Token数过短，效果不好的难题：

![img](https://pic.yupi.icu/yuyi/1739502610454-23b96e8a-8ce4-4d69-9145-b5d9135658c6.webp)

以上就是为什么这样选型和搭建的原因，接下来介绍逐步详细搭建步骤。

### 3 详细搭建步骤

搭建步骤之前写过一篇，当时有个关键步骤拉下了，再加上r1又刚出来，所以我再重新梳理一遍，这次尽量做到步骤足够细致，尽量让完全未接触编程的朋友也可复现。

第一步，安装Pycharm社区版，完全免费，下载地址在我的公众号后台回复：Pycharm，即可获取。下载后基本都是下一步，在此不再赘述。



第二步，下载ollama并安装deepseek-r1:1.5b，在我的公众号后台回复ollama，获取ollama软件，下载安装后打开软件，输入ollama list可以看到我现在安装了三个本地大模型，其中包括r1:1.5b，刚安装ollama现在执行这条命令应该是空的：

![img](https://pic.yupi.icu/yuyi/1739502610410-fc8cc959-6397-40be-b291-b43c6f5e791c.webp)

接下来执行一条命令：ollama pull deepseek-r1:1.5b，就能直接下载它到自己的电脑，如下所示，

![img](https://pic.yupi.icu/yuyi/1739502610827-ad85adb7-e9fc-41b9-8064-36895d5400aa.webp)

下载完就安装好了，比较方便。

接下来就可以愉快的接入到PyCharm 了。

第三步，DeepSeek-r1:1.5b接入到PyCharm。首先下载插件：CodeGPT，打开第一步安装的PyCharm，找到文件(File)-设置(Settings)-插件(Plugins)，输入CodeGPT，即可点击安装(Install)即可：

![img](https://pic.yupi.icu/yuyi/1739502610813-f70ac774-a7d6-4a7d-9b1d-8d59b98bba4a.webp)

安装后在工具(Tools)下会出现CodeGPT，点击Providers，找到Ollama(Local)，对应下图数字2，再到3这里选择刚刚安装的deepseek-r1:1.5b，点击OK就可以了：

![img](https://pic.yupi.icu/yuyi/1739502610805-a5dea937-fc35-4e46-9fe0-c1377cd8c86a.webp)

下面就可以愉快的在PyCharm中使用DeepSeek-r1加速编程学习了，左侧是代码编辑界面，右侧是r1大模型，直接对话式提问，省去了来回不同页面折腾的麻烦：

![img](https://pic.yupi.icu/yuyi/1739502610884-17da0319-e949-40c7-b9a1-437a32c14664.webp)

大家再感受DeepSeek-r1:1.5b大模型的回复延时，几乎1秒钟响应，本人电脑是pro-m1，这响应速度可以了。再看看回答效果，因为公众号文章的GIF帧数有限制，我只截取了前6帧，无任何加速，全部是延时播放速度，展示下效果：

![img](https://pic.yupi.icu/yuyi/1739502610869-b95b2eb5-50d9-473f-95ad-064af5a481a4.gif)

CodeGPT插件显示了Tokens数，有些朋友担心这是不是在计费？不是的！只是一个数字统计，无任何费用，因为使用的是本地自己电脑的算力。

另外，CodeGPT应该是目前大模型+编程UI做的最好的插件了，感兴趣的朋友可以根据此篇文章以上三个步骤安装试试。

### 最后总结一下

本地运行大模型：免费、便捷、适合个人知识管理与编程学习。

选型推荐：deepseek-r1:1.5b + PyCharm社区版 + CodeGPT插件。

在 PyCharm 右侧直接对话 DeepSeek-R1，快速辅助编程。

几乎 1-2秒响应，完全本地快速运行，无额外费用。



> 来源：https://mp.weixin.qq.com/s/QUaAO5BEUpv5pXsHz9T1fw