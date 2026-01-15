# Documentation Accumulation and Knowledge Management

> Record it, so you can go further



Hello everyone, I'm Fish Skin.

Let me share a small story first. When I was a sophomore, I did a project with a team. As I wrote more code for the project, I slowly started leading the project, until I knew the entire project's logic by heart. Team members would come to me when they encountered problems.

But, due to personal time reasons, later I withdrew from the team and stopped doing it, carefully explained the code once to other students.

Guess what happened?

After I withdrew, team members would frequently come ask me about this project. Even more ridiculous, a month later, this project shut down!

When I later asked other students why the project shut down, they said displeased: You don't write documentation, many parts of the project are incomprehensible, can't continue.

Only then did I realize: I had been focused on writing code for the project, but forgot to record my experience and project information, sync with other students, causing the parts I was responsible for to basically be something no one could take over.

Sigh, I was too inexperienced then. After that, whenever I do any project, I write documentation. Even if not for others, at least ensure I can understand the projects I wrote before.

This is also the core this article wants to share — **documentation accumulation**. Whether for individuals or teams, whether in learning, work, or projects, whether for programmers, product managers, or project managers, doing good documentation accumulation is crucial.

Below I'll share with everyone in turn: Why write documentation? How to write good documentation? How to manage documentation well?



## What Is Documentation?

Documentation is a carrier for recording, storing, and transmitting information.

Our project requirement tables, system design proposals, certain research reports, certain meeting records, resolved Bugs, even notes casually recorded when learning some video tutorial, are all documentation.



## Why Write Documentation?

Starting from the definition of documentation, we can already realize documentation's basic functions.

- Record information: collect temporary information
- Store information: prevent information loss and forgetting
- Transmit information: share information with others



Our human brain capacity is limited, can't remember all information. Writing documentation is essentially building our second brain.

Like my brain capacity is relatively small, so I have the habit of casually recording and writing documentation. Sometimes when walking on the road and have a good idea, I immediately take out my phone and record it.



### Value of Documentation to Projects

And for doing projects (especially enterprise large projects), documentation has even further value.

In the early stage of a project, documentation has the meaning of guiding the entire project to proceed smoothly. If we compare doing a project to building a skyscraper, then documentation is the building's blueprint. Without a blueprint, construction workers can only work blindly, whether it can be completed is hard to say, let alone guarantee the building's quality and safety.

Similarly, in the early stage of a project not writing documentation, no systematic plan and execution plan, team members will lose direction during development, often出现 delays, incompletes, rework situations.

> Students who've watched my livestream should know, each project start, I'll write requirements analysis, solution design, technology selection and other content in documentation. Before doing specific functions, also first write design implementation solutions in documentation, then write code. Although writing documentation takes a bit more time, it greatly reduces the entire project's work hours.



In the middle stage of a project, documentation's meaning is to **continuously** record and track project status, make information public and transparent within the team, thereby making correct choices, timely avoid risks.

To use an analogy, treat doing a project as running a marathon, documentation is the road signs along the way, will tell everyone where they've run to, how to run next; and if there's danger ahead, road signs will also warn everyone. Without documentation, everyone quickly scatters, fighting separately; one person encounters risk, might drag down the entire team.



In the late stage of a project, documentation's meaning is to help us review and summarize, continuously maintain the project and knowledge inheritance.

- Review and summarize: by reading documentation, we can review the complete process from project birth to end, thereby analyzing the reasons for the project's success or failure, facilitating us to learn from experience, helping the next project's success.
- Continuously maintain project: if this is a project needing continuous maintenance and updates, with documentation (like Bug manual, user manual), when project has problems, even if changing a project maintainer, can also quickly find solutions from documentation, won't appear "one person leaves, project dies" situation.
- Knowledge inheritance:沉淀 good documentation is predecessors' valuable experience, lessons, ideas and methods summary, very worth learning, in the future can bring inspiration and gains to more team students.



In summary, writing documentation is something that benefits both self and others, every word written is producing value.



---



After understanding the importance of documentation, how should we do good documentation accumulation?

Here we break down documentation accumulation, need to do two things well:

1. Write good documentation (this is prerequisite)
2. Manage documentation well



Below we explain separately.



## How to Write Good Documentation?

To want to write good documentation, we first need to understand "what is good documentation," then learn documentation writing tools and methods.



### What Is Good Documentation?

Several standards I personally judge whether documentation is good:

1) Can be understood by people, easy to understand

First, your documentation is for **people** to read. If recording your own learning notes, first ensure you can understand; if sharing documentation within team, ensure others can understand. If content that can be explained in one sentence, you use 20 sentences to explain in documentation, then even if you wrote documentation, others might still directly trouble you personally.



2) Clear structure, easy to find

Good documentation should be where others scan from top to bottom, know what you're writing, what you want to express, what I can get from your documentation, where I can find content I need.

Like this article, I used multi-level headings to divide article structure, you can directly through catalog outline quickly locate interested content to read.



