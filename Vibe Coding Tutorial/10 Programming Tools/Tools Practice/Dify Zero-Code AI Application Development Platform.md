# Dify: Zero-Code AI Application Development Platform

> Build your AI applications visually



Hello, I'm Fish Skin.

In previous articles, we learned about zero-code platforms where we can use Bolt.new and Baidu Miaoda to quickly generate websites and applications. But if you want to build AI applications, like intelligent customer service, knowledge base Q&A, AI assistants, what tool should you use?

In this article, I'll introduce **Dify**, a zero-code platform specifically for developing AI applications. Through visual methods, you can quickly build powerful AI applications without writing any code.

Let me walk you through using Dify with hands-on examples, while also explaining some core AI concepts along the way.



## I. What is Dify?

[Dify](https://dify.ai/) is an open-source AI application development platform that lets you build AI applications visually.

What's the difference between it and Bolt.new?

Bolt.new is mainly used to generate ordinary websites and applications, like personal homepages, e-commerce sites, etc. While Dify focuses on AI applications, such as:

- Intelligent customer service bots
- Knowledge base Q&A systems
- AI writing assistants
- Document analysis tools
- AI workflow automation

Dify provides a visual configuration interface where you can build AI workflows by dragging and dropping, configure large models, set prompts, add knowledge bases, etc., creating powerful AI applications without writing code.

![](https://pic.yupi.icu/1/853427c8123decb5ea3d163ae3bb8ab635d95e92f7ee14a2e51e54df06e94fd8.png)



## II. Getting Started with Dify

Let me walk you through quickly getting started with Dify through a practical example.



### 1. Create an AI Application

First enter [Dify Platform](https://dify.ai/), register an account and log in. Then create an AI application and enter the AI conversation interface.

![](https://pic.yupi.icu/1/1743560753186-1e9452e6-0d38-4070-b369-c674bc418c91.png)



### 2. Choose a Large Model

When using for the first time, we need to select a **Large Model (LLM)**.

**The large model is the brain of AI**, referring to artificial intelligence models with massive parameters that gain broad knowledge and capabilities through large-scale pre-training.

![](https://pic.yupi.icu/1/1743560803824-ab33d9d9-e994-45e5-8190-fc104e679747.png)

Different large models have different parameter scales, processing capabilities, and accepted conversation lengths. For example, Claude Opus 4.5 has strong programming capabilities, Gemini 3 Pro supports ultra-long context, and DeepSeek is completely free.

![](https://pic.yupi.icu/1/1743560841202-c37cde5b-0b25-4ebb-adff-3ab66af35d75.png)

After selecting a large model, we can set parameters to adjust the model's output. For example, **Temperature** can control the randomness of the model's output:

- Higher temperature value, model output is more random and diverse (suitable for creative writing)
- Lower temperature value, output is more deterministic and conservative (suitable for professional Q&A)

![](https://pic.yupi.icu/1/1743560855583-7efaebb7-3552-4a5b-9787-adbb9acaddc6.png)



### 3. Set Prompts

Now let's converse with AI. The content we input to AI is called **Prompt**, used to guide the model to generate specific content or perform specific tasks.

The quality of the prompt directly determines the accuracy of AI's output. Prompts can be divided into two types:

- System Prompt: Overall constraint on AI's output content, needs to be set in advance
- User Prompt: Content input by users, entered as needed

![](https://pic.yupi.icu/1/1743560920031-d86572e4-b09e-46b4-8aa8-c734a96bec44.png)

For example, if I want to make a programming assistant, I can set in the system prompt:

```
You are a professional programming assistant, skilled in Python, JavaScript, Java and other languages.
When answering questions, be concise and clear, and provide code examples.
```

Then users can directly ask: "How do I read files with Python?"



### 4. Understanding Token

After a conversation, we'll see "Tokens Spent" displayed below the conversation.

![](https://pic.yupi.icu/1/1743561058442-beebd2ac-94a0-4f00-8e56-f819822247e1.png)

Seeing "spent" makes many students nervous. What is Token? Is Token expensive?

**Token is the basic unit for large language models to process text**, which could be a word or punctuation mark. Both model input and output are calculated by Token. Generally, the more Tokens, the higher the cost and the slower the output speed.

Different models have different billing, generally 1 million Tokens costs tens of yuan. You can estimate costs through some online Token calculation tools.

![](https://pic.yupi.icu/1/1743561097206-472514a9-3d13-4408-b222-2207b00f611a.png)

But don't worry too much, for daily use, the cost won't be very high. And many platforms have free quotas.



### 5. Add Knowledge Base (RAG)

Sometimes, large models may lack certain information. For example, asking AI to summarize [Fish Skin's "Nanny-Level Resume Writing Guide"](https://www.codefather.cn/course/cv), the information it gives is inaccurate because it hasn't read this article.

At this time we can enable the knowledge base feature, behind which is **RAG (Retrieval Augmented Generation)** technology, to use external knowledge bases to supplement AI with knowledge.

![](https://pic.yupi.icu/1/1743561648847-337df359-2e2a-4e05-bec6-dfff52b3be1d.png)

First create a knowledge base and upload knowledge documents:

![](https://pic.yupi.icu/1/1743561783744-1ddce7bb-802e-4feb-9e8f-7e0a83b4ad98.png)

Then split the text, you can set chunking rules yourself:

![](https://pic.yupi.icu/1/1743561816205-22494e52-c011-49fe-8537-3b7f0f441a51.png)

Next, use **Embedding** technology to convert text into vector representations and write them into a vector database.

When users ask AI questions, the question is converted into a vector, relevant information is retrieved from the knowledge base, and then this information and the question are input into the large model together for processing, making the large model's answers more accurate.

![](https://pic.yupi.icu/1/1743561872916-7971c368-14bd-49c2-9bd9-604973f469e3.png)

This way, AI can answer questions based on the knowledge base you provided.



### 6. Publish and Call

Okay, our AI application is done. It can be published for others to use, or can be called through **API interface** in your own code programs via network requests.

![](https://pic.yupi.icu/1/1743561915955-ad27735a-c927-4207-b769-03fda32081b6.png)



## III. AI Agents and Workflows

We just made a simple chat assistant. But actually, Dify supports more powerful features — **AI Agents**.

An agent is an AI system capable of perceiving environment, reasoning, planning, making decisions and autonomously taking actions to achieve goals.

![](https://pic.yupi.icu/1/1743561972671-9c7ad13e-a467-4a08-ba14-711d4640939c.png)

We can provide **tools** to agents, such as web search, weather query, database access, etc., letting agents complete more complex tasks.

After installing tools and providing them to agents, they will use these tools when needed. For example, retrieving content from the web, summarizing it, then replying. This way, the scope of application and capability boundaries of AI will be unlimited.

![](https://pic.yupi.icu/1/1743562005435-e5ece3f2-5f4b-4729-b490-a1e51f1f006e.png)

Of course, if the AI large model you use isn't smart enough, it might not use tools. So I suggest choosing reasoning models with stronger thinking capabilities for agents.

Some models use **Chain of Thought (CoT)** and **ReAct** techniques, letting the model first think about the problem, reason and analyze, propose an action plan, then act, then further reason based on results. And the intermediate steps and thinking process are publicly visible, allowing us to understand how the model reached its conclusion.

![](https://pic.yupi.icu/1/1743562152661-80fabf5f-07a4-4463-a980-67da980f0ede.png)

Sometimes, a single agent can't complete our tasks, like automatically generating 100 short videos, or automatically making a game and publishing it online.

At this time we can use **Agent Workflows** (Agentic Workflow), which can through planning and orchestration, let agents freely combine functions to automatically implement various complex tasks. A bit like visual programming.

![](https://pic.yupi.icu/1/1743562195750-57a3b344-4282-4279-bd71-510f60fc17c6.png)



## IV. MCP Service Integration

Finally, let me share a very hot concept called **MCP (Model Context Protocol)**, used to implement standardized interaction between AI and external tools or data.

![](https://pic.yupi.icu/1/1743562215479-a19f8b1c-0190-41b4-8a2f-f508b24e74a7.png)

Simply put, using MCP services, we can more conveniently integrate different tools and data for AI, enhancing AI application functionality.

First install MCP Agent strategy to let agents support calling MCP:

![](https://pic.yupi.icu/1/1743562275496-34bcb486-235d-4d97-bc5a-cdf00f59cff7.png)

Then go to [MCP Collection website](https://mcp.so/) to find the MCP service we need, like querying current time.

![](https://pic.yupi.icu/1/1743562325916-dbef66dc-d0d1-4a60-9bed-68691c462677.png)

Then return to the agent workflow, fill in MCP server address, MCP call commands and query conditions, etc., and AI can send requests to MCP to get data when needed.

![](https://pic.yupi.icu/1/1743562400230-79c99317-98f1-4579-8884-a5bf53623683.png)



## V. Other AI Application Development Platforms

Besides Dify, there are some other AI application development platforms worth knowing about.



### Coze

[Coze](https://www.coze.com/) is an AI application development platform launched by ByteDance, providing lots of plugins to facilitate application development.

Coze's advantages are zero-code, visual workflows, and it provides many pre-built plugins and templates, quick to get started. Suitable for individuals and lightweight applications.



### Alibaba Cloud Bailian

[Alibaba Cloud Bailian](https://bailian.console.aliyun.com/) is an enterprise-level AI application development platform, supporting RAG knowledge bases, process orchestration, and other functions.

Bailian's advantage is enterprise-level capabilities, providing visual process orchestration features, allowing you to build complex AI workflows without writing code. And it's deeply integrated with other Alibaba Cloud services, suitable for enterprise users.



### How to Choose?

If you're an individual developer or don't have programming background and want to quickly make an AI application, both Dify and Coze are good choices.

If you're an enterprise user or Java developer needing stronger stability and enterprise-level features, you can consider Alibaba Cloud Bailian.

I mainly use Alibaba Cloud Bailian myself. After all, as a full-stack programmer focused on Java backend, Alibaba's position in China's Java ecosystem is unshakable. Their Spring AI Alibaba framework has higher integration with their own AI, allowing quick development of complete AI applications.



## VI. Dify Practical Tips

During the process of using Dify, I've summarized some practical tips.

1. Choose the right large model

Different tasks are suitable for different models. If it's creative writing, you can choose GPT-4 or Claude; if it's code generation, Claude's programming ability is stronger; if budget is limited, you can choose DeepSeek or Gemini Flash.

2. Optimize prompts

The quality of prompts directly affects AI output. Suggestions:

- Clearly define role positioning (like "You are a professional...")
- Clearly state task requirements
- Provide specific examples
- Set output format

3. Make good use of knowledge base

If your AI application needs to answer questions based on specific knowledge, definitely use the knowledge base feature. Upload relevant documents and materials to the knowledge base, and AI's answers will be much more accurate.

4. Test and iterate

After making an AI application, definitely test it more. Try various different questions to see if AI's answers meet expectations. If you find problems, adjust prompts or knowledge base, constantly iterate and optimize.

5. Utilize workflows

For complex tasks, you can use the workflow feature. Break the task into multiple steps, each step completes a small task, finally combine them. This is easier to control and debug.



## In Conclusion

Seeing this, I believe you already have a basic understanding of Dify and AI application development.

**Making AI applications with Dify is really simple.** No need to write code, just configure a bit, and you can make powerful AI applications.

And in the process of using Dify, you'll also gradually understand AI's core concepts, like large models, prompts, Token, RAG, agents, etc. These concepts are not only useful in Dify, but also universal in other AI tools.

I suggest you next personally try making a simple AI application with Dify, like a programming Q&A assistant, a document summarization tool, or a knowledge base Q&A system, and slowly you'll discover the fun of AI application development.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
