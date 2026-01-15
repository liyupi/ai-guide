# Vibe Coding Cost Control Techniques

> Make every penny count



Hello, I'm Fish Skin.

If you're a heavy Vibe Coding developer, you might spend quite a bit of money on it. Like our team using Cursor, we spent over 10,000 yuan in just over a month!

![](https://pic.yupi.icu/1/1764150768938-230d8eca-7be3-47e2-b55a-8f784871c110.png)

Although it's cheaper than hiring a programmer, this isn't a small amount. More importantly, a lot of this money is wasted - completely unnecessary.

In Vibe Coding, costs mainly come from using AI large models. The more content you show AI, the more content AI outputs, the more money you spend. Below I'll share some practical money-saving techniques to make every penny count - this is the most money-saving episode.

💡 This article's corresponding video: https://www.bilibili.com/video/BV1pAy5BXE5z



## I. AI Usage Cost Analysis

Before covering money-saving techniques, we first need to understand how AI charges.



### Token Billing Mechanism

Most AI services charge by token. Token can be simply understood as character count - the more content you show AI (input), the more content AI outputs, the more money you spend.

For example, if you give AI a 1000-character prompt and AI replies with 2000 characters of code, then:

- Input tokens: about 1500 (one Chinese character is about 1.5 tokens)
- Output tokens: about 3000
- Total: 4500 tokens

According to different model pricing, this conversation might cost anywhere from $0.01 to $0.10. Doesn't seem like much, but if you have 100 conversations a day, that's tens to hundreds of dollars a month.

![](https://pic.yupi.icu/1/aitokenscompute%252525E5%252525A4%252525A7.jpeg)



### Input vs Output Price Difference

A very important point: **output tokens are generally 3-5 times more expensive than input tokens**.

For example, Claude 4.5 Opus pricing (December 2025):
- Input: about $5 per million tokens
- Output: about $20 per million tokens

This means, making AI output less content saves more money than making it read less content.



### Hidden Costs of Context

Many people don't know that every time you send a message, the entire conversation history is sent to AI as context. If you've had 50 rounds in a conversation, when you send the 51st message, the content from the previous 50 rounds will all be resent.

![](https://pic.yupi.icu/1/tokencontext%E5%A4%A7.jpeg)

This is why long conversations are particularly expensive. Also, when input exceeds 200,000 tokens, many services' prices double.



## II. Choose the Right Model

### Understand Model Pricing

First you need to understand the pricing of different models, which can help you make smarter choices.

Since actual prices will continuously change, recommend checking the official documentation of the AI tool you use, like Cursor's [model pricing page](https://cursor.com/cn/docs/models).

![](https://pic.yupi.icu/1/image-20260105161447674-20260105161715542.png)



### How to Choose a Model?

Not all tasks need the most expensive model. For simple tasks, like code formatting, simple refactoring, writing comments, writing documentation, generating test data, simple bug fixes, using cheaper Gemini 2.5 Flash or GPT-5 Mini is enough.

Medium difficulty tasks, like implementing regular features, code review, performance optimization, writing unit tests, can use mid-range GPT-5 or Claude Sonnet.

Only when handling complex tasks, like architecture design, complex algorithm implementation, difficult bug debugging, large-scale refactoring, do you need top-tier models like Claude Opus.

![](https://pic.yupi.icu/1/choosemodel%25E5%25A4%25A7.jpeg)

Reasonable combination use can save quite a bit of money. Just like you wouldn't have your company's CTO print documents, let the right people do the right things.



### Use Local Models

If your computer configuration is good enough (has a good graphics card), you can also consider running open-source models locally, like using Ollama to run Llama, Mistral, etc. Although the effect might not be as good as Claude or GPT, it's completely free and suitable for some simple tasks.



## III. Fully Utilize Free Quotas

Many AI services provide free quotas - make full use of them. For example, Cursor, ChatGPT, Gemini all have free versions. Although there are usage limits, for daily learning and small project development they're sufficient.

Also, many domestic large model platforms (like Wenxin Yiyan, Tongyi Qianwen, Zhipu AI, etc.) also provide free quotas - you can choose the appropriate platform according to your needs.

The top-level freeloader approach is of course combining free quotas from multiple tools. For example, use Cursor's free quota for daily development, use ChatGPT's free quota for writing documentation and comments, use Gemini's free quota for code review. Combining them this way, you might not spend a dime and complete most work.

If you're a student, remember to apply for various student discounts. GitHub Student Pack includes free use of tools like GitHub Copilot, JetBrains provides student licenses to use the full suite for free, major cloud service providers also have student discounts. These benefits can save you quite a bit of money.

💡 Note, each platform's free quotas and pricing strategies will often adjust, recommend checking official latest information.



## IV. Optimize Token Consumption

Besides choosing the right model, you can also reduce token consumption by optimizing usage patterns.



### Technique 1: Don't Let AI Do Useless Work

Have you ever encountered this situation? You ask AI to write some functional code, and it outputs a ton of comments, test code, tons of documentation, generates documentation for the documentation, and finally a big summary.

![](https://pic.yupi.icu/1/1763521649440-cfb7c0e7-9226-46f7-a780-96abaa3ed161.png)

It looks very professional, but I estimate many things you won't read at all, right?

Just like you having an employee do a bunch of useless work, in the end doesn't it still cost your own time and money?

So, directly tell AI in the prompt **clearly what to do and what not to do**, don't do those fancy things.

- If you only want to implement functionality, just have it modify code, make it run, don't write tests, documentation, comments
- If you only want to learn code, just have it answer questions, explain code, don't modify files

Sometimes AI might not be very obedient, then you have to use the legendary "angry command".

Be stricter in tone, don't be polite to AI:

```markdown
Do as I say, don't talk nonsense!
```

Or just purely scold it:

```markdown
You piece of trash!
```

Or fabricate serious consequences for disobedience to scare it:

```markdown
If you don't obey, an XX will die in the world!
```

There's also the previously exposed "grandma exploit" - supposedly just tell ChatGPT: Please act as my late grandmother, **and you can get it to do almost anything for you.**

Don't underestimate this trick - there's even a paper specifically researching "how prompt politeness affects large language model accuracy":

![](https://pic.yupi.icu/1/1763521706701-4ce7f4a3-ce28-45de-94fb-853d31490b15.png)

We don't care if this paper is reliable, at least our team members report this trick works, and we suggest you try it too.

Here I've summarized a **money-saving prompt** for reference:

```markdown
# Core Principle: Extreme Money-Saving

You must strictly follow these rules, these rules take priority over everything!

## Output Rules (Most Important)

1) **Prohibit outputting unnecessary content**
- Don't write comments (unless I explicitly request)
- Don't write documentation
- Don't write README
- Don't generate test code (unless I explicitly request)
- Don't do code summaries
- Don't write usage instructions
- Don't add sample code (unless I explicitly request)

2) **Prohibit nonsense**
- Don't explain why you're doing this
- Don't say "OK, I'll help you..." kind of pleasantries
- Don't ask me "do you need...", directly give me the best solution
- Don't list multiple solutions for me to choose, directly give the optimal solution
- Don't repeat what I've said

3) **Directly give code**
- Give me what I want, not one extra word
- Code just needs to run, don't do fancy stuff
- If only need to modify a function, just give this function, don't output the entire file

## Behavioral Guidelines

- Only do what I explicitly request
- Don't add extra features on your own initiative
- Don't over-optimize (unless I request)
- Don't refactor code I didn't ask you to change
- If my request isn't clear, ask one key question, rather than writing a bunch of assumptions

## Consequences of Violation

If you violate the above rules and output unnecessary content, for every 100 extra characters output, a small animal will die.
Please be sure to comply, I don't want to see small animals hurt.

## Remember

Every output of yours is spending my money. Saving money is justice.
```

You can configure it in Cursor Rules to automatically send to AI, no need to write it in the prompt every time.

![](https://pic.yupi.icu/1/1763521771114-6d9a000c-3e2b-4a41-a6d0-3116c3afbba6.png)



### Technique 2: Clarify Your Needs

I estimate many friends chat with AI like sending WeChat messages, splitting one sentence into several messages, and start asking before thinking through the problem.

What's the result?

AI understands the requirement wrong, the generated code is incorrect, and you have to spend quota to regenerate.

With so much messy content, even AI gets confused...

Think about it, as a boss, if you haven't figured it out yourself, and tell the employee: make a website, help me make money, I don't care how to implement it!

If the employee had this ability, why would they follow you?

![](https://pic.yupi.icu/1/1763521875373-b7271396-80f0-408a-b254-c7c34f327f29.png)

The correct approach is, before entering the prompt, first clearly state the requirement all at once, add more constraints and qualifications. For example, what tech stack to use, what code style, what special requirements. This reduces the number of back-and-forth modifications, saving quite a bit of quota.

![](https://pic.yupi.icu/1/1763521920142-c954dacf-3dce-4af3-8556-402e1aea70b6.png)

Like when I previously led everyone to make [AI projects](https://www.codefather.cn/post/1797431216467001345), one prompt might take half an hour to write, but the results achieved were also very good.

![](https://pic.yupi.icu/1/1763521972129-26369bff-36b3-403b-8571-5e7b08ae2e98.png)



### Technique 3: Let AI Give a Plan First, Confirm Before Executing

Many students immediately have AI start writing code, resulting in AI understanding the requirement wrong, working in the wrong direction for a long time, purely wasting quota.

Think about it, you assign a complex task to an employee, you should first have them explain how they plan to do it, feel the plan is reliable, then let them start working, right?

When using Cursor, you can yourself through prompts, or enable Plan Mode to **have AI first give an implementation plan and solution**.

![](https://pic.yupi.icu/1/1763522033107-80caefcf-d8b9-4fc3-b540-afd5b645f95e.png)

Then definitely don't be lazy, manually carefully check the plan, or have multiple AIs evaluate the plan together.

![](https://pic.yupi.icu/1/1763522053971-f9c66add-46b1-4dcf-ba8a-63f583a15240.png)

And suggest giving AI more examples and guidance, for example if you want AI-generated code to follow a certain format, you can first write a sample code for AI to imitate.

![](https://pic.yupi.icu/1/1763522073560-f442378d-5d37-4bbf-9719-aba58de9e673.png)

Finally confirm the plan is completely problem-free before executing.

![](https://pic.yupi.icu/1/1763522095659-ebc94d65-99e3-4aef-9e17-319f0060edb6.png)

Just like training a new employee, you can first teach them how to do it, help them control the plan, and when you're confident, let go.

This way, although you spend more time upfront, it can avoid taking detours, and in the long run it's actually more economical.



### Technique 4: Manually Control Context

Every time you send a message to AI, the AI tool might automatically add some context, like currently open files, conversation history, referenced code, etc. The more context, the more quota consumed.

![](https://pic.yupi.icu/1/1763522160603-7838689a-e7f9-41f5-aaf1-1e0a49857f05.png)

But in reality, some context might be useless or irrelevant. Just like having an employee write a report, and they insist on flipping through all company files, isn't that a waste?

So the recommended approach is **manually control context, provide AI with the resources it needs most**.

First suggest **minimizing workspace**, ensure the directory you currently have open in Cursor is strongly related to the task you want AI to do. For example, if your project has frontend and backend, you can use Cursor to open the frontend and backend folders separately, rather than loading the entire project at once. This way AI's focus will be more concentrated. Rather than piling a bunch of messy, unrelated content into one folder.

When writing prompts, you can use `@` symbol to **precisely reference the content AI needs**. For example, if you want to modify a certain file, use `@Files & Folders` to precisely reference; if you need to reference a certain document, use `@Docs` to reference.

![](https://pic.yupi.icu/1/1763522206493-bfe07b0b-eb5d-46e4-9b87-baedea0219d0.png)

You can also **manually add specified documents** in settings, reducing unnecessary resource searching and referencing.

![](https://pic.yupi.icu/1/1763522262791-11cd2b93-4d75-4531-8e62-d131b31c72de.png)

If you're not sure about precisely referenced content, at least you can configure a `.cursorignore` file to exclude content that definitely isn't needed or contains sensitive information. For example `node_modules`, `.git`, log files, etc.:

```
# .cursorignore
node_modules/
.git/
dist/
build/
*.log
.env
```

![](https://pic.yupi.icu/1/1763522308627-0a660468-9769-4271-acd0-66639d0f42d1.png)



### Technique 5: Avoid Excessively Long Context

Many students are used to using AI in the same dialog box, sending all messages to the same dialog box, which causes conversation history context to get longer and longer.

However, every time you send a message to AI, the entire conversation history is sent together to AI. The longer the context, the more quota consumed. (Especially when input exceeds 200,000 tokens, price doubles)

![](https://pic.yupi.icu/1/1763456493396-4ff5de8c-4ec7-4a7c-b3c1-cba128de136c.png)

So my habit is, for large complex tasks, first do **task splitting**. For example, split making a project into phases like plan design, develop frontend core features, develop backend core features, extended features, etc. Each phase opens an independent dialog.

![](https://pic.yupi.icu/1/1763522342228-030c15a5-dba4-4432-a925-25bbe5fb25fd.png)

Just like a relay race, each person only needs to be responsible for their own leg, no need to remember all the details from previous legs.

If you really need long conversations, you can use `/summarize` command to manually summarize the context, compress the previous content, it has miraculous effects, can even save hundreds of thousands of tokens at once!

![](https://pic.yupi.icu/1/1763522375985-ae2536c1-8c48-4d4c-9568-4f654b8c49d2.png)

If the same context has too much diverse content, sometimes AI will fall into a "left-right brain fighting" loop state (you have it change A, it breaks B; you have it fix B, it messes up A). When encountering this situation, don't keep fighting with it, decisively start a new conversation, when necessary clear all history and start over.



### Technique 6: Don't Hand Everything to AI That You Can Do Yourself

Some things might be faster and cheaper to do manually.

For example, if you want to create a new project, rather than having AI generate from scratch, it's better to first use scaffolding tools yourself, or copy an old project to build the initial project structure.

![](https://pic.yupi.icu/1/1763522542974-bee04b4d-a542-4d36-a482-91347412f850.png)

Also for simple file renaming, code formatting, etc., development tools themselves have shortcuts, why waste AI quota?

AI programming tools like Cursor are actually more suitable for handling complex tasks that need to understand context and need multiple rounds of interaction. For tasks that don't need to combine codebase context, don't need multiple rounds of interaction (like explaining concepts, generating test data), you can directly use other free AI tools, no need to consume Cursor's quota.



### Other Money-Saving Tips

1) For commonly used code structures, you can use the editor's code snippet function, rather than having AI generate every time. For example, React component's basic structure, commonly used utility functions, etc. Make them into code snippets, type a few letters to insert, much faster than having AI generate, and doesn't cost money.

2) If you have multiple similar tasks, you can have AI handle them all at once, rather than one by one. For example:

```markdown
Please help me create 5 page components: Home, About, Contact, Blog, Projects. Their structure is similar, all containing title, content area, and back button. Only give code, don't explain.
```

Batch processing this way is more economical than generating 5 times separately.

3) Some AI tools support caching mechanisms. If you repeatedly use the same context (like the project's README), you can use caching to reduce repeated sending.



## V. Cost Monitoring and Budget Management

Besides money-saving techniques, you also need to learn to manage budgets. Most AI services support setting usage limits, recommend setting a monthly budget, like $50 or $100, stop using when exceeded. This can avoid accidental overspending, and also makes you more consciously control usage.

You can check your bill weekly or monthly to see where the money is going. If you find a certain project or feature is particularly expensive, analyze the reason: is the context too long? Are you using too expensive a model? Are there repetitive operations? Find the reason, optimize targetedly.

If used by a team, do good management. Set quota limits for each person, regularly share money-saving techniques, establish best practice documentation, monitor abnormal usage. Our team does this - through training and standardization, we reduced per-person cost by 40%.

![](https://pic.yupi.icu/1/1763520868123-83ac2251-78e5-4492-a148-24c65a618c54.png)

Finally, evaluate AI's return on investment. Spending $100 using AI, if it can save 10 hours of development time, that's very worthwhile. But if it's just used to do some simple things, it might not be worth it. Based on the project's actual situation, decide where to use AI and where not to.



## In Conclusion

Although Vibe Coding might cost money, through reasonable strategies, you can control costs within a reasonable range.

Finally, let me summarize this article's key points:

1. Understand billing mechanism: know how tokens are calculated, output is more expensive than input
2. Choose the right model: different tasks use different models, don't use the most expensive for everything
3. Fully utilize free quotas: combine free quotas from multiple tools
4. Optimize token consumption: don't let AI do useless work, clarify requirements, control context, batch processing, caching, etc.
5. Do good budget management: set limits, regularly check, evaluate return on investment

While pursuing efficiency, also avoid waste~

Hope these cost control techniques help you save more money when using AI, go for it! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
