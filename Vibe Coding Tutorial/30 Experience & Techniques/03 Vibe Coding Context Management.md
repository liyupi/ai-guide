# Vibe Coding Context Management Techniques

> Making AI truly understand your project



Hello, I'm Fish Skin.

In the previous two articles, we covered the core principles and conversation techniques of Vibe Coding. Today we'll discuss a more fundamental but equally important topic — context management.

You may have encountered this situation: when you first start talking with AI, it performs very smartly, and the generated code meets your requirements well. But after chatting for a while, it starts losing memory, forgetting the tech stack you mentioned earlier, forgetting the project's design style, even starting to use completely different approaches to implement features.

This isn't AI getting stupid, but its memory having issues. Below I'll teach you how to give AI a reliable "memory patch" through **context engineering**.



## I. What is Context Engineering?

Before covering specific methods, we need to understand what context is.



### Context is AI's Working Memory

Imagine you're working with a new colleague on a project. If you have to explain from scratch every time what the project is, what technology is used, what standards there are, efficiency will be very low. But if you have a shared project document that the new colleague can glance at and understand, collaboration will be much smoother.

Context is this "project document." It contains all the background information AI needs to know:

- What your project is
- What tech stack is used
- What design standards exist
- What functions have been completed
- What you're currently working on

With this information, AI can give accurate, consistent answers.



### Importance of Context

Many people focus on "writing good prompts," but actually, **context may be more important than prompts**.

A good prompt lets AI understand your current needs, but good context lets AI understand your entire project. The former is a "point," the latter is a "surface."

For example, if you only say "help me write a button," AI might write in native HTML, or React, and the style is its own decision.

But if you provide complete context "project uses React, Tailwind CSS, design style is minimalist modern, main color is blue," AI can give you a button that completely matches the project style. This is the power of context.



### 3 Levels of Context

Context can be divided into 3 levels:

1. Project-level context: Basic information about the entire project, like tech stack, design standards, directory structure, etc.

2. Feature-level context: Information about the function currently being developed, like what this function does, what other functions it depends on, etc.

3. Conversation-level context: Temporary information in the current conversation, like problems just discussed, code snippets just generated, etc.

