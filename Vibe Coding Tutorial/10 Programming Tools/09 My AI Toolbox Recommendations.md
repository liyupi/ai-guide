# My AI Toolbox Recommendations

> My Top 20 most-used AI products this year



Hello, I'm Programmer Fish Skin, former Tencent full-stack developer, [AI Programming Blogger](https://space.bilibili.com/12890453) with 2 million followers across all platforms, and creator of 10+ self-developed products including [AI Navigation](https://ai.codefather.cn) and [Programming Navigation](https://www.codefather.cn).

In previous articles, we systematically learned about the various types of AI programming tools: from AI model selection, zero-code platforms, AI code editors, command-line tools, IDE plugins, AI agent platforms, to auxiliary tool sets.

So the question arises:

- With so many tools, which ones do you actually use, Fish Skin?
- How do these tools work together in practice?
- Any practical experience to share?

In this article, I'll share my Top 20 most-used AI products of 2025, along with my practical insights, hoping to give you some reference.



## I. AI Programming Tools

As a programmer, AI programming tools are what I use most. Below are my main programming tools for this year.



### Cursor

[Cursor](https://cursor.com/) is the AI editor with the best development experience and AI engineering capability in my book. I mainly rely on it for large projects—whether writing code, modifying code, or refactoring code, Cursor's Agent mode can help me get it done.

I especially love its Tab completion feature. When writing code, AI automatically predicts what I want to write, and I press Tab to accept the suggestion. It feels like having an experienced driver sitting next to you—you just think about what to write, and they've already written it for you.

Plus, Cursor can freely switch between multiple models like Claude, GPT, Gemini, etc., and can use your own API Key, so I can choose the most suitable model for different tasks.

However, Cursor's biggest problem is its extremely high price. I previously shared my bill—over 10,000 yuan burned in just over a month. So now I combine it with some free tools to avoid budget explosion.

![](https://pic.yupi.icu/1/yupicursorbilling.png)



### Claude Code

[Claude Code](https://claude.ai/code) is the command-line AI programming tool I use most. Its automation level is very high—not only can it generate code, but also automatically execute commands, install dependencies, and create files.

I generally use it for some simple tasks or to quickly set up project frameworks. For example, if I want to make an image compression tool, I just say one sentence to AI in the command line, and it can automatically build the entire project for me.

![](https://pic.yupi.icu/1/1764146174167-3018c8f3-0ad9-4a4f-9764-246f33b33203.png)

And Claude Code supports Skills—you can write some common standards and processes as Skills for AI to automatically follow, which is especially useful for avoiding repetitive work and team collaboration.

Because Claude Code has restrictions in China, I generally use it with domestic AI large models like Zhipu GLM. This way I can use it normally, and costs are also lower.



### Cline

[Cline](https://cline.bot/) is an AI IDE plugin, one of my backups. When Cursor's budget is used up, or I want to develop in VS Code, I use Cline.

![](https://pic.yupi.icu/1/image-20260108222935455.png)

Cline's biggest advantage is that it's completely free, and its functionality is very comprehensive, basically able to do 80% of what Cursor can. Although the experience isn't as smooth as Cursor, considering it's free, it's already very good.

Plus, Cline supports multiple platforms—not only VS Code, but the entire JetBrains series can use it too. This means when I switch between different editors, I can use the same tool and maintain a consistent experience.



## II. AI Multimedia Creation Tools

Besides programming, I also use AI for content creation. Below are the multimedia creation tools I use most.



### Nano Banana

Nano Banana is the most explosive AI image generation tool this year. I use it to generate comic knowledge explanation images and article cover images.

Its Chinese support is particularly good—unlike Midjourney, it doesn't require English prompts. And the generated image style is very unified, especially suitable for tutorial illustrations.

The anime-style images you see are all made with Nano Banana:

![](https://pic.yupi.icu/1/toolstype%25E5%25A4%25A7.jpeg)

Since using Nano Banana, I've completely said goodbye to Midjourney.



### Jimeng AI

[Jimeng AI](https://jimeng.jianying.com/) is ByteDance's all-in-one AI creation platform, supporting text-to-image, image-to-video, and other functions.

I mainly use it to generate video b-roll footage. For example, when I make tutorial videos and need some background scenes, I use Jimeng AI to generate them. Its video generation speed is fast, and the quality is good.

Plus, Jimeng AI is a domestic platform with fast access speeds, so no need to worry about being blocked.



### Veo 3

[Veo 3](https://aistudio.google.com/models/veo-3) is Google's most advanced AI video generation model. I use it to make some creative short videos.

Veo 3's video quality is indeed very high—physical laws, lighting and shadow effects are all very realistic. But the price is extremely high, so I only use it when I need high-quality video.

![](https://pic.yupi.icu/1/1751177650505-09aecbd1-a858-4a01-a74d-62120f074c98.png)



### Eleven Labs

[Eleven Labs](https://elevenlabs.io/) is an AI voice synthesis tool with particularly realistic voice imitation effects.

And Eleven Labs supports multiple languages and voice styles—you can choose different voices for different scenarios. I use it to synthesize voiceovers for some creative videos.

![](https://pic.yupi.icu/1/image-20260109100507368.png)



## III. AI Large Models

AI large models are the foundation of all AI tools. Below are the large models I've used most this year.



### Zhipu GLM

[Zhipu GLM](https://bigmodel.cn/) is the domestic large model I use most, with strong programming ability and excellent Chinese understanding.

I mainly use it combined with Claude Code to generate non-commercial full-stack projects. Because GLM's API price is very cheap, and the speed is fast, it's especially suitable for making small projects or quickly validating ideas.

Nowadays Zhipu's development is also super strong—starting from GLM-4.6, programming ability has improved significantly, even surpassing Claude Sonnet in some evaluations! The company's IPO is well-deserved.



### Alibaba Tongyi Qianwen

Tongyi Qianwen is the large model our team's products integrate with most. Its advantages are fast generation speed, convenient API integration, and the ability to use [Alibaba Cloud Bailian Platform](https://bailian.console.aliyun.com/) for debugging.

![](https://pic.yupi.icu/1/1752569401445-7023e2c1-f709-4c22-af86-63ee1872c1cd.png)

Our products use it to generate simple content or do intent recognition. For example, when a user inputs a sentence, we use Tongyi Qianwen to determine what the user wants to do, then call the corresponding function.

Plus, Tongyi Qianwen has free quotas, which are enough for a while for small projects.



### DeepSeek

[DeepSeek](https://www.deepseek.com/) as a former hit product, is completely free and has strong programming ability. However, recently both the product ecosystem and the speed of releasing new models are somewhat inferior.

I now mainly use it to verify professional technical knowledge. For example, when I'm writing an article and unsure whether a technical point is correct, I'll ask DeepSeek. Since it's free anyway, I can ask whatever I want without worrying about costs.

![](https://pic.yupi.icu/1/image-20260109100658239.png)



### Gemini

[Gemini](https://gemini.google.com/) possesses powerful reasoning capabilities and multimodal understanding, and supports ultra-long context (1 million Token).

I mainly use it to analyze large projects. For example, when I take over a project with hundreds of files and want to quickly understand the project structure, I use Gemini to analyze.

I also use Gemini's web version to collect some international technology and product research—the reports it gives are very professional.

![](https://pic.yupi.icu/1/image-20260109100840547.png)

However, Gemini has certain usage barriers in China, you know what I mean.



## IV. AI Development Frameworks

Besides directly using AI tools, I also use some AI development frameworks to build AI applications.



### Spring AI

[Spring AI](https://spring.io/projects/spring-ai) is the standard for Java AI development, providing a unified API to simplify large model integration.

When our team works on Java projects, we basically always use Spring AI. It unifies the APIs of various large models into one interface, so developers can easily switch between different models without changing code.

![](https://pic.yupi.icu/1/image-20260109100909041.png)

Plus, Spring AI provides many advanced features like conversation memory, RAG, tool calling, etc., letting us quickly build complex AI applications.



### LangChain4j

[LangChain4j](https://docs.langchain4j.dev/intro) is the Java version of LangChain, supporting declarative syntax with a super pleasant development experience, suitable for building complex Agents.

I especially love its chain call syntax—very elegant to write. And its documentation is very complete, the community is very active, and when you encounter problems, you can check the GitHub Issues area more, it's easy to find solutions.

When I lead the [Programming Navigation](https://codefather.cn/) fish friends in building a big-company-caliber [AI Zero-Code Generation Platform Project](https://www.codefather.cn/course/1948291549923344386), we use LangChain4j + LangGraph4j, which can very conveniently build complex AI workflows.

![](https://pic.yupi.icu/1/1753332332820-9ec614de-65a2-496d-b9b2-dc89c20d06c9.png)



### Vercel AI Gateway

[Vercel AI Gateway](https://vercel.com/ai-gateway) is an AI model gateway service that lets you uniformly call hundreds of AI models.

It provides a unified API, so I don't need to learn each model's API documentation—I can just use Vercel AI Gateway directly.

![](https://pic.yupi.icu/1/1760687990497-90720fbb-0df6-4ede-87b8-64b8702994e9-20251028181254840.png)

I use it to develop some creative projects. For example, if I want to make an AI tool that lets users choose different models, Vercel AI Gateway can help me very conveniently implement this feature.



### Alibaba Cloud Bailian

[Alibaba Cloud Bailian](https://bailian.console.aliyun.com/) is an enterprise-level AI application development platform, supporting RAG knowledge bases, process orchestration, and other functions.

Some of our team's knowledge bases are managed with it. For example, we have many technical documents, and using Bailian's RAG feature can very conveniently let AI answer questions based on these documents.

![](https://pic.yupi.icu/1/1744177887403-6373c63c-d410-49ba-a71c-556389536376.png)

Plus, Bailian provides visual process orchestration functionality, so you can build complex AI workflows without writing code.

![](https://pic.yupi.icu/1/1745388167957-d7995436-fc2f-410e-bc59-4f6db6544359.png)



### OpenRouter

[OpenRouter](https://openrouter.ai/) is a unified AI model routing platform. It supports hundreds of models and can be very conveniently switched—no need to register accounts on each platform.

Whenever a new model is released, I try it on OpenRouter, using it to experience the latest large model capabilities.

![](https://pic.yupi.icu/1/image-20260109101446266.png)

For developers who want to try new things, OpenRouter is a great choice.



## V. AI Browser Plugins

AI browser plugins let me use AI anytime in the browser, which is particularly convenient.

### Monica

[Monica](https://monica.im/) is the all-around AI assistant in the browser, with webpage summarization, video summarization, translation, writing, image processing—all in one.

![](https://pic.yupi.icu/1/image-20260109101602426.png)

I use Monica every day. For example, when reading long articles, I use it to summarize the core content; when reading English documentation, I use it to translate; when looking at code repositories, I summarize the entire project's introduction.

![](https://pic.yupi.icu/1/image-20260109101803122.png)

Monica's biggest advantage is its high integration—almost all commonly used AI functions are there. Plus, it supports multiple large models, so you can choose the most suitable model for the task. Highly recommended.



### AITDK

[AITDK](https://aitdk.com/) is an SEO and content creation artifact—I use it for keyword analysis and competitor research.

Friends who do self-media all know that keyword research is very important. AITDK can help me analyze which keywords have high search volume and low competition, then I write articles or optimize my website targeting these keywords.

Plus, AITDK can analyze competitors' content strategies—see what others are writing, and I can find differentiated angles.

![](https://pic.yupi.icu/1/image-20260109101947603.png)



## VI. AI Daily Conversation

Besides work, I also use AI in daily life to solve some problems.



### ByteDance Doubao

ByteDance Doubao is a national-level AI application with fast speed and good interaction.

When I encounter problems, I often just take out my phone and ask Doubao. Doubao's response speed is particularly fast, and its Chinese understanding is very strong.



### Tencent Yuanbao

Tencent Yuanbao's biggest advantage is that it connects with WeChat, so it can be used anytime, anywhere.

When I see an article in WeChat and want AI to summarize it, I just @Yuanbao directly. This seamless integration experience is particularly good—no need to switch apps, I can use AI right in WeChat.

![](https://pic.yupi.icu/1/image-20260109102243168.png)



## VII. AI Office Tools

When doing content creation, I also use some AI office tools to improve efficiency.



### Baidu Wenxin Assistant

[Baidu Wenxin Assistant](https://image.baidu.com/) integrates many document writing and image processing tools. I often use it to modify images and remove watermarks.

For example, if I take a photo and want to remove the watermark, Wenxin Assistant can handle it in a few seconds. Or if I want to change the background of an image, Wenxin Assistant can also help me implement it.

Plus, Wenxin Assistant has many other features like PPT generation, document translation, etc. For content creators, it's a very practical tool.

![](https://pic.yupi.icu/1/image-20260109102440839.png)



## VIII. Fish Skin AI Navigation

The [AI Navigation Website](https://ai.codefather.cn/) developed by the Fish Skin team is also the AI website I visit most this year—one word: "Complete"!

I regularly check what's new in the AI field. Plus, Fish Skin AI Navigation has organized many categories of AI tools, making it particularly convenient to find tools.

![](https://pic.yupi.icu/1/AI%E8%B5%84%E6%BA%90%E5%A4%A7%E5%85%A8%E7%BD%91%E7%AB%99.png)



## IX. My Usage Strategy

Having shared so many tools, let me briefly summarize:

- **When working on large projects**, I use Cursor + Claude Opus 4.5, because code quality requirements are high and need the strongest AI capabilities.

- **When working on small projects or quickly validating ideas**, I use Claude Code + Zhipu GLM, because speed is fast and costs are low.

- **When budget is used up**, I switch to VS Code + Cline + DeepSeek—completely free, functionality is sufficient.

- **When needing to generate images**, I use Nano Banana, because Chinese support is good and generation speed is fast.

- **When needing to generate video**, I choose Jimeng AI (cost-effective) or Veo 3 (highest quality) based on quality requirements.

- **When encountering problems in daily life**, I directly ask Doubao or Yuanbao, because it's convenient and fast.

- **When writing articles and needing illustrations**, I use Wenxin Assistant to process images, because its functionality is comprehensive.

Choose the most suitable tool based on the scenario—this both guarantees efficiency and controls costs.



## In Conclusion

These are my Top 20 most-used AI products this year, along with my practical insights.

**Tools will constantly update, so choices must be flexible.**

Beyond tools, what's more important is mastering Vibe Coding's core capabilities: how to clearly express requirements, how to effectively converse with AI, how to understand and optimize AI-generated code, how to turn ideas into products.

Now you've mastered the tool knowledge needed for Vibe Coding. Next, it's time to put these tools to use and make real projects!

In the [Project Practice] section, I'll walk you through various projects hands-on, from personal tools to AI applications, from simple to complex, letting you truly master the essence of Vibe Coding.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
