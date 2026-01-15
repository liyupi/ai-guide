# Vibe Coding Full-Stack Application Development

> Building complete full-stack applications with frontend, backend, and database


Hello, I'm Programmer Fish Skin.

In this article, I'll walk you through building 3 complete full-stack projects: a personal blog system, a simple Q&A community, and an online store (Mini version).

What is a full-stack application?

Simply put, it's a complete application with a frontend interface, backend services, and database storage. Users interact through the frontend, data is processed by the backend, and ultimately saved to the database. These projects will teach you how to develop frontends and backends the Vibe Coding way, handling real-world scenarios like user authentication and database operations.

It should be noted that this tutorial focuses more on providing guidance on approach and project development workflow. The goal is to guide everyone in learning how to use Vibe Coding for project development, and you'll need to practice on your own. If you need more complete Vibe Coding graphic and video tutorials, check out Fish Skin's original project practice section.



## I. Full-Stack Development Basics

Before starting the projects, let's understand some basic concepts of full-stack development.

Full-stack development consists of three parts: frontend (the interface users see), backend (business logic processing), and database (data storage).

The frontend is responsible for displaying data and receiving user input, the backend handles requests and business logic, and the database provides persistent storage. The three communicate through API interfaces.

![](https://pic.yupi.icu/1/fullstackarchitecture%E5%A4%A7.jpeg)

For example, when a user publishes an article on a blog website, the frontend collects the article's title, content, and other information, then sends an HTTP request to the backend. Upon receiving the request, the backend verifies whether the data is valid, then calls the database interface to save the article to the database. After successful saving, the backend returns a success response to the frontend, which displays a "Publish successful" message.

There are many mainstream full-stack technology stack options. For Vibe Coding, I recommend using modern, AI-friendly technology stacks. For frontend, you can use React or Vue; for backend, Node.js (Express, Nest.js) or Python (FastAPI); for database, MySQL, PostgreSQL, or MongoDB.

But actually, the specific technology used isn't the most important thing—what matters is understanding the full-stack development mindset. Once you master the approach, you can quickly pick up a different technology stack.

There's a huge advantage to developing full-stack applications with Vibe Coding: you don't need to master all the details of frontend and backend—you just need to know what functionality to implement, and AI will help you generate the code.

For example, you just need to tell AI: "Create a user registration endpoint that receives username, email, and password, validates them, and saves to the database."

AI can help you generate complete backend code, including parameter validation, password encryption, database operations, etc. This greatly lowers the barrier to full-stack development, allowing you to focus on business logic rather than getting tangled in technical details.



## II. Project Practice - Personal Blog System

A blog system is one of the most classic full-stack projects, involving features like article publishing, category management, and comment interactions. Through this project, you can learn how to handle CRUD (Create, Read, Update, Delete) operations, as well as basic functions like user authentication.

This blog system needs to support publishing, editing, deleting, and viewing articles. Articles can be categorized and support tags. Users can register and login to publish their own articles. Visitors can browse articles but cannot publish them. Articles support Markdown format and can have cover images. The homepage displays an article list with pagination and search support.

![](https://pic.yupi.icu/1/demoweb10.png)

For technology selection, frontend uses React + TypeScript + Vite, styling with Tailwind CSS. Backend uses Node.js + Express, database with MySQL. User authentication uses JWT (JSON Web Token). The article editor can reuse the Markdown editor built previously.



### Development Steps

1) Design Database

The first step in development is designing the database. Before writing code, design the database structure first. Create a `database.md` file to define what tables are needed and what fields each table has.

For example, the users table needs: id (primary key), username (username, unique), email (email, unique), password (password, encrypted storage), avatar (avatar URL), created_at (creation time).

The articles table needs: id, title (title), content (content, Markdown format), cover (cover image URL), category (category), tags (tags, JSON array), author_id (author ID, foreign key to users), views (view count), created_at, updated_at.

The categories table needs: id, name (category name), description (category description).

2) Write Requirements Document

After designing the database, you can write the requirements document. Create a `PRD.md` file:

```markdown
# Personal Blog System PRD

## Core Features

### User Features
- Registration: username, email, password
- Login: return JWT token
- Profile: view and edit personal information

### Article Features
- Publish article: title, content, category, tags, cover
- Edit article: modify published articles
- Delete article: can only delete your own articles
- View article: display article details, view count +1
- Article list: support pagination, category filtering, search

### Frontend Pages
- Homepage: article list
- Article detail page
- Write article page (requires login)
- Profile page (requires login)
- Login/Registration page
```

3) Develop Backend with AI

With the documentation, you can start developing the backend with AI. Open Cursor and begin the conversation.

