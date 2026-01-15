# Vibe Coding Security Protection Techniques

> Protect your projects and API keys



Hello, I'm Fish Skin.

Many students without programming foundation don't consider security issues at all when using AI to make projects. They think as long as the code runs, it's fine, and they'll deal with security when problems arise. But in reality, one security issue can destroy an entire project.

I've seen someone lose thousands overnight due to API Key leakage. I've also seen someone's database deleted, with all user data gone. As for large company projects, any problem will cause a huge uproar.

In this article, I'll cover the most easily overlooked security issues in Vibe Coding and how to avoid them.



## I. Fatal Problem - API Key Leakage

Among all security issues, API Key leakage is one of the most common and most fatal.



### What is an API Key?

API Key is like your house key - with it, you can use a certain service. For example, OpenAI's API Key lets you call ChatGPT, Supabase's API Key lets you access the database.

The problem is, if someone else gets this key, they can impersonate you to use these services. If it's a paid service, they'll spend your money; if it's a database, they might read, modify, or even delete your data.



### Common Ways of Leaking

The most common way API Keys leak is: **directly written in code, then uploaded to GitHub**.

Many students might write code to call AI large models like this:

```typescript
// ❌ Never do this!
const OPENAI_API_KEY = 'sb-yupi-abc123def456...';

const response = await fetch('https://xxx/v1/chat/completions', {
  headers: {
    'Authorization': `Bearer ${OPENAI_API_KEY}`
  }
});
```

Then push the code to GitHub.

What's the result?

Since your GitHub project is set to public, anyone can see your code, and thus can see your API Key. Even worse, there are many automated scripts specifically scanning GitHub for API Keys - once found, they're immediately used.

I've heard of someone who put OpenAI's API Key directly in frontend code, then others found his API Key directly from the browser's developer tools, and he was charged thousands within a few hours. By the time he discovered it, the money was already spent.

This lesson teaches us: **API Key leakage is not a small matter, must be taken seriously.**



## II. How to Correctly Manage Sensitive Information?

Since we can't write API Keys in code, what should we do?



### Using Environment Variables

The correct approach is to use environment variables.

Environment variables are configuration information stored in the system or runtime environment, not included in code.

#### Step 1: Create .env File

Create a `.env` file in the project root directory:

```
OPENAI_API_KEY=sb-yupi-abc123def456...
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGci...
DATABASE_URL=postgresql://...
```



#### Step 2: Use in Code

Access these variables in code through `process.env`:

```typescript
// ✅ Correct approach
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

const response = await fetch('https://xxx/v1/chat/completions', {
  headers: {
    'Authorization': `Bearer ${OPENAI_API_KEY}`
  }
});
```



#### Step 3: Add to .gitignore

Ensure `.env` file won't be uploaded to GitHub:

```
# .gitignore
.env
.env.local
.env.*.local
```



#### Step 4: Create .env.example

To let others know what environment variables are needed, create a `.env.example` file:

```
OPENAI_API_KEY=your_openai_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_key_here
DATABASE_URL=your_database_url_here
```

This file can be uploaded to GitHub because it doesn't contain real keys.



### Frontend vs Backend Distinction

Here's an important distinction: **frontend code is public, backend code is private.**

In frontend (code running in browser), even if you use environment variables, these values will eventually be packaged into JavaScript files, and users can see them through developer tools. So, **absolutely don't use sensitive API Keys in frontend code**!

The correct approach is:

- Put sensitive API calls in backend
- Frontend only calls your own backend API
- Backend verifies user identity, then calls third-party API

Let me give some code examples:

```typescript
// ❌ Don't call OpenAI directly in frontend
// Frontend code
const response = await fetch('https://api.openai.com/v1/chat/completions', {
  headers: { 'Authorization': `Bearer ${OPENAI_API_KEY}` }
});

// ✅ Should do this
// Frontend code: call your own backend
const response = await fetch('/api/chat', {
  method: 'POST',
  body: JSON.stringify({ message: userMessage })
});

// Backend code: call OpenAI
export async function POST(request: Request) {
  const { message } = await request.json();

  // Use API Key in backend
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    headers: { 'Authorization': `Bearer ${process.env.OPENAI_API_KEY}` },
    body: JSON.stringify({ messages: [{ role: 'user', content: message }] })
  });

  return response;
}
```



### Using Key Management Services

