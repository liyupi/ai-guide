# Kimi 鸿蒙版 App 体验升级，使用华为仓颉 markdown 解析引擎滑动帧率提升至 2.4 倍

本文转载自： [Kimi 鸿蒙版 App 体验升级，使用华为仓颉 markdown 解析引擎滑动帧率提升至 2.4 倍](https://www.ithome.com/0/877/614.htm)

感谢IT之家网友 [有鲫雪狐](https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2169131) 的线索投递！

[IT之家](https://www.ithome.com/) 8 月 24 日消息，据仓颉编程语言官方消息，Kimi 团队积极适配华为[鸿蒙](https://hmos.ithome.com/)系统，**已于今年 3 月推出了支持全量功能的鸿蒙版应用**，并通过内置仓颉 Markdown 渲染引擎，提升了长对话的渲染性能，实现流畅无卡顿的渲染效果。

![](https://pic.code-nav.cn/post_picture/1610518142000300034/8DdSYDjkhGkNM9s4.webp "Kimi 鸿蒙版 App 体验升级，使用华为仓颉 markdown 解析引擎滑动帧率提升至 2.4 倍")

据称，**Kimi 鸿蒙版 App 集成仓颉前，遇到主线程耗时长，应用卡顿的情况**，线上故障率达到千分之二，其中多数为 appfreeze。主要原因是对话渲染时 markdown 解析部分性能较差，耗时较长。而仓颉社区三方库已具备高性能的 markdown 解析、渲染库。在仓颉团队的推动下，Kimi 采用了仓颉方案优化应用性能。

仓颉三方库社区 Cangjie-TPC 提供了：

> * markdown 解析引擎 **commonmark4cj**（https://gitcode.com/ Cangjie-TPC / commonmark4cj），支持将 markdown 文本解析为节点树。
>
> * 公式解析库 **formula-ffi**（https://gitcode.com/ Cangjie-TPC / formula-ffi），支持将 LaTeX 公式渲染为图片。
>
> * 语法高亮库 **prism4cj**（https://gitcode.com/ Cangjie-TPC / prism4cj），支持解析代码块语法结构，标记高亮色彩。
>
> * markdown 组件库 **markdown4cj**（https://gitcode.com/ Cangjie-TPC / markdown4cj），支持解析代码块语法结构，标记高亮色彩。

这四个库分别提供了**纯仓颉版本**和**互操作版本**，其中互操作版本将仓颉接口封装成了 ArkTS 接口，方便用户在混合工程中直接使用。Kimi 采用的解决方案是：使用互操作版本的 commonmark4cj、formula-ffi、prism4cj 进行文本的解析，在 ArkTS 侧自主开发渲染库，将解析结果渲染成 markdown 组件。

仓颉编程语言官方表示，Kimi 这样做牺牲了部分易用性，但好处是既可以受惠于仓颉相关解析库的高性能，又可以在 UI 侧定制灵活的需求。

**Kimi 集成仓颉三方库后，相比集成前的方案，整体滑动帧率得到 2.4 倍以上优化**。三个仓颉三方库为单点功能带来显著优化，其中 commonmark4cj 带来 4 倍优化，formula-ffi 带来 34 倍优化，prism4cj 带来 2 倍以上优化。具体测试数据如下：

|                                                                     |          |        |
| :-----------------------------------------------------------------: | :------: | :----: |
|                                                                     |  **原版**  | **仓颉** |
|                     **markdown 节点解析耗时**解析 13K 字符                    |   80ms   |  20ms  |
| **数学公式解析耗时**测试会话（https://www.kimi.com/share/d28rvhj1cvfam4v242jg） | 328.40ms | 9.58ms |
|                         **代码块染色**解析 203 行代码块                        |   96ms   |  44ms  |
|                           **滑动帧率**60Hz 刷新率                          |   25 帧   |  60 帧  |

IT之家从仓颉编程语言官方获悉，当前仓颉社区已收录超 140+ 三方库，常用的包括：

* markdown 解析和渲染库 **markdown4cj **(https://gitcode.com/Cangjie-TPC/markdown4cj)

* 压缩库 **zip4cj **(https://gitcode.com/ Cangjie-TPC / zip4cj) 和 **zlib4cj **(https://gitcode.com/Cangjie-TPC/zlib4cj)

* MQTT 通信协议库 **mqtt4cj **(https://gitcode.com/Cangjie-TPC/mqtt4cj)

* 图像加载缓存库 **droplet** (https://gitcode.com/Cangjie-TPC/droplet)

* **动画库 svga-cj**  (https://gitcode.com/Cangjie-TPC/svga-cj)

广告声明：文内含有的对外跳转链接（包括不限于超链接、二维码、口令等形式），用于传递更多信息，节省甄选时间，结果仅供参考，IT之家所有文章均包含本声明。
