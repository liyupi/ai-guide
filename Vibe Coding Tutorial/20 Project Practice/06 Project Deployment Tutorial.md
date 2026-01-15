# Project Deployment Tutorial

> Deploying projects to the internet for global access


Hello, I'm Programmer Fish Skin.

In previous articles, we learned how to develop various projects. But if projects can only run locally, that's too limiting. In this article, I'll teach you how to deploy projects to the internet so people worldwide can access them.

It should be noted that if you're using AI zero-code platforms like Bolt.new, Lovable, Meituan NoCode, or Baidu Miaoda, they generally come with built-in deployment functionality—just click the publish button to go online, very convenient. But if you want more flexible deployment, like using your own domain name, choosing different servers, or deploying more complex full-stack projects, you need to learn more deployment methods.

Below I'll introduce various deployment methods, from the latest AI automated deployment to the most popular Vercel one-click deployment, to professional server deployment. You can choose the appropriate deployment method based on your project type and needs.



## I. Deployment Methods Overview

Before starting, let's understand what deployment methods are available.

For frontend projects (static webpages, single-page applications, etc.), the simplest method is using hosting platforms like Vercel, GitHub Pages, EdgeOne Pages, etc. These platforms provide free hosting services—just upload code and it automatically deploys and generates an access link.

For full-stack projects (including frontend and backend), you can choose containerized deployment (Docker), cloud server deployment (Alibaba Cloud, Tencent Cloud, etc.), or Serverless deployment. These methods are relatively more complex but more powerful.

Below I'll详细介绍 each deployment method.



## II. Let AI Deploy Automatically (Latest and Coolest)

Let me share a latest technique first—let AI help you deploy websites.

In the past, when we developed a website, we needed to propose requirements, design a solution, write code for development, and finally deploy for launch. We all know AI is getting better and better at writing code, gradually replacing some of our programmers' coding work; but actually, AI's capabilities go beyond that—with MCP, it can even help us directly deploy websites online!

Well, well, so I just need to provide a one-sentence requirement, and I don't even need to do the coding and deployment myself—you're trying to make me regress, right?

