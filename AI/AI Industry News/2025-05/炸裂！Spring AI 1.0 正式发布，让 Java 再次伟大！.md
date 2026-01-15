# 炸裂！Spring AI 1.0 正式发布，让 Java 再次伟大！

炸裂，炸裂，炸裂！从第一次提交代码到现在，经过 2 年的沉淀，Spring AI 框架的第一个正式版本 1.0 终于发布了。

![](https://pic.yupi.icu/1/1747881171718-91ac3eb5-049b-4510-8012-6736c40c9c95.png)

有了这玩意，开发 AI 应用就是洒洒水的事，Java 开发者们是不是又爽了，反正我是很兴奋啊，让 Java 再次伟大！

![](https://pic.yupi.icu/1/1747881641460-856dbbed-0d9d-480c-ad16-8e8dfcccbeb5.png)

但可能很多同学还不知道 Spring AI 能干什么，凭什么这玩意就让 Java 伟大了？

正好我最近刚带编程导航的同学做完一套 AI 超级智能体实战项目，毫不夸张地说，我已经把 Spring AI 玩得 “手拿把掐” 了。

![](https://pic.yupi.icu/1/1747881819511-84f8a2c7-994a-4c1f-b785-584cf3572732.png)

下面我来给大家快速分享一下 Spring AI 的核心能力和魔法。看完之后，我相信你会点赞收藏三连，并且说一句：“伟的太大了”。



## Spring AI 核心特性

### 1、大模型调用能力

大模型调用能力是 AI 应用开发的基础，允许应用程序与各种 AI 大模型进行交互，发送提示词并获取模型的响应。Spring AI 提供了统一的接口来支持各种主流大模型，包括 OpenAI GPT 系列、Claude、通义千问等。

![](https://pic.yupi.icu/1/1747881987603-4021fe3f-ee20-4330-8586-32e46beba8c8.png)

Spring AI 通过配置 + 抽象接口简化了大模型的调用过程，我可以直接在配置中声明多个大模型：

```yaml
spring:
  ai:
    # 阿里大模型
    dashscope:
      chat:
        options:
          model: qwen-max
    # 本地大模型
    ollama:
      base-url: http://localhost:11434
      chat:
        model: gemma3:1b
    # 谷歌大模型
    vertex:
      ai:
        gemini:
          chat:
            options:
              model: gemini-1.5-pro-001
```

然后使用支持链式调用的 ChatClient 灵活地调用各种不同的大模型：

```java
// 使用 Spring AI 调用大模型
@Bean
public ChatClient chatClient(ChatModel chatModel) {
    return ChatClient.builder(chatModel).build();
}

public String doChat(String message) {
    ChatResponse response = chatClient
            .prompt(message)
            .call()
            .chatResponse();
    return response.getResult().getOutput().getText();
}
```

只用一行代码，就能支持 Stream 流式响应，实现打字机效果：

```java
chatClient
    .prompt(message)
    .stream()
```

如果不使用 Spring AI，则需要为每个模型分别实现 API 调用，要自己编写请求、解析响应，很麻烦！

```java
// 不使用 Spring AI 调用大模型
public String chatWithOpenAI(String message) {
    // 配置 OpenAI API
    OkHttpClient client = new OkHttpClient();
    MediaType JSON = MediaType.get("application/json; charset=utf-8");
    
    // 构建请求体
    JSONObject requestBody = new JSONObject();
    requestBody.put("model", "gpt-3.5-turbo");
    JSONArray messages = new JSONArray();
    JSONObject userMessage = new JSONObject();
    userMessage.put("role", "user");
    userMessage.put("content", message);
    messages.put(userMessage);
    requestBody.put("messages", messages);
    
    // 发送请求
    RequestBody body = RequestBody.create(requestBody.toString(), JSON);
    Request request = new Request.Builder()
            .url("https://api.openai.com/v1/chat/completions")
            .header("Authorization", "Bearer " + OPENAI_API_KEY)
            .post(body)
            .build();
            
    try (Response response = client.newCall(request).execute()) {
        String responseBody = response.body().string();
        JSONObject jsonResponse = new JSONObject(responseBody);
        return jsonResponse.getJSONArray("choices")
                .getJSONObject(0)
                .getJSONObject("message")
                .getString("content");
    } catch (Exception e) {
        return "Error: " + e.getMessage();
    }
}
```

Spring AI 不仅提供了统一接口支持多种大模型，让我们可以轻松切换模型而无需修改业务代码。它还支持多模态大模型调用，使 AI 能够同时处理文本、图像、音频等多种输入类型。

我们只需要将图片等资源添加到消息对象中，一起发送给 AI 就可以了，使用 Spring AI 几行代码就能实现：

```java
// 调用多模态模型
String response = ChatClient.create(chatModel).prompt()
    .user(u -> u.text("描述这张图片中的内容")
               .media(MimeTypeUtils.IMAGE_PNG, new ClassPathResource("/yupi.png")))
    .call()
    .content();
```

如果不使用 Spring AI，多模态处理将变得复杂得多：

```java
// 不使用 Spring AI 的多模态实现
public String analyzeImage(String textPrompt, File imageFile) {
    // 读取图像文件并编码为 Base64
    String base64Image = "";
    try {
        byte[] fileContent = Files.readAllBytes(imageFile.toPath());
        base64Image = Base64.getEncoder().encodeToString(fileContent);
    } catch (IOException e) {
        return "Error reading image file: " + e.getMessage();
    }
    
    // 构建请求体，不同模型的格式差异很大
    JSONObject requestBody = new JSONObject();
    requestBody.put("model", "gpt-4-vision-preview");
    
    JSONArray messages = new JSONArray();
    JSONObject userMessage = new JSONObject();
    userMessage.put("role", "user");
    
    // 构建复杂的内容数组
    JSONArray contentArray = new JSONArray();
    
    // 添加文本部分
    JSONObject textContent = new JSONObject();
    textContent.put("type", "text");
    textContent.put("text", textPrompt);
    contentArray.put(textContent);
    
    // 添加图像部分
    JSONObject imageContent = new JSONObject();
    imageContent.put("type", "image_url");
    JSONObject imageUrl = new JSONObject();
    imageUrl.put("url", "data:image/png;base64," + base64Image);
    imageContent.put("image_url", imageUrl);
    contentArray.put(imageContent);
    
    userMessage.put("content", contentArray);
    messages.put(userMessage);
    requestBody.put("messages", messages);
    
    // 发送请求并解析响应...
    // 代码略
}
```

此外，Spring AI 提供了强大的 Advisors 机制，有点类似面向切面编程，可以在模型调用前后添加额外的逻辑，增强 AI 的能力。

举个例子，使用 Spring AI 内置的日志 Advisor，一行代码就能在调用 AI 前后记录日志：

```java
// 使用 Advisors 增强 ChatClient
public String doChatWithAdvisors(String message, String chatId) {
    ChatResponse response = chatClient
            .prompt()
            .user(message)
            // 添加日志 Advisor
            .advisors(new LoggingAdvisor())
            .call()
            .chatResponse();
    return response.getResult().getOutput().getText();
}
```

Advisor 的应用场景还有很多，比如调用 AI 前检查提示词是否安全、得到 AI 响应后保存到数据库中等等。

### 2、提示工程

提示工程（Prompt Engineering）是一门复杂的学问，指通过精心设计提示词，让 AI 更准确地理解用户意图，生成更符合预期的回答，减少幻觉（生成虚假信息）的概率，同时优化 AI 模型的性能表现并节省成本。

Spring AI 通过 Prompt 和 PromptTemplate 类实现提示工程。

Prompt 类可以统一封装多种不同类型的提示词，便于发送给大模型：

```java
// 用户提示词
Message userMessage = new UserMessage(userText);
// 系统提示词
Message systemMessage = new SystemMessage(systemText);
Prompt prompt = new Prompt(List.of(userMessage, systemMessage));
```

利用 PromptTemplate 可以创建支持替换变量的提示词模板，便于提示词的维护和复用：

```java
// 使用 Spring AI 的提示模板
PromptTemplate promptTemplate = new PromptTemplate("你好，我是{name}，我擅长{skill}");
Prompt prompt = promptTemplate.create(Map.of(
    "name", "鱼皮", 
    "skill", "编程"
));
ChatResponse response = chatClient.call(prompt);
```

如果不使用 Spring AI，你就需要手动 / 或者利用工具类来拼接提示词字符串，会更麻烦：

```java
// 不使用 Spring AI 需要手动字符串拼接
String name = "AI 恋爱顾问";
String skill = "解决恋爱问题";
String promptText = "你好，我是" + name + "，我擅长" + skill;
// 还需自行实现条件逻辑、变量转义等
if(hasCondition) {
    promptText += "，我注意到你可能遇到了" + conditionType + "问题";
}
// 调用 API 需自行封装请求
Response response = apiClient.sendPrompt(promptText);
```



### 3、会话记忆

会话记忆（Chat Memory）使 AI 能够保存多轮对话历史，理解上下文，实现连贯对话体验，防止 AI 断片儿。

利用 Spring AI 的 Advisor 机制，一行代码就能轻松开启对话记忆：

```java
// 使用 Spring AI 的会话记忆
public String doChatWithMemory(String message, String chatId) {
    ChatResponse response = chatClient
            .prompt()
            .user(message)
            .advisors(
                // 将对话记忆保存到内存中
                new MessageChatMemoryAdvisor(new InMemoryChatMemory())
            )
            .call()
            .chatResponse();
    return response.getResult().getOutput().getText();
}
```

还可以设置会话 id 实现隔离、设置上下文大小限制等参数：

```java
// 使用 Spring AI 的会话记忆
public String doChatWithMemory(String message, String chatId) {
    ChatResponse response = chatClient
            .prompt()
            .user(message)
            .advisors(
                // 将对话记忆保存到内存中
                new MessageChatMemoryAdvisor(new InMemoryChatMemory())
            )
            .advisors(spec -> spec.param(CHAT_MEMORY_CONVERSATION_ID_KEY, chatId)
                    .param(CHAT_MEMORY_RETRIEVE_SIZE_KEY, 10))
            .call()
            .chatResponse();
    return response.getResult().getOutput().getText();
}
```

Spring AI 会自动处理上下文窗口大小限制，避免超出模型最大 token 限制。

如果不使用 Spring AI，需要手动管理对话历史，代码量一下子就上来了：

```java
// 不使用 Spring AI 的会话记忆实现
Map<String, List<Message>> conversationHistory = new HashMap<>();

public String chat(String message, String userId) {
    // 获取用户历史记录
    List<Message> history = conversationHistory.getOrDefault(userId, new ArrayList<>());
    
    // 添加用户新消息
    Message userMessage = new Message("user", message);
    history.add(userMessage);
    
    // 构建完整历史上下文
    StringBuilder contextBuilder = new StringBuilder();
    for (Message msg : history) {
        contextBuilder.append(msg.getRole()).append(": ").append(msg.getContent()).append("\n");
    }
    
    // 调用 AI API
    String response = callAiApi(contextBuilder.toString());
    
    // 保存 AI 回复到历史
    Message aiMessage = new Message("assistant", response);
    history.add(aiMessage);
    conversationHistory.put(userId, history);
    
    return response;
}
```

Spring AI 的实现非常优秀，将会话存储和保存机制分离，我们可以自己定义 ChatMemory，将对话历史保存到数据库等持久存储中。



### 4、RAG 检索增强生成

RAG（Retrieval-Augmented Generation）是指利用外部知识来增强 AI 生成结果的技术。通过从知识库检索相关信息并注入到提示词中，让 AI 能够利用这些信息生成更准确的回答。

比如我带大家做了一个 AI 恋爱大师应用，给 AI 准备了一套专注于恋爱问答的知识库文档：

![](https://pic.yupi.icu/1/1747884552579-4d8d5873-cbac-4e30-85b4-dc12bd8edbdd.png)

利用 RAG 技术，AI 就能从我自己定义的知识库中获取到特定领域的、最新的信息，不仅能减少大模型的幻觉（防止瞎编内容），还能趁机推荐一波自己的课程，岂不美哉？

所以 AI 的回复也不能完全相信哦~

![](https://pic.yupi.icu/1/1747885198412-cf86e734-d482-490a-925b-896401ce0a3a.png)

RAG 的完整工作流程包括文档收集和切割、向量转换和存储、文档过滤和检索、查询增强和关联 4 大步骤。

![](https://pic.yupi.icu/1/1747884491944-04de44f3-e024-434a-b79b-de61c8e603cd.png)

Spring AI 给 RAG 全流程的实现都提供了支持：

1）文档读取。直接利用 Spring AI 提供的文档加载器，各种类型的文档都能轻松读取：

```java
public List<Document> loadDocuments() {
    List<Document> documents = new ArrayList<>();
    // 加载 Markdown 文档
    Resource resource = resourceLoader.getResource("classpath:documents/knowledge.md");
    MarkdownDocumentReaderConfig config = MarkdownDocumentReaderConfig.builder()
            .withHorizontalRuleCreateDocument(true)
            .withIncludeCodeBlock(true)
            .withAdditionalMetadata("source", "knowledge-base")
            .build();
    MarkdownDocumentReader reader = new MarkdownDocumentReader(resource, config);
    documents.addAll(reader.get());
    return documents;
}
```

2）向量存储。利用 Spring AI 提供的 VectorStore 轻松将文档转换为向量并保存到向量数据库中：

```java
// 创建简单向量存储
SimpleVectorStore vectorStore = SimpleVectorStore.builder(embeddingModel)
        .build();
// 加载文档并存储
List<Document> documents = documentLoader.loadDocuments();
vectorStore.add(documents);
```

3）文档过滤检索 + 查询增强关联。直接使用 QuestionAnswerAdvisor，一行代码就可以让 Spring AI 自动从知识库中检索文档，并将检索到的文档提供给 AI 来增强输出结果。

```java
ChatResponse response = chatClient.prompt()
    .user(question)
    .advisors(new QuestionAnswerAdvisor(vectorStore))
    .call()
    .chatResponse();
```

如果不使用 Spring AI，上述过程的实现可就太复杂了，要自己检索文档、构建提示词等等：

```java
// 不使用 Spring AI 的 RAG 实现
public String generateAnswerWithKnowledge(String query) {
    // 1. 将查询转换为向量
    float[] queryVector = embeddingService.embedText(query);
    
    // 2. 在向量数据库中搜索相似内容
    List<Document> relevantDocs = new ArrayList<>();
    for (Document doc : vectorDatabase.getAllDocuments()) {
        float similarity = calculateCosineSimilarity(queryVector, doc.getVector());
        if (similarity > 0.5) {
            relevantDocs.add(doc);
        }
    }
    relevantDocs.sort((a, b) -> Float.compare(
        calculateCosineSimilarity(queryVector, b.getVector()),
        calculateCosineSimilarity(queryVector, a.getVector())
    ));
    
    // 3. 截取前三个最相关文档
    relevantDocs = relevantDocs.subList(0, Math.min(3, relevantDocs.size()));
    
    // 4. 构建提示词，包含检索到的知识
    StringBuilder prompt = new StringBuilder();
    prompt.append("使用以下信息回答问题:\n\n");
    for (Document doc : relevantDocs) {
        prompt.append("---\n").append(doc.getContent()).append("\n---\n\n");
    }
    prompt.append("问题: ").append(query);
    
    // 5. 调用 AI 生成回答
    return aiService.generateResponse(prompt.toString());
}
```

除了实现基础的 RAG 能力外，Spring AI 还提供了更多高级能力来优化 RAG 的效果。比如提供了完整的 ETL流程的支持，能够快速抽取文档、切分处理文档、并加载到向量存储中。

![](https://pic.yupi.icu/1/1747886114680-591a26a3-6674-475b-9eab-e62c52b04b7c.png)

提供了多查询扩展器，可以为原始提示词生成多个查询变体，提高召回文档的几率：

```java
MultiQueryExpander queryExpander = MultiQueryExpander.builder()
    .chatClientBuilder(chatClientBuilder)
    .numberOfQueries(3)
    .build();
List<Query> queries = queryExpander.expand(new Query("谁是程序员鱼皮？"));
```

提供了查询重写器，可以把原始提示词变得更精确和专业：

```java
public String doQueryRewrite(String prompt) {
    QueryTransformer queryTransformer = RewriteQueryTransformer.builder()
            .chatClientBuilder(builder)
            .build();
    Query query = new Query(prompt);
    // 执行查询重写
    Query transformedQuery = queryTransformer.transform(query);
    // 输出重写后的查询
    return transformedQuery.text();
}
```

效果如图：

![](https://pic.yupi.icu/1/1747886020980-0b6e4da9-f59d-4bf5-aabd-fb03d3a3e795.png)

还支持自定义文档检索器，能够更灵活地定义查询规则，比如按照文档的元信息精确查询、只查询相似度最高的 N 条数据等：

```java
DocumentRetriever retriever = VectorStoreDocumentRetriever.builder()
    .vectorStore(vectorStore)
    .similarityThreshold(0.73)
    .topK(5)
    .filterExpression(new FilterExpressionBuilder()
        .eq("name", "鱼皮")
        .build())
    .build();
```



### 5、工具调用

工具调用（Tool Calling）允许 AI 借助外部工具完成自身无法直接完成的任务，比如网络搜索、文件操作、数据查询等。它扩展了 AI 的能力范围，使 AI 能够获取实时信息、执行实际操作。

工具调用实现的本质是拼接提示词，让 AI 选择要调用哪些工具，然后由程序调用工具并将返回结果交给 AI 进行后续输出。

![](https://pic.yupi.icu/1/1747893550889-cf67c903-5461-43bb-bdf1-d3a497f3e36f.png)

利用 Spring AI，只需要通过注解就能快速定义工具：

```java
// 使用 Spring AI 定义工具
public class WebSearchTool {
    @Tool(description = "Search for information from Baidu Search Engine")
    public String searchWeb(
            @ToolParam(description = "Search query keyword") String query) {
        // 网络搜索实现
        return "搜索结果: " + query + " 的相关信息...";
    }
}
```

然后一行代码就能使用工具，Spring AI 会控制程序和大模型进行交互并自动调用工具，非常方便：

```java
ChatResponse response = chatClient
    .prompt()
    .user(message)
    .tools(new WebSearchTool())
    .call()
    .chatResponse();
```

如果不使用 Spring AI，可就太复杂了！

```java
// 不使用 Spring AI 的工具调用实现
public String handleUserRequest(String userMessage) {
    // 1. 构建含工具定义的提示词
    String toolDefinition = """
        {
            "tools": [
                {
                    "name": "searchWeb",
                    "description": "Search for information from Baidu Search Engine",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query keyword"
                            }
                        },
                        "required": ["query"]
                    }
                }
            ]
        }
        """;
    
    // 2. 调用 AI 判断是否需要工具
    JsonObject aiResponse = callAiWithTools(userMessage, toolDefinition);
    
    // 3. 解析 AI 响应判断是否需调用工具
    if (aiResponse.has("tool_calls")) {
        JsonArray toolCalls = aiResponse.getAsJsonArray("tool_calls");
        
        // 4. 依次执行每个工具
        List<String> toolResults = new ArrayList<>();
        for (JsonElement toolCall : toolCalls) {
            String toolName = toolCall.getAsJsonObject().get("name").getAsString();
            JsonObject args = toolCall.getAsJsonObject().get("arguments").getAsJsonObject();
            
            // 5. 根据工具名执行对应工具
            if ("searchWeb".equals(toolName)) {
                String query = args.get("query").getAsString();
                String result = searchWeb(query); // 实际执行搜索
                toolResults.add(result);
            }
        }
        
        // 6. 将工具结果发回给 AI 生成最终回答
        return callAiWithToolResults(userMessage, toolCalls, toolResults);
    }
    
    return aiResponse.get("content").getAsString();
}
```

此外，Spring AI 提供了工具上下文 ToolContext，可以让程序给工具传递额外参数，实现用户身份认证等功能。还支持直接返回模式（returnDirect），可以绕过大模型直接返回工具结果。



### 6、MCP 模型上下文协议

MCP（Model Context Protocol 模型上下文协议）是一种开放标准，目的是增强 AI 与外部系统的交互能力。MCP 为 AI 提供了与外部工具、资源和服务交互的标准化方式，让 AI 能够访问最新数据、执行复杂操作，并与现有系统集成。

可以将 MCP 想象成 AI 应用的 USB 接口，就像 USB 为设备连接各种外设和配件提供了标准化方式一样，MCP 为 AI 模型连接不同的数据源和工具提供了标准化的方法。从而轻松增强 AI 的能力，有效降低开发者的理解成本，并且打造出 MCP 服务生态。

![](https://pic.yupi.icu/1/1747893881601-d78714c3-812d-4945-8b3f-c5be3b2b0d46.png)

利用 Spring AI，我们可以快速接入别人的 MCP 服务，只需要定义 MCP 服务配置，然后直接通过 Bean 注入 MCP 服务提供的工具即可：

```java
// 使用 Spring AI 的 MCP 客户端
// 1. 在配置文件中定义 MCP 服务
// mcp-servers.json
{
  "mcpServers": {
    "amap-maps": {
      "command": "npx",
      "args": ["-y", "@amap/amap-maps-mcp-server"],
      "env": {"AMAP_MAPS_API_KEY": "你的API密钥"}
    }
  }
}

// 2. 在应用程序中使用 MCP 服务
@Resource
private ToolCallbackProvider toolCallbackProvider;

public String doChatWithMcp(String message) {
    ChatResponse response = chatClient
            .prompt()
            .user(message)
            .tools(toolCallbackProvider) // MCP 服务提供的所有工具
            .call()
            .chatResponse();
    return response.getResult().getOutput().getText();
}
```

当然，开发 MCP 服务也很简单。先利用注解定义工具，然后将工具注册到 MCP 服务中：

```java
// 定义工具
public class ImageSearchTool {
    @Tool(description = "search image from web")
    public String searchImage(@ToolParam(description = "Search query keyword") String query) {
        // 搜索图片，返回结果
        return "https://www.codefather.cn";
    }
}

// 注册 MCP 服务
@Bean
public ToolCallbackProvider imageSearchTools() {
    return MethodToolCallbackProvider.builder()
            .toolObjects(new ImageSearchTool())
            .build();
}
```

如果不使用 Spring AI，你就需要引入 MCP 官方的 SDK 进行开发，或者自主实现，太麻烦了！

```java
// 不使用 Spring AI 的 MCP 实现
public String chatWithExternalTools(String userMessage) {
    // 1. 启动外部 MCP 服务进程
    Process mcpProcess = startMcpProcess("npx", "-y", "@amap/amap-maps-mcp-server");
    
    // 2. 建立与 MCP 服务的通信通道
    InputStream inputStream = mcpProcess.getInputStream();
    OutputStream outputStream = mcpProcess.getOutputStream();
    
    // 3. 发送初始化握手消息
    JsonObject initMessage = new JsonObject();
    initMessage.addProperty("jsonrpc", "2.0");
    initMessage.addProperty("method", "initialize");
    // ... 添加更多初始化参数
    sendMessage(outputStream, initMessage);
    
    // 4. 接收并解析服务提供的工具定义
    JsonObject response = readResponse(inputStream);
    JsonArray toolDefinitions = extractToolDefinitions(response);
    
    // 5. 调用 AI 模型，将工具定义传递给模型
    JsonObject aiResponse = callAiWithTools(userMessage, toolDefinitions);
    
    // 6. 解析 AI 响应，如果需要调用工具则发送给 MCP 服务
    if (aiResponse.has("tool_calls")) {
        JsonArray toolCalls = aiResponse.getAsJsonArray("tool_calls");
        List<String> toolResults = new ArrayList<>();
        
        for (JsonElement toolCall : toolCalls) {
            // 7. 将工具调用请求发送给 MCP 服务
            JsonObject toolRequest = new JsonObject();
            toolRequest.addProperty("jsonrpc", "2.0");
            toolRequest.addProperty("method", "executeFunction");
            // ... 添加工具调用参数
            sendMessage(outputStream, toolRequest);
            
            // 8. 接收 MCP 服务的执行结果
            JsonObject toolResponse = readResponse(inputStream);
            toolResults.add(toolResponse.toString());
        }
        
        // 9. 将工具结果发回给 AI 生成最终回答
        return callAiWithToolResults(userMessage, toolCalls, toolResults);
    }
    
    // 10. 最后关闭 MCP 服务
    mcpProcess.destroy();
    
    return aiResponse.get("content").getAsString();
}
```



## 结尾

以上就是 Spring AI 的核心特性解析，相信大家也感受到使用 Spring AI 开发 AI 应用有多爽了吧！

除了前面提到的之外，Spring AI 还提供了大模型评估测试能力，比如评估 AI 回答与用户输入和上下文的相关性；还提供了全面的可观测性功能，帮助开发者监控 AI 应用的运行状态。

不过目前这些特性还不够成熟，Spring AI 也还有很长一段路要走，后续应该也会推出智能体工作流编排框架吧~

------

就先分享到这里，我全程直播带大家做的 AI 超级智能体新项目今天就完结了，教程中给大家讲解了 Spring AI 几乎所有的特性和高级用法，甚至带大家阅读开源 Manus 项目的源码并且实现了拥有自主规划能力的 AI 智能体，欢迎大家来 [编程导航](https://www.codefather.cn/) 学习。

![](https://pic.yupi.icu/1/1747894887694-cd5e7c53-f777-49ad-ae5a-89252a1ac10d.png)

在我们的 [程序员面试刷题神器 - 面试鸭](https://www.mianshiya.com/) 中也新出了 AI 大模型相关的面试题，每道题目都能让你学到很多知识~

![](https://pic.yupi.icu/1/1747894904199-e795908c-638e-4d29-afd5-c8127db010f3.png)

还有 [鱼皮开源的 AI 知识库](https://github.com/liyupi/ai-guide)，里面有很多值得学习的 AI 干货，持续更新~

获取知识库：https://github.com/liyupi/ai-guide

![](https://pic.yupi.icu/1/1747796993472-c3d3dd64-2ccd-407e-b427-0a7992fec7d0.png)

我们下期见咯！