First step, initialize backend project:

```
Please create a Node.js + Express backend project:
1. Initialize project, install dependencies like express, mysql2, jsonwebtoken, bcrypt
2. Create basic project structure: src/routes (routes), src/controllers (controllers), src/models (data models), src/middleware (middleware), src/config (config)
3. Configure database connection
```

This prompt describes what project to create, which dependencies to install, and what the project structure looks like.

Second step, create database tables:

```
Based on the design in database.md, create SQL statements for database tables. Then create an initialization script that automatically creates these tables.
```

AI will generate CREATE TABLE SQL statements based on your database design.

Third step, implement user registration and login:

```
Implement user registration and login functionality:

Registration endpoint (POST /api/auth/register):
- Receive username, email, password
- Validate parameters (username 3-20 characters, email format correct, password at least 6 characters)
- Check if username and email already exist
- Encrypt password with bcrypt
- Save to database
- Return success message

Login endpoint (POST /api/auth/login):
- Receive username, password
- Verify user exists
- Verify password is correct
- Generate JWT token (validity 7 days)
- Return token and user information
```

This prompt describes the functional requirements for two endpoints in detail. AI will implement complete registration and login logic, including parameter validation, password encryption, JWT generation, etc.

Fourth step, implement article CRUD:

```
Implement article CRUD functionality:

Create article (POST /api/posts):
- Requires login (verify JWT token)
- Receive title, content, category, tags, cover
- Get author_id from token
- Save to database
- Return article information

Get article list (GET /api/posts):
- Support pagination (page, pageSize)
- Support category filtering (category)
- Support search (keyword, search title and content)
- Return article list and total count

Get article detail (GET /api/posts/:id):
- Return article detail
- View count +1

Update article (PUT /api/posts/:id):
- Requires login
- Can only update own articles
- Update specified fields

Delete article (DELETE /api/posts/:id):
- Requires login
- Can only delete own articles
```

This prompt includes all article operations. AI will implement complete CRUD functionality, including permission verification, data queries, etc.

4) Develop Frontend with AI

After backend development is complete, you can develop the frontend. It's recommended to first test backend endpoints with Postman or similar tools to ensure they work properly before developing the frontend. This avoids having both frontend and backend problems simultaneously, making it hard to identify where the issue is.

First step, create frontend project:

```
Create React + TypeScript + Vite frontend project, install dependencies like react-router-dom, axios, react-markdown. Configure routes:
- / Homepage (article list)
- /post/:id Article detail
- /write Write article (requires login)
- /profile Profile (requires login)
- /login Login
- /register Register
```

Second step, implement user authentication:

```
Implement user authentication functionality:
1. Create AuthContext to manage login state and user information
2. Store token in localStorage
3. Wrap axios to automatically add token to request headers
4. Create ProtectedRoute component to protect pages requiring login
5. Implement login and registration pages
```

This prompt describes how to implement user authentication. AuthContext is used to manage global login state, ProtectedRoute is used to protect pages that require login to access.

Third step, implement article list page:

```
Implement homepage article list:
1. Fetch article list, display title, cover, category, author, time
2. Support pagination, 10 items per page
3. Support category filtering (category tabs at top)
4. Support search (search box)
5. Click article to navigate to detail page
```

Fourth step, implement article detail page:

```
Implement article detail page:
1. Fetch article detail by ID
2. Use react-markdown to render article content
3. Display author information, publish time, view count
4. If own article, display edit and delete buttons
```

Fifth step, implement write article page:

```
Implement write article page:
1. Use the previously built Markdown editor
2. Input title, select category, add tags, upload cover
3. Edit on left, real-time preview on right
4. Save button calls create article endpoint
5. If in edit mode, load existing article data
```



### Development Tips

When developing full-stack applications, several tips can improve efficiency. First, use environment variables to manage configuration. Sensitive information like database connection strings and JWT secrets should not be hardcoded in code—use environment variables. Create a `.env` file, put configuration in it, then read through `process.env` in code.

Second, handle errors properly. API calls can fail, database operations can error—catch these errors and return friendly messages. You can ask AI to help you create a unified error handling middleware.

Finally, during development use nodemon to automatically restart the backend service, and use Vite's hot reload feature to automatically refresh the frontend page. This way, after modifying code you don't need to manually restart, greatly improving development efficiency.



### Extension Ideas

After completing the basic version, you can continue to extend functionality. For example: add a comment system where users can comment on articles; add a like feature to like favorite articles; support article drafts to save unpublished articles; integrate image upload to upload to cloud storage; add article archiving by month; support RSS subscription for readers to subscribe; optimize SEO so articles are more easily indexed by search engines.



