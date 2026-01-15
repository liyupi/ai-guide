# Vibe Coding Project Development Process

> Complete Vibe Coding workflow from idea to product



Hello, I'm Fish Skin.

In the quick start phase, we've already made a simple web application. That project was very simple and could be built just by talking with AI. But now, let's solve a more practical problem: how do you build a complete, commercial-grade project?

Many students, when starting to use AI for projects, make the same mistake: after opening an AI programming tool, they immediately start chatting with AI and have it generate code. For small projects, this is fine. But if you want to build a complete commercial-grade project, this will cause problems. At first it might go smoothly, but soon you'll find that the AI-generated code becomes increasingly messy, completely not what you wanted. Changing back and forth, your left brain fighting your right brain, finally you have to scrap it and start over, wasting a lot of time.

Why is this? Because you skipped the most important step — **planning**.

In the Vibe Coding era, although AI can help you write code, good planning is still the key to project success. You could even say, planning is more important than before.

Below, I'll share a proven 5-step development process to help you avoid these pitfalls.



## Why Do We Need a Standard Process?

In traditional programming, if your project planning isn't clear, at worst the code quality you write isn't high, but at least you know what you're writing.

But in Vibe Coding, the situation is completely different. If your project planning isn't clear, AI will "freestyle" and generate a bunch of code you don't understand and don't need.

AI isn't magic — it's just a very powerful executor. You tell it what to do, and it does what you tell it. If you yourself don't know what you want to do, AI naturally can't help you build an ideal product.

So, a clear development process can help you:

1. Clarify project goals and requirements
2. Let AI understand your intentions
3. Avoid the project getting out of control
4. Improve development efficiency
5. Build truly useful products



## The Complete 5-Step Workflow

This process is something I've summarized from practice, also referencing the experience of many excellent developers.

It includes 5 steps:

1. Requirements Research (Research)
2. Product Requirements Document (PRD)
3. Technical Design Document (Tech Design)
4. AI Agent Instructions (AGENTS.md)
5. Implementation and Iteration (Build)

Sounds complicated? Don't worry, I'll "spoon-feed" you in the simplest way.

![](https://pic.yupi.icu/1/vibecodingworkflow%E5%A4%A7.jpeg)



## Step 1: Requirements Research (Research)

After understanding the overall process, let's start from the first step and explain in detail how to do each step.

Before starting work, first clarify: what exactly do I want to build? Why build it? Has anyone built something similar?

Many students skip this step and go straight to writing requirements documents. But my experience is, spending 30 minutes doing research can avoid many detours.

How to do it specifically?

1) Clarify Your Goal

First ask yourself a few questions: What problem do I want to solve? Is this problem really worth solving? What do I hope the result looks like?

For example, if you want to build a bookkeeping application, you need to think clearly: is it for yourself or for others? What types of accounts mainly need to be recorded? What core features are needed?



2) Research Similar Products

Go see if there are similar products on the market, how do they do it? What are the pros and cons?

You can search for related apps or websites, look at others' open source projects, or directly ask AI: "What are some good bookkeeping applications? What are their characteristics?"

This step is very important, can help you avoid reinventing the wheel, and can also give you inspiration and reference.



3) Record Your Findings

Record your ideas and research findings in a simple document, like `RESEARCH.md`. This document doesn't need to be very formal — just like writing a diary, recording your thoughts and findings is enough.

For example, suppose you want to build a bookkeeping application. You first research several bookkeeping apps on the market and find that their functions are all too complex, you only need a simple tool. Then you record your ideas, `RESEARCH.md` might look like this:

```markdown
# Bookkeeping Application Requirements Research

## Goal
Build a simple and easy-to-use personal bookkeeping application to help yourself develop the bookkeeping habit.

## Research Findings
- Bookkeeping apps on the market all have too complex functions
- I only need to quickly record income and expenses
- Best to be able to see monthly statistics

## Core Requirements
1. Quickly add income/expense records
2. View records by date
3. View monthly statistics
4. Local data storage
```



## Step 2: Product Requirements Document (PRD)

After completing requirements research, you should have a clear understanding of what you want to build. Next, we need to organize these ideas into a formal document. Clarify what features to build, what features not to build.

This is the most important step in the entire process. A good PRD can let AI accurately understand your intentions and generate high-quality code.



