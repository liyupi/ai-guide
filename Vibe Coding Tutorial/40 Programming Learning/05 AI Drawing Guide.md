# Programmer AI Drawing Complete Guide

> Generate architecture diagrams in 1 minute, say goodbye to manual drawing



Hello, I'm Fish Skin the programmer.

As a programmer, drawing is a common part of work. Whether it's drawing architecture diagrams for reporting to leadership, drawing flowcharts for documentation, or drawing mind maps during brainstorming, drawing ability directly reflects our professional level.

Previously drawing required time and effort - a complex architecture diagram might take hours, with repeated adjustments; now while drinking a cup of water, AI helps you draw, and the effect is especially professional!

Below I'll share **5 major types of AI drawing methods**, each with detailed nanny-level tutorials. Each method is more powerful than the last, recommend liking and bookmarking first. In the future, whether generating prototypes, designing posters, or the architecture diagrams, flowcharts, UML class diagrams, etc. that programmers often draw, it's all a piece of cake~

⭐️ Recommend watching the video version for more detailed operation demonstrations: https://bilibili.com/video/BV1DP7JzAE7k



## The Essence of AI Drawing

Before starting, let's understand the essence of AI drawing: **it's actually having AI generate various text codes that drawing tools can understand**, then importing these codes into corresponding tools for rendering.

This way, you can leverage AI's creativity and tool capabilities to freely generate images.

