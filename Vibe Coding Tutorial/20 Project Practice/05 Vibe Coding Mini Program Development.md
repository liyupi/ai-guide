# Vibe Coding Mini Program Development

> Building WeChat Mini Programs from development to launch


Hello, I'm Programmer Fish Skin.

In previous articles, we built web applications that can be accessed in browsers. Now, let's learn how to develop WeChat Mini Programs, so your applications can run within WeChat.

WeChat Mini Programs are applications that don't require downloading or installation—they run within WeChat as a super app and have a massive user base. For individual developers, Mini Programs are an excellent showcase platform with low development costs and easy user reach.

In this article, I'll walk you through building 2 practical Mini Programs: an expense tracker and a habit checker. I'll also explain the complete Mini Program development and launch process in detail, so you can independently complete the entire process from development to launch.

It should be noted that this tutorial focuses more on providing guidance on approach and project development workflow. The goal is to guide everyone in learning how to use Vibe Coding for project development, and you'll need to practice on your own. If you need more complete Vibe Coding graphic and video tutorials, check out Fish Skin's original project practice section.



## I. Mini Program Development Basics

Before starting the projects, let's understand some basics of Mini Program development.

Mini Programs are lightweight applications that don't require download or installation—use them and go. WeChat Mini Program is the most popular Mini Program platform, along with Alipay Mini Program, Douyin Mini Program, etc. The advantages of Mini Programs include: low development cost (compared to native apps), easy user reach (large WeChat user base), relatively relaxed review process, and rapid iteration capability.

What's the difference between Mini Programs and web applications?

Simply put, Mini Programs run within the WeChat environment and have some special APIs and limitations. For example, Mini Programs can call WeChat's payment, sharing, scanning and other functions, but cannot directly access external links. From a development perspective, Mini Programs use Vue-like syntax, with their own component system and lifecycle. **If you know web development, learning Mini Programs will be very fast.**

WeChat Mini Program technology stack includes: WXML (similar to HTML), WXSS (similar to CSS), and JavaScript. You can use native development, or use frameworks (like Taro, uni-app) for cross-platform Mini Program development. For Vibe Coding, I recommend native development because AI has better support for native syntax and generates higher quality code.

To develop Mini Programs, you need to prepare a few things:

- WeChat developer account (free registration)
- WeChat Developer Tools (official IDE)
- A project idea

![WeChat Developer Tools](https://pic.yupi.icu/1/image-20260112150540207.png)

Registering an account is simple—go to WeChat Public Platform to register a Mini Program account, choose individual type. Downloading the developer tools is also simple—go to the official website to download the version for your system.

Developing Mini Programs with Vibe Coding is similar to developing web applications, just with slightly different syntax. You need to tell AI you're developing a WeChat Mini Program, and it will generate code that conforms to Mini Program specifications. For example, you can say: "Please create an expense tracking page using WeChat Mini Program native syntax, including amount input, category selection, and note input." AI will generate WXML, WXSS, and JS files.

💡 If you want to systematically learn Mini Program development, you can read Fish Skin's [free comprehensive Mini Program learning roadmap](https://www.codefather.cn/course/1789189862986850306/section/1789190355448471554) on Programming Navigation.



## II. Project Practice - Expense Tracker Mini Program

Expense tracking is a very practical function, and many people have the need to track expenses. Building an expense tracker Mini Program allows you to learn the basic Mini Program development process, including data storage, page navigation, component usage, etc.

This expense tracker Mini Program needs to implement basic expense tracking functionality. Users can add income and expense records, including amount, type (income/expense), category (food, transportation, salary, etc.), notes, and date. The homepage displays a record list and statistics (this month's income, expenses, balance). Support filtering records by date. Data is stored locally using WeChat's local storage API.

![](https://pic.yupi.icu/1/demoweb13.png)

Using WeChat Mini Program native development without any frameworks. Data storage uses `wx.setStorageSync` and `wx.getStorageSync`.



### Development Steps

1) First step is to register a Mini Program account. Go to [WeChat Public Platform](https://mp.weixin.qq.com/) to register a Mini Program account. Choose individual type, fill in basic information, complete registration. After registration, you'll get an AppID which will be needed during development.

2) Second step is to download developer tools. Go to [WeChat Open Documentation](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html) to download WeChat Developer Tools, install and log in with WeChat scan.

3) Third step is to create a project. Open Developer Tools, click New Project, fill in project name, select project directory, enter AppID, choose not to use cloud services. Click OK, and a Mini Program project template will be automatically generated.

4) Fourth step is to understand the project structure. The basic structure of a Mini Program project includes:

