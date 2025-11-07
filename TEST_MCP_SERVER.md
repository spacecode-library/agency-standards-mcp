# Test Your MCP Server Locally

## ✅ Status: Connected!

Your MCP server is now connected to Claude Code and ready to test!

```
agency-standards: ✓ Connected
```

---

## 🧪 Quick Tests (5 minutes)

### Test 1: View Design Guidelines

```bash
claude
```

In the Claude Code session, type:

```
Show me our design guidelines for UI/UX
```

**Expected:** Should return your agency's UI/UX standards including modal policies, icon usage, PWA requirements.

---

### Test 2: Generate a Component Template

```
Generate an InlineDeleteButton component that confirms deletions inline without using a modal
```

**Expected:** Complete TypeScript component with:
- Inline confirmation pattern
- Lucide React icons
- Framer Motion animations
- TypeScript interfaces
- Usage examples

---

### Test 3: Review Component Code

```
Review this component:

function Button({ onClick, children }) {
  return (
    <button onClick={onClick} class="btn">
      {children}
    </button>
  );
}

Component type: button
```

**Expected:** Review highlighting:
- Missing TypeScript types
- Should use className instead of class
- Missing accessibility attributes
- Suggestions for improvements

---

### Test 4: Check Modal Policy

```
What's our agency's policy on using modals?
```

**Expected:** Clear policy stating modals only for:
- Critical confirmations
- Authentication flows
- Complex forms
- Critical alerts

---

### Test 5: Analyze Project (If you have one ready)

```
Analyze modal usage in /Users/mukelakatungu/trainer-aide-demo
```

**Expected:** Report showing:
- All modals found
- Which should be inline
- Priority levels
- Conversion examples

---

### Test 6: Check Mobile/Desktop Separation

```
Check mobile/desktop separation in /Users/mukelakatungu/trainer-aide-demo
```

**Expected:** Analysis of:
- Mobile-specific components found
- Desktop-specific components found
- PWA compliance score
- Recommendations

---

### Test 7: Generate Polish Checklist

```
Generate a polish checklist for /Users/mukelakatungu/trainer-aide-demo
```

**Expected:** Prioritized checklist:
- High priority items
- Medium priority items
- Low priority items
- Time estimates

---

### Test 8: Generate Full Project (The Big One!)

```
Generate a starter project for a simple todo app:

SRS: Build a todo list application where users can create tasks, mark them complete, filter by status, and organize with tags.

System Design:
- Frontend: Next.js with TypeScript
- State: Zustand
- Styling: Tailwind CSS
- Features: Add/edit/delete tasks, mark complete, filter, tag system

Project name: todo-master
Type: fullstack-pwa
```

**Expected:** JSON response with:
- Complete folder structure
- 15-20+ key files with full code
- MobileBottomNav component
- DesktopSidebar component
- Inline confirmation patterns
- Professional UI
- TypeScript throughout
- Setup instructions

---

## 📊 Test Checklist

After running tests, verify:

### Tool Functionality
- [ ] Design guidelines display correctly
- [ ] Component generation works
- [ ] Component review provides detailed feedback
- [ ] Modal analysis finds modal components
- [ ] Mobile/desktop check analyzes properly
- [ ] Polish checklist is comprehensive
- [ ] Backend code review works (if you test it)
- [ ] Project generation creates complete structure

### Output Quality
- [ ] Responses follow your agency standards
- [ ] Code examples are complete (not placeholders)
- [ ] TypeScript types are included
- [ ] Recommendations are specific and actionable
- [ ] Examples use Lucide icons (not emojis)
- [ ] Mobile/desktop separation is emphasized

### Performance
- [ ] Responses return within reasonable time (~10-30 seconds)
- [ ] No timeout errors
- [ ] API key working correctly

---

## 🐛 Troubleshooting

### "MCP server not connected"
```bash
# Remove and re-add
export PATH="$HOME/.local/bin:$PATH"
claude mcp remove agency-standards
claude mcp add agency-standards --transport stdio -- \
  /Users/mukelakatungu/agency-standards-mcp/run_mcp_server.sh

# Verify
claude mcp list
```

### "API Error" or "Rate Limit"
- Check API key in `.env`
- Wait a minute and try again
- Reduce request frequency

### "Tool not found"
- Restart Claude Code session
- Verify MCP server is connected: `claude mcp list`

### Slow responses
- Normal for project generation (can take 20-30 seconds)
- Check internet connection
- Verify Anthropic API status

---

## ✅ Success Criteria

Your MCP server is working correctly if:

1. ✅ All 8 tools respond without errors
2. ✅ Generated code follows your standards
3. ✅ Recommendations are specific and actionable
4. ✅ No placeholder code (like "// Add implementation here")
5. ✅ TypeScript types are complete
6. ✅ Professional icons (Lucide) are used
7. ✅ Inline patterns are preferred over modals

---

## 🚀 Ready for Railway Deployment?

Once local testing is successful:

1. ✅ Verify all 8 tools work
2. ✅ Generate at least one test project
3. ✅ Confirm output quality meets your standards
4. 🚀 Proceed to Railway deployment

---

## 📝 Test Results Template

Record your test results:

```
Date: ___________
Tester: ___________

Test 1 - Design Guidelines: ✅ / ❌
Test 2 - Component Generation: ✅ / ❌
Test 3 - Component Review: ✅ / ❌
Test 4 - Modal Policy: ✅ / ❌
Test 5 - Modal Analysis: ✅ / ❌
Test 6 - Mobile/Desktop Check: ✅ / ❌
Test 7 - Polish Checklist: ✅ / ❌
Test 8 - Project Generation: ✅ / ❌

Overall: ✅ Ready for deployment / ❌ Needs fixes

Notes:
_______________________
_______________________
```

---

**Next Step:** Once you've tested and confirmed everything works, we'll deploy to Railway!
