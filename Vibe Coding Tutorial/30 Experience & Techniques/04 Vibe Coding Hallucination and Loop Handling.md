# Vibe Coding Hallucination and Loop Handling

> How to bring out-of-control AI back on track



Hello, I'm Fish Skin.

In previous articles, we covered how to have efficient conversations with AI and how to manage context. But even if you do everything well, you'll inevitably encounter situations where AI goes on strike — it starts talking nonsense, gets stuck in infinite loops, or stubbornly insists on wrong solutions.

This situation is very common in Vibe Coding, we call it AI hallucination. Below I'll teach you how to identify and fix these problems, bringing out-of-control AI back on track.



## I. What is AI Hallucination?

Before covering solutions, we need to understand what AI hallucination is.



### Definition of AI Hallucination

AI hallucination refers to AI-generated content that looks reasonable, but is actually wrong, non-existent, or doesn't match facts.

For example, in this conversation, my real name isn't this...

![](https://pic.yupi.icu/1/image-20260104184328898.png)

In programming scenarios, AI hallucination usually manifests as:

- Making up non-existent APIs or functions
- Giving seemingly reasonable but actually unrunnable code
- Insisting on solutions proven wrong
- Confusing usage of different tech stacks

For example, you ask AI: How to get a component's DOM node in React?

AI might tell you to use `this.getDOMNode()`.

This method sounds very reasonable, but actually doesn't exist in modern React. The correct approach is to use `useRef`.



### Why Do Hallucinations Occur?

There are several reasons for AI hallucinations:

1. Training data limitations: AI's knowledge comes from training data. If the data has errors or outdated information, AI learns wrong knowledge.

2. Context confusion: When conversations are too long or information is too messy, AI might confuse different contexts.

3. Overconfidence: AI is trained to give "definite" answers. Even when uncertain, it appears very confident.

4. Pattern matching errors: AI might mix similar but different concepts together.

Understanding these reasons helps us better deal with hallucination problems.



### Extended Knowledge - Common Types of AI Hallucinations

In Vibe Coding, AI hallucinations mainly have these types:

1. API hallucination: Making up non-existent functions, methods, or properties

2. Syntax hallucination: Confusing syntax of different languages or frameworks

3. Logic hallucination: Code logic looks right, but actually has problems

4. Version hallucination: Using deprecated APIs or outdated approaches

5. Dependency hallucination: Referencing non-existent libraries or wrong package names

Knowing these types helps you quickly identify problems.



## II. Signs of AI Getting Stuck in Infinite Loops

Besides hallucinations, AI has another common problem: getting stuck in infinite loops.



### What is an Infinite Loop?

Infinite loop refers to AI repeatedly trying the same wrong solution, unable to jump out itself.

Typical manifestations:

- First time: AI gives you code, but has a bug.
- Second time: You tell it there's a problem, it changes a bit, but still the same problem.
- Third time: You point out the problem again, it changes again, but still spinning in the same place.
- Fourth time: You start doubting life...

This is an infinite loop. AI is trapped in a wrong way of thinking, unable to get out itself. Not only wastes time, but also wastes a lot of tokens.

![](https://pic.yupi.icu/1/aideadloop大.jpeg)



### Common Scenarios for Infinite Loops

Infinite loops often appear in these scenarios:

1. Complex state management: AI easily gets confused when handling complex state updates

2. Async operations: Easy to make mistakes when涉及 Promise, async/await

3. Type systems: TypeScript's complex type definitions easily confuse AI

4. Performance optimization: AI might get stuck in "optimize => error => revert => re-optimize" loop

5. Cross-file modifications: When modifying multiple files, easy to lose track of one thing while addressing another, especially when the project has many files



### How to Identify Infinite Loops?

Some signals I personally use to identify infinite loops:

- AI gives essentially the same solution 3 times in a row
- Each modification just changes the wording, but core problem isn't solved
- AI starts apologizing and says "let me try again"
- You find yourself repeating the same problem

Once you discover these signals, immediately interrupt, don't continue.



## III. How to Cut Context and Start Over

When AI is stuck in an infinite loop or has serious hallucinations, the most effective method is to cut context and start over.



### Why Cut Context?

Continuing conversation in chaotic context is like sinking deeper into a quagmire. AI will be influenced by previous wrong information, making it hard to give correct answers.

Cutting context is equivalent to giving AI a restart chance, letting it start from a clean state.



### Correct Way to Cut

Don't just start a blank conversation and begin asking questions. The correct method is:

1) Summarize current problem

Before starting new conversation, first organize:

- What function you want to implement
- What solutions have been tried
- What specific problems were encountered
- Current code status



2) Start new conversation