### How to Write a High-Quality PRD?

My suggestion is, first write a simple requirements description yourself, then let AI help you expand it into a complete PRD.

For example, you can first write:

```
I want to build a bookkeeping application that can quickly record income/expenses and view monthly statistics.
Keep it simple and easy to use, no complex features.
```

Then send this paragraph to an AI large model, like Gemini or DeepSeek:

```
Please help me expand this requirement into a complete Product Requirements Document (PRD),
including:
1. Product overview and target users
2. Detailed feature list
3. Feature priorities (MVP and future versions)
4. Interface design requirements
5. Tech stack recommendations
6. Non-functional requirements (performance, security, etc.)
```

AI will help you generate a structured PRD, then you can modify and improve it based on your needs.



### What Should a PRD Include?

A complete PRD usually includes:

- Product Overview (brief introduction of what the product is)
- Target Users (who will use this product)
- Core Features (list all features to build)
- Feature Priorities (what must be done, what can be added later)
- Interface Design (briefly describe what the interface should look like)
- Tech Stack Recommendations
- Code Style and Architecture Patterns
- Constraints and Edge Cases



For example:

```markdown
# Bookkeeping App PRD

## Product Overview
A simple personal bookkeeping application to help users quickly record daily income and expenses.

## Target Users
Individual users who need bookkeeping but don't want to use complex applications.

## Core Features

### Must Do (MVP)
1. Add income/expense record
   - Input amount
   - Select type (income/expense)
   - Select category (dining, transport, salary, etc.)
   - Add note (optional)
   - Select date

2. View record list
   - Display in reverse chronological order
   - Show amount, type, category, note
   - Can delete records

3. Monthly statistics
   - Show total income for the month
   - Show total expenses for the month
   - Show monthly balance

### Can Do Later
- Data export
- Chart display
- Budget settings
- Multi-account management

## Interface Design
- Home page: Display record list and add button
- Add page: Form input
- Statistics page: Display monthly data
```



## Step 3: Technical Design Document (Tech Design)

With a clear PRD, we know what to build.

Next step is to determine what technology to use to implement these features, and roughly the technical architecture.

Create a `TECH_DESIGN.md` file, including:

- Tech Stack Selection (what to use for frontend, what for backend, what for database)
- Project Structure (how to organize code)
- Data Models (what data needs to be stored)
- Key Technical Points (what technical difficulties need attention)

Continuing with the bookkeeping application example. Based on the requirements in the PRD, you decide to use React for frontend because its ecosystem is mature and AI support is good. LocalStorage is enough for data storage since it's a personal tool and doesn't need a backend. The technical design document might look like this:

```markdown
# Bookkeeping App Technical Design

## Tech Stack
- Frontend: React + TypeScript + Vite
- Styling: Tailwind CSS
- Data Storage: LocalStorage
- Deployment: Vercel

## Project Structure

src/
  components/     # Components
  pages/          # Pages
  hooks/          # Custom Hooks
  utils/          # Utility functions
  types/          # Type definitions

## Data Models

### Transaction (transaction record)
- id: string
- amount: number
- type: 'income' | 'expense'
- category: string
- note: string
- date: string

## Key Technical Points
1. Use LocalStorage to store data
2. Use React Hooks to manage state
3. Use date library to handle dates (date-fns)
```
If you're not familiar with technology selection, you can ask AI: "I want to build a bookkeeping application, what tech stack should I use?"

AI will recommend appropriate technologies.



## Step 4: AI Agent Instructions (AGENTS.md)

PRD and technical design are both ready. Now we need to create a specialized instruction file for AI, telling AI what rules to follow in this project.

You can name this file whatever you like, like `AI_RULES.md`, `INSTRUCTIONS.md`, etc. But I recommend using the name `AGENTS.md` because this is an emerging community standard.

