const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const test = require("node:test");

const script = path.join(__dirname, "genReadme.js");

function generateReadme(files) {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), "gen-readme-"));
  try {
    for (const [name, content] of Object.entries(files)) {
      const file = path.join(directory, name);
      fs.mkdirSync(path.dirname(file), { recursive: true });
      fs.writeFileSync(file, content);
    }
    execFileSync(process.execPath, [script, directory]);
    return fs.readFileSync(path.join(directory, "README.md"), "utf8");
  } finally {
    fs.rmSync(directory, { recursive: true, force: true });
  }
}

test("有子目录时保留当前目录的 Markdown 文件", () => {
  const readme = generateReadme({
    "入门.md": "# 入门",
    "进阶/部署.md": "# 部署",
  });
  assert.ok(readme.includes("[入门](入门.md)"));
  assert.ok(readme.includes("[部署](进阶/部署.md)"));
  assert.ok(readme.indexOf("[入门]") < readme.indexOf("## 进阶"));
});

test("子目录没有 Markdown 时仍保留当前目录的文章", () => {
  const readme = generateReadme({
    "入门.md": "# 入门",
    "附件/示例.txt": "示例",
  });
  assert.ok(readme.includes("[入门](入门.md)"));
});

test("没有子目录时保留文章链接并编码空格", () => {
  const readme = generateReadme({ "API 指南.md": "# API 指南" });
  assert.ok(readme.includes("[API 指南](API%20指南.md)"));
});

test("只有子目录时仍包含多层目录中的文章", () => {
  const readme = generateReadme({ "进阶/配置/部署.md": "# 部署" });
  assert.ok(readme.includes("## 进阶"));
  assert.ok(readme.includes("[部署](进阶/配置/部署.md)"));
});

test("不为已有 README 或其他文件类型生成链接", () => {
  const readme = generateReadme({
    "README.md": "旧目录",
    "入门.md": "# 入门",
    "示例.txt": "示例",
    "进阶/README.md": "子目录说明",
    "进阶/部署.md": "# 部署",
  });
  assert.ok(!readme.includes("](README.md)"));
  assert.ok(!readme.includes("](进阶/README.md)"));
  assert.ok(!readme.includes("示例.txt"));
  assert.ok(readme.includes("[部署](进阶/部署.md)"));
});
