# Team R&D Standards

> Enterprise-level development standards practice guide



Hello, I'm Fish Skin the programmer.

A few days ago I shared my one-year entrepreneurship review summary, mentioning one point: as the team expands, we'll pay more attention to development standards and technical沉淀.

Some programmer friends asked: What are development standards?

Other friends said: Fish Skin, don't treat us like outsiders, share your company's development standards for us to see?

![Development Standards](https://pic.yupi.icu/1/image-20240419140208921.png)

Sure, must arrange!

This article will briefly share our company's development standards with everyone. But before starting, I must clarify 2 points:

1. Each team should customize development standards according to their situation. Others' standards are only for reference and may not be most suitable for your team.
2. Limited space, this article only shares some standards I consider important, and removed our sensitive information.

⭐️ This article corresponds to video version: https://bilibili.com/video/BV1fi421C78M



## I. Overall Project Development Process

1) Team jointly confirms goals and planning

Hold meeting to discuss, produce goals and planning documents

2) Product research and requirement analysis

Produce research report and requirement analysis documents

3) Requirement review

Hold requirement review meeting, clarify requirements and work to be done, estimate workload and clarify work time nodes

4) Solution design

Produce solution design documents, like database table design, page design, interface design, etc.

5) Development

Including respective development, unit testing, frontend-backend integration, etc.

6) Testing and acceptance

Including development self-testing, product acceptance, team internal acceptance, etc.

7) Code submission

Submit deployable code, needs to be reviewed by person in charge, can merge after passing

8) Deployment and launch

Publish code to server, team internally notifies launch and updates launch documents. After launch, need to self-verify.

9) Product iteration

Continuously collect user feedback on new features and perform data analysis to verify change effects, facilitating next round of updates and iterations.



## II. Development Standards


### Pre-development Notes

1) Ensure you fully understand the business and requirements, need to do overall solution design first; especially for important requirements and core business, must first verify solution with team members and get approval before starting development to avoid duplicate work.

2) Familiarize yourself with the project before developing, recommend reading project documents, project code, interface documents, frontend component documents, etc.

3) Carefully introduce new dependencies or libraries, or upgrade versions. Major dependency changes need confirmation with other team members.

4) Familiarize yourself with functions and code already implemented by the team, try to reuse, avoid duplicate development.

5) Familiarize yourself with team internal development standards, and configure accordingly in IDE, like frontend configuring ESLint, Prettier and other code standard plugins.



### During Development Notes

1) When developing new features, ensure pulling **latest main branch** code from project repository.

2) Each feature should create its own branch for development. **Never directly modify main branch code!** Note branch names should use English, be semantic enough, don't confuse with others'.

3) When developing, try to reuse existing functions, modules, classes, methods, object code. If existing code is available, don't repeat writing.

4) When developing, follow team internal development standards, try to reference existing project code writing style, especially don't use formats, naming, writing styles inconsistent with original project, avoid being different.

5) During development, for anything unclear, don't guess, timely contact other project members or person in charge to confirm.

6) During development, every once in a while (like 1 - 3 days) can use `git pull` to sync latest main branch code, preventing merge code conflicts.

7) During development, pay attention to overall time schedule control, complete first then perfect, timely feedback if there are risks.

8) When developing, need to pay special attention to capturing and handling exceptional situations.

9) Each branch should try to stay pure, minimize code changes per development and submission. Recommend each branch only changes one function, Bug or module, don't write multiple unrelated functions together, and don't modify unless necessary.

10) After completing partial function development, must self-test! When self-testing, can Mock fake data. **Note absolutely don't test on production, absolutely don't affect production data!**



## III. Code Submission Standards

1) Only code that has passed testing and product acceptance can initiate PR request to merge to main branch. Before this, can submit to own branch.

2) Before initiating PR to merge to main branch, **must completely read your own code 3 times**, avoiding non-standard writing and meaningless changes.

3) Each merge should try to focus on only one function or change, avoid multiple functions coupled together for merging, improving review efficiency and reducing change risk.

4) Each submission needs to provide code change description in commit message, can also supplement by associating requirement documents, test cases, solution documents, effect screenshots, etc.

Commit message can reference [Conventional Commits document](https://www.conventionalcommits.org/zh-hans/v1.0.0/), but not mandatory.

5) Unless special circumstances, all code must be reviewed by at least one project leader through Code Review before merging; and only code merged to main branch is allowed to be published online.



## IV. Launch Standards


### Pre-launch Notes

1) Before launch, besides strictly verifying function features can run normally and meet requirements, also pay special attention to program's:

- Robustness. Like giving user-friendly error prompts, input validation.
- Security. Prevent unauthorized operations, input validation.
- Stability. Try to guarantee 100% successful calls. If there's chance of failure, consider retry or fault tolerance strategies.

2) Unless special circumstances, only functions verified by product and main branch code that passed code review are allowed to be published online.

3) Unless special circumstances, try to launch on workdays (recommend Tuesday ~ Thursday), ensuring problems after launch can be fixed timely.



### Post-launch Notes

1) After launch, must again perform complete process testing, especially focus on permission-related function testing.

2) After launch, must timely sync launch information in the group, notify relevant members, if problems occur, feedback immediately.

3) After first launch, need to immediately configure monitoring alerts.

4) After launch verification passes and is confirmed by internal group members, can publish version update announcement in external user groups.

5) After launch, immediately update project update record documents.

6) Note, launch is not the end point. For a period after launch (at least one week), must continuously observe whether functions you're responsible for run normally, continuously accept user feedback, observe new function effects through data analysis. Any problems during this period need immediate fixing, and prepare for next round of improvement iterations.



## In Conclusion

The above is our company's development standards, hope it helps everyone.

Again, each team should customize development standards according to their situation. This standard is for reference only.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
