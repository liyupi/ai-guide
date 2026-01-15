## DeepSeek R1 + 个人知识库，直接起飞！


DeepSeek R1 + 个人知识库，直接起飞！

今天要讲的：DeepSeek-R1 + 个人知识库打造。  
除了硅基流动，还要用到另一个圈内比较火的第三方客户端：Cherry Studio。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503395801-4c70f1e1-0a51-4ff7-b1d4-ee0b10f0a041.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)

1\. 下载安装 Cherry Studio  
https://cherry-ai.com/  
作为一个完全开源的项目，除去UI设计、功能不谈，Cherry Studio很值得推荐的一点是作者（@kangfenmao）活跃在各大平台、论坛，积极听取用户反馈的同时，更新相当及时。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503395910-33cac31e-7d46-4db1-aa6c-f8ef77667448.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


2\. 模型配置  
安装好Cherry Studio后，首先需要配置模型。搭建个人知识库，仅硅基流动的模型就足够了，所以只需：点击左下角的设置\->选择硅基流动\->打开开关->填入硅基流动的API key。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503395891-52e15ffd-7229-403d-abee-e13e5811bc96.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


接下来，把需要用到的模型添加上。下拉到最下面，点击绿色的管理按钮。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503395843-ca60f57f-08dc-4098-91c3-b0506b6e3385.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


常规模型中，推荐添加下面三个模型：推理模型DeepSeek-R1、通用模型DeepSeek-V3，以及视觉模型Janus-Pro-7B。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503396949-f8d5110a-8274-40df-b72c-8cb2f294a623.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


嵌入（embedding）模型，推荐添加下面两个：完全免费的BAAI/bge-m3和付费的Pro/BAAI/bge-m3。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503396781-1c8015e3-6675-40a5-91b1-0c4ca8690b21.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


一般说来，免费的BAAI/bge-m3模型就够用。  
3\. 创建知识库  
配置完模型，就可以开始创建知识库了！  
点击左侧菜单栏的知识库图标->点击左上角的添加按钮->在弹窗里输入你的知识库名称，随便输，方便查找就行->选择嵌入模型。  
嵌入模型选择上一步中添加的免费模型BAAI/bge-m3就可以。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503396827-010a8349-0158-4e2e-a3e5-326e0074f015.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


接下来就可以往你创建好的知识库里添加资料，Cherry Studio支持各种类型的资料，比如文件、网址、笔记等等。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503396864-2a508bc8-54fc-4fd5-aaf9-97a7465928c7.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


以最常见的文件资料为例，直接把PDF拖拽进去，当看到文件右边的状态符号变为绿色的对勾，就说明该文件已经向量化完毕。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503396884-e338bada-3b51-4522-8d2a-ff5f9c038727.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


4\. 和知识库对话  
添加完资料，就可以开始检索你的个人知识库了。  
两种方式使用。  
一种是直接在知识库最下面的搜索知识库，点击后进行搜索。  
输入你想搜索的内容，点击搜索按钮。就像下面这样。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397365-05aa6d51-278f-4df6-9da4-507377cd6608.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


第二种方法则更为实用：直接在问答的过程中选中知识库，相当于给LLM添加了额外的上下文信息。  
在Cherry Studio的输入框下方，有一个知识库的图标，点击，选择你创建好的知识库。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397343-5a28048b-0917-4001-adb0-076a966e0636.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


选中后，知识库的图标会变成蓝色。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397345-59a63aaf-f09a-4c5c-9ab4-b7b8ce81464a.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


这里我默认的模型是DeepSeek-R1。回答前，会先对知识库进行检索，然后把搜索结果投喂给DeepSeek-R1，由模型进行整理、分析，再生成最终的答案。  
可以看到，DeepSeek-R1的回答结果是基于知识库内容产生的。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397373-51641dc2-ea26-435a-8749-848588d63079.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)


附上DeepSeek-R1的思考过程，一如既往的给力。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397382-0fc4b4c1-c19b-4dba-91fe-8f2cf3f74060.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)

  

近期，由于大量用户涌入硅基流动使用DeepSeek模型，导致硅基的DeepSeek-R1调用可能卡顿，并且思考时间有时离谱的长。所以，上车要趁早啊。  

![](https://cdn.nlark.com/yuque/0/2025/webp/22157260/1739503397819-a3aa2802-a4fc-432e-85d5-bc6a7fb14ff5.webp?x-oss-process=image%2Fresize%2Cw_1080%2Climit_0)

  

> 来源：[https://mp.weixin.qq.com/s/wa\_Swhj2cAvB9Btt2\_-Dbg](https://mp.weixin.qq.com/s/wa_Swhj2cAvB9Btt2_-Dbg)  