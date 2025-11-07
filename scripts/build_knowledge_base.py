#!/usr/bin/env python3
"""
Build knowledge base from all agency projects
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from analyzers.project_analyzer import KnowledgeBaseBuilder
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    # Load environment variables
    load_dotenv()

    # Get project paths
    project_paths_str = os.getenv("PROJECT_PATHS", "")
    if not project_paths_str:
        print("ERROR: PROJECT_PATHS environment variable not set")
        print("Please set it in .env file:")
        print("PROJECT_PATHS=/path/to/project1,/path/to/project2,...")
        sys.exit(1)

    project_paths = [p.strip() for p in project_paths_str.split(",") if p.strip()]

    print(f"\n🔍 Building knowledge base from {len(project_paths)} projects...\n")

    # Build knowledge base
    builder = KnowledgeBaseBuilder(project_paths)
    knowledge_base = builder.build()

    # Save to file
    output_path = Path(__file__).parent.parent / "knowledge_base.json"
    builder.save_to_file(str(output_path))

    # Print summary
    print("\n" + "=" * 60)
    print("📊 KNOWLEDGE BASE SUMMARY")
    print("=" * 60)
    print(f"\nProjects analyzed: {len(knowledge_base['projects'])}")

    print("\n📦 Common Tech Stack:")
    tech_summary = knowledge_base.get("tech_stack_summary", {})
    print(f"  Frameworks: {', '.join(tech_summary.get('frameworks', {}).keys())}")
    print(f"  Styling: {', '.join(tech_summary.get('styling', {}).keys())}")
    print(f"  Icons: {', '.join(tech_summary.get('icons', {}).keys())}")

    print("\n🎨 Design Insights:")
    insights = knowledge_base.get("design_insights", {})
    print(f"  Projects with bottom nav: {insights.get('uses_bottom_nav', 0)}")
    print(f"  Projects with separate mobile/desktop: {insights.get('separate_mobile_desktop', 0)}")
    print(f"  Professional icon usage: {insights.get('professional_icon_usage', 0)}/{len(knowledge_base['projects'])}")

    print("\n✓ Knowledge base saved to:", output_path)
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
