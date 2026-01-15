# Vibe Coding AI Application Development


Hello, I'm Fish Skin.

Nowadays, AI is no longer some unreachable high-tech, but a tool every developer can easily use. By calling AI APIs, you can quickly make various intelligent applications, like chat assistants, writing assistants, image generators, etc. These projects are not only interesting but also very practical — when completed, you can use them directly or add them to your portfolio.

In this article, I'll take you through building 4 popular AI applications: AI chat assistant, intelligent writing assistant, AI image generator, and speech recognition app.

First, I need to explain that this tutorial section is primarily meant to guide you on the approach and project development process, with the goal of teaching everyone how to use Vibe Coding to develop projects. You need to practice hands-on yourself. If you need more complete Vibe Coding graphic and video tutorials, you can check out Fish Skin's original project practice section.



## I. AI Application Development Basics

Before starting projects, let's first understand the basics of AI application development.

AI applications are applications that use AI capabilities (like text generation, image generation, speech recognition, etc.) to solve real problems. You don't need to train AI models — you just need to call ready-made AI APIs. It's like you don't need to know how a car engine works, you just need to know how to drive.

Currently, there are many mainstream AI API services. For text generation, there's OpenAI's GPT-4, Anthropic's Claude, Google's Gemini, and domestic large models like Tongyi Qianwen, Wenxin Yiyan, Zhipu AI, etc. For image generation, there's DALL-E 3, Midjourney, Stable Diffusion, and domestic Wenxin Yige, etc. For speech recognition, there's OpenAI's Whisper, Google Speech-to-Text, iFlytek speech recognition, etc.

The AI application development process is similar to ordinary applications, just with an added step of calling AI APIs. The entire process is: user input → process input → call AI API → process AI response → display results.

Sounds simple, right? Indeed, the barrier to AI application development is already very low.

![](https://pic.yupi.icu/1/aiapp-workflow%E5%A4%A7.jpeg)

When developing AI applications, there are several precautions to note.

First is API Key security — don't expose your API Key in frontend code, otherwise others can steal your Key. Second is cost control — AI APIs charge by usage, so you need to control costs well and avoid waste. Third is error handling — API calls can fail, so you need good error handling and give users friendly prompts. Finally is user experience — AI responses may take several seconds, so there should be loading indicators to let users know processing is underway.



## II. Project Practice - AI Chat Assistant

AI chat assistant is the most basic and also most practical AI application. Through this project, you can learn how to quickly develop a complete AI dialogue application using Vibe Coding.

This project implements a complete chat interface where users can enter questions and AI gives answers. It needs to support multi-turn dialogue — AI should remember what was said before, so the conversation is coherent. For better experience, AI's answers should display word by word, not all at once — this is called streaming output. Dialogue history is saved locally, so refreshing the page won't lose it. There's also a clear dialogue feature to easily start new topics.

![](https://pic.yupi.icu/1/demoweb6.png)

For technology selection, we use React + TypeScript + Vite as the frontend framework, Tailwind CSS for styling. AI capabilities are implemented by calling large model APIs, dialogue history is saved in LocalStorage, and AI's answers are rendered using react-markdown to support code highlighting and other formats.



### Development Steps

1) Preparation

The first step in development is preparation. You need to get an API Key to call AI models. Visit [Zhipu AI Open Platform](https://bigmodel.cn), enter the user console, and click API Key to get it. Zhipu AI's GLM model works well and has free quotas, suitable for learning use.

2) Write Requirements Document

With an API Key, you can start writing the requirements document. Create a `PRD.md` file to clearly define what you want to build:

```markdown
# AI Chat Assistant PRD

## Core Features
1. Users can enter questions, AI gives answers
2. Support multi-turn dialogue, AI remembers previous dialogue content
3. AI answers should display word by word, not all at once
4. Dialogue history is saved locally, refreshing page won't lose it
5. Can clear dialogue to start new topics
6. AI's answers support Markdown format, including code highlighting

## Interface Requirements
- Chat interface similar to WeChat
- User messages on right, AI messages on left
- Input box and send button at bottom
- Simple and modern design style
```

This document clearly states what features to implement and what the interface looks like.

3) Write Technical Design Document

