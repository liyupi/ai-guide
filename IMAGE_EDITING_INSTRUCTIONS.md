# Image Translation Editing Instructions

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
