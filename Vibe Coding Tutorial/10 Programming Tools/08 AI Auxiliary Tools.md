# AI Auxiliary Tool Collection



Hello, I'm Programmer Fish Skin.

In previous articles, we learned about various AI programming tools, including AI zero-code platforms, AI agent platforms, AI code editors, command-line tools, and IDE plugins. But to truly develop projects efficiently, AI tools alone aren't enough — you also need some auxiliary tools to complete the entire workflow.

For example, you might encounter these problems:

- AI messed up the code changes, how do you revert?
- Project is done, how do you deploy it online for others to access?
- Are there other practical tools to improve efficiency?

In this article, I'll introduce commonly used auxiliary tools in Vibe Coding development, helping you complete your entire development toolchain.



## I. Git Version Management

### Why Do You Need Git?

During development, you might encounter these situations:

- Just changed code, but it's broken, want to revert to a previous version
- Want to try a new feature but afraid it will affect existing code
- When collaborating with others, don't know who changed what

Git can help you solve all these problems.

**Git is a version control tool** that can record every modification to code, allowing you to roll back to any historical version at any time.

💡 If you want to become a professional programmer, Git is essential — it's a fundamental skill for enterprise development.



### Git's Core Concepts

Git's workflow is very simple, mainly three steps:

1. Modify code in the working area
2. Add code to staging area (using `git add` command)
3. Commit code to repository (using `git commit` command)

To use an analogy: modifying code is like writing on scratch paper, adding to staging area is like picking out the content you're satisfied with, committing to repository is like formally saving that content to a notebook.

![](https://pic.yupi.icu/1/gitworkflow%E5%A4%A7.jpeg)



### How to Use Git?

There are 2 ways to use Git: **visual tools** and **command line**.

For beginners, I strongly recommend starting with visual tools. Many mainstream development tools now (like Cursor, VS Code) have built-in Git functionality — just a few mouse clicks can complete code commits and pulls, no need to memorize commands at all.

When I first started with Git, I was like this — didn't search for tutorials online at all, just watched others commit projects by clicking a few times in the editor and thought it was magical. Then I learned by imitation and started using this tool. And for a long time I used [GitHub Desktop](https://desktop.github.com/) for foolproof operations, only searching online for solutions when I encountered problems.

![GitHub Desktop APP](https://pic.yupi.icu/1/screenshot-windows-dark.png)

Once you're proficient, you can learn command-line operations. Although command-line looks complex, it's actually more flexible and powerful, and many advanced features can only be implemented through command line.

Here are a few most commonly used commands. Learn these and you can handle 90% of daily development.

```bash
# Clone project
git clone https://github.com/liyupi/ai-guide.git

# Check status
git status

# Add files
git add .

# Commit
git commit -m "Added new feature"

# Push to remote
git push

# Pull latest code
git pull
```

No need to deliberately memorize them — just look them up when needed, or ask AI directly.

Here I suggest everyone install Git on your computer whether you plan to learn it or not — [just install it from the official website](https://git-scm.com/). Some software or tools might depend on Git, and not installing it could cause problems later.



### Actual Usage Scenarios

Let me demonstrate Git's usage with a practical example. Suppose you used Cursor to make a project and want to use Git for version management.

1) First, execute the command in the project's root directory to initialize Git:

```bash
git init
```

2) Then add all files and commit the first version:

```bash
git add .
git commit -m "Initial version"
```

3) Continue development and modify some code. After modification, commit again:

```bash
git add .
git commit -m "Added user login functionality"
```

4) If a modification goes wrong and you want to roll back to a previous version:

```bash
git log  # View history, find the version number you want to roll back to
git reset --hard version_number
```

Git will help you record every modification and allow you to roll back at any time.



### Combining Git and AI Tools

Many AI tools now have built-in Git functionality. For example, Cursor can commit code directly in the editor:

