# Vibe Coding Conversation Engineering Techniques

> The art of iterative dialogue



Hello, I'm Fish Skin.

In the last article, we covered the 5 core principles of Vibe Coding. Today we'll dive deeper into one of the most critical skills — how to have efficient conversations with AI.

Many students, when using AI, treat it like a magic button: enter a sentence, expect it to give a perfect answer directly.

But reality is often that what AI gives is either wrong or not good enough. At this point, everyone complains: AI is too stupid, doesn't understand what I mean at all, is your AI not capable enough?

Actually, the problem isn't that AI is stupid, but that we haven't mastered the skills of conversing with it. Today, I'll teach you how to make AI truly understand your needs through **conversation engineering**.



## I. Conversation Engineering vs Prompt Engineering?

Many friends call communicating with AI "writing prompts" or "prompt engineering." I used to do that too. But nowadays, as AI's understanding of vague instructions gets stronger and stronger, I feel this term isn't comprehensive enough, because it implies a one-way, one-time communication method — you write a perfect prompt, AI gives you a perfect answer.

But in reality, Vibe Coding is more like a conversation. You and AI are working together, exploring together, refining ideas together. This process is **bidirectional, iterative**.

For example, traditional **prompt thinking** is like this:

"Please help me write a responsive navigation bar using React and Tailwind CSS, including Logo, menu items (Home, About, Contact), search box and user avatar, support mobile collapsible menu, colors are dark blue background white text, Logo on left, menu in middle, user info on right..."

You want to say all requirements clearly in one sentence. But often some details are omitted, or not said accurately enough.

While **conversation thinking** is like this:

You: I want to make a navigation bar, can you help me?

AI: Of course. What tech stack do you want to use? Any design requirements?

You: I'm using React and Tailwind CSS. Design-wise, hope it's clean and professional, dark blue background.

AI: Okay. What elements should the navigation bar include?

You: Logo, several menu items, search box and user avatar.

AI: Got it. Need to support mobile?

You: Yes, mobile should collapse into a hamburger menu.

See the difference?

Conversation thinking lets you gradually clarify requirements, rather than needing to think through all details from the start. This is more natural, and easier to get good results.

