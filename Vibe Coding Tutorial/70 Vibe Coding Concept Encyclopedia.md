# Vibe Coding Concept Encyclopedia

> Understand all core terms of AI programming in one article



Hello, I'm Programmer Fish Skin, former Tencent full-stack developer, [AI Programming Blogger](https://space.bilibili.com/12890453) with 2 million followers across platforms, and creator of 10+ self-developed products including [AI Navigation](https://ai.codefather.cn) and [Programming Navigation](https://www.codefather.cn).

While learning Vibe Coding, you'll definitely encounter various unfamiliar terms and terminology. For example, what is a Token? What is a context window? What is RAG? These concepts sound sophisticated, but they're actually not difficult to understand.

This article is your **AI Programming Terminology Dictionary**. I'll use the most easy-to-understand language to clarify the most common and important concepts in Vibe Coding. You can bookmark this page and come back to check whenever you encounter a word you don't understand.



## AI Basic Concepts


### Artificial Intelligence (AI)

Artificial Intelligence is technology that enables computers to simulate human intelligence. Simply put, it's making machines think, learn, and solve problems like humans.

In Vibe Coding, AI is your programming assistant. You tell it what to do, and it helps you write code. It's like having a programmer friend available 24/7, ready to help you work anytime.



### Large Language Model (LLM)

A Large Language Model is an AI system capable of understanding and generating human language. ChatGPT, Claude, Gemini, and DeepSeek are all large language models.

Why "Large"? Because these models have an enormous number of parameters, often tens of billions or even trillions. Generally, more parameters mean a smarter model, but also more computational resources consumed.

You can think of a large language model as a super student who has read massive amounts of books and code. It has seen countless programming examples, so it can help you write code, explain code, and fix bugs.