[AGENTS.md](https://agents.md/) is a standardized file format used to guide AI programming tools on how to work. It's like a "work manual" for AI. This standard is jointly promoted by OpenAI, Anthropic, Google and other companies, and currently over 80,000 open source projects are using it. Mainstream AI programming tools like Cursor, Windsurf, Claude Code, Gemini CLI, GitHub Copilot etc. all support automatically reading AGENTS.md files.

![](https://pic.yupi.icu/1/image-20260109161639565.png)

So what should AGENTS.md contain?

Generally it includes project overview, development standards, testing requirements, code style, precautions, etc.

Continuing with the bookkeeping application example. Based on the previous PRD and technical design, you can create an AGENTS.md file like this:

```markdown
# Bookkeeping App AI Development Instructions

## Project Overview
This is a simple personal bookkeeping application, developed using React + TypeScript.

## Development Standards
- Use TypeScript, ensure type safety
- Components use functional components + Hooks
- Use Tailwind CSS for styling
- All data stored in LocalStorage

## Code Style
- Use ESLint and Prettier
- Component names use PascalCase
- Function names use camelCase
- Constants use UPPER_SNAKE_CASE

## Testing Requirements
- Manually test after completing each feature
- Ensure data is correctly stored and retrieved
- Test various edge cases

## Precautions
- Keep code concise, avoid over-engineering
- Prioritize implementing core features
- Ensure mobile compatibility
```

With this file, AI knows what rules to follow in this project, and the generated code will be more standardized and consistent.



## Step 5: Implementation and Iteration (Build)

The first 4 steps are all preparation. Now we can finally start writing code!

But not all at once — iterate in small steps.



### Stepwise Iteration Strategy

For complex projects, trying to do everything at once is unrealistic. I recommend adopting a 3-step strategy:

#### 1. Generate Basic Framework

First have AI generate the basic project framework, temporarily ignoring whether features work well, just ensure the project can run.

```
Please according to the requirements in PRD.md, TECH_DESIGN.md and AGENTS.md,
initialize the project and create the basic project structure, including:
1. Install necessary dependencies
2. Create directory structure
3. Configure development environment
4. Create basic routing and page framework
Ensure the project can start normally.
```

For students with programming foundation, there's actually a simpler method. You can use scaffolding or project templates to quickly generate the basic framework.

Scaffolding is like an automation tool that helps you generate the basic structure and configuration files of a project, like `create-react-app`, `create-vite`, etc.

Project templates are pre-configured project examples that you can directly copy and use.

Using these tools, you can set up the basic framework in a few minutes without starting from scratch.



#### 2. Gradually Implement Core Features

After the framework is set up, you can start implementing specific features. The key to this step is **first get the core business flow working, implement core features**, rather than pursuing perfection from the start. I suggest breaking the project into multiple small features and implementing them one by one.

For example, the bookkeeping application can be broken down like this:

1. Implement data model and storage
2. Implement add record feature
3. Implement record list display
4. Implement delete feature
5. Implement monthly statistics

For each feature, you can talk to AI like this:

```
I want to implement the add record feature. Please according to the requirements in PRD.md and TECH_DESIGN.md,
create an AddTransaction component including form input and submit functionality.
```

After completing each feature, test it: does the feature work normally? Are there any bugs? Does the interface match expectations?

If there are problems, continue talking with AI and have it modify.



#### 3. Optimize Implementation Details

After core features are all implemented, you can polish the details. While **ensuring you don't affect functionality**, optimize performance, improve user experience, beautify the interface, etc.

After polishing the details, your MVP minimum viable product is complete. Afterwards, you can extend more features based on user feedback and your own ideas.

Additionally, after getting the core features working, I strongly recommend using Git to manage your code. Commit once after completing each feature, so even if problems occur later, you can quickly roll back.

If you don't know Git yet, you can check out [Fish Skin's Git Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866), you'll pick it up quickly.



### Key Techniques to Avoid AI Getting Out of Control

In actual development, you might encounter these problems:

- AI outputs completely irrelevant content
- After implementing a new feature, the original feature doesn't work
- Fixing one bug introduces 3 more bugs

These problems are common, but they all have solutions.

#### 1. Project Modularization

Since AI's context is limited, as project information continues to grow, it may forget previous information, leading to generated code errors. So we need to isolate project functions as much as possible, dividing a large project into multiple small modules.

For example, developing an e-commerce system, you can separate the product management module. When needing AI to generate code for the add product feature, you only need to provide the product table's field design, the business logic rules for adding products, without needing to provide payment settlement, user membership and other unrelated functions as context to AI.



#### 2. Limit Modification Scope

AI-generated code isn't that controllable — often when modifying feature A, it also incidentally modifies feature B. This problem is easily solved — just limit the modification scope in the prompt:

```
Only modify the components/AddTransaction.tsx file:
1. Add form validation functionality
2. Keep existing styles and layout
3. Don't modify other files
```



#### 3. Abstraction and Reuse

Suppose we want AI to generate 2 pages with exactly the same layout. Sometimes it's very rigid — after generating page A, it copies page A's code to generate page B. This is very unfavorable for large project maintenance. Later if AI modifies page A, it might forget to modify page B. So we need to proactively tell AI:

```
Please help me abstract this page into a reusable component,
so other pages can use it by passing different parameters.
```

This can also reduce the total code amount of the project, lighten the burden on AI's contextual memory, and make generation results more accurate.



#### 4. Version Control

I strongly recommend using the Git version control tool. Commit a version after correctly generating each feature. After AI generates new code each time, manually compare the changed files. If problems occur, you can also quickly restore to the previous version, preventing code loss.

```
After completing each feature, commit code:
git add .
git commit -m "Implement add record feature"
```

Cursor comes with Git comparison functionality, making it very convenient to view code changes.



#### 5. Manual Control

Sometimes AI gets stuck in a loop due to lack of key contextual information or its own insufficient capability. For example, making changes back and forth always shows the same error, or it keeps doing useless work. At this point, manual intervention becomes necessary.

You can try manually specifying context, changing the prompt to describe the problem from a different angle, clearing conversation history and starting over, or even manually modifying parts of the code to give AI the correct direction.

At this time, the benefits of learning programming show. If you have some programming foundation, you can better control and intervene in Vibe Coding. You can understand the code AI generates, know where problems occurred, can manually correct key parts, and guide AI in the right direction. This is also why I suggest everyone learn some basic programming knowledge while learning Vibe Coding.



#### 6. Multi-AI Collaboration

Different AI large models are good at different tasks. If a single large model cannot complete the work normally, you can use other large models to generate "methods and instructions for teaching AI to do things."

For example, if you have problems with code generated by GPT in Cursor, you can:
1. Copy the code and error information to Claude or Gemini
2. Have it analyze the problem and give modification suggestions
3. Tell the modification suggestions to GPT and have it modify the code

This multi-model collaboration approach can greatly increase the possibility of solving problems.



## Counter-Example - Unclear Requirements Cause Project Failure

In the project practice section of this Vibe Coding tutorial, I'll share many successful project cases that you can choose to learn based on your interest. Here I only give one counter-example to show you what problems occur when you don't follow the process.

Xiao Aba wants to build a todo application. He directly opens an AI programming tool and enters:

```
Help me build a todo application
```

AI generates an application that looks pretty good. But Xiao Aba quickly discovers problems: no category feature, no priority settings, doesn't like the interface style.

So he continues the conversation:

```
Add category feature
```

AI adds categories, but breaks the original layout. Xiao Aba says:

```
Fix the layout issue
```

AI fixes the layout but introduces new bugs. Just changing back and forth like this, finally the code becomes a mess, and Xiao Aba has to give up on this project.

Where did the problem occur?

First, there were no clear requirements from the start, leading AI to generate code according to its own understanding. Second, each modification was "treating the head when the head hurts, treating the foot when the foot hurts," without overall planning. Finally, without document records, AI had no idea of the project's overall design.

If Xiao Aba had followed the 5-step process from the start, writing clear PRD and technical design, these problems wouldn't have occurred.



## Practical Techniques - Make AI-Generated Code More Accurate

After mastering the complete development process, I'll share some practical techniques to make AI-generated code more accurate and more in line with your expectations. These techniques are what I've summarized from practice and are very practical.

More experience and techniques can be found in the [Experience & Techniques] section of this Vibe Coding tutorial. Here I only list a few I think are crucial.



### 1. Optimize Your Prompt

The quality of your prompt directly determines the accuracy of AI-generated code. A good prompt should include three elements: clarify AI's role, provide specific detail requirements, break down complex tasks.

For example, you can first tell AI its role: "You are an experienced frontend development engineer, good at using React and TypeScript to develop modern web applications."

This way AI knows what perspective to work from, then you provide specific detail requirements.

❌ Bad prompt:
```
Help me make a button
```

✅ Good prompt:
```
Create a primary action button component:
- Use Tailwind CSS
- Support three styles: primary, secondary, danger
- Support loading state (show loading animation)
- Support disabled state
- Has feedback animation when clicked
```



Also learn to break down complex tasks. Don't have AI complete complex tasks all at once, but break them into multiple small tasks:

❌ Bad prompt:
```
Implement user management functionality
```

✅ Good prompt:
```
Step 1: Create user data model and type definitions
Step 2: Implement user registration interface
Step 3: Implement user login interface
Step 4: Implement user info query interface

Now please complete step 1 first.
```

If there's reference code or design, you can also provide it to AI:

```markdown
Refer to this login page's design style: [screenshot or link], create a registration page and keep the style consistent.
```



### 2. Pay Attention to Operating System Differences

AI is more familiar with Linux or Mac system terminal commands. If you use Windows system, you have two choices: install WSL (Windows Subsystem for Linux) to use Linux environment for development, or clearly tell AI you're using Windows system.

Clarify in AGENTS.md:

```markdown
## Development Environment
- Operating System: Windows
- Terminal: PowerShell
- Please use Windows-compatible commands
```

Or clarify during conversation:

```
I'm using Windows system, please provide Windows-compatible commands.
```



### 3. Handling AI Getting Stuck in Loops

Sometimes AI gets stuck in a loop, repeatedly doing the same thing, or can't solve a certain problem. At this point you can try several methods.

1) Clear context. In Cursor, clear the current conversation and start over, but first save important information.