![](https://pic.yupi.icu/1/promptvschat大.jpeg)



### Benefits of conversation

Using conversation thinking has several obvious benefits:

1. Lower cognitive burden: You don't need to think through all details at once, can think while chatting.

2. Easier to discover problems: AI's questions help you discover places you missed.

3. More accurate results: Through multiple rounds of exchange, AI can more accurately understand your needs.

4. Better learning outcomes: During the conversation process, you'll learn a lot of new knowledge and best practices.



## II. Core Techniques of Iterative Conversation

Below I'll share several of the most important conversation techniques.



### Technique One: From Big to Small, Gradually Refine

Don't get bogged down in details from the start. Start from the whole, then gradually refine.

For example, if you want to make a blog system, don't start by saying: help me write a blog system that supports Markdown, code highlighting, comments, likes, categories, tags, search, RSS subscription.

Instead start like this:

1. I want to make a simple blog system where users can publish and view articles
2. Articles need to support Markdown format
3. Can we add code highlighting functionality
4. I also want a simple comment function

Each step is very small, easy to understand and implement. This way AI won't get confused by complex requirements, and you can adjust direction anytime.



### Technique Two: Specific Rather Than Abstract

AI isn't good at understanding abstract concepts, but very good at handling specific descriptions.

❌ Bad example: make a good-looking button

✅ Good example: make a rounded button, blue background (#3B82F6), white text, padding 12px top/bottom 24px left/right, background becomes dark blue (#2563EB) on mouse hover.

❌ Bad example: add a user-friendly error prompt

✅ Good example: when user enters invalid email format, display red text "Please enter a valid email address" below the input box.

The more specific the description, the more accurately AI can implement your requirements.



### Technique Three: Provide References and Examples

You can help AI understand requirements through text descriptions or image examples.

With text descriptions, you can say things like:

- I want a GitHub-like personal homepage layout: user info card on left, activity timeline on right.
- Button style referencing Stripe's design: clean, modern, with subtle shadows.
- Form validation prompt method referencing Airbnb: real-time validation, error prompts below input box.

AI has seen many websites and applications. The references you provide can help it quickly understand what you want.

An even more direct method is using images. Many current AI large models (like Claude, GPT, Gemini) support image understanding. You can:

- Screenshot the design effect you want, let AI copy it
- Screenshot a bug or error that appeared, let AI see the specific problem
- Screenshot a reference website's layout, let AI imitate it

For example, these prompts:

- Please reference this screenshot's layout to design my page: [upload screenshot]
- My page displays abnormally on mobile, look at this screenshot: [upload screenshot], how should I fix it?

A picture is worth a thousand words. Images let AI more accurately understand your needs, especially for UI design, website development, and bug fixing.



### Technique Four: Ask in Steps

Similar to technique 1. For complex functions, don't ask AI to complete everything at once. Break it into multiple steps, proceed step by step.

For example, implementing user login:

1. First help me create a login form, including email and password input boxes, and a login button.
2. Now add client-side validation to the form: email must match format, password at least 6 characters.
3. When user clicks login button, send POST request to /api/login, carrying email and password.
4. If login succeeds, redirect to home page; if fails, display error message.

After completing each step, you can test it, ensure no problems before continuing. This way even if there are errors, it's easy to locate the problem.



### Technique Five: Use Questions to Guide Thinking

Sometimes, you're not sure how to do something, you can let AI help you analyze.

- I want to add a caching mechanism here, but not sure which solution to use. Can you analyze the pros and cons of Redis and Memcached?
- This page loads a bit slowly, what do you think might be the reasons? Any optimization suggestions?
- I'm considering SSR vs CSR, can you help me analyze the applicability of these two approaches in my project?

Such questions let AI use its knowledge advantage to help you make better decisions.



## III. How to Clearly Describe Requirements?

Describing requirements is the most important part of conversation. Describe well, AI can do it right; describe poorly, and you'll go off in the wrong direction.



### Use a Requirement Description Framework

When describing requirements, you can use a systematic framework to organize your thoughts. Here's a practical framework I recommend:

**Basic Version (5 Elements)**:

1. What (What): What function or component to make?
2. Why (Why): What's the purpose of this function?
3. How (How): What are the technical implementation requirements?
4. Style (Style): What are the appearance and interaction requirements?
5. When/Where (When/Where): In what scenarios is it used?

For example:

- I need a search box (What)
- To let users quickly find articles (Why)
- Implement with React, real-time search while typing (How)
- Style should be clean, with search icon, rounded input box (Style)
- Place on the right side of the navigation bar at the top of the page (Where)

Of course, you don't need to say all five elements every time, but I suggest including at least the first three.

**Advanced Version (6 Elements)**:

If you want more professional output, you can supplement this element:

6) Audience (Audience): Who is this function for? What's their technical level?

For example: "This search function is for ordinary users, should be simple and easy to understand, no advanced filtering needed."

This way AI can adjust implementation approach and interaction design based on the audience.



### Explain Technical Background

If you want AI to help you optimize existing projects, then AI needs to know what technology your project uses, to give appropriate code.

Every time you start a new conversation, I suggest first explaining the technical background, like: My project uses Next.js 15 (App Router), TypeScript, Tailwind CSS and Supabase.

If there are special coding standards, also explain them, like: Our project uses functional components, not class components. All API calls use a custom useFetch hook.

This way AI-generated code stays consistent with your project.

Although many AI programming tools now guide AI to first analyze your existing project code, manually specifying the tech stack can make AI-generated content more accurate.

However, if you're not a programmer, or don't understand these technologies much, then this point can be completely ignored. This is why in the AI era, we still need to learn programming — because people who understand technology can better guide and utilize AI.



### Describe Expected Output

Tell AI what kind of output you expect. For example:

- Please give me complete component code, including TypeScript type definitions
- Only give me core logic, no style code needed
- Please give me a complete example that can run directly
- Please explain step by step how this code works

Clearly specifying output format lets AI better meet your needs, otherwise AI might give you a bunch of messy content.

I've found that stronger AI tends to complicate simple requirements. Like I once encountered asking AI to generate a small project, and it generated 7-8 documents for me, wasting a ton of Tokens.



## IV. Techniques for Follow-up Questions and Correction

AI's first answer is often not perfect enough. At this point, you need to improve results through follow-up questions and correction.



### The Art of Follow-up Questions

If AI's answer isn't detailed enough, don't ask again from scratch, but follow up on details.

❌ Bad follow-up: be more detailed (too vague)

✅ Good follow-up:

- You mentioned using useEffect, can you explain in detail why you need to use it here?
- How's this function's performance? Will there be problems handling large amounts of data?
- You chose to use Map instead of Object, what's the consideration?

Specific follow-ups get more specific answers.



### Let AI Proactively Ask You

Sometimes, you might not know what information to provide. At this point, you can have AI proactively ask you:

```markdown
I want to do [your need]. Please ask me a few questions before answering to understand more details, then give a solution.
```

This way AI will ask you some key questions based on its understanding, like tech stack, usage scenarios, design requirements, etc. By answering these questions, you can describe requirements more clearly, and AI can give a more accurate solution.

This approach is especially suitable when you're not clear enough about requirements, letting AI help you clarify your thinking.



### Correction Methods

If AI misunderstood your meaning, correct it promptly.

- No, that's not what I want. I mean...
- This solution doesn't quite fit my scenario, because... Can you give me another solution?
- You misunderstood my needs. I want A, not B.

Don't be shy about correcting AI, feel free to scold it, humiliate it, even treat it like a bad dog and teach it a lesson. It won't get angry, instead will give better answers based on your feedback.



### Request Explanation

If you don't understand the code or solution AI gave, you can ask it to explain.

- What does this code mean? Can you explain line by line?
- Why write it this way? Are there other ways to write it?
- What are the pros and cons of this solution?

Understanding the principles, you can truly master this knowledge.



## V. How to Guide AI's Output?

Sometimes, AI will give some less-than-ideal solutions. At this point, you need to guide it in the right direction.



### Set Constraints

By setting constraints, let AI think within a specific range.

- Please give me a pure JavaScript implementation that doesn't depend on third-party libraries.
- This function needs to complete within 100ms, please consider performance optimization.
- Code should be as concise as possible, not exceeding 20 lines
- Need to consider edge cases, like empty arrays, null values, etc.

These constraints make AI's output more aligned with your actual needs.



### Request Multiple Solutions

Don't settle for the first solution, but have AI give you multiple choices.

- Please give me 3 different implementation approaches, explaining their pros and cons respectively.
- Is there a simpler solution to this problem?
- Besides the method you just mentioned, are there other solutions?

Multiple solutions let you make wiser choices.

Additionally, when doing big projects, Fish Skin has multiple different AI models or AI products give solutions simultaneously, then manually pick. This method works for friends with some professional knowledge.



### Use Role Playing

Have AI play a specific role, getting more professional advice.

- Please review this code as a senior frontend engineer and give improvement suggestions.
- Assume you're a UX designer, what problems does this interaction flow have?
- As a performance optimization expert, how would you improve this page's load speed?

Role playing stimulates AI's professional knowledge in specific fields.

If you don't know what role to have AI play, you can let AI choose the most suitable expert itself:

```markdown
I want to explore [your problem]. Please first choose the most suitable field expert to think about it, can be a real person or expert. Then answer my question from that expert's perspective.
```

For example, if you want to optimize a product's user experience, you can have AI choose an appropriate UX expert. AI might choose a well-known designer or product manager, then give advice from their perspective. Such answers are often more professional and deeper.



## VI. Conversation Template Library

To improve efficiency, you can prepare some commonly used conversation templates.

1) Template for starting new features

