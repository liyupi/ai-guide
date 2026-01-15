# SEO Search Engine Optimization Practice

> Let more people discover your product



Hello everyone, I'm programmer Fish Skin. Our team's programmer interview practice website [Interview Duck](https://www.mianshiya.com/) was indexed and recommended by Baidu and other major search engines less than half a month after launch!

The effect is obvious, when users search "Interview Duck," the first thing they see is our own website, thereby increasing traffic to the website:

![](https://pic.yupi.icu/1/image-20240815102430905.png)

Regarding how to let search engines index websites faster, this is actually a very deep subject, with a professional term called SEO. For individual website owners, search engine traffic is crucial, everyone probably hopes their websites can be seen by more people right? Leaving aside revenue, having a website with large visit volume, can also brag a bit when writing resumes and in interviews~ So I suggest programmer friends best have some understanding of SEO.

Today in this article, I'll use my own Interview Duck website as an example to share some practical SEO techniques with everyone, letting everyone's websites be indexed by search engines faster. At the same time, I'll also introduce a new concept in the AI era — GEO (Generative Engine Optimization), helping your product also be discovered by more people in the AI search era.

Whether you're using Vibe Coding to do personal projects, or want to make a real product, mastering SEO and GEO methods can help you obtain more traffic.

⭐️ Can also watch video explanation, fresh: https://www.bilibili.com/video/BV1tz421i7Q1



## Fish Skin's SEO Dry Goods Sharing

### I. What Is SEO?

SEO stands for Search Engine Optimization, making websites easier to be indexed and presented by search engines, letting more people discover your website through search engines like Baidu, Google, etc., thereby improving website visit volume and visibility.

Before learning how to do SEO optimization, let's first briefly understand SEO's process, that is: How do search engines discover your website and let users find it when searching?



### II. SEO Process

The entire SEO process can be divided into four main phases: crawling, indexing, indexing and ranking. Let me explain these four steps in detail below.

#### 1. Crawling

Crawling is the first step of SEO process, search engines will send out a group of crawler programs (commonly known as spiders), they will crawl everywhere on the internet, visit various websites, and crawl webpage content. These spiders will follow links from one page to another, traversing the entire website as much as possible.

#### 2. Indexing

After crawling is complete, search engines will analyze webpage content and decide whether to index that page into its database. Only indexed pages can be displayed when users search, therefore, ensuring pages are indexed is a key step in SEO. Some websites although have many links and content, as long as search engine spiders don't like and don't index them, then even if others specifically search for your website, they can't find it.

#### 3. Indexing

Indexing refers to search engines organizing and categorizing already indexed webpage content, and establishing a huge index library. This process is similar to tagging each webpage, so that when users search, search engines can quickly find webpages related to search terms.

For example, our Interview Duck website content includes: Java interview question bank, frontend interview question bank, C++ interview question bank, then these few words might be set as indexes. When users search content containing these words, might search our website.

#### 4. Ranking

Now there are so many websites, same indexes are also very many, how to ensure users prioritize searching our website? This involves SEO's final step — ranking.

When users input keywords in search engines, search engines will according to their algorithms, pick out most relevant webpages from index library, and **according to relevance, weight, website quality** etc. factors sort, deciding which webpages appear in search results' first few pages.

This is SEO's process, the SEO optimization techniques I share below are also all centered on these processes.



### III. How to Do SEO Optimization?

#### 1. Keyword Optimization

Keywords refer to vocabulary users input in search engines, can increase website indexing and improve webpage ranking in relevant searches by setting keywords (Keywords) and description (Description) etc. information in website's HTML head information.

Keyword selection needs to be precise and strongly related to website content, avoid over-stuffing keywords, to avoid being judged as cheating behavior by search engines.

For example, to make an interview practice website, can set the following keywords and description:

```html
<meta name="keywords" content="程序员面试,Java面试题,程序员求职,计算机">
<meta name="description" content="程序员面试刷题，就来面试鸭，程序员免费求职面试刷题网站。海量高频Java面试题,帮你备战技术面试。">
```



#### 2. Website Structure Optimization

Website structure optimization is divided into 2 points: whole site page structure optimization and each page's content structure optimization.

For the entire website, page nesting levels should be as flat as possible, try to shorten page levels, to reduce crawler crawling difficulty.

Give an example, below two website structures, which structure's pages do you think are easier for crawlers to completely access?

![](https://pic.yupi.icu/1/image-20240815112845394.png)

The answer goes without saying, for important pages you want to be discovered by search engines faster, should as much as possible shorten the path to jump to that website, and appropriately add more entrances to jump to that page.

For each page, should have clear hierarchical structure, can use reasonable heading tags (like first-level heading `<h1>`) to make page content easier to index.



#### 3. Friendly Links

When I first started doing personal websites in college, I increased website weight through friendly links (although effect is limited). Operation method is very simple, your website adds others' website links, others' websites add your website links, your both sides' websites mutually recommend, easier to improve ranking in search engines.

The principle behind friendly links is also very simple. Many search engines will rank websites according to weight, how is weight calculated? A very simple algorithm (Page Rank), is each website has its own votes, every time others' websites add friendly links that jump to your website, equivalent to voting for your website, websites with high votes can obtain higher weight and ranking. Friendly links are equivalent to mutual voting, better than websites with 0 votes.

![](https://pic.yupi.icu/1/image-20240815113641780.png)

Of course, this mutual recommendation method needs careful use, avoid excessive link exchanging, might cause weight dispersion.



#### 4. Sitemap File

Sitemap website map is a file that lists all pages of your website, usually placed in website's root directory, or specify its location through robots.txt file. It can help search engines more quickly understand your website's structure, and crawl pages you hope to prioritize indexing.

Equivalent to you sending a map to crawlers, crawlers won't easily get lost, also won't easily miss your website's important pages.

For websites with relatively simple structure, using static, fixed Sitemap is enough. As shown below:

![](https://pic.yupi.icu/1/image-20240815114215436.png)

But for websites with continuously updating content, there's also more advanced operation, is using programs to automatically generate dynamic Sitemap, like generating daily newly added questions as a Sitemap file, facilitating crawlers faster discovering latest content.

In addition, some search engines also support active uploading and submitting Sitemap files, can further shorten website discovery and indexing time.



#### 5. SSR Server-Side Rendering

Note, the SSR here isn't the one we talk about when drawing cards in games!

SSR server-side rendering is one of SEO's most effective technologies. Refers to generating **complete HTML pages** on server side, and directly sending them to browser. Compared to traditional frontend AJAX dynamic data request rendering method, SSR can let search engines more easily crawl complete page content, thereby improving SEO effect.

Give an example, if it's a frontend website that dynamically requests data, the webpage content crawlers see might be incomplete, as shown below:

![](https://pic.yupi.icu/1/image-20240815114606517.png)

Because browser pulls webpage from server, then loads JS script, finally sends request to get data.

And if using server-side rendering, server will complete data request, and assemble data into page, then return to frontend, the webpage content crawlers see is more complete, as shown below:

![](https://pic.yupi.icu/1/image-20240815114910820.png)

Although server-side rendering's effect is good, but also increases server pressure, and development cost is usually higher. Like our Interview Duck uses Next.js framework development, stepped in quite a few pits during development process.

Oh right, using PHP to develop server-side rendering websites is very convenient, this might also be one of reasons why PHP was so popular before.



#### 6. SSG Static Site Generation

Somewhat similar to SSR, SSG is SEO optimization's other big weapon. Refers to when building website, pre-generating all pages' **static HTML files**, and directly deploying them to server. When users access website, directly get generated HTML files, compared to SSR server-side rendering, doesn't even need server to temporarily request data anymore.

This method not only greatly improves page loading speed, but also makes search engines able to faster and more completely index all pages. So many blog site generators (like Hugo, VuePress, Hexo) all pack and generate written articles as static HTML, then deploy to server.

Of course, SSG also isn't a silver bullet, suitable for websites with relatively fixed content and lower update frequency, like personal blogs etc. Static websites are essentially a type of cache, if webpage content frequently changes, need to frequently update this file, also has no small cost.

So we can think of a more advanced strategy: SSR + SSG combination! Content relatively fixed webpages use static generation, content changing webpages use server-side rendering, webpages not needing SEO pure client-side rendering is fine.



#### 7. Throw Money

Note, above methods don't guarantee absolute effectiveness, only increase probability of search engine indexing and ranking optimization, SEO strategy needs continuous adjustment and long time verification.

If team doesn't have technicians who understand SEO, and also want to quickly let own website be recommended by search engines, then can only "throw money," simple and crude, is spending money to buy ads, letting your webpage appear in search results' first few positions. Many companies also do this, but for individual website owners without revenue, still honestly use the previously recommended methods.



## GEO in AI Era: Generative Engine Optimization

With the popularity of AI dialogue tools like ChatGPT, more and more users start using AI to search for information, rather than traditional search engines. This has spawned a new concept **GEO (Generative Engine Optimization)**.



### What Is GEO?

GEO refers to optimizing your content, making it easier to be understood and cited by AI search engines (like ChatGPT, Perplexity, Gemini, etc.). When users ask AI questions, AI will crawl relevant content from the internet, then generate answers. If your website content is cited by AI, can obtain more exposure.



### Difference Between GEO and SEO

- SEO: Optimize websites, making traditional search engines (like Baidu, Google) easier to index and rank
- GEO: Optimize content, making AI search engines easier to understand and cite



### How to Do GEO Well?

1) Structured Content

AI prefers clearly structured content. Use headings, lists, tables etc. methods to organize content, letting AI more easily extract key information.

2) Provide Authoritative Information

AI tends to cite authoritative, accurate information. Ensure your content has data support, has source citations, improve content credibility.

3) Use Natural Language

AI's ability to understand natural language is very strong. Write in easy-to-understand language, avoid overly specialized terminology, letting AI more easily understand your content.

4) Answer User Questions

AI search is usually conducted in Q&A form. In content directly answer questions users might raise, like "How to do XX," "What is XX," this way easier to be cited by AI.

5) Keep Content Updated

AI tends to cite latest content. Regularly update your website content, keep information timely.

6) Provide Complete Context

AI needs to understand content's context to accurately cite. Ensure every article has complete background introduction and detailed explanation, don't let readers (and AI) feel confused.



## In Conclusion

In the Vibe Coding era, using AI to make products is already very easy. But, how to let more people discover your product, still needs you to master SEO and GEO methods.

Go for it, let your product be discovered by more people~



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
