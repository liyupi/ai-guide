# OpenSpec：輕量規範開發框架

> 讓文件和程式碼始終保持同步



你好，我是程式員魚皮。

在前面的文章中，我們學習了 Spec-kit 規範驅動開發框架。但你可能會覺得 Spec-kit 的流程太複雜了，有沒有更輕量的選擇呢？

這篇文章，我會介紹 **OpenSpec**，一個輕量的規範驅動開發框架，比 Spec-kit 更簡單易用，適合在現有專案上迭代功能。



## 一、什麼是 OpenSpec？

[OpenSpec](https://openspec.dev/) 是一個輕量的規範驅動開發框架，比 Spec-kit 更簡單易用。

它的核心理念是把規範文件作為程式碼庫的一部分，每次改功能都 **先寫變更提案** => 確認後再實現 => 實現完再把變更歸檔到規範文件中，讓文件和程式碼始終保持同步。

![](https://pic.yupi.icu/1/%E6%BC%AB%E7%94%BB%E5%9B%BE6%E5%A4%A7.jpeg)



## 二、快速上手 OpenSpec

讓我通過一個實際例子，帶你快速上手 OpenSpec。

### 1、安裝 OpenSpec

訪問 [OpenSpec 官方倉庫](https://github.com/Fission-AI/OpenSpec/) 查看文件。

首先確保你的電腦安裝了符合要求的 Node.js 版本（比如我這裡要求 Node.js >= 20.19.0），然後全域安裝 OpenSpec CLI：

```bash
npm install -g @fission-ai/openspec@latest
```

進入你的專案目錄，運行初始化命令：

```bash
openspec init
```

初始化過程中會讓你選擇要整合的 AI 工具（比如 Claude Code、Cursor 等），我這裡選擇 Cursor。

![](https://pic.yupi.icu/1/image-20260116163202471.png)

運行命令後，OpenSpec 會自動在你的專案中生成一個 `openspec/` 目錄，裡面包含：

- `openspec/specs/`：存放主規範文件，記錄了專案的完整現狀
- `openspec/changes/`：存放變更提案，記錄了每次修改的計劃
- ⭐️ `openspec/AGENTS.md`：讓 AI 程式設計助手使用 OpenSpec 進行規範驅動開發的操作指南，包含了如何創建變更提案、編寫需求規範、驗證和歸檔變更的完整工作流程。
- `openspec/project.md`：當前專案的上下文說明（用來記錄專案的信息）

![](https://pic.yupi.icu/1/image-20260116164308965.png)

此外，還會根據你選擇的 AI 程式設計工具，生成對應的命令文件，比如 Cursor 的：

![](https://pic.yupi.icu/1/image-20260116173814973.png)

有了這些文件，我們就可以開始規範化的開發流程了。



### 2、標準化開發流程

參考 [官方文件](https://github.com/Fission-AI/OpenSpec/)，主要分為 5 個步驟：

#### 1）Draft 起草變更提案

直接在 AI 程式設計工具中跟 AI 說，讓它創建變更提案。比如我想添加用戶搜索功能：

```markdown
創建一個 OpenSpec 的 change，添加功能：根據名稱和郵箱搜索用戶
```

也可以用 AI 程式設計工具（比如 Claude Code、Cursor）的斜槓命令：

```markdown
/openspec:proposal 添加功能：根據名稱和郵箱搜索用戶
```

![](https://pic.yupi.icu/1/image-20260116171714070.png)

AI 會給這個功能創建一個獨立的目錄 `openspec/changes/add-user-search/`，目錄下創建一系列文件：

- `proposal.md`：描述要改什麼、為什麼改
- `tasks.md`：實施步驟的任務分解
- `specs/…/spec.md`：需求變更的具體內容

![](https://pic.yupi.icu/1/image-20260116171953809.png)



#### 2）Verify & Review 驗證和審查

可以運行下列命令，查看 AI 創建的變更提案是否正確：

```bash
openspec list                        # 查看所有變更
openspec validate add-user-search    # 驗證格式是否正確
openspec show add-user-search        # 查看詳細內容
```

![](https://pic.yupi.icu/1/image-20260116172259055.png)



#### 3）和團隊一起審查提案

如果需要完善，可以繼續跟 AI 對話，比如：

```markdown
你能幫我添加更多搜索條件和限制麼？
```

AI 會更新規範和任務列表，直到大家達成一致。



#### 4）Implement 實現變更

規範確認後，讓 AI 開始實現：

```markdown
規範已經很完美了，開始生成程式碼吧
```

也可以用斜槓命令：

```markdown
/openspec:apply add-user-search
```

AI 會按照 `tasks.md` 中的任務列表逐一實現，並標記完成狀態。

![](https://pic.yupi.icu/1/image-20260116172654371.png)

很快生成完成，AI 的輸出非常整齊，所有改動一目了然：

![](https://pic.yupi.icu/1/image-20260116172905921.png)



#### 5）Archive 歸檔變更

所有任務完成後，讓 AI 歸檔這次變更：

```markdown
請歸檔這次變更
```

也可以用斜槓命令：

```markdown
/openspec:archive add-user-search
```

或者在終端運行：

```bash
openspec archive add-user-search --yes
```

![](https://pic.yupi.icu/1/image-20260116172957759.png)

這個命令會：

- 將變更文件夾移動到 `openspec/changes/archive/` 歸檔區
- 將需求變更自動合併到 `openspec/specs/` 主規範中
- 保持文件和程式碼的同步

![](https://pic.yupi.icu/1/image-20260116174247313.png)

這樣一來，通過 `openspec/changes/` 的歷史記錄，你可以隨時追溯每次變更的來龍去脈。

此外，整個開發過程中，建議大家定期運行 `openspec validate` 驗證命令， 確保規範的完整性。



## 三、OpenSpec 和 Spec-kit 的區別

到這裡，相信大家也能感受到 OpenSpec 和 Spec-kit 的區別了。

- Spec-kit 需要完整的 7 步流程：制定準則 → 寫需求 → 澄清疑問 → 定方案 → 拆任務 → 檢查 → 寫程式碼），適合從 0 開始做大型新專案
- OpenSpec 的流程更簡化：起草提案 → 審查 → 實現 → 歸檔 → 驗證，上手更快，適合在現有專案上迭代功能。

如果你是在現有專案上迭代功能，OpenSpec 會是更好的選擇。如果你是從 0 開始做大型新專案，Spec-kit 的完整流程能幫你打好基礎。



## 寫在最後

看到這裡，相信你已經對 OpenSpec 有了基本的了解。

**OpenSpec 比 Spec-kit 更輕量，更適合日常開發中的功能迭代。**

如果你覺得 Spec-kit 太重，可以試試 OpenSpec。它的流程更簡單，但同樣能保證文件和程式碼的同步，讓團隊協作更順暢。

建議你親自嘗試在專案中使用 OpenSpec，體驗一下規範驅動開發的好處。



## 推薦資源

1）魚皮 AI 導航網站：[AI 資源大全、最新 AI 資訊、免費 AI 教程](https://ai.codefather.cn)

2）程式設計導航學習圈：[學習路線、程式設計教程、實戰專案、求職寶典、交流答疑](https://www.codefather.cn)

3）程式員面試八股文：[實習/校招/社招高頻考點、企業真題解析](https://www.mianshiya.com)

4）程式員寫履歷神器：[專業模板、豐富例句、直通面試](https://www.laoyujianli.com)

5）1 對 1 模擬面試：[實習/校招/社招面試拿 Offer 必備](https://ai.mianshiya.com)