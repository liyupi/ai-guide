#!/usr/bin/env python3
"""
Generate English versions of images with Chinese text
Uses AI to create new images with English text replacing Chinese
"""

import os
import requests
import json
from pathlib import Path

# Configuration
OPENROUTER_API_KEY = "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"
REPO_ROOT = Path(__file__).parent
OUTPUT_DIR = REPO_ROOT / "image_en"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load translations
with open(REPO_ROOT / "image_translations.json", 'r', encoding='utf-8') as f:
    translations_data = json.load(f)

def create_image_generation_prompt(image_data):
    """Create a prompt for generating an English version of the image"""
    image_path = image_data['image_path']
    chinese_text = image_data['chinese_text']
    translations = image_data['english_translations']
    analysis = image_data.get('analysis', {})

    # Build prompt based on image type
    image_type = analysis.get('image_type', 'banner')
    description = analysis.get('description', '')

    if 'join_us' in image_path:
        prompt = f"""Create a modern, professional promotional banner image for a programming learning platform called "Programming Navigation" (编程导航).

Key elements:
- Main headline: "Start your programming learning journey" (开始你的编程学习之旅)
- Pricing: "360 yuan/year" and "480 yuan/year"
- Call to action: "Learn programming on Programming Navigator" (学编程就上编程导航)
- Include: "WeChat scan QR code" indicator
- Style: Modern, clean, tech-themed with blue/green colors
- Layout: Horizontal banner, suitable for website header
- Include a placeholder QR code area"""

    elif 'coupon' in image_path:
        prompt = f"""Create a professional coupon/voucher image for "Programming Navigation" (编程导航) platform.

Key elements:
- From: "Programmer Yu Pi" (程序员鱼皮)
- Title: "Exclusive Coupon for You" (给您赠送一张优惠券)
- Highlight: "Instant Discount" (立减)
- Include expiration placeholder
- Call to action: "Start your programming journey" (开始编程之旅)
- QR code instruction: "Long press to scan QR code"
- Style: Festive, red/gold colors, professional coupon design"""

    elif '11_11' in image_path:
        prompt = f"""Create a promotional coupon image for a special sale event.

Key elements:
- From: "Programmer Yu Pi"
- Title: "Exclusive Coupon"
- Text: "Instant Discount"
- Call to action: "Start your programming journey"
- Platform: "Programming Navigation"
- Style: Shopping/sale themed, eye-catching colors"""

    elif 'sdk' in image_path:
        # For complex screenshots, we'll create instructions instead
        return None

    else:
        # Generic prompt
        prompt = f"""Create a professional image with English text replacing these Chinese phrases:

Chinese to English mapping:
{json.dumps(translations, indent=2)}

Original description: {description}

Maintain the same layout, style, and professional appearance."""

    return prompt

