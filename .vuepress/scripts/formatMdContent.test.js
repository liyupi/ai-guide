const assert = require("assert");
const fs = require("fs");
const os = require("os");
const path = require("path");
const { spawnSync } = require("child_process");

const formatter = path.join(__dirname, "formatMdContent.js");
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), "format-md-content-"));

function runFormatter() {
  const result = spawnSync(process.execPath, [formatter, tempDir], {
    encoding: "utf8",
  });
  assert.strictEqual(result.status, 0, result.stderr || result.stdout);
}

try {
  const titledFile = path.join(tempDir, "Guide.md");
  const titledContent = "# Guide\n\nBody\n";
  fs.writeFileSync(titledFile, titledContent);

  runFormatter();
  assert.strictEqual(fs.readFileSync(titledFile, "utf8"), titledContent);

  const untitledFile = path.join(tempDir, "Notes.md");
  fs.writeFileSync(untitledFile, "Body\n");

  runFormatter();
  const onceFormatted = fs.readFileSync(untitledFile, "utf8");
  runFormatter();
  assert.strictEqual(fs.readFileSync(untitledFile, "utf8"), onceFormatted);

  console.log("formatMdContent preserves existing titles and is idempotent");
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
