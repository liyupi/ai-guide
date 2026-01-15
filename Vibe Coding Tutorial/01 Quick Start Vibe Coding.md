# Quick Start Vibe Coding

> Build and deploy your first web application in 10 minutes



Hello, I'm Programmer Fish Skin, former Tencent full-stack developer, [AI Programming Blogger](https://space.bilibili.com/12890453) with 2 million followers across platforms, and creator of 10+ self-developed products including [AI Navigation](https://ai.codefather.cn) and [Programming Navigation](https://www.codefather.cn).

In the previous article, we discussed the philosophy and mindset of Vibe Coding. Now, it's time to get hands-on!

In this article, I'll guide you step-by-step to build your first web application within 10 minutes and deploy it to the internet so people around the world can access it.

Yes, you heard that right. You don't need any programming background. As long as you can type and access the internet, you can follow along.



## I. Preparation

Before we start, we need to do some simple preparation. Don't worry, these are all very simple and can be done in 5 minutes.

What you need to prepare:

1. A computer with internet access (Windows, Mac both work)
2. A browser (Chrome, Edge, Safari all work)
3. An AI tool account (we'll use Bolt.new, it's free)
4. A GitHub account (for deployment, also free)

That's it. No need to install any programming software, no need to learn any code. Everything is done in the browser.

💡 What is GitHub?

[GitHub](https://github.com/) is currently the most mainstream free code open-source hosting platform. You can think of it as a "cloud storage" for storing and managing code. All users or teams can upload their code to GitHub for sharing and maintenance, download code from GitHub, etc. Developers can get code for free from GitHub for learning or reference.

If you're interested in GitHub, you can check out [Fish Skin's Nanny-level GitHub Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190804671012866) to learn for free.



### How to Choose an AI Tool?

For complete beginners, I strongly recommend starting with Bolt.new. It's completely online, requires no software installation, and works right in your browser. Best of all, you can see results immediately after writing code, and with one click you can publish it online - completely zero barrier. It also has a free tier that's enough for beginners to practice.

Once you're proficient, it's not too late to learn professional tools like Cursor.

Note: If your network cannot access Bolt.new, you can also try [Meituan NoCode](https://nocode.cn/) or [Baidu Miaoda](https://www.miaoda.cn/). Both are similar AI application generation platforms.



### Register for Bolt.new

1) Open your browser and visit: https://bolt.new

2) Click the "Sign in" button in the upper right corner

3) You can choose to sign in with Google account / GitHub account / email password (GitHub is recommended since it will be used for deployment later)

After successful login, the preparation is complete. Now you can enter requirements in the chat box to generate projects.

![](https://pic.yupi.icu/1/image-20260104140815455.png)



## II. Choose Your First Project

Your first project is very important - it directly determines your learning experience. I suggest choosing a simple but complete project, preferably one with practical use where you can see results.

Based on my experience, the following projects are quite suitable for beginners and can be easily completed.

1) Personal Business Card Webpage: Displays your name, avatar, self-introduction, and contact information. Simple and beautiful. Suitable for friends who want to quickly experience a sense of achievement.

2) Todo Application: A simple task management tool (commonly known as Todo List). Can add tasks, mark completion, delete tasks. Suitable for friends who want to make something practical.

3) Countdown Webpage: Can set a target date (like exam, birthday), displays remaining days in real-time with beautiful visual effects. Suitable for friends who want to make something creative.

In this tutorial, I'll use the classic **Todo Application** as an example because it has complete functionality, strong practicality, and lets you experience the complete development process. If you want to make other projects, that's completely fine - the steps are the same, just change the requirement description to what you want.



## III. Chat with AI to Generate Code

Alright, now comes the most exciting part - chatting with AI and having it help you generate code.


### Round 1: Describe Basic Requirements

In Bolt.new's chat box, enter the following (you can copy directly):

```
Please help me make a todo application webpage with these requirements:

1. Functional requirements:
   - Can input task content and add to list
   - Each task has a checkbox in front, clicking it marks completion
   - Completed tasks show strikethrough
   - Each task has a delete button after it
   - Display count of completed and incomplete tasks

2. Interface requirements:
   - Clean and modern design style
   - Use fresh blue color scheme
   - Rounded buttons and input boxes
   - Appropriate shadow effects
   - Responsive design, works normally on mobile phones

3. Technical requirements:
   - Use HTML + CSS + JavaScript
   - Data saved in browser local storage, refreshing page won't lose data
```

You can also choose large language models, use plan mode, add attachments, enhance prompts, etc., but I suggest not focusing on these at first. Just click send and wait for AI's response.

