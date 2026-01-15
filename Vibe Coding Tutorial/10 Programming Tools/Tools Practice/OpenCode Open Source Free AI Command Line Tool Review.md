# OpenCode: Open Source Free AI Command Line Tool Review

Hello everyone, I'm Programmer Fish Skin.

Claude Code has always been recognized as the AI programming command line tool Top 1, almost god-like existence in AI and programmer circles.

![](https://pic.yupi.icu/1/happy-new-year-claude-coders-v0-o2quvbl99lag1.png)

But this thing is really not friendly to Chinese users...

First, if you want to use Claude Code, you must have special network + official account, otherwise you'll see nothing but red.

![](https://pic.yupi.icu/1/cannotuseclaude.png)

Additionally, in September 2025, Anthropic suddenly announced for some unknown reason **a comprehensive ban on Chinese-controlled enterprises using Claude services**, not only including mainland Chinese companies, but even overseas companies with over 50% Chinese capital are within the ban!

Anthropic even specifically named China, calling us an **hostile country**!

![](https://pic.yupi.icu/1/image-20250905164631315.png)

The world has suffered from Claude Code for too long!

But recently, many programmer friends around me have started switching from Claude Code to another tool — the suddenly hot open-source project OpenCode.

![](https://pic.yupi.icu/1/image-20260107174223010.png)

This thing only took half a year to reach 52k Stars on GitHub!

What does that mean? More than the sum of all the dozens of projects I've open-sourced on GitHub! I'm envious...

![](https://pic.yupi.icu/1/opencodestarhistory.png)

What exactly is OpenCode? Why is it so hot?



## What is OpenCode?

[OpenCode](https://opencode.ai/) is a 100% open-source AI programming command line tool that can be used in **terminals, IDEs, and even desktop applications**.

![](https://pic.yupi.icu/1/screenshot.png)

You might ask: What's the difference between this and Claude Code?

Try it and you'll know, right?

Next, let me walk you through hands-on practice, from zero to installation, configuration, to actually writing code, a full service~



## Getting Started with OpenCode from Scratch

### 1. Install and Run OpenCode

Go directly to the OpenCode official website and copy one command:

![](https://pic.yupi.icu/1/image-20260107174407894.png)

Command as follows:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Then execute it in the terminal to complete installation.

After installation is complete, enter `opencode` to enter the program, and then you can use it happily~

![](https://pic.yupi.icu/1/image-20260107174646918.png)

Let's start with a classic Hello World, AI successfully gave a reply.

![](https://pic.yupi.icu/1/image-20260107174755331.png)

Congratulations, at this point you've already mastered 70% of OpenCode.



### 2. Select Mode and Model

OpenCode supports 2 modes. Default is Build mode, used to build applications and generate code.

Press Tab once to switch to Plan mode, used to generate execution plans.

![](https://pic.yupi.icu/1/image-20260107174952823.png)

Press `Ctrl + p` to open the command panel, which has dozens of built-in commands. Let's first try switching the large model:

![](https://pic.yupi.icu/1/image-20260107175255527.png)

4 free models are provided by default:

![](https://pic.yupi.icu/1/image-20260107175409282.png)

Wow, even Zhipu's latest GLM-4.7 is free? Then my Coding Plan package was opened for nothing?

![](https://pic.yupi.icu/1/image-20260107175513490.png)

Besides free models, OpenCode supports many AI models, you can freely choose:

![](https://pic.yupi.icu/1/image-20260107175614359.png)

After selecting a model, just configure your own API Key:

![](https://pic.yupi.icu/1/image-20260107175657296.png)

If you have a **Claude Pro/Max subscription account** before, you can directly log in and use it, seamlessly migrating from Claude Code.

![](https://pic.yupi.icu/1/image-20260107175745963.png)



### 3. Shortcut Commands

OpenCode supports slash commands. Enter `/` to see many operations, like viewing model list, viewing Agents, managing MCP, switching themes, etc.:

![](https://pic.yupi.icu/1/image-20260107175926346.png)

Supports dozens of different themes, all quite good-looking. From this point you can also see OpenCode really values user experience:

![](https://pic.yupi.icu/1/image-20260107180108430.png)

Enter `@` to quickly associate directory files, adding context for AI:

![](https://pic.yupi.icu/1/image-20260107182710150.png)



### 4. Interactive Experience

Compared to Claude Code, OpenCode really maximizes command-line interactive experience. I even think it's a desktop application disguised as a command line.

You can click a message, and a message action box will pop up. You can withdraw messages and AI replies, also copy, or start a new conversation based on current conversation.

![](https://pic.yupi.icu/1/image-20260107180609525.png)

You can scroll up and down with the mouse to switch selections, and can directly click to enter the next step.

You can press `Ctrl + p` to open the command panel, then enable the sidebar:

![](https://pic.yupi.icu/1/image-20260107181100523.png)

Then the interface becomes like this — you call this a command line?

![](https://pic.yupi.icu/1/image-20260107181218259.png)



### 5. LSP Support

Careful you must have seen, there's an `LSP` in the right sidebar. What the hell is this? Old pervert?

LSP (Language Server Protocol) is a communication protocol developed by Microsoft for communication between code editors and language servers.

Simply put, **LSP is the technology that lets editors understand code.**

For example, when you write code in VS Code, enter `console.` and it automatically suggests `log`, click function name to jump to code definition, wrong code gets red line warning. These code editor features are all LSP working behind the scenes.

OpenCode supporting LSP means AI can truly understand your code structure, instead of treating code as ordinary text and guessing blindly — modifications are more accurate.

For example, I let AI introduce the most valuable code in my AI Q&A platform project, and LSP comes into play. It can help AI quickly locate where a certain piece of code is called, what variables are referenced, instead of letting AI stupidly search text globally.

![](https://pic.yupi.icu/1/image-20260107181807464.png)



### 6. Return to Previous Session

If you accidentally close OpenCode, don't worry, you can open the command panel, select "Switch session" to switch sessions:

![](https://pic.yupi.icu/1/image-20260107183241477.png)

And you can return to previous chat:

![](https://pic.yupi.icu/1/image-20260107183320692.png)



## OpenCode Desktop Version

Although OpenCode supports so many interactions that improve user experience, I estimate most students still don't like the small black box.

No problem, OpenCode also provides a desktop application version! macOS, Windows, Linux all-platform support — this is really the rhythm of competing Claude Code to death...

> Directions: https://opencode.ai/download

![](https://pic.yupi.icu/1/image-20260107182151987.png)

But when I installed and opened it with full enthusiasm, it actually errored!

![](https://pic.yupi.icu/1/image-20260107183123854.png)

After some investigation, I found it was because I had a proxy on. After closing it, it ran normally.

![](https://pic.yupi.icu/1/image-20260107183605119.png)

But being used to Cursor, this interactive experience really feels a bit perfunctory, not recommended for everyone.



## OpenCode Extension Capabilities

So far, I think OpenCode completely crushes Claude Code in frontend user experience, and OpenCode is fully compatible with Claude Code's Skills system!

Skills are capability extensions prepared for AI. You can understand it as work handover documents prepared for new colleagues, containing task execution methods, tool usage instructions, template materials, etc.

For example, you can create a `Company Code Standards Skill`, writing in code style, naming rules, comment requirements, etc. After that, code generated by Claude Code will automatically follow these standards, no need to explain repeatedly each time.

According to official documentation, OpenCode will automatically search these locations for Skills:

- `.opencode/skill/<name>/SKILL.md` (project directory)
- `~/.config/opencode/skill/<name>/SKILL.md` (user directory)
- `.claude/skills/<name>/SKILL.md` (Claude Code compatible)
- `~/.claude/skills/<name>/SKILL.md` (Claude Code compatible)

That means, if you created custom Skills for Claude Code before, you can directly use them here! Another seamless migration.



## Oh My OpenCode Cheat Plugin

If you think OpenCode isn't strong enough, you can try `Oh My OpenCode`, this open-source OpenCode enhancement plugin, already with 10k Stars.

> Project address: https://github.com/code-yeongyu/oh-my-opencode

![](https://pic.yupi.icu/1/image-20260107184457429.png)

How awesome is this plugin? Look at user reviews:

> "It made me cancel my Cursor subscription."

> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day"



Oh My OpenCode's core feature is introducing an agent orchestration system called **Sisyphus**.

I specifically searched for it:

> Sisyphus is a king in Greek mythology who was punished by the gods for deceiving the gods and challenging authority. His punishment was to endlessly roll a boulder up a mountain, only to have it roll down once it reached the top, repeating endlessly, symbolizing futile and ceaseless tasks, but also representing a spirit of resistance against absurd fate.

This system can:

1. Parallel schedule multiple AI models: like let GPT debug while Gemini writes frontend
2. Automatic task management: won't stop until task is complete, persistently like Sisyphus pushing the stone
3. Intelligent code review: automatically detect and clean redundant comments generated by AI
4. Deep LSP integration: provide renaming, jump to definition and other IDE-level features

Simply put, Sisyphus is an AI supervisor that can simultaneously direct multiple AI models to work and watch them complete tasks.

![](https://pic.yupi.icu/1/omo.png)

Although officially it can be installed with one command, I suggest you install bun first, then execute npx to install, otherwise it might error.

```bash
npm install bun -g
npx oh-my-opencode install
```

During installation, it might ask if you have subscriptions to certain models. I don't have anything, just keep choosing "No":

![](https://pic.yupi.icu/1/image-20260107185251337.png)

After installation, enter OpenCode again. After that, you just need to add `ultrawork` (or `ulw`) cheat spell to your prompt to activate all enhancement features. Automatically schedule multiple AI models to work simultaneously, deeply explore codebase, persistently execute.

Let's try it, and by the way verify OpenCode's project-making ability? Can it kick Claude Code away?



## Practical Project - Make an AI Health Assistant with OpenCode

Recently Ant Group's `Ant Afu` AI health assistant became popular. He Jiong teacher can be seen everywhere in TV ads at subway entrances and downstairs from company buildings.

![](https://pic.yupi.icu/1/mayiafuad.jpeg)

Although I haven't used it yet, I heard it can provide AI initial diagnosis by taking photos of skin and reports, and can intelligently answer medical science popularization and treatment suggestions.

Let's also make a similar health assistant website!

Formerly Ant Afu, today Fish Skin Akun.

![](https://pic.yupi.icu/1/image-20260107194117758.png)

First analyze, we need to make a full-stack project including frontend + backend, and the backend also needs to call AI large models to generate content.

Here I choose to use **Vercel AI Gateway** to implement AI capabilities. This is an easy-to-use AI gateway.

![](https://pic.yupi.icu/1/1760687990497-90720fbb-0df6-4ede-87b8-64b8702994e9-20251028181254840.png)

What is an AI gateway?

Simply put, it's like the ticket checkpoint at a train station. Your application's requests first pass through the gateway, which helps you handle a series of complex operations like authentication, rate limiting, monitoring, etc., then forwards requests to AI large models.

![](https://pic.yupi.icu/1/1761645642401-683e786e-3e06-420a-abce-cd43f7bfa901.png)

And Vercel AI Gateway supports connecting to 500+ large models, with free quotas, very suitable for learning and small projects.

> Directions: https://vercel.com/ai-gateway



1) First you need to register and log in to Vercel, then create API Key in the console. Be careful not to leak it:

![](https://pic.yupi.icu/1/1760688078133-7b91b6f3-2fc4-4bb4-b2c1-d517699f0968-20251028181254879.png)



2) Start OpenCode, switch model to GLM-4.7 which has strong programming ability and is free, then enter this prompt:

```markdown
You are a professional programmer. Please help me develop the "Daily Health Assistant" website, where users can record and manage daily health status by chatting with AI.

## Development Requirements

1. Need to include complete frontend and backend, backend using Node.js
2. Use Vercel's AI Gateway to implement AI capabilities, first get usage through official documentation: https://vercel.com/docs/ai-gateway/getting-started
3. Focus on completing core functionality, ensure project can run normally
4. Overall website interface uses fresh green health style, responsive to adapt to various device sizes
5. AI needs to proactively ask user about health status, like sleep, exercise, diet, etc.
```

After clicking send, OpenCode will automatically use web scraping tool to read Vercel AI Gateway's official documentation and learn the latest usage:

![](https://pic.yupi.icu/1/image-20260107190151933.png)

About 5 minutes later, AI completed generating all the code and automatically installed dependencies.

![](https://pic.yupi.icu/1/image-20260107190629349.png)



3) I directly provided AI with the previously obtained Vercel API Key and had it help me start the project:

![](https://pic.yupi.icu/1/image-20260107190751628.png)



4) After successfully starting the project, open browser and visit `localhost:3000` to test the effect.

Result — error! Cannot call AI.

![](https://pic.yupi.icu/1/image-20260107191838608.png)



Maybe AI's understanding of Vercel AI Gateway documentation wasn't good enough, causing it to write wrong AI calling code. So I input the documentation to AI again and had it try once more:

![](https://pic.yupi.icu/1/image-20260107191719979.png)

Result errored again. Even though I had provided AI with API Key, system still errored "Missing API Key".

So I called AI again, telling it "I already provided you with this key before".

![](https://pic.yupi.icu/1/image-20260107192718301.png)

After about 5 rounds of errors and fixes, it still couldn't work normally! I was speechless...

![](https://pic.yupi.icu/1/image-20260107193542108.png)

So, I had an idea: since we're comparing with Claude Code, why not try using Claude Code to fix this problem OpenCode can't solve?

![](https://pic.yupi.icu/1/image-20260107193829543.png)

Let's try! Enter prompt:

```markdown
Now the project backend AI functionality is unavailable
Please refer to https://vercel.com/docs/ai-gateway/getting-started documentation
Help me fix the backend, ensure project can run normally
```

![](https://pic.yupi.icu/1/image-20260107193701784.png)

Claude Code successfully fixed the problem, finally able to use normally:

![](https://pic.yupi.icu/1/image-20260107194915666.png)

💡 Note, if you encounter AI call network timeout issues, you can have AI change the called baseURL to https://ai-gateway.vercel.sh/v1

Previously I used Claude Code / Cursor + GLM for similar tasks and got it done in under 10 minutes. This time it took about 20 minutes, plus back and forth, to get it working.

This makes me have to doubt OpenCode's ability. And I feel GLM large model seems to have become stupider in OpenCode, don't know if it's my illusion...

No way, everyone hypes OpenCode up so much, I must try again, must be my usage problem!

![](https://pic.yupi.icu/1/image-20260107195050357.png)

### Ultrawork Mode

Remember the `ultrawork` (or `ulw`) cheat spell mentioned earlier? Let's do it!

![](https://pic.yupi.icu/1/image-20260107195327425.png)

Enter combat mode:

![](https://pic.yupi.icu/1/image-20260107195346575.png)

You can view sub-agent execution details. First press `Ctrl + x`, then use arrow keys to view different agents.

And when background tasks complete, there's a notification. You can see the "Research Vercel AI SDK conversation mode" task is complete.

![](https://pic.yupi.icu/1/image-20260107195605772.png)

But guess what? I waited nearly 10 minutes and the task still wasn't finished...

Look at this task list, does it need to be this complex? It even created a database for me?

![=](https://pic.yupi.icu/1/image-20260107200237753.png)

I've lost patience to wait, destroy it!

It seems this kind of not-too-complex work can't really demonstrate the advantages of multi-agents. It's like you just want to print a piece of paper, no need to mobilize the whole company, some researching paper types, some researching printer status, some researching how to print more elegantly.



## In Conclusion

After the above simple tests, I'm temporarily watching OpenCode.

The frontend is indeed well done, but backend capabilities feel still behind Claude Code.

If just pursuing frontend convenience, why wouldn't I use Cursor?

![](https://pic.yupi.icu/1/image-20260107200720088.png)

But OpenCode's success illustrates a principle: **whoever is closer to users and can discover pain points has the opportunity to surpass giants.**

Claude Code is indeed strong, but its ban on Chinese users gave the open-source community a perfect opportunity. OpenCode seized this pain point and won users' hearts with a more open approach.

Although the effect needs improvement, after all OpenCode is completely open-source and free. For programmers who like to tinker, customizability is stronger. You can even fork a copy and modify it yourself, play however you want.

OK, that's it for now. Have you used OpenCode? Welcome to discuss your experience in the comments~



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
