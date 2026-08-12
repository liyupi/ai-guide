// 格式化 md 内容
// 1. 如果内容开头不是一级标题，或者二级标题，或者是一级，二级标题，那么就获取到文件名，然后在 md 内容开头添加一个二级标题，例如："## 文件名" + 换行 + 正文内容
// 2. 如果内容开头是一级标题，或者二级标题，那么就不做任何处理
// 3. 脚本接受相对目录参数，例如：node scripts/formatMdContent.js ./docs/guide，递归处理所有 .md

const fs = require("fs");
const path = require("path");

function formatMdContent(content, filePath) {
  // 检查内容是否以一级或二级标题开始
  const firstLine = content.trim().split(/\r?\n/, 1)[0];
  const hasTitle = /^#\s|^##\s/.test(firstLine);
  // 获取文件名（不含扩展名）
  const fileName = path.basename(filePath, path.extname(filePath));

  if (!hasTitle) {
    // 如果没有标题，添加二级标题
    return `## ${fileName}\n\n${content}`;
  } else {
    // 如果有标题，检查标题内容是否与文件名一致
    const titleContent = firstLine.replace(/^#\s|^##\s/, "").trim();
    if (titleContent !== fileName) {
      // 如果标题内容与文件名不一致，在开头添加文件名作为二级标题
      return `## ${fileName}\n\n${content}`;
    }
  }

  return content;
}

function processDirectory(dirPath) {
  // 获取绝对路径
  const absolutePath = path.resolve(process.cwd(), dirPath);

  // 读取目录下的所有文件
  const files = fs.readdirSync(absolutePath);

  files.forEach((file) => {
    const filePath = path.join(absolutePath, file);
    const stat = fs.statSync(filePath);

    if (stat.isFile() && path.extname(file) === ".md") {
      // 读取并处理 markdown 文件
      const content = fs.readFileSync(filePath, "utf8");
      const formattedContent = formatMdContent(content, filePath);

      // 写回文件
      fs.writeFileSync(filePath, formattedContent, "utf8");
      console.log(`已处理: ${file}`);
    } else if (stat.isDirectory()) {
      // 递归处理子目录
      processDirectory(filePath);
    }
  });
}

// 获取命令行参数
const targetDir = process.argv[2];

if (!targetDir) {
  console.error("请提供目标目录路径");
  process.exit(1);
}

try {
  processDirectory(targetDir);
  console.log("所有 Markdown 文件处理完成");
} catch (error) {
  console.error("处理过程中出错:", error);
  process.exit(1);
}