For production environment, recommend using dedicated key management services, like Vercel's environment variable management, AWS Secrets Manager, HashiCorp Vault, etc. These services provide more secure key storage and access control, large companies generally do this.



## III. Other Common Security Issues

Besides API Key leakage, there are other common security issues.



### SQL Injection

SQL injection is one of the most classic security vulnerabilities. If you directly splice user input into SQL queries, attackers can execute malicious SQL statements through special input.

```typescript
// ❌ Dangerous: SQL injection risk
const query = `SELECT * FROM users WHERE email = '${userEmail}'`;

// ✅ Safe: use parameterized queries
const query = 'SELECT * FROM users WHERE email = ?';
const result = await db.execute(query, [userEmail]);
```

Fortunately, if you use modern tools like Supabase, Prisma, etc., they automatically help you prevent SQL injection. But if you write raw SQL, you must pay attention to this problem.



### XSS Attacks

XSS (Cross-Site Scripting) refers to attackers injecting malicious scripts into your website.

For example, if you directly display user input content on the page:

```typescript
// ❌ Dangerous: XSS risk
function Comment({ text }) {
  return <div dangerouslySetInnerHTML={{ __html: text }} />;
}
```

Attackers can input `<script>alert('Fish Skin is a dog')</script>`, and this script will execute in other users' browsers.

![](https://pic.yupi.icu/1/image-20260105155517608.png)

The correct approach is:

```typescript
// ✅ Safe: React automatically escapes
function Comment({ text }) {
  return <div>{text}</div>;
}
```

React by default escapes all content, unless you use `dangerouslySetInnerHTML`. So, **unless necessary, don't use `dangerouslySetInnerHTML`**.



### CSRF Attacks

CSRF (Cross-Site Request Forgery) refers to attackers inducing users to execute unintended operations on logged-in websites.

For example, you're logged into a banking website, then open a malicious website in another tab. This malicious website has code that automatically sends a transfer request to the banking website. Because you're still logged in, the banking website thinks it's your own operation and executes the transfer. This is a CSRF attack.

There are 3 common methods to defend against CSRF:

1) Use CSRF Token: Server generates a random token, must carry this token for each form submission, server verifies if token is correct.

2) Use SameSite Cookie attribute: Set Cookie's SameSite attribute, making browser send Cookie only for same-site requests.

3) Verify request's Referer header: Check which website initiated the request, reject if not your own website.

If you use modern frameworks like Next.js, Nuxt.js, etc., they generally automatically handle CSRF protection.



### Authentication and Authorization

Don't trust any frontend validation!

**Frontend validation is just for user experience, real validation must be done in backend.**

Let me give some code examples:

```typescript
// ❌ Not safe: only check in frontend
function AdminPanel() {
  const isAdmin = localStorage.getItem('isAdmin') === 'true';
  if (!isAdmin) return <div>Access Denied</div>;
  return <div>Admin Panel</div>;
}

// ✅ Safe: verify in backend
// Frontend
function AdminPanel() {
  const { data, error } = useFetch('/api/admin/data');
  if (error) return <div>Access Denied</div>;
  return <div>Admin Panel</div>;
}

// Backend
export async function GET(request: Request) {
  const user = await verifyToken(request);
  if (!user.isAdmin) {
    return new Response('Forbidden', { status: 403 });
  }
  // Return data
}
```



### Dependency Package Security

If your project uses many third-party packages, these packages may also have security vulnerabilities.

A disaster affecting innocent bystanders - recommend regularly running `npm audit` command to check for vulnerabilities.

If vulnerabilities are found, run the following command, it will automatically update vulnerable packages.

```bash
npm audit fix
```

For vulnerabilities that can't be automatically fixed, manually check and decide whether to replace the package.



## IV. Security Checklist

Before releasing each project, recommend going through this checklist with AI + human.



### Keys and Sensitive Information

- [ ] All API Keys use environment variables
- [ ] .env file added to .gitignore
- [ ] Created .env.example file
- [ ] Sensitive API calls done in backend
- [ ] No keys exposed in frontend code
- [ ] Production environment keys different from development environment



### User Input Validation

- [ ] All user input validated
- [ ] Validation done in both frontend and backend
- [ ] Used parameterized queries to prevent SQL injection
- [ ] Avoided using dangerouslySetInnerHTML
- [ ] File uploads checked for type and size



### Authentication and Authorization

