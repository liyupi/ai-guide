# AI Programming Technology Introduction Guide

> Master AI development frameworks, become the talent companies fight for



Hello, I'm Fish Skin the programmer.

As programmers, we not only need to be able to use AI tools and utilize AI to develop projects, but also be able to independently develop AI projects and integrate AI capabilities into our own projects.

As the saying goes: **In the AI era, all traditional businesses are worth reshaping with AI.**

So now many companies are recruiting programmers who can develop AI projects - this is our opportunity. So what knowledge and technologies do we need to learn to become the talent companies fight for?

⭐️ Recommend watching video version: https://www.bilibili.com/video/BV1i9Z8YhEja



## I. AI Development Frameworks

First from a technical perspective, we need to learn mainstream AI development frameworks. Currently the hottest in the Java direction are **Spring AI** and **LangChain4j**.



### Spring AI

[Spring AI](https://docs.spring.io/spring-ai/reference/getting-started.html) is the official AI development framework from Spring, after 2 years of accumulation, officially released version 1.0 in May 2025.

![Spring AI 1.0 Release](https://pic.yupi.icu/1/1747881171718-91ac3eb5-049b-4510-8012-6736c40c9c95.png)

The advantage of Spring AI is **easier integration with mainstream Java development framework Spring**, lower learning curve. It provides many ready-made methods to help us improve efficiency in developing AI applications, like quickly connecting to large models, saving conversation context, connecting to vector databases to implement RAG, etc.

![Spring AI Architecture](https://pic.yupi.icu/1/1743563460857-95800757-867c-4e8a-ba7c-dd490d09fcbd.png)

Spring AI's core features include:

- Large model invocation capability: unified interface supporting multiple mainstream large models (OpenAI, Claude, Tongyi Qianwen, etc.)
- Prompt engineering: provides Prompt and PromptTemplate classes for convenient prompt management
- Conversation memory: one line of code enables conversation memory, automatically handles context
- RAG retrieval augmented generation: complete RAG process support, including document loading, vector storage, retrieval optimization
- Tool calling: quickly define tools through annotations, letting AI call external services
- MCP support: easily access and develop MCP services

For example, using Spring AI to call a large model only requires a few lines of code:

```java
// Use Spring AI to call large model
@Bean
public ChatClient chatClient(ChatModel chatModel) {
    return ChatClient.builder(chatModel).build();
}

public String doChat(String message) {
    return chatClient.prompt(message).call().content();
}
```

Without Spring AI, you'd need to write HTTP requests and parse responses yourself, much more troublesome.



### Spring AI Alibaba

[Spring AI Alibaba](https://java2ai.com/) is Alibaba's domestic version based on Spring AI, specially optimized for the domestic AI ecosystem.

Its advantages include:

- Better support for domestic large models (Tongyi Qianwen, Baidu Wenxin Yiyan, etc.)
- Provides Chinese documentation and technical support
- Optimized for domestic network environment
- Has Alibaba Cloud's ecosystem support

If you mainly use domestic AI services, Spring AI Alibaba is the better choice.



### LangChain4j

[LangChain4j](https://docs.langchain4j.dev/intro) is another mainstream Java AI development framework, characterized by **more flexible, better suited for developing complex agents**.

For example, when developing an intelligent document analysis system, using LangChain4j, the agent can automatically read document content, call search engines to get relevant background knowledge, then based on task requirements, combine document information with external knowledge to generate analysis reports.

LangChain4j's core features include:

- AI Service: declarative development, quickly build AI services through annotations
- Conversation memory: supports multiple conversation memory strategies and persistence
- Structured output: automatically converts AI output to Java objects
- RAG support: complete RAG process, supports multiple vector databases
- Tool calling: flexible tool definition and invocation mechanism
- Guardrails: input/output interceptors, enhanced security

For example, using LangChain4j's AI Service:

```java
@AiService
public interface AiCodeHelperService {
    @SystemMessage(fromResource = "system-prompt.txt")
    String chat(String userMessage);
}
```

Only need to define the interface and annotations, the framework automatically generates the implementation class, very convenient.



### How to Choose a Framework?

| Scenario       | Recommended Framework    | Advantages                      |
| -------------- | ----------------------- | ------------------------------- |
| Java enterprise apps | Spring AI            | Seamless integration with Spring ecosystem |
| Domestic AI services | Spring AI Alibaba    | Better support for domestic large models |
| Agent development    | LangChain4j          | Complete Agent toolchain         |
| Complex workflows    | LangGraph (advanced) | Visual orchestration              |

My suggestion is **learn both, start with Spring AI, then learn LangChain4j which will be simpler**. Many concepts and usages are similar, learn one and you can quickly pick up the other.



## II. AI Integration

The prerequisite for developing AI applications is having access to large models, but large models need computing power to run, and computing power is money. Where do we get large models from?

There are 2 methods: use AI cloud services, or deploy large models locally.



### AI Cloud Services

AI cloud services are when other companies deploy AI large models for us and provide them through API interfaces, charging by usage.

For example Alibaba Cloud Bailian, Volcano Engine, SiliconFlow, OpenAI, etc.

![AI Cloud Services](https://pic.yupi.icu/1/1743563631799-46ff94d5-d51b-4dc5-b6cf-dec28bdcdb39.png)

As programmers, what we need to master is:

1. How to access cloud services through API?
2. How to use AI cloud services to create agents and configure parameters?
3. How to choose the right cloud service? This requires关注各家云服务的计费模式和服务质量
4. How to use cloud services at lower cost and more stably? This requires learning Prompt engineering and high availability technology



### Local Large Model Deployment

Local deployment of large models is also a necessity for many enterprises, data doesn't need to be uploaded to the cloud, effectively ensuring data security and privacy, especially suitable for industries like healthcare and finance that are extremely sensitive to data security.

Local deployment of large models isn't actually difficult, just need to use the [Ollama tool](https://ollama.com/) to deploy various mainstream open-source models with one click.

![Ollama](https://pic.yupi.icu/1/1743563719547-bbed1c54-d1f1-496f-afc2-d755c3538732.png)

But actually, the difficulty of deploying large models isn't the technology, it's mainly the lack of computing power! Otherwise I'd also give our team's [Programming Navigation](https://codefather.cn) and [Interview Duck](https://www.mianshiya.com) a Fish Skin large model each.



## III. AI Domain Business

AI business development in enterprises isn't just about having an AI chat, we also need to master several more complex business developments, like RAG knowledge bases, multimodal, MCP services, ReAct agents.



### RAG Knowledge Base

Many companies have their own business knowledge and documents, will build their own Q&A systems or customer service, this requires using RAG retrieval augmented generation technology.

First through text embedding models, convert enterprise documents into vectors, store in vector database; when users ask questions, the system retrieves relevant vector data in the vector database, finds the most similar document fragments, and inputs them with the question into the large model for processing. This way, the large model can answer based on enterprise real data, more accurately fitting reality.

![RAG Process](https://pic.yupi.icu/1/1743563751814-4123230c-c4b8-458f-bf8b-070c7550dd54.png)

There's so much to learn about RAG, like mainstream vector databases Milvus and PGVector, document extraction/conversion/loading, index building, query strategy optimization, etc. **This is also a focus of AI enterprise interviews!**



### Multimodal

Multimodal is also a mainstream AI business scenario, integrating text, images, audio, video and other different types of data modalities, thereby improving product ease of use and creating more creative features.

For example, making an intelligent shopping guide system, customers can input text descriptions of desired products, the system can also recognize product images uploaded by customers, and even understand shopping needs raised by customers through voice.

![Multimodal](https://pic.yupi.icu/1/1743563981663-8c9f4746-03dc-4b32-8477-ba9a9042922c.png)

To develop multimodal applications, we need to learn modality conversion technologies, like text-to-speech (TTS), speech-to-text (STT), optical character recognition (OCR), etc. However, these all have ready-made tool libraries or cloud services, just need to master the calling methods.



### MCP Services

MCP (Model Context Protocol, Model Context Protocol) can be understood as various services provided to AI, AI using these services can achieve more powerful functionality.

![MCP](https://pic.yupi.icu/1/1743563832927-7a2df71f-acc1-47c4-9135-e7d888749dbc.png)

How to integrate others' MCP services in your project to enhance your project's capabilities; and how to develop your own MCP services for others' projects to use, are both must-learn.

Now using development frameworks like Spring AI can develop MCP services, and there's even a master who made a [website](http://mcpify.ai/) that can create your own MCP service in one sentence, this is truly too cool.

![MCP Generation](https://pic.yupi.icu/1/1743563865750-bbd02b74-2a56-49a9-963f-e633c1484fe5.png)



### ReAct Agents

ReAct is a development paradigm for building agents, aimed at creating agents that can autonomously take action based on reasoning results.

The development process involves knowledge of task planning, tool calling, interaction I/O, exception handling, etc. Especially tool calling, which through Function Call or MCP can implement functions like weather queries, file reading and writing, webpage running, information retrieval, terminal command execution, etc.

![ReAct Agent](https://pic.yupi.icu/1/1743563922663-0096045d-8a99-4202-b30d-df77a341e697.png)

Take developing a video website for example, when the user gives the command "help me develop a Dilidili video website and deploy it online", the agent will first deeply understand the task content, through reasoning organize a series of execution steps, including clarifying requirements, designing solutions, building frameworks, generating code, deploying online, etc. Next, the agent will call corresponding tools to execute these actions.

![Agent Workflow](https://pic.yupi.icu/1/1743564028474-638e6414-9a22-4350-80f3-7bf174dd0f77.png)



## IV. AI Toolchain

Finally, some platforms, tools and libraries we might use when developing AI projects.



### Low-Code Platforms

For example, the mainstream low-code AI development platform [Dify](https://dify.ai/), which lets us build our own AI agents through drag-and-drop, create knowledge bases and import our documents, build complex workflows, etc. Even if you can't write code, you can use it to create complex AI applications.

![Dify](https://pic.yupi.icu/1/1743564064922-03f6365b-a712-47d9-be55-4867b848a269.png)



### Tool Libraries

There are also some tool libraries used when developing AI agents, like:

- Apache Tika: powerful file parser tool library, supports parsing PDF, Word, Excel, PowerPoint and other documents
- Playwright: tool library for simulating browser behavior, useful when AI needs to run webpages, scrape webpage data, automated testing
- JSON format parsing libraries: GSON and Kryo
- HTML document parsing library: jsoup

These libraries basically have no learning cost, just check the documentation when you need to use them.



### Deployment Tools

Projects ultimately need to be deployed online, so we also need to master efficient deployment tools. If for personal learning use, want to quickly launch your own AI small app, can try these platforms:

- [Vercel](https://vercel.com/): deployment platform suitable for frontend applications, supports automatic builds, online browsing, CDN distribution, and also provides free accessible domains
- [Sealos](https://sealos.io/): cloud-native application management platform, supports Kubernetes cluster management
- [Railway](https://railway.com/): lets developers easily deploy Docker containers, no need to worry about server configuration and operations

Of course, to quickly deploy services, Docker containerization technology is also a must-learn, just like an APP installation package, can easily distribute and deploy your applications.

![Docker](https://pic.yupi.icu/1/1743564338228-ffc55f7b-7bcd-40df-a10b-4accfb666379.png)



## V. Learning Resource Recommendations

Quite a lot to learn, right? Don't worry, I'm also continuously learning these contents and will continuously share with everyone.



### 1. AI Learning Roadmap

Complete AI large model application development learning roadmap can be [obtained from Programming Navigation](https://www.codefather.cn/course/1789189862986850306/section/1912024009574629377):

Website: https://www.codefather.cn/learn

![AI Learning Roadmap](https://pic.yupi.icu/1/image-20250912152042459.png)



### 2. AI Project Practice

On [Programming Navigation](https://www.codefather.cn), I've led everyone through multiple sets of AI project tutorials, covering almost all technologies mentioned above:

- AI Programming Assistant: LangChain4j framework introduction, practical conversation memory, structured output, RAG, tool calling, MCP, SSE, etc.
- AI Super Agent: Spring AI framework introduction, practical AI Love Master application + super agent with autonomous planning capability
- AI Zero-Code Application Generation Platform: LangChain4j AI agent, LangGraph4j workflow, microservices architecture
- AI Question-Answering Application Platform: React cross-platform mini program, Vue3 AI application, database sharding, SSE real-time push

These projects are all enterprise-level real projects, can be directly written into resumes after completion.



### 3. Open Source Projects

I've also open-sourced many AI application development projects to share with everyone:

- AI Application Generation Platform: https://github.com/liyupi/yu-ai-code-mother
- AI Super Agent: https://github.com/liyupi/yu-ai-agent
- AI Literature Reading Assistant: https://github.com/liyupi/literature-assistant
- AI Knowledge Base: https://github.com/liyupi/ai-guide



### 4. AI Knowledge Base

In my free open-source [AI Knowledge Base](https://github.com/liyupi/ai-guide), I've collected and summarized the latest and most comprehensive AI knowledge, helping everyone better adapt to the arrival of the AI era.

Website: https://ai.codefather.cn

![](https://pic.yupi.icu/1/image-20260109121412266.png)

Besides various tutorial materials, I also focus on sharing many specific application scenarios of AI tools, like integrating office software to improve efficiency, helping you do self-media, AI batch video production, etc., hope to help everyone draw inferences and find new ideas.



## In Conclusion

AI technology is changing with each passing day, and requirements for programmers are constantly increasing. **AI-related knowledge is no longer just for algorithm engineers to understand, but a basic skill every programmer must master.**

Whether you're a frontend, backend, or full-stack developer, you need to understand the basic concepts and practical methods of AI application development.

Because in future software development, AI will be everywhere.

If you ask me, will AI eliminate programmers?

My answer is still "yes". Because programmers themselves need continuous learning and practice to maintain competitiveness. As long as everyone can learn the knowledge I mentioned, pay more attention to AI frontier news, I believe AI won't steal programmers' jobs, but become the lever for us to transform the world.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