2) Ask questions from a different angle, don't repeat the same question.

For example, the original question is very simple:
```
Why doesn't the login feature work?
```

Change the angle:
```
Please check each step of the login process:
1. Did the frontend correctly send the request?
2. Did the backend receive the request?
3. Is the database query correct?
4. Is the returned data format correct?

Please troubleshoot step by step and tell me which step has the problem.
```



3) Provide more context. AI might be missing key information, so you might as well provide it with related files, error messages, logs, etc.:

```
I encountered a login problem, related information as follows:

1. Frontend code: [paste code]
2. Backend code: [paste code]
3. Error message: [paste error]
4. Network request: [paste request and response]

Please help me analyze where the problem is.
```

If you really can't solve it, you can seek other AI's help. Copy the code and problem to Claude or ChatGPT, have them analyze — they might give different solutions.



### 4. Let AI Help You Optimize Prompts

If you're not sure whether your prompt is good enough, you can have AI help you optimize. This is a very practical technique:

```
I want AI to help me implement user login functionality.
My current prompt is: "Implement login feature"
Please help me optimize this prompt to make it more detailed and accurate,
so AI can generate high-quality code.
```

AI will give you an optimized prompt with more details and requirements.



### 5. Leverage AI's Code Review Capability

After completing features, you can have AI help you review code:

