# Vibe Coding Code Refactoring Techniques

> Avoid AI generating messy spaghetti code



Hello, I'm Fish Skin.

You may have encountered this situation: when you first use AI to make a project, the code is clear and concise, looking very comfortable. But as more and more functions are added, the code starts to become messy. Finally, you dare not touch this code yourself, because changing one place might affect other places.

This situation is particularly common in Vibe Coding, because AI might only focus on "can it run," ignoring "is it maintainable." Below I'll teach you how to identify and repay technical debt, keeping your code always elegant.



## I. What is Technical Debt?

Technical debt is a very vivid metaphor.

Imagine you want to build a house. To finish quickly, you use some temporary solutions: the foundation isn't solid, walls aren't straight, wires are casually strung. The house is built, people can live in it, but there are many hidden dangers. If not fixed in time, problems will get bigger and bigger, and repair costs will get higher and higher.

Technical debt is just like this. To quickly implement functions, you (or AI) adopt some less-than-ideal solutions. These solutions work at the time, but bury hidden dangers for the future. As the project develops, these hidden dangers become actual problems, slowing down your development speed.

In this year's research, it was found that AI-generated code particularly easily produces technical debt. Because AI is good at quickly implementing functions, but not good at considering long-term architecture and maintainability. It will give you code that is "highly functional but systematically lacks architectural judgment."



### Manifestations of Technical Debt

So, how do you judge if your project has technical debt? The most obvious signal is: changing code becomes more and more difficult, you start to fear modifying code, because you don't know where it will affect. If you find yourself often feeling "can't touch this place," "changing here might affect there," it means technical debt is already quite serious.



### Dangers of Technical Debt

The dangers of technical debt are cumulative. At first it might just be messy code, not affecting functions. But as time passes, problems will get more and more serious.

- Development slows down, because you have to spend more time understanding and modifying code
- More and more bugs, because code is too complex, prone to errors
- New functions are hard to add, because existing architecture doesn't support them
- Team collaboration is difficult, because no one can fully understand the code

Worst of all, at some critical point, you might have to rewrite the entire project. This is the "bankruptcy" of technical debt.



## II. Common Problems with AI-Generated Code

When using AI for Vibe Coding, if context management is poor, requirements description isn't clear enough, or you let AI implement too complex functions at once, the generated code might have some quality problems. Below are several typical scenarios — understanding them helps you better guide AI.



### Excessive Nesting

To ensure code runs, AI sometimes generates deeply nested code.

What is nesting?

It's if inside if, loop inside loop, like Russian nesting dolls. For example:

```typescript
function processData(data: any) {
  if (data) {
    if (data.items) {
      if (data.items.length > 0) {
        data.items.forEach(item => {
          if (item.active) {
            if (item.price > 0) {
              // Actual logic
            }
          }
        });
      }
    }
  }
}
```

This kind of code is hard to read and hard to maintain. A better approach is early return:

```typescript
function processData(data: any) {
  if (!data?.items?.length) return;

  const activeItems = data.items.filter(item =>
    item.active && item.price > 0
  );

  activeItems.forEach(item => {
    // Actual logic
  });
}
```

Obviously, the second approach is clearer and easier to understand.



### Duplicate Code

AI might not proactively reuse code, but generates new code for each requirement.

For example, suppose you let AI separately implement user list page, article list page, comment list page. AI will give you three sets of almost identical code, only with different data fields. Or you might have this code in multiple components:

```typescript
const handleSubmit = async () => {
  setLoading(true);
  try {
    const response = await fetch('/api/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    const result = await response.json();
    setData(result);
  } catch (error) {
    console.error(error);
  } finally {
    setLoading(false);
  }
};
```

This duplicate code should be extracted into a common function or custom Hook.



### Lack of Abstraction

AI tends to write specific, direct code, rather than abstract, reusable code.

For example, you want to display user list and article list, AI might give you two completely independent components, even though their structure is almost the same.

A better approach is to create a generic list component, then reuse it with different data and render functions.



### Careless Naming

AI sometimes uses relatively careless names, like `data`, `result`, `temp`, `handleClick`. These names don't accurately express intent, making code hard to understand.

