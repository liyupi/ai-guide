const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const test = require("node:test");

test("README.md does not consume one of the 100 article slots", async () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), "gen-readme-limit-"));

  try {
    for (let i = 0; i < 100; i++) {
      const name = `Article-${String(i).padStart(3, "0")}.md`;
      fs.writeFileSync(path.join(directory, name), `# ${name}\n`);
    }
    await new Promise((resolve) => setTimeout(resolve, 1100));
    fs.writeFileSync(path.join(directory, "README.md"), "# Previous index\n");

    execFileSync(process.execPath, [path.join(__dirname, "genReadme.js"), directory]);

    const readme = fs.readFileSync(path.join(directory, "README.md"), "utf8");
    const links = readme.match(/^\[Article-\d{3}\]\(Article-\d{3}\.md\)$/gm) || [];
    assert.equal(links.length, 100);
  } finally {
    fs.rmSync(directory, { recursive: true, force: true });
  }
});