![AI Drawing Principle](https://pic.yupi.icu/1/1748414656182-9580e13e-97bd-4013-8361-ee19b200c0f7.png)

Although current mainstream AI large models and tools can all achieve drawing functionality, I strongly recommend using **Cursor tool paired with Claude 4 large model** for the best results.

Below I'll introduce several types of AI drawing methods:



## I. Text Drawing

Text drawing is the most popular drawing method among advanced programmers, generating professional technical diagrams through simple text descriptions. Mainstream text drawing languages include **Mermaid** and **PlantUML**.



### Mermaid - Most Popular Text Drawing Tool

Mermaid is currently the most popular text drawing tool, with simple and intuitive syntax, natively supported by major platforms like GitHub and Yuque. Whether you're drawing software architecture diagrams, business flowcharts, database ER diagrams, or Git branch diagrams, Mermaid can handle them easily.

Let's first draw a user login flowchart, just give AI this prompt:

```plain
Please help me draw a user login flowchart using Mermaid syntax, including the following steps:
1. User enters account and password
2. Frontend validates format
3. Send request to backend
4. Backend validates user information
5. If validation successful, generate token and return
6. If failed, return error information
7. Frontend redirects page or displays error based on result
```

Put it in Cursor or other AI tools to execute, AI will generate Mermaid code. Then you can copy the code to tools that support Mermaid to see the effect, like Yuque, Typora, or the online [Mermaid rendering website](https://mermaid-live.nodejs.cn/edit).

![Mermaid Flowchart](https://pic.yupi.icu/1/1748414916480-1151faa7-a03d-49b0-82b0-ba321211456e.png)

Many AI chat assistants have built-in Mermaid rendering tools, can directly see the effect and download:

![AI Built-in Rendering](https://pic.yupi.icu/1/1748415298510-f1389787-6859-4cf6-b0c7-fe6712acf57a.png)

Mermaid also supports multiple chart types, like sequence diagrams, Gantt charts, pie charts, Git branch diagrams, architecture diagrams, etc.



### PlantUML - Professional UML Drawing Tool

PlantUML is another powerful text drawing tool, especially good at drawing UML diagrams, sequence diagrams, and system architecture diagrams. Its syntax is relatively more professional and standardized than Mermaid, and generated charts are also more refined.

Let's use AI + PlantUML to draw a classic order system class diagram:

```plain
Please help me draw a class diagram for an order system using PlantUML syntax, including:
- Order class: order ID, user ID, total amount, status, creation time
- OrderItem class: product ID, quantity, unit price
- User class: user ID, username, email
- Product class: product ID, name, price, inventory
Show their relationships
```

AI will generate professional PlantUML code, similarly put it in Yuque's text drawing, or [PlantUML rendering website](https://www.plantuml.com/plantuml/uml/) to see the effect.

![PlantUML Class Diagram](https://pic.yupi.icu/1/image-20250530125534018.png)



### How to Choose?

| Feature      | **Mermaid**                    | **PlantUML**            | **Graphviz**            |
| ------------ | ------------------------------ | ----------------------- | ----------------------- |
| **Chart Types** | Flowcharts, sequence diagrams, Gantt charts, etc. | Full UML series, architecture diagrams | All types of charts, extremely flexible |
| **Syntax Difficulty** | Simple and intuitive        | Medium, UML standards    | Relatively complex      |
| **Ecosystem Support** | GitHub/GitLab native support | Needs plugin support     | Widely supported        |
| **Use Cases**  | Daily document illustrations | Professional architecture design | Complex network topology |

My suggestion is, choose Mermaid for daily use because of its simple syntax and good platform support; if drawing professional UML diagrams, choose PlantUML.



## II. Web Drawing

Web drawing is a very free and flexible drawing method. Essentially "image is website" - by generating webpage code containing visual elements, various images are rendered in browsers.



### Native Web Drawing

Using core web development technologies (HTML + CSS + JavaScript), we can generate various types of charts. You can also leverage various third-party visualization libraries (like ECharts, D3.js, etc.) to enhance effects.

For example, when needing to display data, AI can use Apache ECharts and other visualization libraries to generate professional data dashboards:

```plain
Please generate a data visualization dashboard page showing real-time data for an e-commerce platform:
1. Page layout: dark background large screen style
2. Include the following charts: real-time sales, category sales proportion, 24-hour sales trend, top 10 hot products, user geographic distribution
3. Use ECharts implementation, with animation effects
```

AI will generate a complete website, including various charts, pretty cool right~

![Data Dashboard](https://pic.yupi.icu/1/1748417511003-49c81cc8-618e-4810-b94d-ebcfbb48885d.png)

You can directly screenshot as needed to get images; you can also quickly share the generated website with others through tools like [Codepen](https://codepen.io/).



### SVG Vector Graphics Drawing

SVG is scalable vector graphics that can be infinitely scaled without distortion, very suitable for drawing UI materials, Logo icons, graphic illustrations, technical architecture diagrams, flowcharts, etc.

Let's use SVG to draw a system architecture diagram:

```plain
Please generate a system architecture diagram in SVG format, showing a typical three-tier architecture:
- Presentation layer: Web frontend, mobile App
- Business layer: API server cluster (3 nodes)
- Data layer: master-slave database, Redis cache
Requirements: use different colors to distinguish layers, add connection lines to show data flow
```

The SVG code generated by AI can be directly saved as an SVG file and opened in a browser.

![SVG Architecture Diagram](https://pic.yupi.icu/1/1748419703308-c3e3ab06-bfd0-4d3e-8bd9-6315fe9e3dde.png)



## III. Professional Drawing Tools - Draw.io

Combining AI with professional drawing tools can achieve 1+1 > 2 effects.

I use the free and open-source **draw.io** quite often. Its advantages are extremely high freedom, supports importing and exporting multiple formats, and has rich graphics libraries and templates.

There's also a hot open-source project [next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) that can directly generate and edit draw.io images through AI dialogue. It gained 6k stars in just a few days!

![AI Draw.io](https://pic.yupi.icu/1/1765425690148-db18c63c-6666-4a0b-a681-0ad4a5c061c3.png)

This project supports online experience. You can draw completely from scratch, like drawing a flowchart to demonstrate how RAG works. AI will automatically generate Draw.io drawing code, and the beautiful flowchart is done quickly!

⭐️ Recommend watching video demonstration: https://bilibili.com/video/BV18NmnB4EeM

![RAG Flowchart](https://pic.yupi.icu/1/1765425750546-988f6dd9-552b-403f-a1ea-f8866c309663.png)

Then you can use Draw.io's own powerful drawing capabilities to manually modify any element or change style. Or have AI help you modify through dialogue, like changing to animated connection lines, and the level instantly goes up.

![Animated Connection Lines](https://pic.yupi.icu/1/1765425815484-e879ea8a-d40a-4857-baab-4124c3eedcee.png)



### Generate Various Technical Diagrams

There are also architecture diagrams involved in programmer work:

```plain
Prompt: draw a microservice architecture diagram for an e-commerce platform
```

![Microservice Architecture Diagram](https://pic.yupi.icu/1/1765425829760-5337eb51-a51a-4327-a1e0-66b6f4ce2176.png)

UML class diagrams:

```plain
Prompt: use UML class diagram to show user management module design
```

![UML Class Diagram](https://pic.yupi.icu/1/1765425843465-53ebe0d1-0df4-46b1-8b27-1bdd98333f5d.png)

ER diagrams:

```plain
Prompt: draw a database ER diagram for an online education platform
```

![ER Diagram](https://pic.yupi.icu/1/1765425852509-4685b9ff-9c86-430c-9e7e-fd1f75877c51.png)

Sequence diagrams:

```plain
Prompt: use sequence diagram to show user login interaction process
```

![Sequence Diagram](https://pic.yupi.icu/1/1765425862905-cab2301b-77c2-47e4-adc1-6d7c617cd33b.png)

All of these are no problem, saving you lots of time and hair~



### Usage Tips

There are also some usage tips, like combining with free icon libraries to make the entire drawing richer:

```plain
Prompt: use AWS icons to generate CDN architecture diagram
```

![AWS Architecture Diagram](https://pic.yupi.icu/1/1765426030861-27a70a15-559b-4540-9177-5e5f66d120b0.png)

You can use native SVG animation tags to add zoom and path animations to the entire drawing:

```plain
Prompt: demonstrate DDOS attack, use SVG's <animateMotion> and <animateTransform type="scale"> to add zoom and path animations
```

![Animation Effect](https://pic.yupi.icu/1/1765425981962-4a730008-8a64-4805-adfc-a63a983e4fde.png)

You can also upload a sketch yourself, like a Mermaid flowchart I generated with a text model, and have AI help me replace it with a more beautiful style:

```plain
Prompt: change to rainbow theme colors, enlarge font, use bold animated connection lines
```

The effect is pretty good!

![Optimized Diagram](https://pic.yupi.icu/1/1765426075534-26f6f2a7-8ee9-421f-ad10-4910b2b7df34.png)

Finally export to various image or document formats, wonderful~

![Export Format](https://pic.yupi.icu/1/1765268527840-a3717305-7bba-4533-8595-c92c21bcd021.png)



### Local Deployment

Note, the official demo website may be limited and unstable. I used it several times in a row and got rejected.

So I recommend downloading the open-source code locally, and following the official documentation [configure your own large model](https://github.com/DayuanJiang/next-ai-draw-io/blob/main/docs/ai-providers.md) to run it; or use Docker for one-click startup, use it however you want.

![Docker Deployment](https://pic.yupi.icu/1/1765426188076-914514ec-c5cd-4ac5-8ca7-e09f0808801e.png)



## IV. Mind Maps

AI can help us quickly generate beautiful mind maps, and export them to formats supported by professional mind mapping software.

I use XMind quite often for mind mapping software, which supports rich styles and themes.

I more recommend having AI generate **Markdown format mind maps**, because Markdown format is more universal and convenient to use in various document tools:

```plain
Please help me generate a mind map about "microservice architecture design", use Markdown format, use indentation to show hierarchy
```

AI will generate this Markdown format:

```markdown
# Microservice Architecture Design

## Service Decomposition Principles
- Single Responsibility
  - Each service is only responsible for one business function
  - High cohesion, low coupling
- Service Autonomy
  - Independent deployment
  - Independent technology selection
```

Import this Markdown file directly into XMind, and a clear-structured mind map is generated!

![Mind Map](https://pic.yupi.icu/1/1748422118001-752df2f4-d369-46b8-8e16-cd96191d554f.png)



## V. AI Drawing Tips



### Tip 1: Provide Example Images for AI to Imitate

When you see a great diagram and want to draw a similar one, you can directly screenshot it to AI and have it help you generate a similar diagram.

For example, imitating the system architecture diagram I provided:

```plain
Please based on the system architecture diagram I provided, generate a diagram with similar style and structure in draw.io format, but change the content to:
- An online education platform architecture
- Keep the original color scheme and layout style
```

The generated result is shown, very similar right?

![Imitate Generation](https://pic.yupi.icu/1/1748424880583-92c573bc-fdb2-45d0-b4e0-d2590ea069c5.png)



### Tip 2: Screenshot Annotation, Precise Modification

If you're not satisfied with some parts of the AI-generated diagram, you can screenshot and circle the parts that need modification, then tell AI how to modify.

![Annotation Modification](https://pic.yupi.icu/1/1748424987920-e61af63a-b688-4cf8-8cd5-e05df1d412c9.png)



### Tip 3: Configure Professional System Presets

The effect AI generates largely depends on the input prompt, so to have AI draw more professional diagrams, configuring a good system prompt is crucial.

In Cursor, we can set project-level Rules, letting AI always follow your drawing standards.

Here's a professional architecture diagram drawing preset for reference:

```plain
# Technical Architecture Diagram Drawing Expert

You are a senior system architect and technical chart design expert.

## Drawing Principles
1. All text must use simplified Chinese
2. Keep diagrams concise and clear, avoid over-complexity
3. Use standard technical icons and symbols
4. Professional color scheme, clear hierarchy

## Color Scheme
- Presentation layer: blue series (#3498db)
- Business layer: green series (#2ecc71)
- Data layer: orange series (#e67e22)
```

Configure this preset in Cursor Rules, and AI will generate images following the rules, ensuring output consistency and professionalism.



## In Conclusion

Reading this far, I believe you've mastered various AI drawing postures! From simple text drawing to complex dynamic charts, AI can handle them all easily.

Not only can it save us lots of time, but mom no longer worries about my ugly drawings!

If you think this content helped you, don't forget to like and bookmark. Friends learning programming and interested in AI are welcome to follow Fish Skin. In my free open-source [AI Knowledge Base](https://ai.codefather.cn), I've also summarized a lot of AI knowledge and tutorial dry goods, hope it helps everyone.

![](https://pic.yupi.icu/1/image-20260109121412266-20260113153648943.png)





## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
