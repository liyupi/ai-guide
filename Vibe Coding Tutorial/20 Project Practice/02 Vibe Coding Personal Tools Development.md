# Vibe Coding Personal Tools Development


Hello, I'm Fish Skin.

In the previous article, we learned the complete 5-step development process. Now, it's time to put this process to real use!

In this article, I'll take you through building 5 practical personal tool projects: personal portfolio website, todo app (advanced version), Markdown note app, Pomodoro timer, weather query app.

First, I need to explain that this tutorial section is primarily meant to guide you on the approach and project development process, with the goal of teaching everyone how to use Vibe Coding to develop projects. You need to practice hands-on yourself. If you need more complete Vibe Coding graphic and video tutorials, you can check out Fish Skin's original project practice section.

The projects below are carefully selected by me — highly practical, truly usable when completed, not toys. Moderate difficulty, suitable for beginners to practice, neither too hard nor too simple. Technically, they cover common scenarios like frontend, data storage, API calls, etc. After completing the basic version, you can continue adding new features. More importantly, these projects can all be added to your portfolio to showcase your abilities to others.

For each project, I'll provide a complete development guide, including requirement analysis, technology selection, development steps, and extension ideas. You can choose projects based on your interests — no need to complete them in order.



## I. Project Practice - Personal Portfolio Website

A personal portfolio website is the best way to showcase your abilities. Whether you're looking for a job, taking freelance work, or want to share your work on social media, a beautiful portfolio website will give you extra points. And this project itself is your first work that can be showcased in your portfolio — pretty cool, right?

This website should include several sections: personal introduction (name, avatar, bio, contact info), skills showcase (what technologies you know), project showcase (projects you've done, including screenshots, descriptions, links). The interface should have responsive design, displaying properly on both mobile and desktop.

For technology selection, we use React + TypeScript + Vite as the frontend framework, Tailwind CSS for styling, and finally deploy to Vercel for launch. This tech stack is very modern and currently the most popular frontend development approach.

![](https://pic.yupi.icu/1/demoweb1.png)



### Development Steps

1) Requirements Research

Before developing any project, do requirements research first. You can look at what others' portfolio websites are like, for example search "developer portfolio examples" online for inspiration. Record design styles and features you like — these can serve as your reference.

2) Write PRD Document

After getting inspiration, write the PRD document. Create a `PRD.md` file to clearly define what content you want to showcase. Here's a reference example:

```markdown
# Personal Portfolio Website PRD

## Core Features
1. Home: Large title + bio + avatar
2. About Me: Detailed introduction + skills list
3. Project Showcase: Project card list, each card contains project name, screenshot, brief description, tech stack, project link
4. Contact: Email, GitHub, social media links

## Design Requirements
- Simple and modern design style
- Dark theme
- Smooth scroll animations
- Mobile responsive
```

This document doesn't need to be very complex — just clearly state core features and design requirements.

3) Write Technical Design Document

Next, write the technical design document `TECH_DESIGN.md`. Define the specific technical approach here:

```markdown
# Technical Design

## Tech Stack
- React + TypeScript + Vite
- Tailwind CSS
- React Router (if multi-page needed)
- Framer Motion (animation effects)

## Project Structure
src/
  components/
    Header.tsx
    Hero.tsx
    About.tsx
    Projects.tsx
    Contact.tsx
    Footer.tsx
  data/
    projects.ts
    skills.ts
  App.tsx
  main.tsx

## Data Management
- Project data and skills data stored in TypeScript files
- Use arrays for easy future addition and modification
```

The purpose of this document is to let AI know what technologies to use and what the project structure looks like.

4) Write AGENTS.md File

Then create the `AGENTS.md` file to tell AI development standards:

```markdown
# Personal Portfolio Website Development Instructions

## Project Overview
Personal portfolio website developed using React + TypeScript + Tailwind CSS.

## Development Standards
- Use functional components + Hooks
- Use Tailwind CSS for styling
- Components should be reusable
- Code should have comments

## Design Requirements
- Dark theme (background #0a0a0a, text #ffffff)
- Use gradients as accent colors
- Add smooth scroll animations
- Ensure mobile responsiveness

## Precautions
- Keep design simple, avoid over-engineering
- Performance optimization: use lazy loading for images
- Ensure all links are clickable
```

This file is development standards for AI, telling it how to write code and what design style to use.

5) Start Development

With these three documents, you can start development. Open Cursor or other AI code editor and start talking with AI.

The first prompt is to initialize the project:

```
Please according to PRD.md, TECH_DESIGN.md and AGENTS.md requirements,
initialize a React + TypeScript + Vite project and install Tailwind CSS.
```