3) Complete content, accurate expression

Good documentation is like a module in a project, it should be complete, highly cohesive, letting people only through this documentation be able to solve their problems.

For example, "Solution to Certain Java Bug" documentation should write out Bug's cause, analysis and investigation process, solution, experience summary. Rather than just throwing out the Bug, not saying how to solve it~ Eh, just playing~

Additionally, some vocabulary and sentence expressions in documentation must try to be as accurate as possible, can't be ambiguous!

For example, when our Yu Smart AI initially estimated costs, wrote "several servers, price accumulates to about ten thousand," "several" and "about ten thousand" are actually relatively vague vocabulary. Similar situations accumulated might lead to cost calculation errors and losses. Later we changed the above vocabulary to similar "1 server 4C 8G, price 1000 yuan / month," achieving more refined cost control.



Additionally, good documentation might have other standards, like product documentation facing users should ensure overall documentation style, layout consistent, bringing readers best experience. Good documentation writing also enhances user recognition of the team, thereby more willing to use the team's products.



### Writing Tools

To do good work, must first sharpen one's tools. Before introducing methods for writing good documentation, first share some writing tools.

Many years ago, writing documentation was basically using Word, but Word actually has many problems and shortcomings. Like need to manually adjust format yourself, same Word document due to compatibility issues can't open or layout is messy on another computer, etc.

So now I strongly recommend everyone learn Markdown (a lightweight markup language), can let you easily write code with consistent layout and format using the same set of syntax.

Like using "## Secondary Heading" to represent secondary heading, using "> Quote" to represent quote copy, etc.

Now many editor software support Markdown, like VS Code we usually use, JetBrains family bucket. But if choosing a local Markdown editor with best experience, I recommend everyone use Typora, this is also software I've used for many years.

In the process of writing documentation, also often need some drawing to assist understanding, like flowcharts, architecture diagrams, etc., can use online tool Draw.io, classic software Visio, etc. If need to draw mind maps, can use XMind. If need to generate some illustrations, can use currently very hot Midjourney (or our Yu Smart AI).

If you need to send documentation to other social media platforms, can directly copy and paste Markdown content to mdnice website, it will automatically help you generate articles with beautiful layout.

Additionally, with the development of web frontend technology, online documentation writing websites are also becoming more and more powerful. If need team collaboration, real-time sharing documentation, can choose tools like Yuque knowledge base, Tencent Docs, Feishu Docs, etc.



### Methods

#### "Copy"

First, to want to write good documentation, the first thing to do is "copy."

Oh no, for scholars, should be called "learning and borrowing."

If you can't write documentation, like project documentation, design documentation, user manuals, what to do?

Very simple, go online find excellent **finished products**, to imitate.

Not only writing documentation, doing social media, making products, writing papers, learning crafts, if you want to do anything well, the first thing should be: see how others do it, learn from others.

- You want to develop websites, go online find existing websites
- You want to make videos, go online find viral videos

This is the simplest truth. Many things have been done by predecessors, so even if others don't share tutorials, as long as you imitate, with some heart can also complete.

Plus now open source culture prevails, many projects and documentation are publicly visible on platforms like GitHub. When you need to write a document, directly first copy well-known project's README.md file, then keep original catalog outline, replace content with your own, get a very standard document, it's that simple.

When you've read and written more documentation, naturally can also form a set of documentation writing methods belonging to yourself (team).



#### Writing Process

Many people hate writing documentation because feel no ideas, don't know where to start, completely don't know what to write.

I also often used to create a blank document, then stare at it...

But later as writing次数 increased, I also cultivated a method that can quickly write content, I call it "writing process."

What is a process? You go to cafeteria to buy breakfast, first line up, then buy steamed bun, then pour soy milk, then find seat, this is a process engraved in DNA.

If you can also have a clear writing process, then writing is as simple as you buying breakfast.

How to do it specifically?

1) First think clearly about article structure, write outline according to theme

Like when I write this article, first write these subheadings: "What is documentation? Why write documentation? How to write good documentation? How to manage documentation?" Set down entire article's framework. Rather than writing from top to bottom aimlessly, writing wherever you think.

The process of writing outline itself is cultivating your structured thinking — structurally decompose complex problems. If you find writing outline is very difficult, then might try using timeline as outline, according to order from far to near, sequentially write your thoughts in each period.



2) Fill in blanks

As long as outline is determined, you have 100% information, this article you will definitely finish. Because what remains is filling in blanks under each chapter.

Like having a mentor plan what you need to do, you have a goal, easier to firmly execute.



3) Optimize

After writing rough content, we need to read documentation 2 - 3 times overall, perform appropriate optimization.

Like when we write code, although function is completed, code might be written poorly, need to modify a bit before submitting code.

List some common optimization points:

1. Fix typos
2. Add connecting words between subheadings, connect above and below, make content more coherent
3. Key points first, put documentation's key information at beginning, attract people to read
4. Illustrations and text, use more metaphors, make documentation easier to understand



