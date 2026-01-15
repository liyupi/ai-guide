# AI IDE Plugins

> Adding AI capabilities to your familiar editor



Hello, I'm Programmer Fish Skin.

In previous articles, we learned about AI code editors and AI command-line programming tools.

But if you have programming foundation and are already used to using integrated development environments (IDEs) like VS Code / IntelliJ IDEA, don't want to switch editors, but still want to do Vibe Coding, what should you do?

**IDE AI Plugins** are the answer you're looking for.

In this article, I'll introduce the most mainstream IDE AI plugins, helping you add AI capabilities to your familiar editor.



## I. Why Choose IDE Plugins?

Before understanding specific plugins, let's first clarify: What's the difference between IDE plugins and Cursor? Why use plugins?

Cursor is a standalone editor — although based on VS Code, it's a complete piece of software. IDE plugins are extensions installed on your existing editor (VS Code, IntelliJ IDEA, etc.), no need to switch editors.

To use an analogy: Cursor is like buying a new car with all features equipped; IDE plugins are like adding new features to your current car — it's still the same car.

The advantages of IDE plugins are obvious. First is no need to switch editors — if you're already used to a certain editor, have configured various plugins and shortcuts, and don't want to adapt to a new environment, then using plugins is the best choice.

Plus, you can install different plugins as needed, combine freely, and if you don't like a plugin you can uninstall and switch to another anytime. Many plugins are open source and free, or you can use your own API Key, making costs more controllable.

If you're a beginner and haven't formed fixed editor habits yet, using Cursor directly might be simpler. But if you're already an experienced user of a certain editor, plugins will be the better choice.



## II. Cline - The Most Powerful Open Source AI Plugin

[Cline](https://cline.bot/) is currently the most powerful open-source AI programming plugin, called the open-source version of Cursor.

Cline's biggest advantage is **cross-platform support** — not only does it support VS Code, but also JetBrains series' IntelliJ IDEA, PyCharm, WebStorm, and other editors.

![](https://pic.yupi.icu/1/image-20260108222935455.png)

It's completely open source and free, supports Claude, GPT, Gemini, DeepSeek and other large models, and can deploy MCP services to extend functionality. Not only can it chat to generate code, but also autonomously execute commands, modify multiple files, use browsers — in short, very comprehensive functionality.

Let me demonstrate Cline's usage flow.



### Using Cline in VS Code

For example, I want to use Cline to create a React project in VS Code.

1) Open the extension store in VS Code, search for "Cline", and click install.

![](https://pic.yupi.icu/1/image-20260108223139213.png)

2) After installation, click the Cline icon in the sidebar. You can use it directly for free, or use your own large model API Key.

![](https://pic.yupi.icu/1/image-20260108223220642.png)

3) After clicking next, Cline will guide you to create an account — just register and login with GitHub or email.

4) Once the account is set up, you can use it happily — directly enter your requirements in the Cline panel:

```
Create a React + TypeScript project including:
- Home page
- About page
- Navigation bar
- Use React Router
```

![](https://pic.yupi.icu/1/image-20260108223531152.png)

5) Next, Cline will automatically run commands, install necessary dependencies, create each component file, configure routing, modify styles. During the entire process you only need to confirm each operation, or let it execute fully automatically.

![](https://pic.yupi.icu/1/image-20260108223742056.png)



### Using Cline in JetBrains

If you're a JetBrains IDE user, open Settings → Plugins in the IDE, search for "Cline", and install it. Usage is exactly the same as the VS Code version.

![](https://pic.yupi.icu/1/image-20260108224135571.png)



## III. Other AI Plugins Worth Attention

Besides Cline, there are some other AI plugins worth understanding.



### GitHub Copilot

[GitHub Copilot](https://github.com/features/copilot) is the most mature AI programming assistant, supporting VS Code, the entire JetBrains series, Vim, Neovim, and other editors.

Main functionality is code completion — when you write code it automatically suggests what to write next. There's also Copilot Chat functionality, allowing you to chat with AI in the sidebar.

![](https://pic.yupi.icu/1/image-20260108225417720.png)

Its advantages are it's mature and stable, code completion quality is very high, and cross-platform support. Most importantly, students and open source contributors can use it for free.



### JetBrains AI Assistant

[JetBrains AI Assistant](https://www.jetbrains.com/ai-assistant/) is the official AI programming assistant launched by JetBrains, specifically optimized for JetBrains IDEs. When it first came out, I even shared about it at the Alibaba Cloud Computing Conference haha.

![](https://pic.yupi.icu/1/image-20260108230013824.png)

It not only has code completion, but can also generate tests, explain code, refactor code, generate documentation, etc. Plus it deeply integrates with various IDE functions like debugging, refactoring, testing, generating commit messages, etc.

![](https://pic.yupi.icu/1/image-20260108225718180.png)

The advantage is it's officially made by JetBrains, so has the best integration with the IDE, supports multiple AI models, and has comprehensive functionality. The downside is it requires a JetBrains paid subscription.



### Continue

[Continue](https://www.continue.dev/) is an open-source AI programming plugin with functionality similar to Cline but more lightweight. Supports multiple AI models, has code completion, chat, code editing and other functions, the interface is quite simple, easy to get started. Completely free, supports VS Code and JetBrains.

![](https://pic.yupi.icu/1/image-20260108230116299.png)



### Supermaven

[Supermaven](https://supermaven.com/) is a plugin focused on code completion. The biggest feature is a 1 million token context window, extremely fast completion speed, and very high accuracy.

![](https://pic.yupi.icu/1/image-20260108230146505.png)



### Amazon Q Developer

[Amazon Q Developer](https://aws.amazon.com/q/developer/) (formerly CodeWhisperer) is an AI programming assistant launched by Amazon.

Features include deep integration with AWS services, supports multiple IDEs (VS Code, JetBrains, etc.), has a free version, and code security scanning. Suitable for developers using AWS services and teams needing code security scanning.



## IV. How to Choose an AI IDE Plugin?

- If you want the most powerful functionality (agents, multi-file editing), choose Cline. It supports VS Code and JetBrains, is completely free, with functionality close to Cursor.
- If you mainly need code completion, choose GitHub Copilot. It's the most mature and stable, with the highest code completion quality, and cross-platform support.
- If you're already subscribed to JetBrains, directly use JetBrains AI Assistant because it has the best integration with the IDE.
- If you want a lightweight tool, choose Continue.

I currently don't use IDE plugins very frequently — before I mainly used Cline (comprehensive functionality + free), GitHub Copilot (high code completion quality), and some domestic AI plugins like Zhipu CodeGeeX, Tongyi Lingma, etc.



## In Conclusion

By now, I've finished introducing mainstream AI programming tools. I suggest everyone experience them and choose what suits you — that's the best.

In the next article, I'll introduce auxiliary tool collections to help you complete your entire development toolchain.

Keep it up!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
