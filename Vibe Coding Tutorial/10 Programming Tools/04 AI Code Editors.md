# AI Code Editors

> A more professional and powerful Vibe Coding development method



Hello, I'm Programmer Fish Skin.

In previous articles, we learned how to use zero-code platforms and AI agent platforms. If you've already made a few projects with these tools, you might start feeling some limitations:

- I want to modify a specific file, but zero-code platforms aren't flexible enough...
- The project is getting larger, managing code in the browser is a bit tough...
- I want to learn a more professional development method, but don't want to give up AI's help...

If you have these thoughts, then congratulations — it's time to upgrade to AI code editors!

AI code editors combine the powerful functionality of traditional code editors with AI's intelligent assistance, allowing you to develop projects more flexibly and professionally. In this article, I'll explain in detail the mainstream AI code editor Cursor and share more AI code editors worth attention.



## I. What is an AI Code Editor?

Before understanding AI code editors, let's first understand a basic concept: What is a code editor?

Simply put, **a code editor is a tool for programmers to write code**, just like Word is a tool for writing documents. Common code editors include VS Code, Sublime Text, Notepad++, etc.

There's also a related concept called **IDE (Integrated Development Environment)**, which is more powerful than a code editor — not only can you write code, but it also integrates a complete set of development tools like debugging, compiling, and version control. Common IDEs include JetBrains' IntelliJ IDEA, PyCharm, WebStorm, etc.

However, in actual use, the line between code editors and IDEs is becoming increasingly blurred. For example, although VS Code is called an editor, by installing plugins, its functionality is already similar to an IDE. So you don't need to worry too much about the difference between these two concepts — just know they're both tools for writing code.

Now let's clarify 2 questions:

- What's the difference between AI code editors and zero-code platforms?
- What's the difference between AI code editors and traditional code editors?



### AI Code Editors vs Zero-Code Platforms

Zero-code platforms are used in browsers — you have AI generate entire applications through conversation, especially suitable for rapidly making prototypes and simple projects. AI code editors need to be downloaded and installed on your computer, can precisely control every file and every line of code, and have a complete development toolchain (like code debugging, version control, etc.), more suitable for complex projects and professional development.

To use an analogy: zero-code platforms are like ordering at a restaurant — the chef cooks and serves it; AI code editors are like cooking in your own kitchen with an intelligent assistant helping you.



### AI Code Editors vs Traditional Code Editors

So what's the difference between AI code editors and traditional code editors (like VS Code, JetBrains, Sublime Text)?

I believe the biggest difference is **deep AI integration**.

Traditional code editors are just tools for writing code — you need to think clearly about how to write each line of code yourself. AI code editors have built-in powerful AI assistants that can help you generate code, explain code, modify code, and even automatically execute multi-file tasks.

Specifically, AI code editors have capabilities that traditional editors don't:

- Generate code by describing requirements in natural language
- AI can understand the context of the entire project
- Can automatically modify multiple files
- Can automatically execute commands (like installing dependencies)
- Has intelligent code completion (much smarter than traditional completion)

Simply put, traditional code editors are "tools for you to write code yourself," AI code editors are "tools for AI to help you write code." In actual use, the efficiency difference could be more than 10 times.

If you have some programming foundation, getting started with AI code editors will be very fast.



## II. Cursor - The Hottest AI Code Editor

Cursor is currently the hottest AI code editor, called "VS Code of the AI era." Because it's based on VS Code, it retains all of VS Code's advantages while adding powerful AI functionality.

