# Website Data Analysis Practice

> Drive product optimization with data



Some classmates asked me: Fish Skin bro, your team has so many website products, how do you all do data analysis?

![](https://pic.yupi.icu/1/1764078727145-d24f43f8-805e-48ee-91a7-363c40334731.png)

Actually there are many existing free resources that can let you effortlessly handle various data analysis scenarios.

- Website traffic statistics
- Frontend error monitoring
- User behavior analysis
- Custom business analysis
- Backend application monitoring analysis
- Backend resource monitoring analysis
- Backend custom metrics analysis

Whether you're using Vibe Coding to do personal projects, or want to make a real product, mastering website data analysis methods can help you understand user behavior and optimize product features. Lots of practical content, suggest bookmarking~

⭐️ Recommended video version: https://bilibili.com/video/BV1CkUDBiEMR



## Website Analysis Nanny-Level Tutorial

Let me first talk about the most basic **website traffic analysis**. You definitely want to know how many people visit your website every day, where they come from, which page they stay on longest right?

You can use Baidu Statistics, 51.LA website statistics or Google Analytics, just need to add a piece of code to your website files to easily access.

![](https://pic.yupi.icu/1/1764078795765-4edf9121-1d66-41e9-9dc0-857afd0294e5.png)



Then you can see visitor quantity and trends, analyze visitor sources, analyze page access situations etc.:

![](https://pic.yupi.icu/1/1764078821580-d93ee50c-61fb-4bdc-af75-76123ec6828b.png)



Can help you understand user preferences, get ideas for page optimization.

![](https://pic.yupi.icu/1/1764078843181-a16b1ff8-8990-44c3-963c-169f6771a32e.png)



If you're making mini-programs, it's even simpler, like WeChat mini-programs just use the officially built-in data analysis.

![](https://pic.yupi.icu/1/1764078876073-0a8ec98f-9146-45f8-8695-d07a8bdd6e82.png)



If you want to analyze others' website traffic, what to do?

You can use Similarweb or AI TDK type tools, input the website address and can see their traffic estimates, visit sources and popular keywords, especially useful when doing competitor analysis and SEO search engine optimization.

![](https://pic.yupi.icu/1/1764078897590-9c89b4ed-59e0-4eb5-8538-edf02ff46f5d.png)



Just knowing users' normal usage situation isn't enough, what if your website buttons can't be clicked, users are frantically getting errors over there, but you know nothing about it here, that would be awkward, might even affect revenue! So **frontend error monitoring** is indispensable.

Sentry is the industry mainstream open-source frontend monitoring, it can help you capture and statistics various code errors.

![](https://pic.yupi.icu/1/1764078928751-dae2960d-184f-41b8-9cb5-713a42fe95ac.png)



Can also record users' system environment and specific error information, convenient for you to troubleshoot and fix bugs.

![](https://pic.yupi.icu/1/1764078961573-911e5c33-bb51-401d-8aea-1afe511bc117.png)



However free version has limitations, or have to self-build server to deploy open-source code. So our team uses domestic Lingque application monitoring, also just one piece of code to access, able to real-time capture frontend's various exception errors, view specific error information etc.

![](https://pic.yupi.icu/1/1764078978982-15683249-ebb8-4165-a773-543f096021e3.png)



Sometimes just knowing where errors occur isn't enough, you also want to know how users actually operate? Why did they trigger this error? Or why are users unwilling to pay? At this time you must bring out **user behavior analysis** tools.

I'll directly take out Microsoft 100% free Clarity, can record users' real operations playback.

![](https://pic.yupi.icu/1/1764079021607-a939888c-9187-4356-97e4-7ca087d748cf.png)



Like our team's [mock interview product - Mian Duoduo](https://ai.mianshiya.com/) is using it, where users clicked, where they scrolled to, which button they hesitated on, all completely clear.

![](https://pic.yupi.icu/1/1764079042768-b8bf7b08-3402-4746-80ec-2375a7ec5253.png)



Can also through heat maps quickly analyze users' preferences, thereby helping optimize product feature button layout, reduce product usage difficulty, discover many problems you couldn't think of out of thin air.

![](https://pic.yupi.icu/1/1764079060438-35285ab2-9a14-41c8-a1f9-62334e94dd63.png)



The tools mentioned before all provide general metrics, but each product's business logic is different, some data you specifically care about, like payment conversion rate, feature usage frequency etc., relying only on existing tools might not get it, at this time you must bring out **custom business analysis**.

At start I was a bit taken for granted, directly paid for some well-known commercial BI products, but later discovered for small teams, actually no need to spend that money, directly build open-source DataEase or Superset is quite good, can connect MySQL database and other various business data sources, then according to requirements configure, drag and drop can make various visualization charts and dashboards.

![](https://pic.yupi.icu/1/1764079103181-400429a4-f0ee-4b9e-9cf8-192cbf43b6b1.png)



If really encounter particularly personalized requirements, can also self-build dashboard. Now with AI support, cooperate with ECharts chart library, write a few prompts can generate visualization dashboard, really much more relaxed.

![](https://pic.yupi.icu/1/1764079122450-bf5767d8-af95-42b0-b4cb-0007a4b55865.png)



Done with frontend, our backend's data analysis also can't fall behind.

Users access your website, behind it all are individual interfaces providing data, how to know whether interfaces are normal? Is there room for optimization? At this time need backend's **application monitoring analysis**.

Like our team using ARMS application real-time monitoring service, can help you comprehensively monitor application's performance, quickly discover interfaces with errors or slow speed.

![](https://pic.yupi.icu/1/1764079185559-220bd32c-5ae3-4085-84f2-738084e03ff3.png)



Can also further view error details, even analyze interface's complete calling chain, can quickly locate problems.

![](https://pic.yupi.icu/1/1764079204985-1645a7fd-e9a0-4efb-beda-8d1d6e4aa2e0.png)



Besides application level, server, database, cache these **resources' monitoring analysis** are also very important, if they all run on cloud, then directly use cloud service provider's built-in monitoring dashboard is fine, various metrics clear at a glance.

![](https://pic.yupi.icu/1/1764079290093-080d053b-6c1e-437d-8378-6100df73521f.png)



If you want to unified monitor analyze more personalized metrics, then have to invite out Prometheus + Grafana this ace combination. Prometheus responsible for collecting various custom metrics data, bringing developers the fire of monitoring.

![](https://pic.yupi.icu/1/1764079319434-2fbd89b9-d827-4fb9-9f38-71f10d5629c5.png)



Grafana then responsible for turning this data into cool visualization big screens. Watching a bunch of real-time changing charts, I seem to control the entire system's pulse, in a trance have feeling of becoming male lead in sci-fi movies~

![](https://pic.yupi.icu/1/1764079336501-6effc5ed-a00d-4311-a763-f1d68019bb0f.png)

---



OK will share here, actually there are many other good open-source projects, like SkyWalking, Zipkin to manage application performance, ELK to centralizedly analyze logs etc.

![](https://pic.yupi.icu/1/1764079353696-b15e7b70-4984-47d5-b036-0b499d17f629.png)



With these tools, website data analysis actually not that complex, key is according to requirements choose appropriate solution, save time down to do product is the right way.

If this article helped you, give it a like, endlessly grateful!

![求点赞](https://pic.yupi.icu/1/%E6%B1%82%E7%82%B9%E8%B5%9E.webp)


## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
