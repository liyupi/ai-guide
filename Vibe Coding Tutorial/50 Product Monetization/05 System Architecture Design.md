# System Architecture Design Practice

> Build a product that stands tall



Hello everyone, I'm Fish Skin. In this article, let's discuss something that sounds very high-level but isn't actually that difficult — **architecture design**. This is content that friends in technical directions must **focus on mastering**, and it's also core work that must be done in the early preparation stage when making products!

In this article, I'll combine my practical experience making products to share with you in turn: What is architecture design? Why do architecture design? How to do architecture design well?

Whether you're using Vibe Coding to do personal projects, or want to make a real product, mastering architecture design methods can make your system more stable and more scalable.



## I. What Is Architecture Design?

Imagine, if we were going to build a skyscraper right now, what would we need to do?

Would we just directly let workers move bricks and stack bricks? Or let excavators dig dig dig?

Of course not!

Before building, there will definitely be an architect who, based on the building's actual use, geographical location, occupancy needs and other information, draws up a blueprint. The blueprint will plan the building's appearance, internal layout, structural details, etc.

After drawing up the blueprint, the architect also needs to determine the framework and support structure for each floor, ensuring they are stable enough and won't collapse when the wind blows.

Afterward, the architect also needs to plan the use of each floor according to the building's actual use and needs, like B1 floor for snacks, 1st floor for clothing luxury goods, etc. These are all confirmed before the building starts construction. It won't be that after workers have already moved bricks, the top temporarily decides "we're not building this floor!"

Software (website) development is the same. Before we "code farmers" actually write code by hand, there's often an experienced architect who first draws up an **architecture design diagram**, planning the entire system's full picture, system scale, and system structure.

The architect also needs to divide the system into various modules according to functions and requirements, like dividing a shopping mall system into user module, product module, order module, etc. And determine the role and interaction collaboration method for each module, ensuring the entire system can operate normally. It won't happen that one function malfunctions and the entire system is paralyzed.

Some friends might ask, then what's the difference between architecture design and the previously discussed technology selection?

Let's still use building as an example, it's actually easy to distinguish. Architecture design is planning how to build and how to arrange each floor; while technology selection is after completing architecture design, choosing specifically what materials, tools or methods to use to complete the building. The two complement each other.

To summarize in one sentence, **architecture design is the process of building stable, reliable and scalable systems**.

And the position we're familiar with "architect," is the person responsible for completing system architecture design, ensuring the system is stable, reliable, and scalable.

In everyone's impression, you might feel architect is a very high-level role. But I personally believe, as long as you can independently complete a system's architecture design, can break down complex systems into modular, scalable components, you're already an architect.

> So becoming an architect in '97 is still somewhat reasonable.



## II. Why Do Architecture Design?

Actually from the building example above, I believe everyone can roughly feel the importance of architecture design.

If before building, we don't first design the building's structure well, then it's difficult to guarantee the building's safety and stability, the whole floor collapses when the wind blows. Similarly, before developing websites, if we don't first design the website's overall architecture well (like not adding a firewall), later when encountering network attacks, the entire system might be unable to access. This is architecture design's core goal: guarantee system **stability, reliability and availability**. In other words, at least let the system be able to run.

> But no worries, as long as either the system or the person can run, it's fine.

Another important reason for doing architecture design is the system's **scalability**. To give an analogy, the built shopping mall building is very popular, we want to add a few more floors on top of the built building, then we must ensure in the beginning that the building's structure can support additional weight, can linearly stack upward. Rather than like the image below:

