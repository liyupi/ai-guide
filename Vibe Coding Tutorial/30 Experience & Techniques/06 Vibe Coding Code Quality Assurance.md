# Vibe Coding Code Quality Assurance

> How to ensure the quality of AI-generated code



Hello, I'm Fish Skin.

Many students have this concern when using AI for development: Is AI-generated code reliable? Are there hidden bugs?

This concern is reasonable. Although AI can quickly generate code, it can't guarantee code quality. As a developer, you need to establish a quality assurance system.

In this article, I'll share some practical methods to help you ensure the quality of AI-generated code.



## I. What is Good Code?

Before covering how to ensure quality, we first need to clarify what good code is.



### Characteristics of Good Code

What kind of code counts as good code?

This question seems simple, but many people can't explain it clearly. Actually, besides being able to run, the most important thing about good code is **good readability**: code is clear and easy to understand, conforms to team development standards, others (including future you) can quickly understand it. On this basis, it also needs **strong maintainability**, easy to modify and extend, without causing cascading changes.

Of course, all this must be built on the premise of **functional correctness** — code correctly implements requirements, has no bugs. At the same time, **performance should be reasonable**, complete tasks within acceptable time, not waste resources. Additionally, code must be **safe and reliable**, have no security vulnerabilities, handle exceptional situations.