- pages directory: stores pages, each page has four files: wxml (page structure), wxss (page styles), js (page logic), json (page configuration)
- utils directory: stores utility functions
- app.js: Mini Program logic
- app.json: Mini Program configuration
- app.wxss: global styles

5) Now you can use Cursor to open the project directory and start developing with AI.

First design the data structure:

```
I want to develop an expense tracker Mini Program, please help me design the data structure.

Information to store:
- Amount
- Type (income/expense)
- Category (food, transportation, shopping, salary, etc.)
- Notes
- Date

Please provide the JavaScript object structure.
```

AI will help you design a reasonable data structure, including the type and description of each field.

Then create the homepage:

```
Please create the homepage (pages/index/index) using WeChat Mini Program native syntax:

Top displays statistics cards:
- This month's income (green)
- This month's expenses (red)
- This month's balance (blue)

Middle displays record list:
- Grouped by date
- Each record shows: category icon, category name, notes, amount
- Income shows green, expenses show red

Bottom has a large "+" button, click to navigate to add page.

Use Flex layout, make the interface beautiful.
```

This prompt describes the layout and styling of the homepage in detail. AI will generate complete WXML, WXSS, and JS code.

Next implement data storage:

```
Create utils/storage.js utility file to encapsulate data storage operations:

1. saveRecord(record): save a record
2. getRecords(): get all records
3. deleteRecord(id): delete a record
4. getMonthRecords(year, month): get records for specified month

Use wx.setStorageSync and wx.getStorageSync to store data.
Records must have unique ID (can use timestamp).
```

This encapsulates the data storage logic, making it convenient to use later.

Then create the add page:

```
Create add record page (pages/add/add):

Top has two tabs: income, expense

Amount input area:
- Large amount input field
- Display "¥" symbol

Category selection area:
- Grid layout displays category icons
- Income categories: salary, bonus, investment, other
- Expense categories: food, transportation, shopping, entertainment, medical, other
- Selected category highlighted

Note input:
- Single-line text input

Date selection:
- Default today
- Click to select date

Bottom save button:
- Click to save record and return to homepage
```

Next implement statistics functionality:

```
Implement statistics functionality on homepage:

1. Calculate this month's total income: filter this month's income records, sum
2. Calculate this month's total expenses: filter this month's expense records, sum
3. Calculate this month's balance: income - expenses

Refresh statistics data when page loads and when returning.
```

Finally implement the record list:

```
Implement record list on homepage:

1. Get all records, sort by date descending
2. Group by date (today, yesterday, earlier)
3. Each record shows category icon, name, notes, amount
4. Long press record to delete

Implement pull-to-refresh functionality.
```



### Development Tips

When developing Mini Programs, several tips can improve efficiency. First, make good use of WeChat Developer Tools' debugging functionality. You can preview effects in the simulator, or preview on a real device. Real device preview requires scanning with WeChat, showing the actual running effect.

Second, Mini Program data storage is synchronous, using `wx.setStorageSync` and `wx.getStorageSync`. If data volume is large, recommend using async versions `wx.setStorage` and `wx.getStorage` to avoid blocking the main thread.

Additionally, Mini Program page navigation has several methods: `wx.navigateTo` (keep current page, can return), `wx.redirectTo` (close current page, cannot return), `wx.switchTab` (jump to tabBar page), `wx.navigateBack` (return to previous page). Choose the appropriate method based on the scenario.

Finally, Mini Programs have some limitations, such as package size cannot exceed 2MB (after subpackaging, each package cannot exceed 2MB), so pay attention to controlling image size and code volume. You can use image compression tools to compress images, and use code subpackaging to split code.



### Extension Ideas

After completing the basic version, you can continue to extend functionality. For example: add budget setting to set monthly budget and alert when over budget; add chart display to show income/expense trends with charts; support category management so users can customize categories; add bill export to export as Excel file; support multiple ledgers like work ledger, life ledger, etc.; integrate cloud sync using WeChat Cloud Development for multi-device sync.



