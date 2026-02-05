# Superpowers：核心技能庫

> 讓 AI 像專業程式設計師一樣工作



你好，我是程式設計師魚皮。

在前面的文章中，我們學習了各種 AI 編程工具和規範化開發框架。但你可能會想：有沒有完整的開發流程，能讓 AI 像專業程式設計師一樣工作呢？

這篇文章，我會介紹 **Superpowers**，一套讓 AI 編程助手變得更專業的軟體開發流程。



## 一、什麼是 Superpowers？

[Superpowers](https://github.com/obra/superpowers) 是一套讓 AI 編程助手變得更專業的 **軟體開發流程**。它不僅為 Claude Code 提供了一套可組合的 **編程技能包**，還提供了規範和指令，確保 AI 能夠正確使用這些技能。

傳統的 AI 編程，你一說需求它就開始劈哩啪啦地寫，結果可能並不是你想要的。而裝了 Superpowers 之後，AI 會先問清楚你到底想做什麼，然後出設計方案讓你確認，接著制定詳細的執行計劃，最後才分步驟去實現，每一步還會自我檢查。

就像給一個剛進公司啥都不懂的 AI 加上了超能力，瞬間讓它有了專業程式設計師的開發習慣。

![](https://pic.yupi.icu/1/%E6%BC%AB%E7%94%BB%E5%9B%BE8%E5%A4%A7.jpeg)



## 二、快速上手 Superpowers

讓我通過一個實際例子，帶你快速上手 Superpowers。

### 1、安裝 Superpowers

參考 [Superpowers 官方文件](https://github.com/obra/superpowers)，在 Claude Code 中執行以下指令安裝。

先註冊市場：

```bash
/plugin marketplace add obra/superpowers-marketplace
```

![](https://pic.yupi.icu/1/image-20260116171109190.png)

再從市場安裝插件：

```bash
/plugin install superpowers@superpowers-marketplace
```

![](https://pic.yupi.icu/1/image-20260116171125164.png)

安裝後執行 `/help` 查看可用指令，你會看到這 3 個指令

- `/superpowers:brainstorm` 通過和用戶互動來不斷改進設計
- `/superpowers:write-plan` 創建實現方案
- `/superpowers:execute-plan` 批量執行方案

![](https://pic.yupi.icu/1/image-20260116171300633.png)



### 2、標準工作流程

下面以開發一個 "用戶註冊模組" 為例，演示 Superpowers 官方的標準工作流程。

首先，在終端中執行 `claude` 指令來啟動 Claude Code，然後按照下面的 7 個步驟操作：

#### 1）Brainstorming 頭腦風暴 => 對齊需求

選擇 `/superpowers:brainstorm` 指令並輸入需求：

![](https://pic.yupi.icu/1/image-20260116175524611.png)

Superpowers 不會急著寫程式碼，而是先通過多輪問答和你對齊需求，比如：

- 用戶註冊模組的主要場景是什麼？
- 希望支援哪些註冊方式？

![](https://pic.yupi.icu/1/image-20260116175456666.png)

通過互動問答，AI 會探索不同方案、不斷改進設計。

![](https://pic.yupi.icu/1/image-20260116175907783.png)

當需求和方案確認無誤後，它會自動將詳細的設計文件保存到 `docs/plans/` 目錄。

![](https://pic.yupi.icu/1/image-20260116180740987.png)



#### 2）Using Git Worktrees 創建獨立工作空間（可選）

設計方案通過後，Superpowers 會幫你創建一個 Git 工作樹（worktree），在新分支上建立隔離的工作空間，執行專案初始化，並驗證測試基線是否乾淨。這樣可以避免污染主分支。

這一步是可選的，我這裡直接讓 AI 繼續執行，看看會發生什麼：

![](https://pic.yupi.icu/1/image-20260116181020601.png)



#### 3）Writing Plans 制定實施計劃

執行 `/superpowers:write-plan` 指令，讓 Superpowers 生成一份詳細的實施計劃，把開發任務拆解成多個原子級步驟（每個任務控制在 2 ~ 5 分鐘）。

我這裡 AI 直接自動執行了，省了一步指令~

![](https://pic.yupi.icu/1/image-20260116180907360-20260116180953363-20260116181058928-20260116181118631.png)

查看 AI 生成的實施計劃文件，每個任務都包含：

- 精確的文件路徑
- 完整的程式碼內容
- 驗證步驟

![](https://pic.yupi.icu/1/image-20260116181910011.png)

好傢伙，這哪裡是實施計劃文件啊，感覺大多數程式碼都寫出來了！

![](https://pic.yupi.icu/1/image-20260116181959589.png)



#### 4）執行任務

執行 `/superpowers:execute-plan` 指令，Superpowers 會採用以下方式之一執行：
- 子代理驅動開發（Subagent-Driven Development）：為每個任務分配一個全新的子代理，經過兩階段審查（規範合規性檢查 + 程式碼質量檢查）
- 批量執行（Executing Plans）：分批執行任務，在關鍵節點暫停讓人工檢查

我這裡 AI 直接問我想要哪種方式：

![](https://pic.yupi.icu/1/image-20260116182128737.png)

我盲選一手 Subagent-Driven 方式，AI 自動選擇了對應的開發技能：

![](https://pic.yupi.icu/1/image-20260116182244311.png)

然後 AI 就開始幹活了：

![](https://pic.yupi.icu/1/image-20260116182445078.png)



#### 5）Test-Driven Development 測試驅動開發

在實現過程中，Superpowers 會強制執行 `紅-綠-重構` 流程：
- 先寫失敗的測試
- 執行測試，確認失敗
- 寫最小化的程式碼讓測試通過
- 執行測試，確認通過
- 提交程式碼

![](https://pic.yupi.icu/1/image-20260116183728764.png)

如果發現有程式碼是在測試之前寫的，Superpowers 會刪除它，強制你先寫測試。



#### 6）Code Review 程式碼審查

每完成一批任務後，Superpowers 會自動觸發程式碼審查，對照計劃檢查程式碼，按嚴重程度報告問題。如果發現嚴重問題（Critical），會阻止繼續進行。

![](https://pic.yupi.icu/1/image-20260116182947482.png)



#### 7）完成開發

所有任務完成後，Superpowers 會驗證所有測試是否通過：

![](https://pic.yupi.icu/1/image-20260116194339313.png)

然後 AI 可能會提供幾個選項，比如合併到主分支 / 創建 PR / 保留分支 / 丟棄更改。

如果你確定功能沒有問題，可以利用 Superpowers 內建的技能來完成開發分支的清理工作。

![](https://pic.yupi.icu/1/image-20260116194520921.png)



## 三、Superpowers 的優缺點

這套 "先設計後編碼" 的規範流程走下來，程式碼質量會更有保障，不過代價就是速度確實比讓 AI 直接生成程式碼會慢很多。真的是慢很多！就這麼個需求我搞了半個多小時！！！

![](https://pic.yupi.icu/1/image-20260116183405162.png)

如果你正在開發大型專案，需要團隊協作，那麼可以試試 Superpowers，前期多花的時間會在後期省回來。但是如果你只是想寫個簡單的腳本或者快速驗證一個想法，用它就有點兒牛刀殺雞了，真沒必要。



## 寫在最後

看到這裡，相信你已經對 Superpowers 有了基本的了解。

**Superpowers 能讓 AI 像專業程式設計師一樣工作，但代價是開發速度會變慢。**

如果你正在做大型專案、需要高質量的程式碼、團隊協作，那麼 Superpowers 會是不錯的選擇。但如果你只是做簡單的個人專案，直接讓 AI 生成程式碼會更快。

選擇合適的工具，才能事半功倍。

到這裡，我們已經學習了多種規範化開發工具，希望你能找到最適合自己的開發方式。



## 推薦資源

1）魚皮 AI 導航網站：[AI 資源大全、最新 AI 資訊、免費 AI 教程](https://ai.codefather.cn)

2）編程導航學習圈：[學習路線、編程教程、實戰專案、求職寶典、交流答疑](https://www.codefather.cn)

3）程式設計師面試八股文：[實習/校招/社招高頻考點、企業真題解析](https://www.mianshiya.com)

4）程式設計師寫履歷神器：[專業模板、豐富例句、直通面試](https://www.laoyujianli.com)

5）1 對 1 模擬面試：[實習/校招/社招面試拿 Offer 必備](https://ai.mianshiya.com)