This prompt is simple but contains all necessary information. AI will read these three documents, then create the project structure according to requirements, install dependencies, and configure Tailwind CSS.

Then implement each component step by step. For example, create the Hero component:

```
Create Hero component including large title, bio and avatar. Use Tailwind CSS to implement dark theme and gradient effects.
```

This prompt tells AI what component to create, what content to include, and what technology to use. AI will generate complete component code.

Next, create the Projects component:

```
Create Projects component to display project list. Each project card includes screenshot, title, description, and tech stack tags.
```

Just like this, step by step, complete the entire website. After completing each component, preview it in the browser to ensure it meets expectations.

6) Deploy and Launch

After development is complete, you can deploy and launch. The deployment process is simple:

- Push code to GitHub
- Log in to Vercel, import GitHub repository
- Click deploy, wait for completion
- Get your website link

Vercel will automatically detect your project type and configure build commands — very smart. After deployment is complete, you'll have an accessible website link that you can share with others.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add blog functionality to write articles sharing your learning experience; add dark/light theme switching so users can choose their preferred theme; support multiple languages to attract international users; add visit statistics to understand website traffic; even add a guestbook feature so visitors can leave messages for you.



## II. Project Practice - Todo App (Advanced Version)

After completing the portfolio website, let's make a more complex project. In the quick start section, we made a simple todo app with only basic add and delete features. Now, let's make a more powerful version and learn how to handle more complex business logic.

This advanced version has much richer features. When adding a todo item, besides the title, you can also set description, due date, priority, and category. When viewing the list, it supports filtering by category, priority, and status, plus a search function to quickly find specific todo items. Of course, it also supports editing and deleting. Data is saved in LocalStorage so it won't be lost when refreshing the page. There's also a statistics feature showing completion rate, number of pending items, etc.

For technology selection, frontend uses React + TypeScript + Vite, state management uses Zustand (a lightweight state management library much simpler than Redux), styling uses Tailwind CSS, date handling uses date-fns, and data storage uses LocalStorage.

![](https://pic.yupi.icu/1/demoweb2.png)



### Development Steps

1) Define Data Model

The first step in development is defining the data model. You need to clarify what fields a todo item contains: id (unique identifier), title (title), description (description), category (category), priority (priority: low, medium, high), dueDate (due date), completed (whether completed), createdAt (creation time). Define these fields clearly, and subsequent development will go very smoothly.

2) Develop by Feature Module

Then develop by feature modules. The recommended order is: first implement the data storage layer, encapsulating LocalStorage read/write operations; then implement state management, using Zustand to create a global store; then implement the add feature; next implement list display and filtering; finally implement search and statistics. This progressive approach — test after completing each module to ensure it works properly.

When talking with AI, you can say:

```
Create Todo data model and LocalStorage utility functions.
```

AI will help you define the data structure and encapsulate storage operations. Although this prompt is simple, AI knows what to do because it will reference your PRD and technical design documents.

Then say:

```
Use Zustand to create global state management, including add, delete, update, filter and other methods.
```

AI will create a complete store with all needed methods. Zustand is a very lightweight state management library, much simpler than Redux, but powerful enough.

Next say:

```
Create AddTodo component including form input and validation.
```

AI will implement the add feature's interface and logic, including input boxes, dropdowns, date pickers, etc. After completing each feature, test it to ensure it works properly.



### Key Technical Points

This project has several key technical points to note. First is state management — because there are many features, using Zustand to manage global state will be much more convenient. You can have AI help you create a store with add, delete, update, filter and other methods.

The filter feature should support multi-condition filtering, like filtering by both category and priority at the same time. The search feature should support fuzzy search, finding keywords in titles and descriptions. These logic implementations can all be done by AI — you just need to tell it the specific requirements.



### Extension Ideas

After completing the basic version, you can continue to extend. For example, add a tags feature so todo items can have multiple tags; support subtasks so a large task can be broken down into multiple small tasks; add a reminder feature to automatically notify before due dates; support exporting data to CSV; even use Firebase to implement cloud sync.



## III. Project Practice - Markdown Note App

After mastering state management and data filtering, let's learn how to handle text editing and real-time preview. Markdown is the most commonly used document format for programmers. Building a Markdown note app lets you learn how to handle text editing, real-time preview, and other features.

This project implements a complete Markdown note application. Users can create notes and enter title and content. The interface uses a split-pane layout — left side is the editor, right side shows real-time preview of rendered results. The left side also displays a note list supporting search. Data is saved in LocalStorage, and notes can be deleted. Code blocks should have syntax highlighting to look more professional.

For technology selection, frontend uses React + TypeScript + Vite, Markdown parsing uses react-markdown, code highlighting uses react-syntax-highlighter, styling uses Tailwind CSS, and data storage uses LocalStorage.

