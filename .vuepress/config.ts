import { defineConfig } from "vuepress/config";
import extraSideBar from "./extraSideBar";
import footer from "./footer";
import navbar from "./navbar";
import sidebar from "./sidebar";

const author = "Programmer Fish Skin";
const domain = "https://ai.codefather.cn";
const tags = [
  "ai",
  "deepseek",
  "AI News",
  "Artificial Intelligence",
  "AI Industry Trends",
  "AI Technology",
  "AI News Updates",
  "AI Dynamics",
  "AI Market Analysis",
  "AI Models",
  "AI Exclusive Analysis",
  "AI Deep Insights",
];

export default defineConfig({
  title: "Fish Skin's AI Knowledge Base",
  description:
    "Fish Skin's AI Knowledge Base - Free DeepSeek Tutorials | Tools | Resources, a one-stop open-source free artificial intelligence knowledge sharing platform, bringing together introductions to popular AI tools like Deepseek, GPT, usage guides, tips sharing, application scenarios, AI monetization, industry news, tutorial resource summaries, providing systematic AI tutorials and selected AI resources to help you quickly master AI technology and become an AI expert!",
  head: [
    // Site icon
    ["link", { rel: "icon", href: "/favicon.ico" }],
    // SEO
    [
      "meta",
      {
        name: "keywords",
        content:
          "ai, deepseek, AI News, Artificial Intelligence, AI Industry Trends, AI Technology, AI News Updates, AI Dynamics, AI Market Analysis, AI Models, AI Exclusive Analysis, AI Deep Insights",
      },
    ],
    // Baidu Analytics
    [
      "script",
      {},
      `
        var _hmt = _hmt || [];
        (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?6998d638562bceef30be297767e91d64";
          var s = document.getElementsByTagName("script")[0];
          s.parentNode.insertBefore(hm, s);
        })();
      `,
    ],
  ],
  permalink: "/:slug",

  // Watch file changes for hot reload
  extraWatchFiles: [".vuepress/*.ts", ".vuepress/sidebars/*.ts"],
  markdown: {
    // Enable line numbers for code blocks
    lineNumbers: true,
    // Support rendering headings beyond level 4
    extractHeaders: ["h2", "h3", "h4", "h5", "h6"],
  },
  // @ts-ignore
  plugins: [
    ["@vuepress/back-to-top"],
    // Google Analytics
    [
      "@vuepress/google-analytics",
      {
        ga: "GTM-WVS9HM6W", // Add your own Google Analytics ID, e.g. UA-00000000-0
      },
    ],
    ["@vuepress/medium-zoom"],
    // https://github.com/lorisleiva/vuepress-plugin-seo
    [
      "seo",
      {
        siteTitle: (_, $site) => $site.title + " - Free DeepSeek Tutorials | Tools | Resources",
        title: ($page) => $page.title + " - Free DeepSeek Tutorials | Tools | Resources",
        description: ($page) => $page.frontmatter.description || $page.description,
        author: (_, $site) => $site.themeConfig.author || author,
        tags: ($page) => $page.frontmatter.tags || tags,
        type: ($page) => "article",
        url: (_, $site, path) => ($site.themeConfig.domain || domain || "") + path,
        image: ($page, $site) =>
          $page.frontmatter.image &&
          (($site.themeConfig.domain && !$page.frontmatter.image.startsWith("http")) || "") + $page.frontmatter.image,
        publishedAt: ($page) => $page.frontmatter.date && new Date($page.frontmatter.date),
        modifiedAt: ($page) => $page.lastUpdated && new Date($page.lastUpdated),
      },
    ],
    // https://github.com/ekoeryanto/vuepress-plugin-sitemap
    [
      "sitemap",
      {
        hostname: domain,
      },
    ],
    // https://github.com/IOriens/vuepress-plugin-baidu-autopush
    ["vuepress-plugin-baidu-autopush"],
    // https://github.com/zq99299/vuepress-plugin/tree/master/vuepress-plugin-tags
    ["vuepress-plugin-tags"],
    // https://github.com/znicholasbrown/vuepress-plugin-code-copy
    [
      "vuepress-plugin-code-copy",
      {
        successText: "Code copied",
      },
    ],
    // https://github.com/webmasterish/vuepress-plugin-feed
    [
      "feed",
      {
        canonical_base: domain,
        count: 10000,
        // Document directories to auto-push
        posts_directories: [],
      },
    ],
    // https://github.com/tolking/vuepress-plugin-img-lazy
    ["img-lazy"],
  ],
  // Theme configuration
  themeConfig: {
    logo: "/logo.png",
    nav: navbar,
    sidebar,
    lastUpdated: "Last Updated",

    // GitHub repository location
    repo: "liyupi/ai-guide",
    docsBranch: "master",

    // Edit links
    editLinks: true,
    editLinkText: "Improve this page",

    // @ts-ignore
    // Footer copyright information
    footer,
    // Extra right sidebar
    extraSideBar,
  },
});