![](https://pic.yupi.icu/1/1745384872015-f84a47fc-0925-4797-9dfc-e4dfae01a3fa.png)



### Model Parameters

Parameters are the "knowledge points" the model learns during training, stored in the model as numbers. More parameters usually means the model can remember more knowledge and is generally smarter.

For example:

- GPT-4 has approximately 1.8 trillion parameters
- Claude 3.5 Sonnet's parameter count is undisclosed, but estimated to be in the hundreds of billions
- DeepSeek-V3 has 671 billion parameters

Parameter count affects model capability and running cost. Generally, models with more parameters are more expensive but produce better results.



### Training and Inference

Training is the process of letting AI models learn knowledge from massive amounts of data. This process requires enormous computational resources and time, usually done by AI companies. You don't need to train models yourself.

Inference is the process of using learned knowledge to answer questions and generate content after the model has finished learning. When you chat with ChatGPT, you're using inference.

To use an analogy: training is like a student going to school to study, inference is like a student taking an exam to answer questions. Our daily use of AI tools all uses inference capabilities.



### Fine-tuning

Fine-tuning is continuing to train an existing model with data from a specific domain to make it perform better in that field.

For example, you could fine-tune a model with massive medical materials to make it a medical expert. Or fine-tune with your company's codebase to make it better understand your project's style.

For ordinary users, fine-tuning is relatively expensive and generally not necessary to do yourself. Using existing models directly is sufficient.



## Token and Billing


### Token

Token is the basic unit AI models use to process text. You can simply understand it as "word chunks."

In English, one Token is approximately one word or part of a word. In Chinese, one Chinese character is usually 1-2 Tokens.

Why is Token important? Because AI services usually charge by Token. Both the text you input and the text AI outputs consume Tokens. The more Tokens you use, the more money you spend.

For example:

- "Hello World" is approximately 2 Tokens
- "你好世界" is approximately 4-6 Tokens

![](https://pic.yupi.icu/1/image-20260112112612434.png)



### Input Token and Output Token

AI services usually calculate input and output Tokens separately:

- Input Token: The content you send to AI (prompts, code, files, etc.)
- Output Token: The content AI returns to you (responses, generated code, etc.)

Generally, output Token is more expensive than input Token, because generating content consumes more computing power than understanding content.

Money-saving tip: Write clear, concise prompts so AI understands your needs in one go, reducing back-and-forth conversation.



### Context Window

Context Window refers to the maximum amount of content an AI model can "remember" at one time, measured in Tokens.

Different models have different context window sizes:

- GPT-4o: 128K Token (approximately 100,000 Chinese characters)
- Claude 3.5 Sonnet: 200K Token (approximately 150,000 Chinese characters)
- Gemini 2.0 Pro: 2M Token (approximately 1.5 million Chinese characters)

The larger the context window, the more code AI can process and the longer conversation history it can remember. If your project has a lot of code, choosing a model with a large context window is more appropriate.

But note that the larger the context window, the more Tokens consumed per request, and the higher the cost.



## Prompt Related


### Prompt

A Prompt is the instruction or question you give to AI. In Vibe Coding, a prompt is your requirement described in natural language.

The quality of your prompt directly determines the quality of AI output. A good prompt should:

- Be specific and clear, not vague
- Include necessary background information
- Explain the expected output format

For example, "make a website" is a vague prompt, while "use React to make an accounting website with three features: add expenses, view list, and show total statistics, use blue color scheme" is a good prompt.

In AI conversations, messages usually have three roles:

- System Prompt: Sets AI's role and behavior rules, invisible to users
- User Prompt: Messages you send to AI
- Assistant Prompt: Messages AI replies to you

Understanding these 3 roles helps you construct conversations better. For example, when debugging, you can simulate previous conversation history in your prompt to help AI better understand the context.



### System Prompt

A System Prompt is an instruction set before the conversation begins, used to define AI's role, behavior, and constraints.

For example, you can set a system prompt: "You are a senior React development expert, please answer questions using a concise and clear code style."

The system prompt remains effective throughout the conversation and is an important way to customize AI behavior.

![](https://pic.yupi.icu/1/1745462990451-6f2b5727-d47b-436c-9da2-50dac64fb790.png)



### Prompt Engineering

Prompt Engineering is the technology of designing and optimizing prompts, aimed at making AI better understand your intent and generate results that better match expectations.

This is one of the core skills of Vibe Coding. Good prompt engineers can use fewer conversation rounds to make AI generate higher quality code.



### Zero-shot Prompting

Zero-shot prompting is giving AI a task directly without providing any examples.

For example: "Please translate this English text to Chinese."

AI will complete the task based on its training knowledge. For simple tasks, zero-shot prompting is usually sufficient.



### Few-shot Prompting

Few-shot prompting is providing several examples in your prompt to let AI learn the format or style you want.

For example:

```
Please translate according to the following format:
English: Hello → Chinese: 你好
English: Thank you → Chinese: 谢谢
English: Good morning → Chinese:
```

By providing examples, AI can more accurately understand your needs and output more consistent results.



### Chain-of-Thought Prompting

Chain-of-thought prompting is having AI think through problems step by step rather than giving answers directly. This is particularly effective for complex reasoning tasks.

You can add "please think step by step" or "Let's think step by step" to your prompt, and AI will show its reasoning process, usually getting more accurate answers.

In programming, chain-of-thought prompting helps AI better understand complex requirements and generate more reasonable code structures.

![](https://pic.yupi.icu/1/chainofthought.png)



### Markdown Language

Markdown is a lightweight text markup language that uses simple symbols to represent format. For example, using `#` for headings, `**text**` for bold, `-` for lists.

In Vibe Coding, Markdown is very important because:

- AI-generated responses are usually in Markdown format
- Project documentation (like README) is written in Markdown
- Rule files are also in Markdown format

Learning Markdown lets you better communicate with AI and write more standardized project documentation.



## AI Programming Patterns


### Vibe Coding

Vibe Coding is a concept proposed by computer scientist Andrej Karpathy in February 2025. It describes a brand new programming method: through natural language conversation with AI, let AI help you write code. You only need to describe requirements, test results, and guide direction.

The core philosophy of Vibe Coding is: you don't need to master programming syntax, only need to clearly express your ideas. AI is responsible for turning your ideas into runnable code.

It's like ordering food delivery: you tell the delivery platform what you want to eat, the restaurant makes it and delivers it to your hands. You don't need to know how to cook, but you need to know what you want to eat.



### Agentic Coding

Agentic Coding means letting AI work like an autonomous "Agent" that can plan tasks, execute operations, and verify results on its own, rather than just passively answering questions.

In Cursor's Agent mode, AI can:

- Automatically read and analyze multiple files
- Plan implementation approaches
- Execute code modifications
- Run tests to verify
- Automatically fix problems

This is more powerful than traditional Q&A AI because it can autonomously complete complex multi-step tasks.

![](https://pic.yupi.icu/1/agent-in-cursor.png)



### Multi-Agent Collaboration

Multi-Agent refers to multiple AI agents working together to complete complex tasks.

For example, one agent is responsible for designing architecture, one for writing frontend code, one for writing backend code, one for code review. They collaborate like a team.

In recent years, multi-agent systems have become an important trend in AI programming, able to handle more complex projects.

![](https://pic.yupi.icu/1/image-20260112112834637.png)



### Agent Orchestration

Orchestration is the process of coordinating and managing multiple AI agents or AI tasks, ensuring they work in the correct order and manner.

Like a band conductor, the orchestrator decides which agent does what at what time, how to pass information, and how to summarize results.

![](https://pic.yupi.icu/1/image-20260112112854174.png)



### Agent Loop

Agent Loop is the core working mechanism of AI agents, describing how agents continuously run to complete tasks.

A typical Agent Loop includes:

1. Perceive: Get current environment information (read files, check errors, etc.)
2. Think: Analyze the situation, decide next action
3. Act: Execute specific operations (write code, run commands, etc.)
4. Observe: Check the results of actions
5. Loop: Decide whether to continue based on results

This cycle continues until the task is complete or a termination condition is reached. Understanding Agent Loop helps you better use tools like Cursor Agent.



### ReAct (Reasoning and Acting)

ReAct is a technical framework that lets AI agents alternate between reasoning and acting.

Traditional AI either only thinks without acting, or only acts without thinking. ReAct enables AI to:

- First reason: Think about the current situation, make a plan
- Then act: Execute specific operations
- Observe results: See how the action worked
- Continue reasoning: Adjust strategy based on results

This "think - act - observe" cycle lets AI more reliably complete complex tasks and is one of the core technologies of modern AI programming tools.

![](https://pic.yupi.icu/1/react-agent.png)



### Tool Use

Tool Use (Function Calling) is technology that enables AI to use external tools and functions. AI itself can only generate text, but through tool use, it can:

- Read and write files
- Execute command line commands
- Search web pages
- Call APIs
- Operate databases

![](https://pic.yupi.icu/1/1746590338968-0240c12b-2956-47f4-b8ff-5b5f831221f6.png)

In Vibe Coding, tool use transforms AI from "only able to speak" to "able to act." For example, Cursor's Agent mode uses tool use to modify your code files.



### Agent Skills

Agent Skills is an open standard launched by Anthropic in October 2025, used to extend AI agents with specific domain professional capabilities.

Simply put, a Skill is a folder containing a `SKILL.md` file that can hold instruction documentation, script code, reference materials, etc. When AI encounters related tasks, it automatically loads the corresponding Skill to enhance its abilities.

![](https://pic.yupi.icu/1/agent%2520skills.jpeg)

You can think of Skills as "new employee onboarding guides" for AI. For example:

- A PDF processing Skill that teaches AI how to fill out PDF forms
- A project deployment Skill containing your team's unique deployment process and scripts
- A code review Skill that defines your project's code standards and checklist

The core design of Skills is **progressive disclosure**: AI only loads relevant content when needed, without stuffing all information into context at once, saving both Tokens and maintaining flexibility.

![](https://pic.yupi.icu/1/agent%20skills%20bundling.jpeg)



### A2A (Agent-to-Agent)

A2A (Agent-to-Agent) refers to protocols or methods for AI agents to communicate and collaborate with each other. It's a foundational technology for multi-agent systems.

Just as people need language to communicate, AI agents also need standardized ways to exchange information, assign tasks, and report results.

A2A protocols enable different AI agents to form teams and work together to complete complex tasks.

![](https://pic.yupi.icu/1/a2a-agent.png)



## Context Management


### Context

Context is all the information AI can reference when answering questions, including:

- Current conversation history
- Code files you have open
- Project structure and configuration
- Reference materials you provide

The richer and more relevant the context, the more AI-generated code meets your needs. This is like handing off work to a new colleague - the more background information you give, the faster they get up to speed.



### Context Engineering

Context Engineering is the technology of strategically managing and optimizing the context information provided to AI.

The core goal is **giving AI just the right amount of information**. Not too little (causing AI to not understand the situation) and not too much (causing information overload and increased costs).

Good context engineering includes:

- Selecting the most relevant files
- Providing necessary background explanations
- Using rule files to define project standards
- Promptly cleaning up irrelevant conversation history



### Rules File

A Rules File is a configuration file placed in the project root directory, used to tell AI about your project standards, technology stack, code style, and other information.

In Cursor, this file is called `.cursorrules`; in Claude Code, this file is called `CLAUDE.md`. (Note: As tool versions update, these file names and standards may change)

With a rules file, AI refers to these rules every time it generates code, producing code that better matches your project's style, saving the trouble of repeatedly emphasizing them.



### RAG (Retrieval-Augmented Generation)

RAG is a technology that enables AI to consult external knowledge bases.

Ordinary AI can only rely on knowledge learned during training, while RAG lets AI first retrieve relevant information from your documents, codebase, or knowledge base when answering questions, then generate responses based on this information.

This is particularly useful for Vibe Coding because AI can reference existing code in your project to generate new code with consistent style.

![](https://pic.yupi.icu/1/1745810809620-15c36bc0-5130-47fc-aaca-7d2a6ce6e3ce.png)



### Vector Database

A Vector Database is a database specifically designed to store and query "vectors" (a numerical representation form). In the AI field, it's often used to store semantic representations of text.

After you store code or documents in a vector database, AI can quickly find semantically similar content, even if the search term and original text aren't identical.

For example, when you search "user login," it can find a function named "handleAuth" because they're semantically related.

![](https://pic.yupi.icu/1/1745813546910-9b39355a-85ab-4673-b52b-7f11349a55d7.jpeg)



### Embedding

Embedding is the process of converting text, code, and other content into numerical vectors. These vectors can capture the semantic information of the content.

In vector space, semantically similar content will be closer together. This is why vector databases can perform semantic search.

You don't need to deeply understand the technical details of embedding, just know that it's a foundational technology for RAG and code semantic search.

![](https://pic.yupi.icu/1/1745812543781-8ef377d0-2dac-4d17-a504-35de13fbaad0.png)



### MCP (Model Context Protocol)

MCP (Model Context Protocol) is an open standard launched by Anthropic in late 2024, used to securely connect AI models to external data sources and tools.

You can think of MCP as the "USB interface" of the AI world. With MCP, AI can conveniently read your files, access databases, and call various tools without each tool needing to develop a separate interface.

![](https://pic.yupi.icu/1/1746710765234-c974bda8-666e-45b3-adc4-ace97cbb8c0a.png)

In Vibe Coding, MCP enables AI to more conveniently obtain project context, improving the accuracy of code generation.

![](https://pic.yupi.icu/1/1746677838632-9278e62b-c850-4d3c-a835-297ccbe2061a.png)



## AI Output Related


### AI Hallucination

AI Hallucination refers to AI fabricating non-existent content, such as fictional APIs, incorrect function usage, or non-existent libraries.

This is an inherent problem with large language models because they generate content based on probability and sometimes "hallucinate" things that don't exist.

How to handle hallucinations:

- Ask AI to provide documentation links for verification
- Check official documentation yourself
- Try a different model
- Start a new conversation and re-describe the problem



### Temperature

Temperature is a parameter that controls the randomness of AI output, typically ranging from 0-2.

- Low temperature (like 0.1): Output is more deterministic and conservative, suitable for writing code
- High temperature (like 1.0): Output is more random and creative, suitable for brainstorming

In programming scenarios, usually use lower temperature to make AI generate more stable, predictable code.



### Streaming Output

Streaming Output means AI displays content to you in real-time as it generates, rather than waiting for complete generation before displaying.

This is like watching a live broadcast rather than a recording - you can see AI's thinking process in real-time, and if you notice the direction is wrong, you can interrupt in time.

Most AI programming tools support streaming output, making the interaction experience smoother.



## Development Tool Concepts


### IDE (Integrated Development Environment)

An IDE is comprehensive software programmers use to write code, usually including a code editor, debugger, terminal, and other tools.

VS Code is currently the most popular IDE. Cursor and Windsurf are both AI code editors developed based on VS Code, inheriting VS Code's functionality while adding AI capabilities.

![](https://pic.yupi.icu/1/image-20260112113710320.png)



### Code Editor

A code editor is a tool for writing and modifying code. It usually provides features like syntax highlighting, code completion, and error hints to help you write code more efficiently.

Common code editors include Sublime Text, etc. The difference from IDEs is that they're relatively lightweight and start quickly, suitable for quickly editing individual files; while IDEs have more comprehensive functionality, integrating debuggers, terminals, version control, and other tools, suitable for large project development.

In the Vibe Coding era, code editors integrate AI capabilities and can automatically generate code, explain code, and fix errors based on your prompts. For example, although Cursor is powerful like an IDE, its core is still an AI-enhanced code editor.



### No-Code Platform

A No-Code Platform is a platform where you can create applications without writing code. You build applications by dragging and dropping components and configuring parameters through a visual interface.

In the AI era, platforms like Bolt.new, Lovable, v0.dev, and Baidu Miaoda combine no-code and AI - you describe requirements in natural language, and the platform automatically generates complete applications.

No-code platforms are particularly suitable for beginners with absolutely no programming experience, or scenarios where you want to quickly create prototypes.

![](https://pic.yupi.icu/1/image-20260104141512389.png)



### Code Completion

Code Completion is a feature where AI predicts what code you're going to write next and automatically provides suggestions.

When you write code, AI infers your intent based on context and provides code snippets for you to choose from. Press Tab to accept the suggestion, greatly improving coding speed.

GitHub Copilot is currently the most well-known AI code completion tool.



### Code Review

Code Review is the process of checking code quality, finding problems, and suggesting improvements.

In traditional development, this is usually done by colleagues or supervisors. In Vibe Coding, you can have AI help you review code. It will point out potential bugs, security issues, performance problems, and provide modification suggestions.

![](https://pic.yupi.icu/1/image-20260112114023226.png)

But note that AI review cannot completely replace human review, especially for important production code.



### Linter

A Linter is a tool that automatically checks code for problems, able to find syntax errors, style issues, potential bugs, etc.

Common linters include ESLint (JavaScript), Pylint (Python), etc. They're like strict grammar teachers, helping you maintain code standards.

In Vibe Coding, linters help you quickly discover problems in AI-generated code.



### Debugging

Debugging is the process of finding and fixing errors in code. When code execution results don't match expectations, you need to debug to locate the problem.

Common debugging methods include:

- Setting breakpoints and executing code step by step
- Checking variable values
- Reading error messages and stack traces
- Adding log output

![](https://pic.yupi.icu/1/image-20251027214825243.png)

In Vibe Coding, you can send error messages to AI and let it help you analyze the cause and provide a fix.



## Project Management Concepts


### MVP (Minimum Viable Product)

MVP is the product version that satisfies core requirements with the minimum functionality.

The benefits of building an MVP:

- Quickly verify if an idea is feasible
- Avoid wasting time on unnecessary features
- Get user feedback faster

For example, when building an accounting app, the MVP version might only have two features: record expenses and view list. Other advanced features can be added later.



### Iterative Development

Iterative development is dividing a large project into multiple small cycles, with each cycle completing part of the functionality.

Each iteration cycle includes: Plan => Develop => Test => Release => Feedback => Improve.

This method is particularly suitable for Vibe Coding because you can have AI first implement core functionality, test it, then gradually add new features.



### Refactoring

Refactoring is the process of improving code structure and quality without changing functionality.

The purpose of refactoring is to make code clearer, more maintainable, and more efficient. Common refactoring includes:

- Extracting repeated code into functions
- Improving variable and function naming
- Simplifying complex logic
- Splitting overly long files

In Vibe Coding, you can have AI help you refactor code, but do it in small steps and test after each refactoring.



### Technical Debt

Technical Debt refers to temporary solutions adopted to quickly complete functionality that will need time to fix and improve in the future.

Like credit card debt, although overdrawing is convenient now, you'll have to pay it back later with interest.

In Vibe Coding, code generated by AI may not be the optimal solution. Accumulating too much technical debt makes the project increasingly difficult to maintain. Regular refactoring is the way to repay technical debt and prevent a pile of messy code.

![](https://pic.yupi.icu/1/v2-806707f0f72072f1db481c237fc035ea_1440w-20260112114757928.png)



### Version Control

Version control is a system that records code change history, allowing you to track each modification, compare different versions, and roll back to previous states.

Git is the most popular version control tool, and GitHub is the most popular code hosting platform.

In Vibe Coding, version control is particularly important. Because AI may generate problematic code, with version control, you can always roll back to a previous normal version.

![](https://pic.yupi.icu/1/image-20260112114940228.png)



### Deployment

Deployment is the process of publishing a developed application to a server so users can access and use it.

Common deployment platforms:

- Vercel: Suitable for frontend and full-stack applications
- Netlify: Suitable for static websites and frontend applications
- Railway, Render: Suitable for backend services

Many no-code platforms (like Bolt.new) support one-click deployment - just click a button to go live.



## Frontend and Backend Concepts


### Frontend

Frontend is the part users can directly see and interact with, including web interfaces, buttons, forms, animations, etc.

Frontend technology stack usually includes:

- HTML: Page structure
- CSS: Styles and layout
- JavaScript: Interaction logic
- React/Vue/Next.js: Modern frontend frameworks

In Vibe Coding, frontend is what AI is best at generating because the results can be directly seen, making verification and adjustment convenient.



### Backend

Backend is the part users can't see, responsible for handling business logic, data storage, user authentication, etc.

Backend technology stack usually includes:

- Node.js/Python/Java: Programming languages
- Express/FastAPI/Spring: Web frameworks
- MySQL/PostgreSQL/MongoDB: Databases

Backend is more complex than frontend and needs to consider security, performance, data consistency, and other issues. Backend code generated by AI needs more careful review.



### Full-stack

Full-stack refers to a complete application that includes both frontend and backend. A full-stack developer is a programmer who can handle both frontend and backend work.

In Vibe Coding, tools like Bolt.new can generate full-stack applications in one go, writing both frontend and backend code for you.

Want to further understand what full-stack programmers are and how to become one? Check out Fish Skin's article: [What is a Full-stack Programmer?](https://www.bilibili.com/opus/534338036646820466)



### API

API (Application Programming Interface) is the interface for communication between different programs.

You can think of an API as a restaurant menu. The menu tells you what dishes are available, how to order, and what you'll get after ordering. You don't need to know how the kitchen cooks, just order from the menu.

In web development, frontend communicates with backend through APIs to get data or submit operations.

![](https://pic.yupi.icu/1/1766718929375-35cd24d6-077e-4a5e-8cbb-7725edf8098f-20260112120508019.png)

Want to further understand API interfaces and standard API interface design specifications? Watch [Fish Skin's API Animation Explainer Video](https://www.bilibili.com/video/BV1WFBXBmExs).



### Database

A database is a system for storing and managing data. User information, content, settings, etc. in applications are all stored in databases.

Common database types:

- Relational databases (MySQL, PostgreSQL): Data stored in table format
- Document databases (MongoDB): Data stored as JSON documents
- Key-value databases (Redis): Suitable for caching and fast lookups

![](https://pic.yupi.icu/1/1764309581505-2ff17977-695f-4d7c-a779-b5d35ad99d6b.png)

![](https://pic.yupi.icu/1/1764309606178-1af81d82-b320-4bed-9c97-5dfe3847d8d3.png)

In Vibe Coding, you can use BaaS services like Supabase and Firebase without building and managing databases yourself.

Want to systematically learn database knowledge? Check out Fish Skin's database introduction tutorial: [Database Introduction Tutorial](https://www.bilibili.com/video/BV1iJSLBbEyD/)



### BaaS (Backend as a Service)

BaaS is a cloud service that provides ready-made backend functionality, including databases, user authentication, file storage, etc.

Common BaaS services:

- Supabase: Open-source Firebase alternative
- Firebase: Google's BaaS platform
- PlanetScale: Managed MySQL service

Using BaaS, you don't need to write backend code or manage servers yourself, greatly accelerating development. Particularly suitable for Vibe Coding scenarios.



## In Conclusion

This article covers the most common concepts and terminology in Vibe Coding. Of course, new concepts in AI and programming are constantly emerging, and this dictionary will continue to update.

You don't need to remember all concepts at once. When you encounter a word you don't understand, come back to check or ask AI. As you continuously practice Vibe Coding, these concepts will naturally become familiar.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
