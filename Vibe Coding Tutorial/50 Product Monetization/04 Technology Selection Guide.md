# Technology Selection Practical Guide

> Choose the right technology, get twice the result with half the effort



Hello everyone, I'm Fish Skin. The content to share in this article is **technology selection**, content that friends in technical directions must master, and also core work that must be done in the early preparation stage when making products.

In this article, I'll combine my practical experience making products to share with everyone in turn: what is technology selection? What does technology selection select? Why do technology selection? How to do technology selection well?

Whether you're using Vibe Coding to do personal projects, or want to make a real product, mastering technology selection methods can let you avoid many detours.



## I. What Is Technology Selection?

The term technology selection sounds very high-level, but it's actually "technology choice," that is, selecting which technologies to use to implement projects. Like using HTML to develop web pages, using C++ to develop Windows desktop applications.

To use an analogy, if we imagine doing a project as leading troops to battle, technology selection is equivalent to choosing weapons before battle. You need to comprehensively select the most suitable weapons based on your own troop types, enemy races, enemy deployment, etc., to win at minimal cost.

Note that technology selection is not only done in the project's early planning and design stages. Every time we add a new feature to the project, we might need to select new technologies to implement it; and as your project expands, might also need to upgrade the existing tech stack.



## II. What Does Technology Selection Select?

"Use which technologies to implement projects," this sentence sounds very simple. Like mentioned above, use HTML to develop web pages, one technology term covers it.

But actually, this is only the shallowest layer. Doing technology selection is not a relaxed matter, it's divided into many levels and details.

Looking from shallow to deep, technology selection includes:

1) Which type of technology to select?

Like programming languages, development frameworks, data storage, cache, queues, etc.

2) What specific technology to select?

Like programming language select Java, Go or C++? Development framework select Spring or Play? Cache select Redis or Memcached?

3) Which specific version of the technology?

Like select Java 8 or 11? Select Vue 2 or Vue 3? Select Redis 5 or 6? Different versions of the same technology often also have big differences.

4) Which specific features of the technology to use?

Like Spring's AOP aspects, Redis's GEO advanced data structures, etc.



So technology selection is still somewhat troublesome. And generally, the larger the project, the more cautious the technology selection, the longer the cycle.

Remember when I built BI visualization project from 0 to 1 at Tencent, just for technology selection, it took several weeks, deeply and comprehensively comparing mainstream domestic and foreign data storage technologies from multiple angles.

Since technology selection might take so much time and energy, then why do we still need to do technology selection?



## III. Why Do Technology Selection?

Believe many friends who haven't worked yet have never systematically done technology selection.

This is very normal, because everyone in the learning stage follows online tutorials to do projects. What technologies to use, which version, even what code to write, all are planned in advance by the instructor.

