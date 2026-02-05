# OpenCode：開源免費的 AI 命令行工具實測

大家好，我是程序員魚皮。

Claude Code 一直是大家公認的 AI 編程命令行工具 Top 1，在 AI 和程序員圈子裡幾乎是神一般的存在。

![](https://pic.yupi.icu/1/happy-new-year-claude-coders-v0-o2quvbl99lag1.png)

但是，這狗玩意兒對中國用戶可不太友好……

首先，如果你想要使用 Claude Code，就必須要有特殊的網路 + 官方賬號，否則就會看到一片紅。

![](https://pic.yupi.icu/1/cannotuseclaude.png)

此外，2025 年 9 月，Anthropic 公司不知道抽什麼風，突然宣布 **全面禁止中國控股企業使用 Claude 服務**，不僅包括中國大陸企業，連海外中資控股超過 50% 的公司都在封禁範圍內！

甚至 Anthropic 還特別點名了中國，把咱們稱為 **敵對國家**！

![](https://pic.yupi.icu/1/image-20250905164631315.png)

天下苦 Claude Code 久矣！

但是最近我身邊很多程序員朋友開始從 Claude Code 轉向了另一個工具，正是突然大火的開源項目 OpenCode。

![](https://pic.yupi.icu/1/image-20260107174223010.png)

這玩意只用了半年的時間，就在 GitHub 上漲到了 5.2w Star！

這是個什麼概念？比我在 GitHub 上開源的幾十個項目的總和加起來都多！慕了慕了……

![](https://pic.yupi.icu/1/opencodestarhistory.png)

OpenCode 到底是什麼？憑什麼這麼火？



## 啥是 OpenCode？

[OpenCode](https://opencode.ai/) 是一款 100% 開源的 AI 編程命令行工具，可以在 **終端、IDE、甚至桌面應用** 中使用。

![](https://pic.yupi.icu/1/screenshot.png)

你可能會問：這玩意兒跟 Claude Code 有啥區別？

試試不就知道了？

接下來我帶大家實操一下，從零開始安裝、配置、到實際寫代碼，一條龍服務~



## 從 0 開始上手 OpenCode

### 1、安裝運行 OpenCode

直接進入 OpenCode 官網，複製一行命令：

![](https://pic.yupi.icu/1/image-20260107174407894.png)

命令如下：

```bash
curl -fsSL https://opencode.ai/install | bash
```

然後在終端中執行，就可以完成安裝了。

安裝完成之後，輸入 `opencode` 進入程序，接下來你就可以愉快地使用了~

![](https://pic.yupi.icu/1/image-20260107174646918.png)

先來個經典的 Hello World，AI 成功給出了回覆。

![](https://pic.yupi.icu/1/image-20260107174755331.png)

恭喜，到這裡你已經掌握了 OpenCode 的 70% 了。



### 2、選擇模式和模型

OpenCode 支持 2 種模式，默認是 Build 模式，用來構建應用、生成代碼。

按一下 Tab 鍵，就可以切換到 Plan 模式，用於生成執行計劃。

![](https://pic.yupi.icu/1/image-20260107174952823.png)

按一下 `Ctrl + p` 鍵，可以打開命令面板，裡面有幾十個內置命令。我們先來試著切換一下大模型：

![](https://pic.yupi.icu/1/image-20260107175255527.png)

默認提供了 4 個免費模型：

![](https://pic.yupi.icu/1/image-20260107175409282.png)

好傢伙，連智譜最新的 GLM-4.7 竟然也免費？那我的 Coding Plan 套餐不是白開了？

![](https://pic.yupi.icu/1/image-20260107175513490.png)

除了免費的模型外，OpenCode 支持超多的 AI 模型，你可以自由選擇：

![](https://pic.yupi.icu/1/image-20260107175614359.png)

選中模型後，配置自己的 API Key 就好了：

![](https://pic.yupi.icu/1/image-20260107175657296.png)

如果你之前有 **Claude Pro/Max 訂閱賬號**，可以直接登錄使用，無縫從 Claude Code 遷移過來。

![](https://pic.yupi.icu/1/image-20260107175745963.png)



### 3、快捷指令

OpenCode 支持斜槓命令，輸入 `/`，能看到很多操作，比如查看模型列表、查看 Agents、管理 MCP、切換主題等等：

![](https://pic.yupi.icu/1/image-20260107175926346.png)

支持幾十個不同的主題，顏值都挺高的，從這點也能看出來 OpenCode 很注重用戶的體驗：

![](https://pic.yupi.icu/1/image-20260107180108430.png)

輸入 `@` 可以快速關聯目錄文件，給 AI 添加上下文： 

![](https://pic.yupi.icu/1/image-20260107182710150.png)



### 4、交互體驗

相比於 Claude Code，OpenCode 真是把命令行的交互體驗拉滿了，甚至我覺得它是一個偽裝成命令行的桌面應用。

你可以點擊某條消息，然後會彈出一個消息動作框，你可以撤回消息和 AI 的回覆，也可以複製、或者基於當前對話新開一個對話框。

![](https://pic.yupi.icu/1/image-20260107180609525.png)

你可以通過鼠標上下滾動來切換選單，並且可以直接通過鼠標點擊進入下一步。

你可以按 `Ctrl + p` 鍵打開命令面板，然後開啟側邊欄：

![](https://pic.yupi.icu/1/image-20260107181100523.png)

然後界面就變成了這樣，你管這叫命令行？

![](https://pic.yupi.icu/1/image-20260107181218259.png)



### 5、LSP 支持

細心的你一定看到了，右邊的側邊欄有個 `LSP`，這是什麼鬼東西？老色批？

LSP（Language Server Protocol 語言服務器協議）是微軟開發的一種通信協議，用於讓代碼編輯器和語言服務器之間進行通信。

簡單來說，**LSP 就是讓編輯器看懂代碼的技術。**

比如你在 VS Code 裡寫代碼，輸入 `console.` 它會自動提示 `log`、點擊函數名能跳轉到代碼定義、寫錯代碼會畫紅線提醒。這些代碼編輯器的功能，背後都是 LSP 在幹活。

OpenCode 支持 LSP，意味著 AI 能真正理解你的代碼結構，而不是把代碼當普通文字瞎猜，改起來更精準。

比如我讓 AI 介紹我的 AI 答題平台項目中最有價值的代碼，LSP 就派上用場了。它能幫 AI 快速定位某段代碼在哪裡被調用、引用了哪些變量，而不是讓 AI 傻傻地全局搜索文本。

![](https://pic.yupi.icu/1/image-20260107181807464.png)



### 6、回到之前的會話

如果你不小心關閉了 OpenCode，不用擔心，可以打開命令面板，選中 “Switch session” 切換會話：

![](https://pic.yupi.icu/1/image-20260107183241477.png)

就能回到之前的聊天了：

![](https://pic.yupi.icu/1/image-20260107183320692.png)



## 桌面版 OpenCode

即使 OpenCode 支持了這麼多改進用戶體驗的交互，但我估計大多數同學還是不喜歡小黑框的。

沒關係，OpenCode 還提供了桌面應用版本！macOS、Windows、Linux 全端支持，這真的是要卷死 Claude Code 的節奏啊……

> 指路：https://opencode.ai/download

![](https://pic.yupi.icu/1/image-20260107182151987.png)

不過當我懷著滿腔熱血安裝並打開它時，竟然報錯了！

![](https://pic.yupi.icu/1/image-20260107183123854.png)

經過一番排查，發現原來是我開了代理，關閉之後就正常運行了。

![](https://pic.yupi.icu/1/image-20260107183605119.png)

但是用慣了 Cursor，這個交互體驗真的有點敷衍了，不推薦大家使用。



## OpenCode 擴展能力

到目前為止，我覺得 OpenCode 在前端用戶體驗上全方面碾壓 Claude Code，而且 OpenCode 完全兼容 Claude Code 的 Skills 系統！

Skills 是一種給 AI 準備的能力擴展包。你可以把它理解成給新同事準備的工作交接文檔，裡面包含任務執行方法、工具使用說明、模板素材等。

比如你可以創建一個 `公司代碼規範 Skill`，把代碼風格、命名規則、註釋要求等寫進去。之後 Claude Code 生成的代碼就會自動遵循這些規範，不用每次都重複說明。

根據官方文檔，OpenCode 會自動搜索這些位置的 Skills：

- `.opencode/skill/<name>/SKILL.md`（項目目錄）
- `~/.config/opencode/skill/<name>/SKILL.md`（用戶目錄）
- `.claude/skills/<name>/SKILL.md`（Claude Code 兼容）
- `~/.claude/skills/<name>/SKILL.md`（Claude Code 兼容）

也就是說，如果你之前給 Claude Code 創建過自定義 Skills，直接拿過來就能用！又是無縫遷移。



## Oh My OpenCode 開掛插件

如果你覺得 OpenCode 還不夠強，可以試試 `Oh My OpenCode` 這個開源的 OpenCode 增強插件，已經 1w Star 了。

> 項目地址：https://github.com/code-yeongyu/oh-my-opencode

![](https://pic.yupi.icu/1/image-20260107184457429.png)

這個插件有多牛？看看用戶評價：

> "It made me cancel my Cursor subscription."（它讓我取消了 Cursor 訂閱）
> 
> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day"（一天內用它解決了 8000 個 eslint 警告）



Oh My OpenCode 的核心功能是引入了一個叫 **Sisyphus** 的智能體編排系統。

我特地去搜了一下：

> 西西弗斯（Sisyphus）是古希臘神話中一位因欺騙眾神、挑戰權威而被諸神懲罰的國王，他的懲罰是永無止境地將一塊巨石推上山頂，而石頭一到山頂便會滾落，如此周而復始，象徵著徒勞無功、永無休止的任務，也代表著一種對荒誕命運的抗爭精神。

這個系統可以：

1. 並行調度多個 AI 模型：比如讓 GPT debug 的同時讓 Gemini 寫前端
2. 自動任務管理：不完成任務不讓停，像西西弗斯推石頭一樣鍥而不捨
3. 智能代碼審查：自動檢測並清理 AI 生成的冗餘註釋
4. LSP 深度集成：提供重命名、跳轉定義等 IDE 級功能

簡單來說，Sisyphus 就是一個 AI 監工，它能同時指揮多個 AI 模型幹活，還會盯著它們把任務做完。

![](https://pic.yupi.icu/1/omo.png)

雖然官方說用一行命令就能完成安裝，但我建議你先安裝 bun，再執行 npx 來安裝，否則可能會報錯。

```bash
npm install bun -g
npx oh-my-opencode install
```

安裝過程中，可能會問你有沒有某些模型的訂閱，我反正啥都沒有，一直選 "No" 就行了：

![](https://pic.yupi.icu/1/image-20260107185251337.png)

安裝完成後，再次進入 OpenCode，之後只需要在你的提示詞裡加上 `ultrawork`（或 `ulw`）這個開掛咒語，就能激活全部增強功能。自動調度多個 AI 模型同時工作、深度探索代碼庫、鍥而不捨地執行。

下面我們試試看，正好來驗證一下 OpenCode 做項目的能力如何？能不能把 Claude Code 一腳踹飛？



## 實戰項目 - 用 OpenCode 做個 AI 健康助手

最近螞蟻集團的 `螞蟻阿福` AI 健康助手火了，地鐵口、公司樓下的電視廣告中隨處可見何炅老師的身影。

![](https://pic.yupi.icu/1/mayiafuad.jpeg)

雖然我還沒有用過它，但是聽說它可以通過拍皮膚、拍報告提供 AI 初診，還能智能回答醫學科普和治療建議。

那我們也來做個類似的健康小助手網站吧！

前有螞蟻阿福，今有魚皮阿坤。

![](https://pic.yupi.icu/1/image-20260107194117758.png)

先分析一下，我們要做的是包含前端 + 後端的全棧項目，而且後端還需要調用 AI 大模型來生成內容。

這裡我選擇用 **Vercel AI Gateway** 來實現 AI 能力，這是一款簡單易用的 AI 網關。

![](https://pic.yupi.icu/1/1760687990497-90720fbb-0df6-4ede-87b8-64b8702994e9-20251028181254840.png)

什麼是 AI 網關？

簡單來說，它就像是火車站的檢票口，你的應用發來的請求先經過網關，網關幫你處理認證、限流、監控等一系列複雜的操作，然後把請求轉發給 AI 大模型。

![](https://pic.yupi.icu/1/1761645642401-683e786e-3e06-420a-abce-cd43f7bfa901.png)

而且 Vercel AI Gateway 支持對接 500 多個大模型，還有免費額度，非常適合學習和小項目。

> 指路：https://vercel.com/ai-gateway



1）首先你需要註冊登錄 Vercel，然後在控制台創建 API Key，注意不要洩露哦：

![](https://pic.yupi.icu/1/1760688078133-7b91b6f3-2fc4-4bb4-b2c1-d517699f0968-20251028181254879.png)



2）啟動 OpenCode，切換模型到編程能力很強、並且免費的 GLM-4.7，然後輸入這段提示詞：

```markdown
你是一位專業的程序員，請幫我開發《每日健康小助手》網站，用戶可以通過和 AI 聊天來記錄和管理每日健康狀態。

## 開發要求

1. 需要包含完整的前端和後端，後端使用 Node.js
2. 使用 Vercel 的 AI Gateway 實現 AI 能力，需要先通過官方文檔來獲取用法：https://vercel.com/docs/ai-gateway/getting-started
3. 以完成核心功能為目標，確保項目可以正常運行
4. 整體網站界面採用清新的綠色健康風格，響應式適配各種尺寸的設備
5. AI 需要主動詢問用戶的健康狀況，比如睡眠、運動、飲食等
```

點擊發送後，OpenCode 會自動使用網頁抓取工具讀取 Vercel AI Gateway 的官方文檔，學習最新的用法：

![](https://pic.yupi.icu/1/image-20260107190151933.png)

大概 5 分鐘左右，AI 就完成了全部代碼的生成，並且自動安裝了依賴。

![](https://pic.yupi.icu/1/image-20260107190629349.png)



3）我直接把之前拿到的 Vercel 的 API Key 提供給 AI，讓它幫我啟動項目：

![](https://pic.yupi.icu/1/image-20260107190751628.png)



4）啟動項目成功後，打開瀏覽器訪問 `localhost:3000`，測試一下效果。

結果報錯了！無法調用 AI。

![](https://pic.yupi.icu/1/image-20260107191838608.png)



可能是 AI 對 Vercel AI Gateway 文檔的理解不到位，導致寫錯了調用 AI 的代碼。於是我再次把文檔輸入給 AI，讓它再戰一次：

![](https://pic.yupi.icu/1/image-20260107191719979.png)

結果又報錯了，明明我已經給 AI 提供了 API Key，系統還是報錯 “缺少 API Key”。

於是我又調了一次 AI，告訴它 “這個 key 我之前已經提供給你了”。

![](https://pic.yupi.icu/1/image-20260107192718301.png)

經過大概 5 次左右的報錯和修復，仍然不能正常使用！我麻了啊……

![](https://pic.yupi.icu/1/image-20260107193542108.png)

於是，我有一個鬼點子：既然要跟 Claude Code 比較，那我不妨嘗試用 Claude Code 修復這個 OpenCode 解決不了的問題？

![](https://pic.yupi.icu/1/image-20260107193829543.png)

試試看！輸入提示詞：

```markdown
現在項目後端 AI 功能不可用
請參考 https://vercel.com/docs/ai-gateway/getting-started 文檔
幫我修復後端，確保項目能正常運行
```

![](https://pic.yupi.icu/1/image-20260107193701784.png)

Claude Code 成功修復了問題，終於能夠正常使用了：

![](https://pic.yupi.icu/1/image-20260107194915666.png)

💡 注意，如果你遇到了調用 AI 網路超時的問題，可以讓 AI 把調用的 baseURL 改為 https://ai-gateway.vercel.sh/v1

之前類似的任務我用 Claude Code / Cursor + GLM，不到 10 分鐘就搞定了。這次竟然花了 20 分鐘左右，還要經過來回拉扯，才能正常使用。

這讓我不得不懷疑 OpenCode 的能力了。而且感覺 GLM 大模型在 OpenCode 中好像變笨了，不知道是不是我的錯覺…… 

不行，大家把 OpenCode 吹得這麼牛批，我得再