This situation might occur because your requirements description isn't specific enough, and AI doesn't know the real purpose of this variable or function.

Good naming should be **self-explanatory**, like `userData`, `apiResponse`, `temporaryBuffer`, `handleLoginButtonClick`.

If you find AI-generated naming too careless, you can explicitly state in requirements: please use meaningful variable names and function names that clearly express their purpose.



## III. How to Use AI to Refactor Code?

Since AI produces technical debt, can you use AI to repay technical debt?

The answer is yes. This is also a major advantage of Vibe Coding — **AI can both quickly write code and quickly modify code**.



### Let AI Identify Problems

You can paste code to AI and let it review from a professional perspective, helping you find problems in the code.

````markdown
Please review this code and find areas for improvement:
```typescript
【paste your code】
```

Please analyze from these angles:
1. Is there duplicate code?
2. Are functions too long?
3. Is naming clear?
4. Is there excessive nesting?
5. Can common logic be extracted?
````

AI will give you a detailed analysis report.



### Let AI Provide Refactoring Solutions

After finding problems, let AI give you refactoring solutions, like:

- You mentioned this code has duplicate logic. Please give me a refactoring solution that extracts the duplicate parts into a common function.
- This function is too long. Please help me split it into several small functions, each doing only one thing.

AI will give you specific refactored code.



### Small Step Refactoring

Note, don't recommend refactoring the entire project at once — this risk is too high, maybe after refactoring your entire project won't run.

The correct approach is small step refactoring, each time only changing a small part.

For example, you find a function is too long, don't split it into 10 small functions at once. First split into 2, test passes, then continue splitting. Each step must ensure functionality doesn't change, tests all pass.

This way even if there are problems, it's easy to roll back.



### Timing for Refactoring

When should you refactor?

My suggestion is:

1) Don't specifically schedule time for refactoring, but refactor anytime during daily development. When you discover code has problems, fix it immediately, don't drag it out.

2) Refactor after completing functions. Function is done, tests pass, spend 10 ~ 15 minutes looking at code, see if there are areas that can be improved.

3) Refactor before adding new functions. If you find existing code isn't suitable for adding new functions, refactor first, making code easier to extend.

4) Regular focused refactoring. Every month or every major version, spend half a day focused refactoring, dealing with accumulated technical debt.



## IV. Modularity and Code Reuse

Modularity is key to avoiding technical debt. Moreover, modular code is more friendly to AI — when you need to modify some function, AI only needs to read related small modules, not the entire several hundred line file, so AI can more accurately understand and modify code.



### What is Modularity?

Modularity is dividing code into independent, reusable modules. Each module only does one thing, does one thing well. Modules communicate through clear interfaces, without interfering with each other.

Good modularity has these characteristics:

- High cohesion: code within modules is closely related
- Low coupling: dependencies between modules are as minimal as possible
- Single responsibility: each module is only responsible for one thing
- Clear interfaces: module inputs and outputs are clear



### Component Splitting

In the frontend development framework React, components are the most basic modules. You can understand components as independent parts on a page, like navigation bar, search box, user card, etc.

But many people (including AI) write very "heavy" components.

For example, a user profile page, AI might write all logic in one component: fetching data, form validation, submit handling, error prompts... The result is a giant component of several hundred lines.

A better approach is to split into multiple small components:

```typescript
// Main component, responsible for coordination
function ProfilePage() {
  const { user, loading, error } = useUser();

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;

  return (
    <div>
      <ProfileHeader user={user} />
      <ProfileForm user={user} />
    </div>
  );
}

// Sub-components, each doing their job
function ProfileHeader({ user }) {
  return (
    <div>
      <Avatar src={user.avatar} />
      <h1>{user.name}</h1>
    </div>
  );
}

function ProfileForm({ user }) {
  // Form logic
}
```

This way, each component is very small, easy to understand and test.

Even if you don't understand frontend or React, you can understand this idea — split big functions into small, independent parts, each part only does one thing. This principle applies to all programming languages and frameworks.



### Function Extraction

When you find a piece of code appears repeatedly in multiple places, you should extract it into a function.

For example, you need to format dates in multiple places:

