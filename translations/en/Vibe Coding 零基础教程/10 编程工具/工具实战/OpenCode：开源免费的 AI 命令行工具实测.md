# OpenCode: Hands-on Review of the Open-Source Free AI Command Line Tool

Hello everyone, I'm programmer Yupi.

Claude Code has long been recognized as the Top 1 AI programming command line tool, almost god-like in the AI and programmer communities.

![](https://pic.yupi.icu/1/happy-new-year-claude-coders-v0-o2quvbl99lag1.png)

But this damn thing isn't very friendly to Chinese users...

First, to use Claude Code, you must have special network access + an official account, otherwise you'll see nothing but red.

![](https://pic.yupi.icu/1/cannotuseclaude.png)

Moreover, in September 2025, Anthropic suddenly announced **a complete ban on Chinese-controlled enterprises using Claude services**, including not only mainland Chinese companies but also overseas companies with over 50% Chinese ownership!

Anthropic even specifically named China, calling us an **adversarial nation**!

![](https://pic.yupi.icu/1/image-20250905164631315.png)

The world has suffered from Claude Code for too long!

But recently, many programmer friends around me have started switching from Claude Code to another tool - the suddenly popular open-source project OpenCode.

![](https://pic.yupi.icu/1/image-20260107174223010.png)

This thing gained 52k stars on GitHub in just half a year!

To put this in perspective - that's more than the total stars of all my dozens of open-source projects on GitHub combined! So jealous...

![](https://pic.yupi.icu/1/opencodestarhistory.png)

What exactly is OpenCode? Why is it so popular?



## What is OpenCode?

[OpenCode](https://opencode.ai/) is a 100% open-source AI programming command line tool that can be used in **terminals, IDEs, and even desktop applications**.

![](https://pic.yupi.icu/1/screenshot.png)

You might ask: How is this different from Claude Code?

Why not try it and see?

Next, I'll walk you through hands-on installation, configuration, and actual coding - a complete one-stop service~



## Getting Started with OpenCode from Scratch

### 1. Installing and Running OpenCode

Go directly to the OpenCode official website and copy this command:

![](https://pic.yupi.icu/1/image-20260107174407894.png)

The command is:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Execute it in the terminal to complete the installation.

After installation, enter `opencode` to launch the program, and you're ready to use it~

![](https://pic.yupi.icu/1/image-20260107174646918.png)

Let's start with the classic Hello World - the AI successfully responded.

![](https://pic.yupi.icu/1/image-20260107174755331.png)

Congratulations, you've now mastered 70% of OpenCode.



### 2. Selecting Modes and Models

OpenCode supports 2 modes. The default is Build mode for application development and code generation.

Press Tab to switch to Plan mode for generating execution plans.

![](https://pic.yupi.icu/1/image-20260107174952823.png)

Press `Ctrl + p` to open the command palette with dozens of built-in commands. Let's try switching the large model first:

![](https://pic.yupi.icu/1/image-20260107175255527.png)

It provides 4 free models by default:

![](https://pic.yupi.icu/1/image-20260107175409282.png)

Wow, even the latest GLM-4.7 from Zhipu is free? Did I waste money on my Coding Plan subscription?

![](https://pic.yupi.icu/1/image-20260107175513490.png)

Besides free models, OpenCode supports a vast number of AI models for you to choose freely:

![](https://pic.yupi.icu/1/image-20260107175614359.png)

After selecting a model, configure your API Key:

![](https://pic.yupi.icu/1/image-20260107175657296.png)

If you previously had a **Claude Pro/Max subscription account**, you can log in directly for seamless migration from Claude Code.

![](https://pic.yupi.icu/1/image-20260107175745963.png)



### 3. Quick Commands

OpenCode supports slash commands. Enter `/` to see many operations like viewing model lists, checking Agents, managing MCP, switching themes, etc.:

![](https://pic.yupi.icu/1/image-20260107175926346.png)

It supports dozens of different themes, all quite aesthetically pleasing, showing OpenCode's focus on user experience:

![](https://pic.yupi.icu/1/image-20260107180108430.png)

Enter `@` to quickly associate directory files and add context for the AI:

![](https://pic.yupi.icu/1/image-20260107182710150.png)



### 4. Interactive Experience

Compared to Claude Code, OpenCode really maximizes the command line interactive experience - I'd say it's a desktop app disguised as a command line tool.

You can click on any message to pop up an action box where you can recall messages and AI responses, copy them, or start a new dialog based on the current conversation.

![](https://pic.yupi.icu/1/image-20260107180609525.png)

You can scroll up and down to switch menus and click directly with the mouse to proceed.

Press `Ctrl + p` to open the command palette and enable the sidebar:

![](https://pic.yupi.icu/1/image-20260107181100523.png)

Then the interface looks like this - you call this a command line?

![](https://pic.yupi.icu/1/image-20260107181218259.png)



### 5. LSP Support

If you're observant, you've noticed the `LSP` in the right sidebar. What's this? Some perverted thing?

LSP (Language Server Protocol) is a communication protocol developed by Microsoft for enabling code editors and language servers to communicate.

Simply put, **LSP is the technology that helps editors understand code.**

For example, when you write code in VS Code and type `console.`, it automatically suggests `log`; clicking a function name jumps to its definition; incorrect code gets red underlines. These editor features are all powered by LSP.

OpenCode's LSP support means the AI truly understands your code structure rather than treating code as plain text, making modifications more precise.

For instance, when I ask the AI to introduce the most valuable code in my AI quiz platform project, LSP comes into play. It helps the AI quickly locate where a code segment is called and what variables it references, instead of having the AI dumbly search the entire text.

![](https://pic.yupi.icu/1/image-20260107181807464.png)



### 6. Returning to Previous Sessions

If you accidentally close OpenCode, don't worry. Open the command palette and select "Switch session":

![](https://pic.yupi.icu/1/image-20260107183241477.png)

You'll return to your previous chat:

![](https://pic.yupi.icu/1/image-20260107183320692.png)



## Desktop Version of OpenCode

Even with all these user experience improvements, I suspect most of you still don't like the black terminal box.

No problem - OpenCode also offers a desktop app version! Supporting macOS, Windows, and Linux - they're really going all out to crush Claude Code...

> Link: https://opencode.ai/download

![](https://pic.yupi.icu/1/image-20260107182151987.png)

But when I installed and opened it with great enthusiasm, it errored!

![](https://pic.yupi.icu/1/image-20260107183123854.png)

After troubleshooting, I found it was because I had a proxy enabled. After disabling it, it ran normally.

![](https://pic.yupi.icu/1/image-20260107183605119.png)

But having gotten used to Cursor, this interaction feels a bit perfunctory - not recommended.



## OpenCode Extension Capabilities

So far, I think OpenCode completely crushes Claude Code in frontend user experience. Moreover, OpenCode is fully compatible with Claude Code's Skills system!

Skills are capability extension packages for AI. Think of them as onboarding documents for new colleagues, containing task execution methods, tool usage instructions, template materials, etc.

For example, you can create a `Company Code Style Skill` documenting code styles, naming conventions, comment requirements, etc. Afterward, Claude Code will automatically follow these standards when generating code without needing repeated explanations.

According to official docs, OpenCode automatically searches for Skills in these locations:

- `.opencode/skill/<name>/SKILL.md` (project directory)
- `~/.config/opencode/skill/<name>/SKILL.md` (user directory)
- `.claude/skills/<name>/SKILL.md` (Claude Code compatible)
- `~/.claude/skills/<name>/SKILL.md` (Claude Code compatible)

This means if you've created custom Skills for Claude Code before, you can use them directly with OpenCode! Another seamless migration.



## Oh My OpenCode Power-Up Plugin

If OpenCode isn't powerful enough for you, try `Oh My OpenCode`, an open-source OpenCode enhancement plugin with 10k stars already.

> Project address: https://github.com/code-yeongyu/oh-my-opencode

![](https://pic.yupi.icu/1/image-20260107184457429.png)

How awesome is this plugin? Check out user reviews:

> "It made me cancel my Cursor subscription."
> 
> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day"

The core feature of Oh My OpenCode is introducing an agent orchestration system called **Sisyphus**.

I looked it up:

> Sisyphus is a king in Greek mythology punished by the gods for deceit and defiance. His eternal punishment was to roll a boulder up a hill, only for it to roll back down upon nearing the top, repeating endlessly - symbolizing futile, never-ending tasks and representing resistance against absurd fate.

This system can:

1. Schedule multiple AI models in parallel: e.g., have GPT debug while Gemini writes frontend
2. Automatic task management: Won't stop until tasks are complete, persevering like Sisyphus pushing his boulder
3. Smart code review: Automatically detects and cleans redundant AI-generated comments
4. Deep LSP integration: Provides IDE-level features like renaming and definition jumping

In short, Sisyphus is an AI overseer that can command multiple AI models simultaneously and ensure they complete tasks.

![](https://pic.yupi.icu/1/omo.png)

Although the official docs say installation is one command, I recommend installing bun first, then using npx to install, otherwise errors may occur.

```bash
npm install bun -g
npx oh-my-opencode install
```

During installation, it might ask if you have subscriptions to certain models. I had none, so I kept selecting "No":

![](https://pic.yupi.icu/1/image-20260107185251337.png)

After installation, re-enter OpenCode. Then just include the `ultrawork` (or `ulw`) power-up incantation in your prompts to activate all enhanced features - automatic multi-model scheduling, deep codebase exploration, relentless execution.

Let's test this and see if OpenCode can handle project work? Can it kick Claude Code to the curb?



## Practical Project - Building an AI Health Assistant with OpenCode

Recently, Ant Group's `Ant Afu` AI health assistant went viral, with ads featuring host He Jiong appearing everywhere from subway stations to office building TVs.

![](https://pic.yupi.icu/1/mayiafuad.jpeg)

Though I haven't used it, I heard it provides AI preliminary diagnosis by scanning skin/reports and intelligently answers medical questions and treatment suggestions.

Let's build a similar health assistant website!

Before there was Ant Afu, now there's Yupi Akun.

![](https://pic.yupi.icu/1/image-20260107194117758.png)

First, let's analyze: we're building a full-stack project with frontend + backend, where the backend needs to call AI models for content generation.

I chose **Vercel AI Gateway** for AI capabilities - a simple, easy-to-use AI gateway.

![](https://pic.yupi.icu/1/1760687990497-90720fbb-0df6-4ede-87b8-64b8702994e9-20251028181254840.png)

What's an AI gateway?

Simply put, it's like a train station ticket gate. Your app's requests first pass through the gateway, which handles authentication, rate limiting, monitoring, and other complex operations before forwarding to AI models.

![](https://pic.yupi.icu/1/1761645642401-683e786e-3e06-420a-abce-cd43f7bfa901.png)

Vercel AI Gateway supports over 500 models and has free tiers, perfect for learning and small projects.

> Link: https://vercel.com/ai-gateway



1) First, register/login to Vercel, then create an API Key in the console (don't leak it):

![](https://pic.yupi.icu/1/1760688078133-7b91b6f3-2fc4-4bb4-b2c1-d517699f0968-20251028181254879.png)



2) Launch OpenCode, switch to the programming-strong, free GLM-4.7 model, and input this prompt:

```markdown
You're a professional programmer. Please help develop the "Daily Health Assistant" website where users can chat with AI to record and manage daily health status.

## Development Requirements

1. Include complete frontend and backend (Node.js backend)
2. Use Vercel's AI Gateway for AI capabilities (refer to official docs: https://vercel.com/docs/ai-gateway/getting-started)
3. Focus on core functionality to ensure the project runs
4. Overall website UI adopts a fresh green health style, responsive across devices
5. AI should proactively ask about health status (sleep, exercise, diet, etc.)
```

After sending, OpenCode automatically uses web scraping to read Vercel AI Gateway's latest docs:

![](https://pic.yupi.icu/1/image-20260107190151933.png)

In about 5 minutes, the AI completed all code generation and automatically installed dependencies.

![](https://pic.yupi.icu/1/image-20260107190629349.png)



3) I directly provided the Vercel API Key to the AI to help launch the project:

![](https://pic.yupi.icu/1/image-20260107190751628.png)



4) After successful launch, open browser to `localhost:3000` to test.

Error! Failed to call AI.

![](https://pic.yupi.icu/1/image-20260107191838608.png)



Perhaps the AI misunderstood Vercel AI Gateway docs, writing incorrect AI calling code. I fed the docs again for another attempt:

![](https://pic.yupi.icu/1/image-20260107191719979.png)

Another error - despite providing the API Key, it still reports "Missing API Key".

I called the AI again, telling it "I already gave you this key earlier".

![](https://pic.yupi.icu/1/image-20260107192718301.png)

After about 5 error-fix cycles, it still didn't work! I'm exhausted...

![](https://pic.yupi.icu/1/image-20260107193542108.png)

Then I had a wild idea: since we're comparing to Claude Code, why not try fixing this OpenCode-unsolvable problem with Claude Code?

![](https://pic.yupi.icu/1/image-20260107193829543.png)

Let's try! Input prompt:

```markdown
Currently, the backend AI functionality isn't working
Please refer to https://vercel.com/docs/ai-gateway/getting-started
Help fix the backend to ensure normal operation
```

![](https://pic.yupi.icu/1/image-20260107193701784.png)

Claude Code successfully fixed the issue - now it works:

![](https://pic.yupi.icu/1/image-20260107194915666.png)

💡 Note: If you encounter AI call timeout issues, have the AI change the baseURL to https://ai-gateway.vercel.sh/v1

Previously, similar tasks with Claude Code/Cursor + GLM took under 10 minutes. This time took about 20 minutes with back-and-forth before working.

This makes me doubt OpenCode's capabilities. Also, GLM seems dumber in OpenCode - maybe just my imagination...

No way - everyone praises OpenCode so much; I must be using it wrong!

![](https://pic.yupi.icu/1/image-20260107195050357.png)

### Ultrawork Mode

Remember the `ultrawork` (or `ulw`) power-up incantation? Let's go!

![](https://pic.yupi.icu/1/image-20260107195327425.png)

Entering battle mode:

![](https://pic.yupi.icu/1/image-20260107195346575.png)

You can view sub-agent operation details: press `Ctrl + x`, then arrow keys to check different agents.

When background tasks complete, there's a notification. Here, "Research Vercel AI SDK Conversation Mode" is done.

![](https://pic.yupi.icu/1/image-20260107195605772.png)

But guess what? After nearly 10 minutes, tasks still unfinished...

Look at this task list - does it need to be this complex? Even databases got involved?

![=](https://pic.yupi.icu/1/image-20260107200237753.png)

I've lost patience - enough!

Apparently, moderately complex work doesn't benefit from multi-agent advantages. It's like needing to print one page but mobilizing the entire company - some researching paper types, some studying printer status, some figuring out elegant printing postures.



## Final Thoughts

After these simple tests, I'm cautiously observing OpenCode for now.

The frontend is indeed excellent, but backend capabilities seem lacking compared to Claude Code.

If just pursuing frontend convenience, why not use Cursor?

![](https://pic.yupi.icu/1/image-20260107200720088.png)

However, OpenCode's success illustrates a principle: **Those closer to users, who identify pain points, have opportunities to surpass giants.**

Claude Code is powerful, but its China ban gave the open-source community a golden opportunity. OpenCode seized this pain point, winning users with openness.

Though effectiveness needs improvement, OpenCode is completely open-source and free, offering stronger customization for tinkering programmers. You can even fork and modify it however you like.

OK, that's all. Have you used OpenCode? Share your experience in the comments~



## Recommended Resources

1) Yupi AI Navigation: [AI resource collection