## III. Project Practice - Habit Checker Mini Program

After completing the expense tracker Mini Program, let's build a project involving calendar and data visualization. Habit checking is a great habit-building tool—many people use check-ins to persist in learning, exercise, early rising, etc. Building a habit checker Mini Program allows you to learn Mini Program calendar components, data visualization, and other features.

This habit checker Mini Program needs to implement habit checking functionality. Users can create check-in projects (like daily study, daily exercise), set check-in goals (consecutive check-in days). Can check in once per day, after checking in displays check-in success. Homepage displays all check-in projects and check-in status. Calendar view shows check-in history, check-in dates marked in green. Statistics displays total check-in days, consecutive check-in days, completion rate, etc.

![](https://pic.yupi.icu/1/demoweb14.png)

Using WeChat Mini Program native development, data storage uses local storage. Calendar component can use third-party component libraries (like Vant Weapp) or implement yourself.



### Development Steps

1) First step of development is designing the data structure. Tell AI:

```
I want to develop a habit checker Mini Program, please help me design the data structure.

Check-in projects:
- id
- name (project name, like "Daily Study")
- target (target days)
- created_at (creation time)

Check-in records:
- id
- project_id (associated project)
- date (check-in date, format YYYY-MM-DD)
- note (check-in note, optional)
- created_at (check-in time)

Please provide data structure and storage solution.
```

AI will help you design a reasonable data structure and explain how to store it locally.

2) Create project list page

Tell AI:

```
Create homepage (pages/index/index) to display check-in project list:

Each project card displays:
- Project name
- Whether checked in today (green checkmark if checked, gray circle if not)
- Consecutive check-in days
- Total check-in days
- Progress bar (checked days / target days)

Bottom has "Add Project" button.

Click project card to enter project detail page.
Click check-in button to check in.
```

This prompt describes the layout and interaction of the homepage. AI will generate complete page code.

3) Implement check-in functionality

Tell AI:

```
Implement check-in functionality:

1. Check if already checked in today
2. If not checked in, create check-in record
3. Save to local storage
4. Display check-in success message
5. Refresh page data

Can add note when checking in (optional).
```

Check-in functionality must prevent duplicate check-ins, so first check if already checked in today.

4) Create project detail page

Tell AI:

```
Create project detail page (pages/detail/detail):

Top displays project information:
- Project name
- Target days
- Checked days
- Consecutive check-in days

Middle displays calendar:
- Display current month
- Check-in dates marked with green background
- Today marked with blue border
- Can switch months

Bottom displays check-in record list:
- Display by date descending
- Show date, note

Top right has delete project button.
```

5) Implement statistics functionality

Tell AI:

```
Implement statistics functionality:

1. Total check-in days: all check-in records for this project
2. Consecutive check-in days: count consecutive days from today backward
3. Completion rate: checked days / target days
4. Longest consecutive check-in: longest consecutive check-in streak in history

Display these statistics on project detail page.
```

Calculating consecutive check-in days is relatively complex—need to traverse backward from today, checking each day for a check-in record until finding a date without a check-in. AI will help you implement this algorithm.

6) Implement calendar component

Tell AI:

```
Implement calendar component:

1. Display all dates of current month
2. Check-in dates marked with green background
3. Today marked with blue border
4. Can switch to previous/next month
5. Click date to view that day's check-in note

Use Grid layout, 7 dates per row (Sunday to Saturday).
```

Calendar component implementation is relatively complex, but AI can help you handle it. If you find implementing it yourself too troublesome, you can also use third-party component libraries like Vant Weapp.



### Development Tips

When developing a habit checker Mini Program, several tips need attention. First is date handling—JavaScript date handling is relatively complex, you can ask AI to help encapsulate some utility functions like getting days in month, judging if it's today, calculating days difference between two dates, etc.

Second is calculating consecutive check-in days. Need to traverse backward from today, checking each day for a check-in record until finding a date without a check-in. You can ask AI to help implement this algorithm—it will consider various edge cases.

Additionally, calendar component implementation is relatively complex—if you find implementing it yourself too troublesome, you can use third-party component libraries. Vant Weapp is an excellent Mini Program UI component library that provides a calendar component. You can ask AI to help integrate Vant Weapp and use its provided calendar component.