![](https://pic.yupi.icu/1/image-20260104141314370.png)



### What is AI Doing?

After sending, you'll see Bolt.new start working.

AI understands your requirements, then creates the project file structure, and automatically generates webpage code. The whole process takes about 2 minutes.

![](https://pic.yupi.icu/1/image-20260104141512389.png)

After code generation is complete, the preview automatically displays on the right side. You'll see an input box, an add button, and a task list area.

Try entering "Learn Vibe Coding with Fish Skin" in the input box, then click the add button to see the effect.

![](https://pic.yupi.icu/1/image-20260104141637255.png)



### Round 2: Refine Details

After seeing the initial version, you might want to adjust some details. For example:

```
Great! But I want to make some adjustments:

1. Change input placeholder text to "What needs to be done today?"
2. Change add button to "➕ Add Task"
3. Change title to "My Todo List" and add a cute icon
4. Change background color to gradient, from light blue to light purple
5. Add a "Clear Completed" button
```

You can also enable visual editing mode, select the element you want to modify, and click wherever you're not satisfied~

![](https://pic.yupi.icu/1/image-20260104141819294.png)

AI will modify the code according to your requirements, and soon you'll see the new effect.

![](https://pic.yupi.icu/1/image-20260104142026165.png)



### Round 3: Add New Features

If you want to add more features, continue chatting with AI:

```
Add a few more features:

1. Tasks can have priority levels (high, medium, low), marked with different colors
2. Can edit added tasks
3. Add a "Clear All" button that requires confirmation
4. When task list is empty, display a friendly prompt
```

AI will continue to help you implement these features.

![](https://pic.yupi.icu/1/image-20260104142238907.png)



### Conversation Tips

Remember these points when chatting with AI:

1. Be specific with requirements: Don't say "make it look better," say "change background to blue gradient, add rounded corners to buttons"
2. Don't change too much at once: 1~5 requests per round is enough, see the effect before continuing
3. Speak up when you encounter problems: If there's a bug or the effect isn't right, tell AI directly "there's a problem with XX"
4. Can ask for explanations: For things you don't understand, you can ask "what does this code do?"



## IV. Verify the Effect

Now, your todo application is complete. Let's test each feature:

1) Enter "Learn Vibe Coding with Fish Skin" in the input box, click add button, task appears in list

2) Click checkbox before task, task text shows strikethrough; click delete button, task disappears from list.

Finally, click the device icon above the preview window to see how it looks on phones and different screens.

![](https://pic.yupi.icu/1/image-20260104142538383.png)

If you find a feature isn't working properly, don't panic. Describe the problem to AI in detail, like "I clicked the delete button but the task wasn't deleted," and AI will help you fix the bug, then test again.

This is the charm of Vibe Coding - when you encounter problems, AI helps you solve them!



## V. Deploy Online

Now that the application is done, let's publish it to the internet so everyone in the world can access it!

### Quick Deployment (Recommended)

Bolt.new provides the simplest deployment method. Just click the "Publish" button in the upper right corner and click publish:

![](https://pic.yupi.icu/1/image-20260104142853639.png)

Then wait a moment, and you'll see the published accessible URL in the chat box:

![](https://pic.yupi.icu/1/image-20260104142912318.png)

After successful deployment, you should be able to access your application from any browser, or share the address with friends so they can access it too.

Congratulations, your first web application is now online. It's that simple!🎉

💡 If you think the address looks ugly, Bolt.new also supports custom domains, but only in the premium version. I don't think it's necessary.



### Extended Knowledge - Manual Deployment

Fish Skin has shared multiple video tutorials on quickly deploying projects online:

- [Vercel Project Deployment Tutorial](https://www.bilibili.com/video/BV1TV4y1j76t)
- [Cloud Editor + Vercel + Object Storage + Internal Network Tunneling 4 Deployment Methods](https://www.bilibili.com/video/BV1UZ4y197i1)
- [Nginx + BT Panel 2 Methods to Deploy Personal Blog](https://www.bilibili.com/video/BV1rU4y1J785)
- [Build Personal Blog with WordPress](https://www.bilibili.com/video/BV14q4y1R7XM)
- [4 Mainstream Frontend and Backend Project Deployments](https://www.codefather.cn/course/1790943469757837313/section/1791075571845345281?contentType=video&tabKey=videoList)

In addition, Fish Skin has led everyone through 20+ projects on [Programming Navigation](https://codefather.cn/), and has explained almost every deployment method. If you want to become a professional programmer, I suggest learning them.

- [AI Zero-Code Application Generation Platform Project](https://www.codefather.cn/course/1948291549923344386): 1Panel + Nginx frontend + Java backend (jar package)
- [Code Generator Sharing Platform Project](https://www.codefather.cn/course/1790980795074654209): BT Panel + Nginx frontend + Java project manager (jar package) backend deployment
- [AI Quiz Application Platform Project](https://www.code-nav.cn/course/1790274408835506178): Vercel frontend + Docker backend + Cloud hosting Serverless platform deployment
- [AI Super Agent Project](https://www.codefather.cn/course/1915010091721236482): Docker frontend + Docker backend + Cloud hosting Serverless platform deployment
- [OJ Online Judging Project](https://www.codefather.cn/course/1790980707917017089): Docker Compose backend microservice deployment

Basically, mastering these deployment methods can handle the vast majority of deployment needs.



## VI. Understand What You Made

Now that the project is done, let's spend a few minutes understanding what you made. This will help you build better projects in the future.



### Project Structure

First, you should know that the foundation of web applications is the "frontend trio":

- HTML (Structure): Defines what elements are on the page, like input boxes, buttons, task lists, statistics.
- CSS (Style): Defines what the page looks like, including colors, fonts, sizes, layout and spacing, animation effects.
- JavaScript (Functionality): Defines how the page works, including adding tasks, marking completion, deleting tasks, local storage logic.

However, in this project, AI chose to use **React**, a modern frontend development framework to help you implement features. React is one of the most popular frontend frameworks currently - it makes development more efficient and code easier to maintain.

So you'll see files with `.tsx` suffix in the project files. These are React component files. But essentially, they're eventually converted to HTML, CSS, and JavaScript that browsers can understand.

![](https://pic.yupi.icu/1/image-20260104162356144.png)

Don't worry, it's completely fine not to understand this now. If you're interested in frontend development, you can check out [Fish Skin's latest Nanny-level Frontend Learning Roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190394078011393) to get started quickly.



### Core Functionality Analysis (Can Skip)

Let's see how several key features are implemented:

1) Add Task: When you click the "Add Task" button, the program first gets the text from the input box, then creates a new task object, adds the task to the list, saves it to local storage at the same time, and finally clears the input box and refreshes the page display. The whole process is as natural as writing a todo item on paper and sticking it on the wall.

2) Mark Complete: When you click the checkbox, the program finds the corresponding task, modifies its completion status, updates local storage, then updates the page display (adds strikethrough to task text), and updates the statistics at the same time. Just like using a pen to draw a line through a task on paper.

3) Local Storage

You might wonder, why are tasks still there after refreshing the page?

This is because data is saved in the browser's local storage (localStorage). Every time you modify a task, the program saves the latest data to localStorage; when you reopen the page, the program reads the previously saved data from localStorage. This way, even if you close the browser, data won't be lost. It's like writing your todo list on a small notebook that won't get lost.

![](https://pic.yupi.icu/1/theoryofworksoftware%E5%A4%A7.jpeg)



### Ask AI

If you want to deeply understand a certain part, you can directly ask AI:

```
Please explain how local storage works?
```

Or:

```
What does this code do?
[paste code]
```

AI will explain to you in easy-to-understand language.



## VII. Try Modifying and Optimizing

Now that you have a practical little application, let's try some modifications and optimizations to deepen understanding.

You can try:

- Change color theme ("Make the application pink themed, gentle and cute feeling")
- Modify text ("Change all text to English version")
- Adjust layout ("Move statistics to bottom of page and center display")

Or add new features, like:

- Task search ("Add a search box that can search task content")
- Task categories ("Add categorization feature, can add tags to tasks")
- Export function ("Add a button that can export all tasks as a text file")

You can also optimize user experience to make the application more usable:

- Add keyboard shortcuts ("Press Enter to quickly add tasks")
- Add animations ("Add fade-in animation when adding tasks, slide-out animation when deleting tasks")
- Optimize empty state ("When there are no tasks, display a cute illustration and encouraging text").

If you think it's simple, you can try adding:

- Due date functionality
- Task reminder functionality
- Support drag-and-drop reordering
- Add dark mode toggle
- Support multiple task lists

Every time you want to add a new feature, just tell AI "I want to add [feature description], how should I do it?" and AI will help you implement it.



## In Conclusion

Congratulations, you've completed your first Vibe Coding practical exercise.

What you just did would have taken months of study to complete a few years ago. But today, it only took you 10 minutes! This is the power of Vibe Coding.

Through this project, you've learned how to clearly describe requirements to AI, continuously optimize projects through multiple rounds of conversation, collaborate with AI to solve problems when they arise, and how to publish projects to the internet. Although you didn't write code, you already understand the basic structure of web applications, how user interaction is implemented, and basic concepts of data storage.

More importantly, you've established the Vibe Coding mindset: **focus on "what to do" rather than "how to do it," make it first then continuously optimize, learn by doing projects rather than learning first then doing, treat AI as a programming partner rather than a tool.**

This is just the beginning. As you do more and more projects, you'll find your ability to express requirements getting stronger, your understanding of technology getting deeper, the things you can make getting more complex, and your creativity truly unleashed.

Remember what I said in the first article: **in the AI era, creativity is more important than technology, ideas are more important than implementation, iteration is more important than perfection.**



### Next Steps

Next, I suggest you do 2~3 similar difficulty projects to consolidate your practice, like personal business card webpage, countdown application, simple calculator, weather query tool.

Practice is the best teacher - only by truly doing it yourself can you truly understand the charm of Vibe Coding.

When you're proficient with the Bolt.new platform and simple project development, you can directly continue learning the follow-up content of this tutorial:

- [Advanced Optional] Programming Tools
- [Advanced Optional] Project Practice
- [Advanced Optional] Experience and Techniques
- [Advanced Optional] Resource Treasury

You can also first learn about Cursor (more professional AI code editor), GitHub (code management and collaboration), more deployment platforms, etc.

Keep going, you can do it!💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