def save_manual_editing_instructions():
    """Save instructions for manual image editing"""

    instructions = """# Image Translation Editing Instructions

This document provides instructions for manually editing images to replace Chinese text with English translations.

## Tools Needed
- **Image Editor**: Photoshop, GIMP, or Affinity Photo
- **Alternative Online Tools**: Canva, Figma, or Photopea

## Images to Edit

### 1. join_us.png
**Purpose**: Promotional banner for programming learning platform

**Text Replacements**:
| Chinese | English | Notes |
|---------|---------|-------|
| 开始你的编程学习之旅 | Start your programming learning journey | Main headline, large text |
| 360元/年 | 360 yuan/year | Pricing option 1 |
| ¥480元/年 | ¥480 yuan/year | Pricing option 2 |
| 学编程就上编程导航 | Learn programming on Programming Navigation | CTA text |
| 微信扫描二维码 | WeChat scan QR code | QR code instruction |

**Editing Steps**:
1. Open image in editor
2. Use text tool to select each Chinese text element
3. Replace with English translation
4. Adjust font size if needed to fit
5. Keep original colors and styling
6. Save as `join_us_en.png`

---

### 2. coupon.jpg
**Purpose**: Promotional coupon image

**Text Replacements**:
| Chinese | English |
|---------|---------|
| 程序员鱼皮 | Programmer Yu Pi |
| 给您赠送一张优惠券 | Presents you with a coupon |
| 立减 | Instant Discount |
| 2026/01/20 23:00 后失效 | Expires after 2026/01/20 23:00 |
| 长按图片识别二维码 | Long press image to scan QR code |
| 开始编程之旅 | Start your programming journey |
| 编程导航 | Programming Navigation |

**Editing Steps**:
1. Open image in editor
2. Replace each text element with English
3. Maintain festive/red-gold color scheme
4. Keep coupon layout and design
5. Save as `coupon_en.jpg`

---

### 3. 11_11.png
**Purpose**: Special sale promotional coupon

**Text Replacements**:
| Chinese | English |
|---------|---------|
| 程序员鱼皮 | Programmer Yu Pi |
| 给您赠送一张优惠券 | Give you a coupon |
| 立减 | Instant Discount |
| 后失效 | Expires after |
| 长按图片识别二维码 | Long press to recognize QR code |
| 开始编程之旅 | Start coding journey |
| 编程导航 | Programming Navigation |

**Editing Steps**:
1. Similar to coupon.jpg
2. Replace text with English translations
3. Save as `11_11_en.png`

---

### 4. sdk_project.png
**Purpose**: Course/tutorial screenshot

**Recommendation**: Keep original and add English captions

**Option A: Add English Captions**
- Place English text overlays near key sections
- Use semi-transparent background for readability
- Save as `sdk_project_en.png`

**Option B: Create English Version**
- This is a complex screenshot with many text elements
- Consider recreating the entire UI in English
- Or keep original and provide English translations separately

---

## Alternative: Use AI Image Generation Services

If you prefer to use AI to generate new images:

1. **Midjourney**: Use prompts from image_generation_prompts.json
2. **DALL-E 3**: Available via ChatGPT Plus or API
3. **Stable Diffusion**: Use locally or via online services

### Sample Prompts (for reference):

**join_us.png**:
```
Create a modern promotional banner for a programming learning website with:
- Headline: "Start your programming learning journey"
- Two pricing tiers: "360/year" and "480/year"
- CTA button: "Learn programming on Programming Navigator"
- QR code placeholder
- Style: Clean, modern tech design, blue gradient background
```

---

## Quick Online Editing Options

If you don't have Photoshop:

1. **Photopea** (https://www.photopea.com/) - Free Photoshop alternative in browser
2. **Canva** (https://www.canva.com/) - Easy-to-use design tool
3. **Figma** (https://www.figma.com/) - Professional design tool (free tier)

### Photopea Workflow:
1. Open https://www.photopea.com/
2. File > Open > select image
3. Use Type tool (T) to select text
4. Replace with English
5. File > Export As > PNG/JPG

---

## After Editing

Once you've created the English versions:

1. Save to `image_en/` directory with `_en` suffix
2. Update markdown files to reference English versions
3. Test in browser to verify display

### Example Update:

**Before**:
```markdown
![Join Us](/image/join_us.png)
```

**After**:
```markdown
![Join Us](/image/join_us_en.png)
```

---

## Automated Script Execution

To use this file as reference for automated processing, see the translations in `image_translations.json`.
"""

    with open(REPO_ROOT / "IMAGE_EDITING_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
        f.write(instructions)

    print("✓ Saved manual editing instructions to IMAGE_EDITING_INSTRUCTIONS.md")

def create_image_generation_prompts():
    """Create prompts for AI image generation"""
    prompts = []

    for image_data in translations_data:
        prompt = create_image_generation_prompt(image_data)
        if prompt:
            prompts.append({
                "image": image_data['image_path'],
                "prompt": prompt,
                "translations": image_data['english_translations']
            })

    with open(OUTPUT_DIR / "image_generation_prompts.json", 'w', encoding='utf-8') as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved {len(prompts)} image generation prompts")

def main():
    print("="*60)
    print("English Image Generation Setup")
    print("="*60)

    # Create prompts for AI image generation
    print("\n1. Creating image generation prompts...")
    create_image_generation_prompts()

    # Create manual editing instructions
    print("\n2. Creating manual editing instructions...")
    save_manual_editing_instructions()

    # Create a simple HTML preview page
    print("\n3. Creating HTML preview page...")
    create_html_preview()

    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)

    print("\nGenerated files:")
    print(f"  - {OUTPUT_DIR}/image_generation_prompts.json")
    print(f"  - IMAGE_EDITING_INSTRUCTIONS.md")
    print(f"  - {OUTPUT_DIR}/preview.html")

    print("\nNext steps:")
    print("  1. Review IMAGE_EDITING_INSTRUCTIONS.md for manual editing")
    print("  2. Or use prompts in image_generation_prompts.json with AI image generators")
    print("  3. Open {OUTPUT_DIR}/preview.html to see before/after comparison")

def create_html_preview():
    """Create HTML preview page for comparing original and English text"""

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Translation Preview</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .image-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .image-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .image-title {
            font-size: 1.2em;
            font-weight: bold;
        }
        .translation-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        .translation-table th,
        .translation-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        .translation-table th {
            background: #f0f0f0;
        }
        .chinese {
            color: #e74c3c;
        }
        .english {
            color: #27ae60;
            font-weight: 500;
        }
        .status {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 500;
        }
        .status.pending {
            background: #fff3cd;
            color: #856404;
        }
        .status.done {
            background: #d4edda;
            color: #155724;
        }
    </style>
</head>
<body>
    <h1>🖼️ Image Translation Preview</h1>
    <p style="text-align: center; color: #666;">
        This page shows Chinese text extracted from images and their English translations.
    </p>
"""

    for image_data in translations_data:
        image_path = image_data['image_path']
        translations = image_data['english_translations']

        html += f"""
    <div class="image-container">
        <div class="image-header">
            <div class="image-title">📸 {image_path}</div>
            <span class="status pending">⏳ Pending English Image</span>
        </div>
        <table class="translation-table">
            <thead>
                <tr>
                    <th width="45%">Chinese (原文)</th>
                    <th width="45%">English (英文)</th>
                </tr>
            </thead>
            <tbody>
"""

        for cn, en in translations.items():
            html += f"""
                <tr>
                    <td class="chinese">{cn}</td>
                    <td class="english">{en}</td>
                </tr>
"""

        html += """
            </tbody>
        </table>
    </div>
"""

    html += """
    <div style="text-align: center; margin-top: 40px; padding: 20px; background: white; border-radius: 8px;">
        <h3>📝 Editing Instructions</h3>
        <p>See <code>IMAGE_EDITING_INSTRUCTIONS.md</code> for detailed editing instructions.</p>
        <p>Or use the prompts in <code>image_en/image_generation_prompts.json</code> with AI image generators.</p>
    </div>
</body>
</html>
"""

    with open(OUTPUT_DIR / "preview.html", 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Created HTML preview at {OUTPUT_DIR}/preview.html")

if __name__ == "__main__":
    main()
