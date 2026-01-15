# TRAE SOLO: AI-Led Full-Stack Development Tool

Hello, I'm Fish Skin.

In previous articles, we learned about various AI programming tools. Whether Cursor or Claude Code, they both use a **human-led + AI-assisted** mode, where you need to constantly converse with AI, confirm, and modify.

But if you want AI to be more proactive, planning tasks itself and automatically executing development, what tool should you use?

In this article, I'll introduce TRAE SOLO, a full-stack development tool that lets AI lead development tasks.



## I. What is TRAE SOLO?

[TRAE](https://www.trae.ai/) is an AI-native programming tool launched by ByteDance, with 2 development modes:

- IDE Mode: Similar to Cursor, preserves traditional development workflow, human-led
- SOLO Mode: Lets AI lead, automatically advance development tasks

The so-called SOLO mode lets **AI lead tasks and automatically execute development**. You only need to have an idea, then work with AI to make that idea a reality.

![](https://pic.yupi.icu/1/image-20250928220322788.png)

What's the difference between TRAE SOLO and Cursor?

To use an analogy, using Cursor is like you're the project manager and AI is the programmer — you need to constantly assign tasks to AI, check results, and suggest modifications. While using TRAE SOLO, AI is both project manager and programmer — you just tell it the goal, and it plans, develops, and tests itself.

According to the latest 2026 evaluation, TRAE performs excellently among AI programming software, especially its customizable agent system, which allows users to define and configure AI agents with different roles and skills based on project needs, like assembling a team.



## II. Core Features of TRAE SOLO

### 1. Automatic Document Generation

TRAE SOLO automatically generates based on your requirements:

- Product Requirements Document (PRD)
- Technical Architecture Document
- API Documentation
- Test Reports

These documents follow enterprise-standard development processes and are very professional.



### 2. Service Integration Capability

TRAE provides powerful integration capabilities, allowing foolproof integration of various services:

- Supabase: Database storage and user authentication
- Stripe: Payment functionality
- OpenRouter: AI services
- Figma: Design prototypes

No need to read official documentation — just click a few times in TRAE to complete integration.

![](https://pic.yupi.icu/1/image-20250928222329915.png)



### 3. Multi-Task Parallel Execution

TRAE SOLO supports multi-task parallel execution, can develop frontend and backend simultaneously, greatly improving efficiency.



### 4. Code Change Tool

TRAE provides DiffView code change tool, clearly showing what code was modified each time, facilitating review and rollback.



### 5. Plan Mode

Besides direct execution, TRAE also supports Plan mode. AI first generates a detailed execution plan, which you confirm before execution. This allows better control over the development process.



## III. How to Use TRAE SOLO?

Let me demonstrate TRAE SOLO's usage workflow with a practical example.

⭐️ Recommended to watch Fish Skin's video tutorial directly, more detailed explanation: https://www.bilibili.com/video/BV1yMn3zuE7L



### Preparation

First need to prepare development tools:

- Download and install [TRAE](https://www.trae.ai/)
- Install [Node.js environment](https://nodejs.org/zh-cn/download)
- If developing Mini Program, also need [WeChat Developer Tools](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)

![](https://pic.yupi.icu/1/%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7%E6%8B%BC%E5%9B%BE.png)



### 1. Requirements Analysis

After preparing tools, enter TRAE's SOLO mode and open a blank project folder.

![](https://pic.yupi.icu/1/image-20250928220647365.png)

First we need to do requirements analysis. Don't overthink it — just tell AI your idea in natural language.

For example, I gave AI this requirement:

```
You are a professional programmer. Please help me develop the "Learning Hero - AI Q&A Guided Learning" WeChat Mini Program.

Users can independently set a topic they want to learn (or be tested on), and AI will generate several interesting knowledge Q&A cards around the topic, guiding users to more easily and happily master knowledge through level-based Q&A.
```

![](https://pic.yupi.icu/1/image-20250928221154635.png)

AI quickly generated detailed product requirements document and technical architecture document, very much following enterprise-standard development process.

![](https://pic.yupi.icu/1/image-20250928221128338.png)

You can see AI is already itching to write code, but don't rush — must first **carefully confirm requirements document**.

AI wrote it quite well, but it might not completely match our expectations. So we need to manually focus on core features to implement, remove unnecessary extra features, first ensure core business flow (P0 requirements) works.

![](https://pic.yupi.icu/1/image-20250928221334652.png)

**Don't find this step troublesome — spend 1 minute now, save 1 hour later!** Must clarify requirements to prevent AI from doing features it shouldn't.

Here's a tip: you can use TRAE's integrated Figma design tool to get some free product UI prototypes here.

![](https://pic.yupi.icu/1/image-20250928221519374.png)

You can click to view a specific prototype's design. Just select the prototype you like, click add to conversation, and TRAE will automatically associate the prototype with the conversation sent to AI.

![](https://pic.yupi.icu/1/image-20250928221618668.png)



### 2. Solution Design

Below we need to do solution design. This used to be the job of architects earning tens of thousands monthly — now let little AI help us SOLO.

When writing this prompt, pay attention to several details and **follow the minimal development principle** to prevent AI from making simple things complex.

```
I've manually adjusted the product requirements document and removed many unnecessary features. Please regenerate the technical architecture document based on my manually modified requirements. Requirements:
1. Prohibit adding features not mentioned in the requirements document
2. Follow minimal development principle, focus on implementing functionality, prohibit providing extensions beyond implementing features, such as deployment, monitoring, rate limiting, etc.
3. Follow frontend-backend separation principle
```

Soon AI generated a complete technical architecture document, including what frontend and backend technologies to use, how to design interfaces, how to design database tables, etc.

![](https://pic.yupi.icu/1/image-20250928221924096.png)

Here I suggest students who can understand the document should still show some professionalism, clarify specific technology choices, and keep AI-generated code within your controllable range. For example, I explicitly specified the project uses Supabase database and uses OpenRouter to integrate Gemini large model for AI services.

![](https://pic.yupi.icu/1/image-20250928221952548.png)

Students who don't understand the document don't need to worry. Just imagine yourself as a boss or product manager. Your programmer colleague worked hard to bring you a technical solution, and you say "I don't care how to implement it, this requirement goes live tomorrow!" Let them go for it.

You must trust AI, trust the power of belief.



### 3. Service Integration

After completing solution design, before officially starting development, we also need to prepare services the project depends on.

Where to store user data? How to make the program connect to AI large models? These are problems we need to solve.

Compared to manually installing services yourself, you can directly use TRAE's integration capabilities — no need to read official documentation to integrate services, just foolproof installation.

![](https://pic.yupi.icu/1/image-20250928222329915.png)

#### Integrate Supabase

[Supabase](https://supabase.com/) is an open-source Backend-as-a-Service (BaaS) platform, providing database storage, user authentication, instant APIs and other functions.

![](https://pic.yupi.icu/1/image-20250928222457606.png)

Click the connect button, and in the popup page complete creating a Supabase account, creating an organization, and authentication authorization.

![](https://pic.yupi.icu/1/image-20250928222520491.png)

Then enter TRAE, after seeing the organization successfully displayed, click create a new project, fill in some project configuration information, then click create.

![](https://pic.yupi.icu/1/image-20250928222545479.png)

After creating the project, return to TRAE and refresh, then click connect — it's that simple.

![](https://pic.yupi.icu/1/image-20250928222608471.png)

If previous AI Vibe Coding made backend developers feel great, this wave is a huge win for frontend developers — simple projects don't even need to build their own backends.



#### Integrate OpenRouter AI Service

TRAE can integrate with multiple AI services. Here I chose [OpenRouter](https://openrouter.ai/), whose advantage is being able to connect to various large models through a unified API, like Gemini, GPT, Claude, etc.

![](https://pic.yupi.icu/1/image-20250928222649319.png)

First go to the official website to register and login, then enter the API Keys page to create a key for calling AI, then configure and fill in the key in TRAE — the AI service is integrated.

![](https://pic.yupi.icu/1/image-20250928222833273.png)

But note, ensure you have enough usage, otherwise calls may fail or report errors for too frequent calls.

![](https://pic.yupi.icu/1/image-20250928222853247.png)



### 4. Backend Development

After completing preparations, we finally enter the exciting development phase.

Here note that since **AI's context is limited**, to better generate complete projects and reduce bugs, it's recommended to do it in steps: first generate backend code, after manual verification passes, then generate frontend code.

Give AI the prompt, first develop backend, ensure project can run normally:

```
Please develop based on the latest product requirements document and technical architecture document, prioritize backend development, ensure project can run normally
```

We can use TRAE's prompt optimization feature for one-click prompt optimization.

![](https://pic.yupi.icu/1/%E4%BC%98%E5%8C%96%E6%8F%90%E7%A4%BA%E8%AF%8D.png)

Click execute, please start your SOLO. AI will first give a task plan:

![](https://pic.yupi.icu/1/image-20250928224232897.png)

Then it autonomously operates the terminal to execute commands, writes backend configuration files and business logic code, writes database table creation statements, etc. For important operations it will actively seek our confirmation — very rigorous.

![](https://pic.yupi.icu/1/image-20250928224300188.png)

If you don't understand, no problem — let it go.

While waiting, you can check out [free programming learning roadmaps](https://codefather.cn/) on Programming Navigation. TRAE has a built-in message notification feature — AI will notify us when tasks are complete.

I feel TRAE has a good handle on training AI — it will verify whether the program runs normally.

![](https://pic.yupi.icu/1/image-20250928224350332.png)

After some time, AI generation is complete. Not only did it generate code, it also thoughtfully generated backend API documentation.

![](https://pic.yupi.icu/1/image-20250928224437599.png)



### 5. Frontend Development

Next is frontend development.

Here be careful — don't continue the previous conversation to write prompts.

Why? Because AI large model's context is limited. Previous operations have already consumed quite a bit of context. To prevent insufficient AI context or confused memory, when generating frontend, open a new clean conversation to write prompts.

![](https://pic.yupi.icu/1/image-20250928224735250.png)

Provide AI with product requirements document, technical architecture document, and backend API documentation in the prompt, and you can let AI focus on frontend code generation.

```
You are a professional programmer. Please help me develop the "Learning Hero - AI Q&A Guided Learning" WeChat Mini Program.

Users can independently set a topic they want to learn (or be tested on), and AI will generate several interesting knowledge Q&A cards around the topic, guiding users to more easily and happily master knowledge through level-based Q&A.

Please generate complete, runnable WeChat Mini Program frontend code for me based on @Product Requirements Document @Technical Architecture Document @Backend API Documentation.
Note:
1. Follow minimal feature principle — don't develop any features not mentioned in the requirements document
2. If displaying images, please use placeholder images picsum.photos (for example picsum.photos/200/300)
```

Okay, execute!

While waiting, you can check out [free interview questions and practice routes](https://www.mianshiya.com/) on Interview Duck.

After some time, AI generation is complete — it SOLO'd 20+ files at once!

![](https://pic.yupi.icu/1/image-20250928224830751.png)

Although it looks cool, honestly I'm a bit nervous — don't know if it can run normally.



### 6. Testing and Verification

Next we come to the exciting testing and verification phase.

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

This is TRAE's **CUE feature** — not only helps you auto-complete code, but also multi-line modify code, auto-predict future possible modification points, especially suitable for code refactoring scenarios, efficiency takes off.

![](https://pic.yupi.icu/1/%E5%A4%9A%E8%A1%8C%E4%BF%AE%E6%94%B9.gif)

After a period of fixing, our Mini Program can run normally. Although the pages look ugly now, as long as the core business flow works and users can use it normally, subsequent optimization is very simple.

![](https://pic.yupi.icu/1/image-20250928230045861.png)



### 7. Continuous Optimization

Finally, if you want to launch the Mini Program, you still need to spend some time optimizing.

Remember, before optimizing, first use Git version control to host existing code and commit a base version. This way, if any problems occur during optimization, you can one-click rollback to the old version.

![](https://pic.yupi.icu/1/image-20250928230154447.png)

Like I mainly let AI help optimize the entire Mini Program's style. Just write a simple prompt:

```
You are a programmer. Please help me optimize the style of each frontend page and element in the entire Mini Program to keep each page consistent.

Reference style: Main color uses vibrant orange, fresh healing cartoon style, simple and elegant, making people feel relaxed and happy.
```

Then use TRAE's prompt optimization feature to get a more detailed optimization plan.

![](https://pic.yupi.icu/1/image-20250928230225960.png)

You can adjust as needed, or let AI go for it.

I suggest everyone commit code after each optimization or new feature, and appropriately open new AI conversations to prevent too much context affecting generation accuracy.

Ultimately, the Mini Program you see is my optimized result — not bad right~

![](https://pic.yupi.icu/1/image-20250928230316272.png)



## IV. Pros and Cons of TRAE SOLO

TRAE SOLO's advantages are obvious.

First is **AI-led development** — you don't need to constantly converse with AI, AI will plan tasks itself and automatically execute. Also **strong service integration capability**, can foolproof integrate Supabase, Stripe and other services without reading documentation.

Plus **automatic document generation**, following enterprise-standard development process, generated documents are very professional. Also **fast access for domestic users**, friendly to Chinese users.

Of course there are some limitations.

First is **needs some guidance** — although AI can execute autonomously, the clearer your requirement description, the better AI's execution effect. Also **generated code may have bugs**, requiring manual testing and fixing.

Also, **context management is important**. If conversation is too long, AI may have confused memory, need to open new conversations timely.

In terms of pricing, TRAE has free and paid versions. Free version has usage limits, paid version charges based on usage.



## V. TRAE SOLO Practical Suggestions

If you want to try TRAE SOLO, I have several suggestions:

1. Clarify requirements

Although AI can plan autonomously, the clearer your requirements, the better AI's execution effect. Suggestions:

- Clearly state core functionality
- Remove unnecessary features
- Provide reference designs (if available)
- Clarify technology choices (if you understand them)



2. Develop in steps

Don't have AI generate the entire project at once, but in steps:

- First generate backend, test passes
- Then generate frontend, test passes
- Finally optimize styles and details

After completing each step, commit code once, so if there are problems you can rollback.



3. Fix bugs promptly

AI-generated code may have bugs, this is normal. When you discover problems, immediately have AI fix them — don't wait until problems pile up.

Send complete error messages to AI, it can generally fix them.



4. Control context

Conversations that are too long will affect AI's accuracy. Suggestions:

- Open new conversation after completing a major feature
- Reference previously generated documents in new conversation
- Avoid doing too much in one conversation



## In Conclusion

Seeing this, I believe you have a comprehensive understanding of TRAE SOLO.

**TRAE SOLO is an important evolution of AI programming tools**, evolving from "integrating AI into tools" to "integrating development tools into AI."

![](https://pic.yupi.icu/1/image-20250928220158367.png)

It feels like development tools are just AI's plaything — it can freely operate the editor, terminal, browser, documentation, integrated services, etc. to autonomously complete tasks. Indeed more efficient and intelligent than before, and can complete complete projects including backends.

But during development everyone note that now **AI really likes making simple things complex**, so it's best to manually carefully confirm requirements document and solution document, and like building blocks, complete development step by step.

Go try using TRAE SOLO to make a small project and experience the feeling of AI-led development~ 🛫




## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
