#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO 增强脚本 - 1H Crypto
==========================
为没有 Article Schema 的页面自动添加结构化数据。

OG/Twitter/Canonical 已在 BaseLayout.astro 中全局包含，无需重复添加。

使用：
  python scripts/enhance_seo.py              # 实际写入
  python scripts/enhance_seo.py --dry-run     # 只检查不修改
"""

import os
import re
import json
import sys
import argparse
from datetime import datetime, timezone, timedelta

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_ROOT  = os.path.join(SITE_ROOT, "src")


def extract_page_info(filepath):
    """从 .astro 文件中提取标题/描述/lang"""
    content = open(filepath, "r", encoding="utf-8").read()
    info = {
        "hasSchema": "application/ld+json" in content,
        "title":       "",
        "description": "",
        "lang":        "zh",
        "urlPath":     "",
    }
    # 从 <BaseLayout title="..."> 中提取
    m = re.search(r'<BaseLayout[^>]*title=\{?["\'](.*?)["\']\}?', content)
    if m:
        info["title"] = m.group(1).replace("\\", "")
    # description
    m = re.search(r'description=\{?["\'](.*?)["\']\}?', content)
    if m:
        info["description"] = m.group(1)[:120]
    # lang
    m = re.search(r'lang=\{?["\'](zh|en)["\']\}?', content)
    if m:
        info["lang"] = m.group(1)
    # 计算 URL 路径
    rel = os.path.relpath(filepath, os.path.join(SRC_ROOT, "pages"))
    url_path = "/" + rel.replace("\\", "/").replace("/index.astro", "/").replace(".astro", "/")
    url_path = re.sub(r"/+$", "/", url_path)
    info["urlPath"] = url_path
    return info, content


def generate_schema_html(title, description, lang, url):
    """生成 Article Schema script 标签（Astro 格式）"""
    lang_code = "zh-CN" if lang == "zh" else "en-US"
    site_name = "1H币研" if lang == "zh" else "1H Crypto"
    date_now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    schema = {
        "@context":        "https://schema.org",
        "@type":           "Article",
        "headline":        title,
        "description":     description,
        "image": {
            "@type":  "ImageObject",
            "url":    "https://1hcrypto.com/og-default.png",
            "width":  1200,
            "height": 630,
        },
        "datePublished":  date_now,
        "dateModified":   date_now,
        "author": {
            "@type": "Person",
            "name": "1H Crypto Trader",
        },
        "publisher": {
            "@type": "Organization",
            "name": site_name,
            "logo": {
                "@type": "ImageObject",
                "url": "https://1hcrypto.com/favicon.svg",
            },
        },
        "mainEntityOfPage": {
            "@type": "@id",
            "@id":  "https://1hcrypto.com" + url,
        },
    }
    # Astro 中需要用 set:html 来输出不转义的 JSON
    schema_json = json.dumps(schema, ensure_ascii=False, indent=2)
    # 转义 Astro 模板中的 { 和 }
    schema_json_escaped = schema_json.replace("{", "{{").replace("}", "}}")
    return (
        '\n  <script type="application/ld+json" set:html={`'
        + schema_json
        + '`}></script>\n'
    )


def scan_pages():
    """扫描所有 .astro 页面"""
    issues = []
    pages_dir = os.path.join(SRC_ROOT, "pages")
    for root, _, files in os.walk(pages_dir):
        for fname in files:
            if not fname.endswith(".astro"):
                continue
            fpath = os.path.join(root, fname)
            info, _ = extract_page_info(fpath)
            if not info["hasSchema"]:
                relpath = os.path.relpath(fpath, SITE_ROOT)
                issues.append({
                    "file":    fpath,
                    "relpath": relpath,
                    "lang":    info["lang"],
                    "title":   info["title"],
                })
    return issues


def main():
    parser = argparse.ArgumentParser(description="SEO enhancement for 1H Crypto")
    parser.add_argument("--dry-run", action="store_true", help="Scan only, do not modify")
    args = parser.parse_args()

    print("🔍 Scanning for missing Article Schema...\n")
    issues = scan_pages()

    if not issues:
        print("✅ All pages already have Article Schema!")
        return

    print(f"Found {len(issues)} pages without Article Schema:\n")
    for item in issues[:10]:
        print(f"  📄 {item['relpath']}")
    if len(issues) > 10:
        print(f"  ... and {len(issues) - 10} more\n")

    if args.dry_run:
        print("[DRY-RUN] No files modified.")
        return

    print("\n🔧 Adding Article Schema to pages...\n")
    fixed = 0
    for item in issues:
        fpath    = item["file"]
        info, content = extract_page_info(fpath)
        schema_html = generate_schema_html(
            info["title"] or item["title"] or "1H Crypto",
            info["description"] or "Crypto price action analysis",
            info["lang"],
            info["urlPath"],
        )
        # 插入到 <BaseLayout ...> 之前
        new_content = content.replace("<BaseLayout", schema_html + "<BaseLayout", 1)
        if new_content == content:
            print(f"  ⚠️  SKIP (no <BaseLayout> found): {item['relpath']}")
            continue
        open(fpath, "w", encoding="utf-8").write(new_content)
        fixed += 1
        print(f"  ✅ {item['relpath']}")

    print(f"\n✅ Added Article Schema to {fixed} page(s).")
    print("\n📋 Next steps:")
    print("  1. Run: npm run build")
    print("  2. Verify with: npx @astrojs/sitemap --check")
    print("  3. Submit sitemap to Google Search Console")


if __name__ == "__main__":
    main()