![](https://pic.yupi.icu/1/image-20260107133923123.png)

Cursor's core advantages:

1. Multiple AI functions: Tab code completion, Agent, Chat, inline editing, etc.
2. Multi-model support: Can use Claude, GPT, Gemini, Grok and other models, plus Auto automatic selection
3. Context-aware: AI can understand the entire project's code, supports up to 1M Token context (Max mode)
4. Mature ecosystem: Based on VS Code, supports all VS Code plugins



### Cursor's Core AI Functions

Cursor's most powerful aspect is that it provides multiple AI functions suitable for different scenarios.



#### 1. Tab Code Completion

This is the most basic function, similar to GitHub Copilot. When you write code, AI automatically predicts what you want to write, and pressing Tab accepts the suggestion.

![](https://pic.yupi.icu/1/image-20260107134002087.png)

This function is especially suitable for writing repetitive code, completing function implementations, and rapidly generating boilerplate code. The advantage is fast speed without interrupting your train of thought; the disadvantage is it can only complete, not make major modifications.



#### 2. Agent

This is Cursor 2.0's most powerful function, and the mode closest to an AI programmer. In this mode, AI can simultaneously modify multiple files, automatically create new files, execute commands (like installing dependencies), understand the entire project structure, and even use a browser for testing.

You can use it to add new features (that require modifying multiple files), refactor code, fix complex bugs, build project frameworks, etc. — it can handle various complex tasks.

Cursor also launched the self-developed **Composer model**, an AI model specifically optimized for software engineering, with generation speed 4 times faster than similar models.

For example:
```
Please add user authentication functionality including:
- Login page
- Registration page
- Authentication middleware
- User database model
```

Agent will automatically analyze the project, install necessary dependency packages, create needed files, modify related code, until the task is complete.

![](https://pic.yupi.icu/1/image-20260107134332952.png)



#### 3. Chat and Inline Editing

Chat is the most commonly used function. You can select a piece of code, then tell AI in natural language what you want to do. You can use it to explain what code does, modify a function, fix bugs, optimize performance, etc.

![](https://pic.yupi.icu/1/image-20260107134511105.png)

Inline editing lets you modify directly in code — press `Cmd/Ctrl + K` to quickly call it, and AI will generate or modify code at the current location.

![](https://pic.yupi.icu/1/image-20260107134532921.png)

Some examples: you can select a piece of code, then say to AI:
- What does this function do?
- Help me optimize performance
- Add error handling



### How to Use Cursor?

Let me demonstrate Cursor's usage process with a complete example.

For instance, I want to make a simulated electronic blackboard where I can draw whatever I want and export as an image.

Wielding the brush freely, so satisfying!

1) First, go to [Cursor official website](https://cursor.com) and download the version suitable for your system (Windows/Mac/Linux are all supported).

2) Create an empty folder to store the entire project code. Recommend using English names, like `yupi-drawboard`.

Then open Cursor and open the folder you just created.

![](https://pic.yupi.icu/1/image-20260107142103143.png)

3) Open the Agent panel, select Agent mode and a large model, then enter a prompt to describe your requirements:

```
Help me develop a simulated electronic blackboard where users can draw and export as an image
```

![](https://pic.yupi.icu/1/image-20260107142244095.png)

Next, have a cup of coffee and wait for AI to generate the code. It will automatically create multiple files, and you can see its work progress in the Agent panel.

![](https://pic.yupi.icu/1/image-20260107142422465.png)

4) After a few minutes, AI has generated the complete code. You can choose to accept all or reject all, or choose which code to accept yourself:

![](https://pic.yupi.icu/1/image-20260107142737589.png)

5) Since the requirements are relatively simple, directly open the `index.html` webpage file in a browser and see the running effect.

![](https://pic.yupi.icu/1/image-20260107142906255.png)

Not bad effect, right? Guess what I wrote~

6) If you need to modify details or fix bugs, just talk to AI directly.

Of course, if you have some programming foundation, you can select a piece of code yourself and press `Cmd/Ctrl + K` to use inline editing.

![](https://pic.yupi.icu/1/image-20260107142631274.png)

When you write new code yourself, AI will automatically suggest (Tab completion function) — just press Tab to accept the suggestion.

This is Cursor's basic usage. Additionally, Cursor supports more capabilities like web search, browser usage, voice input, MCP plugins, etc., which you can slowly explore later.



### Cursor's Pros and Cons

Cursor is the most comprehensive AI code editor I've used so far — its several AI modes cover all scenarios from code completion to agents.

Because it's based on VS Code, all VS Code plugins, themes, and shortcuts work, and if you've used VS Code before, getting started will be very fast.

Plus, you can freely switch between mainstream new models like Claude, GPT, Gemini, and can use your own large models and API Keys.

![](https://pic.yupi.icu/1/1764145641557-9b0b777f-f9ca-4cb4-8566-437dbd4b2cbb.png)

Additionally, Cursor has a large user base, so it's relatively easy to find solutions to problems. There are also the most tutorials and videos online. I myself also keep following Cursor's development trends and have made many tutorials.

However, Cursor's biggest drawback is still the price — the advanced plan itself is relatively expensive, and each plan also has usage limits.

When you exceed the monthly included usage, you can choose to add on-demand usage (billed at API rates) or upgrade to a higher tier. Different models have different API costs, and your model choice will affect usage consumption speed.

For detailed pricing information and usage calculations, I recommend checking [Cursor's official pricing documentation](https://cursor.com/cn/docs/account/pricing), which has the latest and most accurate information.

If you're seriously learning Vibe Coding, I recommend subscribing to the Pro version. The efficiency gain from 20 dollars is worth it for most people. If you're a heavy user using Agent heavily every day, you can consider Pro Plus or Ultra.

For heavy Cursor users like me, even with an advanced plan, I have to face sky-high bills...

![](https://pic.yupi.icu/1/yupicursorbilling.png)

Additionally, Agent mode may need to wait longer when handling complex tasks. Although there's AI assistance, it still requires some programming foundation — complete beginners with zero foundation might find it a bit complex.

For more Cursor usage tips and cost-saving methods, you can check the [Advanced Optional: Experience & Techniques] section of this tutorial series, which has detailed explanations.



## III. Other Mainstream AI Code Editors

Besides Cursor, there are some other AI code editors on the market worth understanding.



### Windsurf

[Windsurf](https://codeium.com/windsurf) is an AI code editor launched by Codeium, whose biggest advantage is it's completely free. After using up your quota, Windsurf can still be used for free, making it especially suitable for students and developers with limited budgets.

And it provides Cascade agent mode (similar to Cursor's Agent) — describe requirements in natural language, and AI will automatically create and modify multiple files. The biggest advantage is it's completely free.

![](https://pic.yupi.icu/1/image-20260107135727334.png)



### Antigravity

[Antigravity](https://antigravity.google) is an agent development platform launched by Google, with an interface similar to VS Code. It uses an Agent-first design where AI agents can autonomously plan, execute, and verify complex tasks.

It integrates large models like Gemini, supports 1M Token context, suitable for developers who want to try the Google AI ecosystem and need ultra-long context for large projects.

![](https://pic.yupi.icu/1/image-20260107135834072.png)



### Kiro

[Kiro](https://kiro.dev) is an AI IDE launched by Amazon, emphasizing "specification-driven development." Write requirements specifications first, then let AI implement them.

It deeply integrates with AWS and can deploy directly to AWS services, suitable for developers using AWS services, teams that need standardized development processes, and scenarios doing enterprise-level applications.

![](https://pic.yupi.icu/1/image-20260107135922286.png)



### TRAE

[TRAE](https://www.trae.ai) is an AI-native programming tool launched by ByteDance. It has 2 development modes:

- IDE mode is similar to Cursor, retaining traditional development workflow
- SOLO mode lets AI lead, automatically advancing development tasks

TRAE's SOLO mode is its biggest highlight, different from traditional human-led + AI-assisted programming — SOLO mode lets AI lead tasks and automatically execute development. You just need an idea, and AI can automatically generate product requirement documents, technical architecture documents, then autonomously write code, install dependencies, test and verify, until the project can run normally.

Moreover, TRAE supports integrating third-party services like Supabase database, Stripe payment, OpenRouter AI services, etc. — you can integrate in a foolproof way without reading documentation. It can help you rapidly develop commercial-grade products with complete frontend and backend.

![](https://pic.yupi.icu/1/image-20250928222329915.png)

The domestic version of TRAE is very suitable for Chinese users with fast access speeds. I used TRAE SOLO to develop a WeChat mini-program — interested folks can watch the [practical video](https://www.bilibili.com/video/BV1yMn3zuE7L).



### Zed

[Zed](https://zed.dev) is a high-performance code editor written in Rust, built by the Atom founding team. Built-in AI assistant, supports multiple AI models, supports real-time collaborative editing.

Advantages are extremely fast startup speed and low resource usage. Suitable for developers pursuing ultimate performance, those with average computer configurations, and those needing team collaboration.

![](https://pic.yupi.icu/1/windows-multibuffer.jpeg)



## IV. How to Choose an AI Code Editor?

By now, you might ask: With so many AI code editors, which one should I choose?

Actually, the choice is simple — mainly depends on your needs and budget.

**Cursor is priority recommended.** As of now, Cursor is still the most powerful and mature ecosystem AI code editor, and I also primarily use Cursor for project development.

As mentioned earlier, its advantages include:

- Comprehensive functionality: Tab, Agent, Chat, inline editing, etc.
- Fast updates: Frequently launches new features
- Strong context understanding: Supports up to 1M Token
- Multi-model support: Can freely switch between Claude, GPT, Gemini, etc., and connect to new models immediately
- Mature ecosystem: Based on VS Code, all plugins work
- Active community: Easy to find solutions to problems

If you have sufficient budget (over 20 USD per month), Cursor is the first choice. If you have limited budget, Windsurf is a great free choice — although relatively simple in functionality, it's completely sufficient for learning.



## V. AI Code Editor Practical Tips

Whether you choose Cursor or other AI code editors, the following practical tips can help you improve efficiency.

### 1. Make Good Use of Context

The most powerful aspect of AI code editors is their ability to understand the context of the entire project. To fully utilize this:

- Create `README.md` in the project root directory describing the overall architecture
- Use `.cursorrules` (or other editor-supported rule files) to tell AI your coding standards
- Reference related files when chatting (`@filename`)

For example:
```
Referencing the code style of @src/components/ImageUploader.vue, create a Card component
```

![](https://pic.yupi.icu/1/image-20260107140926938.png)



### 2. Implement in Steps

Don't present overly complex requirements all at once — do it in steps:

❌ Bad way:
```
Make a complete e-commerce website
```

✅ Recommended way:
```
Step 1: Create product list page
Step 2: Add product detail page
Step 3: Add shopping cart functionality
Step 4: Add checkout functionality
```



### 3. Use Shortcuts

Proficient use of shortcuts can greatly improve efficiency.

Taking Cursor as an example, I suggest trying these shortcuts — they'll let you use the mouse less and operate faster.

Chat-related:
- `Cmd/Ctrl + L`: Toggle sidebar (unless bound to a mode)
- `Cmd/Ctrl + I`: Toggle sidebar (unless bound to a mode)
- `Cmd/Ctrl + K`: Open inline editing, can insert AI-generated code at current location
- `Tab`: Accept suggestion

Code editing:
- `Cmd/Ctrl + Shift + L`: Add selected content to chat
- `Alt + ↑/↓`: Move current line
- `Cmd/Ctrl + /`: Comment/uncomment

File operations:
- `Cmd/Ctrl + Shift + F`: Global search

For more latest default keyboard shortcuts, refer to [official documentation](https://cursor.com/cn/docs/configuration/kbd):

![](https://pic.yupi.icu/1/image-20260104192219087.png)



### 4. Code Review

AI-generated code isn't necessarily perfect — develop the habit of reviewing.

Check if the code logic is correct, if there are security risks, if performance is reasonable, if code style is consistent.

Of course, you can also let AI help you review:

```
Please review this code and point out potential problems
```



### 5. Save Important Versions

Git is currently the most mainstream distributed version control system, an indispensable tool for team collaborative development. It can save and manage all update records of files, and distinguish them using **version numbers**. This enables functionality like restoring edited documents to their pre-modification state, comparing differences between file versions, and preventing old versions from overwriting new ones.

Before making major changes, remember to commit to Git:

```bash
git add .
git commit -m "Version before adding user authentication"
```

This way if AI messes up, you can roll back at any time.

💡 If you want to deeply learn Git and GitHub, you can check out my [Git & GitHub Nanny-Level Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866), completely free.



### 6. Make Good Use of Terminal

AI code editors have built-in terminals and can directly run commands. This way you don't need to switch to other windows — you can complete all operations within the editor.

For example, common frontend development commands:

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Run tests
npm test
```

Cursor also supports generating commands in the terminal:

![](https://pic.yupi.icu/1/image-20260107141312489.png)

No need to memorize these commands! If you use Agent mode, AI may automatically execute these commands without you manually typing them.



### 7. Learn the Generated Code

The process of using AI code editors is also a great learning opportunity. AI-generated code might use some technologies and libraries you're not familiar with — this is a great time to learn.

So don't just have AI generate code and be done with it — try to understand it. Where you don't understand, directly ask AI: "What does this code mean?"

You can also try modifying the code to see what happens. This way you can not only complete projects but also learn real programming knowledge, slowly growing into a professional programmer (Vibe Coding version).



## In Conclusion

By now, I believe you have a comprehensive understanding of AI code editors.

**AI code editors are the key step from "knowing how to use AI" to "professional development."**

It lets you more flexibly control code, handle more complex projects, learn more professional development methods, and accumulate real programming capabilities.

My suggestion is, don't be intimidated by the tool's complexity — boldly try it. Immediately download Cursor or another AI code editor, and try to reimplement in an AI code editor the projects you previously made on zero-code platforms. Although you might be a bit unaccustomed at first, you'll soon experience its power.

In the next article, I'll introduce command-line tools, taking you to experience a more advanced, more geeky Vibe Coding method.

Keep it up!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
