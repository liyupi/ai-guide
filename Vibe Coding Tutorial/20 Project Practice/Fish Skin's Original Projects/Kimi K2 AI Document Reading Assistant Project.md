# Kimi K2 - AI Document Reading Assistant Project Practice

This project is an AI document reading assistant website that can help you quickly understand various complex documents (papers, technical documentation, PDFs, etc.) and help you manage documents.

The project includes complete frontend and backend, developed entirely through AI conversation without writing a single line of code. Suitable for students who want to rapidly practice complete Vibe Coding development workflows and learn how to use AI to develop practical tools.



---

Hello everyone, I'm Programmer Fish Skin. The school season has arrived, and I'm sure many friends are about to start collecting and reading papers. When I learn new technical knowledge myself, I also go read documentation, and I know the pain of reading documents all too well. Individually, every word makes sense, but together they're incomprehensible.

![](https://pic.yupi.icu/1/1757559057843-b9d37369-49bf-4eec-878a-c70ac945cbd9.png)

To help everyone avoid the torture of documentation, I used AI to develop an AI document assistant website that can help you quickly understand various complex documents and manage them for you.

![](https://pic.yupi.icu/1/1757561248387-205bf672-7a6c-452a-a283-698fb526601c.png)

The website is completely free, and the code is completely open source!

Open source repository: [github.com/liyupi/literature-assistant](https://github.com/liyupi/literature-assistant)

![](https://pic.yupi.icu/1/1757829143308-d5bfdac6-847a-4061-9194-4821bdf3d3dc.png)

Below I'll first teach everyone how to use the website, then share the development process, and also how to use Claude Code in China.

⭐️ Recommended video version, learn in 2 minutes: [bilibili.com/video/BV1MnpVzdETW](https://www.bilibili.com/video/BV1MnpVzdETW/)



## How to Use?

First download the open source code to your computer, then directly run the quick start script I provide, and open the webpage to see the results.

💡 Make sure your computer has Node.js and Java environments. You can refer to the README.md documentation for installation.

![](https://pic.yupi.icu/1/1757567928358-ad506045-faaf-47b1-b742-190c83c94ad3.png)



When you need to read a document, click the "Single Import" button, upload the document file, and then fill in the Kimi AI API Key.

![](https://pic.yupi.icu/1/1757560732751-de713284-c039-41c1-b9f4-0af34e4c703c.png)



I chose Kimi because they just released the new K2 model, which performs very well in programming, reasoning, and document understanding;

Moreover, it supports 256K context, so even papers with hundreds of thousands of words can be handled.

![](https://pic.yupi.icu/1/1757560219469-2eab0801-a9b3-49dd-b680-d1d27c1850cf.png)



The new Kimi K2 model also performs very well in benchmark tests like SWE-bench Verified that focus on real software engineering tasks:

![](https://pic.yupi.icu/1/1757560161782-1c78bd3c-a3a5-42f9-b79b-a0b07d808e6b.png)



You only need to log in to [Kimi's development console](https://platform.moonshot.cn/), then enter API Key management to get a key for calling the large model.

![](https://pic.yupi.icu/1/1757560312832-cfd4158d-8c31-4c22-8b42-573551334863.png)



Although new users have free quota, please don't leak your key!

![](https://pic.yupi.icu/1/1757560674974-180d8475-e83e-4b35-ba9b-2ded866aa730.png)



After filling in the API Key, you can generate a document reading guide. The generation speed is very fast.

![](https://pic.yupi.icu/1/1757560771758-4c3df93e-889d-4c74-afa2-90e69347f286.png)



The AI-generated results are quite good, with both images and text, helping you understand complex documents faster.

![](https://pic.yupi.icu/1/1757560820325-87111dd8-cd82-49d0-9385-24ea9a33e885.png)



You can also batch import multiple documents and simultaneously call AI to generate reading guides, improving efficiency.

![](https://pic.yupi.icu/1/1757560886812-1706415c-cff5-4475-872f-ba66891563f7.png)



Additionally, you can use this website as your own smart document collection folder. You can categorize and search imported documents, download original files, and view document reading guides at any time. **Don't let your collected documents get lost again~**

![](https://pic.yupi.icu/1/1757560925975-079ad961-7cc8-498b-99e2-84a4a534023f.png)



## How to Implement?

In the past, such a website might have taken several days to build. But now AI programming technology is very mature. I chose Claude Code AI development tool and easily finished it in a day, without writing a single line of code myself.

First, enter a command in the terminal to install Claude Code:

```bash
npm install -g @anthropic-ai/claude-code
```

Then execute the `claude` command, and you can start asking it questions~

Result: Error!

![](https://pic.yupi.icu/1/1756451588360-37620a0b-bc2f-4ad5-adf9-4efde87f17ed.png)

**Damn it, this crappy thing doesn't support domestic use!**

But no problem, we can switch to Kimi. In the terminal, enter commands to configure environment variables (note the distinction between operating systems):

```bash
# Linux/macOS start high-speed version kimi-k2-turbo-preview model
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
export ANTHROPIC_AUTH_TOKEN=<Your API Key>
export ANTHROPIC_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_SMALL_FAST_MODEL=kimi-k2-turbo-preview

# Windows Powershell start high-speed version kimi-k2-turbo-preview model
$env:ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic";
$env:ANTHROPIC_AUTH_TOKEN="<Your API Key>"
$env:ANTHROPIC_MODEL="kimi-k2-turbo-preview"
$env:ANTHROPIC_SMALL_FAST_MODEL="kimi-k2-turbo-preview"
```



Then you can happily use Claude Code to generate code~

![](https://pic.yupi.icu/1/1756451713145-29e5ba15-76b2-4848-903a-f098b942e2f9.png)



For websites with complete frontend and backend, it's hard to get AI to generate satisfactory results with just one prompt. So we need to **decompose work steps** like real enterprise development: backend first, then frontend, finally frontend-backend integration. It's best to develop features one by one, and adjust promptly when problems arise.

Sharing some reference prompts:

![](https://pic.yupi.icu/1/1757567728565-5724de3e-7863-457b-9866-368c1535bd2c.png)



------

That's it for this sharing. I hope this tool is helpful to everyone. Don't forget to give Fish Skin a like, follow, and share for support. Thank you all~

![](https://pic.yupi.icu/1/1757829315038-73ef4fd7-7fef-4fa2-859d-11bb28381933.webp)



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
