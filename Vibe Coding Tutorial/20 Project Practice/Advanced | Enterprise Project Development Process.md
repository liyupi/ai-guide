# Enterprise Project Development Process

> Revealing how major tech company projects are born


Hello, I'm Programmer Fish Skin.

In previous articles, we learned the Vibe Coding project development process and practiced many personal projects. Most of these projects were completed alone—from requirements to design to development to deployment, fully under your control.

But you might be curious: what's the project development process like in enterprises? Especially those projects with millions of users in major tech companies—what's the real difference from the projects we build while learning programming?

Honestly, the difference is huge! Personal projects are solo efforts where you control your own destiny without dragging down teammates. But enterprise project development is like raiding in a party—everyone's in the same boat, and each person affects the entire project.

![](https://pic.yupi.icu/5563/202311060822776.png)

I interned at several companies during college, and I must say, the development process at major tech companies is quite different from other companies. For most students, if you haven't worked at a major tech company, you probably know nothing about many aspects of the development process.

So this article reveals the project development process at major tech companies to help broaden your horizons. Even if you're using Vibe Coding for personal projects now, understanding enterprise development processes will make your projects more standardized and professional. Moreover, if you want to work at a major tech company in the future, understanding these processes in advance will make you more competitive.

![](https://pic.yupi.icu/5563/202311060822458.png)

If you want a more intuitive understanding of the project development process at major tech companies, I highly recommend watching my video: [How Major Tech Company Projects Are Made](https://www.bilibili.com/video/BV11q4y1T7kY/). Combine the video with this article for better learning results.



### Development Process Panorama

To standardize teams and ensure project progress, the development process at major tech companies is generally quite complex. It can be divided into many stages, summarized in a mind map:

![Enterprise Project Development Process Mind Map](https://pic.yupi.icu/roadmap/enterprise-project-development-process.png)

It should be noted that the above stages are not executed strictly in top-to-bottom order; there may be overlaps between stages. For example, **technology selection** should actually be considered during the **design phase**.

Having worked for over a year, I've been through the complete development process of multiple projects. Below, from my perspective, I'll take you through a quick run-through~

(For entertainment purposes, the following story contains fictional elements)



## Requirements Phase

It's Monday, and Fish Skin arrives at the company on his small electric scooter as usual, unaware that a nightmare awaits him.

### Requirements Generation

At ten in the morning, the product manager finds Fish Skin and tells him: users have reported many features aren't easy to use after our system launched; we need major changes.

The boss also finds Fish Skin and tells him: I opened the page today and it took over ten seconds to load. Our system's performance is terrible!

Fish Skin thinks to himself: Oh no, I'm done! Looks like we'll need to build a new project. More meetings ahead.

![](https://pic.yupi.icu/5563/202311060822455.png)

Sure enough, not long after, a "Welcome to join the meeting" invitation pops up on the screen.



### Requirements Review

The next morning, the boss, product manager, testers, several senior developers, and Fish Skin gather in the conference room to discuss in detail whether the requirements mentioned yesterday **are reasonable and should be done**.

The product manager opens the document and says: For this iteration, we need to work on these requirements. Let me explain in detail, and everyone assess whether there are any problems.



### Requirements Analysis

Next, as the product manager is talking non-stop to the screen, the senior developer next to her can't sit still.

Senior Developer: This requirement is unreasonable!

Product Manager: Why is it unreasonable? Users have this need!

Senior Developer: I know, but it can't be implemented!

Thus begins the classic product-development showdown...

![](https://pic.yupi.icu/5563/202311060822360.png)

Meanwhile, Fish Skin is hiding in the corner, calmly analyzing **how to implement this requirement**. After a while, he proposes a solution with low changes and fast implementation, calming the war.

In the AI era, we can also use AI tools (like ChatGPT, Cursor) to assist in requirements analysis, quickly generating multiple technical solutions for comparison, greatly improving the efficiency of requirements analysis.



### Scheduling

After confirming the requirements are reasonable and achievable, the product manager asks: When can this requirement go live?

Senior Developer: I'm busy this week, next week.

Product Manager: Users might be in a hurry, they need it this week!

Senior Developer: I know, but I can't finish it!

Thus begins the classic product-development showdown...

![](https://pic.yupi.icu/5563/202311060822785.png)

Fish Skin: How about we split this requirement into feature A and feature B? I'll finish feature A this week, schedule feature B for testing next Tuesday, and go live next Thursday?

Like this, we arranged planned completion dates for each requirement one by one.



## Design Phase

The meeting is finally over. Checking the time, it's already time to get off work!

Sigh, the requirements discussion is complete, the product manager's work is somewhat done, but Fish Skin's work is just beginning.

Ready to start writing code right away?

**No, planning how to write code is more important than writing code.**



### Architecture Design

Fish Skin opens documentation and diagramming software, starts organizing the entire system, designing from overall to local: the system's layered structure, interfaces and communication methods between layers, important modules included in each layer, physical deployment methods for each module, and so on.

![Architecture Design of the Well-Known Dubbo Framework](https://pic.yupi.icu/5563/202311060822027.png)

Now with AI tools, we can use AI to assist in generating architecture diagrams, analyzing pros and cons of architecture solutions, and even let AI help us with technical research, greatly improving design efficiency. I recommend watching Fish Skin's [AI Drawing Nanny-Level Guide and Tips Sharing Video](https://www.bilibili.com/video/BV1DP7JzAE7k/).



### High-Level Design

After writing the architecture design, Fish Skin starts analyzing requirements against the PRD (Product Requirements Document) written by the product manager, then organizes the functional modules the system needs, again from overall to local, and analyzes what sub-modules each functional module contains.

Compared to abstract architecture design, high-level design is more closely related to requirements and is a refinement of architecture design.

Let me use an analogy: you're building a house. Architecture design considers the overall picture—how many floors total, how to connect pipes on each floor, how many units per floor, how to lay the foundation, etc. High-level design considers how to divide the interior of each unit—where is the living room, where is the bathroom.

> In many cases, high-level design and architecture design might be in one document without clear separation.



### Detailed Design

After deciding what functions the system has, Fish Skin starts analyzing specifically how to implement each function, what algorithms to use, what details to focus on, etc.



### Solution Alignment

After writing the design document, in the next meeting, Fish Skin discusses the designed solution with other developers (frontend, backend, etc.), ultimately producing a unified solution, then everyone divides the work and gets started.



### Test Case Design

To ensure system functionality is normal and stable, testers (or QA) are very important. For detailed learning about software testing, see [Software Testing Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1990755616108359682). Testing isn't just clicking around the webpage a few times like we do with our own projects.

In large companies, to ensure test coverage and improve testing efficiency, test cases generally need to be designed. For example: user clicks "Login" without entering any data, expected result is warning the user to enter username and password.

![Test Case Management](https://pic.yupi.icu/5563/202311060822534.png)

After test cases are designed, they need review by others, not just handed to testers. Because one person can easily overlook many testing details, it's best to have developers more familiar with the code help supplement them.

Fish Skin also wrote several cases that testing might miss, confirmed them with the tester, trying to expose problems in the testing phase rather than in production.



## Development Preparation

After writing design documents for nearly a week, finally ready to start building the project. But before that, some preparation work is needed.



### Technical Research

Technology is developing so fast now, with new technologies emerging endlessly. So Fish Skin first researches technologies that the project needs or might need.

In the AI era, technical research has become more efficient. We can use AI tools to quickly understand new technologies, compare different solutions, and even let AI help us generate technology selection reports.



### Technology Selection

Through research, Fish Skin found several technologies that can meet requirements, but he starts struggling: with so many technologies, which one should I use? Should I use SSM framework or Spring Boot? Guava or Apache Commons?

Fish Skin opens the documentation software again, starts comparing pros and cons of different technologies. What a headache—there are too many factors to consider in technology selection, such as:

- From a technical perspective alone: performance, ease of use, stability, mainstream status and ecosystem, documentation detail
- Combined with team: team members' familiarity with the technology, control level (is anyone proficient in this technology)
- Combined with business: whether it adapts to business scale (single machine or microservices), whether it adapts to business (read-heavy, write-heavy, or analysis-heavy)

For key projects, Fish Skin doesn't dare to be completely certain about selection, so after writing his selection document, he discusses it with colleagues and Leader before final confirmation.



### Resource Application

After confirming technology, you need to apply for resources. For example, Fish Skin uses MySQL database, but where does this MySQL come from?

In the past, Fish Skin would buy a cloud server and set up MySQL himself. But in enterprises, there's generally a platform for centralized management and resource allocation—just fill in the budget on the platform, wait for leader approval, then wait for resources to be issued. Absolutely must not privately use your own or purchase external servers to deploy projects—it's not secure!

Fish Skin directly applied for a cloud database worth over 20,000 per year this time. Really feels great!

![](https://pic.yupi.icu/5563/202311060822734.png)



### Environment Preparation

After applying for resources like databases, Fish Skin builds an identical local development environment and test environment according to the applied machine version, so he can connect directly later.



### Project Initialization

After the environment is ready, since it's a new project, Fish Skin needs to create a minimal runnable initialization project demo, using **scaffolding** to automatically generate code instead of starting from zero creating files one by one and typing repetitive code.

Now there's an even smarter way: use AI tools (like Cursor, GitHub Copilot) to assist in project initialization and generate template code, greatly saving time.



### Dependency Installation

After generating project code, Fish Skin uses package management tools (frontend yarn/npm, Java Maven/Gradle, etc.) to automatically install dependencies, and the project demo can run!



## Development Phase

After前期 preparation is complete, we finally reach the coding phase that programmer friends are most familiar with, and Fish Skin's favorite phase.

![](https://pic.yupi.icu/5563/202311060822531.png)

Because when designing solutions, you need to stay calm and think carefully—you can't listen to music while doing it. But after the solution design is done and you know exactly what to do, coding implementation is simple, at most encountering some pitfalls that you search online to solve.



### Local Development

When developing, Fish Skin generally writes code locally first. By configuring hot update tools, code updates automatically recompile and package without manually restarting the project, greatly improving development efficiency.

By the way, enterprise development uses version control systems like Git. Remember to create your own branch before developing, and develop on that branch.



### Remote Development

Now there's another popular remote development method—editing remote files like editing local files, directly modifying code on the server. Generally each developer has their own development machine, and remote development saves the trouble of repeated deployment and debugging, improving efficiency. Generally use development tools like VSCode, install remote development plugins to achieve this. Fish Skin previously shared a simple [VSCode Remote Development Practical Video](https://www.bilibili.com/video/BV1s64y167cM), you can check it out.



### AI-Assisted Development

In 2025, AI-assisted development has become mainstream. Fish Skin now often uses AI tools like Cursor, GitHub Copilot when writing code. They can:

- Auto-complete code, improving coding efficiency
- Generate unit tests, ensuring code quality
- Explain complex code, helping understanding
- Discover potential bugs, early warning
- Refactor and optimize code, improving maintainability

I recommend everyone use tools from the [AI Resource Collection](https://ai.codefather.cn/) to improve development efficiency.

![AI Resource Collection Website](https://pic.yupi.icu/1/AI%E8%B5%84%E6%BA%90%E5%A4%A7%E5%85%A8%E7%BD%91%E7%AB%99.png)



### Code Optimization

When writing code, Fish Skin always maintains the good habit of actively optimizing code, focusing on time and space complexity. And when there's too much repeated code, he finds ways to abstract it into functions or use design patterns. I previously wrote an article sharing my programming habits: [My Little Stubbornness When Writing Code](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247497781&idx=1&sn=9c5ec35cda90ca080ba1dbfa78429275&scene=21#wechat_redirect).



### Unit Testing

Attention! Don't think testing is just the tester's job when you hear the word. Developers also need to write small-granularity tests to be responsible for their own code.

Fish Skin generally writes unit tests for each database read/write function and business logic function. For Java, generally use tools like JUnit, and can also use Jacoco to generate test coverage reports. After modifying key code each time, execute unit tests once to prevent unexpected errors.

![Jacoco Test Coverage Report](https://pic.yupi.icu/5563/202311060822942.png)

Now you can also use AI tools to automatically generate unit test code, saving much repetitive labor.



### Development Integration

Fish Skin finally finished writing the backend code and completed self-testing. Next is packaging the written code, publishing the executable project package to the test server, and doing integration testing with the frontend student—letting him request my interface to verify whether system functionality works.



## Testing and Verification

After Fish Skin and the frontend finish integration, he informs the testers and product manager.

Testing and verification is a crucial link in enterprises, arguably the last line of defense. The purpose of testing is to find bugs, try to discover problems in the system, and nip them in the testing phase.

In enterprises, there are many types of testing and verification.



### Integration Testing

Integration testing has larger granularity than unit testing, putting multiple modules or code units together to verify integration and calling relationships between modules.

Because the execution of a single function might be normal, but combining multiple functions to call sequentially might cause problems.

Let me use an analogy: we have a bread-eating system:

Function A: Little Fish eats one bread

Function B: Little Pi eats one bread

Each time there's only one bread. Executing function A and B independently is allowed. But if both execute together, the one that executes later will error.

![](https://pic.yupi.icu/5563/202311060822513.png)



### System Testing

System testing has even larger granularity than integration testing. The test object is the entire system, not only including software but possibly covering hardware testing as well.



### Product Experience

Besides testers verifying system usability, the product manager also needs to experience whether the functionality meets expectations and is easy to use. Most of the time, the product manager will propose modification suggestions during experience, and development might need to make some more changes.



### Acceptance Testing

Testers and the product manager finally indicate no problems. Then comes the final step—giving the entire product or feature to end users to experience. Only when the boss/users say there's no problem is there really no problem!



## Submission Phase

After the system has no problems, Fish Skin can publish the code to the remote repository, generally using version control systems like Git and SVN.

### Code Submission

Fish Skin first triggers code submission locally (git commit). To ensure standards, large projects generally use submission detection plugins (like Husky, pre-commit hook) to prevent you from submitting incorrect code.

Modern code submission also automatically triggers:
- Code format checking (Prettier, ESLint)
- Unit test execution
- Code standard checking (CheckStyle, SonarLint)



### Code Push

The next step is pushing local submissions to the remote branch with the same name. Generally major tech companies have push detection tools that detect code errors, cyclomatic complexity, code standards, etc.—similar to submission detection, preventing you from pushing incorrect or non-standard code.



### Merge Request

After the code branch is pushed to remote, Fish Skin initiates a branch merge request (MR or PR), hoping to merge that branch's code into the main branch (code without problems).

![Initiating New Merge Request](https://pic.yupi.icu/5563/202311060822490.png)



### Code Review

Initiating a merge request doesn't mean you can merge directly—you also need to pass code review, or CR.

Review is divided into two methods: human review and machine review.

I believe many students know about human review—generally your supervisor and other project leads read and comment on your code. If they think there are no problems, they Approve (pass), otherwise send it back for modification.

What's machine review? It's actually machines automatically detecting whether your code meets standards, whether it can successfully build automatically, etc. Generally configured by project leads, it can help discover some problems hard for humans to find.

When first encountering new projects, Fish Skin was often tortured by machine review, frequently being prompted with inexplicable code problems like plus signs need line breaks, need blank lines at end of files, etc. But after paying attention to coding habits, he naturally adapted—really good.

Now there are also AI Code Review tools that can automatically discover problems in code, propose optimization suggestions, further improving code quality.



## Release Phase

After code review passes, Fish Skin's project code can be released and go live.

![](https://pic.yupi.icu/5563/202311060822491.png)

### Packaging and Build

Traditional release method is developers pulling code on the production server, then installing dependencies, then using tools to package and build the code to get deployment packages, running through technologies like Nginx, Tomcat, Docker.

But this has low efficiency with lots of repetitive work. So major tech companies generally use automated build tools like Jenkins, GitLab CI, GitHub Actions and other CI/CD tools. After code is merged to the main branch, machines automatically package and build the code into the final deployment package.



### Pre-Release

To prevent problems on launch, we generally first deploy the project in a pre-release environment, then observe whether it can run normally. The pre-release environment configuration is completely identical to production, but only internal personnel can access it.



### Official Release

After pre-release testing is normal, Fish Skin finally waits for this launch moment. Large projects are generally deployed on multiple machines, so it's impossible to log into machines one by one to publish deployment packages.

Generally companies provide visual release platforms—select machines that need release (generally first canary, selecting a small portion of machines, then full release), click one-click release, wait for project manager approval to pass, then leave it to the machine for automatic deployment!

In the cloud-native era, many companies use Kubernetes for container orchestration and automatic deployment, making the release process more automated and standardized.



## Follow-up

Fish Skin naively thought that after the project went live, he could relax. But later discovered that after project launch, you still need to stay alert. Although it's been tested, unexpected small bugs still appear from time to time, really testing your mentality.

![](https://pic.yupi.icu/5563/202311060823102.png)

Let's see what Fish Skin did after launch?



### Monitoring and Operations

Fish Skin regularly checks the project's monitoring dashboard, observing the project's running status, machine load, interface response time, error rate, and other key metrics.

Modern monitoring systems are very powerful, able to monitor various system metrics in real-time and immediately alert when anomalies are detected. Common monitoring tools include:

- Prometheus + Grafana: open-source monitoring solution
- ELK (Elasticsearch + Logstash + Kibana): log collection and analysis
- SkyWalking: distributed tracing system
- Cloud vendor monitoring services (Alibaba Cloud Monitoring, Tencent Cloud Monitoring, etc.)

Fish Skin shared what he learned. If you want to understand how major tech companies monitor projects, see [Prometheus + Grafana Observability Practical Nanny-Level Tutorial Video](https://www.bilibili.com/video/BV1QPYDztEtW).



### Statistical Analysis

Fish Skin added some logs in the code, and can use log collection and visualization platforms like ELK to analyze these logs, thereby perceiving user behavior and further optimizing business and systems.

For example, I'll statistics the time users spend executing SQL queries, and specifically optimize slow SQL with high repetition rates.



### Incident Feedback

Sometimes users themselves can't clearly describe bugs, and historical bugs aren't easy to find. So inside companies there's generally an incident feedback platform. When internal personnel like product managers receive bugs, they publish a bug incident on that platform, detailing the time, conditions, and details of the bug appearance, facilitating our concentrated analysis and problem handling.

![Incident Feedback Platform](https://pic.yupi.icu/5563/202311060823531.png)



### Documentation

Each time new features and projects go live, Fish Skin documents the project background, design solutions, development process, and some pitfalls, facilitating other students' future understanding of the project—this is very important! Benefits both yourself and others.

Good documentation can:
- Help newcomers quickly understand the project
- Record technical decisions and evolution history
- Avoid repeated pitfalls
- Facilitate subsequent maintenance and iteration



### Iteration and Optimization

Finally, the end of one requirement is often just the beginning of another. Like the project Fish Skin is recently following—phase 1 leads to phase 2, and phase 3 comes before phase 2 is finished. Also need to find time to optimize previous code. These days are endless, no hope in sight!



## Development Process Comparison

To help everyone more clearly understand the difference between enterprise project development and personal project development, Fish Skin compiled a comparison table:

| Phase | Personal Projects | Enterprise Projects |
|-------|------------------|---------------------|
| **Requirements** | Do whatever you want | Requirements review, requirements analysis, scheduling |
| **Design** | Write whatever comes to mind | Architecture design, high-level design, detailed design, solution review |
| **Development** | One person writing code | Multi-person collaboration, branch management, code standards |
| **Testing** | Click around yourself | Unit tests, integration tests, system tests, test cases |
| **Deployment** | Deploy however | Pre-release, canary release, full release |
| **After Launch** | Ignore it | Monitoring, log analysis, bug fixes, iteration optimization |

You can see that enterprise project development process is much more complex, but these processes are all to ensure project quality and stability.



## Learning Suggestions

### How to Learn Enterprise Project Development Process?

1) Learn through project practice: The best learning method is participating in real enterprise projects. If still a student or just started working, recommend observing the team's development process more and actively participating in each phase.

2) Follow tutorials to build complete projects: If you don't have enterprise project experience, you can learn from [Fish Skin's Practical Project Tutorials](https://www.codefather.cn/post/1797431216467001345). [Programming Navigation's Project Tutorials](https://www.codefather.cn/post/1797431216467001345) are all designed according to enterprise development process, including complete phases like requirements analysis, architecture design, development, testing, and deployment.

3) Learn Git and CI/CD: Version control and automated deployment are foundations of enterprise development, key learning areas. Recommend learning [Git Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866) and [CI/CD Continuous Integration Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1990755091384152066).

4) Understand agile development: Most modern internet companies use agile development. Understand concepts like Scrum, Sprint, daily standups.



### Recommended Learning Path

To summarize, if you want to systematically learn enterprise project development, recommend learning related technologies in the following order:

1. [Git and GitHub Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866): Master version control
2. [Software Engineering Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190653197918210): Understand development standards and design patterns
3. [DevOps Engineer Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1990755061927555073): Understand DevOps practices
4. [CI/CD Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1990755091384152066): Master automated deployment
5. Follow [Fish Skin's Project Tutorials](https://www.codefather.cn/post/1797431216467001345) to build complete projects: Experience enterprise-level project development process



## Recommended Resources

### Video Tutorials

- ⭐ [Fish Skin's Major Tech Company Project Development Process Video](https://www.bilibili.com/video/BV11q4y1T7kY/): How major tech company projects are made

### Project Practice

- ⭐ [Programming Navigation - Fish Skin Original Project Tutorial Series](https://www.codefather.cn/post/1797431216467001345): Enterprise-level project development complete process
- [Project Learning Suggestions](https://www.codefather.cn/post/xiangmu-xuexijianyi): How to learn projects

### Tools and Platforms

- [Git](https://git-scm.com/): Version control system
- [GitHub](https://github.com/) / [GitLab](https://about.gitlab.com/): Code hosting platforms
- [Jenkins](https://www.jenkins.io/): Automated build tool
- [Jira](https://www.atlassian.com/software/jira): Project management tool
- [ZenTao](https://www.zentao.net/): Domestic project management tool

### Tech Blogs

- [Atlassian Blog](https://www.atlassian.com/blog): Agile development and project management
- [GitLab Blog](https://about.gitlab.com/blog/): DevOps and collaboration processes
- [Spotify Engineering](https://engineering.atspotify.com/): Spotify team collaboration
- [Netflix TechBlog](https://netflixtechblog.com/): Netflix R&D effectiveness



## In Conclusion

After reading this article, I believe you have a clearer understanding of enterprise project development process. The biggest difference between enterprise development and personal development is: enterprise development emphasizes process, standards, collaboration, and quality assurance, while personal development focuses more on rapid feature implementation.

You might ask: What's the relationship between learning Vibe Coding and understanding enterprise development process?

Actually, there's a big relationship. Although Vibe Coding allows us to quickly develop projects, many concepts and practices of enterprise-level projects are still worth learning. Things like requirements analysis, architecture design, code review, automated testing, monitoring and operations—these are all key links to ensuring project quality.

Even if you use AI for development, you must follow these basic development standards. Good processes and standards won't limit your creativity, but will make your project more stable and maintainable.

If you want to work at a major tech company, recommend understanding enterprise project development process in advance and learning related tools and methodologies. Follow my project tutorials to build a few complete projects and practice enterprise-level project development process—this will make you more competitive in job seeking and work.

I recommend reading my previous article: [Major Tech Company Secrets! 30 Tips to Improve Team R&D Efficiency](https://www.codefather.cn/post/1996475461198192641) to learn more major tech company R&D practices.

Now, it's time to truly use the knowledge you've learned and start your own creation journey.

Keep it up, future hit product founders! 💪

![](https://pic.yupi.icu/1/%E5%8A%A0%E6%B2%B9%E8%A1%A8%E6%83%85%E5%8C%85.jpeg)