```typescript
// Duplicate code
const formattedDate1 = new Date(date1).toLocaleDateString('zh-CN');
const formattedDate2 = new Date(date2).toLocaleDateString('zh-CN');
const formattedDate3 = new Date(date3).toLocaleDateString('zh-CN');

// Extract into function
function formatDate(date: Date | string): string {
  return new Date(date).toLocaleDateString('zh-CN');
}

const formattedDate1 = formatDate(date1);
const formattedDate2 = formatDate(date2);
const formattedDate3 = formatDate(date3);
```

This not only reduces duplication, but also makes code easier to maintain. If you want to change date format later, you only need to change one place.



### Using Custom Hooks

In the frontend development framework React, custom Hooks are a good way to reuse logic. Hooks are special functions used to manage state and side effects.

💡 You don't need to understand what professional terms like Hook, component, state management are. Just tell AI:

```markdown
This logic is repeated in multiple places, please help me extract it into a reusable module.
```

Then AI will automatically help you do abstraction and reuse.

For example, you need to fetch user data in multiple components, you can extract the user data fetching code into a Hook and reuse it elsewhere:

```typescript
// Before extraction: each component repeats these logics
function ProfilePage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchUser().then(setUser).catch(setError).finally(() => setLoading(false));
  }, []);

  // ...
}

// After extraction: create custom Hook
function useUser() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchUser().then(setUser).catch(setError).finally(() => setLoading(false));
  }, []);

  return { user, loading, error };
}

// Usage is very simple
function ProfilePage() {
  const { user, loading, error } = useUser();
  // ...
}
```

Custom Hooks make code more concise and easier to test.



## V. From Toy Projects to Commercial Products

Many people use AI to make toy projects — they work, but aren't professional enough or can't make money.

At this point you might think: how to turn it into a scalable commercial product?



### Characteristics of Toy Projects

Toy projects generally have these characteristics:

- All code in one file, or file organization is very chaotic
- No clear architecture, code written wherever
- Lacks error handling, only considers normal cases
- No tests, entirely manual testing
- Lots of hardcoding, configuration and code mixed together

Such projects can be used for demonstration or learning, but aren't suitable for long-term maintenance and expansion as commercial products.



### Characteristics of Commercial Products

Commercial products should be like this:

- Clear directory structure, at a glance see where things go
- Clear architecture, like MVC, MVVM or other patterns
- Complete error handling, considering various exceptional situations
- Sufficient testing, core functions have test coverage
- Configuration separation, environment variables, configuration files and code separated
- Complete documentation, has README, API documentation, comments, etc.

From toy to commercial product, you need to consciously improve code quality and refactor.

![](https://pic.yupi.icu/1/projectpk%E5%A4%A7.jpeg)



### Refactoring Steps

How to refactor a toy project into a commercial product?

I suggest proceeding in steps:

1) Organize directory structure. Categorize code by function or type, put in different folders. Like components in `components`, utility functions in `lib`, type definitions in `types`.

2) Extract duplicate code. Find duplicate logic, extract into common functions or components. This step can greatly reduce code volume.

3) Split large files. Split large files into small files, each file only responsible for one thing. For example, a large `utils.ts` can be split into `format.ts`, `validate.ts`, `storage.ts`, etc.

4) Add type definitions. If using TypeScript, add complete types to all functions and components. This can help you discover many potential problems.

5) Improve naming. Change unclear variable names, function names to descriptive names. This makes code easier to understand.

6) Add tests and documentation. Write tests for core functions, write README for project, add comments for complex logic.

All these steps can also be completed through AI-led + human verification. The key is each step must ensure functionality doesn't change and tests pass smoothly. Don't be greedy, take it step by step.



## VI. Practical Case - Refactoring a Chaotic Project

Let me use a real example to show how to refactor a chaotic project.



### Initial State

Suppose you used AI to make a todo app, all code in one `App.tsx` file, about 500 lines.