![](https://pic.yupi.icu/1/demoweb3.png)



### Development Steps

1) Implement Basic Layout

The first step in development is implementing the basic layout — creating a split-pane layout with the editor on the left and preview on the right. This layout is easily implemented using Tailwind CSS's Flex or Grid.

You can tell AI this:

```
Create a split-pane layout with Markdown editor (large text box) on the left and preview area on the right. Use Tailwind CSS for responsive layout.
```

AI will create a beautiful split layout — side-by-side on desktop, automatically stacking vertically on mobile.

2) Integrate Markdown Parsing

Then integrate Markdown parsing. Using the react-markdown library, you can easily convert Markdown text to HTML. You just need to pass the text to this component and it will automatically render.

Tell AI:

```
Use react-markdown to convert Markdown text to HTML and display rendered results in the preview area.
```

This prompt is very concise, but AI knows what to do. It will install the react-markdown library, import the component, and then use it in the preview area.

3) Implement Real-Time Preview

Next implement real-time preview. The key to this feature is listening to editor input changes and updating the preview area in real-time. When the user edits on the left, the right side should synchronously display the rendered results.

Tell AI:

```
Listen to editor input changes and update preview area in real-time. When user edits on the left, the right side synchronously displays Markdown rendered results.
```

This feature is easily implemented using React's state management. AI will store the editor content in state, then pass it to the preview component — every time content changes, the preview automatically updates.

4) Add Code Highlighting

Code highlighting is also important, making code blocks look more professional. Tell AI:

```
Configure react-syntax-highlighter so code blocks support syntax highlighting. Support multiple programming languages like JavaScript, Python, Java, etc.
```

AI will configure react-syntax-highlighter — when there are code blocks in Markdown, they'll be rendered with syntax highlighting, different syntax elements displaying in different colors.

5) Add Note Management Features

Finally add note management features. Tell AI:

```
Implement note management features:
- Add note list on left side showing all note titles
- Clicking a note switches to that note
- Support creating new notes and deleting notes
- Support searching notes (by title)
- Data saved in LocalStorage
```

This prompt includes all feature requirements, and AI will implement all features at once.



### Key Technical Points

The key to this project is implementing Markdown real-time preview. When users edit on the left, the right side should display rendered results in real-time. This feature is easily implemented using the react-markdown library.

Code highlighting is also important — you can have AI help you configure react-syntax-highlighter to support syntax highlighting for multiple programming languages. For better user experience, you can have AI add some optimizations, like Tab key inserting spaces instead of switching focus, supporting Ctrl+B for bold and other shortcuts, auto-saving drafts, etc.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, support image upload so notes can insert images; add table of contents navigation to automatically generate article outline; support exporting to PDF for easy sharing; add theme switching with multiple editor themes; support multiple Markdown styles like GitHub style, standard style, etc.



## IV. Project Practice - Pomodoro Timer

The previous projects were all about data display and management. Now let's make a project involving timers and notifications. The Pomodoro Technique is a popular time management method. Building a Pomodoro app lets you learn how to handle timers, notifications, and other features.

The Pomodoro Technique works by focusing for 25 minutes, then resting for 5 minutes, cycling like this. This app needs to implement a countdown feature supporting start, pause, and reset. Users can customize the work and rest durations. When time is up, it should send a notification reminder and can play a notification sound. There's also a statistics feature recording the number of completed Pomodoros to help users understand their work efficiency.

For technology selection, frontend uses React + TypeScript + Vite, styling uses Tailwind CSS, notifications use the browser's built-in Notification API, and data storage uses LocalStorage.

![](https://pic.yupi.icu/1/demoweb4.png)



### Development Steps

1) Implement Countdown Logic

The core of development is implementing countdown logic. Tell AI:

```
Implement Pomodoro countdown feature:
- Default 25 minutes work, 5 minutes rest
- Support start, pause, reset
- Display time in MM:SS format
- Trigger reminder when countdown ends
```

This prompt clearly states what features to implement. AI will use JavaScript's setInterval to implement the countdown, subtracting 1 each second, and triggering a reminder when it reaches 0.

2) Implement Notification Feature

Then implement the notification feature. The browser's Notification API can send system notifications, but needs to request user permission first. Tell AI:

```
Implement browser notification feature:
- Request notification permission when page loads
- Send notification when countdown ends
- Notification title is "Pomodoro", content is "Time's up, take a break!"
```

This prompt states when notifications are triggered and their content. AI will first check if the browser supports notifications, then request permission, and finally send a notification when time is up.

3) Add Sound Effects

You can also add sound effects. Play a notification sound when time is up so users know even if they're not looking at the screen. Tell AI:

```
Add notification sound feature:
- Prepare a notification sound file (place in public directory)
- Play notification sound when countdown ends
```

AI will use the Audio object to play the audio file.

4) Add Statistics Feature

Finally add the statistics feature. Tell AI:

```
Implement statistics feature:
- Record number of completed Pomodoros
- Display today's completed count, this week's completed count
- Data saved in LocalStorage
```

This way users can see their work efficiency and feel more accomplished.



### Key Technical Points

The core of this project is countdown logic and notification functionality. The countdown must be accurate, subtracting 1 each second with no error. The notification feature needs to request user permission first — if the user refuses permission, give a friendly prompt.

For better user experience, you can update the page title during timing so users can see the remaining time even when switched to other tabs. You can also add a notification sound that plays when time is up.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add a long break feature — rest for 15 minutes after 4 Pomodoros; record daily Pomodoro counts and generate statistical charts; add a task list to associate Pomodoros with specific tasks; data visualization using charts to show work efficiency; even support background music to make working more atmospheric.



## V. Project Practice - Weather Query App

Finally, let's make our first project that needs to call an external API. This project lets you learn how to interact with backend services and handle asynchronous requests and errors.

This project implements weather query functionality. Users enter a city name to query current weather, displaying temperature, weather conditions, humidity, wind speed, and other information. It also displays weather forecasts for the next few days. It can automatically get the user's location and display weather. Frequently used cities can be bookmarked for easy future queries.

![](https://pic.yupi.icu/1/demoweb5.png)

For technology selection, frontend uses React + TypeScript + Vite, styling uses Tailwind CSS, weather data is obtained through [OpenWeatherMap API](https://openweathermap.org/api) (free), and bookmarked cities are saved in LocalStorage.

![](https://pic.yupi.icu/1/image-20260112141920735.png)



### Development Steps

1) Register API

The first step in development is registering for the API. Go to the OpenWeatherMap website to register an account and get a free API Key. Registration is simple — just fill in basic information. The free version has certain call limits but is completely sufficient for learning and personal use.

2) Encapsulate API Requests

Then encapsulate API requests. Create an API utility file that encapsulates all API calls here. Tell AI:

```
Create API utility file to encapsulate weather API calls:
- Define API base URL and API Key (read from environment variables)
- Create getCurrentWeather function to get current weather
- Create getForecast function to get future weather forecast
- Support querying by city name or coordinates
- Must have error handling
```

This prompt states what features to encapsulate, and AI will create a complete API utility file.

3) Implement Search Feature

Next implement the search feature. Tell AI:

```
Implement weather query feature:
- User enters city name and clicks search
- Call API to get weather data
- Display temperature, weather conditions, humidity, wind speed and other information
- Show loading animation during query
- Show friendly prompt on query failure (like "City not found")
```

This prompt includes both feature requirements and user experience requirements. AI will implement a complete search feature including loading state and error handling.

4) Implement Location

You can also implement the location feature. Tell AI:

```
Implement automatic location feature:
- Use browser's Geolocation API to get user location
- Query weather based on coordinates
- Show prompt if user refuses location permission
```

This way users don't need to manually enter city names — more convenient.

5) Add Bookmark Feature

Finally add the bookmark feature. Tell AI:

```
Implement city bookmark feature:
- Queried cities can be bookmarked
- Bookmark list saved in LocalStorage
- Clicking a bookmarked city allows quick query
- Support deleting bookmarks
```

This way users can quickly check weather for frequently used cities.



### Key Technical Points

The key to this project is handling API calls properly. API requests can fail — you need good error handling. For example, city not found, invalid API Key, network errors, etc. — all should show friendly prompts. During requests, show a loading animation so users know a query is in progress.

Also pay attention to API Key security. Don't write it directly in code — use environment variables. Create a `.env.local` file and put the API Key in it, then read it through environment variables in code. Remember to add `.env.local` to `.gitignore` and don't commit it to Git to avoid leaking.



### Extension Ideas

After completing the basic version, you can continue to extend features. For example, add weather icons and animations to make the interface more lively; display air quality index to focus on health; support multi-city comparison to view multiple cities' weather at once; add weather alerts to timely warn of severe weather; even query historical weather to analyze weather trends.



## In Conclusion

Through these 5 projects, you've learned core Web development skills: component development, state management, data persistence, API calls, user interaction, etc. From a simple portfolio website to a complex todo app, from text editor to timer, to calling external APIs — each project has let you master new skills.

If you encounter difficulties during development, or want to learn more development techniques and best practices, you can refer to the experience & techniques section of this tutorial, which has more detailed explanations.

After mastering personal tool development, in the next article, I'll take you through building cooler AI applications. Let's explore the infinite possibilities of AI together.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
