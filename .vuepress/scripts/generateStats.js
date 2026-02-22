const fs = require("fs");
const path = require("path");

// Directories to skip during analysis
const SKIP_DIRS = new Set([".git", ".github", ".vuepress", "node_modules", "translations"]);

/**
 * Recursively collect markdown file info
 * @param {string} dirPath
 * @param {string} relativeTo - base path for computing relative paths
 * @returns {Array<{relativePath: string, size: number, lines: number, chars: number, title: string, category: string}>}
 */
function collectMarkdownFiles(dirPath, relativeTo) {
  const results = [];
  let items;
  try {
    items = fs.readdirSync(dirPath, { withFileTypes: true });
  } catch {
    return results;
  }

  for (const item of items) {
    const fullPath = path.join(dirPath, item.name);
    if (item.isDirectory()) {
      if (SKIP_DIRS.has(item.name) || item.name.startsWith(".")) continue;
      results.push(...collectMarkdownFiles(fullPath, relativeTo));
    } else if (item.isFile() && item.name.endsWith(".md")) {
      try {
        const content = fs.readFileSync(fullPath, "utf-8");
        const rel = path.relative(relativeTo, fullPath);
        const parts = rel.split(path.sep);
        const category = parts.length > 1 ? parts[0] : "根目录";

        // Extract title from first heading or filename
        const headingMatch = content.match(/^#\s+(.+)$/m);
        const title = headingMatch ? headingMatch[1].trim() : item.name.replace(".md", "");

        // Count Chinese characters + English words
        const chineseChars = (content.match(/[\u4e00-\u9fff]/g) || []).length;
        const englishWords = (content.match(/[a-zA-Z]+/g) || []).length;

        results.push({
          relativePath: rel,
          size: Buffer.byteLength(content, "utf-8"),
          lines: content.split("\n").length,
          chars: content.length,
          chineseChars,
          englishWords,
          title,
          category,
          subcategory: parts.length > 2 ? parts[1] : "",
        });
      } catch {
        // skip unreadable files
      }
    }
  }
  return results;
}

/**
 * Aggregate stats from file list
 */
function computeStats(files) {
  const totalFiles = files.length;
  const totalChars = files.reduce((s, f) => s + f.chars, 0);
  const totalLines = files.reduce((s, f) => s + f.lines, 0);
  const totalSize = files.reduce((s, f) => s + f.size, 0);
  const totalChineseChars = files.reduce((s, f) => s + f.chineseChars, 0);
  const totalEnglishWords = files.reduce((s, f) => s + f.englishWords, 0);

  // Category breakdown
  const categoryMap = {};
  for (const f of files) {
    if (!categoryMap[f.category]) {
      categoryMap[f.category] = { fileCount: 0, chars: 0, lines: 0, size: 0, chineseChars: 0 };
    }
    categoryMap[f.category].fileCount++;
    categoryMap[f.category].chars += f.chars;
    categoryMap[f.category].lines += f.lines;
    categoryMap[f.category].size += f.size;
    categoryMap[f.category].chineseChars += f.chineseChars;
  }

  // Subcategory breakdown (for main categories)
  const subcategoryMap = {};
  for (const f of files) {
    if (!f.subcategory) continue;
    const key = f.category + " / " + f.subcategory;
    if (!subcategoryMap[key]) {
      subcategoryMap[key] = { fileCount: 0, chars: 0, chineseChars: 0 };
    }
    subcategoryMap[key].fileCount++;
    subcategoryMap[key].chars += f.chars;
    subcategoryMap[key].chineseChars += f.chineseChars;
  }

  // Top 15 longest files
  const topFiles = [...files]
    .sort((a, b) => b.chars - a.chars)
    .slice(0, 15)
    .map((f) => ({ title: f.title, chars: f.chars, chineseChars: f.chineseChars, category: f.category }));

  // File size distribution
  const sizeRanges = [
    { label: "< 1KB", min: 0, max: 1024 },
    { label: "1-5KB", min: 1024, max: 5120 },
    { label: "5-10KB", min: 5120, max: 10240 },
    { label: "10-50KB", min: 10240, max: 51200 },
    { label: "> 50KB", min: 51200, max: Infinity },
  ];
  const sizeDistribution = sizeRanges.map((r) => ({
    label: r.label,
    count: files.filter((f) => f.size >= r.min && f.size < r.max).length,
  }));

  return {
    totalFiles,
    totalChars,
    totalLines,
    totalSize,
    totalChineseChars,
    totalEnglishWords,
    categoryMap,
    subcategoryMap,
    topFiles,
    sizeDistribution,
  };
}

/**
 * Generate the HTML stats page
 */
function generateHTML(stats) {
  const categories = Object.entries(stats.categoryMap).sort((a, b) => b[1].fileCount - a[1].fileCount);
  const subcategories = Object.entries(stats.subcategoryMap).sort((a, b) => b[1].fileCount - a[1].fileCount).slice(0, 20);

  const categoryLabels = JSON.stringify(categories.map(([k]) => k));
  const categoryFileCounts = JSON.stringify(categories.map(([, v]) => v.fileCount));
  const categoryChinese = JSON.stringify(categories.map(([, v]) => v.chineseChars));
  const sizeLabels = JSON.stringify(stats.sizeDistribution.map((d) => d.label));
  const sizeCounts = JSON.stringify(stats.sizeDistribution.map((d) => d.count));
  const topLabels = JSON.stringify(stats.topFiles.map((f) => f.title.length > 18 ? f.title.slice(0, 18) + "…" : f.title));
  const topChars = JSON.stringify(stats.topFiles.map((f) => f.chineseChars));
  const subLabels = JSON.stringify(subcategories.map(([k]) => k));
  const subCounts = JSON.stringify(subcategories.map(([, v]) => v.fileCount));

  const formatNum = (n) => n.toLocaleString("zh-CN");

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>鱼皮 AI 知识库 - 数据统计</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: #f0f2f5; color: #333; }
  .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 40px 20px; text-align: center; }
  .header h1 { font-size: 2em; margin-bottom: 8px; }
  .header p { opacity: 0.9; font-size: 1.1em; }
  .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
  .summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 24px 0; }
  .stat-card { background: #fff; border-radius: 12px; padding: 24px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s; }
  .stat-card:hover { transform: translateY(-4px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
  .stat-card .number { font-size: 2em; font-weight: 700; color: #667eea; }
  .stat-card .label { font-size: 0.9em; color: #666; margin-top: 4px; }
  .charts { display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 20px; margin: 20px 0; }
  .chart-box { background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
  .chart-box h3 { margin-bottom: 16px; color: #444; font-size: 1.1em; }
  .chart-box canvas { width: 100% !important; }
  .table-box { background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin: 20px 0; overflow-x: auto; }
  .table-box h3 { margin-bottom: 16px; color: #444; }
  table { width: 100%; border-collapse: collapse; }
  th, td { padding: 10px 14px; text-align: left; border-bottom: 1px solid #eee; }
  th { background: #f8f9fa; color: #555; font-weight: 600; }
  tr:hover { background: #f8f9fe; }
  .footer { text-align: center; padding: 24px; color: #999; font-size: 0.85em; }
  @media (max-width: 600px) {
    .charts { grid-template-columns: 1fr; }
    .header h1 { font-size: 1.5em; }
    .stat-card .number { font-size: 1.5em; }
  }
</style>
</head>
<body>
<div class="header">
  <h1>📊 鱼皮 AI 知识库 · 数据统计</h1>
  <p>自动分析仓库内容，可视化展示教程统计数据</p>
</div>
<div class="container">
  <div class="summary">
    <div class="stat-card"><div class="number">${formatNum(stats.totalFiles)}</div><div class="label">📄 文档总数</div></div>
    <div class="stat-card"><div class="number">${formatNum(stats.totalChineseChars)}</div><div class="label">✍️ 中文字数</div></div>
    <div class="stat-card"><div class="number">${formatNum(stats.totalEnglishWords)}</div><div class="label">🔤 英文单词</div></div>
    <div class="stat-card"><div class="number">${formatNum(stats.totalLines)}</div><div class="label">📝 总行数</div></div>
    <div class="stat-card"><div class="number">${(stats.totalSize / 1024).toFixed(0)} KB</div><div class="label">💾 内容体积</div></div>
    <div class="stat-card"><div class="number">${categories.length}</div><div class="label">📂 内容分类</div></div>
  </div>

  <div class="charts">
    <div class="chart-box">
      <h3>📁 各分类文档数量</h3>
      <canvas id="categoryFileChart"></canvas>
    </div>
    <div class="chart-box">
      <h3>✍️ 各分类中文字数</h3>
      <canvas id="categoryCharsChart"></canvas>
    </div>
    <div class="chart-box">
      <h3>📏 文件大小分布</h3>
      <canvas id="sizeChart"></canvas>
    </div>
    <div class="chart-box">
      <h3>📂 子分类文档数量 (Top 20)</h3>
      <canvas id="subCategoryChart"></canvas>
    </div>
  </div>

  <div class="table-box">
    <h3>🏆 内容最丰富的文档 (Top 15)</h3>
    <table>
      <thead><tr><th>#</th><th>标题</th><th>分类</th><th>中文字数</th></tr></thead>
      <tbody>
        ${stats.topFiles.map((f, i) => `<tr><td>${i + 1}</td><td>${f.title}</td><td>${f.category}</td><td>${formatNum(f.chineseChars)}</td></tr>`).join("\n        ")}
      </tbody>
    </table>
  </div>

  <div class="table-box">
    <h3>📊 各分类详细数据</h3>
    <table>
      <thead><tr><th>分类</th><th>文档数</th><th>中文字数</th><th>总行数</th><th>体积</th></tr></thead>
      <tbody>
        ${categories.map(([k, v]) => `<tr><td>${k}</td><td>${v.fileCount}</td><td>${formatNum(v.chineseChars)}</td><td>${formatNum(v.lines)}</td><td>${(v.size / 1024).toFixed(1)} KB</td></tr>`).join("\n        ")}
      </tbody>
    </table>
  </div>
</div>

<div class="footer">
  <p>数据自动生成于 ${new Date().toLocaleDateString("zh-CN")} · <a href="https://github.com/liyupi/ai-guide" target="_blank">GitHub</a></p>
</div>

<script>
const COLORS = ['#667eea','#764ba2','#f093fb','#f5576c','#4facfe','#00f2fe','#43e97b','#fa709a','#fee140','#30cfd0','#a18cd1','#fbc2eb','#ff9a9e','#fad0c4','#ffecd2'];

new Chart(document.getElementById('categoryFileChart'), {
  type: 'pie',
  data: {
    labels: ${categoryLabels},
    datasets: [{ data: ${categoryFileCounts}, backgroundColor: COLORS }]
  },
  options: { responsive: true, plugins: { legend: { position: 'right' } } }
});

new Chart(document.getElementById('categoryCharsChart'), {
  type: 'bar',
  data: {
    labels: ${categoryLabels},
    datasets: [{ label: '中文字数', data: ${categoryChinese}, backgroundColor: '#667eea' }]
  },
  options: { responsive: true, indexAxis: 'y', plugins: { legend: { display: false } } }
});

new Chart(document.getElementById('sizeChart'), {
  type: 'doughnut',
  data: {
    labels: ${sizeLabels},
    datasets: [{ data: ${sizeCounts}, backgroundColor: COLORS.slice(0, 5) }]
  },
  options: { responsive: true, plugins: { legend: { position: 'right' } } }
});

new Chart(document.getElementById('subCategoryChart'), {
  type: 'bar',
  data: {
    labels: ${subLabels},
    datasets: [{ label: '文档数', data: ${subCounts}, backgroundColor: '#764ba2' }]
  },
  options: { responsive: true, indexAxis: 'y', plugins: { legend: { display: false } } }
});
</script>
</body>
</html>`;
}

// Main
const rootDir = path.resolve(__dirname, "../..");
const files = collectMarkdownFiles(rootDir, rootDir);
const stats = computeStats(files);
const html = generateHTML(stats);
const outputPath = path.resolve(rootDir, "stats.html");
fs.writeFileSync(outputPath, html, "utf-8");
console.log(`统计页面已生成: ${outputPath}`);
console.log(`共分析 ${stats.totalFiles} 个文档，${stats.totalChineseChars.toLocaleString()} 个中文字，${stats.totalLines.toLocaleString()} 行`);
