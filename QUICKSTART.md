# Quick Start Guide - Agency Standards MCP Server

## ✅ Setup Complete!

Your MCP server is configured and ready to use with:
- ✅ API key configured
- ✅ 4 projects analyzed
- ✅ 8 tools implemented
- ✅ Knowledge base built
- ✅ API connection verified

---

## 🚀 Add to Claude Code (2 minutes)

### Step 1: Add the MCP Server

```bash
export PATH="$HOME/.local/bin:$PATH"

claude mcp add agency-standards --transport stdio -- \
  python /Users/mukelakatungu/agency-standards-mcp/src/agency_mcp_server.py
```

### Step 2: Verify Connection

```bash
claude mcp list
```

You should see:
```
agency-standards: connected
```

### Step 3: Launch Claude Code

```bash
claude
```

---

## 🎯 Try Your First Commands

### 1. View Your Design Guidelines

```
> Show me our design guidelines for UI/UX
```

**What you'll get:**
- Complete UI/UX excellence standards
- Modal vs inline interaction rules
- PWA architecture requirements
- Code quality standards

---

### 2. Generate an Inline Component

```
> Generate a component template for an InlineDeleteButton that confirms deletions inline without using a modal
```

**What you'll get:**
- Complete TypeScript component
- Inline confirmation pattern
- Professional icons (Lucide)
- Smooth animations
- Accessibility built-in
- Usage examples

---

### 3. Generate a Starter Project

```
> Generate a starter project for a task management app:

SRS: Build a task manager with projects, tasks, tags, and deadlines. Users should be able to create projects, add tasks to projects, assign tags, set priorities, and mark tasks complete.

System Design:
- Frontend: Next.js with TypeScript
- Backend: Node.js with Express
- Database: PostgreSQL
- Features: Project CRUD, Task CRUD, Tag management, User authentication

Project name: task-master
Type: fullstack-pwa
```

**What you'll get:**
- Complete project structure
- Separate MobileBottomNav and DesktopSidebar
- Inline interactions (no unnecessary modals)
- Professional UI components
- TypeScript throughout
- Tailwind CSS styling
- Setup instructions
- 15-20+ key files with complete code

---

### 4. Review a Component

```
> Review this component against our standards:

[paste your component code]

Component type: button
```

**What you'll get:**
- ✅ What's excellent
- ⚠️ Issues found (High/Medium/Low priority)
- 💡 Specific suggestions with code examples
- Overall score and summary

---

### 5. Analyze Modal Usage

```
> Analyze modal usage in my project at /Users/mukelakatungu/trainer-aide-demo
```

**What you'll get:**
- List of all modals found
- Which should be inline
- Priority levels
- Inline conversion examples
- Time estimates

---

### 6. Check Mobile/Desktop Separation

```
> Check mobile/desktop separation in /Users/mukelakatungu/class-dash-demo
```

**What you'll get:**
- Analysis of mobile/desktop components
- PWA compliance score
- Missing components
- Implementation guide with code examples

---

### 7. Generate Polish Checklist

```
> Generate a polish checklist for the project at /Users/mukelakatungu/wellness-frontend focusing on UI and accessibility
```

**What you'll get:**
- High/Medium/Low priority items
- Specific locations and fixes
- Time estimates
- Standards verification

---

### 8. Get Backend Review

```
> Review this API endpoint against our backend standards:

[paste your backend code]

Code type: controller
```

**What you'll get:**
- Security analysis
- Code quality review
- Issues with priorities
- Suggested improvements with examples

---

## 💡 Pro Tips

### Be Specific
```
✅ Good: "Review this DeleteButton component for a user table"
❌ Vague: "Review this button"
```

### Provide Context
```
✅ Good: "Generate a project for inventory management with suppliers, products, and orders"
❌ Vague: "Generate a project"
```

### Iterate
```
> Generate a ConfirmationDialog component

[Review output]

> Make it inline instead of a modal, and add Framer Motion animations
```

### Reference Your Projects
```
> Generate a project similar to trainer-aide-demo but for meal planning
```

---

## 🎨 Your Agency Standards Summary

### Design Philosophy
- **Inline-first**: Modals only for critical confirmations, auth, alerts
- **Professional**: Lucide icons, never emojis
- **Separated**: Mobile and desktop are different components
- **Smooth**: 300ms animations, Framer Motion
- **Type-safe**: TypeScript everywhere

### Tech Stack (from your projects)
- **Frontend**: Next.js or Vite + React
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Components**: Radix UI, Headless UI
- **Icons**: Lucide React, Heroicons
- **Animations**: Framer Motion
- **Forms**: React Hook Form + Zod
- **State**: Zustand
- **Data**: React Query

### PWA Standards
**Desktop:**
- Sidebar navigation
- Multi-column layouts
- Hover states

**Mobile:**
- Bottom navigation (4-5 items)
- Single-column layouts
- Horizontal card scrolling
- 48×48px touch targets
- Safe area insets

---

## 🔧 Troubleshooting

### MCP Server Not Found
```bash
# Make sure path is set
export PATH="$HOME/.local/bin:$PATH"

# Re-add the server
claude mcp remove agency-standards
claude mcp add agency-standards --transport stdio -- \
  python /Users/mukelakatungu/agency-standards-mcp/src/agency_mcp_server.py
```

### API Errors
```bash
# Check your API key
cat ~/agency-standards-mcp/.env | grep ANTHROPIC_API_KEY

# Test connection
cd ~/agency-standards-mcp
source .venv/bin/activate
python scripts/test_setup.py
```

### Knowledge Base Out of Date
```bash
# Rebuild after adding new projects
cd ~/agency-standards-mcp
source .venv/bin/activate
python scripts/build_knowledge_base.py
```

---

## 📚 Available Tools Reference

| Tool | Purpose |
|------|---------|
| `generate_project_starter` | Generate complete starter projects |
| `generate_polish_checklist` | Create prioritized improvement lists |
| `review_ui_component` | Review UI components against standards |
| `review_backend_code` | Review backend code for security/quality |
| `generate_component_template` | Generate production-ready components |
| `get_design_guidelines` | Access design guidelines |
| `analyze_modal_usage` | Find modals that should be inline |
| `check_mobile_desktop_separation` | Verify PWA compliance |

---

## 🎯 Example Workflow

### Starting a New Client Project

1. **Get requirements from client meeting**
   ```
   > Show me our design guidelines to prepare for client meeting
   ```

2. **Create SRS and system design docs**

3. **Generate starter project**
   ```
   > Generate a starter project from these documents:
   [paste SRS and design]
   ```

4. **Review and customize**
   ```
   > Analyze modal usage in ./new-project
   > Check mobile/desktop separation in ./new-project
   ```

5. **Get polish checklist**
   ```
   > Generate polish checklist for ./new-project
   ```

6. **Hand off to team with standards**
   - Developers work with MCP server guidance
   - Review components as they build
   - Generate templates as needed

---

## 🚀 Next Steps

### For You (Agency Owner)
1. ✅ Test all 8 tools
2. ⏳ Set up remote server (Phase 4) for team access
3. ⏳ Create developer onboarding
4. ⏳ Deploy to production

### For Your Developers (Coming in Phase 5)
- Receive API key
- Add MCP server to their Claude Code
- Access same standards remotely
- Generate and review code with guidance

---

## 📞 Support

- **Test Setup**: `python scripts/test_setup.py`
- **Rebuild KB**: `python scripts/build_knowledge_base.py`
- **Documentation**: See `README.md` and `docs/`

---

**Ready to build elite software!** 🚀
