# Developer Onboarding - Agency Standards MCP Server

Welcome to the team! This guide will help you set up access to our Agency Standards MCP Server.

---

## What You're Getting

An AI-powered development assistant that:

✅ **Generates starter projects** matching our quality standards
✅ **Reviews your code** against agency best practices
✅ **Provides component templates** with proper patterns
✅ **Enforces design standards** (inline-first, professional icons, PWA)
✅ **Checks mobile/desktop separation** for PWA compliance
✅ **Analyzes modal usage** and suggests inline alternatives
✅ **Creates polish checklists** for your projects
✅ **Reviews backend code** for security and quality

---

## Quick Setup (5 minutes)

### Step 1: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### Step 2: Add Agency MCP Server

**Your API Key:** `[YOUR_API_KEY_HERE]`

```bash
claude mcp add agency-standards \
  --transport http \
  -e API_KEY=[YOUR_API_KEY_HERE] \
  https://[SERVER_URL]/mcp
```

### Step 3: Verify Connection

```bash
claude mcp list
```

You should see:
```
agency-standards: ✓ Connected
```

### Step 4: Test It!

```bash
claude
```

In Claude Code:
```
> Show me our design guidelines
```

---

## Available Tools

### 1. 📋 Get Design Guidelines

```
> Show me our design guidelines for UI/UX
```

**Use when:** Starting a new feature, reviewing designs, preparing for client meetings

---

### 2. 🚀 Generate Starter Project

```
> Generate a starter project for [description]:

SRS: [Paste your SRS document]
System Design: [Paste system design]
Project name: project-name
Type: fullstack-pwa
```

**Use when:** Starting a new project after client requirements are gathered

**What you get:**
- Complete folder structure
- 15-20+ key files with code
- Separate mobile/desktop components
- Type-safe TypeScript
- Professional UI
- Setup instructions

---

### 3. 🔍 Review UI Component

```
> Review this component:

[paste your component code]

Component type: button / form / modal / layout / etc.
```

**Use when:** After writing a component, before committing code

**What you get:**
- What's excellent
- Issues (High/Medium/Low priority)
- Specific suggestions
- Code examples

---

### 4. 🎨 Generate Component Template

```
> Generate a [ComponentName] component for [purpose]

Should it be inline: yes / no
```

**Examples:**
- "Generate an InlineDeleteButton component"
- "Generate a UserProfileCard component"
- "Generate a FilterDropdown component"

---

### 5. ✅ Generate Polish Checklist

```
> Generate a polish checklist for /path/to/project
```

**Use when:** Project is "feature complete" but needs refinement

**What you get:**
- High priority fixes
- Medium priority improvements
- Low priority enhancements
- Time estimates

---

### 6. 📱 Check Mobile/Desktop Separation

```
> Check mobile/desktop separation in /path/to/project
```

**Use when:** Building PWA, want to verify proper mobile/desktop handling

---

### 7. 🔎 Analyze Modal Usage

```
> Analyze modal usage in /path/to/project
```

**Use when:** Want to find modals that should be inline interactions

---

### 8. 🔧 Review Backend Code

```
> Review this backend code:

[paste code]

Code type: controller / service / route / model
```

**Use when:** After writing API endpoints, services, or database code

---

## Our Design Standards (Quick Reference)

### ✅ DO

**UI/UX:**
- ✅ Inline interactions (confirmations, notifications, feedback)
- ✅ Professional icons (Lucide, Heroicons)
- ✅ Smooth animations (Framer Motion, 300ms)
- ✅ TypeScript everywhere
- ✅ Separate mobile & desktop components

**PWA:**
- ✅ Desktop: Sidebar navigation
- ✅ Mobile: Bottom navigation (4-5 items)
- ✅ Touch targets 48×48px minimum
- ✅ Safe area insets

**Code:**
- ✅ TypeScript types for everything
- ✅ Accessibility (ARIA, semantic HTML)
- ✅ Error handling & loading states
- ✅ Clean, organized structure

### ❌ DON'T

- ❌ Modals for simple confirmations (use inline)
- ❌ Emojis in production UI (use professional icons)
- ❌ Mobile as "shrunk desktop" (separate components!)
- ❌ Missing TypeScript types
- ❌ Hardcoded values
- ❌ Poor contrast ratios

---

## Example Workflows

### Workflow 1: New Project

```
1. Receive client requirements
2. Create SRS and system design docs
3. Ask MCP: "Generate starter project from these docs"
4. Review generated code
5. Customize and build features
6. Ask MCP: "Generate polish checklist"
7. Polish and deliver
```

### Workflow 2: Code Review

```
1. Write a component
2. Ask MCP: "Review this component against our standards"
3. Fix issues based on feedback
4. Commit code
```

### Workflow 3: Ensuring Quality

```
1. Project is "done"
2. Ask MCP: "Analyze modal usage in ./my-project"
3. Convert modals to inline where suggested
4. Ask MCP: "Check mobile/desktop separation"
5. Fix separation issues
6. Ask MCP: "Generate polish checklist"
7. Complete checklist items
8. Deliver polished project
```

---

## Tips & Best Practices

### Be Specific

✅ Good: "Review this DeleteButton component for a user management table"
❌ Vague: "Review this button"

### Provide Context

✅ Good: "Generate a project for inventory management with suppliers, products, orders"
❌ Vague: "Generate a project"

### Iterate

```
> Generate a ConfirmationDialog component

[Review output]

> Make it inline instead of a modal
```

### Use for Learning

The MCP server provides examples and explanations. Read them to understand our standards better!

---

## FAQs

**Q: Can I use the MCP server for personal projects?**
A: The MCP server is for agency projects only.

**Q: What if I disagree with a suggestion?**
A: The MCP server suggests best practices based on agency standards. If you have a good reason to deviate, discuss with your tech lead.

**Q: Can I generate an entire app?**
A: The MCP server generates high-quality starter projects. You'll still need to build features, integrate APIs, and test thoroughly.

**Q: What if the API is slow?**
A: Project generation can take 20-30 seconds. Other tools are faster (5-10 seconds).

**Q: What if I get rate limited?**
A: You have 100 requests/minute. If you hit this, wait a minute. If consistently hitting limits, contact admin.

---

## Troubleshooting

### "MCP server not connected"

```bash
# Remove and re-add
claude mcp remove agency-standards
claude mcp add agency-standards --transport http -e API_KEY=[YOUR_KEY] [SERVER_URL]
```

### "Invalid API key"

Contact your tech lead for a new API key.

### "Rate limit exceeded"

Wait 60 seconds and try again.

### Tool not responding

- Check internet connection
- Verify API key is correct
- Restart Claude Code session

---

## Getting Help

- **Documentation**: [Link to docs]
- **Tech Lead**: [Contact info]
- **Slack**: #dev-mcp-support

---

## Your Checklist

Setup complete when you've:

- [ ] Installed Claude Code
- [ ] Added agency MCP server
- [ ] Verified connection (`claude mcp list` shows ✓ Connected)
- [ ] Tested design guidelines command
- [ ] Read this documentation
- [ ] Understand the 8 tools available
- [ ] Know when to use each tool

---

**Welcome aboard! Build amazing things!** 🚀