Following this process, a complete documentation is born.



#### Continuous Optimization

Whether writing your own learning notes, or project documentation, user manuals, not finished after writing one version. Good documentation needs continuous optimization and iteration. If someone points out problems or documentation content is outdated, should timely fix and handle. Otherwise wrong documentation not only can't help people, but also produces misleading.

Like when we were developing Yu Smart AI, unfortunately referenced a nonsense expired documentation, making the already not rich team worse off.



#### Accumulation

Often friends ask me: Fish Skin, you usually work and are highly productive like a breeding sow, how do you do it?

Actually I have a habit, record things I find interesting in life, or suddenly thought of inspiration, organize every once in a while. Later I surprisingly discovered, some fragmented content could actually be strung together to tell, composed into an article.

Like playing a game, equipment you want to brush never appears, equipment fragments you don't care about actually accumulate a lot. Then one day, you discover fragments can all synthesize complete equipment, actually quite useful, this is unintentional planting willows creating shade.

Writing documentation is also same. Even if you can't write a comprehensive systematic documentation, when you encounter Bug at work, casually open a document to record; encounter Bug again, open previous document to record again. After many times, slightly organize, isn't a high-quality documentation here?



### Example

Take our Yu Smart AI as example. When first writing project initiation documentation, according to above "process" method, first set documentation outline:

1. Why do it? Project background
2. What to do? Requirements analysis
3. How to do? Design plan
4. How specifically to do? Work arrangements, etc.

Then one by one supplement and improve, after each meeting and going online, continuously update and improve this documentation.

In the process of improving documentation, I also see many previously recorded content, reminding myself not to go off track during this project.



## How to Manage Documentation Well?

As our project continuously iterates, documentation number also becomes more and more, more and more fragmented. How to manage these documents well, let everyone quickly find when need to read, this is a big problem.

Especially for large projects, suppose 100 people develop together, each person writes 10 documents that's 1000 documents. How to manage these 1000 documents?

First need an awareness: discovering problems early is much lower cost than solving problems later.

So managing documentation well should mainly rely on "early stage strategy" and "mid-stage continuous optimization," rather than later artificially organizing large amounts of documentation.

> Code shit mountain comes this way, more bad code piles up, less people dare to touch.

So first, before starting project, must establish a standardized **documentation system**.

1) Documentation online

As long as it's project/work related documentation, don't let everyone write locally, but directly use online documentation to **real-time collaborate**. Simple truth, you locally change a sentence, others locally also change same document's sentence, then whose version prevails?

Like all internal documentation of our Yu Smart AI uses Yuque knowledge base to host. All project information is public and transparent within team, thereby maximally eliminating information asymmetry.

And online knowledge base has another benefit, convenient to search and find, search entire knowledge base content with one click.



2) Grouping

As documentation or knowledge bases increase, will inevitably burden everyone's search. So I at **the very beginning** grouped all team internal knowledge bases by theme, as shown below:

![](https://pic.yupi.icu/1/image-20230705134114445.png)

Documents under each knowledge base also established corresponding groups:

![](https://pic.yupi.icu/1/image-20230705134325495.png)

Of course, grouping operation also needs to be done continuously. If at start there's no way to estimate what groups there will be, then wait until later need grouping, immediately create new one.



3) Access Control

So-called access control is letting some members only see part of documentation. Doing this is not only for security, can also let everyone focus on their own work, better find documentation they need.

Currently each knowledge base of our Yu Smart AI team has strict access control. Only when everyone needs to see certain knowledge base, I'll give them corresponding permissions. Of course this doesn't mean limiting team members' learning. If he's interested in certain knowledge base, can directly apply to view.

Mainstream online documentation software basically supports access control and permission management, no difficulty in implementation.



4) Cultivate Team Documentation Culture

Remember the story I shared at the beginning of this article? Some people might not have awareness of writing documentation, or just don't love writing documentation! If this person is also an important project contributor, then information he personally masters that team doesn't know will accumulate more, finally will appear "others can't touch his code," "once he leaves project dies" situation.

To nip this risk in the bud, I repeatedly emphasize to team members, must write more work documentation, timely sync information. Even for some important work, I'll make documentation part of everyone's work results. Slowly, everyone formed the habit of writing documentation, document classification.



---



Documentation accumulation is an important link in making good products. Whether you're using Vibe Coding to do personal projects, or want to make a real product, must attach importance to documentation writing and management.

Remember these key points:

1. Documentation is your second brain, record anytime
2. Good documentation should be easy to understand, clear structure, complete content
3. Learn to use Markdown and online documentation tools
4. Writing documentation should be processed: outline → fill in blanks → optimize
5. Documentation needs continuous optimization and accumulation

In the Vibe Coding era, AI can help you write code, but project ideas, design plans,踩过的 pits, these all need you to record yourself. Only沉淀 good documentation can let project go further.

Go for it, start developing the good habit of writing documentation from today! 💪


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