Then write the technical design document `TECH_DESIGN.md`:

```markdown
# Technical Design

## Tech Stack
- React + TypeScript + Vite
- Tailwind CSS
- Zhipu AI API
- LocalStorage to store dialogue history
- react-markdown to render Markdown

## Data Structure
- Message: role (user or assistant), content (content), timestamp (timestamp)
- Dialogue history stored in LocalStorage

## API Calls
- Use Zhipu AI Chat Completions API
- Enable stream mode for streaming output
- API Key stored in environment variables
```

This document explains what technology to use, what the data structure is, and how to call the API.

4) Write AGENTS.md File

Next, create the `AGENTS.md` file to tell AI development standards:

```markdown
# AI Chat Assistant Development Instructions

## Project Overview
AI chat assistant developed using React + TypeScript, calling Zhipu AI API to implement dialogue functionality.

## Development Standards
- Use TypeScript, ensure type safety
- Use Tailwind CSS for styling
- API Key read from environment variables, don't hardcode
- Errors should have friendly prompts

## Feature Requirements
- Implement streaming output, AI answers display word by word
- Support multi-turn dialogue, send historical messages to API
- Dialogue history saved in LocalStorage
- Support Markdown rendering and code highlighting

## Precautions
- Handle API call failures
- Clear prompts when loading
- Disable input box when sending to avoid duplicate sending
```

This file is development standards for AI, telling it how to write code.

5) Talk with AI to Develop

With these three documents, you can start talking with AI to develop. Open Cursor and put these 3 documents in the project root directory.

The first step is to initialize the project:

```
Please according to PRD.md, TECH_DESIGN.md and AGENTS.md requirements,
initialize a React + TypeScript + Vite project and install necessary dependencies: Tailwind CSS, react-markdown, react-syntax-highlighter.
```

This prompt tells AI what project to create and what dependencies to install. AI will read these three documents, then create the project structure according to requirements, install dependencies, and configure Tailwind CSS.

The second step is to create data types and API encapsulation:

```
Create types.ts file, define Message type. Then create api.ts file to encapsulate Zhipu AI API calls, must support streaming output, parameters read from environment variables.
```

This step lays the foundation for subsequent development — encapsulating data structure and API calls makes later use very convenient.

The third step is to implement the chat interface:

```
Create ChatInterface component to implement chat interface. Requirements:
1. Message list displays above, user messages on right, AI messages on left
2. Input box and send button at bottom
3. Use Tailwind CSS to implement WeChat-like chat interface style
4. Messages must support Markdown rendering
```

This prompt states the interface layout and style requirements. AI will create a complete chat interface component.

The fourth step is to implement dialogue functionality:

```
Implement send message feature:
1. After user enters message, add to message list
2. Call API to get AI response
3. Use streaming output, display AI's answer word by word
4. Also send historical messages to API for multi-turn dialogue
5. Disable input box when loading, display "Thinking..."
```

This prompt includes all requirements for dialogue functionality. Streaming output is key — it makes AI's answers appear word by word like typing, greatly improving user experience. Multi-turn dialogue is also important — previous dialogue history must be sent to the API together so AI can remember what was said before.

The fifth step is to add data persistence:

```
Use LocalStorage to save dialogue history:
1. Auto-save after each dialogue update
2. Read history when page loads
3. Add "Clear Dialogue" button to clear history
```

This way, after users refresh the page, the previous dialogue is still there and won't be lost.

The sixth step is to optimize user experience:

```
Optimize user experience:
1. Auto-scroll to bottom when new messages appear
2. Add copy button for easily copying AI's answers
3. Code blocks must have syntax highlighting
4. Display friendly error prompts when API calls fail
```

Although these details are small, they can greatly improve user experience.



### Development Tips

During development, several techniques can make you more efficient. First, don't have AI implement all features at once — break it into multiple small steps and test after completing each step. This way, even if there are problems, it's easy to locate and fix.