```
Please review my login feature code, check:
1. Are there security issues (like plaintext password transmission)
2. Are there performance issues
3. Does the code follow best practices
4. Are there potential bugs
5. Can user experience be improved

Please give specific improvement suggestions.
```

AI's reviews can often discover problems you didn't notice. For core features, you can also have multiple different AI large models review simultaneously for cross-validation.



## In Conclusion

Reading here, you might think: this process seems a bit complex, is it really necessary?

My answer is: absolutely necessary!

I've personally used Vibe Coding to build at least 30+ projects, from simple tools to complex full-stack applications. In my practice, those projects that had good planning from the start all went very smoothly in development and successfully launched. Most of those "do as you think" projects were abandoned halfway. Planning is Everything — this is the first core principle of Vibe Coding.

Although it takes time to write documents in the early stage, later development will be very smooth, and the quality of AI-generated code will also be higher.

And good planning won't limit your creativity, instead it will make you more free. Because you know what you're doing and know where to go with each step.

Of course, this process isn't set in stone. As your experience increases, you'll find a rhythm that suits you. But at the start, I strongly recommend following this process to develop good habits.

Finally, let me emphasize these key points again: planning is more important than code, documents are AI's compass, small step iteration without losing control, modularization is key for large projects, version control is your regret medicine.

Now, you've mastered the complete project development process. In the next article, I'll take you through using this process to build 5 practical personal tool projects, letting you experience the power of this process.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
