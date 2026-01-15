# Cursor + LangChain4j - AI Programming Assistant Project Practice

This is a complete full-stack AI programming assistant project tutorial. This project uses a combination of manual coding + Vibe Coding development—writing Java code to call AI, and using AI tools like Cursor to assist with coding. The focus is on learning how to integrate AI capabilities into Java projects, systematically teaching you almost all mainstream usages and features of the LangChain4j framework. Suitable for students with some Java backend development foundation to quickly get started with AI application development and add AI projects to their resumes.

Estimated learning time: 1 ~ 5 hours.



Hello everyone, I'm Programmer Fish Skin. Now AI application development is basically an essential skill for programmers, significantly increasing competitiveness during job searches. Previously, I used Spring AI to create an [open-source AI Super Agent project](https://github.com/liyupi/yu-ai-agent). This time, I'll help you quickly master another mainstream Java AI application development framework: LangChain4j.

This tutorial is also carefully designed by me. I refuse boring theory—instead, I use a programming assistant project to teach you almost all mainstream LangChain usages and features through practice. After finishing this tutorial, you'll not only learn LangChain, but also directly gain a project experience. Isn't that great?

**This article is nearly 10,000 words, a bit long. I recommend bookmarking it. The video version offers a better experience~**

> Complete video tutorial: https://bilibili.com/video/BV1X4GGziEyr
>
> Project code open source: https://github.com/liyupi/ai-code-helper



## Requirements Analysis

We need to implement an AI programming assistant that can help users answer questions and provide programming learning guidance suggestions, such as:

- Programming learning roadmaps
- Project learning suggestions
- Programmer job-seeking guides
- Common programmer interview questions