Second, give AI enough context when talking. Clearly tell it what features to implement, what specific requirements, and what standards to follow. The clearer the context, the higher the quality of code AI generates.

If there are problems with the code, remember to send the complete error message to AI and let it help you analyze and fix. Don't just say "the code has an error," but paste the specific error message to it.



### Extension Ideas

After completing the basic version, you can continue to extend features.

For example, add system prompt settings to let AI play different roles (like programming assistant, writing assistant, psychological counselor, etc.); support managing multiple dialogue sessions to conduct multiple topic conversations simultaneously; add voice input feature to talk with AI using voice; integrate image recognition feature to let AI look at images and answer questions; support exporting dialogue records to save important dialogue content.



## III. Project Practice - Intelligent Writing Assistant

After mastering the basic AI dialogue process, let's make a more professional application — intelligent writing assistant. Writing assistant is one of the most practical AI application scenarios. Through this project, you can learn how to use prompt engineering to let AI complete different writing tasks.

This project supports multiple writing modes, like article continuation, content rewriting, copywriting generation, email writing, etc. Users can adjust parameters like creativity and output length to control AI's generation effect. They can also optimize text grammar and expression with one click, making text more professional. For easy selection, multiple versions can be generated at once, and users choose the most satisfactory one. Generated content is saved to history records for easy viewing and management.

![](https://pic.yupi.icu/1/demoweb7.png)

The tech stack is similar to the chat assistant, using React + TypeScript + Vite with Tailwind CSS. The core is still calling Zhipu AI API, with data saved in LocalStorage.



### Development Steps

1) Design Prompt Templates

The first step in development is designing prompt templates. Before writing code, first design prompt templates for different writing tasks. Create a `prompts.md` file to define prompts for various writing modes:

```markdown
# Writing Assistant Prompt Templates

## Article Continuation
Please continue writing the following article, keep style consistent, content coherent:
[User input content]

## Content Rewriting
Please rewrite the following content to make it more fluent and professional:
[User input content]

## Content Expansion
Please expand the following content, add more details and examples:
[User input content]

## Content Summary
Please summarize the following content, extract core points:
[User input content]

## Email Writing
Please write a [formal/friendly] email, topic is: [topic]

## Copywriting Generation
Please write a [style] style marketing copy for [product name]
```

Prompts are the core of AI applications — good prompts make AI generate better results. A good prompt usually contains 3 elements: clear task description, sufficient contextual information, clear output format requirements.

![](https://pic.yupi.icu/1/promptcompare%E5%A4%A7.jpeg)

For example, if you want AI to write an article, don't just say "help me write an article," but clearly state the topic, target audience, word count requirements, and what content to include. For example:

```markdown
Please write a popular science article about AI programming for zero-foundation readers, easy to understand with many examples, 800-1000 words, including what AI programming is, why learn it, and how to get started.
```

This way AI knows how to write.

If rewriting content, tell AI the background of the content. For example:

```markdown
This is the opening paragraph of a tech blog, please rewrite it to be more attractive while maintaining professionalism.
```

This way AI knows what direction to take the rewrite.

Specifying output format is also important. If you want AI to summarize an article, you can clearly require:

```markdown
Please summarize this article, output format:
1. Core points (3-5 points)
2. Key data (if any)
3. Conclusion (one sentence)
```

This way the generated result is more standardized and better meets your needs.

Sometimes, giving AI some examples works better. For example, if you want AI to write marketing copy, you can first give it a few examples to reference the style. This method is called Few-shot Learning and is effective in many scenarios.

2) Write Requirements Document

After designing prompt templates, you can write the requirements document. Create a `PRD.md` file:

```markdown
# Intelligent Writing Assistant PRD

## Core Features
1. Split layout, input on left, generated results on right
2. Support 6 writing modes: continue, rewrite, expand, summarize, email, copywriting
3. Can adjust creativity (temperature) and output length
4. Generated content displays in streaming fashion
5. Have "Optimize Prompt" button, AI helps user optimize description
6. Save generation history

## Interface Requirements
- Top: Large title
- Input area: Large text box (multi-line)
- Parameter area: Size selection, style selection
- Button area: Optimize prompt, generate content
- Display area: Display generated content + copy button
- Sidebar: History records
```

