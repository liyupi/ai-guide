# Project R&D Process Selection

> Fast or stable?



Hello everyone, I'm Fish Skin.

I wonder if everyone likes eating spicy snack strips (latiao)? I love them anyway.

When eating latiao, I would think: How are these delicious latiao made?

To satisfy my curiosity, I even searched online specifically, and was shocked!

I found that some latiao production processes are very "advanced," not relying entirely on workers to make them, but having a **production assembly line**. After preparing raw materials, machines sequentially complete mixing, stirring, cutting, seasoning, frying, cooling, packaging and other operations, while workers only need to supervise.

![](https://pic.yupi.icu/1/6f6e8ad610e6418e9556fb0fb95afda1.jpeg)

With such a clear set of processes, the entire latiao production process becomes orderly, workers (or machines) only need to do their own things step by step, overall efficiency is higher; and if every step is fully verified, latiao quality and safety will also be higher.

This is the importance of **standard processes**.

Returning to today's topic, if we want to develop and launch a product, we also need a set of standard R&D processes.

So-called R&D process refers to: **a series of work steps and methods** customized to efficiently complete product R&D. Team members only need to work according to these steps and methods in sequence, and can smoothly complete high-quality products.

So what kind of R&D process should teams customize when collaborating on development? Should R&D process steps be as many as possible, or as few as possible?

In this article, I'll combine my experience working at large companies and leading small teams to share in turn: large company's standard R&D process, small team's agile R&D, and our Fish Skin AI team's R&D process selection. Hope to help everyone open their minds, improve team project development efficiency and project quality.



## Large Company's Standard R&D Process

This is the focus shared in this article.

For large companies, often hundreds or thousands of people participate in a project together. So to ensure stable project progress, large company R&D processes are usually very **complete and complex**, including very many steps, and each step's requirements are also very strict.

I divide large company R&D process steps into several phases, summarized with a mind map, which will be clearer:

![Large company R&D process mind map](https://pic.yupi.icu/1/3334dda0-2177-4816-bc91-94e7d3b77bde.png)

If we use producing latiao as a metaphor for R&D projects. Then large company R&D project process is like the latiao production process using **standard assembly line** I mentioned at the beginning.

> Note, the above phases are not executed completely in top-to-bottom order, phases may overlap, like technical research and technology selection should actually be considered during the design phase.



### Requirements Phase

The goal of the requirements phase is: Clarify why do we want to make the product? What kind of product do we want to make? What functions should the product have?

Now, assume latiao is the product we want to make.

Since the requirements phase is the **very beginning** link in the R&D process, I will introduce it in detail divided into 4 sub-phases.



#### Requirement Generation

Why do we want to make latiao? Maybe after conducting market research, we found everyone loves eating latiao and making latiao can make a fortune; maybe we accidentally discovered an idea for improving latiao flavor; maybe we found our resources are very suitable for producing latiao, etc.

In the requirement generation phase, the most important thing is to collect and organize as many requirements as possible, don't let possible opportunities slip away.

Sometimes, a casual idea might be a very meaningful requirement.



#### Requirement Review

After collecting many requirements, we need to review the requirements, determine their feasibility, cost and benefit, requirements and risks, and whether they align with our product positioning, rather than doing everything.

Like if we plan to produce a new flavor of latiao, need to first research and evaluate whether the new flavor will be popular and whether it can be produced.



#### Requirements Analysis

After reviewing requirements, we need to further analyze the requirements, refining requirements into product **specific** functions or features, or work to be completed.

For example, to produce a new flavor of latiao, we need to determine latiao spiciness and specific flavor, develop new recipe, ensure latiao safety, design new packaging bag for latiao, etc.



#### Scheduling

After clarifying requirements through requirements analysis, we need to do requirements scheduling.

In this phase we need to formulate production plans, arranging completion priority order and implementation cycle for requirements based on requirement importance and required resources, etc.

For example when producing latiao, we first spend 1 month developing recipe, then spend 3 days purchasing raw materials, spend 3 days producing latiao, spend 1 day verifying safety, meanwhile spend 3 days designing new packaging bag for latiao.



### Design Phase

In the design phase our goal is: Think clearly in advance how do we make our product? How to implement functions?

For producing latiao, the design phase's goal is "confirm latiao recipe."

First, **architecture design** is like determining latiao's main materials and production process, ensuring that subsequently based on this we can make various different new flavors of latiao, rather than every new flavor's recipe being completely mixed from scratch (scalability).

**Outline design** is similar to overall conception of latiao, like type of chili, ratio of chili powder to flour, size of latiao, etc.

**Detailed design** is supplementing and improving outline design, deeply researching **details** of each ingredient in the recipe, determining specific requirements for each step. Like first put 3 grams of chili powder, then put 100 grams of flour, then mix and stir 3 times (I made this up).

After completing the above design, we need to share our design and discuss with other team members, ensuring everyone's **solution alignment**, ideas are completely consistent. Rather than waiting until after listing, letting different users eat latiao with different recipes.

In the design phase, not only product managers and R&D engineers are needed, test students also need to participate, conducting **test case design** in advance. Define standards for quality verification of latiao, for example specific spiciness between xx ~ xx, latiao length is 10 cm, etc.



### R&D Preparation

In the R&D preparation phase, what we need to do is: Prepare basic conditions needed for project R&D.

For example before formally producing latiao, we first need to conduct **technical research**, conducting research in advance on feasibility of implementing new flavor recipes by consulting materials. Then we need to conduct **technology selection**, choosing what tools or machines to use to mix recipes and cut latiao.

After completing technology selection, also need to conduct **resource application**, confirming team funds are enough for us to use advanced tools or machines, purchase raw materials and equip workers.

In large companies, resource application is often very strict. Like when I was at Tencent, wanting to apply for 1 server to deploy project required going through leadership, operations and several other layers of approval.

After applying for resources, we need to conduct **environment preparation**, finding a clean and hygienic site equipped with water and electricity to place latiao production machines and workers. In R&D process, environment preparation work is setting up development environment, installing software and tools necessary for development, etc.

Afterward, we can conduct **project initialization** and **dependency installation**, arranging machines and workers at designated positions, connecting water and electricity, starting machines, installing machine programs, etc., getting everything ready. In R&D process, we might use tools like scaffolding to automatically generate clean project initial code, and use package managers to install basic dependencies needed to run the project, then can happily write code!



### R&D Phase

The R&D phase is when programmers show their skills, this phase's goal is writing code to complete the project.

The R&D phase can be divided into: local development, remote development, code optimization, unit testing, development integration 5 small phases.

First, each developer can write code on their own computer (local development), or can choose to collaboratively develop code on the same public machine (remote development). After completing basic functions in development, need to conduct code optimization, like adding exception handling to improve robustness, using multi-threading to optimize performance, etc. Afterward, need to write basic unit tests themselves to verify code can run normally and return expected results. Finally, programmers need to cooperate with each other, conducting development integration, that is calling each other's code to verify complete functionality availability.

Metaphorically as producing latiao, this phase is machines and personnel cooperating with each other, completing latiao stirring, cutting, seasoning, inspection and other operations. Since I haven't participated in latiao production, I don't know if they still have manual tasting phase, if discovering bad taste, still need to fix the machine (programmers fix Bugs), or manually add some secret ingredients (code optimization).



### Testing and Verification

After completing development, we must conduct testing and verification, this phase's goal is: Ensure product functions run normally, eliminate Bugs!

Some students might ask: In the R&D phase, didn't programmers already write unit tests themselves?

But, unit testing is only a most basic guarantee, can only guarantee their own code has no problems; if multiple people's code needs to call and cooperate with each other, also need further testing — **integration testing**, to guarantee everyone's code integrated together also has no problems.

Besides unit testing and integration testing, relatively common test types also include system testing, acceptance testing.

**System testing** is after integration testing, conducting comprehensive functional and performance testing on the entire system, testing scope is larger.

And **acceptance testing** is usually the last phase of testing, confirming whether system meets actual requirements and user expectations.

Here there's also a concept of **product experience**, which is feeling product function pros and cons from real user perspective. Strictly speaking, product experience isn't only conducted during testing phase, but should run through entire development process, facilitating discovering problems and improving in advance.

Metaphorically as producing latiao, after we produce latiao, not only do we taste ourselves, but also need professional tasters to experience and inspect whether latiao recipe and production have problems.



### Submission Phase

The submission phase's goal is: Submit and push tested local code to remote repository, and merge to main branch, preparing for launch.

In actual development, since projects are maintained by multiple people, to reduce code conflicts and bad code, will adopt **code review** mechanism. Before wanting to merge code to main branch, must initiate MR (Merge Request) **merge request**, then have project负责人 (generally your leader or colleague) check your code, only allow merging after no problems.

This way, all code will be checked by at least 2 members, code quality will be higher, also reducing probability of launch Bugs.

Metaphorically as producing latiao, code review is like having professional food hygiene agencies inspect latiao production safety standards, if discovering any problems with recipe or production process, send back to redo.



### Release Phase

After going through "eighty-one tribulations," our project can finally be released!

First, we need to package the latiao we produced, turning into sellable packaging bags. Then not doing large-scale promotion and marketing from the start, but first giving some customers to taste, letting them give some reviews. If everyone praises the latiao, then can officially list latiao, going to the public.

In R&D process, we also need to **package and build** the completed development code. Then first conduct **pre-release** (or canary release), giving some users to experience; after confirming no problems, then **officially launch**.



### Follow-up

At this point, our R&D process isn't over yet! Can only say a round of launch is completed.

After product launches, we still need to continuously collect and accept user feedback opinions, and conduct statistical analysis on user reviews, thereby continuously optimizing and iterating our product.

In addition, documentation沉淀 is also very important, need to record all kinds of problems, materials, knowledge encountered in this R&D process, facilitating team continued improvement.



---

---

How about it, feel large company R&D process is very complex?

In fact, after completing first launch, every time we need to add new functions to product, must completely experience above process once! Even sometimes, just requirement review this one step needs to experience 1 - 2 weeks of discussion!

Although this kind of R&D process can guarantee project quality, it's not necessarily suitable for small teams, especially for startups, time is money.

So below share R&D process suitable for small teams — agile development.



## Small Team's Agile R&D

If the above large company R&D process focuses more on **specification and stability**, then agile development focuses more on **team collaboration and rapid iteration**.

In agile development, many steps of the above large company R&D process can be simplified, even omitted, very flexible.

For example in the morning we think about making a product, at noon team members meet together to discuss requirements and confirm core functions that must be done for product launch, in the afternoon directly start R&D writing code. First use fastest speed to complete core functions, usable is fine, then continuously discuss new requirements, continuously develop and launch, improve product.

Put more time invested in R&D, main theme is fast!

![Agile development process](https://pic.yupi.icu/1/image-20230712185656368.png)

If using agile R&D method to produce latiao, roughly like this:

Our team discovered people in a certain area really love eating latiao, then directly purely manually use hardworking hands to first make a few packs, fastest speed let these people taste; then based on these people's feedback to improve our recipe, upgrade our packaging; after big sales, then introduce machines, buy factory, batch automated production of latiao.

Need to note, agile development is a software development methodology, specific methods aren't just one, like Scrum, Kanban, extreme programming, etc. But roughly understanding its basic concepts and applicable scenarios is enough.



## R&D Process Selection

After understanding the above 2 R&D processes, how should we choose when doing projects?

First need to clarify a point: **no absolutely good choice**. Whatever R&D process, each has respective advantages, need to choose based on actual situation.

Although agile development pursues ultimate speed and flexibility, also needs high cooperation between team members, and brings greater risks. Possibly after investing several weeks of development time discover made a useless project. Relatively speaking, large company R&D process although needs to consume more early-stage resources and energy, but can bring higher product quality and R&D progress stability.

So for our Fish Skin AI team, choose to run fast or run stable?

The answer is: Only kids make choices, I want them all!

![](https://pic.yupi.icu/1/image-20230712184257231.png)

First, analyze our own actual situation:

1. We are a small team, without large company resources and infrastructure (like assembly line automated build platform)
2. We are making AI products, need rapid launch to seize market
3. Our team classmates are all in a 40 sqm small office, everyone can closely collaborate

From these points, we will obviously more tend toward agile development. But on the basis of agile development, we retained large company standard R&D process's design phase and submission phase, and gave website complete monitoring statistics, for continuously improving product.

Complete process is as follows:

![](https://pic.yupi.icu/1/image-20230712190738396.png)

We hope website development while pursuing speed, can balance scalability and code quality. Therefore, on one hand we invested more time in design phase, using more generalized architecture design to support entire system (like using microservices architecture, independently splitting payment center), thereby able to handle future business growth.

On the other hand, in collaborative development, we use Git to manage code, and adopt simplified Git Flow model, letting each R&D student create their own independent development branch. After各自 function development is completed, I am responsible for code review, after passing then merge code to main branch, thereby guaranteeing main branch stability.

Code review interface:

![Code review](https://pic.yupi.icu/1/image-20230712193216012.png)

Some students might ask: Why cut off the testing verification phase? You don't test when making products?

Under ideal circumstances, before product launch definitely need specialized test engineers to test and verify. But reality is, our team doesn't have test engineers!

So our strategy is:

1. First, frontend and backend engineers respectively develop and self-test functions. Before launch, I will meet with team members responsible for that function to verify whether functions are normal.
2. Second, problems cannot be completely handled, system is continuously improving. Therefore, we will launch as soon as possible, recruit some beta users to experience system and feedback Bugs.

This way, we can invest more time in R&D, while not losing attention to product quality and opportunities for continuous improvement.



---

R&D process selection has no absolute right or wrong, key is to customize based on team actual situation and project requirements.

Remember these key points:

1. Large company R&D process focuses on specification and stability, suitable for large teams
2. Agile development focuses on rapid iteration, suitable for small teams
3. Can combine advantages of both, customize process suitable for yourself
4. Must retain core links (like design, code review), simplify non-essential links
5. R&D process needs continuous optimization, continuously improve

In the Vibe Coding era, AI can help you quickly complete development work, but a good R&D process can make team collaboration more efficient, project quality more guaranteed.

Go for it, find R&D process suitable for yourself, let project run fast and stable~



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