Finally, check-in data may grow more and more, so pay attention to performance optimization. You can load only the most recent 3 months of data, load earlier data on demand to avoid loading too much data at once causing page lag.



### Extension Ideas

After completing the basic version, you can continue to extend functionality. For example: add check-in reminders to remind users at a set time daily; implement check-in sharing to generate check-in poster to share to Moments; add check-in leaderboard to compete with friends on who persists longer; implement check-in rewards where consecutive check-ins earn badges; support data export to export check-in records; integrate cloud sync using WeChat Cloud Development for multi-device sync.



## IV. Complete Mini Program Launch Process

After development is complete, how do you launch a Mini Program? Here's a detailed explanation of the Mini Program launch process.

1) Complete Mini Program Information

On WeChat Public Platform, complete the Mini Program's basic information: Mini Program name, description, avatar, category (choose appropriate category). Individual type Mini Programs have some limitations, such as cannot use payment functionality, cannot use certain categories. If you need these features, you need to register an enterprise type.

2) Configure Server Domain

If the Mini Program needs to call backend APIs, you need to configure server domain on WeChat Public Platform. Only configured domains can be accessed in the Mini Program. Note, the domain must be HTTPS and needs an SSL certificate. For local development, you can check "Do not verify legal domains" in Developer Tools.

3) Upload Code

In WeChat Developer Tools, click the "Upload" button in the top right, fill in version number and project notes, click upload. After uploading, the code is submitted to WeChat servers.

4) Submit for Review

On WeChat Public Platform, enter "Version Management" to see the version just uploaded. Click "Submit for Review", fill in review information. Review information includes: test account (if login required), test instructions (tell reviewers how to test), privacy-related instructions, etc. After submission, wait for review. Review time is stated as 1-7 days, generally passes in 1-2 days.

5) Launch

After review approval, you'll receive a notification. On WeChat Public Platform, click the "Launch" button, and the Mini Program is officially live. After launch, users can access your Mini Program through search, scanning, sharing, etc.

6) Version Update

To update the Mini Program, repeat the above process: upload code → submit for review → launch. You can use "Phased Release" feature to first release to some users, then full release after testing shows no issues.

![](https://pic.yupi.icu/1/weapp-workflow%E5%A4%A7.jpeg)



### Common Review Issues

Mini Program review may encounter some problems—here are a few common ones.

1) Incomplete functionality. Reviewers find features cannot be used normally, such as clicking buttons with no response, page display errors, etc. Ensure all functions work normally—test completely yourself before submission.

Second is category mismatch. Mini Program functionality doesn't match the selected category. For example, you built a tool-type Mini Program but chose social category. Choose appropriate category—if unsure, you can consult WeChat customer service.

Missing required instructions. For example, Mini Program needs to get user location but doesn't explain the purpose. Clearly explain in privacy policy why these permissions are needed and how the data will be used.

4) Content violations. Mini Program content violates WeChat's regulations, such as containing inappropriate content. Carefully read WeChat Mini Program operation guidelines to ensure content compliance.

If review doesn't pass, you'll receive the rejection reason. Modify based on the reason and resubmit for review.

**Don't be discouraged—many Mini Programs get rejected the first time, this is normal.**



## V. My Experience Launching "Learning Hero" Mini Program

Finally, I want to share my real experience launching "Learning Hero" Mini Program, hoping to give you some inspiration.

"Learning Hero" is an AI Q&A guided learning Mini Program where users can input topics they want to learn, and AI automatically generates related knowledge Q&A cards, guiding users to master knowledge more easily and happily through gamified Q&A.

![](https://pic.yupi.icu/1/%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E6%25BC%2594%25E7%25A4%25BA%25E6%258B%25BE%25E5%259B%25BE.png)

The development process was actually very fast—with AI programming tools, I basically completed a Mini Program with complete frontend, backend, and AI capabilities in 1 day. But would you believe I spent nearly 2 months getting this Mini Program officially launched?!

In the past, I wouldn't have believed this myself—I remember launching Mini Programs quickly in college, looks like times have really changed.



### Complete Launch Process

1) Mini Program Filing

There used to be no such step, but since September 1, 2023, all newly developed WeChat Mini Programs must complete filing before going live.