![](https://pic.yupi.icu/1/image-20260109110826513.png)

You can also let AI help you automatically execute Git commands — just tell it "help me use Git to manage the project."

Additionally, AI can help you generate commit messages — everything can be Vibe Coded!

I suggest everyone develop a habit: **commit once after completing each feature**.

This way, even if AI messes up the code, you can roll back to a previous version at any time. With Git, you can confidently let AI modify code, since you can always roll back.



### Learning Suggestions

Git's functionality is very powerful, but for Vibe Coding, mastering the above usage is sufficient. If you want to deeply learn Git and GitHub, you can check out the [Git & GitHub Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866) I wrote. This learning roadmap covers all Git's core knowledge points from zero to mastery, and is completely free.



## II. Deployment Hosting Platforms

You've made a project with AI, and although it runs well locally, if you want others to access it too, you need to deploy the project to a server.

Traditional deployment methods are complex: rent a server, configure environment, upload code, configure domain, etc. But now there are many free deployment platforms that can get your project online in minutes.



### Vercel

[Vercel](https://vercel.com) is currently the most popular frontend deployment platform, especially suitable for React, Next.js, Vue, static websites, and other frontend projects.

Advantages include completely free for personal projects, extremely fast deployment (usually 1~2 minutes), automatic HTTPS and CDN acceleration configuration; plus deep integration with GitHub, automatically deploying when you push code.

Using Vercel is super simple.

1) First visit [Vercel official website](https://vercel.com) to register an account — recommend using GitHub account to register and login.

2) Create a project, you can directly bind GitHub and select an already hosted project, then click the "Deploy" button:

![](https://pic.yupi.icu/1/image-20260109111323983.png)

3) Wait 1~2 minutes, and the project is online!

After successful deployment, Vercel will automatically give you a domain like `your-project.vercel.app`, and you can also bind your own domain.

Plus, every time you push code to GitHub, Vercel will automatically redeploy — completely manual operation-free.

💡 For the specific process, you can watch my video tutorial: https://www.bilibili.com/video/BV1TV4y1j76t



### Netlify

[Netlify](https://www.netlify.com/) is similar to Vercel but with more comprehensive functionality. Supports more frameworks and static site generators, has features like form processing, serverless functions, larger free quotas, and supports A/B testing and analytics. Usage is similar to Vercel, so I won't go into detail.



### EdgeOne Pages Domestic Deployment Platform

[EdgeOne Pages](https://pages.edgeone.ai) is an edge full-stack development platform launched by Tencent Cloud, based on Tencent Cloud's EdgeOne infrastructure, providing serverless deployment experience from frontend pages to dynamic APIs.

EdgeOne is Tencent Cloud's edge security acceleration platform — simply put, it's a combination of "network acceleration + security protection." It utilizes Tencent's global network nodes to serve your website from locations closer to users, making loading faster. It also integrates web protection capabilities, filtering and intercepting malicious traffic at the edge to protect your website's security.

Based on this powerful infrastructure, EdgeOne Pages has advantages like fast domestic access speed, deep integration with Tencent Cloud services, supports edge functions, and has free quotas. More suitable for domestic developer babies~



### GitHub Pages

[GitHub Pages](https://pages.github.com/) is a free static website hosting service provided by GitHub. Advantages include completely free, unlimited traffic, and seamless integration with GitHub.

Usage is super simple — after creating a repository on GitHub and uploading website files, just enable GitHub Pages in the repository settings:

![](https://pic.yupi.icu/1/image-20260109111917547.png)

Then you can access it via `username.github.io/repo-name`. Suitable for personal homepages, project documentation, simple static websites.



### How to Choose?

- If your project is Next.js, choose Vercel (officially recommended)
- If it's other frontend frameworks or static websites, both Vercel and Netlify work
- If you're a domestic user wanting faster access speed, choose EdgeOne Pages
- If it's just a simple static page, GitHub Pages is simplest

I mainly use Vercel + EdgeOne Pages because of their speed and good experience. For domestic projects I use EdgeOne Pages, and access speed is indeed much faster.



### Cloudflare CDN

If you want your website's access speed to be even faster, you can also use Cloudflare's [free CDN service](https://www.cloudflare.com/zh-cn/).

CDN (Content Delivery Network) caches your website content on servers around the world. When users access, it automatically selects the server closest to them, greatly improving loading speed.

![](https://pic.yupi.icu/1/1763643073516-5248d56c-bf7d-4537-b8f8-681a104626d9.png)

Cloudflare's advantages include:

- Completely free (for personal websites)
- Global CDN acceleration covering 200+ cities
- Automatic HTTPS certificates
- DDoS protection and web firewall
- Free DNS service

Usage is simple — register a Cloudflare account, add your domain, then change your domain's DNS servers to the addresses provided by Cloudflare. Cloudflare will automatically help accelerate and protect your website.

You can also directly use Cloudflare's Pages deployment capability — upload your code directly, and let it handle one-click deployment and free domains, even more convenient~

![](https://pic.yupi.icu/1/1763643412558-4d499b46-5e16-4f83-9df7-06a85175df35.png)

If your website is deployed on Vercel or Netlify, they already have CDN acceleration, so you don't need to configure Cloudflare separately. But if you're renting your own server for deployment, I strongly recommend using Cloudflare for acceleration.



### More Deployment Methods

I've shared multiple video tutorials on rapidly deploying projects online:

- [Vercel Project Deployment Tutorial](https://www.bilibili.com/video/BV1TV4y1j76t)
- [Cloud Editor + Vercel + Object Storage + Intranet Tunneling - 4 Deployment Methods](https://www.bilibili.com/video/BV1UZ4y197i1)
- [Nginx + Baota Panel - 2 Methods for Deploying Personal Blog](https://www.bilibili.com/video/BV1rU4y1J785)
- [WordPress to Build Personal Blog](https://www.bilibili.com/video/BV14q4y1R7XM)
- [4 Mainstream Frontend/Backend Project Deployment Methods](https://www.codefather.cn/course/1790943469757837313/section/1791075571845345281?contentType=video&tabKey=videoList)

Additionally, in [Programming Navigation](https://codefather.cn/), I've led everyone through building 20+ projects, and I've explained almost every deployment method. If you want to become a professional programmer, I recommend learning them.

- [AI Zero-Code Application Generation Platform Project](https://www.codefather.cn/course/1948291549923344386): 1Panel + Nginx frontend + Java backend (jar package)
- [Code Generator Sharing Platform Project](https://www.codefather.cn/course/1790980795074654209): Baota panel + Nginx frontend + Java project manager (jar package) backend deployment
- [AI Q&A Application Platform Project](https://www.code-nav.cn/course/1790274408835506178): Vercel frontend + Docker backend + cloud hosting Serverless platform deployment
- [AI Super Agent Project](https://www.codefather.cn/course/1915010091721236482): Docker frontend + Docker backend + cloud hosting Serverless platform deployment
- [OJ Online Judge Project](https://www.codefather.cn/course/1790980707917017089): Docker Compose backend microservice deployment

Basically, mastering these few deployment methods will handle the vast majority of deployment needs.



## III. MCP Services - Extending AI Capabilities

MCP (Model Context Protocol) is an open standard that allows AI tools to connect to various external tools and data sources.

Simply put, MCP is like installing various "plugins" on AI, letting it do more things. For example, filesystem MCP lets AI read and write files, GitHub MCP lets AI operate GitHub repositories, database MCP lets AI query databases, browser MCP lets AI browse web pages.

![](https://pic.yupi.icu/1/mcp.png)

Now almost all mainstream AI programming tools support MCP, including Cursor, Claude Code, Cline, Windsurf, Gemini CLI, Kiro, etc. You can use various MCP services in these tools, greatly extending AI's capabilities.

Let me use Cursor as an example to demonstrate how to configure and use MCP.



### Using MCP in Cursor

Let me demonstrate how to configure and use MCP in Cursor with a practical example.

For instance, I want Cursor to know the current accurate time.

1) Use the MCP collection website to search for the MCP tool you need, and obtain the MCP configuration information — you'll need it later:

![](https://pic.yupi.icu/1/image-20260109113038258.png)

Since this MCP tool needs to use the `uvx` command to install, we first need to install the uv tool. Refer to the [official installation documentation](https://docs.astral.sh/uv/getting-started/installation/), select your operating system and execute one command to complete the installation.

![](https://pic.yupi.icu/1/image-20260109113308798.png)

After installation, execute the `uvx` command — you should see the output in the image below, indicating successful installation:

![](https://pic.yupi.icu/1/image-20260109113427041.png)



2) Open Cursor settings, find the MCP configuration option, and click to add MCP:

![](https://pic.yupi.icu/1/image-20260109113809834.png)



3) Cursor manages MCP through JSON files. Add the MCP server configuration copied earlier:

```json
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": [
        "mcp-server-time",
        "--local-timezone=America/New_York"
      ]
    }
  }
}
```

![](https://pic.yupi.icu/1/image-20260109112647904.png)



4) After saving, you'll find the MCP tool is successfully enabled. Now AI can get the latest time.

![](https://pic.yupi.icu/1/image-20260109113524465.png)



5) You can ask AI: What time is it now?

AI can give you the most accurate time by calling MCP.

![](https://pic.yupi.icu/1/image-20260109113631840.png)



There are more commonly used MCP servers, such as:

- @modelcontextprotocol/server-filesystem: Filesystem access
- @modelcontextprotocol/server-github: GitHub operations
- @modelcontextprotocol/server-postgres: Database queries
- @modelcontextprotocol/server-puppeteer: Browser automation



If you want to learn more about MCP services, you can visit:

- [Fish Skin AI Navigation's MCP Collection](https://ai.codefather.cn/): Various practical MCP services organized
- [mcp.so](https://mcp.so/): MCP server marketplace where you can find various MCP services
- [GitHub awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers): Community-maintained MCP server list

These websites will continuously update with the latest MCP services — recommend bookmarking them.



## IV. Other Practical Tools

Besides version management, deployment platforms, and MCP, there are some other practical tools worth understanding.



### GitHub Code Hosting

[GitHub](https://github.com/liyupi) is the world's largest code hosting platform — you can not only host code but also communicate with excellent developers from around the world ♂.

On GitHub you can host code, showcase projects, learn from others' code, and participate in open source projects. Plus, many AI tools support integration with GitHub, like Cursor, Vercel, Netlify, etc.

![Fish Skin GitHub's Project Repositories](https://pic.yupi.icu/1/image-20251126231252956.png)

I suggest creating a GitHub repository for each of your projects — this both backs up your code and showcases your work.



### Image Hosting Tools

If your project needs images, you'll encounter a problem: where to put the images?

Putting them directly in the project makes the project very large, and if you put image files on your own small pipe server, loading speed will be relatively slow. This is where image hosting tools come in.

**Image hosting tools are services specifically for storing and managing images** — you upload images and they give you a link, which you can use in your project.

Image hosting tools come in two types: **online image hosting** and **local image hosting tools**.

Online image hosting means uploading images directly on a webpage, like [imgchr](https://imgchr.com/) — the advantage is it's simple and convenient, the downside is it might not be very stable.

I recommend [PicGo](https://molunerfinn.com/PicGo/) more, a local image hosting tool that supports multiple image hosting platforms (GitHub, Qiniu Cloud, Tencent Cloud, Alibaba Cloud, etc.). You can manage images locally, automatically copy links after upload — very convenient.

![](https://pic.yupi.icu/1/image-20260109114343606.png)

Plus, PicGo supports shortcut key upload, screenshot upload, and other features — it's particularly handy to use. If you frequently need to insert images in articles or projects, I strongly recommend trying PicGo.

When writing articles, I generally use the Typora writing tool + PicGo for uploading images, ensuring that images in my articles can be accessed from any computer.



### Environment Variable Management

In projects, you often need to use sensitive information like API Keys, database passwords, etc. Never write these directly in code! Otherwise, as soon as someone sees your code, these keys are leaked.

The correct approach is to use environment variables. For local development, create a `.env` file:

```
OPENAI_API_KEY=your_key_here
DATABASE_URL=your_database_url
```

Then read it in code using `process.env.OPENAI_API_KEY` style.

When deploying to Vercel or Netlify, add environment variables in their settings pages — no need to upload the `.env` file. This is both secure and convenient to manage.



### Domain Services

Simply put, a domain name is your website's address. Like `codefather.cn`, `dogyupi.com`.

If you want your project to have a memorable web address, you need to purchase a domain name rather than having users access via IP.

For domestic users, I recommend purchasing domains from well-known cloud service providers like [Alibaba Cloud](https://wanwang.aliyun.com/) or [Tencent Cloud](https://dnspod.cloud.tencent.com/). Prices are usually a few dozen yuan per year, and the operation interfaces are in Chinese and very convenient.

![](https://pic.yupi.icu/1/image-20260109114615834.png)

Note that **if your website server is in China, the domain needs to be filed (registered)**. The filing process takes about 1~2 weeks and requires providing ID, phone number, and other information.

If your website is deployed on foreign platforms like Vercel or Netlify, or if you purchase a domain from a foreign platform, you can skip filing and go online quickly.



### Database Services

A database is where data is stored.

For example, if you make a to-do list application, users' to-do items need to be stored in a database; if you make a blog website, article content needs to be stored in a database.

For Vibe Coding developers, I strongly recommend [Supabase](https://supabase.com/). It's an open-source database service that offers free quotas and is very feature-rich:

- Provides PostgreSQL database (powerful relational database)
- Built-in user authentication functionality (registration, login, password reset, etc.)
- Provides file storage functionality, can store images, videos, etc.
- Real-time data synchronization, automatically updates when data changes
- User-friendly visual interface, manage data without writing SQL

![](https://pic.yupi.icu/1/image-20260109114906767.png)

Plus, Supabase's documentation is very detailed, making it especially convenient to use with AI tools. You just need to tell AI: "use Supabase to make a user registration feature," and AI can help you write the code.

Besides Supabase, there are other options:

- PlanetScale: MySQL database, has free quotas
- MongoDB Atlas: NoSQL database, has free quotas

If you want to quickly learn more about databases, you can watch [my database quick start video](https://www.bilibili.com/video/BV1iJSLBbEyD/).



### Code Snippet Management - Code Copy

During development, you might encounter some useful code snippets you want to save for later. Or you encounter a Bug and want to share code with someone to help you look at it. This is where code snippet management tools come in.

I strongly recommend [Code Copy](https://codecopy.cn/), developed by our team. This is a simple and easy-to-use code sharing tool that allows fast, cross-device free code sharing.

![Code Copy](https://pic.yupi.icu/1/1705646241236-26786c47-1251-4891-85f3-e91ac9e4be94-20240125151504219-20240222165129145.png)

Code Copy's advantages:

- Interface similar to editors commonly used by programmers, can add and delete code snippets
- Supports multiple sharing scopes (public, encrypted, personal only)
- Supports multiple sharing methods (copy link, QQ share, mobile scan, WeChat mini-program, etc.)
- Also has a code library feature, can view and learn quality code shared by other students
- Supports online code execution, AI intelligent code analysis and error correction

Whether on computer or mobile, you can get a good reading experience. And it's completely free — no need to worry about code leakage.

**Please! When asking others to help fix bugs, don't take blurry photos or send code directly in chat anymore** — share with Code Copy and it will be much more comfortable for the other person.



### Icon Libraries and Assets

When making websites or applications, you often need some icons and image assets. Here are some free resource websites:

Icon libraries:

- [iconfont](https://www.iconfont.cn/): Alibaba vector icon library, China's largest icon library, completely free
- [Font Awesome](https://fontawesome.com/): Popular foreign icon library, has free and paid versions
- [Iconify](https://iconify.design/): Integrates multiple icon libraries, one-stop search

Placeholder images:

- [Picsum Photos](https://picsum.photos/): Randomly generates placeholder images, can specify dimensions

Free images:

- [Unsplash](https://unsplash.com/): High-quality free images, can be used commercially
- [Pexels](https://www.pexels.com/): Free images and video assets

These resources can all be used for free and are high quality. Combined with AI tools, you can quickly make beautiful websites.



## In Conclusion

OK, these are the commonly used auxiliary tools in Vibe Coding development — I bet everyone's bookmarking like crazy now.

When starting to learn, you might feel like there's a lot to learn. But actually, you don't need to learn everything at once — you can proceed step by step. When you encounter problems, learn the corresponding tools then — this is the most efficient way to learn.

I suggest you try downloading and using Git, push code to GitHub, then deploy to Vercel. Watching your project run online and sharing it with friends will give you an exploding sense of achievement!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
