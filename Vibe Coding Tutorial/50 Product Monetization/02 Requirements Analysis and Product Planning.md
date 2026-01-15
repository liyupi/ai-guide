# Requirements Analysis and Product Planning

> Think clearly what to do, so you can do it better



Hello everyone, I'm Fish Skin. Before making any product, the first thing we must do is **requirements analysis**.

What is requirements analysis? Simply put, it's analyzing and clarifying user requirements.

Then why do requirements analysis? How to do requirements analysis well? Are there any precautions?

This article, I'll combine my experience making products to take everyone through understanding requirements analysis methods and techniques. Whether you're using Vibe Coding to do personal projects, or want to make a real product, these methods can help you.



## Why Do Requirements Analysis?

Let me give you a personal experience. Once a good buddy I hadn't seen in years came to Shanghai to visit me. Because we're very close, I thought I'd treat him to a seafood buffet, so I directly made a reservation. Result? When I brought him to the seafood restaurant, he told me: Bro, I'm allergic to seafood...

The result was very awkward, wasting the reservation fee and time for nothing. This is the result of not doing requirements analysis.

Before we develop projects and make products, the same principle applies. If you only act on momentary impulse or subjective speculation, ignoring users' real needs, you might spend a lot of manpower and resources, only to make a product users don't need at all.

Like when I first did programming knowledge sharing, I suffered from not doing requirements analysis. With passion I updated many videos I thought were useful, but didn't get many likes. Looking back, it was just self-indulgence.

So, requirements analysis is crucial. You can think of it as a bridge, a bridge connecting our product and users, able to help us better reach users' hearts, clarify what we need to do.

> Note, requirements analysis isn't only for product managers and bosses! For programmers, requirements analysis is equally crucial. This determines whether your subsequent development work is meaningful. Never be a "robot" who only listens to orders and writes code.



## What Does Requirements Analysis Involve?

About requirements analysis, there are many methodologies online. I've summarized these methods and will explain them to you from 3 aspects.



### Three Aspects

The first aspect is **starting from yourself**, I call it "free analysis." Making products should be a fun thing, why so many rules and constraints? Whatever ideas you have, whatever you want to make, first record as much as possible freely.

When I decided to make Yu Smart AI, I had roughly thought out what functions to make, like AI chat, AI drawing, AI Mask, AI Navigation, AI writing books that everyone has. This step doesn't need real "analysis," just imagine freely, diverge thinking.

The second aspect is **starting from users**. If you're only learning, making things for yourself for fun, then only doing the first aspect's free analysis is also reasonable. But if you want to make an attractive online product that more people use, you definitely need to return to users, be user-centric.

In one sentence: Confirm **what users need, what pain points they have**, to screen or improve the functions we need to make, avoid self-indulgence.

There are many methods, like common questionnaires, communicating with users, meeting discussions, etc. For our startup small team, we ourselves are users, so when we do requirements analysis, first we all meet and discuss, everyone thinks about "whether I would use this function." If for some function we all feel we wouldn't use it, then definitely don't do it; and if for some function everyone thinks "Damn, this is awesome," then this might be our core highlight function.

The third aspect is **starting from competitors**, also called competitive product analysis. When you're not clear what functions to make, have no ideas, go experience similar products, believe you'll have many ideas.

Many students learning programming often ask: how to expand projects? The answer is: look at what functions similar projects have, add them to your project.

But one thing to note, your competitors also might not have done some functions perfectly. When experiencing competitor products, can record your real usage experience, take the essence and discard the dross, have possibility to surpass them.



### Clarify Requirements

Through the above 3 aspects of thinking and practice, we can basically confirm the core functions to make (analogous to writing an outline when you write an essay).

Next need to further decompose and refine requirements, try to clarify each small function point, and specifically what to do (analogous to filling content according to your outline).

For example, the core function our Yu Smart AI wants to make is AI chat, can be decomposed into:

1. Create AI chat
2. View my AI chat list
3. View chat information
4. Send chat message
5. AI intelligent answer
6. View chat message records
7. Message toolbar

Can also further decompose certain functions, like message toolbar is divided into: copy message, voice reading, download message, etc.



### Prioritization

After we refine requirements, we might surprisingly discover: so many things to do!