![](https://pic.yupi.icu/1/image-20230711174331231.png)

Similarly, if we want the website to be able to handle increasing user volume and new business functions, must also have good architecture design to support it. Don't let the situation where website user count increases and the website can't be accessed happen.

In addition, good architecture design can also improve system performance and user experience. For example in the mall, reasonably arranging the number and position of elevators can help users quickly reach the stores they want to go to; and if website architecture design is reasonable, like using fewer layers to complete the same functions, then can respond to user operations more quickly.

In summary, if you want to let the website stand tall like a skyscraper, early-stage architecture design is necessary!



## III. How to Do Architecture Design Well?

"Being able to complete architecture design" and "being able to do architecture design well" still have a big difference. Below I'll combine my many years of learning experience and Fish Skin AI's architecture design to share some key points I think for doing architecture design well.



### Master Methodology

The prerequisite for doing architecture design well is having certain theoretical knowledge. So-called methodology refers to a set of **specific problem solutions** formed by predecessors through summary and induction. Just like when we do math problems we know how to apply formulas to solve problems.

There are many methodologies that help architecture design. Like object-oriented design encountered when first learning programming, basic software development principles, 23 classic design patterns, SOA service-oriented architecture, DDD domain-driven design, etc. Mastering the ideas behind these methodologies is the **premise** for doing architecture design well.

For example, among the five basic principles SOLID of object-oriented design, there is a point of **single responsibility principle**, which means: a class or module should have one and only one single responsibility, each class or module should only focus on a specific function or responsibility. In other words, each module should only do its own job well.

When we were doing Fish Skin AI website's architecture design, first we followed the single responsibility principle, dividing the system **by functions** into user module, assistant module, chat module, drawing module, payment module, etc. This way, when we want to expand chat-related functions, we don't need to modify assistant module's code. We can also assign different modules to different classmates in the team for development.

![](https://pic.yupi.icu/1/image-20230711192728792.png)



### Learn Classic Architectures

Predecessors plant trees, descendants enjoy the shade. Before we have the ability to independently design an architecture, we might as well stand on giants' shoulders, learning some classic architectures summarized and practiced by predecessors.

Just give a few simple examples:



#### 1) Layered Architecture

First is the most classic layered architecture, dividing the system into multiple different layers, each layer has specific functions and responsibilities, and only "deals with" its direct upper layer and direct lower layer.

For example the three-layer architecture commonly used when developing Java enterprise-level backend projects, dividing the system into presentation layer, business logic layer, data access layer.

The presentation layer is responsible for accepting user requests, passing user input parameters to the business logic layer for processing, and returning data, pages and other content to users.

The business logic layer is responsible for processing complex business logic, like calling AI capabilities to complete intelligent dialogue, then processing, calling the data access layer to store results in the database, also is the main development part of our system.

The data access layer is responsible for operating underlying data sources, like doing CRUD on databases, files, cache, etc.

![](https://pic.yupi.icu/1/image-20230711194035810.png)

Layered architecture's applicability is very broad, the vast majority of enterprise-level systems can use layered architecture as basic architecture design.

Computer networks also adopted classic layered architecture. In OSI seven-layer reference model, computer networks are divided from bottom up into physical layer, data link layer, network layer, transport layer, session layer, presentation layer and application layer. Each layer only processes specific functions, like data transmission, data routing; layers communicate with each other through interfaces (or called protocols).

Our Fish Skin AI backend also used layered architecture, just that on the basis of the original three-layer architecture, between the business logic layer and data access layer we added a Manager layer (common logic layer), extracting **common logic** frequently called by the business logic layer, facilitating reuse.



#### 2) Microservices Architecture

The "micro" in microservices is relative to the concept of "monolithic" projects. Microservices architecture refers to dividing a complete large system into multiple tiny, autonomous services, each service can be independently deployed, independently scaled and maintained, without affecting each other, services communicate through network for collaboration, thereby realizing the complete functionality of the originally large system.

Our Fish Skin AI used microservices architecture. I also mentioned earlier, we first divided the system by functions into multiple modules.

But if we only logically divided these modules, actually all code is still deployed in the same project, after packaging it's still one executable file. Then all modules either are all running or all are down, essentially still a monolithic project. One service crashes, possibly causing the entire project to be unable to run!

![](https://pic.yupi.icu/1/image-20230711200006355.png)

So we extracted the code of some important modules (like payment module) from the original project, separately as a service, and also started backups, thereby guaranteeing payment business's stability. Can't affect revenue no matter what, right~

![](https://pic.yupi.icu/1/image-20230711200339275.png)

There are also many frameworks that can implement microservices design, like Java's Spring Cloud, Apache Dubbo, etc. But learning microservices is more about the thinking, that is **how to reasonably divide services**.

Not all projects need to divide all functions into sub-services. Like our Fish Skin AI, also didn't separate user module and assistant module, the reason is these two modules' business isn't complex and there are tight dependencies, after dividing it's actually not good for maintenance.



#### 3) Event-Driven Architecture

In event-driven architecture, each module communicates through events' (or messages') **publish-subscribe model**.

Give the simplest example, there are two modules: payment module and member module. When user payment is successful, the payment module will send a "XX user payment successful" event to the member module, after receiving this event the member module opens membership for the corresponding user.

![](https://pic.yupi.icu/1/image-20230711202025430.png)

But in actual application, event-driven architecture will often introduce an **event bus**, equivalent to an intermediary, responsible for centrally collecting and distributing events.

For example Fish Skin AI's chat function and drawing function adopted event-driven architecture. When upstream returns AI reply message or generated image, will send "success" message to event bus, then event bus forwards these messages to corresponding modules for processing. As shown below:

![](https://pic.yupi.icu/1/image-20230711201650066.png)

This way, decoupling (mutual non-influence) is achieved between modules. If later I want to add multiple chat modules, just need to connect that module with the event bus, won't affect other modules' operation.



### Focus on Requirements and Pain Points

The projects we encounter during learning process, almost all can apply the above several mainstream architectures. But specifically how to do architecture design well, must be analyzed by combining actual requirements and pain points to be solved.

Take Fish Skin AI as an example. I also mentioned earlier, we first divided the system by requirements (functions) into multiple modules, then separately packaged some modules as services for independent deployment.

But architecture design didn't end here. Next, let's analyze our website's pain points, mainly in these two aspects: "security" and "access interoperability".



#### Security

According to my previous rollover experience, after website goes online it will definitely suffer various attacks! So, we expanded on the original layered architecture, adding high-defense servers and Nginx firewall before the presentation layer, adding distributed rate limiting and permission verification processing after the presentation layer.

> Adding centralized distributed rate limiting and permission verification processing before the presentation layer is also reasonable, mainly based on actual needs.

The improved architecture is shown in the image:

![](https://pic.yupi.icu/1/image-20230711203808233.png)

If users use unlawful means to frequently send requests to the system in a short time, then they will be intercepted at the rate limiting layer, won't proceed to subsequent business logic processing.



#### Access Interoperability

Our AI drawing module needs to rely on third-party services to complete some functions, but the third-party services don't support cross-region access, networks can't interoperate, what to do?

At this time, we have 2 options to choose from:

1) Deploy the entire system in the region where the third-party service is located. As shown below:

![](https://pic.yupi.icu/1/image-20230711205545871.png)

2) Build a proxy between the AI drawing module and third-party service, let the proxy help send and respond to requests. As shown below:

![](https://pic.yupi.icu/1/image-20230711210049633.png)

If it were you, which would you choose?

Option 1's benefit is convenience, but the disadvantage is also very obvious, moving the entire system to another region means that users in the original region accessing all system functions will have slower speed.

Option 2's benefit is only needing to change the request address information sent by the AI drawing module, while the system's other functions (like querying user information) performance is completely unchanged; the disadvantage is needing to build additional services, increasing implementation cost.

In the end, we chose option 2 and improved the architecture design, increasing a bit of implementation cost to exchange for better user experience.

Through this example, I want to tell everyone: **there's no absolutely perfect architecture design**. Just like with technology selection, our goal in doing architecture design is to find the optimal solution under actual circumstances.



### Think Ahead

When we do architecture design, we need to cultivate the habit of thinking ahead, not only targeting current status, but提前预见 system's possible future development, reserving enough **scalable** space.

For example our Fish Skin AI, although at the beginning there were only 100 beta users, we would design the system according to the standard of 10,000 or even 100,000 users, so we used distributed storage middleware instead of local server to store user login Session; although early historical chat message count only accumulated 50,000, we提前 designed message expiration elimination mechanism, and decoupled the message module, preventing message count from reaching millions or tens of millions and affecting system query performance.

Of course, thinking ahead also needs a degree. Must avoid over-design, don't提前 consider things that absolutely won't happen, don't提前 consume costs far exceeding growth.



---



Finally, note that **architecture design is a continuous process**, need to continuously optimize and iterate according to business actual situation. Like when discovering business revenue isn't high, reduce costs by simplifying architecture; when business develops at high speed, timely expand services to handle growth.



## In Conclusion

Architecture design is an important foundation for making good products. Good architecture design can make systems more stable, more scalable, and have better performance.

Remember these key points:

1. Architecture design requires mastering basic methodologies and design patterns
2. Must learn classic architectures, stand on giants' shoulders
3. Must focus on actual requirements and pain points, not design for design's sake
4. Must have the awareness of thinking ahead, reserve expansion space
5. Architecture design is a process of continuous optimization

In the Vibe Coding era, AI can help you quickly generate code, but the overall system architecture design still needs your own thinking and planning. As long as you have architecture design awareness and enough accumulation, anyone can become an architect!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