![](https://pic.yupi.icu/1/goodcode%E5%A4%A7.jpeg)



### Common Problems with AI-Generated Code

So, what problems does AI-generated code usually have?

Based on my experience, the most common is **over-complexity** — AI often writes a lot of unnecessary code to implement functions. Another common problem is **lack of boundary handling** — AI might only consider normal cases to make code run quickly, ignoring special cases like null values and errors.

AI-generated code also often has the problem of **code duplication**. Especially in frontend development, if you let AI generate multiple similar pages separately, it won't proactively reuse code, but generates independent code for each page.

For example, suppose you're making a management backend with user list page, article list page, comment list page. These three pages have very similar layout and functions: all display data in tables, all have search boxes, all have pagination. But if you let AI generate them 3 times separately, it will give you 3 sets of almost identical code, only with different data fields. A better approach is to first have AI generate a generic list component, then reuse it with different configurations. This way not only is there less code, it's also easier to maintain.

Sometimes there are also **performance problems**, using inefficient algorithms or data structures. Understanding these problems lets you check and improve in a targeted way.



### Establish Quality Standards

Knowing what good code is, next you need to establish clear quality standards for your project.

In terms of code standards, suggest using ESLint or Prettier to unify code style, define clear naming rules (like variables use camelCase, constants use UPPER_SNAKE_CASE), and specify file and folder organization.

For functional standards, require all functions to have tests, handle boundary cases, errors have friendly prompts.

For performance, you can set specific metrics, like page load time doesn't exceed 3 seconds, API response time doesn't exceed 1 second, use virtual scrolling for large data volumes, etc.

You can write these standards in project documentation so AI also knows.

💡 However, in actual development you still need to be flexible. If you're just developing a small Demo project, just do it, don't need to consider so much.



## II. Code Review

Code review is the first line of defense for quality assurance.



### Why Review AI Code?

Some students think: AI-generated code can run, why review it?

This idea is actually quite dangerous.

First, AI isn't perfect, it makes mistakes, generates buggy code. More importantly, AI only knows technology, **doesn't understand your specific business logic**, the code it generates might be technically fine but unreasonable for the business.

Also, AI might only focus on current functions, not considering future extensibility. Code that runs today might become technical debt tomorrow. Moreover, reviewing code is also a learning opportunity, helps you understand how code works, improve your own technical level. So, reviewing AI code is essential, especially for students with programming foundation.

![](https://pic.yupi.icu/1/whyreviewcode%E5%A4%A7.jpeg)



### Review Focus

So, when reviewing AI-generated code, what aspects should you focus on?



#### 1. Functional Correctness

The most basic requirement is: can the code correctly implement requirements?

This sounds simple, but easily overlooked. You need to run code, **test all functions**, try various inputs, including normal and abnormal.

Pay special attention to boundary cases, like null values, maximum values, minimum values, etc., these are often high-risk areas for bugs.

For example:

```typescript
// AI-generated code
function divide(a: number, b: number): number {
  return a / b;
}
```

Think about it, what's wrong with this code?

The answer is: doesn't handle the case where divisor is 0.

```typescript
// Improved:
function divide(a: number, b: number): number {
  if (b === 0) {
    throw new Error('Divisor cannot be 0');
  }
  return a / b;
}
```



#### 2. Code Readability

After functionality is correct, next look at whether code is easy to read.

Remember, code is for people to read, not just for machines to execute.

When checking, ask yourself a few questions:

- Are variable names clear?
- Do function names express functionality?
- Is logic easy to understand?
- Are comments needed?

If you're confused when reading code, others will be too.

For example:

```typescript
// Bad naming
function f(x: number): number {
  return x * 2 + 1;
}

// Good naming
function calculateDiscountedPrice(originalPrice: number): number {
  const discount = 0.2; // 20% off
  return originalPrice * (1 - discount);
}
```



#### 3. Error Handling

Code needs to handle errors gracefully, not crash when something goes wrong.

You need to check if API calls have error handling, if user input has validation, if exceptional situations have friendly prompts. Much AI-generated code only considers normal flow, completely ignores error handling, which is very dangerous.

For example:

```typescript
// Bad error handling (none at all)
async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  const user = await response.json();
  return user;
}

// Good error handling
async function fetchUser(id: string) {
  try {
    const response = await fetch(`/api/users/${id}`);

    if (!response.ok) {
      throw new Error(`Failed to fetch user: ${response.statusText}`);
    }

    const user = await response.json();
    return { data: user, error: null };
  } catch (error) {
    console.error('Error fetching user:', error);
    return { data: null, error: error.message };
  }
}
```



#### 4. Performance Issues

Then there are performance issues. Code needs to be efficient, not waste resources.

You can see if there are unnecessary loops, repeated calculations, if data structure choices are reasonable. AI sometimes chooses the simplest but not most efficient solution to quickly implement functions.

For example:

```typescript
// Poor performance
function findUser(users: User[], id: string): User | undefined {
  // Traverses entire array every time, O(n)
  return users.find(user => user.id === id);
}

// Better performance
class UserManager {
  private userMap: Map<string, User>;

  constructor(users: User[]) {
    // Use Map for storage, lookup is O(1)
    this.userMap = new Map(users.map(u => [u.id, u]));
  }

  findUser(id: string): User | undefined {
    return this.userMap.get(id);
  }
}
```



#### 5. Security Issues

For commercial projects, this is crucial. Code needs to be secure, have no vulnerabilities.

Need to check if there are SQL injection risks, XSS attack risks, if sensitive information is encrypted, if API Keys are exposed. AI's understanding of security might not be deep enough, easily leaving security risks.

For example, SQL injection. SQL injection means attackers insert malicious SQL code in input to execute unexpected database operations.

For example, this code is insecure:

```typescript
// ❌ Insecure: directly splicing user input
const query = `SELECT * FROM users WHERE name = '${userName}'`;
```

Suppose user inputs username `admin' OR '1'='1` when logging in, directly splicing this input into SQL statement becomes:

```sql
SELECT * FROM users WHERE name = 'admin' OR '1'='1'
```

This query will return all users because `'1'='1'` is always true. Attackers can bypass verification and log into any account.

The correct approach is to use parameterized queries:

```typescript
// ✅ Secure: use parameterized queries
const query = 'SELECT * FROM users WHERE name = ?';
db.execute(query, [userName]);
```

Parameterized queries automatically escape special characters, preventing SQL injection.

If you're interested in web security, you can use Fish Skin's [free network security self-study site](https://github.com/liyupi/ceshiya) to learn this knowledge:

![](https://pic.yupi.icu/1/%E6%B5%8B%E8%AF%95%E9%B8%AD%E7%BD%91%E7%AB%99.png)



### Review Process

You can follow these steps to establish a systematic review process:

1. Read through yourself first: quickly browse code, see if there are obvious problems

2. Run tests: test all functions, including boundary cases

3. Line-by-line review: carefully check every line of code, think about whether there are problems

4. Record problems: write down discovered issues

5. Ask AI to improve: give feedback to AI about problems, let it fix them

6. Review again: confirm fixed code has no new problems

This process might be a bit tedious, but can greatly improve code quality.

For friends without programming foundation, if you can't understand code yourself, you can use other AI large models to help review. This is a very practical technique: **use multiple AIs for cross-validation**.

For example, for code generated by Cursor (Claude), you can copy it to ChatGPT or Gemini, let them help you review:

```markdown
Please review this code, find potential issues, including bugs, performance problems, security risks.
```

Different AIs have different perspectives and training data, can complement each other — a problem one AI might miss, another AI can discover.

When I do important projects myself, I often have 2 ~ 3 different AIs review the same code, then synthesize their suggestions. Although this takes a bit more time, it can greatly reduce the risk of errors. Especially for critical business logic, security-related code, performance-sensitive parts, an extra layer of protection is always good.



## III. Testing

Testing is a key means of ensuring code quality.



### Why Write Tests?

Many students think writing tests is a waste of time, but actually the opposite is true. Testing can discover problems during development, not wait until after launch for users to discover. With tests, you can confidently refactor code without fear of breaking things. Moreover, test code itself is good documentation, showing how to use your functions or components.

Also, although writing tests takes time, it saves more debugging time. Think about it, if you manually test all functions every time you change code, how much time would that take? With automated testing, just run it to know if there are problems.

So, writing tests is worth it.

![](https://pic.yupi.icu/1/testpk%E5%A4%A7.jpeg)



### Types of Testing

There are mainly 3 types of testing.

- Unit testing: test individual functions or components, fast, easy to locate problems, high coverage needed
- Integration testing: test collaboration between multiple modules, ensure interfaces between modules are correct, cover main flows
- End-to-end testing: simulate complete user operations, test entire system, cover key scenarios

For Vibe Coding projects, I suggest **focusing on unit tests and integration tests**. Although end-to-end tests are also important, they're more costly — can just cover the most critical scenarios.



### Let AI Help You Write Tests

Nowadays the vast majority of test code no longer needs to be written manually — you can directly let AI help you generate test code.

````markdown
Please write unit tests for this function, covering normal cases and boundary cases:
```typescript
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}
```
````

AI will generate test code like this:

```typescript
import { describe, it, expect } from 'vitest';

describe('calculateTotal', () => {
  it('should correctly calculate total', () => {
    const items = [
      { price: 10, quantity: 2 },
      { price: 5, quantity: 3 }
    ];
    expect(calculateTotal(items)).toBe(35);
  });

  it('should handle empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('should handle quantity of 0', () => {
    const items = [{ price: 10, quantity: 0 }];
    expect(calculateTotal(items)).toBe(0);
  });

  it('should handle decimals', () => {
    const items = [{ price: 10.5, quantity: 2 }];
    expect(calculateTotal(items)).toBe(21);
  });
});
```

This test code's function is: use `describe` to define a test group (testing the calculateTotal function), then use multiple `it` to define specific test cases. Each test case calls the function and checks if results meet expectations. For example, the first test checks normal case, second test checks empty array, third test checks quantity of 0 case, fourth test checks decimals. When running these tests, if all `expect` pass, it means function works normally; if any fail, it means there's a problem with the code.

With these tests, you can ensure the function works normally in various situations.



### Extended Knowledge - Test-Driven Development (TDD)

You can try test-driven development (TDD). This is a "write tests first, then code" development method.

Sounds counterintuitive right? Generally don't we write code first, then tests?

But TDD's logic is: you first define how the function should work (write tests), then let AI implement the function according to tests. This ensures code meets requirements and is testable from the start.

The specific process is:

1. First write a failing test (because function isn't implemented yet)
2. Then let AI implement the function to make tests pass, run tests to ensure all tests pass
3. Finally optimize code but keep tests passing

This way, you avoid writing code that "looks like it works but actually has problems".



## IV. Advanced Debugging Techniques

Even with review and testing, you'll still encounter bugs. At this point, you need to master debugging techniques.



### 1. Use Breakpoint Debugging

Many students only know how to use `console.log` when debugging code — that is, adding a line `console.log(variableName)` in code to print variable values, then viewing in browser console.

Although this method is simple, it's not efficient, and after debugging you have to delete these logs.

Actually breakpoint debugging is much more efficient. In VS Code or Cursor, you just need to click left of the line number to set a breakpoint, then press F5 to start debugging.

![](https://pic.yupi.icu/1/image-20260105092822939.png)

Code will pause at the breakpoint, and you can view all variable values:

![](https://pic.yupi.icu/1/image-20260105092855154.png)

You can also execute code step by step, seeing what happens at each step. This is much more convenient than adding `console.log` everywhere then deleting.



### 2. Browser Debugging Tools

When doing frontend development, browser debugging tools are your good helpers. Press F12 in browser to open developer tools.

Inside are several commonly used panels:

- Console panel can view logs and errors, execute JavaScript code, view variable values
- Sources panel can set breakpoints, execute step by step, view call stack
- Network panel can view API requests, check requests and responses, analyze load time
- Performance panel can analyze performance bottlenecks, view render time, find slow operations

![](https://pic.yupi.icu/1/image-20260105093342746.png)

Mastering these tools will greatly improve your debugging efficiency.



### 3. Binary Search Problem Location

If you're not sure where the problem is, try binary search method.

Easy to understand — directly split code in half, comment out one half, see if problem still exists. If it does, problem is in the other half; if not, problem is in this half. Then continue splitting the problematic half in half, repeat this process until you find the problem.

Although this method is simple, it's very effective, especially when handling large blocks of code.



### 4. Rubber Duck Debugging

This is a seemingly mystical and rigid, but actually scientifically grounded method.

When you're stuck on a bug, try explaining your code to someone (or a rubber duck): blah blah, this function should do this... It first does this... Then does that... Hmm, something seems wrong here...

Magically, during the explanation process, you'll often discover the problem. Because explaining forces you to reorganize your thoughts and look at problems from different angles.

What programmer doesn't have a little yellow duck?

![](https://pic.yupi.icu/1/smallyellowduck%E4%B8%AD.jpeg)



### 5. Let AI Help You Debug

Give error message and related code to AI, let it help you analyze:

````markdown
This code has an error:
```
TypeError: Cannot read property 'map' of undefined
```

The code is:
```typescript
function UserList({ users }) {
  return (
    <div>
      {users.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
}
```

Please help me analyze the problem and give a solution.
````

AI will tell you the problem might be `users` is `undefined`, and give a solution.

This is undoubtedly the most commonly used method by students, but it's not 100% effective — can try first, if it doesn't work then handle manually.



## V. Quality Checklist

You can establish a quality checklist, have AI + human go through it before each code commit.

However, now AI large models' programming ability is getting stronger and stronger, many AI tools have built-in code checking capabilities, automatically prompting for some common problems. So just understand this checklist simply, no need to memorize it.



### Function Check

- [ ] All functions work normally
- [ ] Boundary cases are handled
- [ ] Error cases have friendly prompts
- [ ] User experience is smooth



### Code Check

- [ ] Code conforms to project standards
- [ ] Variable and function naming is clear
- [ ] No duplicate code
- [ ] Complex logic has comments
- [ ] No commented-out code



### Performance Check

- [ ] No unnecessary repeated calculations
- [ ] List rendering uses key
- [ ] Large data volumes use pagination or virtual scrolling
- [ ] Images are optimized



### Security Check

- [ ] User input is validated
- [ ] Sensitive information is not exposed
- [ ] API Keys use environment variables
- [ ] No SQL injection risks



### Test Check

- [ ] Core functions have unit tests
- [ ] Test coverage meets standards
- [ ] All tests pass
- [ ] Manually tested main flows



### Documentation Check

- [ ] README is up to date
- [ ] Important functions have comments
- [ ] API interfaces have documentation
- [ ] Environment variables have descriptions



## VI. Using Linters and Formatters

Automated tools can help you discover many problems.

💡 This part is quite professional, mainly suitable for students with programming foundation. If you're completely zero foundation, you can skip first and come back when needed.



### ESLint Code Checking

ESLint is a JavaScript / TypeScript code checking tool that can automatically discover problems in code, like unused variables, possible bugs, non-standard practices, etc. Like an automated code reviewer, helping you discover problems before running code.

Installation and configuration (latest configuration method based on [official documentation](https://eslint.org/docs/latest/use/getting-started)):

```bash
npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

Create `.eslintrc.json` configuration file, define checking rules:

```json
{
  "parser": "@typescript-eslint/parser",
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended"
  ],
  "rules": {
    "no-console": "warn",
    "no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

Run check:

```bash
npm run lint
```

ESLint will tell you problems in code, like unused variables, potential bugs, etc.



### Prettier Code Formatting

Prettier is a code formatting tool that can automatically adjust code format, like indentation, line breaks, quote types, etc., making code look more neat and unified. Like Word's "format painter" function — one click makes all code maintain the same style.

Installation (latest usage based on [official documentation](https://prettier.io/)):

```bash
npm install -D prettier
```

Create `.prettierrc` configuration file, define formatting rules, like whether to use semicolons, single quotes or double quotes, how many spaces for indentation, etc.:

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

Run formatting:

```bash
npx prettier --write "src/**/*.{ts,tsx}"
```

Prettier will automatically adjust code format, making code look neater.



### Integrate in Editor

Install ESLint and Prettier plugins in VS Code / Cursor / WebStorm and other programming tools, automatically check and format when saving files.

Take VS Code as example, configure in `settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

This way every time you save a file, code will automatically format and fix problems.



### Integrate in Git

Use Husky and lint-staged tools to automatically check before committing code.

Husky is a Git hook tool that can automatically execute scripts during Git operations (like commit, push). lint-staged is specifically used to check files about to be committed, not the entire project.

Execute command to install these tools:

```bash
npm install -D husky lint-staged
npx husky init
```

Then configure in `package.json`:

```json
{
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```

This way every time you execute `git commit` to commit code, it will automatically check and format code.



## VII. Continuous Code Quality Improvement

Code quality isn't a one-time job, but a process of continuous improvement. Regularly spend time refactoring — simplify complex functions, extract duplicate code, improve naming, add comments. Suggest spending half an hour refactoring every week or after completing each function, keeping code clean.

If it's team development, regularly holding code review meetings is very helpful. Can select a few pieces of code each week to review together, discuss what was done well, what can be improved, share best practices, unify code style. This not only improves code quality, but also promotes learning and communication between team members.

Also, for programmers, it's important to look at excellent open source projects. React's source code, Next.js's source code, code from well-known component libraries are all good learning materials. See how others write, learn their techniques and ideas. Every time you discover a bug or encounter a problem, record it: what was the problem, why did it occur, how was it fixed, how to avoid recurrence. These experiences can help you avoid repeating mistakes and continuously improve code quality.



## In Conclusion

Code quality is the most easily overlooked but most important part of Vibe Coding. AI can help you write code quickly, but can't guarantee code quality. As a developer, you need to establish a complete quality assurance system, or at least know what kind of code is good and high quality.

Finally, let me summarize this article's key points:

1. Clarify quality standards: know what good code is, establish project quality standards.

2. Seriously review code: don't blindly trust AI, carefully review every line of code.

3. Write tests: testing is key to ensuring quality, don't be lazy.

4. Master debugging techniques: learn to use breakpoints, browser tools, etc. for efficient debugging.

5. Use automated tools: ESLint, Prettier and other tools can automatically discover problems.

6. Continuous improvement: regularly refactor, learn excellent code, record lessons learned.

Fast development is important, but code quality is more important. Better to be a bit slower and ensure quality.

Hope these methods help you establish a complete code quality assurance system, making your Vibe Coding projects more stable and reliable.

Go for it, partners! 👍🏻



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
