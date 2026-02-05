# Gemini CLI: Hands-on Testing of Google's Free AI Command Line Tool

Hello, I'm Yupi.

Google has launched an interesting AI command-line tool — Gemini CLI, which directly integrates AI into the terminal.

![](https://pic.yupi.icu/1/1750927083919-e42152fe-9df9-4686-b813-388ae261b738.png)

According to the [official introduction](https://github.com/google-gemini/gemini-cli), this tool can:

- Handle large codebases (up to 1 million Token context)
- Multimodal capabilities: Generate new applications from PDFs or sketches
- Automate operations: Help query code merge requests and handle complex code merges
- Integrated with numerous tools: Supports connecting to MCP servers, image, video, and audio generation
- Built-in search, and more

Positioned against Claude Code, it currently offers free usage quotas, and best of all, the code is open source!

![](https://pic.yupi.icu/1/image-20260112165459541.png)

As of January 2026, Gemini CLI has already garnered **90,000+ GitHub Stars**, skyrocketing in popularity!

So, how does this tool actually perform? I'll take you through a hands-on experience and share my genuine impressions.

⭐️ Recommended video version: [https://bilibili.com/video/BV1LuKdzjEAc](https://www.bilibili.com/video/BV1LuKdzjEAc/)



## 1. Installation and Setup

Following the official documentation, we first need to install the Node.js runtime environment. Simply go to the [official website](https://nodejs.org/) to install it, **note that the version must be >= 20** (latest requirement as of 2026).

Then, open the terminal and enter a command to install the tool globally:

```bash
npm install -g @google/gemini-cli
```

Or install using Homebrew (macOS/Linux):

```bash
brew install gemini-cli
```

After installation, enter the `gemini` command to perform some basic setup:

![](https://pic.yupi.icu/1/1750927215041-aef86c7f-90b6-41e1-8509-cb53809372dd.png)

Next is the crucial part, requiring a wave of account verification. Individual users should select the first option.

![](https://pic.yupi.icu/1/1750927255279-3b2d860a-c514-492a-8b27-a8abe27b4b31.png)

Here, you might encounter two types of verification failures. The first is due to network issues (hard to resolve), and the second is an account type mismatch, as shown:

![](https://pic.yupi.icu/1/1750927301003-4937f694-3fc9-493f-8309-e169439f59fa.png)

For the second case, the solution is simple. Go to the [Google Cloud](https://console.cloud.google.com/) console, create a new project to get a `project_id`:

![](https://pic.yupi.icu/1/1750927486133-ecf76c02-ba82-4f85-adfe-4d168247bee6.png)

Then, enter the following command in the terminal to set the environment variable, and retry to log in:

```bash
export GOOGLE_CLOUD_PROJECT=<your project_id>
```

After successful login, we can start using it.



## 2. Practical Testing

Next, I selected 8 different scenarios to verify its capabilities from multiple aspects. You can also get a sense of Gemini CLI's actual performance. Only when everyone says it's good is it truly good.

![](https://pic.yupi.icu/1/1750928002955-c44764ed-abd4-4568-ad07-954d909aa360.png)

### 1. Basic Q&A

Input prompt:

```
Hello, what can you do? What are your advantages?
```

Unexpectedly, it started with an error? And various gibberish.

![](https://pic.yupi.icu/1/1750928093701-0a2cdf6c-483c-4198-8933-00268b7ca2af.png)

After a while, it finally filled the screen with red errors. The error message indicated that I didn't enable API permissions:

![](https://pic.yupi.icu/1/1750928146165-9359e7e2-0dfa-4b7e-b3bb-31bfcf94b540.png)

Directly visiting the URL in the error message allows you to enable API permissions in the console. Let's enable it:

![](https://pic.yupi.icu/1/1750928172586-6ec6dd3b-db41-4fb3-b096-e933936e1e37.png)

Try again! This time, the AI's response was on point. It said it's an AI software engineer, ensuring transparent and secure operations. The result was decent, but the speed was a bit slow. A simple question took 20 seconds, which is a side effect of intelligent agents.

![](https://pic.yupi.icu/1/1750928224341-15221ba1-7dd2-462a-91f2-f9d832eda07c.png)



### 2. Web Search

Input prompt to let the AI automatically download memes:

```markdown
Please help me get 10 healthy panda head memes and download them to the current directory
```

The AI recommended several meme websites but couldn't download them directly:

![](https://pic.yupi.icu/1/1750928294365-8a9833e9-a05a-413f-8090-af944d2b4daf.png)

Does it not support download tools?

We can press the `/` key to see the commands supported by Gemini CLI:

![](https://pic.yupi.icu/1/1750928337773-c1fec292-a628-4b3d-93e4-a8846ab7b5b2.png)

Looking at the tool list, it seems there's no web resource download tool, which is tough for the AI. But it supports writing Shell scripts, so let's guide the AI to write a script for resource download.

![](https://pic.yupi.icu/1/1750928445912-9ba1f2bd-2262-499b-bec0-0f5caf967a47.png)

Prompt:

```markdown
Please help me get 10 healthy panda head memes and download them to the current directory. You can achieve this by writing an executable script
```

This time, we can see the agent starting to plan tasks autonomously. It first created a script, and the "write file" operation requires our confirmation. It's recommended to choose "Allow Once" for safety:

![](https://pic.yupi.icu/1/1750928484880-802fa820-8ebe-44d2-963e-34b4eeca590c.png)

When encountering issues, it tries to **re-plan** and retry, which is a key capability of intelligent agents:

![](https://pic.yupi.icu/1/1750928516938-edbd9bb5-1507-4835-a83f-fa64ab5bed4d.png)

After task completion, it remembers to clean up the script, which is a nice touch.

![](https://pic.yupi.icu/1/1750928581541-3e1fdfc3-f18b-4202-9b74-b7e351cce7fd.png)

Alright, mission accomplished. Let's check the downloaded files. Is this size serious? It indeed failed; the downloaded images were completely wrong!

![](https://pic.yupi.icu/1/1750928679026-e945b956-7b1c-40ae-b941-5c41afbab70f.png)



### 3. File Operations

Input the following prompt to let the AI help process my local meme files:

```markdown
Help me double the size of all memes, convert them to WEBP format, and then combine all memes into a GIF
```

Then, I should specify the file path, or the AI might not know what to process.

When I pressed the `@` key to specify the file path, the input box froze? Honestly, this interaction experience isn't great. Every time I select a file, it freezes, and I can't select directories.

![](https://pic.yupi.icu/1/1750928995135-adc3d93a-6afc-4c0e-b971-5ba627ec3fc5.png)

After some struggle, I found that I need to select slowly, following the directory tree listed by the program. Let's select one image first:

![](https://pic.yupi.icu/1/1750929221785-9d4261ea-92e5-439e-b038-54ccb9bcfa33.png)

Okay, this time the AI was smart and asked if I wanted to process multiple files. Definitely:

![](https://pic.yupi.icu/1/1750929281202-176c6599-3e3c-4b0c-93ba-2462c91bf375.png)

Then, the AI found it couldn't process images and needed to download an image processing tool. It said it would use Mac's package management tool to install it. Agree:

![](https://pic.yupi.icu/1/1750929456285-d75c4e55-2593-424c-8bf0-1e52222305eb.png)

After a long wait, it still wasn't done after nearly 10 minutes?!

![](https://pic.yupi.icu/1/1750929498503-93b9d475-97a3-4979-92b5-c1538dce9396.png)

Maybe it's my network, but I couldn't wait any longer. Honestly, by this point, I was already a bit frustrated. It's 2:30 AM, and I'm waiting for software installation?

![](https://pic.yupi.icu/1/1750929564667-ba06cda8-cd5e-44b5-afac-28c62e3af961.png)

Isn't this something you could easily do with a simple Python script?

This tool seems more suited for programmers, with some guidance needed. For example, let's have the AI use a Python script to achieve the task:

```markdown
Help me double the size of all memes, convert them to WEBP format, and then combine all memes into a GIF, using a Python script
```

We can see the AI installed an image processing library and created a virtual environment. Its consideration for security is commendable:

![](https://pic.yupi.icu/1/1750929702268-23a76696-f001-444f-8986-f28ad42d3b39.png)

Then, it wrote and executed the script:

![](https://pic.yupi.icu/1/1750929740570-990bbe0f-f685-4e7d-be7f-ef53402882e5.png)

Task successfully completed. Let's check the results:

![](https://pic.yupi.icu/1/1750929779663-14caecd9-ae80-4727-bc3f-0542fbdf71fe.png)

The size was indeed doubled, the format was successfully converted, and the GIF was generated. Finally, a task completed successfully. Not bad. Processing local images this way is indeed more convenient than web-based AI applications.



### 4. Code Generation

Input the following prompt to have the AI create a pixel photography website:

```markdown
Please help me create a website that can call the camera to take photos, convert the photos to pixel style, support downloads, and have a simple and cool interface
```

This time, the generation speed was quite fast, but it required multiple manual confirmations during the process:

![](https://pic.yupi.icu/1/1750929959173-97f40707-bbcc-4cba-a021-4e3c9e7372d4.png)

Let's check the generated website:

![](https://pic.yupi.icu/1/1750930213995-9ca12c77-e2f4-4626-9da4-8f2783d73eeb.png)

You can adjust the pixel density and download photos with one click. The effect is quite good, and the AI successfully completed this task~

![](https://pic.yupi.icu/1/1750930254795-38b8adcb-3a87-44dd-99d4-0b37532ae1fc.png)



### 5. Code Explanation

Add a learning guide to the newly generated project. Input prompt:

```markdown
Help me generate a learning guide for this project to help new developers get started quickly
```

Since the AI has context, it directly understood which project I wanted it to analyze and quickly generated a project document.

![](https://pic.yupi.icu/1/1750930402860-d39c7707-0e3d-4cc8-aaeb-dbf9344589e4.png)

Then, I asked the AI to open the document file:

![](https://pic.yupi.icu/1/1750930530481-8b8f0abf-30fd-48ff-b36c-61b168af2cde.png)

I originally wanted the AI to directly open a Markdown reader, but it output a bunch of irrelevant content. I don't understand.

![](https://pic.yupi.icu/1/1750930702812-27e5e920-9e3c-48f7-8957-60025b80b773.png)

I'll open it myself. The generated document content is decent, standard GitHub open-source project documentation.

![](https://pic.yupi.icu/1/1750930759557-f4b0a16f-d1c8-46fe-b0e5-21910a2bf752.png)



### 6. Architecture Diagram Generation

Alright, given that the previous task was completed well, let's increase the difficulty. Have the AI generate a layered architecture diagram for the project:

```markdown
Help me generate a layered architecture diagram for the current project
```

The result was a bit of a mix-up. The AI generated an architecture design document:

![](https://pic.yupi.icu/1/1750930929870-b368fc52-c779-42f0-9ad5-fb056b99ef84.png)

You call this pure English document an architecture diagram?

![](https://pic.yupi.icu/1/1750930979557-8ab249fe-727e-4041-99b7-9e154a742090.png)

Then, I'll exert my remaining professionalism and have it generate drawing code for the architecture diagram:

```markdown
Help me generate draw.io code for the layered architecture diagram of the current project
```

This time, it looks more reliable:

![](https://pic.yupi.icu/1/1750931031112-0247644b-2626-459a-ae81-a240ad782400.png)

Let's drag the AI-generated architecture diagram code file into draw.io and open it.

Buddy? You call this an architecture diagram?

![](https://pic.yupi.icu/1/1750931055227-1e674680-468c-4c4d-b182-8bd3026c993e.png)

Let's try the same task with Cursor + Claude 4.

Ah, Claude is quite confident, saying "I can generate a more complete and detailed layered architecture diagram for you":

![](https://pic.yupi.icu/1/1750931203239-924cc09e-c80f-4acf-9855-66d6b4102cac.png)

Alright, let's see the generated result. Isn't the difference clear?

![](https://pic.yupi.icu/1/1750931312134-a573f7ff-07ca-4852-830a-07d74bc21690.png)



### 7. Visualization Chart Generation

Have the AI analyze the project's commit history. Input prompt:

```markdown
Based on the current project's commit history, generate a visualization chart to help me analyze the project's development timeline
```

We can see the AI using the git log command to view the commit history and then starting to generate the chart.

![](https://pic.yupi.icu/1/1750931424995-0e5cd8c2-1dfe-4f09-ac29-c08b1c1388b4.png)

Wait? Where's the chart???

My expectation was definitely to generate an image, or at least a character drawing that looks like a chart. It's a bit tough for it.



### 8. Multimodal

By the time I got to testing multimodal capabilities, it was already 3 AM, and I was numb. Sigh, let's try multimodal one last time.

Input image generation prompt:

```markdown
Help me generate a new image with a similar style based on the images in the current directory
```

This time, the AI directly refused, not supporting image creation. Why not write a script? You don't need AI; an image processor would work, right?

![](https://pic.yupi.icu/1/1750931630520-47da3d4e-c55e-4b1c-9507-17dd0f08cb1e.png)

Then, let's try explaining an image. Input image explanation prompt:

```markdown
Help me explain all the images in the current directory
```

It did explain them, but I have to complain—it's still in English. Probably related to the program's language settings. The experience isn't that great.

![](https://pic.yupi.icu/1/1750931670952-251c1eb3-487a-44ca-b217-194f92a5442a.png)

Gemini CLI likely uses the Gemini 2.5 Pro model, which has native multimodal input capabilities, meaning it can recognize images but can't create them. Audio and video creation are probably achieved through third-party large models (or MCP tools).

Finally, let's have it explain a PDF. Input prompt:

```markdown
Help me summarize the content of the PDF and generate a new PDF
```

The result surprised me. The AI prompted that the input exceeded the token limit?

![](https://pic.yupi.icu/1/1750931736351-d36ac39e-23ce-42c1-af30-d1f56284d48a.png)

Isn't it supposed to have a 1 million token context? Why does reading a tiny PDF exceed the limit? I wouldn't be surprised if it couldn't generate a PDF, but my