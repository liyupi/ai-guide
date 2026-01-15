# System Monitoring and Alerting Practice

> Discover problems in time, guarantee system stability



Hello everyone, I'm programmer Fish Skin, today sharing some very practical system monitoring and alerting tools.

Whether you're using Vibe Coding to do personal projects, or want to make a real product, mastering system monitoring and alerting methods can help you promptly discover and handle problems, guarantee system stable operation.



## Why Use Monitoring Alerting?

Speaking of monitoring alerting, students without enterprise development experience very easily neglect it, even some students feel unnecessary, at worst when Bug appears then fix it.

![](https://pic.yupi.icu/1/image-20240729172241587.png)

**This kind of thinking is hugely wrong!**

We imagine system as human body. Sometimes, a person surface looks very healthy, but possibly just didn't have opportunity to discover internal abnormalities, result wait until really something happens, often consequences to bear are more serious. So need regular physical examination, timely discover and handle problems. System monitoring alerting's effect is also similar, can timely discover system's potential abnormalities and problems、when online problems appear can also first time discover, early handle, thereby prevent or reduce failure.

Besides, monitoring system also has some other benefits, let's continue looking.



## How to Implement Monitoring Alerting?

Most directly thought of method is self write code to implement, like for functions needing special attention add some logic, when some exception appears send SMS / email /企微 message OK. We at start did this:

![](https://pic.yupi.icu/1/image-20240729173020018.png)

But actually business alerting is only one of monitoring alerting's layers, like human body surface skin examination. If we want to more comprehensively, more accurately monitor system's health, still need to do全方位 physical examination inside and outside, including server monitoring, network monitoring, application monitoring, database monitoring, API interface monitoring etc.

Yes, sounds very complex, so monitoring in modern operations has a more professional alias, called "observability." Observability refers to system's ability to understand and diagnose its health status and performance through monitoring and analyzing its internal state. This concept not only includes traditional monitoring, but also extends to data collection, analysis and response. Give an example, we through monitoring discover system memory utilization rate not high, can appropriately降配 save cost; discover system memory utilization rate too high, can consider whether to升配 expand.

Wanting to self optimize system's observability is still very complex, data collection, data storage, data analysis, alerting mechanism, availability guarantee, performance etc all need to consider, big companies all have scale infrastructure team to do.

For our individual developers or small companies, since it's全方位 "physical examination," we generally won't do it ourselves, but will choose more professional tools or services, directly use and access OK. Below recommend several our team uses.



## Monitoring Tool Recommendations

### 1. Server Monitoring

1) Server's own monitoring capability

As long as you use big company's cloud servers, basically all come with server monitoring, can also set alerts. Like below Tencent Cloud Lightweight Application Server's monitoring, can see CPU, memory, network bandwidth, hard disk etc. resource usage:

![](https://pic.yupi.icu/1/image-20240729175223676.png)



2) Container platform's monitoring capability

If you use container method to deploy project, basically container platform also comes with monitoring alerting capability. Like WeChat Cloud Hosting's service monitoring, besides seeing system resource occupation, can also see interface call volume, request error volume, interface QPS and response time, equivalent to coming with part of API interface monitoring capability.

![](https://pic.yupi.icu/1/image-20240729175504698.png)

And cloud hosting platform supports receiving alerting information in WeChat group, very convenient. Once node gets attacked, immediately can notify you.

![](https://pic.yupi.icu/1/image-20240729175751550.png)



### 2. Database Monitoring

Before, without database monitoring, we very hard to pay attention to database's running status, don't know it working hard or not,有没有摸鱼 or overload overtime. But now, if you use third-party cloud service provider's cloud database, can directly on platform view database resource utilization. Like our Tencent Cloud database comes with monitoring:

![](https://pic.yupi.icu/1/image-20240729180105756.png)

Before could only through user feedback or server failure to discover harm system slow SQL, now using cloud database comes with intelligent butler, can first time help you discover slow SQL, take preventive measures.

![](https://pic.yupi.icu/1/image-20240729180157868.png)

Can also one-click help your database do physical examination, not 100 points all need timely modify:

![](https://pic.yupi.icu/1/image-20240729180528480.png)



### 3. Application Monitoring

Application monitoring's range relatively broad, we use Alibaba Cloud's application real-time monitoring service ARMS, main reason is after comparison Alibaba in Java application service this aspect's professionalism truly higher.

Including application server (like Java's Tomcat) status, API interface calling situation, system internal dependency service calling situation, scheduled task calling situation, thread pool status, virtual machine memory, GC situation etc.

![](https://pic.yupi.icu/1/image-20240729181837634.png)

![](https://pic.yupi.icu/1/image-20240729182031915.png)

Can also view application topology structure, analyze calling chain etc.:

![](https://pic.yupi.icu/1/image-20240729181939087.png)

Besides monitoring capability, its alerting capability is truly strong! We connected service to企微, as long as some link has problem, immediately will send us alert. Can also quickly view alert details, claim alert, shield alert etc.

![](https://pic.yupi.icu/1/image-20240729182157448.png)

Truthfully speaking, we first few days after accessing this thing, quite painful, because exposed many system problems not discovered before, late night企微 also kept滴滴滴滴滴滴搁那 sound! Our team's development classmates miserable.

![](https://pic.yupi.icu/1/image-20240729182459731.png)

But now already used to it... er, accurately speaking is after system through optimization, already became more healthy~

No matter what, accessing monitoring alerting still very necessary, feels like opened通透 world, know system's status like palm of hand!

But monitoring service's use exceeds certain times, needs fees, about monthly tens of G free quota, for enterprise projects actually very quickly used up. For learning or personal websites can try.



### 4. Frontend Monitoring

Besides above monitoring, sometimes we still want to understand user behavior, user attributes and business indicators, like daily how many users access website, use PC or mobile, mobile what brand, how many new users register etc. Then maybe also need frontend monitoring (of course can also backend埋点 statistics), before shared, use Baidu Statistics, one line of code can access into frontend website, very convenient~

![](https://pic.yupi.icu/1/image-20240625112621549.png)





## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
