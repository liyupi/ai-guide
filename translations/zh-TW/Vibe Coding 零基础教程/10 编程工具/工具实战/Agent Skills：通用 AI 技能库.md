# Agent Skills：通用 AI 技能庫

> 讓 AI 快速學會新技能

你好，我是程式員魚皮。

在前面的文章中，我們學習了如何用 AI 生成程式碼。但你可能會發現一些問題：

- AI 生成的介面總是千篇一律的藍紫漸變色
- 每次都要輸入一大段相同的提示詞，太麻煩了
- AI 在某些特定任務上表現不夠專業

有沒有辦法讓 AI 快速學會新技能，變得更專業呢？

這篇文章，我會介紹 **Agent Skills**，Anthropic 推出的 AI 技能系統，可以讓 AI 快速掌握各種專業技能。

⭐️ 推薦觀看影片動畫版，更通俗易懂：[https://bilibili.com/video/BV1T7zzBQEaA](https://www.bilibili.com/video/BV1T7zzBQEaA/)

## 一、沒有 Agent Skills 之前

在了解 Agent Skills 之前，讓我們先看看以前是怎麼解決這些問題的。

假設你正在用 AI 開發網站，為了讓 AI 生成的效果更好，你告訴 AI：

- 介面不要使用藍紫漸變色
- 不要生成一大堆沒用的文件
- 你要遵循公司的程式碼規範

阿巴阿巴，洋洋灑灑幾百字。

![](https://pic.yupi.icu/1/1769306620114-3ddb877f-7e14-4e89-abbe-bcd19c33c9ff.png)

之後每次開發網站時，你都要寫這麼一段又臭又長的提示詞，太麻煩了！

於是聰明的你開始想辦法。

先把常用的提示詞保存到單獨的文件（比如 `prompts.md`），每次手動投餵給 AI。

![](https://pic.yupi.icu/1/1769306653314-5b3a0f47-eff0-4c1c-9b9c-26139abfee80.png)

然後創建了資源文件夾，把公司的程式碼規範、設計素材都塞進去，告訴 AI 參考這些寫。

![](https://pic.yupi.icu/1/1769306679682-3f1a3eae-893e-4860-b97d-c7f91b111a8b.png)

接著你還寫了一些腳本，讓 AI 生成程式碼後自動執行格式化、運行測試、提交程式碼到 Git。

![](https://pic.yupi.icu/1/1769306691846-4dcf892d-1969-40ae-8e73-b7c5c5c5d018.png)

最後再寫個 `AGENTS.md` 文件，把所有規範和工作流程都寫進去，讓 AI 自動讀取。

你沾沾自喜：嘿嘿，俺這套工作流，堪稱完美！

![](https://pic.yupi.icu/1/1769306725742-e3c9a7e4-f18b-469c-b3d3-78f38ea8a37e.png)

但很快，你發現了問題，隨著規範越寫越多，文件越來越臃腫，每次對話都要佔用很多 AI 上下文空間，浪費 tokens。

![](https://pic.yupi.icu/1/1769306754832-fad954ff-b289-4e02-a714-e5ca7dafc9cc.png)

這時候，Agent Skills 就該登場了！

## 二、什麼是 Agent Skills？

[Agent Skills](https://claude.com/blog/skills) 是 Anthropic 推出的 [一套開放標準](https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/overview)，目的是讓 AI 能夠學習使用各種專業技能，而不用每次都重複輸入提示詞。

![](https://pic.yupi.icu/1/1769306883902-94de7351-58e4-43ae-86da-e017725d59cc.png)

它定義了一種 **封裝 AI 工作流** 的標準：開發者可以把複雜的任務指令、腳本和資源打包成一個 **技能（Skill）**；作為用戶，你只需要安裝這些技能，AI 就能立刻學會這項本事，不用重複造輪子。

簡單來說，它就是給 AI 裝備的 **技能包**。技能包裡有精心設計的提示詞、程式碼腳本、還有各種資源文件。

![](https://pic.yupi.icu/1/1769306811193-2ee3acbc-5e36-46c2-8d08-b2682494fb56.png)

把 AI 想像成一個職場小白，給他裝上 `文件處理技能`，它就立刻知道怎麼生成 PPT、處理 Excel 表格；裝上 `程式碼規範技能`，它就知道怎麼按照公司標準寫程式碼。

![](https://pic.yupi.icu/1/1769306900359-2a2b73da-a366-411d-ad3b-2ae61f6b5bc4.png)

你可能會想：等等，這不就是把教 AI 做事的文件和 AI 要用到的文件打包成文件夾嗎？

![](https://pic.yupi.icu/1/1769306918453-1b2d34df-db49-4932-88cd-89eec0c9f773.png)

沒錯，差不多就是這個意思。但 Anthropic 把它做成了一個通用標準，而且在實現原理上有一些新花樣。下面我們先來實戰使用一下 Agent Skills，再揭秘其中的奧秘。

## 三、Agent Skills 入門實戰

目前對 Agent Skills 支持最完善的工具是 Anthropic 官方的 [Claude Code](https://claude.com/product/claude-code)，我們就以此為例，安裝並使用 Skills。

![](https://pic.yupi.icu/1/1769306959992-8489754c-6a63-4685-b804-f27836e92df8.png)

### 1、安裝 Skills 技能

先打開 Claude Code 並輸入命令，添加官方技能市場：

```plain
/plugin marketplace add anthropics/skills
```

![](https://pic.yupi.icu/1/1769307009465-4e04d585-3f68-4fcb-a3b0-ba43ad70139a.png)

這就像是在你的 AI 助手里開通了一個技能商店，接下來你就可以從商店中獲取技能了。

![](https://pic.yupi.icu/1/1769307026089-70a117da-b18e-4c7d-992b-1d08e30a7a0b.png)

在 Claude Code 中輸入命令，安裝官方提供的技能包：

```plain
/plugin install example-skills@anthropic-agent-skills
```

![](https://pic.yupi.icu/1/1769307063576-10e2ce68-b5cd-41c7-8d6c-da0781298929.png)

這個 example-skills 包含了一堆官方示例技能，包括前端設計、網頁測試、動圖製作等等。

![](https://pic.yupi.icu/1/1769307079120-6aaf2999-fee5-4fdb-a5e3-2ba66824b4de.png)

裝完之後，你就可以直接讓 AI 使用這些技能了。

還有另外一種安裝方式，也可以在 Claude Code 中輸入一行命令來安裝 [frontend-design](https://www.claudeskill.site/en/skills/anthropic-agent-skills:frontend-design) 技能。

```markdown
skill install anthropic-agent-skills:frontend-design
```

### 2、前端設計技能

比如你要做一個網站，以前沒裝技能的時候，AI 生成的程式碼又是那個熟悉的藍紫漸變色，千篇一律的 AI 審美。

![](https://pic.yupi.icu/1/1769307096370-df6a9ece-2720-4e1d-b725-431eb4e54afa.png)

現在安裝了 frontend-design 這個 **教 AI 生成專業設計感網站** 的技能後，你輸入：“幫我開發個人作品集網站”。

AI 會主動問你：我發現你安裝了前端設計技能，需要用它來生成更具設計感的頁面嗎？

![](https://pic.yupi.icu/1/1769307135496-aa2a1e4e-4e8a-43e5-a138-9a148410b52e.png)

確認之後，AI 會利用技能生成程式碼，告別藍紫漸變，生成獨特風格的精美頁面。

![](https://pic.yupi.icu/1/1769307161745-c81ca221-9902-49dd-96de-a99d50a17684.png)

我們不用每次都給 AI 輸入一大堆相同的提示詞，裝一次技能就行了。

### 3、文件處理技能

除了程式碼相關的技能，官方還提供了文件處理技能包。

![](https://pic.yupi.icu/1/1769307180929-3b2d4bcf-c1a7-40e0-831d-336c78b9ccb8.png)

同樣在 Claude Code 中輸入一行命令安裝：

```plain
/plugin install document-skills@anthropic-agent-skills
```

![](https://pic.yupi.icu/1/1769307200501-48c05a43-75d0-4cf9-bc4f-3f89554f6295.png)

這個技能包裡有 PPT 製作、Word 文件生成、Excel 數據分析、PDF 解析等技能。

![](https://pic.yupi.icu/1/1769307220369-c4c7889b-6ddc-4f29-8247-9fe02af6d3eb.png)

接下來如果你讓 AI 做個 PPT，它會自動調用 PPT 製作技能，直接生成排版好的 PPT 文件，幫你節省幾個小時。

![](https://pic.yupi.icu/1/1769141161384-f52f68b1-9260-4ae2-bf92-f418673660e6.png)

![](https://pic.yupi.icu/1/1769307245673-c64d081e-09c5-4cee-a3a2-7eaa0e1c98ad.png)

## 四、揭秘 Agent Skills 內部原理

你可能會好奇：為什麼 Skills 能做到安裝即用？技能包裡面到底有啥？AI 又是怎麼知道該用哪個技能的？

[技能](https://agentskills.io/what-are-skills) 其實就是一個包含 `SKILL.md` 技能說明文件的文件夾，還可以包含可執行腳本、資源和參考文件。

![](https://pic.yupi.icu/1/1769307275438-55f0f5fb-b429-43cc-9964-c48486af404e.png)

```markdown
my-skill/
├── SKILL.md          # 必需：指令和元數據
├── scripts/          # 可選：可執行腳本
├── references/       # 可選：參考文件
└── assets/           # 可選：模板和資源
```

由於每個技能的複雜度不同，結構也會存在區別。我們可以在本地目錄中找到已安裝的技能文件夾。

![](https://pic.yupi.icu/1/1769141068658-ef05e94f-380b-4784-b78c-2c588289832a.png)

以官方的 PPT 製作技能為例，它的結構是這樣的：

```plain
skills/pptx/
├── SKILL.md          # 技能說明書（必需）
├── ooxml/            # OOXML 相關資源
├── scripts/          # 處理腳本
├── html2pptx.md      # HTML 轉 PPT 說明
├── ooxml.md          # OOXML 格式說明
└── LICENSE.txt       # 許可證
```

包含一個核心的技能說明文件 `SKILL.md`，還有腳本、參考文件和各種資源文件。

![](https://pic.yupi.icu/1/1769307298133-872126c8-e0b4-4264-8914-33ddea77c83d.png)

而 frontend-design 前端設計技能只有一個 `SKILL.md` 文件。

![](https://pic.yupi.icu/1/1769307312566-e868eead-6723-42e1-80ba-fbffd9976cf2.png)

### SKILL.md 文件結構

`SKILL.md` 文件是每個技能的核心，它包含兩個關鍵部分。

第一部分是 **元數據**，用 YAML 格式寫在文件開頭：

```yaml
---
name: frontend-design
description: 生成具有專業設計感的前端程式碼，避免千篇一律的 AI 審美
---
```

其中 `name` 是技能的名字。`description` 是技能的描述，告訴 AI 什麼時候應該使用這個技能。描述寫得越清晰，AI 就越容易在合適的時機調用它。

![](https://pic.yupi.icu/1/1769307333844-a1c504a9-0bf9-41b0-ac0b-364e4edf881d.png)

第二部分是 **指令內容**，就是一套經過精心設計的提示詞，指導 AI 具體怎麼做。

以 [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) 技能為例，它的指令內容包括：

- 設計思考：在寫程式碼前，先分析產品目的、用戶群體、技術約束，然後選擇一個大膽的美學方向（極簡、復古未來、工業風、有機自然、奢華精緻等）
- 前端美學指南：包括字體選擇（避免 Arial、Inter 等爛大街字體，選擇有個性的組合）、配色主題（主色調配鮮明點綴色）、動效設計、空間構成、背景和視覺細節
- 避坑指南：明確禁止紫色漸變、系統字體、千篇一律的佈局等 AI 審美陷阱

![](https://pic.yupi.icu/1/1769307344477-48419e65-53ea-4cfe-a495-f70be84b2afe.png)

### 漸進式披露機制

如果有多個 Skills，AI 怎麼知道該用哪個技能呢？如果把每個技能說明文件都塞給 AI，不是很佔用上下文麼？

這就要說到 **漸進式披露（Progressive Disclosure）** 這個核心機制了。

當你讓 AI 執行任務時，它會先掃描技能目錄，但不會把所有內容都加載到上下文中。而是只讀取每個技能的元數據（名字和描述），發現描述和任務相關，就知道該用這個技能了。

![](https://pic.yupi.icu/1/1769307378437-dce56ae8-4336-47c1-9ac6-dc39776222c7.png)

然後才把完整的技能說明文件讀進來，按照裡面的指令執行：

![](https://pic.yupi.icu/1/1769307391204-f81c2a91-e21e-46bb-a49f-205196aa7774.png)

並根據需要加載技能包中的其他資源：

![](https://pic.yupi.icu/1/1769307417577-6c55f619-9bf2-43d5-bc76-80f65c3db3c4.png)

**用到哪個查哪個**，既精準匹配又節省上下文，這就是漸進式披露的精髓。

所以 Agent Skills 的本質就是 **把專業知識打包成一個文件夾，讓 AI 按需讀取並使用**。

![](https://pic.yupi.icu/1/1769307432541-5753722e-ba96-404a-b042-c130afb4378f.png)

## 五、跨工具使用 Agent Skills

除了 Claude Code 之外，其他 AI 工具支持 Agent Skills 嗎？

當然！[Agent Skills](https://agentskills.io/) 已經成為通用標準，Cursor、VS Code、Codex 等工具都支持。

![](https://pic.yupi.icu/1/1769307453878-b670716c-f2c7-4eb4-9986-671a7b42b480.png)

Skills 的社區也非常活躍，你可以在 [Claude Skills Hub 市場](https://www.claudeskill.site/zh/skills)、開源的 [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) 等地方找到很多現成的技能。

![](https://pic.yupi.icu/1/1769307598569-a61f88f7-5b26-41fe-a302-652034ed655c.png)

比如有個叫 [UI UX Pro MAX](https://ui-ux-pro-max-skill.nextlevelbuilder.io/) 的技能特別火，專門用於提升 AI 的設計能力。

![](https://pic.yupi.icu/1/1769307611502-fa3224d8-9e04-41cd-848a-de9619edf762.png)

### 在 Cursor 中使用 Agent Skills

用法很簡單，首先按照 [開源倉庫文件](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 的指引，安裝官方提供的命令行工具：

```bash
npm install -g uipro-cli
```

![](https://pic.yupi.icu/1/1769307627168-c682f14b-4517-4325-ad4a-33e88661e714.png)

然後進入到你的項目目錄下，根據使用的 AI 工具執行對應的命令。比如我這裡用 Cursor：

```bash
uipro init --ai cursor
```

![](https://pic.yupi.icu/1/1769307641070-2138ef02-8f26-460a-8cdd-979c59b725de.png)

它會自動把技能安裝到 Cursor 的配置目錄裡。

![](https://pic.yupi.icu/1/1769307669797-86215fbf-b9de-436f-9864-460eb307c5c5.png)

安裝完成後，可以看到它的文件結構：

![](https://pic.yupi.icu/1/1769307694431-c4ad6aa0-b559-4ae5-8573-0687948551f2.png)

接下來，當你讓 AI 開發一個網站時，可以使用斜槓命令手動觸發技能