![](https://pic.yupi.icu/1/1752213314439-7925d7ba-0d1d-46f1-9f70-b1d391ac854d.png)

Let me walk you through it—let AI help me generate and deploy a personal blog website.



### Prepare Tools

The tools we need include:

- Cursor: AI programming tool, responsible for calling AI to generate code
- EdgeOne Pages MCP: Service that can quickly deploy websites to CDN and generate publicly accessible links

What is EdgeOne Pages MCP? Let's break down these terms.

EdgeOne is a CDN acceleration service provided by Tencent Cloud that caches your website's resources on edge nodes closest to users, improving website performance.

![](https://pic.yupi.icu/1/1752216739540-3dbb9132-3ae0-4a5d-9949-2a4299663c39.png)

EdgeOne Pages is a website deployment service based on this CDN that allows you to easily deploy websites to CDN and get a publicly accessible address, without needing to set up your own server.

![](https://pic.yupi.icu/1/1752216784265-0a71fe3a-7944-40b2-b5ce-87215df060fe.png)

MCP is the currently popular Model Context Protocol that allows AI models to easily use various tools to enhance capabilities and complete more complex tasks.

![](https://pic.yupi.icu/1/1752216828838-510154d5-6a89-4089-84b9-fadeccb9d724.png)

The purpose of EdgeOne Pages MCP is obvious—provide AI with website deployment tools, and this is a relatively popular MCP.

![](https://pic.yupi.icu/1/1752217054075-0f149a76-9e42-482e-ae26-e23762c7ad1e.png)



### Quick Practice

1) Activate Pages Service

First go to [EdgeOne Console](https://console.cloud.tencent.com/edgeone/pages) to activate the Pages service:

![](https://pic.yupi.icu/1/1752209404627-3a3193d9-4c94-4f80-ad02-435ff22f16ed.png)

After activating the service, you'll enter the project management page by default—let's not rush to create a project yet:

![](https://pic.yupi.icu/1/1752209421726-11d8eff7-7bdd-4a85-accf-c70f74ead15a.png)

Since we'll complete website deployment through MCP in a moment, we first need to get an API Token as the credential for calling the service:

![](https://pic.yupi.icu/1/1752209504079-6741bbd0-438e-48a4-86be-6eddfc3efa83.png)



2) Configure MCP

Create a new project folder `yupi-blog`, open it in Cursor, then enter settings and add MCP service:

![](https://pic.yupi.icu/1/1752209949437-369134bc-303b-46fc-bca1-e1a57a335f82.png)

Copy and paste this configuration into the MCP configuration file:

```json
{
  "mcpServers": {
    "edgeone-pages-mcp-server": {
      "command": "npx",
      "args": ["edgeone-pages-mcp"],
      "env": {
        "EDGEONE_PAGES_API_TOKEN": "Your API Token",
        "EDGEONE_PAGES_PROJECT_NAME": ""
      }
    }
  }
}
```

Note to change the API Token to your own, and remove comments, otherwise it will error:

![](https://pic.yupi.icu/1/1752210048110-15bf78cc-da14-4f7f-b9d5-3ec510332bf7.png)

Normally, you'll see the MCP service successfully load—it turned green, it turned green!

![](https://pic.yupi.icu/1/1752211512400-a59c2010-8701-4b75-80d9-014ad03e8b4a.png)

This service provides 2 tools:

- deploy_html: deploy HTML content to EdgeOne Pages, returns public access URL
- deploy_folder_or_zip: deploy folder or ZIP file to EdgeOne Pages, returns public access URL

Note, this MCP service needs NPX tool to successfully start locally. NPX can directly run commands from NPM packages without global installation, often used for executing scaffolding tools and one-time commands.

If you don't have NPX command, or your Node.js version is too low (best not lower than 20), it will cause the tool to fail to load.

![](https://pic.yupi.icu/1/1752211437222-1400be90-e460-4948-b7f3-45a6a78ffe7d.png)

In this case, you just need to go to the [official website to install Node.js](https://nodejs.org/zh-cn), it will automatically help you install NPM and NPX tools:

![](https://pic.yupi.icu/1/1752209643527-73a7c2cc-046c-4faa-8531-2a22da95d4bd.png)

If NPX tool wasn't automatically installed, use NPM package manager to install NPX:

```bash
npm i -g npx
```



3) Generate and Deploy Website

After preparing the MCP service, let's generate the website. Enter the following prompt to let AI help me generate a personal blog website:

```
Help me generate a personal blog website based on Programmer Fish Skin's GitHub, geek style, simple and elegant; after generation, deploy the website
@https://github.com/liyupi
```

Looking at AI's thought process, it already thought to use EdgeOne Pages to deploy the website:

![](https://pic.yupi.icu/1/1752211869664-b74dc4d9-57b1-4bb7-9f02-703112b613eb.png)

Very quickly the website was generated and deployed—you can see AI called the MCP tool to deploy HTML and got the access address:

![](https://pic.yupi.icu/1/1752212029384-16cfba8f-babb-49c0-9d41-3b76ee78eecf.png)

Just open the URL directly to see the result—too convenient!

![](https://pic.yupi.icu/1/1752212096367-0a0fac32-118e-485a-9277-8dd507ff66d3.png)

However, the currently generated website is relatively simple, just an HTML page, and didn't even create code files locally.



4) Deploy Website Directory

Let's try a more complex project—use the following prompt to let AI use a frontend framework to develop a multi-page website:

```
Help me generate a personal blog website based on Programmer Fish Skin's GitHub, geek style, simple and elegant;
Need to include multiple pages, require using Vue framework for modular development;
After generation, deploy the website
@https://github.com/liyupi/
```

![](https://pic.yupi.icu/1/1752212265608-6aa96245-199f-487f-9c57-bc2f0550cdf6.png)

This time you'll need to wait quite a while—Fish Skin suggests you use this time to get a glass of water and move around a bit. Recently I've been sitting too still and my shoulders feel as hard as rock.

![](https://pic.yupi.icu/1/1752217850836-e83f0d59-a657-4048-94cd-a515e960a4d7.png)

We'll find that although a lot of code was generated, it didn't automatically deploy, just gave deployment suggestions:

![](https://pic.yupi.icu/1/1752213747665-192b57be-90a5-44e4-92b1-5cd468394707.png)

Looking at AI's thought process, it turns out the deployment tool failed:

![](https://pic.yupi.icu/1/1752214113764-2afad6bc-5777-4e9e-b2d2-745476caadc2.png)

After my testing, I found that if you want to deploy a website directory or zip file, it's best to first create a project in the Pages web version, then let MCP upload the website files to this project.

So let's use the officially provided example to deploy a random website first:

![](https://pic.yupi.icu/1/1752215857055-9a84b9d5-4787-4181-b054-8883884c34b2.png)

Change the project name to `yupi-blog`, just click "Start Deployment":

![](https://pic.yupi.icu/1/1752215971422-9e57abea-077a-4847-88b3-bd1cd1de4217.png)

Wait for deployment, about 30 seconds and it's done:

![](https://pic.yupi.icu/1/1752216002653-9d7c5127-642a-4b3c-b542-c9e6cfcd0dde.png)

After the project is successfully deployed, we modify the Cursor MCP configuration and fill in the just-created project name:

![](https://pic.yupi.icu/1/1752216064120-e1e8e58e-0eaa-4b9c-814b-605c664c35a3.png)

Then talk to AI again and let it help me deploy the website directory:

![](https://pic.yupi.icu/1/1752213933060-071efc16-a9ac-4333-8fd9-53beeeeedd90.png)

You can see this time AI successfully executed the deployment tool and got the access address:

![](https://pic.yupi.icu/1/1752216306792-fb4c2e9c-d600-4b7c-b3c4-d5ae02614974.png)

Looking at the website effect—not bad, very tech-feeling!

![](https://pic.yupi.icu/1/1752216337356-667e0577-b0a5-4f44-b147-5bb3ab14824e.png)

However note, the generated website uses a temporary domain by default, which has a relatively short validity period:

![](https://pic.yupi.icu/1/1752216364625-c93f7b26-133a-4aac-a849-77ee6840e6f1.png)

If you have a domain name, I recommend configuring a custom domain, then you can access it indefinitely~

![](https://pic.yupi.icu/1/1752216408600-03b16e94-4668-4295-b7bb-2a07bc5592c7.png)

How about that, pretty simple right? When MCP can be easily used on mobile in the future, imagine this: you're walking down the street chatting with a friend, your friend recommends a blogger to you—Programmer Fish Skin, you just say one sentence to AI, and 2 minutes later, you can give your friend a website to introduce this blogger, like magic.

![](https://pic.yupi.icu/1/1752218294278-9d31872f-e883-4736-a3f6-584ee31e9ad7.png)

It's worth mentioning that EdgeOne Pages should currently be free—really nice.

![](https://pic.yupi.icu/1/1752216569752-fbd0f243-7d43-44de-af69-d3d6eb954f8a.png)



## III. Vercel One-Click Deployment (Recommended)

[Vercel](https://vercel.com) is currently the most popular frontend deployment platform, especially suitable for React, Next.js, Vue, static websites and other frontend projects.

Vercel's advantages include completely free for personal projects, extremely fast deployment speed (generally 1-2 minutes), automatic HTTPS and CDN acceleration configuration; and deep integration with GitHub, automatically deploying when you push code to a GitHub repository.



### Usage Steps

1) First visit [Vercel official website](https://vercel.com) to register an account, recommend using GitHub account to register and login.

2) Create a project, you can directly bind GitHub and select already-hosted projects, click "Deploy" deployment button:

![](https://pic.yupi.icu/1/image-20260109111323983.png)

3) Wait 1-2 minutes, and the project is online!

After successful deployment, Vercel automatically gives you a domain name, like `your-project.vercel.app`, and you can also bind your own domain name. Plus every time you push code to GitHub, Vercel automatically redeploys—completely no manual operation needed.



### Command Line Deployment

Besides web interface operation, Vercel also provides command line tools that let us deploy projects to the platform with one command. First use NPM to install Vercel CLI tool:

```bash
npm i -g vercel@latest
```

Then, directly in the project folder you want to deploy, enter the `vercel` command to deploy the current project:

![](https://pic.yupi.icu/1/1752218682107-8c8457e4-3fbe-40d8-afb8-f6cb0691beee.png)

The method to let AI complete automatic deployment is also simple—you just need to tell AI in the prompt "you can use vercel command line tool to complete website deployment", smart as it is, it will definitely help you complete the task.

💡 For specific process, you can watch Fish Skin's video tutorial: https://www.bilibili.com/video/BV1TV4y1j76t

Besides Vercel, there's also [Netlify](https://www.netlify.com/), a similar platform. Netlify and Vercel have similar functionality, but Netlify is more comprehensive, supporting more frameworks and static site generators, with form processing, serverless functions and other features, larger free quota, and supports A/B testing and analytics. Usage is similar to Vercel: register account => connect GitHub => select project => click deploy. If your project isn't Next.js (Next.js is best with Vercel), consider using Netlify.



## IV. GitHub Pages Deployment

[GitHub Pages](https://pages.github.com/) is a free static website hosting service provided by GitHub. Advantages include completely free, unlimited traffic, and seamless integration with GitHub.

Usage is super simple—after creating a repository on GitHub and uploading website files, just enable GitHub Pages in repository settings:

![](https://pic.yupi.icu/1/image-20260109111917547.png)

Then you can access via `username.github.io/repo-name`. Suitable for personal homepages, project documentation, simple static websites.

GitHub Pages limitation is it can only deploy static websites, cannot run backend code. But for pure frontend projects, it's completely sufficient. And completely free, no need to worry about traffic limits.



## V. Cloud Server Deployment

If you want more control, you can rent a cloud server and deploy the project yourself. Domestic mainstream cloud service providers include Alibaba Cloud, Tencent Cloud, Huawei Cloud, etc.

Basic process for cloud server deployment:

1) Purchase a cloud server (recommend 2 core 4G configuration to start, first-time purchase has new user discounts)

2) Install runtime environment, like Node.js, Nginx, MySQL database, etc.

3) Upload code to server

4) Configure Nginx reverse proxy

5) Configure domain name and SSL certificate

This process is somewhat complex for complete beginners, but you can use visual management tools like Baota Panel or 1Panel to greatly simplify operations. These panels provide graphical interfaces—no need to remember complex commands, just click the mouse to complete configuration.

![](https://pic.yupi.icu/1/1736821032080-4be9c9e5-6dfe-434b-8db8-7eb8d7068a16.png)

Advantages of cloud server deployment are you have complete control, can adjust configuration anytime, and it's more stable. Disadvantages are needing some programming or operations knowledge, and servers require payment (generally tens to hundreds of yuan per month).

💡 For specific process, you can watch Fish Skin's video tutorials:
- [Cloud Editor + Vercel + Object Storage + Intranet Penetration 4 deployment methods](https://www.bilibili.com/video/BV1UZ4y197i1)
- [Nginx + Baota 2 methods to deploy personal blog](https://www.bilibili.com/video/BV1rU4y1J785)
- [WordPress build personal blog](https://www.bilibili.com/video/BV14q4y1R7XM)
- [4 mainstream frontend and backend project deployment methods](https://www.codefather.cn/course/1790943469757837313/section/1791075571845345281?contentType=video&tabKey=videoList)

Fish Skin has led the Programming Navigation community through 20+ projects, explaining almost every deployment method:
- [AI Zero-Code Application Generation Platform Project](https://www.codefather.cn/course/1948291549923344386): 1Panel + Nginx frontend + Java backend (jar package)
- [Code Generator Sharing Platform Project](https://www.codefather.cn/course/1790980795074654209): Baota Panel + Nginx frontend + Java project manager (jar package) backend deployment

Basically, learning these few deployment methods can handle the vast majority of deployment needs.



## VI. Docker Containerized Deployment

For full-stack projects containing frontend and backend, Docker is a great deployment method. Docker can package your application and runtime environment into a container that can run on any server supporting Docker.

Docker's advantages include good environment consistency—no "runs on my computer but not on server" problems. Plus it's convenient to manage multiple applications, each running independently without affecting each other.

Basic process for using Docker deployment:

1. Write Dockerfile to define application's runtime environment
2. Build Docker image
3. Run Docker container
4. Configure Nginx reverse proxy (if needed)

This process is relatively more complex, but you can let AI help you complete it. You just need to tell AI: "Help me write a Dockerfile to deploy this Node.js project." AI will generate complete Dockerfile and deployment scripts.

If you want to learn enterprise-level deployment methods, recommend studying Docker deeply.

💡 For specific process, you can watch Fish Skin's project tutorials:
- [AI Quiz Application Platform Project](https://www.codefather.cn/course/1790274408835506178): Vercel frontend + Docker backend + cloud hosting Serverless platform deployment
- [AI Super Agent Project](https://www.codefather.cn/course/1915010091721236482): Docker frontend + Docker backend + cloud hosting Serverless platform deployment
- [OJ Online Judge Project](https://www.codefather.cn/course/1790980707917017089): Docker Compose backend microservice deployment



## VII. CDN Acceleration Optimization

After deployment, if you want to make website access speed faster, you can also use CDN acceleration.

CDN (Content Delivery Network) caches your website content on servers around the world—when users access, it automatically selects the server closest to them, greatly improving load speed.

![](https://pic.yupi.icu/1/1763643073516-5248d56c-bf7d-4537-b8f8-681a104626d9.png)

[Cloudflare](https://www.cloudflare.com/zh-cn/) provides free CDN service, advantages include:

- Completely free (personal websites)
- Global CDN acceleration, covering 200+ cities
- Automatic HTTPS certificates
- DDoS protection and Web firewall
- Free DNS service

Usage is simple—register Cloudflare account, add your domain, then change your domain's DNS servers to addresses provided by Cloudflare. Cloudflare will automatically help accelerate and protect your website.

You can also directly use Cloudflare's Pages deployment capability, upload your code directly, let it one-click deploy and get a free domain—even more convenient~

![](https://pic.yupi.icu/1/1763643412558-4d499b46-5e16-4f83-9df7-06a85175df35.png)

If your website is deployed on Vercel or Netlify, they already have CDN acceleration, no need to configure Cloudflare additionally. But if you're renting your own server for deployment, strongly recommend using Cloudflare acceleration.



## VIII. Domain Names and SSL Certificates

After deployment, you might want to configure a memorable domain name for your website, rather than always having users access via hard-to-remember IP addresses.



### Purchasing Domain Names

Domain names are website addresses, like [codefather.cn](https://codefather.cn/), [dogyupi.com](http://dogyupi.com/). For domestic users, I recommend purchasing domain names from well-known cloud service providers like [Alibaba Cloud](https://wanwang.aliyun.com/) or [Tencent Cloud](https://dnspod.cloud.tencent.com/). Price is generally tens of yuan per year, and the operation interface is in Chinese, very convenient.

Note that if your website server is in China, the domain name needs filing (ICP备案). Filing process takes about 1-2 weeks, requiring ID card, phone number and other information. If your website is deployed on foreign platforms like Vercel, Netlify, or you purchase the domain name from foreign platforms, you can skip filing and go online quickly.



### Configuring SSL Certificates

Modern websites basically require HTTPS, so you need to configure SSL certificates. Good news is, most deployment platforms automatically configure SSL certificates—no manual operation needed.

For example, Vercel, Netlify, GitHub Pages, EdgeOne Pages all automatically configure HTTPS—you just need to bind the domain name.

If you're renting your own server for deployment, you can use free [Let's Encrypt](https://letsencrypt.org/zh-cn/) certificates, or use Cloudflare's CDN—they both automatically configure HTTPS.



## In Conclusion

Through this article, you've learned multiple project deployment methods. From the latest AI automated deployment, to the most popular Vercel one-click deployment, from simple GitHub Pages, to professional cloud servers and Docker containerized deployment—each method has its own applicable scenarios.

I suggest for beginners, start with simple methods. If you're using AI zero-code platforms, just use their built-in publish functionality. If you're developing with code editors like Cursor, recommend starting with Vercel or GitHub Pages—you can go online in minutes. Once you're proficient, learn Docker and cloud server deployment—these are enterprise-level deployment methods, more professional and more flexible.

Now, choose a deployment method suitable for you and publish your project to the internet~



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
