# Spec-kit：規範驅動開發框架

> 讓 AI 按照專業流程開發專案

你好，我是程式設計師魚皮。

在前面的文章中，我們學習了如何用 AI 快速生成程式碼。但你可能會發現，AI 有時候會 「想到哪寫到哪」，生成的程式碼可能不符合預期，或者專案做到一半就亂套了。

有沒有辦法讓 AI 按照專業的流程來開發專案呢？

這篇文章，我會介紹 **Spec-kit**，一個由 GitHub 推出的規範驅動開發框架，讓 AI 像專業程式設計師一樣工作。

讓我們開始吧！



## 一、什麼是 Spec-kit？

[Spec-kit](https://github.com/github/spec-kit) 是 GitHub 推出的規範驅動開發（SDD）框架。

什麼是規範驅動開發呢？

傳統開發流程是：想到什麼寫什麼，邊寫邊改，最後再補文件。這樣容易導致需求不明確、程式碼和文件對不上。

而規範驅動開發的思路正好相反：**先把需求寫成規範文件，並且把規範文件當作程式碼的唯一真相來源**。你可以把規範文件理解為 "法律條文"，它包含了詳細的需求描述、系統設計和介面定義。AI 必須嚴格遵守這些條文來生成程式碼，確保產出完全符合預期。

![](https://pic.yupi.icu/1/%E6%BC%AB%E7%94%BB%E5%9B%BE4%E5%A4%A7.jpeg)



## 二、快速上手 Spec-kit

讓我通過一個實際例子，帶你快速上手 Spec-kit。

### 1、安裝 Spec-kit

首先打開終端，利用 uvx 命令直接安裝運行 Specify 工具，並初始化一個專案：

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init my-project
```

![](https://pic.yupi.icu/1/image-20260116141308958.png)

選擇你使用的 AI 編程工具，Spec-kit 支援 Claude Code、GitHub Copilot 等幾乎所有主流編程工具。這裡我選 Claude Code：

![](https://pic.yupi.icu/1/image-20260116141507190.png)

根據作業系統選擇腳本類型，Windows 選下面的，其他選上面的：

![](https://pic.yupi.icu/1/image-20260116141537030.png)

執行完這個命令後，會在當前目錄下創建一個 `my-project` 資料夾：

![](https://pic.yupi.icu/1/image-20260116141613246.png)

資料夾裡面包含了這些核心文件：

- `.specify/memory/constitution.md`：專案的基本準則和約定
- `.specify/scripts/`：一些可執行腳本
- `.specify/templates/`：模板文件
- `.claude/commands/`：定義了一套內建的斜槓命令，讓你在 AI 編程工具中可以直接調用

![](https://pic.yupi.icu/1/image-20260116142528820.png)

初始化程式還給了我們一些指引，告訴我們接下來如何運用這些命令來開發專案。

![](https://pic.yupi.icu/1/image-20260116141715310.png)

用 Claude Code 打開這個專案資料夾，就可以在對話中使用定義好的命令了。

![](https://pic.yupi.icu/1/image-20260116142740271.png)



### 2、標準化開發流程

接下來就是標準化的開發流程，參考 [官方文件](https://github.com/github/spec-kit)，主要分為 7 個步驟：

#### 1）Constitution 制定專案準則

運行 `/speckit.constitution` 命令，定義專案的基本原則、程式碼規範、效能標準等。這是專案的 "憲法"，後續所有開發都要遵守。

比如：

```markdown
/speckit.constitution 禁止使用藍紫漸變色風格的 UI
```

💡 如果你要做中文專案，最好在制定專案準則時就明確告訴 AI 「整個網站使用中文」。

![](https://pic.yupi.icu/1/image-20260116160508054.png)

AI 更新了專案準則文件：

![](https://pic.yupi.icu/1/image-20260116160610169.png)

建議每一步我們都用 Git 提交一個版本，這樣出了問題後能及時回滾，也便於我們看到每一步改動的文件。

![](https://pic.yupi.icu/1/image-20260116160745548.png)



#### 2）Specify 編寫功能規範

運行 `/speckit.specify` 命令，描述要做什麼功能、為什麼做、用戶需求是什麼。比如：

```markdown
/speckit.specify 我想做個【自動提醒我喝水的網站】
```

![](https://pic.yupi.icu/1/image-20260116161231223.png)

AI 為這次的需求創建了一個新的 Git 分支，防止污染現有專案。在這個分支下創建了一個需求規格文件（spec.md） + 一個需求檢查文件（requirements.md）。

![](https://pic.yupi.icu/1/image-20260116161307642.png)

需求規格文件非常詳細，還包含了邊緣測試用例，針對用戶各種可能的操作進行處理。

![](https://pic.yupi.icu/1/image-20260116161926017.png)

需求檢查文件中記錄了 AI 對於需求的理解，打勾表示 AI 理解並確認了：

![](https://pic.yupi.icu/1/image-20260116161500358.png)



#### 3）Clarify 釐清不明確的地方（可選）

如果你發現需求檢查文件中有的條目沒有打勾，那你需要通過 Clarify 命令來讓 AI 引導你進一步明確需求，直到所有的條目都打上勾。

運行 `/speckit.clarify` 命令，AI 會提出結構化的問題，讓你來回答。從而幫你填補需求中的空白，比如邊界情況、錯誤處理等。

![](https://pic.yupi.icu/1/image-20260116162702812.png)



#### 4）Plan 制定技術方案

運行 `/speckit.plan` 命令，讓 AI 決定用什麼技術棧、系統架構、資料模型、API 介面等。

![](https://pic.yupi.icu/1/image-20260116163506902.png)

制定技術方案完成，這次生成了一大堆文件，簡單了解一下：

- CLAUDE.md 專案開發指南，記錄技術棧和專案結構，用於指導 Claude Code 接下來如何開發
- quickstart.md 快速入門指南，包含 6 個實施階段和部署方案
- plan.md 實施方案，定義了純客戶端架構、儲存策略、憲法合規性檢查等
- data-model.md 資料模型設計，定義了 4 個核心實體（提醒設定、水量日誌、每日進度、歷史記錄）和儲存結構
- research.md 技術研究文件，記錄了 8 項關鍵技術決策
- contracts/api-contract.md API 介面文件

![](https://pic.yupi.icu/1/image-20260116164021646.png)

接下來，我們就可以準備開發實現了。

![](https://pic.yupi.icu/1/image-20260116163553725.png)



#### 5）Tasks 拆解任務

運行 `/speckit.tasks` 命令，把計劃拆解成可執行的任務列表，並標註依賴關係和優先級。

![](https://pic.yupi.icu/1/image-20260116164537006.png)

生成了一個任務列表文件，每一步要做什麼都非常清晰：

![](https://pic.yupi.icu/1/image-20260116164612533.png)



#### 6）Analyze 分析檢查（可選）

運行 `/speckit.analyze` 命令，檢查規範、計劃、任務是否完整一致，提前發現設計缺陷。

![](https://pic.yupi.icu/1/image-20260116164936733.png)

可以看到，AI 沒有檢查出問題，還讓我自信地進行下一步，真爽死了！



#### 7）Implement 執行實現

最後，運行 `/speckit.implement` 命令，讓 AI 按照任務列表生成程式碼。

![](https://pic.yupi.icu/1/image-20260116170006815.png)

大功告成，看一下效果~

![](https://pic.yupi.icu/1/image-20260116170146827.png)

因為我這裡始終沒有提到使用中文輸出，所以網站內容都是英文的，不過我覺得效果還可以。



## 三、Spec-kit 的優缺點

到這裡，我們已經學會了如何用 Spec-kit 開發完整專案，再複習一下完整流程：

![](https://pic.yupi.icu/1/%25E6%25BC%25AB%25E7%2594%25BB%25E5%259B%25BE5%25E5%25A4%25A7.jpeg)

即使不用 Spec-kit，我們開發完整專案時也可以人工遵循這些步驟。

這種模式最大的好處是 **對齊**。所有人都基於同一份清晰的規範文件工作，大家對需求的理解高度一致，既減少了溝通中的誤解，又能確保程式碼品質。

不過缺點也很明顯，對於小專案，本來直接寫程式碼幾分鐘就能搞定了，上面這套流程走下來差不多要半個小時！

所以這套流程比較適合團隊從 0 開始做完整的新專案，雖然流程比直接寫程式碼慢一些，但能大大降低返工的風險，長遠來看反而更高效。



## 寫在最後

看到這裡，相信你已經對 Spec-kit 有了基本的了解。

**Spec-kit 不是萬能的，但在合適的場景下，它能幫你大幅提升專案品質。**

如果你正在做大型專案、需要團隊協作、對程式碼品質要求高，那麼可以試試 Spec-kit。但如果你只是想寫個簡單的腳本或者快速驗證一個想法，直接讓 AI 生成程式碼會更快。

選擇合適的工具，才能事半功倍。

在接下來的文章中，我會繼續介紹其他規範化開發工具，幫你找到最適合自己的開發方式。



## 推薦資源

1）魚皮 AI 導航網站：[AI 資源大全、最新 AI 資訊、免費 AI 教程](https://ai.codefather.cn)

2）編程導航學習圈：[學習路線、編程教程、實戰專案、求職寶典、交流答疑](https://www.codefather.cn)

3）程式設計師面試八股文：[實習/校招/社招高頻考點、企業真題解析](https://www.mianshiya.com)

4）程式設計師寫履歷神器：[專業模板、豐富例句、直通面試](https://www.laoyujianli.com)

5）1 對 1 模擬面試：[實習/校招/社招面試拿 Offer 必備](https://ai.mianshiya.com)