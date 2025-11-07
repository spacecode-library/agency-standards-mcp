#!/usr/bin/env python3
"""
Test script to verify MCP server setup
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def main():
    print("🧪 Testing Agency Standards MCP Server Setup\n")
    print("=" * 60)

    # Test 1: Check .env file
    print("\n1. Environment Variables")
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key and api_key.startswith("sk-ant-"):
        print("   ✅ ANTHROPIC_API_KEY is set")
    else:
        print("   ❌ ANTHROPIC_API_KEY is missing or invalid")
        sys.exit(1)

    project_paths = os.getenv("PROJECT_PATHS", "")
    if project_paths:
        paths = [p.strip() for p in project_paths.split(",")]
        print(f"   ✅ PROJECT_PATHS configured ({len(paths)} projects)")
    else:
        print("   ⚠️  PROJECT_PATHS not set")

    # Test 2: Check knowledge base
    print("\n2. Knowledge Base")
    kb_path = Path(__file__).parent.parent / "knowledge_base.json"
    if kb_path.exists():
        import json
        with open(kb_path) as f:
            kb = json.load(f)
            projects = kb.get("projects", [])
            print(f"   ✅ Knowledge base exists ({len(projects)} projects analyzed)")
            for proj in projects:
                print(f"      - {proj.get('name')}")
    else:
        print("   ⚠️  Knowledge base not found (run: python scripts/build_knowledge_base.py)")

    # Test 3: Check skill document
    print("\n3. Agency Standards Skill")
    skill_path = Path(__file__).parent.parent / "src" / "skills" / "AGENCY_STANDARDS_SKILL.md"
    if skill_path.exists():
        size = skill_path.stat().st_size
        print(f"   ✅ Skill document exists ({size:,} bytes)")
    else:
        print("   ❌ Skill document missing")
        sys.exit(1)

    # Test 4: Check MCP server
    print("\n4. MCP Server")
    server_path = Path(__file__).parent.parent / "src" / "agency_mcp_server.py"
    if server_path.exists():
        print("   ✅ MCP server file exists")

        # Count tools
        with open(server_path) as f:
            content = f.read()
            tool_count = content.count("@app.tool()")
        print(f"   ✅ {tool_count} tools implemented")
    else:
        print("   ❌ MCP server missing")
        sys.exit(1)

    # Test 5: Test Anthropic API connection
    print("\n5. Anthropic API Connection")
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)

        # Simple test call
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=50,
            messages=[{"role": "user", "content": "Reply with just 'OK'"}]
        )

        if response.content[0].text:
            print("   ✅ API connection successful")
        else:
            print("   ⚠️  API response unexpected")
    except Exception as e:
        print(f"   ❌ API connection failed: {str(e)}")
        sys.exit(1)

    # Test 6: Check dependencies
    print("\n6. Dependencies")
    try:
        import mcp
        print("   ✅ MCP SDK installed")
    except ImportError:
        print("   ❌ MCP SDK missing")
        sys.exit(1)

    try:
        import fastapi
        print("   ✅ FastAPI installed")
    except ImportError:
        print("   ⚠️  FastAPI not installed (needed for Phase 4)")

    print("\n" + "=" * 60)
    print("\n✅ All checks passed! Your MCP server is ready to use.\n")
    print("Next steps:")
    print("1. Add to Claude Code:")
    print("   claude mcp add agency-standards --transport stdio -- \\")
    print(f"     python {server_path}")
    print("\n2. Test in Claude Code:")
    print("   claude")
    print("   > Show me our design guidelines")
    print("\n3. Generate your first project:")
    print("   > Generate a starter project for [your app idea]")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
