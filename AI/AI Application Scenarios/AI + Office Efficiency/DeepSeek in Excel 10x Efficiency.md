## DeepSeek嵌入到Excel，提升10倍工作效率，太牛了！


昨天跟大家分享了DeepSeek的简单用法，有粉丝就问道：能将DeepSeek嵌入到Excel吗？

当然可以了，我们需要借助VBA代码来实现，以下的代码都是由DeepSeek自动生成的，我们还需要调用DeepSeek的API，

实现在A1单元格中输入数据，然后点击按钮执行，在B1单元格中输出结果的效果，我们来看下具体怎么做的

![img](https://pic.yupi.icu/yuyi/1739500999272-ee9397b5-62c2-423d-b53b-695644b46146.webp)

### 一、获取API

首先我们需要获取DeepSeek的API，只需来到官网，右上角点击【API开放平台】，然后在右侧找到【API keys】然后在中间点击【API keys】，就会显示窗口，我们需要为其设置一个名字，然后复制下API，等下需要用到。

![img](https://pic.yupi.icu/yuyi/1739500999275-43b619a8-74ec-4c4a-b0ec-6affe8204823.webp)

### 二、插入VBA代码

打开Excel，按下快捷键ALT+F11，调出VBA的编辑窗口，然后在左侧点击空白的区域，找到【插入】选择【模块】之后将下面的代码粘贴到窗口中

我们需要将【你的API】替换为你刚才获取的API地址

![img](https://pic.yupi.icu/yuyi/1739500999509-195d3321-c3ef-46eb-866e-d667c5a30aaf.webp)

```vbnet
Sub CallDeepSeekAPI()
    Dim question As String
    Dim response As String
    Dim url As String
    Dim apiKey As String
    Dim http As Object
    Dim content As String
    Dim startPos As Long
    Dim endPos As Long
    
    ' 获取 A1 单元格中的问题
    question = ThisWorkbook.Sheets(1).Range("A1").Value
    
    ' 设置 API 的 URL 和 API 密钥
    url = "https://api.deepseek.com/v1/chat/completions" ' 替换为实际的 API URL
    apiKey = "你的API" ' 替换为你的 API 密钥
    
    ' 创建 HTTP 请求对象
    Set http = CreateObject("MSXML2.XMLHTTP")
    
    ' 设置请求头
    http.Open "POST", url, False
    http.setRequestHeader "Content-Type", "application/json"
    http.setRequestHeader "Authorization", "Bearer " & apiKey
    
    ' 设置请求体
    Dim requestBody As String
    requestBody = "{""model"":""deepseek-chat"",""messages"":[{""role"":""user"",""content"":""" & question & """}]}"
    
    ' 发送请求
    http.send requestBody
    
    ' 获取响应
    If http.Status = 200 Then
        response = http.responseText
        
        ' 从 JSON 字符串中提取 content 字段
        startPos = InStr(response, """content"":""") + Len("""content"":""")
        endPos = InStr(startPos, response, """")
        content = Mid(response, startPos, endPos - startPos)
        
        ' 将结果写入 A2 单元格
        ThisWorkbook.Sheets(1).Range("A2").Value = content
    Else
        ' 如果请求失败，显示错误信息
        ThisWorkbook.Sheets(1).Range("A2").Value = "Error: " & http.Status & " - " & http.statusText
    End If
End Sub
```

### 三、设置按钮

点击【开发工具】然后点击【插入】在表单控件中选择【选择】，然后直接新建按钮，将按钮指定给【CallDeepSeekAPI】这个宏即可

到此就设置设置完毕了，只需在A1单元格输入问题，然后点击【按钮】等待一段时间就能得到结果，大家可以动手试一下~

![img](https://pic.yupi.icu/yuyi/1739500999992-c3359cbb-2927-4997-8305-4efcde15be17.gif)



> 来源：https://mp.weixin.qq.com/s/ZD6KRtYPr7gpsPtAiwiLvQ