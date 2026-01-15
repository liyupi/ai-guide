# Vibe Coding FAQ and Solutions


Hello, I'm Programmer Fish Skin, former Tencent full-stack developer, [AI Programming Blogger](https://space.bilibili.com/12890453) with 2 million followers across platforms, and creator of 10+ self-developed products including [AI Navigation](https://ai.codefather.cn) and [Programming Navigation](https://www.codefather.cn).

Previously, I systematically explained various techniques and methods of Vibe Coding. In this article, I'll summarize the most commonly encountered problems and solutions in Vibe Coding practice.

You can use this as a quick reference guide. When you encounter problems, check here first - you might find the answer. If it's not here, you can also ask questions on my [Programming Navigation](https://www.codefather.cn/), or exchange ideas and find answers with other AI enthusiasts in [Fish Skin's AI Navigation](https://ai.codefather.cn/).




## Vibe Coding Concept Understanding


### What's the difference between Vibe Coding and traditional programming?

Answer: Traditional programming is you writing code yourself, Vibe Coding is you describing requirements in natural language and having AI help you write code. Traditional programming requires you to master programming language syntax and details, while Vibe Coding focuses more on expressing requirements and guiding AI. But essentially, they're both solving problems, just in different ways. You can think of traditional programming as cooking yourself, Vibe Coding as ordering food delivery - you get to eat either way, but the process is completely different.



### Is Vibe Coding suitable for everyone?

Answer: Vibe Coding lowers the barrier to programming, allowing more people to participate in development. But it's not all-powerful - for very complex systems, projects with extremely high performance requirements, or scenarios needing deep optimization, traditional programming may be more suitable. Vibe Coding is best suited for rapid prototyping, personal projects, small to medium applications, and utility software. If you're a complete beginner wanting to learn programming, or want to quickly turn ideas into products, Vibe Coding is perfect for you.



### After learning Vibe Coding, do I still need to learn traditional programming?

Answer: Yes, but don't rush. Vibe Coding can help you quickly implement features, but to truly understand code, debug complex problems, and optimize performance, you still need programming fundamentals. I suggest learning programming knowledge while using Vibe Coding to build projects. This way of learning is more efficient and motivating. You can first use AI to build a few projects, and after gaining a sense of achievement, systematically learn programming - this will be much more interesting than starting with books from the beginning.



### Is AI-generated code reliable?

Answer: AI-generated code works, but isn't necessarily perfect. It may have bugs, performance issues, or security vulnerabilities. So you need to test functionality, review code, and continuously optimize. Don't blindly trust AI - maintain critical thinking. Just like you'd check if food delivery is fresh, AI-generated code needs your oversight. However, as AI models improve, code quality is getting better and better.



### Will Vibe Coding replace programmers?

Answer: It won't completely replace, but will change how programmers work. Just as calculators didn't replace mathematicians and search engines didn't replace librarians, AI programming tools will become assistants to programmers, not replacements. Future programmers will need stronger product thinking, architecture capabilities, and problem-solving skills, not just coding ability. Programmers who can use AI will be more competitive than those who can't.



### What is AI hallucination?

Answer: AI hallucination refers to AI fabricating non-existent content, such as inventing a non-existent API, incorrect function usage, or libraries that don't exist at all. This is an inherent problem with AI models because they generate content based on probability. When encountering hallucinations, don't panic - ask AI to provide documentation links for verification, or check official documentation yourself. If AI insists on errors, try a different model or start a new conversation to re-describe the problem.



### What does MVP mean?

Answer: MVP stands for Minimum Viable Product. Simply put, it's making the simplest but usable version first, then gradually improving it. For example, when building an accounting app, the MVP version might only have three features: record expenses, view list, and calculate total. Other features like categorization, charts, and export can be added later. The benefit is quickly validating ideas, avoiding getting stuck in details from the start, and maintaining development momentum.



### What is a context window?

Answer: Context window refers to the maximum amount of content an AI model can "remember" at one time, usually measured in Tokens. For example, Claude Sonnet 4.5 has a context window of 200K Token, approximately equivalent to 150,000 Chinese characters. The larger the context window, the more code AI can process and the longer conversation history it can remember. If your project has a lot of code, choosing a model with a large context window is more appropriate. For example, Gemini 3 Pro supports 1M Token.




## Vibe Coding Tool Selection


### Which is better, Cursor or Windsurf?

Answer: Both are excellent, each with its own characteristics. Cursor has a more mature ecosystem, larger community, more plugins, and more complete documentation. Windsurf has some innovative features like Cascade mode and a more modern interface.

If you're a beginner, I suggest starting with Cursor because it's easier to find solutions when you encounter problems. If you like trying new things, you can try Windsurf. Of course, the best approach is "I want them all" - try both and see which suits your workflow better.



### Is the free version sufficient?

Answer: For learning and small projects, the free version is sufficient. Cursor's free version has a monthly quota for certain models. But for daily work or large projects, I recommend the paid version. The paid version has more quotas, stronger models, and better experience - essentially trading money for time.

You can try the free version first and upgrade if you find it useful. Students can take full advantage of various free resources - completely sufficient for learning.



### How do I choose an AI model?

Answer: Choose based on task complexity and budget. Use cheaper models (Gemini Flash, DeepSeek) for simple tasks, powerful models (Claude Opus, GPT-5) for complex tasks. If doing frontend UI, Gemini 3 Pro performs very well. If doing full-stack projects, Claude Sonnet is more comprehensive. If budget is limited, domestic models (DeepSeek, Tongyi Qianwen, Zhipu GLM) offer great value.

If you're unsure, you can use Auto mode to let the tool choose automatically, or first try a cheaper model and switch to a stronger one if needed.



### What's the difference between Bolt.new and v0.dev?

Answer: Bolt.new is better suited for full-stack applications - it can generate complete frontend and backend code, and can run and debug directly in the browser. v0.dev focuses more on frontend UI components and is particularly good at generating beautiful interfaces. If you want to quickly build a complete application, use Bolt.new. If you just want to generate some UI components, use v0.dev. Both are no-code platforms that don't require software installation - just open a browser and use them, especially suitable for beginners.



### Where do I get an API Key?

Answer: Go to the corresponding service's official website to register an account, then generate a Key in settings or the API page. For example, OpenAI's Key is obtained at platform.openai.com, Anthropic's Claude Key at console.anthropic.com, and Supabase's Key is in project settings.

After generating an API Key, remember to keep it safe - don't leak it or commit it to public repositories like GitHub. I recommend using environment variables or configuration files to manage API Keys, avoiding hardcoding them in code.



### How do I access Cursor and Claude from within China?

Answer: Cursor can be accessed directly, but Claude's official website may be difficult to access from within China. You can use domestic models as alternatives - DeepSeek, Tongyi Qianwen, and Zhipu GLM are already very close to international models in programming capability, and they have faster access speeds and lower prices. If you must use Claude, consider using the API approach or relay services like OpenRouter.



### What AI modes does Cursor have?

Answer: Cursor 2.0 mainly provides 2 major AI interaction modes:

1. Chat mode: Conversation mode, suitable for asking questions, explaining code, and small-scale modifications.
2. Agent mode: The most powerful mode, can autonomously plan and execute complex tasks, modify multiple files simultaneously, and supports running multiple agents in parallel.

If you just want to ask questions or modify a function, Chat is enough. If you're adding new features or modifications involving multiple files, Agent is more appropriate. Agent mode also supports Plan Mode, which generates a plan for your confirmation before executing modifications.



### Should I choose a no-code platform or code editor?

Answer: If you're completely zero foundation or just want to quickly build a prototype, use a no-code platform (Bolt.new, v0.dev). If you want to build complex projects, need more control, or want to learn programming, use a code editor (Cursor, Claude Code, etc.).

No-code platforms are simple and fast but have limited flexibility. Code editors are powerful but have a steeper learning curve. I suggest starting with a no-code platform to get a feel for things, then learning code editors once you're comfortable.




## Vibe Coding Usage Tips


### What if AI-generated code has errors?

Answer: Copy the complete error message and relevant code to AI and have it analyze and fix it. Make sure to include the complete error stack, not just one sentence. If AI can't fix it, try switching to a stronger model, or start a new conversation to re-describe the problem. You can also look up documentation or search for solutions yourself, or seek help in communities or forums. Often, error messages themselves contain clues to the solution - learning to read error messages is important.



### What if AI always uses the wrong tech stack?

Answer: At the beginning of each conversation, clearly state your tech stack. For example: "I'm using React + TypeScript + Tailwind CSS, please implement using these technologies."

Or configure a `.cursorrules` file in your project so AI automatically knows your tech stack.

If AI still uses the wrong one, interrupt and correct immediately: "I'm using React, not Vue, please rewrite using React!"

After emphasizing multiple times, AI will remember.



### How do I make AI-generated code match project style better?

Answer: Provide reference code for AI to imitate. For example: "Please write the new component referencing this component's style," then paste the reference code.

Or explain code style in detail in context files, including naming rules, component structure, comment format, etc.

You can also provide a code specification document for AI to follow.

Most importantly, be as specific as possible with prompts - don't just say "make it look better," clearly explain what "better" means.



### What if AI-generated code has poor performance?

Answer: First use tools like Chrome DevTools and Lighthouse to find performance bottlenecks, then have AI optimize specifically. For example: "This list renders very slowly, please optimize with virtual scrolling," or "This function is very slow with large data, please optimize the algorithm."

Don't pursue perfect performance from the start - get the functionality working first, then optimize when you discover bottlenecks. In most cases, AI-generated code performance is already sufficient.



### How do I handle AI hallucinations?

Answer: If AI invents a non-existent API, ask it to provide documentation links. If it can't provide them, it's a hallucination - tell it to use the correct API.

If AI gets stuck in a loop, cut off the context and start a new conversation.

If AI insists on an incorrect solution, try a different model or check documentation yourself.

For uncertain content, always verify - don't believe blindly. I recommend developing the habit of checking documentation - it's an essential programmer skill.



### How do I debug AI-generated code?

Answer: Use breakpoint debugging instead of just console.log.

You can set breakpoints in your browser or editor, execute code step by step, and view variable values. This gives you a clearer view of code execution. If you still can't find the problem, give the error message and code to AI and have it help you analyze. You can also have AI add detailed logging to help you understand code execution flow.

Debugging is an essential programmer skill and worth spending time learning.



### How do I improve prompt quality?

Answer: Prompts should be specific, clear, and structured. Don't say "make a website," say "make an accounting website with three features: add expenses, view list, and show total statistics, use blue color scheme, clean and modern style."

You can break prompts into several parts: functional requirements, interface requirements, technical requirements. You can also provide reference examples, like "interface style should reference Notion."

Remember, the more detailed your prompt, the more AI-generated results will match expectations.



### What if AI-generated code is too verbose?

Answer: Have AI refactor the code, extract repeated parts, and simplify logic. For example: "This code is too long, please refactor it, extract common functions, reduce duplication." Or "Please implement this feature in a more concise way."

AI generally prioritizes making code work over being concise, so you need to actively request optimization. But don't over-pursue conciseness - readability is more important.



### How do I have AI explain code?

Answer: By having AI explain code, you can faster understand and learn. You can directly ask AI "What does this code do? Please explain in detail," or "What's the logic of this function? Why is it written this way?" AI will explain to you in easy-to-understand language.

If the explanation is too simple, you can say "Please explain in more detail, including what each step does." If the explanation is too complex, you can say "Please explain in simpler language, I'm a beginner," or even say "I'm an idiot" - the effect might be unexpected~



### How do I handle outdated AI-generated code?

Answer: AI's training data may lag, so sometimes it generates old version code. You need to clearly tell AI to use the latest version, like "Please use React 19's latest syntax" or "Please use Next.js 15's App Router." And be sure to provide AI with the latest official documentation.



### How do I add code examples to prompts?

Answer: Simply wrap code with three backticks and paste it into your prompt. For example:

````markdown
Please reference this code's style:

```jsx
Code content
```
````

If the code is long, you can only paste key parts. You can also use the `@` capability of AI code editors to have AI read files from your project, like "Please reference the style of @src/components/Button.tsx". Providing code examples helps AI more accurately understand your needs.



### What if AI always generates repetitive code?

Answer: Remind AI to extract common functions or components. For example: "This code has a lot of repetition, please extract into common functions," or "Please create a reusable component." You can also explicitly state in your prompt "avoid repetitive code, use DRY principle." If AI still generates repetitive code, you can manually refactor yourself or try a different model.



### How do I handle unsafe AI-generated code?

Answer: Have AI review code security. For example: "Please check if this code has security issues" or "Please add input validation to prevent XSS attacks." You can also use security scanning tools - for frontend code, you can use ESLint security plugins. For sensitive operations (like user authentication, payments), be extra careful and preferably have experienced developers review, or use multiple different advanced AI models for cross-validation.




## Vibe Coding Project Development


### What if code gets messy halfway through a project?

Answer: Refactor promptly - don't wait until it's completely chaotic to deal with it. After completing each feature, spend 10~15 minutes organizing code. Extract repetitive code, split large functions, improve naming, add comments.

If it's already very messy, you can have AI help you refactor, but do it in small steps and test after each step. For example: "Please help me refactor this file, extract common functions," rather than "refactor the entire project." Small steps, quick iterations, gradual improvement.

Note: Before refactoring, be sure to commit the current code with Git first! This way, even if refactoring has problems, you can always roll back to the previous version. Developing the habit of frequent commits is the best way to protect your code.



### How do I deploy AI-generated projects?

Answer: Many no-code platforms (like Bolt.new) support one-click deployment - just click a button to go online.

For manual deployment, you can use platforms like Vercel or Netlify. Push code to GitHub, then connect your repository on the platform - it will automatically build and deploy.

If you need a backend, you can use BaaS services like Supabase. If you need your own server, you can use Docker for containerized deployment.

In short, deployment isn't that difficult - just follow Fish Skin's deployment tutorial step by step.



### What if bugs appear after project launch?

Answer: First, use monitoring tools (Sentry, LogRocket) to collect error information. Then, reproduce the problem locally to find the cause.

After fixing, have AI write more tests to ensure the problem doesn't recur. Finally, deploy the fix version as soon as possible.

To avoid this situation, fully test before launch, including functional testing, edge case testing, and testing on different devices. You can have friends help test - they often discover problems you didn't notice alone.



### How do I turn a toy project into a real product?

Answer: You need to consider many aspects, such as:

1. Improve error handling, consider various exceptional situations
2. Add tests to ensure functional stability
3. Optimize performance to make the application run faster
4. Strengthen security to protect user data
5. Improve UI to make the application more usable
6. Write good documentation for easier maintenance and extension
7. Also consider SEO, monitoring, logging, etc.

This is a continuous improvement process - don't expect perfection in one step. Improve a little at a time, and gradually it will become a real product.



### How do I evaluate project quality?

Answer: Don't just focus on features - quality is equally important. A feature-complete but buggy project is not as good as a simple but stable and reliable one.

You can evaluate from these aspects:

- Functional completeness (are all requirements implemented)
- Code quality (is it clear and maintainable)
- Performance (load speed, response speed)
- Security (are there vulnerabilities)
- User experience (is it easy to use)
- Test coverage (are there sufficient tests)



### What if AI can't solve a problem?

Answer: First, definitely don't keep banging away at one AI - you can try a different AI model. Different models excel in different areas.

If you have programming fundamentals, it's best to check official documentation - documentation is the most authoritative resource.

Or search for solutions to similar problems, like in the GitHub Issues section - many problems have been encountered by others before, just copy their solution.

You can also seek help in communities or forums, like asking in [Programming Navigation](https://codefather.cn/); or consult experienced developers - sometimes one sentence can wake you up.

Remember, AI is a tool, not all-powerful - human wisdom is equally important.



### How do I manage project versions and code?

Answer: Use Git for version control and host code on GitHub.

- Commit after completing each feature, write clear commit messages
- If trying new features, create a new branch, merge after testing confirms no issues
- Regularly back up code to avoid data loss
- For team collaboration, establish branch strategies and code standards

Git is an essential programmer skill, absolutely worth spending time learning. But don't memorize Git commands by rote - AI can help you handle them.



### How do I handle project dependencies and package management?

Answer: Use npm or pnpm to manage dependencies, regularly update package versions.

Also pay attention to these points:

1. Check package security to avoid using vulnerable packages
2. If you encounter dependency conflicts, let AI help you solve them
3. Don't install too many unnecessary packages - each package increases project size and complexity
4. Regularly clean unused dependencies to keep the project tidy

If you're unsure which package to use, you can ask AI to recommend - it will give you several options and comparisons.



### How do I test AI-generated code?

Answer: For important projects, you can have AI help you write automated tests, like unit tests and integration tests.

But don't completely trust AI - you must manually test! Click through every feature and try various edge cases.

Testing not only discovers bugs but also helps you better understand code behavior. Don't feel testing wastes time - it saves you more debugging time. You can also have friends or invite users to help test - they often discover problems you didn't think of.



### How do I optimize AI-generated UI interfaces?

Answer: You can have AI reference excellent designs, like describing in text "interface style should reference Notion, clean and modern," or find screenshots of excellent websites to paste for AI to understand and reference.

If you have some programming foundation, or have UI component libraries you like, you can directly recommend them to AI. Like Ant Design, Material-UI, shadcn/ui - they provide ready-made beautiful components.

Remember, good UI isn't flashy - it's clear, consistent, and easy to use.



### How do I handle multi-person collaborative development?

Answer: Use Git branch management - everyone develops on their own branch, then merges to main branch when complete.

Additionally, several important points:

1. Establish code standards to maintain consistent code style. You can have AI help generate team collaboration documents, including development standards, Git workflows, etc.
2. Use Pull Requests for code review and learn from each other
3. Regularly sync code to avoid conflicts
4. Use project management tools (like Notion) to assign tasks
5. Maintain communication, discuss problems promptly when they arise



### How do I add a database to my project?

Answer: The simplest method is using BaaS services like Supabase or Firebase. They provide database, authentication, storage and other functions without needing to build servers yourself.

Just tell AI "Please integrate Supabase database" and it will help you generate the code.

For small projects, BaaS services are completely sufficient and worry-free.

If you need more control, you can use databases like PostgreSQL or MongoDB, but you'll need to deploy and manage them yourself.



### How do I handle user authentication and authorization?

Answer: Don't implement authentication systems from scratch - it's too easy to have security issues. I recommend using ready-made solutions like Supabase Auth, Firebase Auth, Auth0, NextAuth.js. These solutions provide complete authentication flows including email verification, password reset, and third-party login.

Just tell AI "Please implement user login and registration using NextAuth.js" and it will help you integrate.

For learning projects, you can implement simply, but for commercial projects, definitely use mature solutions.




## Vibe Coding Learning and Growth


### Can someone with zero foundation learn Vibe Coding?

Answer: Absolutely. Vibe Coding lowers the programming barrier - even with zero foundation you can get started. I suggest starting with no-code platforms (Bolt.new), first build a few small projects to build confidence. Then learn while doing - understand some basic programming concepts like variables, functions, conditionals, loops, etc. Don't try to learn deeply from the start - just being able to understand AI-generated code is enough. Gradually, you'll find yourself understanding more and more, even able to modify code yourself.



### How long does it take to learn Vibe Coding?

Answer: Getting started is fast - in less than 10 minutes you can build your first project. But to master it requires day-to-day practice. I suggest spending 1~2 hours practicing daily, first doing some small projects to gain experience, then trying commercial-grade products.

Remember, learning is a continuous process - don't rush for quick results. What matters isn't how fast you learn, but whether you can persist. A little progress every day, and looking back after a few months, you'll be amazed at your growth.



### What learning resources do you recommend?

Answer:

1. Official documentation is the best resource, like Cursor's documentation, Claude's documentation.
2. [Fish Skin's AI Navigation](https://ai.codefather.cn/) has collected a large number of AI tools and learning resources.
3. Bilibili and YouTube have many Vibe Coding video tutorials - I also frequently share in this area on my "Programmer Fish Skin" account.
4. GitHub has resource collections like awesome-vibe-coding
5. You can also join developer communities like [Programming Navigation](https://www.codefather.cn/) to exchange ideas and learn with others



### How do I improve my Vibe Coding skills?

Answer: Practice is the most important thing.

- Build various types of projects, from simple to complex
- Learn excellent prompts and conversation techniques - see how others use AI
- Understand AI-generated code, don't just copy and paste
- Summarize experience and lessons, record problems encountered and solutions
- Keep learning, follow new tools and technologies
- Try refactoring previous projects, improving them with newly learned techniques
- Teaching others is also a great way to learn - it deepens your understanding, output promotes input



### How do I balance AI assistance and self-learning?

Answer: Don't completely rely on AI, but don't completely reject it either. You can first have AI generate code, then understand and modify it yourself. When you encounter something you don't understand, think about it first, then ask AI.

If you're still in the introductory phase, you can periodically do some exercises without AI to consolidate fundamentals.

**Remember, AI is a tool, an accelerator, but cannot replace your thinking.**

Just as calculators can't replace mathematical thinking, AI can't replace programming thinking. Use AI to improve efficiency, use thinking to enhance ability.



### How do I maintain learning motivation?

Answer: Work on projects you're interested in, not just for the sake of learning.

You can:

- Set small goals and reward yourself after completing each one
- Learn with friends and encourage each other
- Share your work and get feedback and recognition
- Record your learning process and see your progress

Learning is a marathon, not a sprint - take it slow and enjoy the process. Most importantly, remember why you started learning, what you want to do, and who you want to become. Don't compare yourself to others, compare yourself to your past self.




## Vibe Coding Cost and Efficiency


### How do I control AI usage costs?

Answer: There are many techniques to save real money:

- Use cheaper models for simple tasks, expensive models only for complex tasks
- Take full advantage of free resources, like DeepSeek and Tongyi Qianwen's free quotas
- Optimize prompts - say it clearly the first time to reduce back-and-forth conversation
- Avoid having AI generate large amounts of unnecessary code
- Use caching features to reduce redundant computation

For the learning phase, free resources are completely sufficient. For commercial projects, the cost is worth it because AI can greatly improve efficiency, and the saved labor cost far exceeds the AI cost.



### How do I improve development efficiency?

Answer: There are many techniques to improve efficiency:

- Use keyboard shortcuts to reduce mouse operations
- Utilize Agent mode to let AI work automatically, reducing manual time investment
- Prepare prompt templates - directly apply them for common requirements
- Use code snippets to quickly insert common code
- Configure your development environment to reduce repetitive work
- Learn some basic knowledge to faster understand and modify AI-generated code

Most importantly, plan well - think clearly before starting to avoid rework. When completing Vibe Coding projects, true efficiency isn't speed, it's avoiding wrong turns.



### How do I avoid repetitive labor?

Answer: A programmer's advantage is being "lazy" - the key to avoiding repetitive labor is **accumulation and reuse**.

Specific approaches:

- Save commonly used prompts, configurations, and code snippets - directly copy when needed, or have AI reuse them
- Use template projects - create new projects based on templates rather than generating from scratch
- Record solved problems for direct reference next time
- Build your own knowledge base and accumulate experience



### How do I choose the right subscription plan?

Answer: For the learning phase, start with the free version and upgrade only when insufficient. For daily work or building commercial projects, Cursor Pro offers the best value. If you need heavy usage, consider API pay-per-use. If budget is limited, domestic model subscriptions are cheaper.

In short, don't subscribe to the most expensive plan from the start - try it out first and find what suits you best. Also don't reject payment - after all, tools are for improving efficiency, and if they save you time, the cost is worth it.



## In Conclusion

This article has summarized dozens of common questions, covering concept understanding, tool selection, usage tips, project development, learning growth, cost and efficiency, and more. These are all problems I've encountered in my own practice or that students frequently ask about in the [AI Programming Community](https://ai.codefather.cn/).

Of course, Vibe Coding is still developing rapidly, new problems will continue to appear, and new solutions will continue to emerge. I suggest you keep learning, follow community developments, and communicate with other developers - infinite progress!






## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