Filing operation is free—mainly just filling in some individual/enterprise information in the backend. But review cycle is approximately 2-22 working days (including MIIT review). I submitted for filing before National Day holiday, it passed after 12 days; if not for holiday, might have been faster.

2) Mini Program Category Application

Because my Mini Program uses AI large model for Q&A functionality, I needed to add "Deep Synthesis - AI Q&A Category", otherwise couldn't pass code release review.

![](https://pic.yupi.icu/1/image-20251203212944981.png)

So I followed the modification guide to add the category, but it turns out adding AI-related categories requires qualification documents! Because I'm using someone else's large model, I need the technology entity's "Internet Information Service Algorithm Filing" and "Cooperation Agreement between Mini Program Entity and Technology Entity."

![](https://pic.yupi.icu/1/5b7bf1460d71ff74477082606e6e7cf8.png)

What? Still need a cooperation agreement?! At this step I estimate a large wave of beginners will be discouraged—I also had a headache when I first saw this.

![](https://pic.yupi.icu/1/image-20251203215116730.png)

But don't panic—just go directly to the corresponding staff for whichever AI large model service you're using. For example, I'm using Alibaba Cloud's large model, so I went directly to their official website to contact customer service, their technical support responded quickly and was very enthusiastic. You just need to clearly describe your requirements, and they'll help handle it.

![](https://pic.yupi.icu/1/image-20251203195218556.png)

It took about 10 days to smoothly get the category application materials, then just submit the application.

3) Code Release Review

Feels like Mini Program review is getting stricter and stricter—especially for newly created Mini Programs, it's easy to get rejected for unexpected reasons.

Like the situation I encountered—a certain button in the Mini Program didn't respond after clicking, so it was rejected.

![](https://pic.yupi.icu/1/%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E5%25AE%25A1%25E6%25A0%25B8-%25E4%25B8%258D%25E9%2580%259A%25E8%25BF%2587%25E7%259A%2584%25E5%258E%259F%25E5%259B%25A0.png)

I'm not taking the blame for this—who let AI be lazy?!

So I had a teammate help add a click popup, then resubmitted for review.

![](https://pic.yupi.icu/1/%E5%B0%8F%E7%A8%8B%E5%BA%8F%E5%AE%A1%E6%A0%B8-%E8%A1%A5%E4%BA%86%E4%B8%AA%E5%85%B3%E4%BA%8E%E6%88%91%E4%BB%AC%E7%9A%84%E4%BF%A1%E6%81%AF.png)

After about 2-3 days, code review finally passed.

4) However, because my Mini Program also involves "social" category, it needed to enter step four: Mini Program reporting.

![](https://pic.yupi.icu/1/image-20251203214139938.png)

When I saw this 7 days * 24h review duration, the chicken leg I was chewing on suddenly became tasteless...

Fortunately, after 7 days, my Mini Program was finally launched—it really wasn't easy!

Let's review the complete process:

![](https://pic.yupi.icu/1/image-20251203195031382.png)



### Experience Summary

Although this Mini Program launch took me nearly 2 months, some of that idle time was actually me not seeing notifications in time. But even considering only the required processes, it takes about 1 month.

If you just want to build a simple tool Mini Program that doesn't involve AI features and categories requiring reporting (like social, finance, medical, etc.), you should save considerable time.

![](https://pic.yupi.icu/1/0.png)

However, I estimate many students now have the idea of using AI to build a "Mini Program with AI features," so I still recommend:

1. Apply for Mini Program categories early: if involving AI features, prepare qualification materials as early as possible
2. Build minimum viable version first: make a Demo to pass review and complete the launch/release process once
3. Plan time accordingly: development may take only a few days, but launch process may take weeks or even months
4. Test thoroughly before review: ensure all functions work normally to avoid rejection for minor issues
5. Provide detailed test process: provide test account and detailed test instructions



## In Conclusion

Through these 2 Mini Program projects, you've learned the basic Mini Program development process. More importantly, you've learned how to launch a project so real users can use it.

Mini Program development has some special characteristics compared to web development, but the core approach is the same. With the Vibe Coding approach, you can quickly develop fully functional Mini Programs. If you want to learn more Mini Program development tips and best practices, refer to the Experience & Techniques section of this tutorial.

After completing Mini Program development, in the next article I'll teach you how to deploy various projects to the internet so people worldwide can access your work.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