```typescript
// App.tsx (500 lines)
function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');
  const [loading, setLoading] = useState(false);

  // 100 lines of data fetching logic
  useEffect(() => { /* ... */ }, []);

  // 50 lines of add logic
  const handleAdd = () => { /* ... */ };

  // 50 lines of delete logic
  const handleDelete = () => { /* ... */ };

  // 50 lines of edit logic
  const handleEdit = () => { /* ... */ };

  // 50 lines of filter logic
  const filteredTodos = todos.filter(/* ... */);

  // 200 lines of JSX
  return (
    <div>
      {/* lots and lots of code */}
    </div>
  );
}
```

Although the code works, all functional logic is written together, not conducive to reading and maintenance.



### Refactoring Steps

#### Step 1: Extract Custom Hook

First, we extract all logic related to todo data (fetching, adding, deleting, updating) into an independent Hook. This way the main component doesn't need to care how data is managed, only needs to call these methods.

```typescript
// hooks/useTodos.ts
function useTodos() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);

  const addTodo = async (text: string) => { /* ... */ };
  const deleteTodo = async (id: string) => { /* ... */ };
  const updateTodo = async (id: string, text: string) => { /* ... */ };

  useEffect(() => {
    // Fetch data
  }, []);

  return { todos, loading, addTodo, deleteTodo, updateTodo };
}
```



#### Step 2: Split Components

Next, split the UI part into multiple small components. Each component only responsible for displaying and handling its own logic — like input box only handles input, list only displays, filter only filters. This way each component is very simple, easy to understand and modify.

```typescript
// components/TodoList.tsx
function TodoList({ todos, onDelete, onEdit }) {
  return (
    <div>
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onDelete={onDelete}
          onEdit={onEdit}
        />
      ))}
    </div>
  );
}

// components/TodoItem.tsx
function TodoItem({ todo, onDelete, onEdit }) {
  // Single todo item logic
}

// components/TodoInput.tsx
function TodoInput({ onAdd }) {
  // Input box logic
}

// components/TodoFilter.tsx
function TodoFilter({ filter, onChange }) {
  // Filter logic
}
```



#### Step 3: Reorganize Main Component

Finally, assemble the extracted Hook and split components. Now the main component only needs to coordinate these parts, telling them what to do, without caring how specifically to do it.

```typescript
// App.tsx (50 lines)
function App() {
  const { todos, loading, addTodo, deleteTodo, updateTodo } = useTodos();
  const [filter, setFilter] = useState('all');

  const filteredTodos = useFilteredTodos(todos, filter);

  if (loading) return <LoadingSpinner />;

  return (
    <div>
      <TodoInput onAdd={addTodo} />
      <TodoFilter filter={filter} onChange={setFilter} />
      <TodoList
        todos={filteredTodos}
        onDelete={deleteTodo}
        onEdit={updateTodo}
      />
    </div>
  );
}
```

See the difference? Code instantly went from 500 lines to 50 lines, and each part is very clear.



### Refactoring Results

Refactored code has these advantages:

- Each file is very small, easy to understand
- Clear responsibilities, each component only does one thing
- Easy to test, can test each component and Hook independently
- Easy to extend, to add new functions just add new components
- Easy to maintain, changing one place won't affect other places
- AI understands better: when you need to modify some function, AI only needs to read related small files (like 50-line `TodoInput.tsx`), not the entire 500-line `App.tsx`. This way AI can more accurately understand context and generate better code.

This is the transformation from toy project code to commercial product code.



## In Conclusion

Refactoring and technical debt management are aspects of Vibe Coding that need human intervention. AI can help you quickly write code, but can't always help you keep code elegant — you need to consciously do it.

Let me summarize today's key points:

- Understand technical debt: know what technical debt is, how it's produced, what dangers it has
- Identify AI code problems: excessive nesting, duplicate code, lack of abstraction, careless naming, these are all common problems
- Use AI to refactor: AI can both produce technical debt and help you repay technical debt
- Small step refactoring: don't change too much at once, each time only change a small part, ensure functionality doesn't change
- Modularity thinking: split code into independent, reusable modules, maintain high cohesion, low coupling
- Timely refactoring: don't procrastinate, fix problems immediately when discovered, don't let technical debt accumulate

Remember, elegant code requires careful maintenance and continuous refactoring.

Hope these refactoring techniques help you avoid code becoming a shit mountain, keeping your Vibe Coding projects always elegant.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