- [ ] Used secure authentication scheme (like JWT, OAuth)
- [ ] Passwords encrypted and stored (using bcrypt, etc.)
- [ ] Sensitive operations require re-verification
- [ ] Implemented permission control, different users have different permissions
- [ ] Sessions have expiration time



### HTTPS and Transport Security

- [ ] Production environment uses HTTPS
- [ ] Cookies set with Secure and HttpOnly flags
- [ ] Used SameSite Cookie to prevent CSRF
- [ ] Sensitive data encrypted during transmission



### Dependencies and Third-Party Services

- [ ] Regularly run npm audit to check for vulnerabilities
- [ ] Only use trusted third-party packages
- [ ] Regularly update dependency packages
- [ ] Review third-party package permissions



### Error Handling and Logging

- [ ] Error messages don't expose sensitive information
- [ ] Production environment doesn't show detailed error stack traces
- [ ] Logs don't record passwords and other sensitive information
- [ ] Implemented error monitoring and alerting



## V. Let AI Help You with Security Checks

Undoubtedly, AI can also help you discover and fix security issues.

You can have AI review your code for security:

```markdown
Please review this code from a security perspective and find potential security issues:
【paste your code】
Focus on checking:
1. Any SQL injection risks?
2. Any XSS attack risks?
3. Is user input validated?
4. Is sensitive information exposed?
5. Is error handling secure?
```

AI will give you detailed security analysis.

After discovering problems, have AI help you fix them:

```markdown
You mentioned this code has SQL injection risk. Please give me a secure implementation using parameterized queries.
User input here isn't validated. Please add validation logic to ensure email format is correct and password length is at least 8 characters.
```

But note, **don't completely rely on AI's security advice**. AI might miss some problems, or give solutions that aren't secure enough. You need to combine with your own judgment, and when necessary consult official documentation or find multiple AI large models to confirm.



### Using Security Scanning Tools

Besides AI, you can also use specialized security scanning tools:

- Snyk: Scan dependency package vulnerabilities
- SonarQube: Code quality and security analysis
- OWASP ZAP: Web application security testing

![](https://pic.yupi.icu/1/evo-by-snyk-hp-image_j0acql.png)

These tools can automatically discover many security issues.



## VI. Secure Development Habits

Security isn't a one-time job, but requires forming habits, always keeping it in mind.



### Principle of Least Privilege

Give each user and service only necessary permissions, don't give extra permissions.

For example, if an API Key only needs to read data, don't give it write permission. If a user is just a regular user, don't give them admin permission.

This way, even if a key or account is stolen, the loss will be smaller.



### Regularly Rotate Keys

Don't use one API Key forever. Regularly change keys, like every 3 months or every 6 months.

Most services support creating multiple API Keys. You can first create a new Key, update it in the project, after confirming no problems, then delete the old Key.



### Monitor Abnormal Activity

Many API services provide usage monitoring and alerting functions, remember to enable them to discover anomalies in time.

If your API call volume suddenly spikes, it might mean the Key was stolen. If someone tries multiple failed logins, they might be brute-forcing passwords.



### Keep Updated

Security vulnerabilities will be continuously discovered, and software packages will continuously update to fix vulnerabilities. Regularly update your dependency packages, follow security announcements, timely fix known security issues.



### Backup Data

Even with all protections, problems can still happen. Recommend regularly backing up data, so you can recover even in worst-case scenarios.

If you use third-party backend services like Supabase, they might automatically backup. If it's your own database, set up regular backups.



## In Conclusion

Security issues are often the most easily overlooked because they're not as intuitive as functionality or performance. But once a security issue occurs, the consequences can be catastrophic.

Finally, let me summarize this article's key points:

1. API Key leakage is the biggest risk: absolutely don't write API Keys in code, use environment variables.
2. Distinguish between frontend and backend: sensitive operations must be done in backend, don't trust any frontend validation.
3. Understand common vulnerabilities: SQL injection, XSS, CSRF all need to be guarded against.
4. Use security checklist: go through checklist before each release, ensure nothing is missed.
5. Form security habits: least privilege, regularly rotate keys, monitor anomalies, keep updated, backup data.
6. Make good use of tools: AI and security scanning tools can help you discover problems, but don't completely rely on them.

Security is a continuous process, not a one-time effort. Stay vigilant, regularly check, to protect your projects and users.

Hope these security protection techniques help you avoid common security issues, making your Vibe Coding projects more secure and reliable.

Thanks for your hard work studying, treat yourself to a chicken leg 🍗, then set off!



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
