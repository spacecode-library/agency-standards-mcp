# Agency Standards MCP Server

A custom MCP server that embodies your agency's elite design and development standards. Acts as a senior developer with 15+ years of experience to generate high-quality starter projects and enforce design patterns.

## Features

### 8 Powerful Tools

1. **generate_project_starter** - Generate complete starter projects from SRS/system design
2. **generate_polish_checklist** - Review projects and create prioritized improvement lists
3. **review_ui_component** - Review UI components against agency standards
4. **review_backend_code** - Review backend code for security and quality
5. **generate_component_template** - Generate production-ready component templates
6. **get_design_guidelines** - Access agency design guidelines
7. **analyze_modal_usage** - Find modals that should be inline interactions
8. **check_mobile_desktop_separation** - Verify proper PWA mobile/desktop separation

## Quick Start

### 1. Setup

```bash
# Install dependencies
cd agency-standards-mcp
export PATH="$HOME/.local/bin:$PATH"
source .venv/bin/activate

# Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 2. Build Knowledge Base

```bash
# Analyze your projects and build knowledge base
python scripts/build_knowledge_base.py
```

This will scan the 4+ projects and extract:
- Tech stack patterns
- Component structures
- Design patterns (modal vs inline)
- Mobile/desktop patterns
- Icon usage

### 3. Test Locally

```bash
# Add to Claude Code
claude mcp add agency-standards --transport stdio -- python src/agency_mcp_server.py

# Verify
claude mcp list

# Test in Claude Code
claude
```

### 4. Try the Tools

In Claude Code session:

```
> Show me our design guidelines

> Generate a starter project for a task management app:
  SRS: Build a simple task manager with projects, tasks, and tags
  System Design: React frontend with Node.js backend, PostgreSQL database

> Review this component against our standards:
  [paste component code]

> Analyze modal usage in my project at ~/my-project

> Generate an InlineDeleteButton component
```

## Design Philosophy

### Inline-First, Professional-Always

- **Inline interactions** by default (modals only for critical confirmations, auth, alerts)
- **Professional icons** (Lucide React) - NEVER emojis
- **Separate mobile/desktop components** - not just responsive CSS
- **Smooth animations** (Framer Motion, 300ms transitions)
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **Clean, modern, slick** design

### PWA Standards

**Desktop:**
- Sidebar navigation
- Multi-column layouts
- Hover states
- Keyboard shortcuts

**Mobile:**
- Bottom navigation (4-5 items max)
- Single-column layouts
- Horizontal scrolling for cards
- Touch-optimized (48×48px hit targets)
- Safe area insets

## Project Structure

```
agency-standards-mcp/
├── src/
│   ├── agency_mcp_server.py      # Main MCP server with 8 tools
│   ├── agency_mcp_remote.py      # Remote HTTP server (Phase 4)
│   ├── analyzers/
│   │   └── project_analyzer.py   # Project pattern extraction
│   ├── skills/
│   │   └── AGENCY_STANDARDS_SKILL.md  # Complete standards document
│   └── tools/                     # Individual tool implementations
├── scripts/
│   └── build_knowledge_base.py   # Build knowledge base from projects
├── docs/
│   └── DEVELOPER_GUIDE.md        # Developer onboarding guide
├── tests/                         # Test suite
├── knowledge_base.json            # Analyzed project patterns
├── .env                           # Environment variables
└── README.md                      # This file
```

## Knowledge Base

The MCP server learns from your existing projects:

- **trainer-aide-demo**: Next.js + TypeScript + Tailwind
- **class-dash-demo**: Next.js + Supabase + React Query
- **wellness-frontend**: Vite + React + TypeScript
- **praktijk-epd-frontend-1**: Enterprise web app

Extracted patterns:
- Tech stack preferences (Next.js, Vite, TypeScript, Tailwind)
- Component organization (ui/, layout/, shared/)
- Design patterns (inline vs modal ratio)
- Mobile patterns (bottom nav, safe area insets)
- Icon libraries (Lucide React, Heroicons)

## Configuration

### Environment Variables

```bash
# .env file
ANTHROPIC_API_KEY=your_api_key_here
PROJECT_PATHS=/path/to/project1,/path/to/project2,...
ADMIN_API_KEY=admin-key-for-remote-server
SERVER_URL=http://localhost:8000
PORT=8000
```

### Update Standards

To update design standards, edit:
```
src/skills/AGENCY_STANDARDS_SKILL.md
```

To rebuild knowledge base after adding projects:
```bash
python scripts/build_knowledge_base.py
```

## Usage Examples

### Example 1: Generate Starter Project

```
User: Generate a starter project for an inventory management system

MCP Response:
- Complete Next.js + TypeScript project structure
- Separate MobileBottomNav and DesktopSidebar
- Inline delete confirmations
- Professional UI with Lucide icons
- Type-safe with Zod validation
- Ready to customize and deploy
```

### Example 2: Review Component

```
User: Review this DeleteButton component

MCP Response:
✅ Excellent: TypeScript types, professional icons
⚠️ Issue: Uses modal for confirmation (should be inline)
💡 Suggestion: [Shows inline pattern code example]
```

### Example 3: Polish Checklist

```
User: Generate polish checklist for ~/my-project

MCP Response:
## HIGH PRIORITY
- [ ] Convert 3 modals to inline interactions (locations listed)
- [ ] Add separate mobile/desktop navigation components
- [ ] Fix 5 accessibility violations

## MEDIUM PRIORITY
- [ ] Add loading states to async actions
- [ ] Implement error boundaries

[Complete prioritized checklist with time estimates]
```

## Development

### Adding New Tools

1. Add tool function to `src/agency_mcp_server.py`:
```python
@app.tool()
async def my_new_tool(param: str) -> str:
    """Tool description"""
    # Implementation
    return result
```

2. Test locally:
```bash
claude mcp remove agency-standards
claude mcp add agency-standards --transport stdio -- python src/agency_mcp_server.py
```

### Running Tests

```bash
# Run test suite
python -m pytest tests/

# Test specific tool
python src/agency_mcp_server.py --test generate_project_starter
```

## Deployment (Phase 4)

Deploy to Railway/Render/DigitalOcean for remote team access.

See `docs/DEPLOYMENT.md` for full instructions.

## Cost Estimates

**Monthly costs for 10 developers:**

- Claude API: ~$12/month
  - Project generations: ~$7.50
  - Reviews: ~$3.00
  - Misc queries: ~$1.50
- Hosting: $10-50/month
  - Railway: $5/month
  - Render: $7/month
  - DigitalOcean: $12/month

**Total: ~$20-60/month**

Very affordable for maintaining high-quality standards across your team!

## Support

- **Documentation**: See `docs/` folder
- **Issues**: Create issue in repository
- **Updates**: Pull latest changes and rebuild knowledge base

## Next Steps

1. ✅ Phase 1: Project setup - Complete
2. ✅ Phase 2: Knowledge base - Complete
3. ✅ Phase 3: MCP tools - Complete
4. ⏳ Phase 4: Remote server with authentication
5. ⏳ Phase 5: Developer onboarding system
6. ⏳ Phase 6: Deployment and testing
7. ⏳ Phase 7: Documentation and handoff

## Version

**v1.0.0** - Initial release with 8 core tools

---

Built with ❤️ for maintaining elite software development standards
