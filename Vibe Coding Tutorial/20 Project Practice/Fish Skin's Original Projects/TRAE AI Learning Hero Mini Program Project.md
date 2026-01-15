# TRAE - AI Learning Hero Mini Program Project Practice

This is a Learning Hero WeChat Mini Program project that helps users learn any subject through gamification. Users input a topic they want to learn, and AI automatically generates related knowledge Q&A cards. Learning happens through answering multiple-choice questions.

This is a pure Vibe Coding project, primarily teaching how to use the TRAE AI programming tool to quickly develop WeChat Mini Programs. By describing requirements in natural language, AI automatically generates Mini Program code with complete frontend and backend, and leverages TRAE's integrated database and payment services. Suitable for students who want to learn AI-driven Mini Program development and master the TRAE tool.



---

Hello everyone, I'm Programmer Fish Skin. Have you ever had this experience: want to learn some new technology, get a headache opening documentation, easily get distracted watching videos, buy a bunch of courses but always give up halfway...

I'm like this often, a late-stage patient of learning anxiety.

![](https://pic.yupi.icu/1/image-20250928214315214.png)

As a programmer, I've long wanted to create a program to cure my learning anxiety, but kept procrastinating because it seemed too complicated. Until now, when AI programming became powerful enough, I finally took action! Using TRAE, I completed this "Learning Hero" Mini Program in just 1 day, making learning as relaxed and fun as playing games~

![](https://pic.yupi.icu/1/%E5%B0%8F%E7%A8%8B%E5%BA%8F%E6%BC%94%E7%A4%BA%E6%8B%BC%E5%9B%BE.png)

Let me first take everyone through experiencing this Mini Program, then I'll share the tools and techniques used throughout the development process. Still a **comprehensive AI project development tutorial**.

Save this and let's get started!

> Recommended video version: https://bilibili.com/video/BV1yMn3zuE7L



## Project Experience

Open the Mini Program and you'll see a very clean and vibrant interface. Click Start Learning, then input any topic you want to learn, such as Java Basics.

![](https://pic.yupi.icu/1/image-20250928215038368.png)

AI will automatically generate related knowledge Q&A cards based on the topic.

![](https://pic.yupi.icu/1/image-20250928215106136.png)

Then you just need to click-click-click to answer multiple-choice questions. Don't worry about getting them wrong, because every question has explanations. Even if you've never heard of this topic before, you can still learn.

![](https://pic.yupi.icu/1/image-20250928215137518.png)

Besides technical knowledge, you can also try more topics, like a vocabulary word, a movie, or even a person.

![](https://pic.yupi.icu/1/%E5%A4%9A%E7%AD%94%E9%A2%98%E6%8B%BC%E5%9B%BE.png)

Originally boring concepts become vivid and interesting through Q&A format. Learning anxiety disappears instantly~

You can also view your learning history, relearn or check solutions.

![](https://pic.yupi.icu/1/%E5%AD%A6%E4%B9%A0%E5%8E%86%E5%8F%B2%E6%8B%BC%E5%9B%BE.png)

Brush up occasionally, and you can become a Learning Hero!



## Development Implementation

In the past, a Mini Program like this might take several days.

But now using TRAE IDE's AI programming, I'll guide everyone to build this Mini Program **without writing a single line of code**.

Steps:

1. Prepare development tools
2. Requirements analysis
3. Solution design
4. Service integration
5. Backend development
6. Frontend development
7. Testing and verification
8. Continuous optimization



### 1. Prepare Development Tools

Since we're using AI for development, tool selection is important. This time I'm using the [TRAE](https://www.trae.ai/) AI programming tool because its SOLO mode has been really hot lately, and I wanted to try it.

Unlike traditional human-led + AI-assisted programming, SOLO mode lets **AI lead tasks and automatically execute development**. You just need an idea, then work with AI to make that idea a reality.

![](https://pic.yupi.icu/1/image-20250928220322788.png)

Additionally, since we're developing a frontend project, we definitely need [Node.js environment](https://nodejs.org/zh-cn/download); since we're developing a WeChat Mini Program, we definitely need [WeChat Developer Tools](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html). Just go to the corresponding official websites to download and install.

![](https://pic.yupi.icu/1/%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7%E6%8B%BC%E5%9B%BE.png)



### 2. Requirements Analysis

After preparing tools, enter Trae's SOLO mode and open a project folder cleaner than my face.

![](https://pic.yupi.icu/1/image-20250928220647365.png)

First, we need to do requirements analysis.

Don't overthink it — just tell AI your idea in natural language.

For example, I gave AI this requirement:

```markdown
You are a professional programmer. Please help me develop the "Learning Hero - AI Q&A Guided Learning" WeChat Mini Program.

Users can independently set a topic they want to learn (or be tested on), and AI will generate several interesting knowledge Q&A cards around the topic, guiding users to master knowledge more easily and happily through level-based Q&A.
```

![](https://pic.yupi.icu/1/image-20250928221154635.png)

AI quickly generated detailed product requirements document and technical architecture document, following enterprise-standard development process.

![](https://pic.yupi.icu/1/image-20250928221128338.png)

You can see AI is eager to write code, but don't rush —一定要先 **仔细确认需求文档**.

AI did a good job, but it might not completely match our expectations. So we need to manually focus on the core features to implement, remove unnecessary extra features, and first ensure the core business flow (P0 requirements) works.

![](https://pic.yupi.icu/1/image-20250928221334652.png)

**不要嫌这一步麻烦，现在多花 1 分钟，以后节约 1 小时！**

Must clarify requirements to prevent AI from doing features it shouldn't.

Here's a tip: you can leverage TRAE's integrated Figma design tool to get some free product UI prototype designs here.

![](https://pic.yupi.icu/1/image-20250928221519374.png)

You can click to view a specific prototype's design. Just select the prototype you like, click add to conversation, and TRAE will automatically associate the prototype with the conversation sent to AI. This cross-product interaction is quite cool (though students learning with me should know the implementation principle hehe).

![](https://pic.yupi.icu/1/image-20250928221618668.png)

But life needs surprises, so here I'll let AI play freely and see what creativity emerges~



### 3. Solution Design

Next, we need to do solution design. This used to be the job of architects earning tens of thousands monthly, but now let little AI help us SOLO.

When writing this prompt, pay attention to several details and **follow the minimal development principle** to prevent AI from making simple things complex.

```markdown
I have manually adjusted the product requirements document and removed many unnecessary features. Please regenerate the technical architecture document based on my manually modified requirements. Requirements:
1. Prohibit adding features not mentioned in the requirements document
2. Follow minimal development principle, focus on implementing functionality, prohibit providing extensions beyond implementing features, such as deployment, monitoring, rate limiting, etc.
3. Follow frontend-backend separation principle
```

Soon AI generated a complete technical architecture document, including what frontend and backend technologies to use, how to design interfaces, how to design database tables, etc.

![](https://pic.yupi.icu/1/image-20250928221924096.png)

Here I suggest students who can understand the document should still show some professionalism, clarify specific technology choices, and keep AI-generated code within your controllable range. For example, I explicitly specified the project uses Supabase database, uses OpenRouter to integrate Gemini large model for AI services.

![](https://pic.yupi.icu/1/image-20250928221952548.png)

What what what? What are these?

Don't worry, I'll explain soon.

![](https://pic.yupi.icu/1/image-20250928222144713.png)

Students who don't understand the document don't need to worry either. Just imagine yourself as a boss or product manager. Your programmer colleague worked hard to bring you a technical solution, and you say "I don't care how to implement it, this requirement goes live tomorrow!" Let them go for it.

You must trust AI, trust the power of belief~



### 4. Service Integration

After completing solution design, before officially starting development, we also need to prepare the services that the project depends on.

Where to store user data? How to make the program connect to AI large models?

These are problems we need to solve.

Compared to manually installing services yourself, you can directly use TRAE's integration capabilities without needing to read official documentation to integrate services — foolproof installation.

We focus on integrating 2 services.

![](https://pic.yupi.icu/1/image-20250928222329915.png)



#### Integrate Supabase

[Supabase](https://supabase.com/) is an open-source Backend-as-a-Service (BaaS) platform that provides database storage, user authentication, instant APIs and other functions, helping developers quickly build and manage program backends.

![](https://pic.yupi.icu/1/image-20250928222457606.png)

Click the connect button, and in the popup page complete creating a Supabase account, creating an organization, and authentication authorization.

![](https://pic.yupi.icu/1/image-20250928222520491.png)

Then enter TRAE, after seeing the organization successfully displayed, click create a new project, fill in some project configuration information, then click create.

![](https://pic.yupi.icu/1/image-20250928222545479.png)

After creating the project, return to TRAE and refresh, then click connect — it's that simple~

![](https://pic.yupi.icu/1/image-20250928222608471.png)

If previous AI Vibe Coding made backend developers feel great, this wave is a huge win for frontend developers — simple projects don't even need to build their own backends~



#### Integrate OpenRouter AI Service

TRAE can integrate with multiple AI services. Here I chose [OpenRouter](https://openrouter.ai/). Its advantage is being able to connect to various large models through a unified API, such as Gemini, GPT, Claude, etc.

![](https://pic.yupi.icu/1/image-20250928222649319.png)

First, go to the official website to register and login, then enter the API Keys page to create a key for calling AI, then configure and fill in the key in TRAE — the AI service is integrated.

![](https://pic.yupi.icu/1/image-20250928222833273.png)

But note, ensure you have enough usage, otherwise calls may fail or report errors for too frequent calls.

![](https://pic.yupi.icu/1/image-20250928222853247.png)



#### Integrate Stripe Payment Service

Additionally, you can integrate [Stripe payment service](https://docs.stripe.com/), which lets you add payment and subscription features to your product with minimal code.

![](https://pic.yupi.icu/1/image-20250928223013523.png)

Just go to the official website to register an account, it will automatically provide you with a sandbox test environment and corresponding API keys. You can create your own products and set pricing.

![](https://pic.yupi.icu/1/image-20250928223151134.png)

Then fill this information into TRAE configuration, and afterwards AI programming will generate payment-related code.

![](https://pic.yupi.icu/1/image-20250928223346093.png)

However, since WeChat Mini Programs have some restrictions, I won't integrate it here. Everyone just needs to understand — it's still quite useful for web and APP products.



### 5. Backend Development

After completing preparations, we finally enter the exciting development phase.

Here note that since **AI's context is limited**, to better generate complete projects and reduce bugs, it's recommended to do it in steps: first generate backend code, after manual verification passes, then generate frontend code.

OK, give AI the prompt, first develop backend, ensure project can run normally:

```markdown
Please develop based on the latest product requirements document and technical architecture document, prioritize backend development, ensure project can run normally
```

We can use TRAE's prompt optimization feature for one-click prompt optimization.

![](https://pic.yupi.icu/1/%E4%BC%98%E5%8C%96%E6%8F%90%E7%A4%BA%E8%AF%8D.png)

Hmm, indeed more rigorous than before.

Click execute, please start your SOLO~ AI will first give a task plan:

![](https://pic.yupi.icu/1/image-20250928224232897.png)

Then it autonomously operates the terminal to execute commands, writes backend configuration files and business logic code, writes database table creation statements, etc. For important operations it will actively seek our confirmation — very rigorous.

![](https://pic.yupi.icu/1/image-20250928224300188.png)

If you don't understand, no problem — let it go~

While waiting, you can check out [free programming learning roadmaps](https://codefather.cn/) on Programming Navigation. TRAE has a built-in message notification feature — AI will notify us when tasks are complete.

I feel TRAE has a good handle on training AI — it will verify whether the program runs normally. However, since we haven't filled in the information required for WeChat login, it's normal that interfaces can't be fully called.

![](https://pic.yupi.icu/1/image-20250928224350332.png)

After some time, AI generation is complete. Not only did it generate code, it also thoughtfully generated backend API documentation.

![](https://pic.yupi.icu/1/image-20250928224437599.png)

Hey, this is very useful.



### 6. Frontend Development

Next, frontend development.

Here be careful — don't continue the previous conversation to write prompts.

Why?

Because AI large model's context is limited. Previous operations have already consumed quite a bit of context. To prevent insufficient AI context or confused memory, when generating frontend, open a new clean conversation to write prompts.

![](https://pic.yupi.icu/1/image-20250928224735250.png)

Provide AI with product requirements document, technical architecture document, and backend API documentation in the prompt, and you can let AI focus on frontend code generation.

```markdown
You are a professional programmer. Please help me develop the "Learning Hero - AI Q&A Guided Learning" WeChat Mini Program.

Users can independently set a topic they want to learn (or be tested on), and AI will generate several interesting knowledge Q&A cards around the topic, guiding users to master knowledge more easily and happily through level-based Q&A.

Please generate complete, runnable WeChat Mini Program frontend code for me based on @Product Requirements Document @Technical Architecture Document @Backend API Documentation.
Note:
1. Follow minimal feature principle — don't develop any features not mentioned in the requirements document
2. If displaying images, please use placeholder images picsum.photos (for example picsum.photos/200/300)
```

OK, execute!

While waiting, you can check out free interview questions and practice routes on [Interview Duck](https://www.mianshiya.com/).

After some time, AI generation is complete — it SOLO'd 20+ files at once!

![](https://pic.yupi.icu/1/image-20250928224830751.png)

Although it looks cool, honestly I'm a bit nervous — don't know if it can run normally.



### 7. Testing and Verification

Next, we come to the exciting testing and verification phase.

First need to open WeChat Developer Tools, import existing project folder, first choose to use test account for development and debugging.

![](https://pic.yupi.icu/1/image-20250928225118198.png)

After opening the project, first click "Test Account" in the upper right, follow the [documentation](https://developers.weixin.qq.com/miniprogram/dev/devtools/sandbox.html) guidance to get the test account's AppID and AppSecret key:

![](https://pic.yupi.icu/1/image-20250928225220066.png)

Then manually fill them into the backend configuration file, otherwise WeChat login won't work.

![](https://pic.yupi.icu/1/image-20250928225304614.png)

Then we can compile and run the project.

Result — error as expected!

![](https://pic.yupi.icu/1/image-20250928225522618.png)

Expected, expected... Mini Program development is still harder than web development, after all WeChat Developer Tools and documentation are constantly updating.

![](https://pic.yupi.icu/1/image-20250928225618743.png)

But no problem, issues are inevitable during development. The solution is simple, one sentence: **Whatever error you get, send the error message to AI and let AI fix it!**

Like I encountered several typical problems:

1) Image path problem: Use TRAE's prompt optimization feature to better guide AI to fix bugs according to specified steps

![](https://pic.yupi.icu/1/image-20250928225717687.png)

2) Login failure problem: Click "Details" in the upper right of Developer Tools, enter local settings, check "Don't verify legal domains"

![](https://pic.yupi.icu/1/image-20250928225825654.png)

3) Interface path problem: This might be caused by too long context — let AI comprehensively fix frontend's backend interface call paths and parameters

![](https://pic.yupi.icu/1/image-20250928225903118.png)

4) Environment configuration problem: Environment variable names read in code don't match configuration file — this problem is relatively simple, we can manually modify.

When I typed a character, the editor automatically prompted which code to modify, and supports cross-line modification.

![](https://pic.yupi.icu/1/image-20250928225955681.png)

This is TRAE's CUE feature — not only helps you auto-complete code, but also multi-line modify code, auto-predict future possible modification points, especially suitable for code refactoring scenarios, efficiency takes off.

![](https://pic.yupi.icu/1/%E5%A4%9A%E8%A1%8C%E4%BF%AE%E6%94%B9.gif)

After a period of fixing, our Mini Program can run normally. Although the pages look ugly now, as long as the core business flow works and users can use it normally, subsequent optimization is very simple.

![](https://pic.yupi.icu/1/image-20250928230045861.png)



### 8. Continuous Optimization

Finally, if you want to launch the Mini Program, you still need to spend some time optimizing.

Remember, before optimizing, first use Git version control to host existing code and commit a base version. This way, if any problems occur during optimization, you can one-click rollback to the old version.

![](https://pic.yupi.icu/1/image-20250928230154447.png)

Like I mainly had AI help optimize the entire Mini Program's style. Just write a simple prompt:

```markdown
You are a programmer. Please help me optimize the style of each frontend page and element in the entire Mini Program to keep each page consistent.

Reference style: Main color uses vibrant orange, fresh healing cartoon style, simple and elegant, making people feel relaxed and happy.
```

Then use TRAE's prompt optimization feature to get a more detailed optimization plan.

![](https://pic.yupi.icu/1/image-20250928230225960.png)

You can adjust as needed, or let AI go for it.

I suggest everyone commit code after each optimization or new feature, and appropriately open new AI conversations to prevent too much context affecting generation accuracy.

Ultimately, the Mini Program you see is my optimized result — not bad right~

![](https://pic.yupi.icu/1/image-20250928230316272.png)

But since I'm stuck in the certification filing process (already filing), it will be a while before everyone can experience the Mini Program.

![](https://pic.yupi.icu/1/%E5%A4%87%E6%A1%88.png)



## Summary

Finally, let me talk about my feelings using TRAE SOLO for project development.

First, I felt the evolution of AI programming tools — SOLO evolved from **integrating AI into tools to integrating development tools into AI**.

![](https://pic.yupi.icu/1/image-20250928220158367.png)

It feels like development tools are just AI's plaything — it can freely operate the editor, terminal, browser, documentation, integrated services, etc. to autonomously complete tasks. It's indeed more efficient and intelligent than before, and can complete full projects including backend. Moreover, AI follows enterprise-standard development processes, automatically fixes most problems, checks if projects can run — unlike before when generated code often couldn't run.

But during development everyone note: now **AI really likes to make simple things complex**, so it's best to manually carefully confirm requirements documents and solution documents, and like building blocks, complete development step by step.

Later I'll also share more AI programming techniques — after all, AI is a tool, and only when used correctly can it maximize its value.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
