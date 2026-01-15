# Product Pricing Strategy Design

> Make users willing to pay for your product



Hello everyone, I'm Fish Skin. Let me ask everyone a question first, if you spent a lot of time making a user-facing product, next which way would you choose to charge users?

Is it direct charging, letting users one-time purchase permanent usage rights of the product?

Or subscription model, letting users purchase product usage rights by month or year?

The above two ways are both mainstream monetization models shared in the previous article. But actually besides these "package payment" product payment mechanisms, there are some more flexible "pay-as-you-go" mechanisms, like points mechanism, package system, single payment, etc.

In this article, I'll use my own AI product as an example to explain a universal design about payment mechanisms — **points mechanism**.

Whether you're using Vibe Coding to do personal projects, or want to make a real product, understanding the points mechanism can help you design more flexible pricing strategies.



## What Is the Points Mechanism?

Different from users directly obtaining products or services through purchasing or time-based subscription (like monthly membership), for the points mechanism, users purchase **virtual points**, then can **as needed** use these points to obtain services.

Believe everyone isn't unfamiliar with this payment mechanism, the diamonds, gold coins, point coupons we top up when playing mobile games are all typical points mechanisms.

![](https://pic.yupi.icu/1/image-20230719131457025.png)

And it's no exaggeration to say, now the vast majority of domestic mobile games will use this mechanism.

Why?



## Why Choose the Points Mechanism?

Here I'll introduce the advantages of the points mechanism from both product and development perspectives.



### Product Perspective

Can think about the advantages of the points mechanism starting from our own perspective, like ask yourself: Under what circumstances would I choose to top up points rather than purchase membership?



#### 1. More Flexible

The foremost reason is definitely more flexible. I can use points to selectively purchase multiple items in the game, like half for equipment, half for lottery draws, thereby bringing myself maximum benefit with the same amount.

Our AI product supports users directly purchasing points, and provides multiple different points packages, users can flexibly use these points for different services like AI chat, AI drawing, etc.

![](https://pic.yupi.icu/1/image-20230719144924694.png)



#### 2. Lower Trial Cost

Before I clearly understand a product's functions, or before I'm "addicted" to a product, I won't easily purchase more expensive membership. But, might be willing to first pay a little money to experience paid functions.

Using the points mechanism provides users with lower trial cost. Compared to directly rejecting users with high prices, first letting users experience the value of paid functions, they might be more willing to continue paying, thereby increasing product revenue.

This approach has an additional benefit: Focus on using the product's functions, rather than flashy marketing tactics (century membership) to attract people, more beneficial to product reputation.

Our AI product also referenced many mobile game tactics, lowest only needs 6 yuan to purchase points.



#### 3. Lower Psychological Cost

Before I spend a higher fixed price to purchase a product, I will definitely consider many aspects: Like how long will I use it? Which functions will I use? Are these functions worth these prices?

The more thinking users need for decision-making, the less fixed the purchase intention.

And using the points mechanism, I don't need to consider much, like just use 1 yuan to top up 10 points, purchase intention will be stronger.

In addition, the points mechanism abstracts price into virtual points, letting users focus more on the purchased product itself rather than monetary expenditure, more natural when consuming points.



#### 4. Increase User Stickiness

The points mechanism can increase user stickiness and retention rate. Once I purchase points, will unconsciously produce the psychology of "I want to spend these points," will continue using this product, thereby further enhancing dependence on this product.

In our AI product, to retain users and cultivate usage habits, supports letting users daily claim a certain amount of points for free, this approach is especially important in product early stage.

![](https://pic.yupi.icu/1/image-20230719145440147.png)



#### 5. Adapt to Diverse Businesses

If a system has many functions, for users, definitely don't want to have independent restrictions on usage of each function, like:

- AI chat remaining 10 times
- AI drawing remaining 5 times
- AI book writing remaining 0 times

If user only wants to use AI book writing function, then compared to buying packaged packages, definitely more hope to directly buy AI book writing times, product needs to support this purchase choice.

And if user wants to simultaneously use AI drawing and AI book writing functions, then definitely more hope to buy a packaged package for these two functions, product also needs to support this purchase choice.

As functions increase, purchase choices that need to be supported will grow exponentially, pricing of various purchase choices will also be increasingly difficult to unify.

And if unify all the above times to "points," then for users it's easier to understand, don't need to care how many times left for each function, don't need to calculate carefully how to buy most cost-effectively, can freely allocate points.

For the company, not only can simplify the pricing process, but also through combining various functions or businesses, achieve overall sales increase. Tencent's Q coin is a typical example, any product under Tencent might attract you to top it up.



### Development Perspective

From a development perspective, I think the points mechanism's biggest advantage lies in **generalization**.

And the benefits brought by generalized design are divided into: unified concept, simplified development, improved scalability.



#### 1. Unified Concept

Don't know if everyone has heard of the KISS principle (Keep It Simple, Stupid), keep it simple, the simpler the better.

In the system development process, the fewer concepts that appear, the more beneficial to system design, development and maintenance.

Compared to letting product's various functions respectively correspond to different usage time limits, using **points** this unified general concept is more convenient for R&D and product students' communication and understanding.

Give an extreme example:

- AI chat function consumes 1 "chat coin"
- AI drawing function consumes 2 "drawing coins"
- AI book writing function consumes 3 "book writing coins"
- User A still has 2 "chat coins", 3 "drawing coins", 9 "book writing coins"
- User A can still use 2 times AI chat, 1 time AI drawing, 3 times AI book writing

Everyone needs to simultaneously pay attention to 3 types of functions and their corresponding virtual coins.

And if unified to the concept of points, the above information is easy to understand:

- AI chat, AI drawing, AI book writing functions respectively consume 1, 2, 3 points
- User A still has 14 points



#### 2. Simplify Development

At the very beginning, because system functions were still relatively few, we planned to separately limit users' usable times for each function. Like users can only use 10 times AI chat, 5 times AI drawing per day.

Then when writing code, need to separately add **specific** verification and statistics logic in both AI chat and AI drawing functions, like:

```java
// AI chat function
void doChat() {
  // Get and verify user's remaining AI chat times
  chatLeftNum = user.getChatLeftNum()
  if (chatLeftNum < 1) {
    throw new Exception("Insufficient AI chat times")
  }
  // Operation successful, AI chat times - 1
  chatLeftNum--;
  chatLeftNum = chatLeftNum - 1;
}

// AI drawing function
void doDraw() {
  // Get and verify user's remaining AI drawing times
  drawLeftNum = user.getDrawLeftNum()
  if (drawLeftNum < 1) {
    throw new Exception("Insufficient AI drawing times")
  }
  // Operation successful, AI drawing times - 1
  drawLeftNum = drawLeftNum - 1;
}
```

In addition, need to store more information in database, like:

| User id | AI chat times | AI drawing times | Other |
| ------- | ------------- | ---------------- | ----- |
| 1       | 1             | 5                | ...   |
| 2       | 2             | 6                | ...   |

As can be imagined, as system function count increases, similar but not completely identical verification logic will be more and more, system will be increasingly difficult to maintain; and database also needs to continuously add new columns, occupy more storage space.

If using the points mechanism, can unify various call time variables (chatLeftNum and drawLeftNum) to points (points), different functions consume different points.

Example code is as follows:

```java
// AI chat function
void doChat() {
  // Get and verify user's remaining points
  points = user.getPoints()
  if (points < 1) {
    throw new Exception("Insufficient AI chat times")
  }
  // Operation successful, points - 1
  points = points - 1;
}

// AI drawing function
void doDraw() {
  // Get and verify user's remaining points
  points = user.getPoints()
  if (points < 2) {
    throw new Exception("Insufficient AI drawing times")
  }
  // Operation successful, points - 2
  points = points - 2;
}
```



Can also unify abstract points verification and consumption logic as common public methods, example code is as follows:

```java
// Check remaining points
// Parameter type represents function
void checkPoints(type) {
  needPoints = 1;
  if (type === "draw") {
    needPoints = 2;
  }
  points = user.getPoints();
  if (points < needPoints) {
    throw new Exception("Insufficient remaining points")
  }
}

// Consume remaining points
// Parameter type represents function
void usePoints(type) {
  needPoints = 1;
  if (type === "draw") {
    needPoints = 2;
  }
  points = user.getPoints();
  // Reduce points
  points = points - needPoints;
}
```



After having these 2 public methods, original code can be simplified to:

```java
// AI chat function
void doChat() {
  checkPoints("chat");
  ...
	usePoints("chat")
}

// AI drawing function
void doDraw() {
	checkPoints("draw");
  ...
	usePoints("draw");
}
```



Of course, this still isn't best practice, because code still contains "hard logic" — distinguishing consumed points based on type.

We can write a json configuration file, specially storing all functions' corresponding points consumption, example code is as follows:

```json
[
  {
    "type": "chat",
    "usePoints": 1
  },
  {
    "type": "draw",
    "usePoints": 2
  },
]
```



Then write a public method, according to function (type) take out corresponding points consumption from that configuration file, example code is as follows:

```java
int getUsePoints(type) {
  list = readJSON("Configuration file")
  for (item : list) {
      if (item.type == type) {
          return item.usePoints;
      }
  }
  return 0;
}
```



Then the common points verification and consumption methods, don't need to write if else anymore!

```java
// Check remaining points
// Parameter type represents function
void checkPoints(type) {
  needPoints = getUsePoints(type);
  points = user.getPoints();
  if (points < needPoints) {
    throw new Exception("Insufficient remaining points")
  }
}

// Consume remaining points
// Parameter type represents function
void usePoints(type) {
  needPoints = getUsePoints(type);
  points = user.getPoints();
  // Reduce points
  points = points - needPoints;
}
```



Afterward if we need to add new functions, only need to add an element in the json configuration file, like:

```json
{
  "type": "writeBook",
  "usePoints": 2
}
```



And no matter how many new functions system adds later, database always only needs to store user's remaining points, don't need to repeatedly add new columns. Greatly simplified development!



#### 3. Improve Scalability

Generally speaking, the more general the logic, the stronger the scalability.

If we don't use the points mechanism, but respectively add corresponding time limits to each function, if we want to further increase time consumption distinction within this function, logic will become more and more complex.

Give an example, AI drawing function also supports additional function image-to-image, if only using AI drawing, consumes 1 time; if want to additionally use image-to-image function, consumes 2 times; then if there are additional functions, consume how many times? Will situation needing to consume 1.5 times appear? If times don't support decimals, what to do?

Very likely system as above logic increases, slowly walks into a dead end, unable to continue expanding new functions.

If using the points mechanism, we can magnify the number's base, like 1 time corresponds to 10 points, this way beneficial for us to set additional points consumption for additional functions. Like AI drawing consumes 20 points, additionally using image-to-image increases 10 points, more beneficial for system expansion.



## Application of Points Mechanism

Because of the above advantages of the points mechanism, our AI product chose it as the main payment system.

Of course, the points mechanism also has disadvantages, like not intuitive enough, value not fixed, etc. And for products where "marketing > value" itself, giving users certain trial cost might instead not have as much sales as membership subscription.

So whether to apply the points mechanism needs comprehensive consideration combining actual situation and product nature.

Like our AI product, simultaneously combines three systems: points mechanism, membership system and package system, providing users with more comprehensive choices. Like users can become members to daily claim more points, enjoy more benefits; can also obtain more points through package discounts; also has the generality and flexibility brought by the points mechanism itself.

In addition, the points mechanism itself is a type of **generalized design**, not only can be used as payment system, but can also be applied to many different scenarios, like:

- In e-commerce platforms, consumers can exchange other products through shopping points.
- In food delivery platforms, users can exchange discount offers through ordering points.
- In education platforms, students can watch courses to get points, used to exchange specific rewards.



## In Conclusion

The points mechanism is a flexible and general pricing strategy design. It not only improves user experience, but also simplifies system development, improves scalability.

Remember these key points:

1. Points mechanism is more flexible, lowers user trial cost and psychological cost
2. Points mechanism can adapt to diverse business needs
3. Points mechanism can unify concepts, simplify development
4. Points mechanism must be used combining actual situation, not omnipotent
5. Can combine points mechanism, membership system, package system and other multiple methods

In the Vibe Coding era, implementing points mechanism code can let AI help you generate. But, how to design reasonable pricing strategy, make users willing to pay for your product, still needs your serious thinking.

Go for it, design pricing strategy that satisfies users! 💪



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