3) Talk with AI to Develop

With documents, you can talk with AI to develop.

First step, create basic interface:

```
Please create intelligent writing assistant interface according to PRD.md:
1. Split layout
2. Left side: Mode selection dropdown + input text box + generate button
3. Right side: Display generated content
4. Use Tailwind CSS, interface should be beautiful
```

Second step, implement prompt templates:

```
Create promptTemplates.ts file, according to templates in prompts.md, implement prompt functions for 6 writing modes. Each function receives user input and returns complete prompt.
```

This way the prompt logic is encapsulated, and different writing modes use different prompts.

Third step, implement generation feature:

```
Implement content generation feature:
1. User selects mode, enters content, clicks generate
2. Generate corresponding prompt based on selected mode
3. Call Zhipu AI API using streaming output
4. Display generated content in real-time on right side
5. Support Markdown rendering
```

Fourth step, add parameter adjustment:

```
Add advanced settings panel:
1. Creativity slider (temperature: 0-1)
2. Output length slider (max_tokens: 100-2000)
3. These parameters must be passed to API call
4. Can collapse/expand advanced settings
```

The temperature value affects the creativity of output.

- 0-0.3 is more conservative, suitable for factual content
- 0.4-0.7 is more balanced, suitable for most scenarios
- 0.8-1.0 is very creative, suitable for creative writing.

Fifth step, add history records:

```
Implement history records feature:
1. Save to LocalStorage after each generation
2. Save content: prompt, generated result, generation time
3. Left side displays history records list
4. Clicking history records lets you view previous content
5. Support deleting history records
```



### Prompt Optimization Tips

If you're not sure whether your prompt is good enough, you can have AI help you optimize. For example, you can ask:

```
I want AI to help me rewrite articles to make them more professional. My current prompt is: "Please rewrite this passage." Please help me optimize this prompt to generate better results from AI.
```

AI will give you a more detailed and effective prompt, like:

```markdown
This is the opening paragraph of a tech blog, please rewrite it to be more attractive while maintaining professionalism. Requirements:
1. Use more vivid language
2. Maintain technical accuracy
3. Word count around 200
```



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add more writing templates to support different types of writing like papers, reports, novels, etc.; support custom prompt templates to let users create their own templates; add multi-language translation feature to translate to other languages with one click; implement batch generation to generate multiple versions at once for selection; add text comparison feature to compare differences between different versions.



## IV. Project Practice - AI Image Generator

From text generation to image generation, let's make a cooler AI application. AI image generation is one of the coolest AI applications — with simple text descriptions, you can generate beautiful images. This project lets you learn how to call image generation APIs.

The core of this project is text-to-image generation. Users enter descriptions, select size and style, click generate and get images. To help users write better prompts, you can add an "Optimize Prompt" feature that lets AI help users expand simple descriptions into detailed prompts. Generated images are saved to history records and support downloading.

![](https://pic.yupi.icu/1/demoweb8.png)

The tech stack is similar to previous projects, mainly calling image generation APIs. Zhipu AI also provides image generation capability, and you can use the same API Key by [visiting the official site to get it](https://bigmodel.cn).



### Development Steps

1) Understand Image Generation API

The first step in development is understanding the image generation API. The main parameters of image generation APIs include:

- prompt: Image description (most important)
- size: Image dimensions (like 1024x1024)
- quality: Quality (standard or high definition)
- style: Style (realistic or artistic)

Different parameter combinations generate images with different effects.

2) Write Requirements Document

Then write the requirements document `PRD.md`:

```markdown
# AI Image Generator PRD

## Core Features
1. User enters image description, clicks generate
2. Can select image size and style
3. Show loading animation during generation (usually takes 10-30 seconds)
4. Display image after generation, can download
5. Have "Optimize Prompt" button, AI helps user optimize description
6. Save generation history

## Interface Requirements
- Top: Large title
- Input area: Large text box (multi-line)
- Parameter area: Size selection, style selection
- Button area: Optimize prompt, generate image
- Display area: Display generated image + download button
- Sidebar: History records
```