![](https://pic.yupi.icu/1/image-20230331134500590-20230706153049690-20230706153117049-20230706163222417.png)

But actually, it's not that technology selection wasn't done, but that the instructor did it for you. When the instructor selects which technologies to use to lead you in doing projects, it's essentially also doing technology selection, will combine factors like market demand, technology popularity, etc.

So why do technology selection?

The answer is simple, to develop and maintain projects **better**.

"Better" here might be improving efficiency, saving costs, enhancing development experience, improving project scalability, etc.

Imagine, when we develop projects in teams in enterprises, if the leader (or architect) to save trouble, selects a technology only he's familiar with that other team members can't use at all, will the entire project's development progress be fast? If to save small money, selects a low-cost, roughly-made cloud database, will the entire project's performance be high?

Before developing a **complete project**, if we thoughtlessly directly determine a technology and start writing code, possibly later, suddenly it fails. Like when I selected a cheap tire for my electric bike, initially it could run normally, but one day halfway the tire blew, could only foolishly wait in place...

Let me give a personal college failure experience. In college I led a team to do a campus forum website. Remember I used React to develop frontend pages. Initially very smooth, wrote dozens of pages in one breath; but until one day needed to develop post page information status save function, only discovered React doesn't have ready-made keep-alive (cache component state) like Vue Router. Later spent a long time finding a similar component, result was a bunch of Bugs!

Moreover, the more intrusive the technology is to project code (like development frameworks), the higher the later switching cost. Like the failure example I gave above, after writing dozens of pages, then switching development frameworks will be very troublesome; and sometimes, when you introduce new components or libraries to the project, might conflict with existing dependency versions, causing the project to not run later. At this time, do you choose to switch to old technology, or spend more energy finding new technology that doesn't conflict with old technology? Even worse, to be compatible with the outrageously old technology framework used by the project originally, dare not introduce any new technologies, leading to developing everything yourself... truly one wrong step, every wrong step after!

These are actually problems brought by not doing technology selection, or improper technology selection, also confirming the necessity of our doing technology selection.

Looking back now, it was indeed lack of experience then. If I could consider this point at the very beginning, first globally confirm technologies that might be needed to implement project functions, and select appropriate technologies, could reduce later risks, save much time.



## IV. How to Do Technology Selection Well?

After understanding the importance of technology selection, let's talk about how to do technology selection well.

Next, I'll combine my team's technology selection experience to take everyone through mastering technology selection key points from several aspects.



### 4.1 Clarify Context

First need to clarify one point: there's no absolutely perfect technology, our goal in technology selection is under **limited conditions**, select technology **optimal solution** in **specific scenarios**.

Several keywords:



#### 1) Limited Conditions

Refers to team size, personnel skills, time cost, money cost, etc.

Like if everyone only knows Java, project is urgent to go online, then definitely prioritize Java-related tech stack, don't just because you heard Go language has high performance, make everyone work overtime to learn Go.

Like company lacks funds, no resources, then compared to selecting paid services (like cloud databases), might as well directly build on one server ourselves.

Like company has many resources, but lacks manpower, then services like databases don't need to be built ourselves, directly buy third-party cloud services.

A relatively common selection approach is to first start from the manpower angle, see what technologies team members know. If requirements are very urgent, then definitely prioritize technologies everyone is relatively familiar with, first complete phase 1 requirements quickly deliver, later research more suitable technology architecture, continuously optimize. Also like if team has relatively mature practical experience and knowledge precipitation for certain technology, also has corresponding technical expert, then can prioritize using that technology. Take the most typical example, Alibaba's R&D team prioritizes Java, ByteDance prioritizes Go.

Then consider from the resource angle, see if team's resources are suitable for using this technology. Like startup small team, no funds, then can use MySQL instead of Elasticsearch to implement search functionality, sacrifice flexibility to save money. Also like company can only provide 4G memory servers, then when selecting some open source technologies need to pay attention to their memory usage, can't exceed this threshold.



#### 2) Specific Scenarios

Refers to our technology selection must revolve around **specific business and requirements**, fit reality, not use technology for technology's sake.

Can think about the following questions:

1. What functions do you want to implement? Like to make a network disk system, need to focus on selecting file storage technology; to make a chatroom system, need to focus on selecting real-time communication technology.
2. What's your business volume level? If user count is large, data storage is large, can choose distributed databases, or database sharding; if many users use system simultaneously (high concurrency), can choose Nginx or LVS to implement load balancing.
3. What are the system's core business processes and key data structures? Like to make a management system, then database choosing mainstream relational database MySQL is good; and if to make data analysis system, then should choose OLAP type database, like ClickHouse, etc.
4. Which performance indicators does the system focus more on? Like log collection scenarios focus more on high performance and throughput, then can choose Kafka message queue to collect; like focus on low latency and message accuracy, then can choose RabbitMQ.



Limited conditions + specific scenarios = context, can also be understood as team and project actual situation.



#### 3) Optimal Solution

Many times, when we do technology selection and design algorithms, there's no absolute optimal solution, but comprehensive trade-off of time, space, stability, availability, performance, etc.

Different contexts, the optimal solution selected is also different. This is the most interesting, and also the most torturous part of technology selection!

> CAP theory is also like this, it refers to in a distributed system, cannot simultaneously satisfy Consistency, Availability and Partition Tolerance these three characteristics, can only trade-off between the three based on actual situation.



### 4.2 Thorough Research

After clarifying our team and project's actual situation, we need to do thorough research. Can use Baidu, Google, GitHub and other search engines, or articles and videos etc. to explore information about various technologies that might be used.

Including:

- What is this technology? What's it for?
- What advantages and disadvantages does this technology have?
- What's the usage cost of this technology?
- What scenarios is this technology more suitable for?
- What's the background and reputation of this technology, etc.



There are also many websites that can help us get technology selection information, like:

- Technology Radar: https://www.thoughtworks.com/zh-cn/radar
- Framework Performance Comparison: [https://www.techempower.com/benchmarks](https://www.techempower.com/benchmarks/#section=data-r21)



But I haven't used these websites for a long time. Since AI dialogue technology became popular, when I do technology selection, I'll directly ask AI (GPT or Yu Smart), let it help me get information.

Like ask it: You are an expert in computer programming field, now I want to make a XX system, roughly has XX functions, limited conditions are XX. Please help me list technologies needed to implement these, require recommending more similar technologies and listing each technology's introduction, advantages and disadvantages, applicable scenarios, facilitating my evaluation of technology selection optimal solution for implementing this system.



Note, in the research stage, everyone should first search for as many related technologies as possible, rather than limiting your vision to a certain technology.

Recommend recording all researched technology information in documentation in the form of tables or lists, continuously improve and supplement, facilitating comparison and final technology selection.

Like below:

![](https://pic.yupi.icu/1/image-20230706180955933.png)

In large company large projects, technology selection must provide sufficient basis and reasons, will get approval from superiors or other members.



### 4.3 Comparison and Selection

After collecting enough information, we can comprehensively select the most suitable technology based on context + collected information.

Besides context, recommend everyone prioritize selecting: technologies with high popularity, backed by big companies, continuously maintained, high activity, open source, complete documentation, many users and good ecosystem.

Like the famous frontend framework Vue and Java backend framework Spring Boot. Everyone's impression of them is powerful, simple and easy to use, many learning resources, so these two technologies are mainstream, company demand is also large.

Absolutely don't choose technologies lacking documentation, few people use niche technologies! Once problems appear later, can't find solutions online, possibly the entire project cannot continue!



### 4.4 Minimal Demo Verification

Before finally confirming the technology to select, don't forget to verify whether this technology can be applied to our project, rather than directly deciding!

Recommended practice is to write a minimal Demo to quickly verify whether technology is usable. Like using Vue Router page routing technology, then write a click button, quickly jump to `/about` page Demo.

This process is essentially achieving the transition from theory to practical implementation.

Also thanks to the development of AI technology, now want to write Demo to quickly verify, don't need to write code yourself, directly ask GPT:

![](https://pic.yupi.icu/1/image-20230706182008022.png)



If our system is an old project, need to focus on compatibility of newly introduced technologies with old project dependencies. At this time, writing minimal Demo verification is very necessary, can avoid version conflicts in advance.



### 4. Daily Accumulation

Besides the above methods, to do technology selection well, accumulation of experience value is also very important. Like a ten-year architect in e-commerce field, to make a new e-commerce system, can immediately think of appropriate technology selection, even the entire system's complete implementation solution.

Give everyone two suggestions:

1) Continuous recording

Record **every** technology you see related to your learning direction or work in documentation first. When have time can quickly understand the technology's general information, know what this technology does, what it's for. When need to use it can think of it, or can search from documentation.

2) Broaden boundaries

Don't fantasize about using one technology to conquer the world, also don't satisfy with your own technology field. Especially in self-learning stage, doing some small projects, can occasionally try using some new technologies not usually contacted, broaden your technology selection range horizontally.

Like although my work is Java backend, I often do some frontend projects, and each time switch technologies, like Vue, React, Svelte, etc.



## V. Technology Selection Practice

After introducing methodology, finally share our team's technology selection practice for Yu Smart AI.

Following the several steps shared above, first clarify context.



### 5.1 Clarify Context

#### 1) Limited Conditions

Our team has few people, everyone's most familiar technology framework is backend Java Spring Boot + frontend React, so frontend and backend technology frameworks are basically determined.

Also don't have enough funds to buy many servers and third-party services, so for most non-core services, use Java Tomcat standalone deployment, and use Pagoda Linux for server management.



#### 2) Specific Scenarios

4 questions 4 answers:

1. What functions do you want to implement? Our P0 level core functions to implement are: AI chat, AI assistant, content review. AI chat and content review can both use third-party GPT services to implement.
2. What's your business volume level? In website early stage, user concurrency won't be very large, tentatively qps (queries per second) not exceeding 3, currently don't need load balancing technology.
3. What are the system's core business processes and key data structures? Core business process is user sends dialogue => AI auto replies => store message records. So involves saving dialogue and message records. Since one dialogue can contain multiple message records, very suitable to choose relational database MySQL to implement.
4. Which performance indicators does the system focus more on? Because my previous websites were often attacked, so this time very focused on system security and availability. To control concurrency, can choose Redis + Redisson to implement distributed rate limiting, control each user's message sending frequency not too frequent.



#### 3) Optimal Solution

Here's an example: consume cost using third-party cloud database service, or build database ourselves on server?

When still in school, I would definitely choose the latter. Because many projects are for self-learning and practice, if it runs is fine; building database myself can also help me familiarize with Linux server commands. Of course most crucial is still saving money, save down to add a chicken leg to lunch isn't it fragrant?

But now doing online projects facing users, I'll be more inclined to use ready-made cloud database services. Database construction, operations, management, optimization are all done for you, you get database account password and can directly use, don't worry about database downtime. Compared to investing more funds, can greatly save our "already not rich" development and operations costs.

This is our current optimal solution for database technology selection.



### 5.2 Thorough Research

Mentioned above, our system's **vast majority of functions** use mainstream technology Spring Boot + React to implement. They both belong to our team members' specialties, also are well-known technologies with good ecosystems, no need for more research.

Conversely, we invested relatively more time in **content review** this small function's research.

Why?

Because for AIGC products, content review is crucial; and more crucially, content review costs money!

To balance both content review quality and cost, we locked our eyes on cloud services provided by several domestic big companies, that is BAT.

And through reading official documentation and customer service inquiry, organized the following comparison table:

> Data is example reference only, please refer to official for accuracy

![](https://pic.yupi.icu/1/image-20230706195734818.png)



### 5.3 Comparison and Selection

With the above comparison table, we can combine actual business situation to select which content review technology to use.

Like in our dialogue function, allowing users to input maximum characters at once around 1000 - 2000, dialogue function usage QPS not exceeding 10, then selecting provider A or B is both reasonable.

> We can split user's single input into multiple paragraphs, bypass character limit by sending multiple requests.



### 5.4 Minimal Demo Verification

After determining the technology to use, the remaining work is very simple. For third-party provided content review cloud services, we just need to open official documentation, can find ready-made example code, download to local execute successfully.

![](https://pic.yupi.icu/1/image-20230706200934291.png)



### 5.5 Daily Accumulation

Finally, about daily accumulation, actually mentioned in the previous article "Documentation Accumulation". Our team continuously pays attention to AI-related technology trends every day. As long as discovering new technologies, will immediately record in team's public knowledge base. When need to use this technology, further research.



---



Technology selection is an important link in making good products. Choose the right technology, get twice the result with half the effort; choose wrong technology, might put project in dilemma.

Remember these key points:

1. Technology selection must combine team actual situation and project requirements
2. Must thoroughly research, compare from multiple sides
3. Prioritize technologies with high popularity, good ecosystem
4. Must write minimal Demo to verify feasibility
5. Must continuously accumulate technology selection experience

In the Vibe Coding era, AI can help you quickly understand various technologies, even help you generate Demo code. But, how to select the most suitable technology based on actual situation still needs your own judgment and accumulation.

Go for it, choose the right technology, make your product development smoother! 💪


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