![](https://pic.yupi.icu/1/contextlevel大.jpeg)

Managing these three levels of context well, you can keep AI always "in the zone."



## II. AI's Short-term Memory

Let's start with the most basic — how to manage AI's short-term memory?



### What is a Context Window?

AI has a context window, which can be understood as its short-term memory capacity. This window is limited, typically from several thousand to several hundred thousand tokens (roughly equivalent to several thousand to several hundred thousand words).

When you talk with AI, each message takes up space in this window. The longer the conversation, the fuller the window gets. When the window is full, early conversation content gets forgotten.

This is why AI loses memory — not that it really forgot, but early information has been squeezed out of the window.



### One Conversation, One Task

The simplest management method is: **one conversation does only one thing**.

Don't discuss login function, payment function, and performance optimization all in one conversation. This makes context chaotic, and AI easily gets confused.

Correct approach is:

- When doing login function, start a new conversation
- When done, tested and passed, start another new conversation for payment function
- When encountering performance issues, start another new conversation specifically for optimization

Each conversation focuses on one task, context stays clear.

Of course, if it's multiple simple functions, putting them all in one conversation is fine, be flexible~



### Regularly Compress Context

If a task really requires a long conversation, you can regularly compress context.

The specific approach is: when the conversation is halfway through, have AI summarize the progress so far.

Some AI programming tools have built-in instructions for summarizing context, can use directly:

![](https://pic.yupi.icu/1/image-20260104180238760.png)

You can also manually enter a prompt to summarize:

```markdown
Please summarize what we've done so far, including:
1) What functions have been completed
2) What technical solutions have been used
3) What problems remain to be solved
```

Then, you can use this summary to start a new conversation and continue the work. This is equivalent to compressing the previous long conversation into a brief summary.



### Make Good Use of Recaps

When starting a new conversation, have AI briefly review previous content.

For example:

```markdown
We previously made a login form, using React Hook Form and Zod validation. Now I want to redirect to the home page after successful login.
```

This way AI can quickly recall previous work and give coherent answers.



## III. AI's Long-term Memory

Besides short-term memory in conversations, you also need to establish long-term memory for the project, typically by **providing project documentation**.



### README.md: Project's ID Card

`README.md` is the project's most important document, it should include:

1. Project introduction: What this project does, what problem it solves

2. Tech stack: What technologies, frameworks, libraries are used

3. Directory structure: Purpose of main files and folders

4. Development standards: Code style, naming rules, etc.

5. How to run: Commands for installing dependencies and starting the project

A good `README.md` should let anyone (including AI) understand the project's basic situation at a glance.

For example:

````markdown
# My Blog System

A concise personal blog system, supporting Markdown writing and code highlighting.

## Tech Stack

- Frontend: Next.js 14 (App Router) + TypeScript + Tailwind CSS
- Backend: Supabase (PostgreSQL + Auth)
- Deployment: Vercel

## Directory Structure

- `/app` - Next.js pages and routes
- `/components` - Reusable components
- `/lib` - Utility functions and configuration
- `/public` - Static assets

## Development Standards

- Use functional components, not class components
- All components must have TypeScript types
- Styles use Tailwind CSS, no custom CSS
- API calls uniformly use functions from `/lib/api.ts`

## How to Run

```bash
npm install
npm run dev
```
````

Fish Skin's open-source projects' `README.md` basically follow this structured format, like the [AI Zero-Code Application Generation Platform Project](https://github.com/liyupi/yu-ai-code-mother), for everyone's reference.

Every time you start a new conversation, paste the `README.md` content to AI, and it can quickly understand your project.



### TODO.md: Project Task List

`TODO.md` records the project's pending tasks and progress, it should include:

1. Completed functions: What functions have been done

2. Functions in development: What you're currently working on

3. Functions to be developed: What to do next

4. Known issues: What bugs or places need optimization

For example:

```markdown
# Development Progress

## Completed ✅

- [x] User registration and login
- [x] Article list page
- [x] Article detail page
- [x] Markdown rendering

## In Progress 🚧

- [ ] Article editing function
  - [x] Editor interface
  - [ ] Save draft
  - [ ] Publish article

## To Be Developed 📋

- [ ] Comment function
- [ ] Search function
- [ ] Tag system

## Known Issues 🐛

- Mobile navigation bar displays abnormally on some devices
- Code highlighting contrast not enough in dark theme
```

`TODO.md` lets both you and AI clearly know the project's progress, avoiding duplicate work or missing functions.



### Update Documents Promptly

The biggest problem with documents is becoming outdated. So, every time you complete a function or make important changes, promptly update `README.md` and `TODO.md`.

You can have AI help you update:

```markdown
We just completed the article editing function. Please help me update TODO.md, mark "article editing function" as completed.
```

AI naturally knows the importance of this, so when we generate code AI might automatically generate these documents for us.



## IV. Context Strategies for AI Programming Tools

Different AI tools handle context differently, you need to understand their characteristics.



### Cursor's .cursorrules

Cursor supports creating a `.cursorrules` file in the project root directory, as the project's system prompt.

You can write in this file:

```
This is a Next.js blog project.

Tech stack:
- Next.js 16 (App Router)
- TypeScript
- Tailwind CSS
- Supabase

Code standards:
- Use functional components
- All components must have TypeScript type definitions
- Styles only use Tailwind CSS
- Don't use any type

Design style:
- Minimalist, modern
- Main color: #3B82F6 (blue)
- Border radius: 8px
- Shadow: subtle

Please always follow these standards.
```

This way, Cursor will automatically reference these rules when generating code.

💡 Note, as AI programming tools update, these rules might change, suggest checking [official documentation](https://cursor.com/cn/docs/context/rules) more often.

![](https://pic.yupi.icu/1/image-20260104181209687.png)



### Claude Code's CLAUDE.md

Claude Code reads the `CLAUDE.md` file in the project root directory as context.

You can put more detailed information in this file:

```markdown
# Project Context

## Project Overview
Personal blog system, supporting Markdown writing.

## Tech Stack
- Next.js 16 + TypeScript + Tailwind CSS
- Supabase (database + authentication)

## Important Decisions
1. Why Supabase: Simple, free quota sufficient, built-in authentication
2. Why App Router: This is Next.js's future direction
3. Why not Redux: Project is simple, React Context is enough

## Known Issues
- Mobile navigation bar needs optimization
- Code highlighting theme needs adjustment

## Next Steps
- Implement comment function
- Add search
```

This file is equivalent to a project manual for AI.



### Universal Strategy: Context Folder

If the tool you use doesn't support specific context files, you can create a `/docs` folder and put all documents in it:

```
/docs
  - README.md (project overview)
  - TECH_STACK.md (tech stack details)
  - DESIGN.md (design standards)
  - API.md (API documentation)
  - TODO.md (task list)
```

Every time you start a new conversation, just paste the relevant document content to AI.



## V. Techniques for Fixing Context Breakage

Even with good context management, sometimes AI still loses track. At this point, you need to know how to fix it.



### How to Identify Breakage?

Context breakage usually shows these signs:

- AI suddenly uses a different tech stack (like you clearly use React, but it writes Vue code for you)
- AI forgets previously discussed design solutions
- AI-generated code style is inconsistent with before
- AI repeatedly asks questions you've already answered

Once you discover these signals, fix promptly.



### Fix Method 1: Reprovide Context

The simplest method is to paste the context again.

```markdown
Wait, our project uses React and TypeScript, not Vue.
This is our tech stack: [paste README.md's tech stack section]. Please regenerate code with the correct tech stack.
```



### Fix Method 2: Reference Previous Content

If it forgot previously discussed content, you can reference it.

```markdown
Remember we previously decided to use Context API to manage state? Please continue with this solution, don't switch to Redux.
```



### Fix Method 3: Start New Conversation

If context is already too chaotic to fix (like the same bug has been fixed multiple times with no result), the best approach is to start a new conversation.

In the new conversation, first provide complete context, then continue working. Although this means starting over, it ensures subsequent conversation quality.



### Fix Method 4: Back on Track Prompt

Sometimes, you can use a clear prompt to get AI back on track.

```markdown
Please pause. Our current goal is to implement login functionality, using React Hook Form and Supabase Auth.
Please confirm you understand this goal, then we continue.
```

This is equivalent to giving AI a restart chance. However, Fish Skin tested this, sometimes this prompt might not work.



## VI. Best Practices for Context Management

Based on my experience and community summary, here are some best practices for context management.



### 1. Establish Documents from Project Start

Don't wait until the project is halfway done to remember writing documents. Create `README.md` and `TODO.md` from day one and keep updating.

This not only helps AI, but also helps you clarify your thinking.



### 2. Use Tool's Native Context Mechanisms

If the tool you use supports specific context files (like `.cursorrules`), prioritize using these mechanisms, they're the most efficient.



### 3. Keep Context Concise

Context isn't better the more there is. Too much information will actually confuse AI.

Suggest providing only the most important, most relevant information. If information isn't useful for the current task, don't put it in context, it wastes tokens.



### Practice Four: Use Hierarchical Structure

Suggest dividing context into different levels and files, rather than piling everything in one file.

For example:
- README.md puts project overview and basic information
- TECH_STACK.md puts detailed tech stack explanation
- DESIGN.md puts design standards
- Each function module has its own documentation



### Practice Five: Regularly Review and Update

Every week or after completing a major function, review documents, see if there's outdated content, update promptly.

You can have AI help you check:

```markdown
Please check my README.md, see if there's anything inconsistent with current code.
```



### 6. Enhance Code Context with Comments

Add meaningful comments in code, explaining "why" not just "what."

❌ Bad comment:

```typescript
// Get user data
const user = await getUser(id);
```

✅ Good comment:

```typescript
// Get user data from Supabase
// Note: This doesn't include sensitive information (like passwords), only returns public fields
const user = await getUser(id);
```

Good comments help AI understand code's intent, making more reasonable decisions when modifying.



## VII. Practical Case: Establishing Complete Context System

Let me use a real example to show how to establish a complete context system for a project.

Suppose you're making an online notes app.



### Step 1: Create README.md

```markdown
# Online Notes App

A concise online notes app, supporting Markdown editing and real-time saving.

## Tech Stack

- Frontend: React 18 + TypeScript + Vite
- UI Library: Tailwind CSS + Headless UI
- Editor: CodeMirror 6
- Backend: Supabase (PostgreSQL + Realtime)
- Deployment: Vercel

## Core Functions

1. User registration and login
2. Create, edit, delete notes
3. Markdown real-time preview
4. Auto-save notes
5. Note search

## Directory Structure

- `/src/components` - React components
- `/src/pages` - Page components
- `/src/lib` - Utility functions and API
- `/src/hooks` - Custom Hooks
- `/src/types` - TypeScript type definitions

## Development Standards

- Components use functional components + Hooks
- All components must have TypeScript types
- Styles only use Tailwind CSS
- API calls uniformly use functions from `/src/lib/api`
- State management uses Zustand

## Design Style

- Minimalist, professional
- Main color: #6366F1 (Indigo)
- Border radius: 6px
- Font: Inter
```



### Step 2: Create TODO.md

```markdown
# Development Progress

## Completed ✅

- [x] Project initialization
- [x] Supabase configuration
- [x] User authentication (registration/login)
- [x] Notes list page

## In Progress 🚧

- [ ] Notes editor
  - [x] CodeMirror integration
  - [x] Markdown syntax highlighting
  - [ ] Real-time preview
  - [ ] Auto-save

## To Be Developed 📋

- [ ] Note search
- [ ] Note categories/tags
- [ ] Export function
- [ ] Dark theme

## Known Issues 🐛

- Editor performance poor on mobile
- Long notes load slowly
```



### Step 3: Create rules File

```
Project: Online Notes App

Tech stack:
- React 18 + TypeScript + Vite
- Tailwind CSS + Headless UI
- CodeMirror 6
- Supabase
- Zustand (state management)

Code standards:
- Use functional components
- All components must have TypeScript type definitions
- Props type naming: ComponentName + Props (like EditorProps)
- Styles only use Tailwind CSS
- Don't use any type
- API calls must have error handling

Design standards:
- Main color: #6366F1
- Border radius: rounded-md (6px)
- Spacing: Use Tailwind's standard spacing (4, 8, 12, 16...)
- Buttons: px-4 py-2, darker on hover
- Input fields: border-gray-300, focus border-indigo-500

Naming standards:
- Component files: PascalCase (like NoteEditor.tsx)
- Utility functions: camelCase (like formatDate.ts)
- Constants: UPPER_SNAKE_CASE (like API_URL)

Please always follow these standards.
```



### Step 4: Add Context Comments in Code

```typescript
// src/lib/api/notes.ts

/**
 * Notes API function collection
 *
 * Technical choice explanation:
 * - Use Supabase Client instead of direct SQL
 * - All functions return { data, error } format
 * - Errors handled uniformly here, no exceptions thrown
 */

import { supabase } from './supabase';
import type { Note } from '@/types';
```

With this complete context system, whenever you start a new conversation, just paste the relevant documents to AI, and it can quickly get into the zone and give accurate answers.



## In Conclusion

Context engineering is the most easily overlooked but extremely important part of Vibe Coding. Many people focus on "how to ask" but ignore "how to make AI remember."

Let me summarize this article's key points:

1. Context is AI's working memory: it determines whether AI can understand your project.

2. Manage three levels well: project-level, feature-level, conversation-level context all need attention.

3. Establish documentation system: README.md, TODO.md, context files are all essential.

4. Utilize tool features: Different tools have different context mechanisms, make good use of them.

5. Fix breakage promptly: When you discover AI lost memory, fix immediately, don't continue.

6. Keep concise and updated: Context should be refined, accurate, promptly updated.

Mastering context engineering, you can keep AI always in state, greatly improving development efficiency.

Next article, I'll explain methods for debugging AI hallucinations, teaching you how to handle AI error situations.

Go for it, go go go! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
