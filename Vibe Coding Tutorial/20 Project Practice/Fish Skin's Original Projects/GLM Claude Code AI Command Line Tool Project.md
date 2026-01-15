# GLM + Claude Code - AI Command Line Programming Tool Project Practice

This project will guide you in using pure Vibe Coding to leverage Claude Code in developing Yupi Code, an AI command-line programming tool that compares to Claude Code.

The entire development process is completed through conversation with AI, without writing a single line of code. Suitable for students who want to rapidly practice a complete Vibe Coding development workflow and learn how to use AI to develop AI tools.



---

Hello everyone, I'm Programmer Fish Skin. Recently, a friend started learning AI programming (influenced by me). She heard that Claude Code, this AI programming tool, is awesome, but when she tried it, she found she needed a foreign Claude account to log in.

![](https://pic.yupi.icu/1/1766562559951-d1371bb9-99d3-467a-aeec-421cd12eb3bb.png)

Then she complained to me grumbling.

So I joked: Don't be sad, how about I make a Claude Code for you?

![](https://pic.yupi.icu/1/1766562773776-4a34c38c-c95b-4eb9-8b02-81ca86133188.png)

The result, she took it seriously!

I ↓

![](https://pic.yupi.icu/1/1766562833168-97c7d4fc-bfe5-4a09-9215-dcfbdb546cb4.png)

No choice, had to try.

Coincidentally, the domestic AI large model GLM-4.7 was just released. I saw many bloggers online hyping it as "the strongest programming model in China," "the strongest open-source model," "the best alternative to Claude," even claiming it surpasses GPT-5.2 and Claude Sonnet 4.5.

![](https://pic.yupi.icu/1/1766563074181-1ee8e12d-2868-4b23-b993-c0e61800565e.png)

Saying it's the strongest in China, fine. But surpassing Claude? Can I believe that?

Well then, I'll try using GLM-4.7 to make my own AI programming tool, comparing to Claude Code, and see what GLM-4.7 is really made of.

![](https://pic.yupi.icu/1/1766551074508-575a037d-174a-43d2-bbfe-e223082fc665.png)

Next, let's together **use GLM-4.7 + Claude Code** to develop a **GLM-4.7-based Claude Code clone** AI programming tool.

Before starting the project, first give it a resounding name — let's call it `Yupi Code`!

Next, we'll follow this "Fish Skin AI Vibe Coding Development of Claude Code Clone Yupi Code" process, without writing a single line of code, step by step building "Claude Code"!

- Environment preparation => Install tools and configure environment, able to Vibe Coding
- Technical research => Confirm it meets generation requirements
- Design and development => Including solution design, code generation, bug fixing, to get MVP minimum viable product
- Version control => Prevent issues from subsequent changes
- Capability optimization => Support more features comparing to Claude Code, like web search, streaming output, deep thinking, etc.

![](https://pic.yupi.icu/1/1766549738919-9e627293-954a-4f39-8625-d1dcb1835cbc.jpeg)



## Environment Preparation

Zhipu's GLM-4.7 is compatible with multiple coding tools. Besides Claude Code, it also supports mainstream coding tools like Cursor, Cline, etc., flexibly adapting to various development scenarios.

Integrating GLM into Claude Code is also simple, done in 1 minute.

First open terminal and enter one command to install Claude Code:

```shell
npm install -g @anthropic-ai/claude-code
```



Then execute `claude` command to open the program. By default it requires logging into a Claude account, otherwise it can't be used:

![](https://pic.yupi.icu/1/1764145940075-ace6fd24-a09c-41c0-b400-1cffc394fc8a.png)



But no problem, let's replace the AI large model behind it with domestic GLM-4.7. First enter `{User Directory}/.claude` directory and create a `settings.json` configuration file:

![](https://pic.yupi.icu/1/1764146110361-06e13de5-7de4-4fc5-9533-3651447d5e19.png)



Then modify the configuration file content as follows, remember to replace with your own API Key:

![](https://pic.yupi.icu/1/1764146125955-3029843c-26b8-4628-b2b7-a9d8abb2aef1.png)



API Key can be obtained directly from Zhipu development platform:

Directions: https://bigmodel.cn/

![](https://pic.yupi.icu/1/1766552195823-7f90ead2-3e07-4eb4-92e2-7ef12c591e61.png)



Next you can use it happily~

![](https://pic.yupi.icu/1/1766549578200-7189d326-db17-4edd-9e27-2d9da3af06cf.png)



Besides this method, the official documentation also provides a simpler way, directly using the automation assistant, following the guidance to complete environment configuration:

![](https://pic.yupi.icu/1/1766552079851-2cd903df-febb-4860-98fc-51c1143b4105.png)



## Technical Research

If you want to fully utilize AI to develop projects, there are several difficulties:

1. The project needs to include complete frontend and backend, requiring the large model to have strong **coding ability**
2. Need to make the backend project integrate AI large models. Each large model has different integration and development methods, need to let AI **read documentation** to understand the latest development methods
3. If you want to optimize interface effects, also need **image understanding ability**, giving AI an image and letting it recreate it

Before officially starting development, we need to confirm that GLM-4.7 and Claude Code working together can meet these capability requirements.

According to Zhipu's official introduction, Claude Code has built-in Zhipu-specific MCP tools that developers don't need to install themselves. Including **search and web reading** capabilities, and **visual understanding capabilities** that can directly parse screenshots/design drafts/error images.

Let's test them one by one. First is web search capability, keeping up with current events:

![](https://pic.yupi.icu/1/1766541771159-00bcb3ee-422b-4895-9ab6-15e5ad44937e.png)

Test web reading capability, let it read information from our Programming Navigation website:

![](https://pic.yupi.icu/1/1766485091937-8555eddf-7301-4161-92d9-4f19251cf9d1.png)

Test image understanding capability, I gave AI a "From Strong to Weak Leaderboard background image":

![](https://pic.yupi.icu/1/1766552716828-cc3c5015-a220-44c4-9c99-9ea6e6cc9a2e.png)

AI's understanding is quite accurate, even reading the specific text.

OK, all capabilities meet requirements. Below let's enter the solution design and development phase.



## Design and Development

First create a clean project directory `yupi-code`, open terminal and enter that directory:

![](https://pic.yupi.icu/1/1766545100781-86907b5b-56df-42de-a36f-21b2738102cd.png)



Then enter the prompt:

```markdown
Help me develop a terminal AI programming tool similar to Claude Code, capable of using GLM-4.7 model to help users answer questions and generate code
```

Generally, the first prompt of the entire project is the most important. If I were developing a complex commercial project, I would definitely polish this prompt carefully, writing at least a few hundred words (students who've seen my [AI Programmer Training Ground Project](https://mp.weixin.qq.com/s/cd7K9WQiOkP7AJglZ1b1Ng) should know).

![](https://pic.yupi.icu/1/1766553004293-19edef3f-ab54-4275-83fa-d5d78ed1a8ce.png)

But when testing AI models, I like to do the opposite — standing from most users' perspective, deliberately entering a simple prompt to see if AI can guide me to generate a project that meets requirements.

Sure enough, AI determined this is a complex project and wanted to enter **planning mode** — first clarify requirements, design solution, then develop.

![](https://pic.yupi.icu/1/1766545143400-e5909edc-d015-4ed8-8a98-c1428a5807e4.png)



Then we need to clarify requirements through selection, and let AI generate a solution.

Claude Code's interaction is quite well done. First select programming language — suggest honestly choosing the first one AI recommends:

![](https://pic.yupi.icu/1/1766545700277-0a92c7af-af6a-4bf3-b045-b35a8810fe82.png)



Next is selecting features for the project. If it were before, I might first let AI only develop basic conversation functionality, get the flow working, then add other features.

But now I have more confidence in AI. **Let's just select all the features and get it done!**

![](https://pic.yupi.icu/1/1766545748726-b5bcf0c2-1650-409d-9cfb-56874d80e7aa.png)



Other settings don't need much explanation:

![](https://pic.yupi.icu/1/1766545906676-50ffc0ba-404a-42e0-af0e-c4797a5d5d77.png)



After completing selections, AI gives a detailed implementation plan. Must read carefully:

![](https://pic.yupi.icu/1/1766546189349-27a4a8d7-92c0-4cf4-931e-e98e304736c9.png)



You can directly execute, or give AI further guidance. For example, I let AI-generated application call Zhipu Coding Plan package's BASE URL, which can save some cost, and provided AI with official API documentation to facilitate AI generating accurate code.

![](https://pic.yupi.icu/1/1766546246817-adc95f50-246d-4c9c-b0cd-35f6433c9b40.png)



After confirming, start execution. AI will first call built-in tools to search and parse documentation:

![](https://pic.yupi.icu/1/1766546433884-517bb8d9-8eb0-4a44-bd9c-0b0591af4184.png)



Then AI lists a Todo List and generates code and documentation step by step:

![](https://pic.yupi.icu/1/1766546471145-170595b6-05b5-440e-a208-671c362eb002.png)



During this time, if you discover serious problems, like finding AI-generated code has completely deviated from expectations, then pause early or manually input prompts to guide AI. If you find AI only generated a small piece of code incorrectly, my suggestion is to endure it — AI will mostly likely discover and fix the problem itself in the end.

After about ten-plus minutes, AI generation is complete, and it even told me how to use it:

![](https://pic.yupi.icu/1/1766546800949-d8f28864-141e-477e-af98-a25bf02d99e7.png)



Unfortunately, I'm too lazy to read. I'll just give the API Key to AI and have it run for me, right?

In Vibe Coding development mode, everything I do myself is disrespect to AI.

![](https://pic.yupi.icu/1/1766553290398-ad4d9c90-f804-4f46-b040-c65f821897d0.png)

Input prompt:

```markdown
My API key is xxxxxxx, please help me run it
```



Then, it crashed...

![](https://pic.yupi.icu/1/1766546943625-ae073ada-da33-429a-bbf8-a642f50204dd.png)



Don't panic, directly let AI check and fix errors itself. Also for convenience, should provide a quick start script that lets me start the AI programming tool with one command like running Claude Code.

Prompt:

```markdown
Help me check and fix errors in the project, and create a shortcut script that lets users start the program by entering "yupicode" in command line like Claude
```



A few minutes later, AI finished fixing and provided a `yupicode` script:

![](https://pic.yupi.icu/1/1766547157316-1e78081d-7d98-43c2-8fc6-37f40dcd1d81.png)



I opened a new terminal, then ran the `yupicode` script, trying to converse with AI:

![](https://pic.yupi.icu/1/1766488187720-0dedd977-3663-4146-8fc6-bd5e8d65a7ea.png)

I have to say, the effect is pretty good!

It even provides some commands like Claude Code, such as clearing conversation history, viewing help, etc.:

![](https://pic.yupi.icu/1/1766488215355-476254ae-1fdd-44fe-94a7-939621a5b3f3.png)



Seeing this, I feel the project is basically usable. Suggest using Git for version control to prevent issues from subsequent changes.

What? You don't know what Git is?

No problem, just give it to AI:

```markdown
Now the project is basically usable, help me commit a git version to prevent issues from subsequent changes
```

![](https://pic.yupi.icu/1/1766547719776-e4ca2495-158d-441e-b995-d2e3b475187b.png)



Testing reveals the current Yupi Code still has some shortcomings, like not supporting search:

![](https://pic.yupi.icu/1/1766488309079-9e05324c-b780-4476-b7a1-09e0b0a12ed4.png)

Next let's optimize the project and add more Claude Code-supported capabilities.



## Capability Optimization

1) First add web search capability, directly throw Zhipu's official documentation to it. Prompt as follows:

```markdown
Seems like web search isn't supported now, please refer to
  https://docs.bigmodel.cn/api-reference/%E5%B7%A5%E5%85%B7-api/%E7%BD%91%E7%BB%9C%E6%90%9C%E7%B4%A2
  documentation, add web search tool calling capability
```



![](https://pic.yupi.icu/1/1766547400820-047db1e2-dee7-4bb3-875c-3c3d03d7bf60.png)



Soon AI added the new feature. Reopen yupicode to verify — it's working normally:

![](https://pic.yupi.icu/1/1766542072968-2a635280-4f04-41c7-9e72-b149b503b18e.png)



2) Next optimize AI response effect. Currently it waits a bit then directly outputs complete answer. Need to adjust to streaming output typewriter effect.

Prompt:

```markdown
I hope to have a spinning icon while waiting for AI response; and AI's response can be real-time streaming output
```



AI quickly handled it:

![](https://pic.yupi.icu/1/1766547560315-96b3044c-21d4-4017-b3b2-8e6c599fdfac.png)



3) GLM-4.7 further strengthened interleaved thinking capabilities, introducing **reserved thinking** and **round-level thinking**, making complex task execution more stable and controllable. We should also let Yupi Code output model thinking information, tool calling information, etc., to help users understand the situation.

Input prompt:

```markdown
Help me output model thinking information and tool calling information. You can understand how to develop through official documentation
```



![](https://pic.yupi.icu/1/1766547838246-0de4e1a6-46e7-4fa0-9f69-2cc6c137d941.png)



Test the optimized effect. For example "Introduce Fish Skin's AI Navigation website," you can clearly see the thinking process:

![](https://pic.yupi.icu/1/1766491085646-e55d65e2-f1f4-4de5-9b2e-a580f6671fab.png)



## Mission Accomplished

Here, Yupi Code developed by imitating Claude Code is complete. Let's use it to try developing a small website.

For example, an animated algorithm learning Demo. Prompt:

```markdown
Help me develop an animated website for learning bubble sort algorithm, using Q-version anime style and Chiikawa color scheme
```



![](https://pic.yupi.icu/1/1766491627903-c7a8401b-a029-4f60-86c2-583459f60098.png)



Effect shown in picture — the art style is quite good. But if later large models can automatically generate illustration images and add them to websites, that would be even better.

![](https://pic.yupi.icu/1/1766492330648-78beb8fe-20f5-4577-9a5a-9c6844b15ba1.png)



Now develop a simulated electronic blackboard. Prompt:

```markdown
Help me develop a simulated electronic blackboard where users can draw and export as images
```



![](https://pic.yupi.icu/1/1766543009945-1be675f7-2cb1-43ce-9794-36cfa3cf9f87.png)



It's Christmas, Fish Skin draws everyone a Christmas tree, plus a small gift — how can this not be considered programmer romance~

![](https://pic.yupi.icu/1/1766548114861-81c8b4d2-b7fc-4134-8722-264edf56f229.png)



------



OK, this is my complete process of **using domestic AI large model GLM-4.7 + Claude Code** to develop a **GLM-4.7-based Yupi Code**.

From my experience, GLM-4.7 compared to previous domestic large models has improved stability in handling complex tasks. Even when encountering problems, it will automatically fix them, making the final generated code runnable.

Moreover, GLM-4.7's tool calling ability is strengthened. Working with AI programming tools like Claude Code, it directly has built-in web search, web reading, image interpretation and other common AI programming capabilities, without needing to find MCP to enhance yourself.

I have to say, as a loyal developer who has been following Zhipu AI, I can really feel their efforts in the AI programming direction over these past few months. I believe everyone has witnessed it too.

However, since the current Yupi Code was entirely done by AI in one go, there are still many areas that can be optimized and improved. If there's time later and everyone is interested, perhaps I'll properly refine this tool and open-source it. My ultimate goal is to let the **AI large model GLM-4.7 + Claude Code** developed **GLM-4.7-based Yupi Code** programming tool be able to develop a **GLM-4.7-based** programming tool, like Yupi Son Code. I think good AI tools should be able to achieve infinite nesting, crazy self-bootstrapping!

![](https://pic.yupi.icu/1/1766549948743-c5e1340a-5b3d-4419-b5df-c2fd4a5c2c7f.jpeg)

Understand, applause~


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