At this time, some students might plan to give up: so troublesome, won't do it!

Don't panic, no system can be done in one step. What we need to do is prioritize requirements, decide which to do first, which later, then implement step by step.

So how to divide priorities?

A relatively common method is based on requirement importance, urgency, influence scope, implementation complexity and other factors, divide requirements into these 4 levels: P0 - P3.

- P0: Highest priority requirements, must have. Without this function the website cannot go online. Like Yu Smart AI's chat and content review functions.
- P1: Priority requirements to do, best to have. Generally refers to functions that aren't urgent in early stage, but must be done later as highlight functions. Like Yu Smart AI's share, image-to-image functions.
- P2: Medium priority requirements, can have. Generally refers to requirements that can improve user experience, bring some value, can do when time resources allow. Like Yu Smart AI's assistant advanced configuration functions.
- P3: Lowest priority requirements, optional. Either bring relatively low value, or implementation complexity is high, can wait until team members have slack time to do. Like Yu Smart AI's... uh we don't seem to have P3 requirements yet, no one can slack under Fish Skin (🐶 just joking)!

After dividing priorities this way, everyone just prioritize doing P0. After P0 is done, first go online with a version, quickly find users to verify whether requirements are really reasonable and can bring value, then continue subsequent development and iteration.



### Requirements Management

Even when requirements are few in early stage, still need to record and manage requirements. Rather than storing all the above information in your mind, otherwise situations like "Eh, why did I want to make this function?" will appear.

So how to do requirements management?

The simplest way is to use documents to record. Don't think of this as very complex, just like recording what you want to eat today, write it down in a list.

Recommend using Yuque, Feishu and other online knowledge base websites, rather than local recording, so can sync messages with team students in real time, collaborative editing.

Relatively more formal, can use a spreadsheet to make a requirements schedule table, record each function, module, details, priority and other information

![](https://pic.yupi.icu/1/image-20230704115312375.png)

Can also use XMind and other mind map tools to divide requirements into levels, not only clearer when team collaborates, also looks better when doing PPT to raise investment.

Even more formal, can use professional requirements (project) management systems like Jira, Tapd, Teambition, can help manage more complex, multi-dependency requirements.

Note, requirements management is something to continuously do. And not that all requirements and functions you can immediately think of, but once have any ideas and inspiration, absolutely don't miss them, must immediately take out your phone and record them!



## Don't Let Fake Requirements Hurt You!

Last but most important point, don't let fake requirements hurt you!

This is not only said to product managers and bosses, but even more emphasized to all students who actually do requirements (like programmers, testers).

If we compare complete system functions to a jigsaw puzzle, fake requirements are like a defective irregular piece, looks somewhat useful, but actually can't help us complete the puzzle, waste our time.

So, how do we avoid fake requirements?

Besides the requirements analysis, user feedback, prioritization, requirements management mentioned above, we should also let as many team students as possible participate, more communication and validation, repeated evaluation, can also use data analysis and other means for scientific verification.

Each of us as a team member should also proactively apply to participate in requirement review, master more information, help team make more correct decisions.

Sometimes, as a small developer in a large enterprise team, we might not be able to overly participate in requirement analysis and project decision-making. But if discover requirements are unreasonable, should also raise and feedback as early as possible, rather than foolishly spending time and effort on useless requirements (or even useless systems).

Our Yu Smart AI actually also had fake requirements, also because of one of my decision mistakes, made a nearly useless function. But later we discovered this through some means and optimized the system. Of course, that's later, will share with you in future chapters.

So, when development students encounter fake requirements, hope you can confidently say to product: this requirement is unreasonable! I won't do this requirement!



---



Requirements analysis is the first step to making good products, also the most important step. Whether you're using Vibe Coding to do personal projects, or want to make a real product, must attach importance to requirements analysis.

Remember these key points:

1. Requirements analysis must start from three aspects: yourself, users, competitors
2. Must refine requirements into specific function points
3. Must prioritize requirements, do core functions first
4. Must continuously manage and optimize requirements
5. Must be wary of fake requirements, more communication and validation

In the Vibe Coding era, the cost of implementing requirements is already very low. But, thinking clearly what to do is still most important. Only when direction is right can you get twice the result with half the effort.

Go for it, look forward to seeing you make valuable products! 💪


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