## III. Project Practice - Q&A Community

After completing the blog system, let's challenge ourselves with a more complex project—a Q&A community. A Q&A community is somewhat more complex than a blog system, involving features like questions, answers, likes, and acceptance. Through this project, you can learn how to handle more complex data relationships and user interactions.

This Q&A community needs to support users asking and answering questions. Users can post questions, and other users can answer them. Both questions and answers support likes. Questioners can accept the best answer. The homepage displays a question list, sortable by hot, latest, unsolved, etc. Each question has tags and can be filtered by tag. Users have a points system—asking, answering, and being accepted all earn points.

![](https://pic.yupi.icu/1/demoweb11.png)

The technology stack is similar to the blog system: frontend uses React + TypeScript + Vite, backend uses Node.js + Express, database uses MySQL.



### Development Steps

1) Design Database

The first step in development is designing the database. Create a `database.md` file:

```markdown
# Q&A Community Database Design

## Users Table (users)
- id, username, email, password, avatar
- points: User points
- created_at

## Questions Table (questions)
- id, title, content (Markdown)
- tags: Tags (JSON array)
- author_id: Questioner ID
- views: View count
- answers_count: Answer count
- votes: Like count
- is_solved: Whether solved
- created_at, updated_at

## Answers Table (answers)
- id, content (Markdown)
- question_id: Question ID
- author_id: Answerer ID
- votes: Like count
- is_accepted: Whether accepted
- created_at, updated_at

## Votes Table (votes)
- id, user_id, target_type (question/answer)
- target_id: Target ID
- created_at
```

2) Develop with AI

After designing the database, you can start developing with AI. The development process is similar to the blog system, but note several key points.

The first key point is the points system:

```
Implement points system:
- Post question: -5 points
- Answer question: +10 points
- Answer accepted: +30 points
- Question liked: +5 points
- Answer liked: +10 points

Automatically update user points in corresponding operations.
```

This prompt describes the points rules. AI will automatically handle point changes when implementing features—for example, after a user answers a question, automatically add 10 points to that user.

The second key point is the like feature:

```
Implement like functionality:
- Users can like questions and answers
- Each user can only like the same target once
- After liking, target's votes count +1
- After unliking, votes count -1
- Return whether user has liked the target
```

The like feature must prevent duplicate likes, so it needs to record user like behavior. When returning data, tell the frontend whether the user has already liked, so the frontend can correctly display the like button state.

The third key point is accepting answers:

```
Implement answer acceptance feature:
- Only questioner can accept answers
- Each question can only accept one answer
- After acceptance, question status changes to solved
- Answerer receives points reward
```

This logic should be implemented on the backend to ensure correct permission control.

The fourth key point is question list sorting:

```
Implement multiple sorting for question list:
- Latest: Order by creation time descending
- Hot: Order by like count descending
- Unsolved: Filter questions where is_solved = false
Support filtering by tags.
```



### Development Tips

When developing a Q&A community, several points need attention. First is data consistency—for example, when liking, you need to simultaneously update the likes table and the target's votes count. Either both operations succeed or both fail. You can ask AI to help you implement database transactions to ensure data consistency.

Second is performance optimization. The question list may have a lot of data, so implement pagination well. You can ask AI to help implement paginated queries, returning only one page of data at a time, avoiding loading too much data at once causing page lag.

Additionally, determining like status is important. When returning question or answer lists, tell the frontend whether the current user has already liked, so the frontend can correctly display the like button state (red for liked, gray for not liked).



### Extension Ideas

After completing the basic version, you can continue to extend functionality. For example: add comment functionality to comment on answers; add follow feature to follow interesting questions or users; implement notification system to notify questioners of new answers; optimize search functionality using full-text search to improve search quality; add leaderboard to display points ranking; implement badge system where completing achievements earns badges.



## IV. Project Practice - Online Store

After mastering user interaction and points systems, let's build a project involving transaction processes. An online store is one of the most complex full-stack projects, involving features like product management, shopping cart, and order processing. Through this project, you can learn how to handle e-commerce business logic.

This Mini version store needs to implement basic e-commerce functionality. Product display (list and details), shopping cart (add, delete, modify quantity), order management (create orders, view orders), user address management. No need to implement payment functionality—after order creation, just display as pending payment status. This reduces development difficulty and focuses on core business processes.

![](https://pic.yupi.icu/1/demoweb12.png)

The technology stack is similar to previous projects: frontend uses React + TypeScript + Vite, backend uses Node.js + Express, database uses MySQL.



### Development Steps

1) Design Database

The first step in development is designing the database. Create a `database.md` file:

```markdown
# Online Store Database Design

## Users Table (users)
- id, username, email, password, avatar
- created_at

## Products Table (products)
- id, name, description, price, stock (inventory)
- images: Image URLs (JSON array)
- category: Category
- created_at, updated_at

## Cart Items Table (cart_items)
- id, user_id, product_id, quantity (quantity)
- created_at

## Addresses Table (addresses)
- id, user_id, name (recipient), phone, province, city, district, detail
- is_default: Whether default address
- created_at

## Orders Table (orders)
- id, order_no (order number), user_id, address_id
- total_price: Total price
- status: Status (pending payment, paid, shipped, completed, cancelled)
- created_at, updated_at

## Order Items Table (order_items)
- id, order_id, product_id, quantity, price (price at time of order)
```

2) Develop with AI

After designing the database, you can start developing with AI. The development process is similar to previous projects, but note several key points.

The first key point is shopping cart functionality:

```
Implement shopping cart functionality:

Add to cart (POST /api/cart):
- Receive product_id, quantity
- If cart already has this product, accumulate quantity
- If new product, create new record
- Check if inventory is sufficient

Get cart (GET /api/cart):
- Return cart item list
- Include product details (name, price, images, etc.)
- Calculate total price

Update quantity (PUT /api/cart/:id):
- Update specified item quantity
- Check inventory

Delete item (DELETE /api/cart/:id):
- Delete specified item from cart
```

Shopping cart functionality needs to handle quantity accumulation well, and also check inventory to avoid adding quantities exceeding inventory.

The second key point is order functionality:

```
Implement order functionality:

Create order (POST /api/orders):
- Receive address_id and cart item ID list
- Check if inventory is sufficient
- Calculate total price
- Generate order number (timestamp + random number)
- Create order and order item records
- Deduct inventory
- Clear ordered items from cart
- Use database transaction to ensure data consistency

Get order list (GET /api/orders):
- Return user's order list
- Support filtering by status
- Include order item details

Get order detail (GET /api/orders/:id):
- Return order details
- Include shipping address, order item list

Cancel order (PUT /api/orders/:id/cancel):
- Can only cancel pending payment orders
- Restore inventory
- Update order status to cancelled
```

This prompt includes all order operations. Creating orders is the most complex, involving operations on multiple tables—use database transactions to ensure data consistency.

The third key point is address management:

```
Implement address management functionality:

Add address (POST /api/addresses):
- Receive recipient information
- If set as default address, set other addresses' is_default to false

Get address list (GET /api/addresses):
- Return user's address list
- Default address sorted first

Update address (PUT /api/addresses/:id):
- Update specified address

Delete address (DELETE /api/addresses/:id):
- Delete specified address
- If deleting default address, set first address as default
```



### Development Tips

When developing an e-commerce system, several key points need special attention. First is inventory management—when creating orders, check inventory, and use database transactions when deducting inventory to ensure no overselling occurs. You can ask AI to help you implement optimistic locking or pessimistic locking to handle concurrency issues.

Second is order number generation. Order numbers must be unique—you can use timestamp plus random number, or use the snowflake algorithm. You can ask AI to help you implement an order number generation function.

Additionally, handle the relationship between shopping cart and orders properly. When creating orders, copy product information from the shopping cart to the order items table rather than directly referencing the shopping cart. Because product prices may change, orders should save the price at time of order, ensuring the order amount won't change due to product price changes.

Finally, validate data properly. For example, quantity cannot be negative, price cannot be negative, inventory cannot be negative, etc. You can ask AI to help you add complete parameter validation on the backend to avoid dirty data entering the database.



### Extension Ideas

After completing the basic version, you can continue to extend functionality. For example: add product search and filtering by price, category, sales volume, etc.; add product reviews where users can review purchased products; implement coupon system supporting discounts like spend-X-get-Y-off and percentage discounts; integrate payment functionality to accept Alipay or WeChat Pay; add order shipping tracking to view shipping information; develop merchant backend to manage products and orders; implement product recommendation algorithm to recommend products based on user preferences.



## In Conclusion

Through these 3 full-stack projects, you've learned the complete web application development process: from a simple blog system, to a complex Q&A community, to an online store involving transaction processes. Each project has let you master different business scenarios and technical points.

Full-stack development looks complex, but with the Vibe Coding approach, you'll find it's not as difficult as you imagine. The key is understanding business logic, knowing what functionality to implement, then letting AI help you generate the code. If you want to learn more full-stack development tips and best practices, refer to the Experience & Techniques section of this tutorial.

After mastering full-stack application development, in the next article I'll take you through WeChat Mini Program development, letting your application run within WeChat to reach more users.



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