3) Talk with AI to Develop

With documents, you can talk with AI to develop.

First step, create basic interface:

```
Please create AI image generator interface according to PRD.md:
1. Input box: User enters image description
2. Parameter selection: Size (3 options), Style (2 options)
3. Two buttons: Optimize prompt, generate image
4. Image display area
Use Tailwind CSS, interface should be beautiful.
```

Second step, implement image generation feature:

```
Implement image generation feature:
1. Call Zhipu AI image generation API
2. Send prompt, size, style parameters
3. Show loading animation and prompt text during generation
4. Display image after successful generation
5. Show friendly prompt on error
```

Image generation usually takes 10-30 seconds, so loading prompts are important — let users know generation is in progress, not stuck.

Third step, implement prompt optimization feature:

```
Implement prompt optimization feature:
When user clicks "Optimize Prompt" button:
1. Send user's simple description to AI
2. Have AI expand into detailed image generation prompt
3. Prompt should include: subject, style, lighting, color, composition and other details
4. Fill optimized prompt back into input box
```

This feature is very practical and helps users who can't write prompts well generate better images.

Fourth step, add history records:

```
Implement history records feature:
1. Save to LocalStorage after each successful generation
2. Save content: prompt, image URL, generation time
3. Left side displays history records list (thumbnail + prompt)
4. Clicking history records lets you view large image
5. Support deleting history records
```

Fifth step, add download feature:

```
Implement image download feature:
When user clicks download button, download currently displayed image.
Filename format: ai-image-[timestamp].png
```



### Image Generation Prompt Tips

The quality of image generation largely depends on prompts. A good prompt usually includes these elements: subject (what to draw), action or state (what doing), environment background (where), style (what style), lighting (what light), color (what tone), quality words (high definition / 4K, etc.).

For example, if you want to generate an image of a cat, you can describe it like this:

```markdown
A cute orange cat sitting on a windowsill watching the rain outside, warm indoor lighting, soft tones, delicate fur texture, depth of field effect, high definition quality, 4K.
```

Such description includes all key elements, and the generated image quality will be better.

Regarding style, you can use some keywords to specify. For realistic style use photorealistic, realistic, detailed; for cartoon style use cartoon style, anime style, cute; for oil painting style use oil painting, artistic, impressionist; for watercolor style use watercolor, soft colors; for cyberpunk style use cyberpunk, neon lights, futuristic.

Quality words are also important, like high quality, detailed, 4K, 8K, professional, masterpiece, etc. — these words make AI generate more refined images.

If you're not sure how to write prompts, you can have AI help you. For example, if you want to generate an image with content being a programmer writing code in a coffee shop. You can tell AI:

```
I want to generate an image, content is: a programmer writing code in a coffee shop. Please help me expand this description into a detailed image generation prompt.
```

AI will give you a detailed description including scene, lighting, tone, composition and other aspects. For example:

```markdown
A young programmer sitting by the window in a cozy coffee shop, focused on writing code on a laptop, a steaming latte on the table, warm afternoon sunlight spilling onto the table through the window, blurred coffee shop background in the back, soft lighting, warm tones, cinematic composition, depth of field effect, high definition quality, professional photography.
```

💡 If using foreign AI image generation models, English prompts might work better.



### Cost Control Recommendations

Note that image generation is much more expensive than text generation, so pay attention to controlling costs. During development and testing, standard quality is enough — no need for high definition. Optimize prompts before generating to avoid wasting quota on repeated attempts. If budget is limited, consider using cheaper alternatives.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add image editing features to modify based on existing images; support batch generation to generate multiple images at once; add style presets to quickly select common styles; implement image zoom feature to view details; even add community sharing feature to let users share their generated images.



## V. Project Practice - Speech Recognition Application

Finally, let's make an AI application involving audio processing. Speech recognition lets your application support voice input, greatly improving user experience. This project lets you learn how to handle audio data and call speech recognition APIs.