In new conversation, first provide complete context:

```markdown
I'm developing a blog system, tech stack is Next.js 16 + TypeScript + Supabase.
I want to implement auto-save functionality for articles, but encountered problems.
I tried using useEffect to listen for content changes, but it causes frequent saves. I also tried debounce, but sometimes loses data.
This is my current code: [paste relevant code]
Please help me analyze the problem and give a solution.
```



3) Clearly Require Different Approach

Tell AI the previous solution doesn't work, need to change approach:

```markdown
The previous solutions all have problems, please give me a completely different implementation approach.
```

This way AI won't repeat previous mistakes.

Or first use other AI models to give different solutions, then directly paste the solution to AI for it to implement.



### When Should You Cut?

Not all problems need cutting context. If it's just a small problem, correct it in current conversation. But if you encounter these situations, decisively cut:

- Conversation has too many rounds (over 20), context is already very long, continuing will only cost more and be more chaotic
- AI starts confusing concepts, like getting your tech stack wrong, or mixing code from different functions
- You yourself feel confused, can't clearly describe current state, continuing will only get more chaotic
- Also the "infinite loop" situations mentioned earlier

Simply put, when you discover the conversation is already out of control, it's time to cut. Rather than struggling in the quagmire, better to start over.



## IV. How to Feed AI Error Information

Many times, AI-generated code has bugs, but it doesn't know. At this point, you need to accurately feed it the error information.



### Completely Copy Error Messages

Don't just say "code has errors" or "doesn't work," but copy the complete error message to AI.

❌ Bad feedback: Your code has problems, can't run.

✅ Good feedback:

```markdown
Code throws error when running, error message follows:
TypeError: Cannot read property 'map' of undefined
    at NoteList (NoteList.tsx:15)
    at renderWithHooks (react-dom.development.js:14985)
This is line 15 code:
{notes.map(note => <NoteItem key={note.id} note={note} />)}
```

Complete error messages let AI quickly locate problems.



### Provide Context Code

Besides error messages, also provide relevant code context.

```markdown
This is the complete code for the component that errored, error occurs at line 9:
export function NoteList() {
  const [notes, setNotes] = useState();

  useEffect(() => {
    fetchNotes().then(data => setNotes(data));
  }, []);

  return (
    <div>
      {notes.map(note => <NoteItem key={note.id} note={note} />)}
    </div>
  );
}
```

This way AI can see complete context and give accurate fix.



### Explain Reproduction Steps

If it's a bug related to user interaction, explain how to reproduce.

```markdown
This error only appears in specific situations:

1. User first enters page normally
2. After clicking 'refresh' button normally
3. But if user first deletes a note, then clicks "refresh", it throws error

Error message is: [paste error message]
```

After all, AI can't see user actions. Detailed reproduction steps help AI understand the problem's essence.



### Use Browser Console

If there's a problem with the webpage frontend, definitely make good use of the browser console.

Press F12 to open developer tools, switch to Console tab, you'll see:

- Error messages (red)
- Warning messages (yellow)
- Log messages (white)

Screenshot or copy this information to AI, it can more quickly find problems.

