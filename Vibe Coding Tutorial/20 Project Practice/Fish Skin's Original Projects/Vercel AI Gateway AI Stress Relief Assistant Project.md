# Vercel AI Gateway - AI Stress Relief Assistant Project Practice

The focus of this article is not on development, but on learning AI Gateway concepts and usage methods. Through comic-style explanations and Vibe Coding project practice, you can understand how to flexibly switch between different AI models in AI applications through Vercel AI Gateway, reducing development costs and maintenance complexity. Suitable for students who want to learn AI Gateway technology and need to quickly integrate multiple AI models.



---

You are Xiao Aba, a newly hired AI application development engineer.

![](https://pic.yupi.icu/1/1761152281564-61073333-da43-4ac2-b6ca-09460e87331a.png)

The crappy boss says: The company plans to build an intelligent customer service system recently. Xiao Aba, you're new, so this important task is entrusted to you! As the saying goes: Heaven bestows great responsibilities on newcomers~

![](https://pic.yupi.icu/1/1761645372915-7d9df0cf-f44a-4643-8d67-3e7103fb03db.png)

You think to yourself: Isn't this just calling an API? What's so hard about it?

So you roll up your sleeves and start writing code, first integrating OpenAI's GPT model.

Just as you finish, the crappy boss says: Also add the Claude model, I heard it performs better in some scenarios.

So you write another bunch of code to call the Claude model.

The moment you finish, the crappy boss says again: Hmm, I've heard the domestic Tongyi Qianwen is also quite good, integrate that too!

![](https://pic.yupi.icu/1/1761645406716-99acb82f-2f1f-4a62-a3c6-076ac17b1e6d.png)

You frown and think: I have to write code to call this model too. Boss, aren't you being a bit excessive...

The crappy boss seems to hear your thoughts:

- Oh right, calling AI has costs, need to implement user authentication
- Oh oh, to prevent malicious users from frantically calling AI, also need rate limiting
- Oh oh oh, AI-generated content might have issues, need content safety validation
- Oh oh oh oh! Also need to ensure system stability, can't have one model being down cause the entire service to fail
- Oh oh oh oh oh! This project will definitely be popular, need to consider how AI can handle large volumes of requests
- Oh oh oh oh oh oh! Also need to observe AI call counts and costs for cost reduction and efficiency improvement
- Oh oh oh oh oh oh oh...

You watch the boss gradually go mad and start doubting life: How can calling an AI interface be so complex?

![](https://pic.yupi.icu/1/1761645432489-6e2f67db-40f5-40fe-a6f0-c18ead6e6d8a.png)



⭐️ Video version: [https://bilibili.com/video/BV14NyrBTEeB](https://www.bilibili.com/video/BV14NyrBTEeB)



## What is an AI Gateway?

Just then, Fish Skin, known as the "AI Prince," walks over. Seeing your distressed expression, he laughs: What's wrong, is this so hard?

You're a bit annoyed: You're talking without feeling the pain. With so many requirements, won't I have to write a huge chunk of code?

Fish Skin: All these scenarios the boss mentioned can be solved through **AI Gateway**~

You ask curiously: Gateway? What's that?

Fish Skin: A gateway is like the ticket checkpoint at a train station. All passengers must first pass through the checkpoint, where the ticket inspector checks your ticket and then directs you to the correct platform.

![](https://pic.yupi.icu/1/1761645506547-26d820e6-cda3-482e-a7e9-dcadcbbb0445.png)

In system architecture, requests sent by frontend users first pass through the gateway. The gateway uniformly handles user authentication, intercepts malicious requests, controls traffic, monitors and counts requests, etc., then forwards requests to backend servers for processing.

![](https://pic.yupi.icu/1/1761645542774-a2da29dc-3d2c-4e1b-adcf-dc5dd59d0881.png)

You nod: Wow, so if I have multiple backend services, I don't need to write these functions separately for each service.

Fish Skin: Exactly, and if one backend service goes down, the gateway can automatically forward requests to other services.

![](https://pic.yupi.icu/1/1761645571947-8cb4a141-7d6f-4add-a82b-7a70716f23e7.png)

You're curious: Then what's the AI Gateway you just mentioned?

Fish Skin: Traditional API gateways are usually placed between your application and various backend services; while AI Gateway is specifically designed for AI applications, placed between your application and various AI model services (like OpenAI, Tongyi Qianwen, DeepSeek, etc.).

![](https://pic.yupi.icu/1/1761645615469-787296d8-1fb6-4452-b406-c79ef537f193.png)

Your application only needs to send **standard requests** to the AI Gateway, and it will automatically help you complete a series of complex operations like user authentication, rate limiting, security protection, failover, load balancing, monitoring and statistics, and forward requests to AI large models for processing.

![](https://pic.yupi.icu/1/1761645642401-683e786e-3e06-420a-abce-cd43f7bfa901.png)

If you need to integrate different large models, you only need to modify the large model name in the standard request. The AI Gateway will handle routing for you, no need to write a separate set of integration code for each model~

![](https://pic.yupi.icu/1/1761645657980-b463d0b2-eecd-4635-99ee-fed9f121bf4e.png)

You cheer: This is too powerful! With AI Gateway, all the problems the boss mentioned can be solved! So what AI Gateway products are available now?

![](https://pic.yupi.icu/1/1761645679096-3ceb73df-a858-4410-abc1-041222b497f4.png)



## AI Gateway Selection

Many AI players' first exposure to AI Gateway might be [OpenRouter](https://openrouter.ai/). It's more like an AI model aggregation platform, supporting integration with hundreds of models through a unified interface.

![](https://pic.yupi.icu/1/1761645719834-eadcde16-711c-474c-9838-5ea5f01be452.png)

Many AI tools support configuring OpenRouter. For ordinary AI users, through it you can use more large models and more stable services.

![](https://pic.yupi.icu/1/1761645743475-53493cb1-5be9-4b0b-8b9a-a497ac13d7c7.png)



You ask: Are there AI Gateway products specifically for developers?

Fish Skin nods: Of course, there are already quite a few mature AI Gateway products on the market. For example, if you search online, the top-ranked ones are:

1) [Vercel AI Gateway](https://vercel.com/ai-gateway): This is a recently popular new product. Its biggest feature is easy to get started, and **zero additional cost** — if you use your own API Key, the gateway itself doesn't charge extra. Suitable for frontend developers to quickly build full-stack AI applications.

2) [Cloudflare AI Gateway](https://www.cloudflare.com/zh-cn/developer-platform/products/ai-gateway/): As one of the world's largest CDN service providers, Cloudflare's AI Gateway main advantage is wide global node coverage and strong security protection capabilities.

3) [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway): Kong itself is a very mature API Gateway, now specifically enhanced for AI scenarios, with relatively complete enterprise-level features.

![](https://pic.yupi.icu/1/image-20251018111819481.png)

4) [Higress AI](https://higress.ai/): Alibaba Cloud's open-source AI Gateway, supporting unified protocol conversion for 100+ large models, providing enterprise-level features like semantic caching, token rate limiting, MCP transformation, etc. Suitable for enterprises with complex AI integration needs.

![](https://pic.yupi.icu/1/image-20251019163817976-20251028181254777.png)



You scratch your head: This looks too complex. How should I get started with AI Gateway?

Fish Skin: Don't worry, we can start learning with the relatively simple Vercel AI Gateway. Talk is cheap, give me 2 minutes, and I'll take you through mastering Vercel AI Gateway usage in practice~



## Vercel AI Gateway Practice

#### 1. Register and Get API Key

First open [Vercel official website](https://vercel.com/) to register an account. Binding a credit card gives you $5 free usage credits, enough for learning and testing.

![](https://pic.yupi.icu/1/1760687990497-90720fbb-0df6-4ede-87b8-64b8702994e9-20251028181254840.png)



Then create an API Key in the console. Be careful not to leak it:

![](https://pic.yupi.icu/1/1760688078133-7b91b6f3-2fc4-4bb4-b2c1-d517699f0968-20251028181254879.png)



#### 2. Official Demo

Next, you can use the official quick start tutorial to create a project and run an AI chat Demo:

![](https://pic.yupi.icu/1/image-20251019160232722.png)



Simply put, 4 steps:

1. Create new project
2. Install AI SDK and AI Gateway dependency packages
3. Configure environment variables, fill in API Key configuration
4. Write example Demo code



#### 3. Stress Relief Assistant Project

But the official Demo is a bit too simple. We might as well use AI to build a "Stress Relief Assistant" website project, where users can chat with an AI specifically designed to help relieve stress.

Here I chose Cursor as my AI development tool, directly letting AI help me generate complete frontend + backend code that meets requirements.

![](https://pic.yupi.icu/1/1761645829262-bd9950ef-6334-410f-ab27-140873cb56a4.png)

Since Vercel AI Gateway is relatively new, AI might not understand its usage. So I directly threw Vercel AI Gateway's official documentation to Cursor, letting it learn usage through the documentation.

![](https://pic.yupi.icu/1/1761645854330-54b6ab38-7f1f-45a5-ac34-463ee63477a7.png)



Complete prompt as follows:

```markdown
You are a professional programmer. Please help me develop the "Stress Relief Assistant" website, where users can relieve stress by chatting with an AI specifically designed to help people relieve stress.

## Development Requirements

1. Need to include complete frontend and backend, backend using Node.js
2. Use Vercel's AI Gateway to implement AI capabilities, first get as much usage as possible through official documentation: https://vercel.com/docs/ai-gateway/getting-started
3. Focus on completing core functionality, ensure project can run normally, don't output documentation, don't do any extra features
4. Overall website interface uses relaxing light colors, responsive to adapt to various device sizes
```



After clicking execute, AI will first call MCP tool to get information from the webpage. Here I used `Firecrawl MCP`:

![](https://pic.yupi.icu/1/1760690503357-7412db47-4389-49e2-b42c-dc6eabdc283b-20251028181255024.png)



About 6 minutes later, AI completed generating all the code. Unfortunately AI wasn't very obedient here, still generated a bunch of documentation, taking more time than generating the code itself!

![](https://pic.yupi.icu/1/image-20251019161322770.png)



Then create `.env` environment variable configuration file in root directory, fill in AI Gateway's API Key:

![](https://pic.yupi.icu/1/1760689844332-79459841-46e3-4356-9fe7-76062a90464c-20251028181255097.png)



Finally, install dependencies and execute startup script:

![](https://pic.yupi.icu/1/1760690024471-f89bf1e3-3d9e-4857-8a68-a236ffa0af14-20251028181255125.png)



Visit `localhost:3000` to see the project:

![](https://pic.yupi.icu/1/1760690223277-56f89c2a-b4c5-43d6-a61d-3f744bcd9aef-20251028181255161.png)



Honestly, the effect is really good, gave me a bit more motivation to write a few more words haha:

![](https://pic.yupi.icu/1/1760690245830-e877986b-1bb6-4c6a-96ad-92b738a57fed-20251028181255188.png)



You sigh: With the AI + AI Gateway combo, developing AI projects is so fast!

Fish Skin nods: Exactly, and throughout the process we don't need to worry about a model going down — the gateway will automatically handle these issues.

![](https://pic.yupi.icu/1/1761645903883-94c22619-2cac-41a4-87c3-d51ec96586e0.png)



#### 4. More Features

Not only that, Vercel AI Gateway supports many domestic and international large models, each with different pricing standards:

![](https://pic.yupi.icu/1/image-20251019165234650.png)



You can also configure your own model API Keys:

![](https://pic.yupi.icu/1/image-20251019162655475.png)



Additionally, it provides **observability** and other enterprise-level features, helping you understand AI usage and cost analysis:

![](https://pic.yupi.icu/1/1760691345180-9ce7ec43-c651-4c19-a918-90b87034b7fe-20251028181255384.png)



Your eyes light up: Wow, I'll use this for all my future AI project development!

Fish Skin shakes his head helplessly: Xiao Aba, remember "there is no silver bullet."

If your personal project only needs to simply call a single AI model, just calling the API is enough; if your personal or team's small project needs AI Gateway features (like integrating multiple models), then you can choose Vercel AI Gateway; but if you're developing enterprise-level applications with high security and stability requirements, choosing a more professional gateway like Higress or Kong is more appropriate, can help you write a billion less lines of messy code 💩!

![](https://pic.yupi.icu/1/1761645922466-4284b8ac-7928-424e-a0eb-09629e7e66a1.png)



## Ending

A few months later, you refactored the company's intelligent customer service system using AI Gateway, with excellent results.

You sigh with emotion: This is standing on the shoulders of giants. Indeed, don't reinvent the wheel — lazy people drive world progress!

![](https://pic.yupi.icu/1/1761645939970-276a3391-2f40-4b85-8d23-d36c5a491f8c.jpeg)

Fish Skin coquettishly says: So that's your excuse for being too lazy to like me???

![](https://pic.yupi.icu/1/1761646182922-0edead80-b8e9-4b8f-a90d-e35fa8712f3b.png)


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
