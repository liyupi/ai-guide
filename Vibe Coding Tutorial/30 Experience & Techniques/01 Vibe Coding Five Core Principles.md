# Vibe Coding Five Core Principles

> Five most important mindsets to take you from beginner to mastery



Hello, I'm Fish Skin.

If you've already used AI to create a few small projects, you might notice an interesting phenomenon: sometimes AI is particularly obedient and gets it right the first time; but other times it's particularly stubborn, and no matter what you say, it can't do well.

Why is this?

Actually, like traditional programming, Vibe Coding has its own "principles." These aren't some mystical knowledge, but rather ways of thinking and working principles verified by countless people. Master these principles, and you can help AI better understand your intentions and create higher quality things.

Today I want to share the 5 most important core principles in Vibe Coding. These come from my own practical experience, and also reference summaries from many community experts. Learn them, and your Vibe Coding level will have a qualitative leap.

![](https://pic.yupi.icu/1/waytovibecoding大.jpeg)




## Principle One: Planning is Everything

This is the most important principle in Vibe Coding, bar none.

Many students, when using AI, start by saying: "Help me make a bookkeeping app."

Then expect AI to give perfect results directly.

But often things don't go as expected — what AI makes either doesn't meet expectations or gives up halfway.

Why?

Because you didn't plan well.

In 2025 Vibe Coding practice, there's a repeatedly verified conclusion: **5 minutes spent on planning saves you 30 minutes of rework.**



### Planning is more important than code

There's a saying in traditional programming: "Sharpen your axe before you cut trees."

In Vibe Coding, this saying is even more important. Because although AI writes code fast, it won't help you think "what to do," only "how to do it."

If you're not clear what you want to do, AI will do it according to its own understanding. The result is: you get a working application, but it's not the one you wanted.

So, before starting to write code, you need to answer these questions:

- What is the core function of this application?
- How will users use it?
- Which functions are essential, which can be added later?
- Are there any special restrictions or requirements?

The answers to these questions are your plan.



### How to plan well?

Many students will say: I don't know how to plan, I'm not a product manager.

Don't worry, AI can help you. You can treat AI as your product manager and complete planning together.

For example, you can start the conversation like this:

"I want to make a Pomodoro timer app, but I haven't figured out exactly what features to include. Can you ask me some questions like a product manager would, to help me clarify my thinking?"

AI will start asking you a series of questions, like:

- Can users customize work and rest durations?
- Should there be a reminder when timing ends? Sound or popup?
- Need to record how many Pomodoros the user completed?

By answering these questions, you'll gradually turn vague ideas into clear requirements. Finally, you can have AI help you organize it into a **Product Requirements Document (PRD)**.

This document is your "project constitution." Afterward, every time you talk with AI, you can paste it to let AI understand your goals.



### Planning determines code shape

In my process of using AI to make projects, I found an interesting point: **AI will prioritize making code runnable over making code structure reasonable.**

Once code runs, AI tends to patch on top of existing code rather than redesign. This is like building a house — if the foundation is crooked, everything built on it will be crooked.

So, planning is your foundation. Before the shit mountain code forms, you need to first determine the overall structure and direction. This avoids later rework.

![](https://pic.yupi.icu/1/shitcode.png)

Precisely because planning is so important, many AI programming tools now provide Plan Mode, helping you generate planning first, manually confirm, then generate code.

For example, Cursor's planning mode:

![Cursor planning mode](https://pic.yupi.icu/1/image-20260104170011408.png)

In Claude Code, you can press `Shift + Tab` twice to enter plan mode.

![](https://pic.yupi.icu/1/image-20260109143426848.png)

In this mode, you can discuss back and forth with Claude until satisfied with its plan. Then switch to auto-accept edit mode, letting Claude complete the task at once without repeatedly confirming each edit.

This "plan first, execute later" approach can greatly improve development efficiency and avoid wasting time going in the wrong direction.



## Principle Two: MVP Thinking

MVP stands for Minimum Viable Product, meaning **Minimum Viable Product**. This is a very important mindset.

Simply put, MVP thinking is: **first make the simplest, but usable version, then gradually improve.**



### Why use MVP thinking?

Many students, when doing projects, always want to get it right in one go. For example, making a bookkeeping app, thinking about needing categories, statistics, charts, export, multiple accounts...恨不得 add all features.

The result?

Get stuck halfway, or what's made is too complex, and you don't even know how to modify it anymore.

MVP thinking helps you avoid this problem. It lets you focus on the most core functions, first do this function well, make it stable, then consider others.

For example, a bookkeeping app, MVP version might only need 3 functions:

1. Record one expense
2. View all expenses
3. Calculate total amount

It's just that simple.

After this version is done and usable, then consider adding categories, adding charts.



### Benefits of MVP thinking

Using MVP thinking has several obvious benefits:

1. Lower difficulty: You don't need to solve all problems at once, only the most important one.

2. Fast validation: You can quickly make a usable version to see if your idea is feasible.

3. Maintain motivation: Seeing your work grow bit by bit gives you more sense of achievement and more willingness to continue.

4. Easy to adjust: If you find the direction is wrong, you can quickly adjust without wasting too much time.



### How to apply MVP thinking?

When talking with AI, you can clearly tell it:

"Let's first make an MVP version that only includes the most core functions. We'll add other functions later."

Then list the 2-3 functions you think are most important. This way AI won't make you a "comprehensive" thing, but focus on doing core functions well.

**Remember, done is better than perfect.**

First make it, then slowly optimize.



## Principle Three: Iteration Over Perfection

This principle is similar to MVP thinking, but with a different focus. MVP thinking is about "what to do," while this principle is about "how to do it."

Simply put: **don't expect to get it right once, approach the goal gradually through multiple iterations.**



### Why is iteration important?

Although AI is powerful, it's not magic. It can't completely understand your requirements at once, nor can it generate perfect code at once.

This is normal — just like chatting with a friend, sometimes you need to explain several times before the other person understands what you mean.

So, the correct approach is: **break big tasks into small steps, proceed step by step.**

For example, if you want to make a login page, don't ask AI to complete all functions at once. You can break it down like this:

1. First make a simple login form (only email and password)
2. Then add form validation (check email format, password length)
3. Then connect backend API
4. Finally add error prompts and loading animation

Each step is very small, easy to complete. Complete one step, test it, no problems then continue to the next.



### Iteration rhythm

A good iteration rhythm is like this:

1. Propose requirement: tell AI what you want to do
2. Generate code: AI gives you code
3. Test run: you run the code to see the effect
4. Find problems: identify what's wrong
5. Adjust optimize: tell AI where the problem is, let it improve

Then repeat this cycle, each cycle bringing your project closer to the goal.



### Don't fear rework

Many students see problems in AI-generated code and think: damn thing, have to start over.

Actually, don't think like that. In Vibe Coding, rework is very normal. Because you're exploring and learning together with AI.

What's important is that each rework should bring gains. You need to understand why the previous plan didn't work, what's better about this plan, so you can continuously improve.

**Iteration isn't wasting time, it's the necessary path to success.**

Like me, after much Vibe Coding, I can actually handle the accuracy of AI-generated code quite well, sometimes able to predict whether AI still needs rework. But anyway, I'm confident AI can definitely help me complete tasks. Just do it!



## Principle Four: Context is King

This is a principle many people easily overlook, but it's extremely important.

What is context?

Simply put, it's the background information AI needs to know. For example, what tech stack your project uses, what functions were done before, what special requirements there are, etc.



### Why is context so important?

**AI has no memory.**

Every time you start a new conversation, it doesn't know what you said before.

If you don't give it enough context, it will do it according to its own understanding, and the result might not match your project at all.

For example, if you only say "help me write a button." AI might write in native HTML, or React, or Vue. Colors, sizes, styles are all decided by itself.

But if you say: "My project uses React and Tailwind CSS, please help me write a blue-toned, rounded, shadowed button." AI can give you a result that meets requirements.

This is the power of context.



### How to provide good context

There are several techniques for providing context:

1) Use project documents: Remember the Product Requirements Document PRD mentioned in principle one?

Every time you start a new conversation, paste it, so AI knows what your project is like.

2) Explain tech stack: Clearly tell AI what framework and library you're using. Like "I'm using Next.js and Supabase."

3) Reference existing code: If you want new functions to be consistent with existing functions, you can tell AI the structure of existing code, like "Please reference my settings page code structure to write this new page."

4) Describe design style: If there are design requirements, must explain clearly. Like "Our design style is minimalist, professional, main color is dark blue." Otherwise AI will likely give you a blue-purple gradient page, you know.