![](https://pic.yupi.icu/1/image-20260104190230437.png)

If you don't know if it's a frontend problem, or don't know what frontend is at all, it's probably a frontend problem.



## V. Judging Problem Source

Sometimes, the problem isn't with AI, but with your requirements or logic itself.

If it's AI's problem, it generally has these characteristics:

- Code syntax errors or can't run
- Using non-existent APIs
- Logic obviously doesn't match your description
- Code style completely inconsistent with before

These problems can be solved through better prompts or cutting context.

But if it's a logic problem, it generally has these characteristics:

- Code runs, but result is wrong
- Edge cases not handled
- Performance problems
- Poor user experience

These problems need you to rethink requirements, not blindly blame AI.



### How to Judge Problem Source?

A simple method is to ask yourself: if I gave this requirement to a real developer, could they do it right?

If the answer is "not sure" or "might also have problems," it's likely the requirement itself isn't clear enough.

At this point, you need to first:

1. Re-sort requirements
2. Clarify boundary conditions
3. Draw flowcharts or state diagrams
4. Write detailed test cases

Then discuss implementation solutions with AI.

Some students say: How do I know if a real developer could do it right?!

This is also a lack of professional knowledge. If you understand technology yourself, you can better control AI and judge problems. Even if you don't know the answer to this problem, you can try describing your requirements in a different way, or use other AI to polish requirements and help you judge.



## VI. Practical Case: Fixing an Out-of-Control Project

Let me use a real case to show how to fix an out-of-control project.



### Scenario Description

You're making a todo app, want to implement drag-and-drop sorting. You've had over ten rounds of conversation with AI, but the function still isn't right:

- First time: AI used a non-existent library
- Second time: Switched to react-beautiful-dnd, but code errors
- Third time: Fixed errors, but data doesn't update after dragging
- Fourth time: Data updates, but interface doesn't refresh
- Fifth time: Interface refreshes, but order is wrong
- You start doubting life...

What would you do next?



### 1. Pause and Analyze

Don't continue! First pause, analyze the problem:

- What's the core problem? (drag-and-drop sorting)
- Why is it always wrong? (maybe AI's understanding of state management is wrong)
- Is there a simpler solution? (maybe don't need a library)



### 2. Cut Context

Start a new conversation, but this time ask in a different way:

```markdown
I want to implement a simple drag-and-drop sorting function. Don't use third-party libraries, use native HTML5 Drag and Drop API
Requirements:
1. User can drag list items
2. Show placeholder when dragging
3. Update order when dropped
4. Data managed with useState
Please first give me a simplest implementation, just needs to be draggable, no animation needed.
```



### 3. Gradually Improve

AI gives a simple version, you test and find it works, great.

Then gradually add features:

1. Good, now add visual feedback when dragging: dragged item becomes semi-transparent.
2. Then add placeholder: show dashed box at target position when dragging.
3. Finally add smooth animation effects.

Each step is very small, each can be tested, this way it won't get out of control.



### 4. Summarize Experience

After problem solved, have AI help you summarize:

```markdown
We just implemented drag-and-drop sorting. Please summarize:
1. Why didn't the previous solutions work?
2. What are the key points of this solution?
3. What should be noted when implementing similar functions in the future?
```

These summaries can be added to your project documents, avoiding repeating the same pitfalls later.



## VII. Techniques to Prevent Hallucinations

Besides fixing problems, we can also prevent them in advance.



### 1. Require AI to Explain

Don't blindly accept AI's answers, have it explain why it does this.

- Why did you choose useCallback instead of useMemo?
- What are the pros and cons of this solution?
- Are there other implementation approaches?

Through explanation, you can discover if AI really understands the problem.



### 2. Require Documentation Links

If AI mentions an API or library, have it provide official documentation links.

```markdown
You mentioned react-query's useInfiniteQuery, can you give me the official documentation link?
```

If AI can't give a link, or the link is wrong, then the API might be made up.



### 3. Step-by-Step Verification

Don't implement the entire function at once, but verify in steps.

- First help me implement the core part, others use fake data for now
- This step runs, then we do the next step

Small steps, fast running, verify each step, can discover problems early.



### 4. Use Type System

Recommend using TypeScript technology in projects. It's a programming language that adds type checking to JavaScript, can fully leverage its type system to prevent problems.

What is a type system?

Simply put, it's clearly marking each variable and function with what type of data it is. For example, this variable is a number, that variable is a string, this function returns a user object, etc. With these annotations, the editor can discover problems while you write code, rather than only throwing errors at runtime.

Look at an example:

```ts
// ❌ No type definition: AI might generate wrong code
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// If passed data format is wrong, only throws error at runtime
calculateTotal([{ name: 'product' }]); // Runtime error: price is undefined

// ✅ Has type definition: editor immediately prompts error
interface Item {
  name: string;
  price: number;
}

function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// Editor immediately prompts with red wavy line: missing price property
calculateTotal([{ name: 'product' }]); // Discover error when writing
```

If the generated project is relatively complex, AI should default to using TypeScript technology. You can also actively require AI: Please add complete TypeScript type definitions for all functions and components.

This way, if AI-generated code has type mismatch problems, the editor will immediately prompt you with red wavy lines, and you can discover and fix immediately. This is much more efficient than waiting until runtime to discover problems.



### 5. Write Tests

Have AI help you write test cases:

```markdown
Please write unit tests for this function, covering normal cases and edge cases.
```

Tests help you discover logic problems.



### 6. Let AI Autonomously Verify Work

Don't just have AI do work, also let it know how to verify its own work.

For example, when developing web applications, you can have AI open a browser to test the UI. After discovering problems, it automatically iterates until the function runs normally. This forms an automated feedback loop:

```markdown
Please implement this function, and automatically open a browser to test after completion. If problems are discovered, please automatically fix and retest until the function works normally.
```

This approach lets AI work more autonomously, reducing manual intervention, especially suitable for handling tasks requiring multiple iterations, and is also a technique strongly recommended by Claude Code's founder.



## VIII. Common Hallucination Scenarios and Coping Methods

Based on my experience, here are some common hallucination scenarios and coping methods.



### Scenario 1: Fabricated API

Manifestation: AI uses an API that sounds reasonable but doesn't actually exist.

Coping:

```markdown
This API can't be found in official documentation, are you sure it exists? Please give me the documentation link.
```

If AI admits the error, have it give the correct API:

```markdown
Then what's the correct approach? Please implement using the officially recommended method.
```



### Scenario 2: Outdated Approach

Manifestation: AI uses a deprecated API or old version approach.

Coping:

```markdown
This approach is from the old version. I'm using React 19, please use the latest approach.
```

Then clearly require:

```markdown
Please use Hooks rather than Class components.
```



### Scenario 3: Confused Tech Stack

Manifestation: AI mixes usage of different frameworks.

Coping:

```markdown
Wait, you gave Vue's approach, I'm using React. Please rewrite in React's way.
```

Then re-emphasize tech stack:

```markdown
My project uses React 19 + TypeScript, please ensure code matches this tech stack.
```



### Scenario 4: Logic Loophole

Manifestation: Code runs, but has obvious logic problems.

Coping:

```markdown
This solution has a problem: if user closes page during loading, data will be lost. Please consider this edge case.
```

Then require improvement:

```markdown
Please add error handling and data persistence.
```



### Scenario 5: Performance Problem

Manifestation: Code works, but performance is poor.

Coping:

```markdown
This solution will be very slow when data volume is large. Please optimize performance, like using virtual scrolling or pagination.
```

Then require analysis:

```markdown
Please analyze this solution's time complexity and give optimization suggestions.
```



## In Conclusion

AI hallucination and infinite loops are inevitable problems in Vibe Coding, but they're not scary. As long as you master the correct coping methods, you can quickly solve them.

Let me summarize this article's key points:

1. Understand hallucination's essence: AI doesn't make mistakes intentionally, but is limited by training data and context.

2. Identify infinite loop signals: Three times in a row with same wrong solution, be alert.

3. Be brave to cut context: Don't sink deeper in the quagmire, restart promptly.

4. Provide complete information: Error messages, code context, reproduction steps all need to be given to AI.

5. Distinguish problem sources: Judge if it's AI's problem or logic's problem.

6. Prevention is better than cure: Discover problems early through explanation, verification, testing.

Remember, AI is your assistant, not magic. It will make mistakes, but as long as you master debugging methods, you can make it a reliable partner.

Next article, I'll explain Vibe Coding efficiency improvement techniques, teaching you how to improve development efficiency through shortcuts, templates, automation, etc.

Go for it, partners! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
