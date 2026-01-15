#!/usr/bin/env python3
"""
Image Text Translation and Regeneration Script v2
Uses OpenRouter + Google Gemini 2.5 Flash to process images
"""

import os
import sys
import base64
import requests
import json
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import quote

# Configuration
OPENROUTER_API_KEY = "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"
MODEL = "google/gemini-2.5-flash"  # Full model with vision support
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Directories
REPO_ROOT = Path(__file__).parent
IMAGE_DIR = REPO_ROOT / "image"
PUBLIC_DIR = REPO_ROOT / ".vuepress" / "public"
OUTPUT_DIR = REPO_ROOT / "image_processed"

def encode_image_to_base64(image_path: str) -> str:
    """Encode image to base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_image_mime_type(image_path: str) -> str:
    """Get MIME type for image"""
    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    return mime_types.get(ext, 'image/png')

def analyze_image_with_gemini(image_path: str) -> Dict:
    """
    Analyze image using Gemini 2.5 Flash via OpenRouter
    Returns extracted text and description
    """
    try:
        base64_image = encode_image_to_base64(image_path)
        mime_type = get_image_mime_type(image_path)
        data_url = f"data:{mime_type};base64,{base64_image}"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Vijay-Duke/ai-guide",
            "X-Title": "AI Guide Image Translation"
        }

        # Using correct format for Gemini vision
        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Please analyze this image and provide the following information in JSON format:
{
  "has_text": true/false,
  "has_chinese": true/false,
  "all_text": ["extract all text visible in the image"],
  "chinese_text": ["list only Chinese text found"],
  "description": "describe the image content, layout, colors, and style",
  "text_elements": [{"text": "extracted text", "position": "describe where it appears", "style": "describe font/style"}]
}

Be thorough in extracting ALL text from the image."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url
                            }
                        }
                    ]
                }
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')

        # Try to parse as JSON
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # If response isn't valid JSON, extract what we can
            return {
                "has_text": True,
                "raw_response": content,
                "chinese_text": [],
                "description": content
            }

    except Exception as e:
        print(f"  Error analyzing {image_path}: {e}")
        return {
            "has_text": False,
            "has_chinese": False,
            "error": str(e),
            "image_path": str(image_path)
        }

def translate_text_to_english(chinese_texts: List[str], context: str) -> Dict[str, str]:
    """Translate Chinese text to English while preserving context"""
    if not chinese_texts:
        return {}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""Translate the following Chinese text to English.

Context: This is from {context}

Chinese text to translate:
{json.dumps(chinese_texts, ensure_ascii=False, indent=2)}

Return ONLY a JSON object mapping Chinese text to English translation:
{{
  "chinese_text_1": "english_translation_1",
  "chinese_text_2": "english_translation_2"
}}
"""

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')

        # Extract JSON from response
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print(f"  Warning: Could not parse translation response")
            return {}

    except Exception as e:
        print(f"  Error translating text: {e}")
        return {}

def find_all_images() -> List[Path]:
    """Find all images in the repository"""
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    images = []

    for ext in image_extensions:
        # Search in image directory
        images.extend(IMAGE_DIR.glob(f"*{ext}"))
        # Search in public directory
        images.extend(PUBLIC_DIR.rglob(f"*{ext}"))

    # Filter out node_modules and other unwanted directories
    images = [img for img in images if 'node_modules' not in str(img)]

    return sorted(set(images))

def save_report(data: Dict, filename: str):
    """Save analysis results to JSON file"""
    with open(REPO_ROOT / filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    """Main execution"""
    print("=" * 60)
    print("Image Text Translation Analysis")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Find all images
    images = find_all_images()
    print(f"\n✓ Found {len(images)} images")

    # Analyze each image
    results = []
    images_with_chinese = []

    for i, image_path in enumerate(images, 1):
        print(f"\n[{i}/{len(images)}] Processing: {image_path.name}")

        analysis = analyze_image_with_gemini(str(image_path))
        analysis['image_path'] = str(image_path)
        analysis['relative_path'] = str(image_path.relative_to(REPO_ROOT))
        analysis['file_size'] = image_path.stat().st_size

        results.append(analysis)

        # Check for Chinese text
        chinese_text = analysis.get('chinese_text', [])
        has_chinese = analysis.get('has_chinese', False) or (chinese_text and len(chinese_text) > 0)

        if has_chinese or chinese_text:
            images_with_chinese.append(analysis)
            print(f"  ⚠️  Chinese text detected!")
            if chinese_text:
                print(f"  Text: {chinese_text}")

                # Translate to English
                print(f"  → Translating...")
                translations = translate_text_to_english(
                    chinese_text,
                    f"image {image_path.name}"
                )
                analysis['english_translations'] = translations
                print(f"  ✓ Translations: {translations}")
        else:
            print(f"  ✓ No Chinese text")

        # Save progress after each image
        save_report({'results': results, 'images_with_chinese': images_with_chinese}, "image_analysis_v2.json")

    # Print summary
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)

    print(f"\nImages with Chinese text: {len(images_with_chinese)}/{len(images)}")

    if images_with_chinese:
        print("\n" + "-" * 60)
        print("IMAGES REQUIRING TRANSLATION:")
        print("-" * 60)

        for img in images_with_chinese:
            print(f"\n📸 {img['relative_path']}")
            if 'chinese_text' in img and img['chinese_text']:
                print(f"  Chinese: {img['chinese_text']}")
            if 'english_translations' in img:
                print(f"  English: {img['english_translations']}")

    print(f"\n✓ Full report saved to: image_analysis_v2.json")
    print(f"✓ Images needing translation: {len(images_with_chinese)}")

if __name__ == "__main__":
    main()