![](https://pic.yupi.icu/1/1752027043776-cd6d17ed-175f-4c7e-8b25-aee81a5296b2-20250710114302208.png)



To implement these requirements, we first need to be able to call AI to complete **basic conversation**, and also support implementing **multi-turn conversation memory**. Additionally, if we want to further enhance AI capabilities, we need to let it **use tools** to search online content; we can also let AI answer based on our own **knowledge base**, providing users with resources and experience we've accumulated in the programming field.

![](https://pic.yupi.icu/1/1752028612444-351672a3-3725-4850-82b5-57d63d0ba866.png)

If we were to implement the above features from scratch, it would be quite troublesome. Therefore, we need to use an AI development framework to improve efficiency.

## What is LangChain4j?

Currently mainstream Java AI development frameworks include [Spring AI](https://spring.io/projects/spring-ai) and [LangChain4j](https://docs.langchain4j.dev/intro). They both provide many **ready-to-use APIs** to help you call large models and implement commonly used AI development features, such as what we'll learn today:

- Conversation memory
- Structured output
- RAG knowledge base
- Tool calling
- MCP
- SSE streaming output

Based on my personal experience, many concepts and usages of these two frameworks are similar. They both provide many plugin extensions and support integration with Spring Boot projects. Although there are some coding differences, which is better comes down to personal preference.

**How should you choose in actual development?**

I'll first take you through developing a complete project using LangChain4j, and then reveal the answer—at that point, you'll have your own ideas too.

## AI Application Development

### Creating a New Project

Open the IDEA development tool and create a new Spring Boot project. **Choose Java version 21** (because LangChain4j has a minimum requirement of version 17):

![](https://pic.yupi.icu/1/1751944012715-3ac04ad2-42e9-4c41-b998-a5318050e27c.png)

Choose dependencies. Use Spring Boot version 3.5.x and include Spring MVC and Lombok annotation libraries:

![](https://pic.yupi.icu/1/1751944035875-83da11bb-e5fa-4a19-ae57-9c214cc0f523.png)

After creating the new project, first modify the configuration file suffix to `yml` for easier configuration later:

![](https://pic.yupi.icu/1/1751944110301-93054763-76d8-4686-ac6e-971e81b4acd4.png)

Here I'd suggest creating an `application-local.yml` configuration file, writing sensitive configurations used during development here, and adding it to `.gitignore` to prevent accidental open-sourcing.

### AI Conversation - ChatModel

ChatModel is the most basic concept, responsible for interacting with AI large models.

First, you need to introduce at least one [AI large model dependency](https://mvnrepository.com/artifact/dev.langchain4j/langchain4j-community-dashscope-spring-boot-starter). Here I choose Alibaba Cloud's domestic large model, which provides an integration dependency package with Spring Boot projects, making it quite convenient:

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-community-dashscope-spring-boot-starter</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```

You need to get a large model calling key from [Alibaba Cloud Bailian Platform](https://bailian.console.aliyun.com/?tab=model#/api-key). Be careful not to leak it!

![](https://pic.yupi.icu/1/1752030336360-af14dd92-7708-45dd-8420-fe87727726f3.png)

Back in the project, add large model configuration to the configuration file, specifying the model name and API Key:

```yaml
langchain4j:
  community:
    dashscope:
      chat-model:
        model-name: qwen-max
        api-key: <Your API Key here>
```

You can [choose the model name as needed](https://bailian.console.aliyun.com/?tab=doc#/doc/?type=model). Use qwen-max for best results, or choose qwen-plus which balances effect, speed, and cost.

![](https://pic.yupi.icu/1/1752030577658-2b939caa-cf27-4065-aac5-e4f3234646b6.png)

Besides writing configuration to let Spring Boot automatically build ChatModel, you can also create ChatModel objects yourself through constructors. This approach is more flexible, and in LangChain4j we'll often use this method to construct objects.

```java
ChatModel qwenModel = QwenChatModel.builder()
                    .apiKey("Your API key here")
                    .modelName("qwen-max")
                    .enableSearch(true)
                    .temperature(0.7)
                    .maxTokens(4096)
                    .stops(List.of("Hello"))
                    .build();
```

After having ChatModel, create an AiCodeHelper class, inject the auto-configured qwenChatModel, write simple conversation code, and use Lombok annotations to print output result logs:

```java
@Service
@Slf4j
public class AiCodeHelper {

    @Resource
    private ChatModel qwenChatModel;

    public String chat(String message) {
        UserMessage userMessage = UserMessage.from(message);
        ChatResponse chatResponse = qwenChatModel.chat(userMessage);
        AiMessage aiMessage = chatResponse.aiMessage();
        log.info("AI output: " + aiMessage.toString());
        return aiMessage.text();
    }
}
```

Write a unit test and say hello to AI:

```java
@SpringBootTest
class AiCodeHelperTest {

    @Resource
    private AiCodeHelper aiCodeHelper;

    @Test
    void chat() {
        aiCodeHelper.chat("Hello, I'm Programmer Fish Skin");
    }
}
```

Run the unit test in Debug mode. It runs successfully and you can view the output:

![](https://pic.yupi.icu/1/1751947565712-9e3c0a68-930b-4968-8a54-19eb8beb48c9.png)

If you encounter a lombok error about not finding symbols:

![](https://pic.yupi.icu/1/1751947096901-ca5ec0a7-ecd1-4447-9f7e-b679ad56dcde.png)

You can modify IDEA's annotation processor configuration to use the lombok in your project:

![](https://pic.yupi.icu/1/1751947494173-01ebf704-c87b-4c6b-96a3-58aafccd5458.png)



### Multimodality

Multimodality refers to the ability to simultaneously process, understand, and generate multiple different types of data, such as text, images, audio, video, PDF, etc.

![](https://pic.yupi.icu/1/1752051068307-72038162-f759-4fce-a0d8-0b5eec4cc59e.png)

Using multimodality in LangChain4j is simple—user messages can add images, audio/video, PDF, and other media resources.

![](https://pic.yupi.icu/1/1752031262335-7dda9965-faa8-44e9-8a18-f748549299fa.png)

First, let's write a method that supports passing in custom UserMessage:

```java
public String chatWithMessage(UserMessage userMessage) {
    ChatResponse chatResponse = qwenChatModel.chat(userMessage);
    AiMessage aiMessage = chatResponse.aiMessage();
    log.info("AI output: " + aiMessage.toString());
    return aiMessage.text();
}
```

Then write a unit test, passing in an image:

```java
@Test
void chatWithMessage() {
    UserMessage userMessage = UserMessage.from(
            TextContent.from("Describe the image"),
            ImageContent.from("https://www.codefather.cn/logo.png")
    );
    aiCodeHelper.chatWithMessage(userMessage);
}
```

But the effect isn't ideal. The qwen-max model can't directly view or analyze images:

![](https://pic.yupi.icu/1/1751948068455-4a25e7b7-9186-4148-bf42-de66b10ecef1.png)

![](https://pic.yupi.icu/1/1751949077879-32103f89-88f4-45b0-8609-77bc9ad8403d.png)



This is also the most critical issue with multimodal development currently. Although the coding isn't difficult, the large model itself needs to support multimodality. You can see the [large model capability support table](https://docs.langchain4j.dev/integrations/language-models/) on the LangChain official website, but everything should be based on actual testing.

![](https://pic.yupi.icu/1/1752031226164-9a0cf728-a4d7-4005-8bbf-3f43c0479c01.png)



Currently, the framework's support for multimodality isn't that great either—one careless move and it errors out. So let's just understand this usage for now. Interested students can also implement multimodality using other models like OpenAI.



### System Prompts - SystemMessage

System prompts are hidden instructions that set AI model behavior rules and role positioning. Users typically can't see them directly. The system prompt is equivalent to giving the AI a personality and capability boundaries—telling the AI "Who are you? What can you do?"

Based on our requirements, let's write a system prompt:

```markdown
You are a programming assistant who helps users answer questions related to programming learning and job interviews, and provides suggestions. Focus on 4 directions:
1. Plan clear programming learning roadmaps
2. Provide project learning suggestions
3. Give complete programmer job-seeking guides (like resume optimization, application techniques)
4. Share high-frequency interview questions and interview techniques
Please answer using concise, easy-to-understand language, helping users learn and job hunt efficiently.
```

Programming Navigation students can watch [AI Super Agent Project Episode 3](https://www.codefather.cn/course/1915010091721236482/section/1916676331948027906), which covers prompt optimization techniques.

![](https://pic.yupi.icu/1/1752031662526-ffba01f1-3358-4d6b-a6e3-e293781cc77c.png)

The most direct way to use system prompts is to create a system message and send it to AI together with the user message.

Modify the chat method, code as follows:

```java
private static final String SYSTEM_MESSAGE = """
        You are a programming assistant who helps users answer questions related to programming learning and job interviews, and provides suggestions. Focus on 4 directions:
        1. Plan clear programming learning roadmaps
        2. Provide project learning suggestions
        3. Give complete programmer job-seeking guides (like resume optimization, application techniques)
        4. Share high-frequency interview questions and interview techniques
        Please answer using concise, easy-to-understand language, helping users learn and job hunt efficiently.
        """;

public String chat(String message) {
    SystemMessage systemMessage = SystemMessage.from(SYSTEM_MESSAGE);
    UserMessage userMessage = UserMessage.from(message);
    ChatResponse chatResponse = qwenChatModel.chat(systemMessage, userMessage);
    AiMessage aiMessage = chatResponse.aiMessage();
    log.info("AI output: " + aiMessage.toString());
    return aiMessage.text();
}
```

Run the unit test and converse with AI again. Clearly, the system preset has taken effect:

![](https://pic.yupi.icu/1/1751949397794-26716439-7ccb-46f2-add4-ff299989b10e.png)



### AI Service

Before learning more features, we need to understand LangChain4j's most important development pattern—AI Service, which provides many high-level abstract APIs that are more convenient to use, developing AI applications as services.

#### Using AI Service

First, introduce the langchain4j dependency:

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j</artifactId>
    <version>1.1.0</version>
</dependency>
```

Then create a programming assistant AI Service, using declarative development methods. Write a conversation method, then directly define system prompts through the `@SystemMessage` annotation.

```java
public interface AiCodeHelperService {

    @SystemMessage("You are a programming assistant")
    String chat(String userMessage);
}
```

However, since our prompt is quite long, writing it in the annotation isn't elegant. So let's create a separate file `system-prompt.txt` in the resources directory to store the system prompt.

The `@SystemMessage` annotation supports reading system prompts from files:

```java
public interface AiCodeHelperService {

    @SystemMessage(fromResource = "system-prompt.txt")
    String chat(String userMessage);
}
```

Then we need to write a factory class to create the AI Service:

```java
@Configuration
public class AiCodeHelperServiceFactory {

    @Resource
    private ChatModel qwenChatModel;

    @Bean
    public AiCodeHelperService aiCodeHelperService() {
        return AiServices.create(AiCodeHelperService.class, qwenChatModel);
    }
}
```

Calling the `AiServices.create` method creates an implementation class for the AI Service. The underlying principle uses Java's reflection mechanism to create a proxy object that implements the interface. The proxy object is responsible for converting input and output—for example, converting String-type user message parameters to UserMessage type and calling ChatModel, then converting AI-returned AiMessage type to String type as the return value.

But we don't need to care about so much—just write interfaces and annotations to develop. Do you like this development approach?

Write a unit test, calling our developed AI Service:

```java
@SpringBootTest
class AiCodeHelperServiceTest {

    @Resource
    private AiCodeHelperService aiCodeHelperService;

    @Test
    void chat() {
        String result = aiCodeHelperService.chat("Hello, I'm Programmer Fish Skin");
        System.out.println(result);
    }
}
```

Debug run. Discover that an AI Service proxy class was generated and the system prompt took effect. Isn't this much more convenient than manually splicing system messages before?

![](https://pic.yupi.icu/1/1751953464452-273ae8c5-4354-467e-b14b-668d64c3b1f3.png)

#### Using in Spring Boot Projects

If you think manually calling the create method to create Service is troublesome, in Spring Boot projects you can introduce dependencies:

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-spring-boot-starter</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```

Then add the `@AiService` annotation to the AI Service, and it will automatically create the service instance:

```java
@AiService
public interface AiCodeHelperService {

    @SystemMessage(fromResource = "system-prompt.txt")
    String chat(String userMessage);
}
```

Remember to comment out the previous factory class's @Configuration annotation, otherwise there will be Bean conflicts

Run the unit test again. You can also have a normal conversation:

![](https://pic.yupi.icu/1/1751953748624-64447a00-d43c-4f8e-9fd1-805efa910753.png)

Although this approach is more convenient, it lacks the flexibility of manual construction (you can freely set many parameters). So I recommend still using manual construction. For subsequent features, we'll also implement them based on this AI Service development pattern.

### Conversation Memory - ChatMemory

Conversation memory refers to enabling AI to remember users' previous conversation content and maintain context coherence. This is a core feature of AI applications.

How to implement conversation memory? The most traditional way is to maintain the message list yourself. You not only need to manually add messages, but when there are many messages, you need to consider eviction, and messages from different users need to be isolated. Just thinking about it gives me a headache!

```java
// Implement conversation memory yourself
Map<String, List<Message>> conversationHistory = new HashMap<>();

public String chat(String message, String userId) {
    // Get user history
    List<Message> history = conversationHistory.getOrDefault(userId, new ArrayList<>());

    // Add new user message
    Message userMessage = new Message("user", message);
    history.add(userMessage);

    // Build complete history context
    StringBuilder contextBuilder = new StringBuilder();
    for (Message msg : history) {
        contextBuilder.append(msg.getRole()).append(": ").append(msg.getContent()).append("\n");
    }

    // Call AI API
    String response = callAiApi(contextBuilder.toString());

    // Save AI reply to history
    Message aiMessage = new Message("assistant", response);
    history.add(aiMessage);
    conversationHistory.put(userId, history);

    return response;
}
```

#### Using Conversation Memory

LangChain4j provides us with ready-to-use `MessageWindowChatMemory` conversation memory, storing up to N messages, with excess messages automatically evicted. After creating conversation memory, set chatMemory when constructing AI Service:

```java
@Configuration
public class AiCodeHelperServiceFactory {

    @Resource
    private ChatModel qwenChatModel;

    @Bean
    public AiCodeHelperService aiCodeHelperService() {
        // Conversation memory
        ChatMemory chatMemory = MessageWindowChatMemory.withMaxMessages(10);
        AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
                .chatModel(qwenChatModel)
                .chatMemory(chatMemory)
                .build();
        return aiCodeHelperService;
    }
}
```

Write a unit test to test whether conversation memory works:

```java
@Test
void chatWithMemory() {
    String result = aiCodeHelperService.chat("Hello, I'm Programmer Fish Skin");
    System.out.println(result);
    result = aiCodeHelperService.chat("Hello, who am I again?");
    System.out.println(result);
}
```

Debug run the unit test. You can see the message list stored in conversation memory:

![](https://pic.yupi.icu/1/1751954519469-e2f60419-ad5d-41fd-945d-c13d9861fe0f.png)

View the output results. Conversation memory has taken effect:

![](https://pic.yupi.icu/1/1751954654615-b4efd4d5-b87a-4980-9c65-0e252c4dd379.png)

#### Advanced Usage

Conversation memory is by default stored in memory and will be lost after restart. You can customize the implementation class of the [ChatMemoryStore](https://docs.langchain4j.dev/tutorials/chat-memory#persistence) interface to save messages to other data sources like MySQL.

![](https://pic.yupi.icu/1/1752040734375-fa8362f4-c2d2-4ecd-9f3d-f328f0459b58.png)

If you have multiple users and want to isolate messages between each user, you can add a memoryId parameter and annotation to the conversation method, passing in memoryId when calling the conversation (similar to chat room room numbers):

```java
String chat(@MemoryId int memoryId, @UserMessage String userMessage);
```

When constructing AI Service, you can specify **creating separate conversation memory for each memoryId** through chatMemoryProvider:

```java
// Construct AI Service
AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
        .chatModel(qwenChatModel)
        .chatMemoryProvider(memoryId -> MessageWindowChatMemory.withMaxMessages(10))
        .build();
```



### Structured Output

Structured output refers to converting the text output returned by large models into structured data formats, such as a JSON, an object, or a complex object list.

![](https://pic.yupi.icu/1/1752051496139-a403e8ad-9b0d-4b1c-924a-cd572f872b05.png)

There are 3 implementation methods for structured output:

- Using large model JSON schema
- Using Prompt + JSON Mode
- Using Prompt

The default is Prompt mode, which is **appending content** to the original user prompt to specify that the large model forcibly outputs JSON text containing specific fields:

```markdown
You are a professional information extraction assistant. Please extract person information from the given text,
and strictly return results in the following JSON format:

{
    "name": "Person's name",
    "age": Age number,
    "height": Height (meters),
    "married": true/false,
    "occupation": "Occupation"
}

Important rules:
1. Only return JSON format, don't add any explanations
2. If information is unclear, use null
3. age must be a number, not a string
4. married must be a boolean value
```

Interested students can [read this article](https://glaforge.dev/posts/2024/11/18/data-extraction-the-many-ways-to-get-llms-to-spit-json-content/) to learn more. However, we don't need to care about these during development—just modify the return value of the conversation method, and the framework will automatically help us implement structured output. Very satisfying!

![](https://pic.yupi.icu/1/1752051189479-456a7016-ab27-4a18-8927-088724ac5ddb.png)

For example, let's add a method to **have AI generate a learning report**. AI needs to output a learning report object containing a name and a suggestion list:

```java
@SystemMessage(fromResource = "system-prompt.txt")
Report chatForReport(String userMessage);

// Learning report
record Report(String name, List<String> suggestionList){}
```

Write a unit test:

```java
@Test
void chatForReport() {
    String userMessage = "Hello, I'm Programmer Fish Skin, I've been learning programming for two and a half years. Please help me create a learning report";
    AiCodeHelperService.Report report = aiCodeHelperService.chatForReport(userMessage);
    System.out.println(report);
}
```

Run the unit test. The effect is quite good:

![](https://pic.yupi.icu/1/1751955304297-a26adf70-eda0-4ebc-ae2e-aa5a8e67cf02.png)

If you find that AI sometimes can't generate accurate JSON, you can use JSON Schema mode, directly constraining the LLM's output format in the request. This is currently the most reliable and highest-precision structured output implementation.

```java
ResponseFormat responseFormat = ResponseFormat.builder()
        .type(JSON)
        .jsonSchema(JsonSchema.builder()
                .name("Person")
                .rootElement(JsonObjectSchema.builder()
                        .addStringProperty("name")
                        .addIntegerProperty("age")
                        .addNumberProperty("height")
                        .addBooleanProperty("married")
                        .required("name", "age", "height", "married")
                        .build())
                .build())
        .build();
ChatRequest chatRequest = ChatRequest.builder()
        .responseFormat(responseFormat)
        .messages(userMessage)
        .build();
```



### Retrieval-Augmented Generation - RAG

RAG (Retrieval-Augmented Generation) is a hybrid architecture combining information retrieval technology with AI content generation, solving the large model's knowledge timeliness limitations and hallucination problems.

Simply put, RAG is like giving AI a "cheat sheet." Before answering questions, AI first checks a specific knowledge base to acquire knowledge, ensuring answers are based on real materials rather than imagination. Many companies also build their own intelligent customer service based on RAG, using accumulated domain knowledge to reply to users.

The complete RAG workflow is as follows:

![](https://pic.yupi.icu/1/1752052410659-f9a142b9-0c2a-4a99-9c8c-8339970c96eb.png)

Let's practice this. First, I prepared 4 documents and placed them in the `resources/docs` directory:

![](https://pic.yupi.icu/1/1752041906112-ac985734-3a43-44a7-b13d-a1632e426828.png)

LangChain provides 3 RAG implementation methods, which I call: minimalist version, standard version, and advanced version.

#### Minimalist RAG

**The minimalist version is suitable for quickly viewing effects**. First, you need to introduce additional dependencies, which include built-in offline Embedding models that work out of the box:

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-easy-rag</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```

Sample code is as follows. Use the built-in document loader to read documents, then use the built-in Embedding model to convert documents into vectors and store them in the automatically injected Embedding memory store. Finally, bind the default content retriever to the AI Service.

```java
// RAG
// 1. Load documents
List<Document> documents = FileSystemDocumentLoader.loadDocuments("src/main/resources/docs");
// 2. Use built-in EmbeddingModel to convert text to vectors, then store in auto-injected memory embeddingStore
EmbeddingStoreIngestor.ingest(documents, embeddingStore);
// Construct AI Service
AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
        .chatModel(qwenChatModel)
        .chatMemory(chatMemory)
        // RAG: retrieve matching text segments from memory embeddingStore
        .contentRetriever(EmbeddingStoreContentRetriever.from(embeddingStore))
        .build();
```

You can see that the minimalist version is characterized by "everything by default." In actual development, for better results, I recommend using the standard or advanced version.

#### Standard RAG

Let's try the standard RAG implementation. For better results, we need:

- Load Markdown documents and split them as needed
- Add filename information to Markdown documents
- Customize the Embedding model
- Customize content retriever

Add Embedding model configuration to the Spring Boot configuration file, using Alibaba Cloud's provided `text-embedding-v4` model:

```yaml
langchain4j:
  community:
    dashscope:
      chat-model:
        model-name: qwen-max
        api-key: <You API Key here>
      embedding-model:
        model-name: text-embedding-v4
        api-key: <You API Key here>
```

Create `rag.RagConfig`, write RAG-related code, execute the initial RAG process, and return a customized content retriever Bean:

```java
/**
 * Load RAG
 */
@Configuration
public class RagConfig {

    @Resource
    private EmbeddingModel qwenEmbeddingModel;

    @Resource
    private EmbeddingStore<TextSegment> embeddingStore;

    @Bean
    public ContentRetriever contentRetriever() {
        // ------ RAG ------
        // 1. Load documents
        List<Document> documents = FileSystemDocumentLoader.loadDocuments("src/main/resources/docs");
        // 2. Document splitting: split each document by paragraph, max 1000 characters, overlap max 200 characters each time
        DocumentByParagraphSplitter paragraphSplitter = new DocumentByParagraphSplitter(1000, 200);
        // 3. Custom document loader
        EmbeddingStoreIngestor ingestor = EmbeddingStoreIngestor.builder()
                .documentSplitter(paragraphSplitter)
                // To improve search quality, add document name to each TextSegment
                .textSegmentTransformer(textSegment -> TextSegment.from(
                        textSegment.metadata().getString("file_name") + "\n" + textSegment.text(),
                        textSegment.metadata()
                ))
                // Use specified vector model
                .embeddingModel(qwenEmbeddingModel)
                .embeddingStore(embeddingStore)
                .build();
        // Load documents
        ingestor.ingest(documents);
        // 4. Custom content retriever
        ContentRetriever contentRetriever = EmbeddingStoreContentRetriever.builder()
                .embeddingStore(embeddingStore)
                .embeddingModel(qwenEmbeddingModel)
                .maxResults(5) // Maximum 5 retrieval results
                .minScore(0.75) // Filter out results with score less than 0.75
                .build();
        return contentRetriever;
    }
}
```

Then bind the content retriever when building AI Service:

```java
@Resource
private ContentRetriever contentRetriever;

@Bean
public AiCodeHelperService aiCodeHelperService() {
    // Conversation memory
    ChatMemory chatMemory = MessageWindowChatMemory.withMaxMessages(10);
    // Construct AI Service
    AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
            .chatModel(qwenChatModel)
            .chatMemory(chatMemory)
            .contentRetriever(contentRetriever) // RAG retrieval augmented generation
            .build();
    return aiCodeHelperService;
}
```

Write a unit test:

```java
@Test
void chatWithRag() {
    Result<String> result = aiCodeHelperService.chatWithRag("How do I learn Java? What are some common interview questions?");
    System.out.println(result.content());
    System.out.println(result.sources());
}
```

Debug run. You can see the split document segments, with some document segments having overlapping content:

![](https://pic.yupi.icu/1/1751962218145-1291831b-be55-44d8-9d73-af3e4bbe3dff.png)

You can see the actually sent, enhanced Prompt in conversation memory:

![](https://pic.yupi.icu/1/1751962545347-a358cb1b-94d8-47ec-b9e1-c72234aeff4a.png)

![](https://pic.yupi.icu/1/1751962597654-e87d90cc-3240-4982-9c8e-a5228468b1e7.png)

The answer effect also meets expectations:

![](https://pic.yupi.icu/1/1751962714819-a74a07e9-2f0b-44ce-b4ee-db4a4041966c.png)



#### Getting Cited Source Documents

If we can display answer sources below AI's responses, it's easier to increase content credibility:

![](https://pic.yupi.icu/1/1752042954244-609fbce6-beb7-4d4b-87a5-c26cd3b8bb9a.png)

In LangChain4j, implementing this feature is simple. Add a method to AI Service, wrap the original return type with a Result class, and you can get the wrapped result, from which you can obtain RAG-cited source documents, Token consumption, etc.

```java
@SystemMessage(fromResource = "system-prompt.txt")
Result<String> chatWithRag(String userMessage);
```

Modify the unit test, output more information:

```java
@Test
void chatWithRag() {
    Result<String> result = aiCodeHelperService.chatWithRag("How do I learn Java? What are some common interview questions?");
    String content = result.content();
    List<Content> sources = result.sources();
    System.out.println(content);
    System.out.println(sources);
}
```

Execution result as shown. We obtained cited source document information:

![](https://pic.yupi.icu/1/1751973326587-f0a61ddc-a0b7-4eb8-949b-d19e257262fc.png)

#### Advanced RAG

This is a set of standard RAG implementations. Most of the time, the standard version is sufficient. The advanced version is more flexible, additionally supporting query transformers, query routing, content aggregators, content injectors, and other features, pipeline the entire RAG workflow (RAG pipeline).

![](https://pic.yupi.icu/1/1752043947317-362c8de1-26e4-4657-ada0-fb414a2dab13.png)

After defining the RAG workflow, finally provide it to AI Service through RetrievalAugmentor:

```java
AiServices.builder(xxx.class)
    ...
    .retrievalAugmentor(retrievalAugmentor)
    .build();
```

Additionally, previously we used in-memory vector storage, which requires reloading documents and calling the embedding model every startup, which is quite time-consuming. So in actual development, I recommend using independent storage. [Officially supports many third-party storage](https://docs.langchain4j.dev/integrations/embedding-stores/). Personally, I quite recommend PG Vector—install a plugin on the original relational database to support vector storage, and it supports many features.

![](https://pic.yupi.icu/1/1752044157711-6b5a9190-93ff-4a97-aa43-c42c519a2a0b.png)

### Tool Calling - Tools

Tool calling can be understood as letting AI large models **borrow external tools** to accomplish things they can't do themselves.

Like humans, if they can't complete work with just their hands and feet, they can use a toolbox.

Tools can be anything, such as web search, calls to external APIs, accessing external data, or executing specific code, etc.

For example, when the user asks "Help me check Shanghai's latest weather," AI itself doesn't have this knowledge. It can call a "check weather tool" to complete the task.

Note that the essence of tool calling **is NOT the AI server calling these tools itself, nor is it sending tool code to the AI server for execution**. It can only make requests, expressing "I need to execute XX tool to complete the task." What actually executes the tools is our own application, which then tells AI the results so it can continue working.

![](https://pic.yupi.icu/1/1752051591909-adecdfe5-87d0-4801-b556-58beea244ebe.png)



The web search capability we need can be implemented through tool calling. Let's refine the requirements here: let AI search interview questions through my [Interview Duck brushing questions website](https://www.mianshiya.com/).

The implementation is simple. Because Interview Duck's search page **supports passing different search keywords through URL parameters**, we just need to use the **Jsoup library** to scrape the question list from Interview Duck's search page.

Good guy, I'm scraping my own site? But everyone, don't try this—you'll easily get banned.

![](https://pic.yupi.icu/1/1752044504400-9b3b8719-dff6-4071-a084-e1236434b0c0.png)



First, introduce the Jsoup library:

```xml
<dependency>
    <groupId>org.jsoup</groupId>
    <artifactId>jsoup</artifactId>
    <version>1.20.1</version>
</dependency>
```

Then write the tool in the `tools` package. You can declare tools with the `@Tool` annotation. Note **you must carefully write descriptions of the tool and tool parameters**, as this directly determines whether AI can correctly call the tool.

```java
@Slf4j
public class InterviewQuestionTool {

    /**
     * Get a list of interview questions related to keywords from the mianshiya.com website
     *
     * @param keyword Search keyword (e.g., "redis", "java multithreading")
     * @return List of interview questions, or error message if failed
     */
    @Tool(name = "interviewQuestionSearch", value = """
            Retrieves relevant interview questions from mianshiya.com based on a keyword.
            Use this tool when the user asks for interview questions about specific technologies,
            programming concepts, or job-related topics. The input should be a clear search term.
            """
    )
    public String searchInterviewQuestions(@P(value = "the keyword to search") String keyword) {
        List<String> questions = new ArrayList<>();
        // Build search URL (encode keyword to support Chinese)
        String encodedKeyword = URLEncoder.encode(keyword, StandardCharsets.UTF_8);
        String url = "https://www.mianshiya.com/search/all?searchText=" + encodedKeyword;
        // Send request and parse page
        Document doc;
        try {
            doc = Jsoup.connect(url)
                    .userAgent("Mozilla/5.0")
                    .timeout(5000)
                    .get();
        } catch (IOException e) {
            log.error("get web error", e);
            return e.getMessage();
        }
        // Extract interview questions
        Elements questionElements = doc.select(".ant-table-cell > a");
        questionElements.forEach(el -> questions.add(el.text().trim()));
        return String.join("\n", questions);
    }
}
```

Bind tools to AI Service:

```java
// Construct AI Service
AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
        .chatModel(qwenChatModel)
        .chatMemory(chatMemory)
        .contentRetriever(contentRetriever) // RAG retrieval augmented generation
        .tools(new InterviewQuestionTool()) // Tool calling
        .build();
```

Write a unit test to verify the tool's effectiveness:

```java
@Test
void chatWithTools() {
    String result = aiCodeHelperService.chat("What are some common computer network interview questions?");
    System.out.println(result);
}
```

Debug run. Discover that AI called the tool:

![](https://pic.yupi.icu/1/1751964854933-395ecc9e-0fb6-4788-b8e2-ae5ef1d094a7.png)

The tool retrieved a question list:

![](https://pic.yupi.icu/1/1751964893075-84d0ac23-fe02-47c0-95c3-e422d1305448.png)

You can see through Debug that AI Service loaded the tools:

![](https://pic.yupi.icu/1/1751964979312-65f04b40-9554-438b-83ff-025009f30a1c.png)

You can see the tool calling process through conversation memory:

![](https://pic.yupi.icu/1/1751965074185-165ed1b9-a50f-4d21-ae85-b8c439f5065c.png)

Output results meet expectations:

![](https://pic.yupi.icu/1/1751965104933-af4b3181-4dc0-40bb-9ef9-5e1c0e26b389.png)

Previously we only demonstrated the simplest tool definition method—declarative. LangChain4j also provides a programmatic tool definition method, but I believe you won't want to do this (unless you're dynamically creating tools).

![](https://pic.yupi.icu/1/1752045043475-a61743d1-e1ea-4912-bfac-d77ce6e43858.png)

Besides web searching, there are other classic tools, such as file reading/writing, PDF generation, calling terminals, outputting charts, etc. We can develop these ourselves, or directly use tools developed by others through MCP.



### Model Context Protocol - MCP

MCP (Model Context Protocol) is an open standard designed to enhance AI's interaction capabilities with external systems. MCP provides a standardized way for AI to interact with external tools, resources, and services, enabling AI to access the latest data, execute complex operations, and integrate with existing systems.

Think of MCP as the USB interface of AI applications. Just as USB provides a standardized way to connect various external devices and accessories, MCP provides a standardized method for AI models to connect to different data sources and tools.

![](https://pic.yupi.icu/1/1752051649523-398e66d6-87fa-4cc4-8c9d-951939844405.png)

Simply put, through the MCP protocol, AI applications can easily access services provided by others to implement more functions, such as querying geographic locations, operating databases, deploying websites, or even making payments.

Previously, we implemented interview question search through tool calling. Below, let's use MCP to implement **web-wide content search**, which is also a typical MCP application scenario.

First, search for a Web Search service from the MCP service market. I recommend [this one](https://mcp.so/server/zhipu-web-search/BigModel?tab=content), because it provides SSE online calling services, so we don't need to install and start it locally ourselves, which is very convenient.

![](https://pic.yupi.icu/1/1752045285371-fd70d350-80bd-4037-9b57-ff8d3a37ccf5.png)

But also note that using other people's services may require an API Key, generally pay-per-use.

You first need to [get an API Key from the platform official](https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys). We'll use it shortly:

![](https://pic.yupi.icu/1/1752045399400-4e8fe95f-5d5c-47dc-aa6e-4225f2df23aa.png)

Then we need to use this MCP service in our program. The tricky part is that I feel LangChain's support for MCP isn't that great. The official documentation doesn't even mention the MCP dependency package to introduce. I found the dependency from the open-source repository:

![](https://pic.yupi.icu/1/1751967113982-099b0b9a-d5a3-43e0-bdf1-1ccfb8d093b2.png)

Introduce dependency:

```xml
<!-- https://mvnrepository.com/artifact/dev.langchain4j/langchain4j-mcp -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```

Add API Key configuration to the configuration file:

```yaml
bigmodel:
  api-key: <Your Api Key>
```

Create `mcp.McpConfig`, initialize and communicate with the MCP service according to the official development method, and create an McpToolProvider Bean:

```java
@Configuration
public class McpConfig {

    @Value("${bigmodel.api-key}")
    private String apiKey;

    @Bean
    public McpToolProvider mcpToolProvider() {
        // Communicate with MCP service
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("https://open.bigmodel.cn/api/mcp/web_search/sse?Authorization=" + apiKey)
                .logRequests(true) // Enable logging to view more information
                .logResponses(true)
                .build();
        // Create MCP client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .key("yupiMcpClient")
                .transport(transport)
                .build();
        // Get tools from MCP client
        McpToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(mcpClient)
                .build();
        return toolProvider;
    }
}
```

Note that above we called MCP through SSE. If you start MCP service locally through npx or uvx, you need to first install the corresponding tools, and use the following configuration to establish communication:

```java
McpTransport transport = new StdioMcpTransport.Builder()
    .command(List.of("/usr/bin/npm", "exec", "@modelcontextprotocol/server-everything@0.6.2"))
    .logEvents(true) // only if you want to see the traffic in the log
    .build();
```

Apply MCP tools in AI Service:

```java
@Resource
private McpToolProvider mcpToolProvider;

// Construct AI Service
AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
        .chatModel(qwenChatModel)
        .chatMemory(chatMemory)
        .contentRetriever(contentRetriever) // RAG retrieval augmented generation
        .tools(new InterviewQuestionTool()) // Tool calling
        .toolProvider(mcpToolProvider) // MCP tool calling
        .build();
```

Write a unit test:

```java
@Test
void chatWithMcp() {
    String result = aiCodeHelperService.chat("What is Programmer Fish Skin's Programming Navigation?");
    System.out.println(result);
}
```

Execute the unit test. View the search process through logs:

![](https://pic.yupi.icu/1/1751967601320-5242e432-ea07-4038-bc6f-7364aefe3d6a.png)

MCP service takes effect, retrieving content from the web as the answer:

![](https://pic.yupi.icu/1/1751967705158-c4591073-858c-4584-a5ee-7d2ecb5261d6.png)

Currently, the documentation doesn't mention how to develop MCP using LangChain4j, but I also don't recommend developing MCP in Java currently.

### Guardrails

Actually, I think the name "guardrail" isn't great. We can just understand it as an interceptor. There are input guardrails and output guardrails, which can execute additional operations before requesting AI and after receiving AI's response, such as authorization before calling AI, logging after calling AI.

![](https://pic.yupi.icu/1/1752051765814-ca0a709d-216e-4f84-8a05-0a8b9a3a6b66.png)

Let's try it out. Before calling AI, perform sensitive word detection. If the user's prompt contains sensitive words, directly reject.

Create `guardrail.SafeInputGuardrail`, implementing the InputGuardrail interface:

```java
/**
 * Security detection input guardrail
 */
public class SafeInputGuardrail implements InputGuardrail {

    private static final Set<String> sensitiveWords = Set.of("kill", "evil");

    /**
     * Detect whether user input is safe
     */
    @Override
    public InputGuardrailResult validate(UserMessage userMessage) {
        // Get user input and convert to lowercase for case-insensitive matching
        String inputText = userMessage.singleText().toLowerCase();
        // Use regex to split input text into words
        String[] words = inputText.split("\\W+");
        // Iterate through all words, check if sensitive words exist
        for (String word : words) {
            if (sensitiveWords.contains(word)) {
                return fatal("Sensitive word detected: " + word);
            }
        }
        return success();
    }
}
```

LangChain4j provides several quick return methods. Simply put, return success if you want to continue calling AI, otherwise return fatal.

![](https://pic.yupi.icu/1/1751968291132-96a670ce-6551-4726-8c62-045021303af1.png)

Modify AI Service, using input guardrail:

```java
@InputGuardrails({SafeInputGuardrail.class})
public interface AiCodeHelperService {

    @SystemMessage(fromResource = "system-prompt.txt")
    String chat(String userMessage);

    @SystemMessage(fromResource = "system-prompt.txt")
    Report chatForReport(String userMessage);

    // Learning report
    record Report(String name, List<String> suggestionList) {
    }
}
```

Write a unit test, write a prompt containing sensitive words:

```java
@Test
void chatWithGuardrail() {
    String result = aiCodeHelperService.chat("kill the game");
    System.out.println(result);
}
```

Run and view the effect. Input detection is triggered, directly throwing an exception:

![](https://pic.yupi.icu/1/1751968796339-ebf23753-55ad-4123-a4dc-e599859a28a1.png)

If it doesn't contain sensitive words, it passes smoothly.

![](https://pic.yupi.icu/1/1751968877451-3ac9f488-0b78-4c04-a227-3c89b54847c8.png)

Of course, besides input guardrails, you can also write output guardrails to detect AI response results.

### Logging and Observability

Previously, we all viewed running information through Debug, which is not only inconvenient for debugging but also definitely not suitable for production environments.

The official provides [logging](https://docs.langchain4j.dev/tutorials/logging) and [observability](https://docs.langchain4j.dev/tutorials/observability) to help us better debug programs and discover problems.

#### Logging

Enabling logging is simple. When constructing the model, specify enabling, or write Spring Boot configuration directly, supporting printing AI request and response logs.

```java
OpenAiChatModel.builder()
    ...
    .logRequests(true)
    .logResponses(true)
    .build();
langchain4j.open-ai.chat-model.log-requests = true
langchain4j.open-ai.chat-model.log-responses = true
logging.level.dev.langchain4j = DEBUG
```

However, not all ChatModels support this. For example, my testing shows QwenChatModel doesn't support it. In this case, we can only rely on observability.

#### Observability

You can obtain ChatModel call information by customizing a Listener. This is more flexible.

Create `listener.ChatModelListenerConfig`, output requests, responses, and error information:

```java
@Configuration
@Slf4j
public class ChatModelListenerConfig {

    @Bean
    ChatModelListener chatModelListener() {
        return new ChatModelListener() {
            @Override
            public void onRequest(ChatModelRequestContext requestContext) {
                log.info("onRequest(): {}", requestContext.chatRequest());
            }

            @Override
            public void onResponse(ChatModelResponseContext responseContext) {
                log.info("onResponse(): {}", responseContext.chatResponse());
            }

            @Override
            public void onError(ChatModelErrorContext errorContext) {
                log.info("onError(): {}", errorContext.error().getMessage());
            }
        };
    }
}
```

But just defining a Listener doesn't seem to work for QwenChatModel, so we need to manually construct a custom QwenChatModel.

Create `model.QwenChatModelConfig`, construct the ChatModel object and bind the Listener:

```java
@Configuration
@ConfigurationProperties(prefix = "langchain4j.community.dashscope.chat-model")
@Data
public class QwenChatModelConfig {

    private String modelName;

    private String apiKey;

    @Resource
    private ChatModelListener chatModelListener;

    @Bean
    public ChatModel myQwenChatModel() {
        return QwenChatModel.builder()
                .apiKey(apiKey)
                .modelName(modelName)
                .listeners(List.of(chatModelListener))
                .build();
    }
}
```

Then, you can change the name of the originally referenced ChatModel to `myQwenChatModel` to prevent conflicts with the auto-injected ChatModel by Spring Boot.

Call AI again, and you can see a lot of information:

![](https://pic.yupi.icu/1/1751974020940-84059541-3935-4505-b114-6fcc809b04f5.png)

### AI as a Service

至此，AI 的能力基本开发完成，但是目前只支持本地运行，需要编写一个接口提供给前端调用，让 AI 能够成为一个服务。

我们平时开发的大多数接口都是同步接口，也就是等后端处理完再返回。但是对于 AI 应用，特别是响应时间较长的对话类应用，可能会让用户失去耐心等待，因此推荐使用 SSE（Server-Sent Events）技术实现实时流式输出，类似打字机效果，大幅提升用户体验。

#### SSE 流式接口开发

LangChain provides 2 methods to support streaming responses (note that streaming responses don't support structured output).

One method is [TokenStream](https://docs.langchain4j.dev/tutorials/ai-services#streaming). First, let the AI conversation method return TokenStream, then when creating AI Service, specify a streaming chat model StreamingChatModel:

```java
interface Assistant {

    TokenStream chat(String message);
}

StreamingChatModel model = OpenAiStreamingChatModel.builder()
    .apiKey(System.getenv("OPENAI_API_KEY"))
    .modelName(GPT_4_O_MINI)
    .build();

Assistant assistant = AiServices.create(Assistant.class, model);

TokenStream tokenStream = assistant.chat("Tell me a joke");

tokenStream.onPartialResponse((String partialResponse) -> System.out.println(partialResponse))
    .onRetrieved((List<Content> contents) -> System.out.println(contents))
    .onToolExecuted((ToolExecution toolExecution) -> System.out.println(toolExecution))
    .onCompleteResponse((ChatResponse response) -> System.out.println(response))
    .onError((Throwable error) -> error.printStackTrace())
    .start();
```

I personally prefer another method, [using Flux](https://docs.langchain4j.dev/tutorials/ai-services/#flux) instead of TokenStream. Students familiar with reactive programming should be no stranger to Flux, right? Just make the AI conversation method return a Flux reactive object. Sample code:

```java
interface Assistant {

    Flux<String> chat(String message);
}
```

Let's try it. First, introduce the reactive package dependency:

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-reactor</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```

Then add a streaming conversation method to AI Service, here also supporting multi-user conversation memory:

```java
// Streaming conversation
Flux<String> chatStream(@MemoryId int memoryId, @UserMessage String userMessage);
```

Since we need to use a streaming model, we need to add streaming model configuration:

```yaml
langchain4j:
  community:
    dashscope:
      streaming-chat-model:
        model-name: qwen-max
        api-key: <Your Api Key>
```

When constructing AI Service, specify the streaming chat model (auto-inject), and supplement conversation memory provider:

```java
@Resource
private StreamingChatModel qwenStreamingChatModel;

AiCodeHelperService aiCodeHelperService = AiServices.builder(AiCodeHelperService.class)
        .chatModel(myQwenChatModel)
        .streamingChatModel(qwenStreamingChatModel)
        .chatMemory(chatMemory)
        .chatMemoryProvider(memoryId ->
                MessageWindowChatMemory.withMaxMessages(10)) // Each session stores independently
        .contentRetriever(contentRetriever) // RAG retrieval augmented generation
        .tools(new InterviewQuestionTool()) // Tool calling
        .toolProvider(mcpToolProvider) // MCP tool calling
        .build();
```

Finally, write the Controller interface. For convenience in testing, use a Get request here:

```java
@RestController
@RequestMapping("/ai")
public class AiController {

    @Resource
    private AiCodeHelperService aiCodeHelperService;

    @GetMapping("/chat")
    public Flux<ServerSentEvent<String>> chat(int memoryId, String message) {
        return aiCodeHelperService.chatStream(memoryId, message)
                .map(chunk -> ServerSentEvent.<String>builder()
                        .data(chunk)
                        .build());
    }
}
```

Add server configuration, specifying backend port and interface path prefix:

```yaml
server:
  port: 8081
  servlet:
    context-path: /api
```

Start the server, use the CURL tool to test calling:

```bash
curl -G 'http://localhost:8081/api/ai/chat' \
  --data-urlencode 'message=I am Programmer Fish Skin' \
  --data-urlencode 'memoryId=1'
```

You can see the streaming output results:

![](https://pic.yupi.icu/1/1751975773168-c4ddd770-abd7-4555-90b6-8d487630aee4.png)



#### Backend CORS Support

To allow the frontend project to smoothly call backend interfaces, we need to configure cross-origin support in the backend. Create a cross-origin configuration class in the config package. Code as follows:

```java
/**
 * Global cross-origin configuration
 */
@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        // Cover all requests
        registry.addMapping("/**")
                // Allow sending cookies
                .allowCredentials(true)
                // Allow which domains (must use patterns, otherwise * will conflict with allowCredentials)
                .allowedOriginPatterns("*")
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
                .allowedHeaders("*")
                .exposedHeaders("*");
    }
}
```

Note, configuring `.allowedOrigins("*")` together with `.allowCredentials(true)` will cause a conflict, because for security reasons, cross-origin requests cannot simultaneously allow all domain access and send authentication information (like cookies).



## AI-Generated Frontend

Since this project doesn't need very complex pages, we can use AI to quickly generate frontend code, greatly improving development efficiency. Here, Fish Skin uses [mainstream AI development tool Cursor](https://www.cursor.com/), challenging myself to not write a single line of code, generating a frontend project that meets requirements.

### Prompt

First, prepare a detailed prompt. Generally, it needs to include requirements, technology selection, backend interface information, and can also provide some prototype diagrams, backend code, etc.

```markdown
You are a professional frontend developer. Please help me generate corresponding frontend project code based on the following information.

## Requirements

The application is "AI Programming Assistant," helping users answer questions related to programming learning and job interviews, and providing suggestions.

There's only one page, the homepage: the page style is a chat room. Above is the chat history (user information on the right, AI information on the left), below is the input box. Upon entering the page, automatically generate a chat room ID to distinguish different sessions. Call the chat interface through SSE to display conversation content in real time.

## Technology Selection

1. Vue3 project
2. Axios request library

## Backend Interface Information

Interface address prefix: http://localhost:8081/api

## SpringBoot Backend Interface Code

@RestController
@RequestMapping("/ai")
public class AiController {

    @GetMapping("/chat")
    public Flux<ServerSentEvent<String>> chat(int memoryId, String message) {
        return aiCodeHelperService.chatStream(memoryId, message)
                .map(chunk -> ServerSentEvent.<String>builder()
                        .data(chunk)
                        .build());
    }
}
```

Note: If using Windows system, it's best to supplement "you should use Windows-supported commands to complete tasks" in the prompt.



### Development

Create a new frontend project folder `ai-code-helper-frontend` in the project root directory. Use the Cursor tool to open that directory, enter the Prompt and execute. Note to choose Agent mode, Thinking deep thinking model (recommend Claude):

![](https://pic.yupi.icu/1/1751976145149-beefc903-31e1-4a4f-8bbe-edf41a3a4806.png)

Besides source code, Fish Skin here even generated the project introduction document `README.md`. Really satisfying!

![](https://pic.yupi.icu/1/1752025773338-e87a94c7-db0b-4213-9cc8-f643b14f5182.png)

After generating code, open the terminal and execute the `npm run dev` command, or open the `package.json` file and use the Debug button to start the project:

![](https://pic.yupi.icu/1/1752026474929-cd4a7225-1e48-4e95-a08e-6f69ea256d45.png)

### Viewing Effects

After running the frontend project, first verify whether functionality is normal, then verify styles. If functionality is unusable (for example, no reply after sending messages), you can press F12 to open the browser console to view frontend error information, or check the backend project console error information. Analyze specific error information concretely. This involves some frontend-related knowledge. Students who don't understand frontend should ask AI more to help fix bugs. **If you really can't handle it, don't struggle blindly!** Just use Fish Skin's code.

For example, I encountered an error connecting to the backend SSE service. I directly copied the error message to AI to solve it:

![](https://pic.yupi.icu/1/1752025968566-ab2c2d53-59e4-4519-bf55-e07b095f1e5d.png)

Successfully run, view the effect:

![](https://pic.yupi.icu/1/1752026740589-5b4670c8-3f5c-470e-afba-4cfd469c31ee.png)

![](https://pic.yupi.icu/1/1752026767000-6599f85f-5926-4174-a06e-55e30e4df667.png)

After ensuring functionality and styles are problem-free, remember to commit code first (to prevent subsequent pollution from AI-generated code), then you can add more features as needed, such as using Markdown to display AI reply messages.

![](https://pic.yupi.icu/1/1752027043776-cd6d17ed-175f-4c7e-8b25-aee81a5296b2-20250710114303496.png)



## Summary

OK, that's the LangChain4j practical project tutorial. How about it, did everyone learn or "learn waste"?

Back to the question at the beginning: **how should you choose an AI development framework in actual development?**

Take Spring AI and LangChain4j for example—I wonder which framework everyone prefers? I actually prefer Spring AI's development model, and Spring AI currently supports more capabilities. Plus there's domestic Spring AI Alibaba's giant support, better ecosystem, and easier problem-solving when you encounter issues. LangChain4j's advantage is that it can be used independently of Spring projects, with more freedom and flexibility.

However, you only need to focus on learning one of these frameworks. Many concepts and usages are similar:

![](https://pic.yupi.icu/1/1752050425995-3b2b8cf4-ad48-41ec-a1e5-154ae6cd8526.png)




## Recommended Resources

1) Fish Skin AI Navigation Website: [AI Resource Collection, Latest AI News, Free AI Tutorials](https://ai.codefather.cn)

2) Programming Navigation Learning Circle: [Learning Roadmaps, Programming Tutorials, Practical Projects, Job Search Guide, Q&A Discussion](https://www.codefather.cn)

3) Programmer Interview Questions: [Internship/Campus Recruitment/Social Recruitment High-Frequency Topics, Enterprise Real Question Analysis](https://www.mianshiya.com)

4) Programmer Resume Tool: [Professional Templates, Rich Example Sentences, Direct Path to Interview](https://www.laoyujianli.com)

5) 1 on 1 Mock Interview: [Essential for Getting Offers in Internship/Campus Recruitment/Social Recruitment Interviews](https://ai.mianshiya.com)