This project implements voice recording and recognition features. Users click a button to start recording, click again to stop, then convert speech to text. It supports multiple languages, recognition results can be edited, and saved to history records.

![](https://pic.yupi.icu/1/demoweb9.png)

Recording functionality uses the browser's built-in MediaRecorder API — no additional libraries needed. Speech recognition calls Zhipu AI's speech recognition capability, [visit the official site to get API Key](https://bigmodel.cn/). Other tech stack is similar to previous projects.



### Development Steps

1) Understand Speech Recognition API

The first step in development is understanding the speech recognition API. Calling the speech recognition API is simple: upload audio file, specify language (optional), and return recognized text.

2) Write Requirements Document

Then write the requirements document `PRD.md`:

```markdown
# Speech Recognition Application PRD

## Core Features
1. Large recording button, click to start recording, click again to stop
2. Button turns red when recording, with animation effect
3. After stopping, show "Start Recognition" button
4. Show loading prompt during recognition
5. Display recognition results below, can be edited
6. Save recognition history

## Interface Requirements
- Simple single page
- Large circular recording button in center
- Recognition result area
- History records list at bottom
```

3) Talk with AI to Develop

With documents, you can talk with AI to develop.

First step, implement recording feature:

```
Please implement browser recording feature:
1. Use MediaRecorder API to record audio
2. Need to request microphone permission
3. Click button to start recording, click again to stop
4. Button turns red when recording, with pulse animation
5. Save audio data (Blob format) after stopping
```

This prompt states what technology to use and what features to implement. MediaRecorder API is a recording interface provided by the browser — no need to install additional libraries, very convenient.

Second step, implement speech recognition:

```
Implement speech recognition feature:
1. Call Zhipu AI speech recognition API
2. Upload recorded audio file
3. Specify language as Chinese
4. Display recognition results
5. Show friendly prompt on error
```

Third step, optimize interface and experience:

```
Optimize interface and user experience:
1. Recording button should be large and prominent (diameter 120px)
2. Recognition result area should support editing
3. Add copy button for easily copying recognition results
4. Show loading animation and prompt text during recognition
5. Overall use simple and modern design
```

Fourth step, add history records:

```
Implement history records feature:
1. Save to LocalStorage after each successful recognition
2. Save content: recognized text, timestamp
3. Bottom displays history records list
4. Clicking history records lets you view details
5. Support deleting history records
```



### Development Tips

During development, several techniques need attention. First is handling microphone permissions — on first use, the browser will ask the user whether to allow microphone access. If the user refuses, give a friendly prompt: "Microphone permission is needed for recording. Please allow microphone access in browser settings," and provide a button to request permission again.

Second is audio format processing. Audio recorded by MediaRecorder might be in webm format — most speech recognition APIs support this format. If not supported, you can have AI help you convert the format.

Third is recording duration limit. To avoid files being too large and recognition time too long, you can limit recording duration, like maximum 60 seconds. Show a countdown when recording, and automatically stop when time is reached. You can also display recording duration in real-time so users know how long they've recorded.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add voice translation feature to automatically translate to other languages after recognition; support real-time recognition, recognizing while speaking; add keyword extraction feature to automatically extract important information; support multi-person dialogue recognition to distinguish different speakers; add subtitle generation feature to generate subtitles for videos; even integrate into other applications like chat assistants to let chat assistants support voice input.



## In Conclusion

Through these 4 AI application projects, you've learned the basic process of AI application development: from simple chat assistants to professional writing assistants, from cool image generators to practical speech recognition applications. Each project lets you master different AI capabilities.

The barrier to AI application development is already very low — you don't need to understand complex machine learning algorithms, just need to know how to call APIs and design good prompts, and you can make very cool applications. If you want to learn more AI application development techniques and best practices, you can refer to the experience & techniques section of this tutorial.

After mastering AI application development, in the next article, I'll take you to challenge more complex full-stack application development, learning how to handle frontend, backend, and databases. Let's continue moving forward!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
