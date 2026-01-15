#!/usr/bin/env python3
"""
Efficient Image Text Translation and Regeneration
Processes images with Chinese text and creates English versions
"""

import os
import sys
import base64
import requests
import json
from pathlib import Path
from typing import List, Dict, Optional
# from PIL import Image, ImageDraw, ImageFont  # Will need for image editing later
# import io

# Configuration
OPENROUTER_API_KEY = "YOUR_API_KEY_HERE"
MODEL_VISION = "google/gemini-2.5-flash"
MODEL_TEXT = "google/gemini-2.5-flash"  # Use paid model for translations too
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Directories
REPO_ROOT = Path(__file__).parent
IMAGE_DIR = REPO_ROOT / "image"
PUBLIC_DIR = REPO_ROOT / ".vuepress" / "public"
OUTPUT_DIR = REPO_ROOT / "image_en"
OUTPUT_DIR.mkdir(exist_ok=True)

def encode_image(image_path: str) -> str:
    """Encode image to base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def extract_text_from_image(image_path: str) -> Dict:
    """Extract Chinese text from image using Gemini Vision"""
    try:
        base64_image = encode_image(image_path)
        mime_type = "image/png" if image_path.endswith('.png') else "image/jpeg"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL_VISION,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analyze this image and extract all Chinese text. Return JSON:
{
  "has_chinese": boolean,
  "chinese_text": ["list of all Chinese text found"],
  "image_type": "screenshot|poster|banner|icon|qrcode|other",
  "description": "brief description",
  "background_color": "dominant background color",
  "text_positions": [{"text": "chinese text", "area": "where it appears"}]
}"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}
                        }
                    ]
                }
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')

        # Extract JSON from markdown response
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0].strip()
        elif '```' in content:
            content = content.split('```')[1].split('```')[0].strip()

        return json.loads(content)

    except Exception as e:
        return {"error": str(e), "has_chinese": False}

def translate_to_english(chinese_texts: List[str], context: str) -> Dict[str, str]:
    """Translate Chinese text to English"""
    if not chinese_texts:
        return {}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""Translate these Chinese phrases to English. Context: {context}

Chinese:
{json.dumps(chinese_texts, ensure_ascii=False, indent=2)}

Return ONLY this JSON format:
{{
  "chinese1": "english1",
  "chinese2": "english2"
}}"""

    payload = {
        "model": MODEL_TEXT,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '')

        # Extract JSON
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0].strip()
        elif '```' in content:
            content = content.split('```')[1].split('```')[0].strip()

        return json.loads(content)
    except:
        return {}

def process_images():
    """Process all images with Chinese text"""
    # Target images (exclude icons, qrcodes)
    target_images = [
        "image/join_us.png",
        "image/coupon.jpg",
        "image/11_11.png",
        "image/sdk_project.png"
    ]

    results = []

    for rel_path in target_images:
        image_path = REPO_ROOT / rel_path
        if not image_path.exists():
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {rel_path}")
        print('='*60)

        # Extract text
        print("Extracting Chinese text...")
        analysis = extract_text_from_image(str(image_path))

        if analysis.get('error'):
            print(f"  Error: {analysis['error']}")
            continue

        chinese_text = analysis.get('chinese_text', [])
        has_chinese = analysis.get('has_chinese', False)

        if not has_chinese or not chinese_text:
            print("  ✓ No Chinese text found")
            continue

        print(f"  Chinese text found: {chinese_text}")

        # Translate
        print("\nTranslating to English...")
        translations = translate_to_english(chinese_text, rel_path)
        print(f"  Translations: {translations}")

        # Save original and analysis
        output_data = {
            "image_path": rel_path,
            "chinese_text": chinese_text,
            "english_translations": translations,
            "analysis": analysis
        }
        results.append(output_data)

    # Save results
    with open(REPO_ROOT / "image_translations.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Images processed: {len(results)}")
    print(f"Results saved to: image_translations.json")

    # Print translation table
    print("\n" + "-"*60)
    print("TRANSLATION TABLE:")
    print("-"*60)
    for r in results:
        print(f"\n📸 {r['image_path']}")
        for cn, en in r['english_translations'].items():
            print(f"  CN: {cn}")
            print(f"  EN: {en}")

if __name__ == "__main__":
    process_images()
