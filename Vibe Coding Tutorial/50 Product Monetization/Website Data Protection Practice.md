# Website Data Protection Practice

> Protect your data, prevent malicious crawling



Hello everyone, I'm programmer Fish Skin. Two days ago模拟 interviewed one社招 two years experienced brother, because his performance not bad, I临时起意, communicated with him our最近 encountered business scenario problems. Question as follows:

Recently we didn't make a [Programmer Practice Website - Interview Duck](https://mianshiya.com/), many bad people targeted our website, want to use crawler to grab our 10,000+ interview questions, 300+ interview question bank data. So how should we prevent this crawler behavior? Like how to identify these illegal data crawling users and automatically ban accounts?

The entire question's communication process everyone can watch video to learn: https://www.bilibili.com/video/BV1b142187Tb

Below I'll directly汇总 share methods to prevent crawlers with everyone, total exactly 10 methods! The last method very unique~



## How to Prevent Website From Being Crawled?

#### 1. Use Protocol Terms

robots.txt is a file placed in website root directory, used to tell search engine crawlers which parts don't hope to be crawled.

Give an example, can in robots.txt file add following rules to prohibit specific directories or files from being crawled:

```
User-agent: *
Disallow: /private/
Disallow: /important/
```

Although most compliant crawlers will abide by these rules, malicious crawlers might ignore it, so, relying only on robots.txt can't completely stop all crawlers. But it's protection's first step, plays a declaration and deterrence role.

Can in website's service terms or usage agreement clearly prohibit crawler crawling data, and treat violating these terms behavior as illegal, if website content gets malicious crawler crawled and causes damage, robots.txt can serve as one of evidences violating these terms.



#### 2. Restrict Data Access Conditions

Compared to directly exposing all data, can require users to log in or provide API key to access specific data. Can also set identity authentication mechanism for key content, like using OAuth 2.0 or JWT (JSON Web Tokens), ensure only authorized users can access sensitive data, effectively stop unauthorized crawlers from getting data.



#### 3. Statistics Access Frequency and Ban

Can utilize cache tools like Redis distributed cache or Caffeine local cache to record each IP or client's request times, and set threshold limit single IP address's access frequency. When detecting abnormal traffic, system can automatically ban that IP address, or take other strategies.

Need to note, although Map can also statistics request frequency, but because requests continuously accumulate, occupied memory will also continuously grow, so don't recommend using Map this kind of data structure that can't automatically release resources. If must use memory to do request frequency statistics, can use Caffeine this kind of cache technology with data elimination mechanism.



#### 4. Multi-Level Processing Strategy

To prevent "误伤", compared to directly banning illegal crawler's clients, can set a more flexible multi-level processing strategy to deal with crawlers. Like, when detecting abnormal traffic, first issue warning; if crawler behavior continues to exist, then take stricter measures, like temporarily ban IP address; if after unbanning continue crawling, then do permanent ban etc. punishments.

Specific processing strategy can customize according to actual situation, also don't recommend making too complex, don't therefore加重 system's burden.



#### 5. Auto Alert + Manual Intervention

Can implement auto alert capability, like when detecting abnormal traffic or crawler behavior, system can automatically send企微 message notification. Then website's administrator can timely intervene, further analyze and handle crawler's requests.

This point before also shared with everyone, not only针对 crawlers, enterprise's online systems best access全方位 alerts, like interface errors, CPU / memory occupation rate too high etc.

![](https://pic.yupi.icu/1/image-20240729173020018.png)



#### 6. Crawler Behavior Analysis

Illegal crawler and normal user's behavior generally have difference, crawler often follows specific access patterns. Like normal users each question need to look a while, looking time also different, while crawler generally according to fixed order, fixed frequency to get questions, very obviously can recognize.

Like below situation, possibly is crawler:

![](https://pic.yupi.icu/1/image-20240806112610085.png)



#### 7. Request Header Detection

Each request sent to server has request header information, can through checking request header's User-Agent and Referer etc. identifiers, intercept crawler requests.

Of course, this trick only prevent newbies, because request headers can be very easily forged, only need through browser's own network console get response normal request header information, can bypass detection.

![](https://pic.yupi.icu/1/image-20240806112956799.png)



#### 8. Independently Public Data

Remember college information security class, learned a knowledge point: one method to prevent network attack is, let attacker's cost greater than actual benefit. Like password 10 minutes valid, crack password needs spend 15 minutes, won't have people to crack.

Applied to crawler scene, our approach is, don't do any restrictions, directly let everyone not log in can also view our website's question data! And also provided question's various screening functions, collection functions. Most classmates just for self study, this way, no need to spend time to crawl data~

![](https://pic.yupi.icu/1/image-20240806113508903.png)



#### 9. Traceability Technology

Although questions are all public, but some we specially invited big company experts to write quality question solutions are only member visible. If have users use crawler to crawl this part of data, need to be careful! Generally speaking, as long as you logged in at a website, definitely will have access records, if you leaked website login after visible content, especially paid content, website administrator definitely has method to trace back who you are.

Relatively commonly used traceability technology is watermark, blind watermark etc. For our Interview Duck, itself is through WeChat login, and if you are member, definitely also have payment records. These technologies not only help mark data source, can also when data abused trace its source, thereby enhancing data's protection.



#### 10. Popularize Law

Besides above these methods, can also through accessing anti-crawler service, accessing verification code, increasing dynamic timestamp etc. methods further limit crawlers. But remember, crawler has no way to perfectly defend! Because you can't limit real users, attackers can completely simulate real user's access method to get your website data, like find 10 users, each person gets few hundred questions.

So my last method is — popularize law. Can on website publish clear legal statement, tell users unauthorized crawling behavior is illegal, can play certain deterrence role to crawler behavior. And also through publishing videos and articles methods, let vast programmer friends raise legal awareness. Crawler has certain risk, self learning no problem, but definitely don't give others' website cause pressure,搞不好 have suspicion of destroying computer system!

![](https://pic.yupi.icu/1/image-20240730121945226-20240806114829247.png)



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
