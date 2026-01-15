# Gemini CLI: Google's Free AI Command Line Tool - First Test Review

Hello everyone, I'm Fish Skin.

Google has launched an interesting AI command line tool — Gemini CLI, which directly embeds AI right into the terminal.

![](https://pic.yupi.icu/1/1750927083919-e42152fe-9df9-4686-b813-388ae261b738.png)

According to the [official introduction](https://github.com/google-gemini/gemini-cli), this tool can:

- Handle large codebases (up to 1 million Token context)
- Has multimodal capabilities: can generate new applications from PDFs or sketches
- Can automate DevOps: help you query code merge requests, handle complex code merges
- Integrates numerous tools: supports connecting to MCP servers, supports image, video, audio generation
- And has built-in search, etc.

It's positioned as a competitor to Claude Code, now with free usage quotas, and the best part is the code is open source!

![](https://pic.yupi.icu/1/image-20260112165459541.png)

As of January 2026, Gemini CLI already has **90,000+ GitHub Stars**, skyrocketing!

So how is this tool really? Let me take you through a hands-on experience and share my honest feelings.

⭐️ Recommended video version: [https://bilibili.com/video/BV1LuKdzjEAc](https://www.bilibili.com/video/BV1LuKdzjEAc/)



## I. Installation and Startup

Following the official documentation, we first need to install the Node.js runtime environment. Just go to the [official website](https://nodejs.org/) to install it. **Note the version must be >= 20** (latest 2026 requirement).

Then open the terminal and enter one command to install the tool globally:

```bash
npm install -g @google/gemini-cli
```

Or install with Homebrew (macOS/Linux):

```bash
brew install gemini-cli
```

After installation is complete, enter the `gemini` command and do some basic setup:

![](https://pic.yupi.icu/1/1750927215041-aef86c7f-90b6-41e1-8509-cb53809372dd.png)

Next is the key part, you need to go through account verification. For individual users, just select the first option.

![](https://pic.yupi.icu/1/1750927255279-3b2d860a-c514-492a-8b27-a8abe27b4b31.png)

Here you might encounter 2 types of verification failures. The first is network reasons (this is hard to fix), and the second is that the account type doesn't meet requirements, as shown:

![](https://pic.yupi.icu/1/1750927301003-4937f694-3fc9-493f-8309-e169439f59fa.png)

For the second case, the solution is simple. Go to the [Google Cloud](https://console.cloud.google.com/) console, create a new project to get a `project_id`:

![](https://pic.yupi.icu/1/1750927486133-ecf76c02-ba82-4f85-adfe-4d168247bee6.png)

Then enter the following command in the terminal to set the environment variable and retry to log in:

```bash
export GOOGLE_CLOUD_PROJECT=<your project_id>
```

After successful login, we can start using it.



## II. Hands-on Testing

Next I selected 8 different scenarios to verify its capabilities from multiple aspects. You can also get a feel for how good Gemini CLI really is. What users say is good is really good.

![](https://pic.yupi.icu/1/1750928002955-c44764ed-abd4-4568-ad07-954d909aa360.png)

### 1. Basic Q&A

Enter the prompt:

```
Hello, what can you do? What are your advantages?
```

I didn't expect it to error right from the start? And all kinds of nonsense.

![](https://pic.yupi.icu/1/1750928093701-0a2cdf6c-483c-4198-8933-00268b7ca2af.png)

After a while, finally the whole screen was red with errors. Looking at the error message, I hadn't enabled API permissions:

![](https://pic.yupi.icu/1/1750928146165-9359e7e2-0dfa-4b7e-b3bb-31bfcf94b540.png)

Just visit the URL in the error message and you can go to the console to enable API permissions. Enable it, enable it:

![](https://pic.yupi.icu/1/1750928172586-6ec6dd3b-db41-4fb3-b096-e933936e1e37.png)

Again! This time AI's reply was on point. It said it's an AI software engineer, ensuring transparency and security of operations. The result was okay, just the speed was a bit slow — such a simple question took 20 seconds. This is also a side effect of agents, I guess.

![](https://pic.yupi.icu/1/1750928224341-15221ba1-7dd2-462a-91f2-f9d832eda07c.png)



### 2. Web Search

Enter a prompt to let AI automatically go online and download memes:

```markdown
Please help me get 10 wholesome panda head memes and download them to the current directory
```

The result was AI recommended several meme websites for me, but couldn't download directly:

![](https://pic.yupi.icu/1/1750928294365-8a9833e9-a05a-413f-8090-af944d2b4daf.png)

Does it not support download tools?

We enter the `/` key to see the commands Gemini CLI supports:

![](https://pic.yupi.icu/1/1750928337773-c1fec292-a628-4b3d-93e4-a8846ab7b5b2.png)

Go in to view the tool list and find there seems to be no web resource download tool. Can't blame the AI. But it supports writing Shell scripts, so we might as well guide AI to write scripts to implement resource download.

![](https://pic.yupi.icu/1/1750928445912-9ba1f2bd-2262-499b-bec0-0f5caf967a47.png)

Prompt:

```markdown
Please help me get 10 wholesome panda head memes and download them to the current directory. You can implement image download by writing executable scripts.
```

This time you can see the agent starting to plan tasks autonomously. First it created a script, then the "write file" operation needs our confirmation. Here I suggest selecting "allow only once" to be safer:

![](https://pic.yupi.icu/1/1750928484880-802fa820-8ebe-44d2-963e-34b4eeca590c.png)

When it encounters problems, it tries to **replan** and retry. This is also a key capability of agents:

![](https://pic.yupi.icu/1/1750928516938-edbd9bb5-1507-4835-a83f-fa64ab5bed4d.png)

After the task completes, it remembers to clean up the script, which is nice.

![](https://pic.yupi.icu/1/1750928581541-3e1fdfc3-f18b-4202-9b74-b7e351cce7fd.png)

Okay, done. Let's look at the downloaded files. Are these sizes serious? Sure enough, it failed — the downloaded images are completely wrong!

![](https://pic.yupi.icu/1/1750928679026-e945b956-7b1c-40ae-b941-5c41afbab70f.png)



### 3. File Operations

Enter the following prompt to let AI help me process my local meme files:

```markdown
Help me enlarge all meme sizes by 1x, convert to WEBP format, and combine all memes into a GIF
```

Then I should specify the file path, otherwise AI might not know what to process.

The result was when I entered `@` to specify the file path, oh my, the input box just froze? I have to say, this interaction experience isn't great. Every time I select a file it freezes, and I can't select directories.

![](https://pic.yupi.icu/1/1750928995135-adc3d93a-6afc-4c0e-b971-5ba627ec3fc5.png)

After some struggle, I found I had to select slowly, following the directory tree listed by the program. Let's just select one image first:

![](https://pic.yupi.icu/1/1750929221785-9d4261ea-92e5-439e-b038-54ccb9bcfa33.png)

Okay, this time AI was smart and asked if I wanted to process multiple files. Absolutely:

![](https://pic.yupi.icu/1/1750929281202-176c6599-3e3c-4b0c-93ba-2462c91bf375.png)

Then AI found it couldn't process images and wanted to download an image processing tool. It said it wanted to use Mac's package manager to install it. Just agree:

![](https://pic.yupi.icu/1/1750929456285-d75c4e55-2593-424c-8bf0-1e52222305eb.png)

After a long wait, nearly 10 minutes and still not done?!

![](https://pic.yupi.icu/1/1750929498503-93b9d475-97a3-4979-92b5-c1538dce9396.png)

Maybe it's my network, but I really couldn't wait any longer. Honestly, by this point in testing, my mentality was already a bit broken. Waiting for software installation at 2:30 AM?

![](https://pic.yupi.icu/1/1750929564667-ba06cda8-cd5e-44b5-afac-28c62e3af961.png)

I mean, couldn't you just write a simple Python script for this?

I feel this tool still needs to be for programmers, with some guidance. For example, let's guide AI to use Python scripts to implement the task:

```markdown
Help me enlarge all meme sizes by 1x, convert to WEBP format, and combine all memes into a GIF. Implement using Python scripts.
```

You can see AI installed an image processing library, then created a virtual environment. I have to say its consideration for security is okay:

![](https://pic.yupi.icu/1/1750929702268-23a76696-f001-444f-8986-f28ad42d3b39.png)

Then it wrote and executed the script:

![](https://pic.yupi.icu/1/1750929740570-990bbe0f-f685-4e7d-be7f-ef53402882e5.png)

Task successfully completed. Let's see the effect:

![](https://pic.yupi.icu/1/1750929779663-14caecd9-ae80-4727-bc3f-0542fbdf71fe.png)

The sizes are indeed enlarged, format conversion succeeded, and GIF was successfully generated. Finally completed a task smoothly. Not bad. Processing local images this way is indeed much more convenient than web-based AI applications.



### 4. Generate Code

Enter the following prompt to let AI make me a pixel photography website:

```markdown
Please help me create a website that can call the camera to take photos, convert photos to pixel style, and support downloading. The interface should be simple and cool.
```

This time generation speed was quite fast, just needed multiple manual confirmations during the process:

![](https://pic.yupi.icu/1/1750929959173-97f40707-bbcc-4cba-a021-4e3c9e7372d4.png)

Let's look at the generated website effect:

![](https://pic.yupi.icu/1/1750930213995-9ca12c77-e2f4-4626-9da4-8f2783d73eeb.png)

You can adjust pixel density and one-click download photos. The effect is pretty good. AI successfully completed this task~

![](https://pic.yupi.icu/1/1750930254795-38b8adcb-3a87-44dd-99d4-0b37532ae1fc.png)



### 5. Explain Code

Add a learning guide to the just-generated project. Enter prompt:

```markdown
Help me generate a learning guide for this project to help new developers get started quickly.
```

Since AI has context, it directly got which project I wanted it to analyze, and quickly generated a project document.

![](https://pic.yupi.icu/1/1750930402860-d39c7707-0e3d-4cc8-aaeb-dbf9344589e4.png)

Then I let AI help me open the document file:

![](https://pic.yupi.icu/1/1750930530481-8b8f0abf-30fd-48ff-b36c-61b168af2cde.png)

I wanted AI to directly open a Markdown reader, but unexpectedly it directly output a bunch of irrelevant content to me. I don't understand.

![](https://pic.yupi.icu/1/1750930702812-27e5e920-9e3c-48f7-8957-60025b80b773.png)

Well, I'll open it myself. The generated document content is passing — standard GitHub open-source project documentation.

![](https://pic.yupi.icu/1/1750930759557-f4b0a16f-c1d8-46fe-b0e5-21910a2bf752.png)



### 6. Generate Architecture Diagram

Okay, since the previous task was completed okay, let's increase the difficulty. Let AI generate a layered architecture diagram for the project:

```markdown
Help me generate a layered architecture diagram for the current project.
```

The result was a bit of a farce. AI generated an architecture design document for me:

![](https://pic.yupi.icu/1/1750930929870-b368fc52-c779-42f0-9ad5-fb056b99ef84.png)

You call this pure English document an architecture diagram?

![](https://pic.yupi.icu/1/1750930979557-8ab249fe-727e-4041-99b7-9e154a742090.png)

Let me exercise what little professionalism I have left and ask it to help me generate drawing code for an architecture diagram:

```markdown
Help me generate draw.io code for a layered architecture diagram of the current project.
```

This time it looks much more reliable:

![](https://pic.yupi.icu/1/1750931031112-0247644b-2626-459a-ae81-a240ad782400.png)

Come on, let's drag the AI-generated architecture diagram code file into draw.io to open.

Hey bro? You call this an architecture diagram?

![](https://pic.yupi.icu/1/1750931055227-1e674680-468c-4c4d-b182-8bd3026c993e.png)

Come on, same task, let's try with Cursor + Claude 4.

Hey, look how confident Claude is, saying "I can generate a more complete and detailed layered architecture diagram for you":

![](https://pic.yupi.icu/1/1750931203239-924cc09e-c80f-4acf-9855-66d6b4102cac.png)

Okay, look at the generated effect. Isn't the difference immediately obvious!

![](https://pic.yupi.icu/1/1750931312134-a573f7ff-07ca-4852-830a-07d74bc21690.png)



### 7. Generate Visualization Charts

Let AI help me analyze the project's commit records. Enter prompt:

```markdown
Generate visualization charts based on the current project's commit records to help me analyze the project's development history.
```

You can see AI uses the git log command to view code commit records, then starts generating charts.

![](https://pic.yupi.icu/1/1750931424995-0e5cd8c2-1dfe-4f09-ac29-c08b1c1388b4.png)

Wait? Where's the chart???

My expectation was definitely to generate an image, or at least some ASCII art that looks like a picture. A bit too much to ask, I guess.



### 8. Multimodal

By the time I got to verifying multimodal, it was already 3 AM. I was already numb. Sigh, one last坚持 to try multimodal.

Enter image generation prompt:

```markdown
Help me generate a new image with a similar style based on images in the current directory.
```

This time AI simply refused, doesn't support image creation. Couldn't you write a script?! You don't use AI, use some image processing, that would work too, right?

![](https://pic.yupi.icu/1/1750931630520-47da3d4e-c55e-4b1c-9507-17dd0f08cb5e.png)

Let's try explaining an image then. Enter image explanation prompt:

```markdown
Help me explain all images in the current directory.
```

This time it did explain. I have to complain, it even output in English. Maybe it's related to the program's language setting, but the experience isn't that great.

![](https://pic.yupi.icu/1/1750931670952-251c1eb3-487a-44ca-b217-194f92a5442a.png)

Gemini CLI should be using the Gemini 2.5 Pro model behind the scenes, which has native multimodal input capabilities, meaning it can recognize images but cannot create images. Creating audio and video should also be through third-party large models (or MCP tools).

Finally, let's have it explain a PDF. Enter prompt:

```markdown
Help me summarize the PDF content and generate a new PDF.
```

The result was unexpected. AI prompted that input exceeded token limit?

![](https://pic.yupi.icu/1/1750931736351-d36ac39e-23ce-42c1-af30-d1f56284d48a.png)

Isn't it supposed to have 1 million token context? How come reading a tiny PDF exceeds the limit? I wouldn't find it strange that you can't generate PDFs. This PDF file has just a few words and a few pictures. Why?

![](https://pic.yupi.icu/1/1750931817587-41d3c5ef-aca8-4ba6-b89a-a1d55c739c61.png)

I originally wanted to have it generate audio and video too, but forget it. I already have some judgment about this tool.



## III. Pros and Cons of Gemini CLI

After testing 8 dimensions, my feeling is **hard to describe**. Maybe my expectations for Google were too high.

### Advantages

Let me start with advantages. **Terminal operations on local files are indeed more convenient**, and it can be installed with one command, used in existing terminals without downloading a new terminal software. That's pretty good.

And Gemini CLI's biggest advantage is **completely free** (with free quotas), supports Gemini 2.5 Pro model, 1 million Token context window, 1000 requests per day. For budget-limited developers, this is a great choice.

Additionally, Gemini CLI is **completely open source** (Apache 2.0 license), supports MCP server integration, and can extend various functions.

### Disadvantages

But the problems are also obvious.

First is **AI agent effectiveness is average**. Natural language understanding capability is insufficient — it overdoes things, goes off track, does wrong things. And speed is relatively slow; simple questions take a long time.

Second is **interaction experience isn't good enough**. Terminal interaction experience is indeed not as good as web and client. It's hard to see the thinking process, interface display and interaction effects are just so-so. File selector often freezes, selecting files is inconvenient.

Also, **usage barrier is relatively high**. For non-programmers, the barrier to using it is still quite high — need to be familiar with terminal operations. And some functions require additional configuration, like Google Cloud Project.

### Who is it suitable for?

I think using AI to generate terminal commands is great (like Warp AI), but if you insist on using AI in this frame to generate content, I think it's really not necessary.

Gemini CLI might still be somewhat useful for tech giants who are good at Linux server operations, but using this on company servers still requires attention to security.



## In Conclusion

Seeing this, I believe you have a comprehensive understanding of Gemini CLI.

I think Gemini CLI is mediocre, not at the level of overwhelming online hype. At this stage, this thing is more suitable for trying out and learning, not as a daily productivity tool.

However, although the experience is average now, considering Google's technical strength and the open-source free development model, I believe with version iteration, this tool will get better and better. **And for us, having more tool choices is never a bad thing.**

If you have a limited budget and want to try command-line AI tools, Gemini CLI is a good choice. But if you pursue the best experience, I still recommend Claude Code.

What do you think of this tool? Welcome to leave comments in the comments section. Interested students can also experience it and see if it feels the same as mine, or if there are some correct usage methods and techniques. Also welcome to share in the comments. Students learning programming and AI, remember to follow Fish Skin~


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
