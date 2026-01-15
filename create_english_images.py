#!/usr/bin/env python3
"""
Create English versions of images with Chinese text
Uses PIL to add English text overlays
"""

import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json

# Configuration
REPO_ROOT = Path(__file__).parent
IMAGE_DIR = REPO_ROOT / "image"

# Load translations
with open(REPO_ROOT / "image_translations.json", 'r', encoding='utf-8') as f:
    translations_data = json.load(f)

def get_font(size, bold=False):
    """Get font for text"""
    try:
        # Try system fonts
        font_names = [
            "Arial.ttf",
            "Arial Bold.ttf" if bold else "Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNSDisplay.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]

        for font_name in font_names:
            try:
                if os.path.exists(font_name):
                    return ImageFont.truetype(font_name, size)
            except:
                continue

        # Fallback to default
        return ImageFont.load_default()
    except:
        return ImageFont.load_default()

def create_english_join_us():
    """Create English version of join_us.png"""
    img_path = IMAGE_DIR / "join_us.png"
    if not img_path.exists():
        return None

    # Open original image
    img = Image.open(img_path).convert("RGBA")

    # Create a transparent overlay
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    width, height = img.size

    # English text replacements
    texts = [
        ("Start Your Programming Learning Journey", width // 2, height // 4, 48, (255, 255, 255)),
        ("360 yuan/year", width // 2, height // 2 - 30, 36, (255, 255, 255)),
        ("480 yuan/year", width // 2, height // 2 + 30, 36, (255, 255, 255)),
        ("Learn programming on Programming Navigator", width // 2, height * 3 // 4, 32, (255, 255, 255)),
    ]

    for text, x, y, size, color in texts:
        font = get_font(size, bold=True)
        # Get text bbox for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Draw text with shadow for better visibility
        draw.text((x - text_width // 2 + 2, y - text_height // 2 + 2), text,
                 fill=(0, 0, 0, 180), font=font)
        draw.text((x - text_width // 2, y - text_height // 2), text,
                 fill=color + (255,), font=font)

    # Composite images
    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")

    output_path = IMAGE_DIR / "join_us_en.png"
    result.save(output_path, "PNG")
    print(f"✓ Created {output_path.name}")
    return output_path

def create_english_coupon():
    """Create English version of coupon.jpg"""
    img_path = IMAGE_DIR / "coupon.jpg"
    if not img_path.exists():
        return None

    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    width, height = img.size

    # Red/gold festive colors
    texts = [
        ("Programmer Yu Pi", width // 2, height // 6, 40, (255, 255, 255)),
        ("Exclusive Coupon for You", width // 2, height // 3, 48, (255, 215, 0)),
        ("Instant Discount", width // 2, height // 2, 52, (255, 69, 0)),
        ("Start Your Programming Journey", width // 2, height * 2 // 3, 32, (255, 255, 255)),
        ("Programming Navigation", width // 2, height * 3 // 4, 28, (255, 255, 255)),
    ]

    for text, x, y, size, color in texts:
        font = get_font(size, bold=True)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Draw with shadow
        for offset in [3, 2, 1]:
            draw.text((x - text_width // 2 + offset, y - text_height // 2 + offset),
                     text, fill=(0, 0, 0, 100), font=font)
        draw.text((x - text_width // 2, y - text_height // 2), text,
                 fill=color + (255,), font=font)

    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")

    output_path = IMAGE_DIR / "coupon_en.jpg"
    result.save(output_path, "JPEG", quality=95)
    print(f"✓ Created {output_path.name}")
    return output_path

def create_english_11_11():
    """Create English version of 11_11.png"""
    img_path = IMAGE_DIR / "11_11.png"
    if not img_path.exists():
        return None

    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    width, height = img.size

    # Similar to coupon but for 11.11 sale
    texts = [
        ("Programmer Yu Pi", width // 2, height // 6, 36, (255, 255, 255)),
        ("Exclusive Coupon", width // 2, height // 3, 44, (255, 215, 0)),
        ("Instant Discount", width // 2, height // 2, 48, (255, 69, 0)),
        ("Start Coding Journey", width // 2, height * 2 // 3, 30, (255, 255, 255)),
        ("Programming Navigation", width // 2, height * 3 // 4, 26, (255, 255, 255)),
    ]

    for text, x, y, size, color in texts:
        font = get_font(size, bold=True)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        for offset in [2, 1]:
            draw.text((x - text_width // 2 + offset, y - text_height // 2 + offset),
                     text, fill=(0, 0, 0, 120), font=font)
        draw.text((x - text_width // 2, y - text_height // 2), text,
                 fill=color + (255,), font=font)

    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")

    output_path = IMAGE_DIR / "11_11_en.png"
    result.save(output_path, "PNG")
    print(f"✓ Created {output_path.name}")
    return output_path

def create_simple_text_image(img_path, output_path, texts):
    """Generic function to create English version with text overlays"""
    if not img_path.exists():
        return None

    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    width, height = img.size

    for text, x, y, size, color in texts:
        font = get_font(size, bold=True)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Add shadow/outline for readability
        draw.text((x - text_width // 2 + 2, y - text_height // 2 + 2),
                 text, fill=(0, 0, 0, 150), font=font)
        draw.text((x - text_width // 2, y - text_height // 2), text,
                 fill=color + (255,), font=font)

    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")
    result.save(output_path)
    print(f"✓ Created {output_path.name}")
    return output_path

def main():
    print("=" * 60)
    print("Creating English Image Versions")
    print("=" * 60)

    created_files = []

    # Process each image
    print("\n1. join_us.png")
    result = create_english_join_us()
    if result:
        created_files.append(result)

    print("\n2. coupon.jpg")
    result = create_english_coupon()
    if result:
        created_files.append(result)

    print("\n3. 11_11.png")
    result = create_english_11_11()
    if result:
        created_files.append(result)

    # For sdk_project.png, create a version with English caption
    print("\n4. sdk_project.png (keeping original + adding caption)")
    img_path = IMAGE_DIR / "sdk_project.png"
    if img_path.exists():
        img = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(img)

        # Add caption at bottom
        font = get_font(24, bold=True)
        caption = "Tracking SDK Project Practice - Tutorial Screenshot"
        bbox = draw.textbbox((0, 0), caption, font=font)

        # Draw background bar
        padding = 20
        bar_height = bbox[3] - bbox[1] + padding * 2
        draw.rectangle([(0, img.height - bar_height), (img.width, img.height)],
                      fill=(0, 0, 0, 200))

        # Draw text
        draw.text(((img.width - (bbox[2] - bbox[0])) // 2,
                 img.height - bar_height + padding),
                 caption, fill=(255, 255, 255), font=font)

        output_path = IMAGE_DIR / "sdk_project_en.png"
        img.save(output_path)
        print(f"✓ Created {output_path.name}")
        created_files.append(output_path)

    print("\n" + "=" * 60)
    print(f"Created {len(created_files)} English image versions")
    print("=" * 60)

    for f in created_files:
        print(f"  {f.name}")

    return created_files

if __name__ == "__main__":
    main()