### Context files

Some AI tools support context files. For example, Claude Code can read the `CLAUDE.md` file in the project root directory as a system prompt.

You can write project basic information, tech stack, design specifications in this file. This way every time AI can automatically get this information, you don't need to repeat every time.

This is a very efficient approach, highly recommended.



## Principle Five: Think Like a Product Manager

The last principle, and also the most easily overlooked one.

Many people think using AI to make things is just "tell it what to do, it does what." But actually, your role isn't just someone giving orders, but should be a product manager.



### What is product manager thinking?

What is a product manager's core job?

It's converting user requirements into requirement documents that the development team can understand.

In Vibe Coding, you are the product manager, AI is your development team.

You need to:

- Understand users' (that is, yourself or your target users') real needs
- Break down requirements into clear feature points
- Consider every detail of user experience
- Make trade-offs between functionality, time, and quality



### Focus on user experience

A good product manager doesn't only focus on whether functions are implemented, but also on whether users feel comfortable using them.

For example, a login page, not only needs to be able to log in, but also consider:

- If user enters wrong password, is there a friendly prompt?
- When login button is loading, does it display "Logging in"?
- If network is slow, will user think the page is stuck?

These details, AI won't necessarily proactively consider, need you to proactively raise them.



### Make good trade-offs

Excellent product managers have another important ability: knowing what to do, what not to do.

