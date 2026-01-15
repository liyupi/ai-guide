#!/usr/bin/env python3
"""
Image Text Translation and Regeneration Script
Uses OpenRouter + Google Gemini 2.5 Flash to process images
"""

import os
import sys
import base64
import requests
import json
from pathlib import Path
from typing import List, Dict, Optional

# Configuration
OPENROUTER_API_KEY = "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"
MODEL = "google/gemini-2.5-flash-image"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Directories
REPO_ROOT = Path(__file__).parent
IMAGE_DIR = REPO_ROOT / "image"
PUBLIC_DIR = REPO_ROOT / ".vuepress" / "public"

def encode_image(image_path: str) -> str:
    """Encode image to base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_gemini(image_path: str) -> Dict:
    """
    Analyze image using Gemini 2.5 Flash via OpenRouter
    Returns extracted text and description
    """
    try:
        base64_image = encode_image(image_path)

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ai.codefather.cn",
            "X-Title": "AI Guide Translation"
        }

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analyze this image and respond in JSON format:
{
  "has_chinese_text": boolean,
  "chinese_text": ["list of chinese text found"],
  "image_description": "detailed description of the image",
  "visual_elements": ["list of visual elements like icons, buttons, layouts"],
  "suggested_english_text": {"chinese_text": "english_translation"},
  "text_positions": [{"text": "chinese text", "position": "description of where it appears"}]
}

If no Chinese text is found, set has_chinese_text to false and return empty arrays."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "response_format": {"type": "json_object"}
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()
        content = result['choices'][0]['message']['content']

        return json.loads(content)

    except Exception as e:
        print(f"Error analyzing {image_path}: {e}")
        return {
            "has_chinese_text": False,
            "error": str(e)
        }

def find_all_images() -> List[Path]:
    """Find all images in the repository"""
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']
    images = []

    for ext in image_extensions:
        # Search in image directory
        images.extend(IMAGE_DIR.glob(f"*{ext}"))
        # Search in public directory
        images.extend(PUBLIC_DIR.rglob(f"*{ext}"))

    # Filter out node_modules and other unwanted directories
    images = [img for img in images if 'node_modules' not in str(img)]

    return sorted(set(images))

def save_analysis_report(images_data: List[Dict], output_path: Path):
    """Save analysis results to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(images_data, f, indent=2, ensure_ascii=False)

def main():
    """Main execution"""
    print("=" * 60)
    print("Image Text Translation Analysis")
    print("=" * 60)

    # Find all images
    images = find_all_images()
    print(f"\nFound {len(images)} images")

    # Analyze each image
    results = []

    for i, image_path in enumerate(images, 1):
        print(f"\n[{i}/{len(images)}] Analyzing: {image_path}")

        analysis = analyze_image_with_gemini(str(image_path))
        analysis['image_path'] = str(image_path)
        analysis['relative_path'] = str(image_path.relative_to(REPO_ROOT))

        results.append(analysis)

        if analysis.get('has_chinese_text'):
            print(f"  ⚠️  Chinese text found!")
            if 'chinese_text' in analysis:
                print(f"  Text: {analysis['chinese_text']}")
        else:
            print(f"  ✓ No Chinese text")

        # Save progress after each image
        save_analysis_report(results, REPO_ROOT / "image_analysis_report.json")

    # Print summary
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)

    images_with_chinese = [r for r in results if r.get('has_chinese_text')]
    print(f"\nImages with Chinese text: {len(images_with_chinese)}/{len(images)}")

    if images_with_chinese:
        print("\nImages needing translation:")
        for img in images_with_chinese:
            print(f"  - {img['relative_path']}")
            if 'chinese_text' in img:
                print(f"    Text: {img['chinese_text']}")

    print(f"\nFull report saved to: image_analysis_report.json")

if __name__ == "__main__":
    main()