```markdown
I want to develop a new feature: [feature description]. My tech stack is [tech stack]. Please help me:
1) Analyze the core requirements of this feature
2) Suggest a reasonable implementation solution
3) List possible problems
```

2) Template for debugging problems

```markdown
I encountered a problem: [problem description]. Error message is: [error message]. Related code is: [code snippet]. Please help me:
1) Analyze possible causes
2) Give a solution
3) Explain why this problem occurred
```

3) Template for optimizing code

```markdown
This is my code: [code snippet]. Its function is [function description]. Please help me:
1) Find possible performance issues
2) Improve code readability
3) Point out potential bugs
```

4) Template for learning new knowledge

```markdown
I want to learn [technology/concept]. Please:
1) Explain in simple language what it is
2) Give me a practical usage example
3) Tell me when I should use it
```

These templates can help you quickly start conversations, saving time.

More AI prompt templates can be found on Fish Skin's [AI Resource Navigation Website](https://ai.codefather.cn/prompt):

![](https://pic.yupi.icu/1/image-20260104174539349.png)



## VII. Common Conversation Traps

When talking with AI, there are some common errors to avoid.



### Trap 1: Asking Too Much at Once

Don't cram too much content into one question.

❌ Bad example: Help me implement user registration, login, password reset, email verification, permission management, profile editing functions.

This way AI won't know where to start, or will give you a comprehensive but not deep enough answer.

Correct approach: ask only one function at a time, finish one before moving to the next.



### Trap 2: Don't Assume AI Has Memory

AI's memory is limited. Don't assume it remembers what was said long ago.

If you're not sure if AI's memory capacity is enough, and still want to reference previous content, it's best to explain again: Remember the login form we made before? Now I want to build on that...

Or directly paste the relevant code: This is the login form code we wrote before: [code]. Now I want...

However, many AI programming tools will display current memory capacity, helping you control it:

![](https://pic.yupi.icu/1/image-20260104174741309.png)



### Trap 3: Don't Continue Without Testing

Every time AI gives you code, you must test! Don't continue asking for the next function without testing.

If there are problems with the code, promptly feed back to AI. Don't wait until you've done many functions before discovering there are problems with the basic parts.



### Trap 4: Over-reliance

Don't ask AI everything. Some simple problems, checking documentation yourself, searching, or using other tools might be faster.

AI is suitable for:
- Generating code frameworks
- Solving complex problems
- Learning new concepts
- Reviewing and optimizing code

Not suitable for:
- Querying API documentation
- Finding simple syntax errors
- Doing simple calculations (better to use a calculator)

Of course, not saying AI can't do these, just analyze specific scenarios~



## VIII. Practical Case: Complete Conversation Flow

Let me use a real example to demonstrate a complete, recommended conversation flow.

Suppose you're making the "Add Task" function of a todo app.



### Round 1: Clarify Requirements

You: "I want to add a create new task function to my todo app."

AI: "Okay. How do you want users to add tasks? A form, an input box, or some other way?"

You: "Just a simple input box, after user enters task content they press enter to add."

AI: "Got it. Besides content, does the task need other information? Like due date, priority, etc.?"

You: "MVP version won't have these for now, just task content is fine."



### Round 2: Technical Implementation

You: "I'm using React and TypeScript. Please help me write this input box component."

AI: [gives code]

You: "Looks good. But I want the input box at the top of the page, full width, with a light blue border."

AI: [gives improved code]



### Round 3: Add Functionality

You: "Now when user presses enter, the task needs to be added to the task list. My task list is managed with useState."

AI: [gives logic for adding task]

You: "Great. But if the input box is empty, a task shouldn't be added."

AI: [adds validation logic]



### Round 4: Optimize Experience

You: "After adding a task, the input box should automatically clear and keep focus, so users can continuously add multiple tasks."

AI: [adds clear and focus logic]

You: "Perfect! Finally, can we show a brief success message when adding a task?"

AI: [adds notification function]



---



See? Through multiple rounds of conversation, we gradually improved this function. Each step was very small, easy to understand and test.



## IX. Deep Dive into Prompt Engineering

If you want to learn prompt techniques more deeply, here are some recommended resources.



### Learn Cursor's Prompt Design

As one of the most popular AI programming tools, Cursor's prompt design is very worth learning. Cursor's system prompt is over 500 lines long, including role definition, operation constraints, tool usage, and other modules, embodying many prompt engineering best practices.

For example:
- Ensuring AI understands key points through repeated emphasis
- Using negative instructions (NEVER) and positive instructions (ALWAYS) to reinforce constraints
- Providing detailed descriptions and usage examples for each tool
- Unified output format for easier subsequent processing

Fish Skin specially recorded a video, detailed breakdown of Cursor's prompt design: [「Analyzed Cursor's Prompts, Was Absolutely Amazed!」](https://www.bilibili.com/video/BV1bBaBzXEae/)

If you're interested in prompt engineering, or want to develop your own AI applications, highly recommend watching this video.



### Other Learning Resources

- [Alibaba Cloud Bailian Prompt Guide](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide): Systematic prompt writing tutorial
- [Fish Skin's AI Resource Navigation](https://ai.codefather.cn/prompt): Curated prompt template library
- [Fish Skin's AI Knowledge Base](https://github.com/liyupi/ai-guide): Open-source AI learning resources



## In Conclusion

Conversation engineering is one of the most important skills in Vibe Coding. It's not simply "writing prompts," but a continuous, bidirectional, iterative communication process.

Let me summarize the key points:

1. Replace prompt thinking with conversation thinking: Treat communication with AI as cooperation, not giving orders.

2. From big to small, gradually refine: First determine overall direction, then dive into details.

3. Specific rather than abstract: Use clear, specific language to describe your needs.

4. Make good use of follow-ups and correction: Don't settle for the first answer, make it more perfect through follow-up questions.

5. Guide rather than command: Guide AI to give better answers through constraints, role playing, etc.

6. Avoid common traps: Don't ask too much at once, don't assume AI has perfect memory.

Mastering these techniques, you can have efficient conversations with AI, making it truly your capable assistant.

Next article, I'll explain **context engineering**, teaching you how to manage project information so AI always understands your project.

Go for it, future Vibe Coding masters! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
