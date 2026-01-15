# MCP Service Development Nanny-level Tutorial

> Develop MCP services from scratch



Hello, I'm Fish Skin the programmer.

There's an AI-related concept that's particularly hot called MCP, full name Model Context Protocol. This is an open standard launched by Anthropic, with the goal of providing a unified, standardized interface for large language models and AI assistants, enabling AI to easily operate external tools and complete more complex tasks.

This article will take everyone through MCP quickly, understand its core concepts, and use the interview question search MCP service we developed for our product [Interview Duck](https://www.mianshiya.com/) as an example to lead everyone through hands-on MCP server and client development!

Open source reference: https://github.com/yuyuanweb/mcp-mianshiya-server

![MCP Service](https://pic.yupi.icu/1/1744008993525-16f07f5b-e3b4-4f1a-97dd-ea886c8d945d.png)



## I. Why Is MCP So Important?

Previously, if we wanted AI to process our data, we basically had to rely on pre-trained data or uploading data, which was both troublesome and inefficient. Moreover, even very powerful AI models would have data isolation problems and couldn't directly access new data.

Now, MCP solves this problem. It breaks through the model's dependence on static knowledge bases, giving it stronger dynamic interaction capabilities, able to call search engines like humans, access local files, connect to API services, and even directly operate third-party libraries.

More importantly, as long as everyone follows the MCP protocol, AI can seamlessly connect to local data, internet resources, development tools, productivity software, and even the entire community ecosystem, achieving true "internet of everything." This will greatly improve AI's collaboration and work capabilities, with immeasurable value.

![MCP Architecture](https://pic.yupi.icu/1/1744006127873-09bedb4a-5c7c-4cd0-9c4d-3620f319eac7.png)



## II. MCP Overall Architecture

MCP's core is a "client-server" architecture, where the MCP client host can connect to multiple servers. The client host refers to programs that want to access data through MCP, like Claude Desktop, IDE, or AI tools.

![MCP Architecture Diagram](https://pic.yupi.icu/1/1742979138403-f9f03e19-3537-461e-95d5-6f8a9a413c3a.jpeg)



## III. MCP Development

MCP usage is divided into two modes: STDIO mode (local execution) and SSE mode (remote service).



### MCP Server (Based on stdio Standard Stream)

stdio-based implementation is the most common MCP client solution. It communicates with MCP servers through standard input/output streams. Particularly suitable for locally deployed MCP servers.

**1. Add Dependency**

```xml
<dependency>
  <groupId>org.springframework.ai</groupId>
  <artifactId>spring-ai-mcp-server-spring-boot-starter</artifactId>
  <version>1.0.0-M6</version>
</dependency>
```

**2. Configure MCP Server**

```yaml
spring:
  application:
    name: mcp-server
  main:
    web-application-type: none # Must disable web application type
    banner-mode: off # Disable banner
  ai:
    mcp:
      server:
        stdio: true # Enable stdio mode
        name: mcp-server # Server name
        version: 0.0.1 # Server version
```

**3. Implement MCP Tool**

`@Tool` is the core annotation in Spring AI MCP framework for quickly exposing business capabilities as AI tools. Below is example code:

```java
/**
 * Search Interview Duck interview questions based on search term
 */
@Tool(description = "Search Interview Duck interview questions based on search term")
public String callMianshiya(String searchText) {
    // Execute logic to search questions from Interview Duck database
    System.out.println("User wants to search:" + searchText);
}
```

**4. Register MCP Tool**

```java
@Bean
public ToolCallbackProvider serverTools(MianshiyaService mianshiyaService) {
    return MethodToolCallbackProvider.builder()
             .toolObjects(mianshiyaService)
             .build();
}
```

**5. Run Server**

```bash
mvn clean package -DskipTests
```



### MCP Client (Based on stdio Standard Stream)

**1. Add Dependency**

```xml
<dependency>
  <groupId>org.springframework.ai</groupId>
  <artifactId>spring-ai-mcp-client-spring-boot-starter</artifactId>
  <version>1.0.0-M6</version>
</dependency>
```

**2. Configure MCP Server**

```yaml
spring:
  ai:
    mcp:
      client:
        stdio:
          servers-configuration: classpath:/mcp-servers-config.json
```

Where `mcp-servers-config.json` configuration is as follows:

```json
{
  "mcpServers": {
    "mianshiyaServer": {
      "command": "java",
      "args": [
        "-Dspring.ai.mcp.server.stdio=true",
        "-Dspring.main.web-application-type=none",
        "-Dlogging.pattern.console=",
        "-jar",
        "/yourPath/mcp-server-0.0.1-SNAPSHOT.jar"
      ]
    }
  }
}
```

**3. Initialize Chat Client**

```java
@Bean
public ChatClient initChatClient(ChatClient.Builder chatClientBuilder,
                                 ToolCallbackProvider mcpTools) {
    return chatClientBuilder.defaultTools(mcpTools).build();
}
```

**4. Interface Call**

```java
@PostMapping(value = "/ai/answer")
public String generate(@RequestBody AskRequest request) {
    return chatClient.prompt()
            .user(request.getContent())
            .call()
            .content();
}
```



### MCP Server (Based on SSE)

Besides stdio-based implementation, Spring AI also provides an MCP solution based on Server-Sent Events (SSE). Compared to stdio, SSE is more suitable for remotely deployed MCP servers.

**1. Add Dependency**

```xml
<dependency>
  <groupId>org.springframework.ai</groupId>
  <artifactId>spring-ai-mcp-server-webflux-spring-boot-starter</artifactId>
  <version>1.0.0-M6</version>
</dependency>
```

**2. Configure MCP Server**

```yaml
server:
  port: 8090
spring:
  ai:
    mcp:
      server:
        name: mcp-server
        version: 0.0.1
```

**3. Run Server**

```bash
mvn clean package -DskipTests
java -jar target/mcp-server-0.0.1-SNAPSHOT.jar
```



## IV. Software Using MCP

Besides using programs to call MCP services, MCP servers also support any AI assistant that supports the MCP protocol, like Claude, Cursor, Cherry Studio, etc., all can quickly connect.

Take Cherry Studio as an example:

1. Open Cherry Studio "Settings", click "MCP Servers"

![Cherry Studio Settings](https://pic.yupi.icu/1/1743063238632-2156707f-cfa4-4493-bf3e-68279f3972b9.png)

2. Click "Edit JSON", add MCP configuration to the configuration file

3. In "Settings => Model Service" select a model, check tool function calling feature

4. Enter chat page, check enable MCP service below input box

![Enable MCP](https://pic.yupi.icu/1/1743063248363-b3a09c97-1bb9-4f97-ab0a-2cee5a641c83.png)

Configuration complete. Try searching interview questions, effect is not bad!

![Search Effect](https://pic.yupi.icu/1/1743063251268-145a5d00-4495-49e8-91db-f5536efca436.png)

It even parses interview experiences, returning links to multiple interview questions and answers!

![Interview Experience Analysis](https://pic.yupi.icu/1/1743143537320-1fca3955-3128-42a6-bd32-0cace3bab2ab.png)

Of course, we [Interview Duck Official](https://www.mianshiya.com/) also implemented this feature, helping everyone with interview review:

![Interview Duck Interview Experience Analysis](https://pic.yupi.icu/1/1744008304237-fdfb2b99-9038-43de-94ed-ca0760afdf40.png)



## V. Upload MCP Service

Just like developing an APP, we can also share our completed MCP service to third-party MCP service platforms. Like MCP.so, can be understood as an app store for MCP services.

![MCP.so](https://pic.yupi.icu/1/1744008425870-c5b7958e-98cc-4a14-a4af-cba3af01fcde.png)

Just click the submit button to the left of the avatar, then fill in the MCP service's project address and server configuration example, click submit.

![Submit MCP](https://pic.yupi.icu/1/1744008547763-70effe90-c0aa-4683-bbc8-060639266529.png)

After submission, it can be searched on the platform:

![Search MCP](https://pic.yupi.icu/1/1744008638998-003207ee-8394-4ded-9ea6-83dbf189477c.png)



---



OK, that's all for sharing. If you learned it, remember to like and bookmark. Also welcome everyone to exchange your views and understanding of MCP in the comments~



## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