In Vibe Coding, you also need to make such trade-offs. Not all functions need to be done, not all details need to be perfect. You need to decide priorities based on your goals and time.

For example, if you just want to make a Demo to show friends, then data persistence might not be important, good-looking interface that lets you show off is more important.

But if you want to make a real commercial product, then data security, performance optimization can't be ignored.

These judgments all require you to think like a product manager.



### Communicating with AI

Another important product manager skill is communication. You need to clearly convey your ideas to the development team (that is, AI).

Don't say "make a good-looking button," but say "make a rounded, blue background, white text, darkens on hover button."

Don't say "add a search function," but say "add a search box at the top of the page, after user enters keywords and presses enter, display all articles containing that keyword."

The more specific the requirements, the better AI can understand your intentions.

Programmer friends should understand best, an unclear product manager will make you suffer.

![](https://pic.yupi.icu/1/d2fea61b927529d4c3a4007e7c36379f.jpeg)




## Practical Application of Principles

Let me use a real example to show how these 5 principles work together.

Suppose you want to make a "Daily Quote" small app that displays an inspirational quote every day.



### Apply Principle One: Plan first

You don't directly let AI start writing code, but first plan together with it:

"I want to make a daily quote app. Can you help me clarify requirements?"

AI might ask you:

- Where do quotes come from? Fixed list or from API?
- Can users refresh to get new quotes?
- Need to save user's favorite quotes?

Through these questions, you clarify MVP version functions: **Display one random quote each time opened, user can click button to refresh.**



### Apply Principle Two: MVP thinking

You decide to first make the simplest version:

1. One page
2. Display one quote
3. One "New Quote" button

Other functions (like favorites, sharing) later.



### Apply Principle Three: Iterative development

You break the task into small steps:

1) Create a simple page, display one fixed quote.

Step 2: Add a quote array, randomly select one to display.

3) Add "New Quote" button, after clicking display new quote.

Each step is very small, easy to test and adjust.



### Apply Principle Four: Provide context

In each conversation, you'll explain:

"I'm using React and Tailwind CSS. Design style is minimalist, warm, main color is orange."

This way AI-generated code stays consistent with your project.

Of course, if you use professional AI development tools (like Cursor), the tool will help you maintain context, no need to repeat every conversation.



### Apply Principle Five: Product manager thinking

You consider user experience details, like:

- When clicking button, can we add a fade-in fade-out animation effect? This makes switching more natural.
- If quote is too long, can it automatically adjust font size?

These details make your app more refined.



## In Conclusion

These 5 core principles are the most important experience I summarized in Vibe Coding practice. They aren't some profound skills, but simple but effective ways of thinking.

Let me summarize again:

1. Planning is Everything: Planning is more important than code, think clearly before starting.
2. MVP thinking: First make the simplest usable version, then gradually improve.
3. Iteration over perfection: Approach the goal gradually through multiple small steps.
4. Context is king: Give AI enough background information, only then can it do it right.
5. Think like a product manager: Focus on user experience, make good feature trade-offs.

These principles look simple, but truly mastering them requires continuous practice. I suggest in your next project, consciously apply these principles and see how they work.

Remember, Vibe Coding isn't just letting AI write code, more importantly it's how you guide AI, how you manage the entire development process. Master these principles, and you can go from someone who "can use AI" to someone who "uses AI well."

Next article, I'll explain how to have efficient conversations with AI, that is, "conversation engineering" techniques.

Go for it, you can do it! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
