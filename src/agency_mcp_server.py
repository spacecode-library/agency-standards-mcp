#!/usr/bin/env python3
"""
Agency Standards MCP Server

Provides tools for generating high-quality projects following agency standards.
Acts as a senior developer with 15+ years of experience.
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from anthropic import Anthropic
from dotenv import load_dotenv
from mcp.server import FastMCP

# Load environment variables
load_dotenv()

# Initialize MCP server
app = FastMCP("agency-standards")

# Load knowledge base
KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "knowledge_base.json"
KNOWLEDGE_BASE = {}

if KNOWLEDGE_BASE_PATH.exists():
    with open(KNOWLEDGE_BASE_PATH) as f:
        KNOWLEDGE_BASE = json.load(f)

# Load agency skill document
SKILL_PATH = Path(__file__).parent / "skills" / "AGENCY_STANDARDS_SKILL.md"
AGENCY_SKILL = ""

if SKILL_PATH.exists():
    with open(SKILL_PATH) as f:
        AGENCY_SKILL = f.read()

# Initialize Anthropic client
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_claude_response(prompt: str, max_tokens: int = 8000, temperature: float = 0.3) -> str:
    """Get response from Claude"""
    try:
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        return f"Error calling Claude API: {str(e)}"


# ============================================================================
# Tool 1: generate_project_starter
# ============================================================================


@app.tool()
async def generate_project_starter(
    srs_document: str,
    system_design: str,
    project_name: str,
    project_type: str = "fullstack-pwa",
) -> str:
    """
    Generate a complete, production-ready starter project from SRS and system design.

    This tool acts as a senior full-stack developer with 15+ years of experience,
    creating projects that embody elite design standards:
    - Modern, slick, professional UI
    - Inline interactions (minimal modals)
    - Separate mobile/desktop views for PWA
    - TypeScript throughout
    - Professional icons (Lucide React)
    - Smooth animations (Framer Motion)
    - Well-organized, clean code

    Args:
        srs_document: Software Requirements Specification document
        system_design: System design document
        project_name: Name for the generated project
        project_type: Type of project (fullstack-pwa, frontend-only, backend-only)

    Returns:
        JSON structure with complete project files, setup instructions, and polish checklist
    """

    # Build comprehensive context
    context = f"""You are a senior full-stack developer with 15+ years of experience building
elite, enterprise-grade applications. Your specialty is creating modern, slick, professionally
designed systems that users love and developers enjoy working on.

=== CRITICAL: AGENCY STANDARDS ===
{json.dumps(KNOWLEDGE_BASE.get('design_insights', {}), indent=2)}

**Design Philosophy:**
- Inline interactions by default (modals ONLY for critical confirmations, auth, alerts)
- Professional icons (Lucide React) - NEVER emojis
- Separate mobile and desktop components - NOT just responsive CSS
- Smooth animations (Framer Motion, 300ms transitions)
- Clean, modern, slick design
- TypeScript for type safety
- Tailwind CSS for styling

**PWA Requirements:**
- Desktop: Sidebar navigation, multi-column layouts, hover states
- Mobile: Bottom navigation (4-5 items), single-column, horizontal scrolling for cards
- Safe area insets for devices with notches
- Touch-optimized hit targets (48×48px minimum)

=== PROJECT REQUIREMENTS ===
**SRS DOCUMENT:**
{srs_document}

**SYSTEM DESIGN:**
{system_design}

**PROJECT NAME:** {project_name}
**PROJECT TYPE:** {project_type}

=== TECH STACK (Based on your past projects) ===
{json.dumps(KNOWLEDGE_BASE.get('tech_stack_summary', {}), indent=2)}

**Recommended Stack:**
- Next.js (App Router) OR Vite + React
- TypeScript
- Tailwind CSS
- Radix UI or Headless UI
- Lucide React icons
- Framer Motion animations
- React Hook Form + Zod validation
- Zustand state management
- React Query data fetching

=== EXAMPLES FROM YOUR PAST PROJECTS ===
{json.dumps([p.get('name') for p in KNOWLEDGE_BASE.get('projects', [])[:3]], indent=2)}

Component organization patterns:
{json.dumps([p.get('folder_structure') for p in KNOWLEDGE_BASE.get('projects', [])[:2]], indent=2)}

=== YOUR MISSION ===
Generate a COMPLETE, production-ready starter project following these standards:

1. **Project Structure:**
   - Create proper folder hierarchy (components/ui, components/layout, hooks, lib, types)
   - Separate mobile and desktop components
   - Organized by feature

2. **UI Components:**
   - Inline confirmation buttons (no modals for simple actions)
   - MobileBottomNav component with safe-area-inset
   - DesktopSidebar component
   - Professional UI primitives (Button, Input, Card, etc.)

3. **Code Quality:**
   - TypeScript interfaces for all props
   - Proper error handling
   - Loading states
   - Accessibility (ARIA, semantic HTML)

4. **Mobile/Desktop:**
   - Separate components at lg breakpoint (1024px)
   - Bottom nav on mobile
   - Sidebar on desktop

=== OUTPUT FORMAT ===
Return a JSON object with this EXACT structure:

{{
  "project_name": "{project_name}",
  "project_type": "{project_type}",

  "folder_structure": {{
    "frontend/": {{
      "src/": {{
        "components/": {{
          "ui/": ["Button.tsx", "Input.tsx", "Card.tsx", ...],
          "layout/": ["DesktopSidebar.tsx", "MobileBottomNav.tsx", "Header.tsx"],
          "features/": {{
            "feature1/": ["Component1.tsx", "Component2.tsx"]
          }}
        }},
        "hooks/": ["useMediaQuery.ts", "useAuth.ts"],
        "lib/": ["utils.ts", "api.ts"],
        "types/": ["index.ts"],
        "app/": {{"page.tsx": "", "layout.tsx": ""}}
      }},
      "public/": {{}},
      "package.json": "",
      "tailwind.config.ts": "",
      "tsconfig.json": ""
    }},
    "backend/": {{
      "src/": {{
        "controllers/": [],
        "services/": [],
        "models/": [],
        "routes/": [],
        "middleware/": []
      }}
    }}
  }},

  "key_files": {{
    "frontend/src/components/layout/DesktopSidebar.tsx": "COMPLETE FILE CONTENT WITH IMPORTS",
    "frontend/src/components/layout/MobileBottomNav.tsx": "COMPLETE FILE CONTENT",
    "frontend/src/components/ui/Button.tsx": "COMPLETE FILE CONTENT",
    "frontend/src/components/ui/InlineDeleteButton.tsx": "COMPLETE FILE CONTENT (example of inline pattern)",
    "frontend/src/hooks/useMediaQuery.ts": "COMPLETE FILE CONTENT",
    "frontend/package.json": "COMPLETE FILE CONTENT",
    "frontend/tailwind.config.ts": "COMPLETE FILE CONTENT",
    "backend/src/routes/index.ts": "COMPLETE FILE CONTENT (if backend)",
    ... (include at least 15-20 key files with FULL content)
  }},

  "design_system": {{
    "colors": {{
      "primary": "#...",
      "secondary": "#...",
      ...
    }},
    "typography": {{
      "fontFamily": "Inter, sans-serif",
      ...
    }},
    "spacing": {{}},
    "icons": "lucide-react"
  }},

  "setup_instructions": [
    "1. Install dependencies: npm install",
    "2. Set up environment variables: cp .env.example .env",
    "3. Run development server: npm run dev",
    ...
  ],

  "features_implemented": [
    "✓ Separate mobile/desktop layouts",
    "✓ Bottom navigation on mobile",
    "✓ Inline interactions (minimal modals)",
    "✓ Professional icons (Lucide)",
    "✓ Type-safe with TypeScript",
    ...
  ],

  "next_steps": [
    "Polish UI animations",
    "Add more feature-specific components",
    "Implement backend API endpoints",
    ...
  ]
}}

CRITICAL REQUIREMENTS:
1. Use inline patterns for confirmations (show example InlineDeleteButton)
2. Separate MobileBottomNav and DesktopSidebar components
3. Professional icons only (Lucide React)
4. TypeScript types for everything
5. Tailwind CSS for styling
6. Include actual code, not placeholders
7. Follow the folder structure from past projects
8. Make it production-ready, not a skeleton

Generate the complete project now!"""

    # Get response from Claude
    response = get_claude_response(context, max_tokens=16000, temperature=0.2)

    return response


# ============================================================================
# Tool 2: generate_polish_checklist
# ============================================================================


@app.tool()
async def generate_polish_checklist(
    project_path: str, focus_areas: Optional[List[str]] = None
) -> str:
    """
    Generate a comprehensive polish checklist for a project.

    Reviews the project against agency standards and creates a prioritized
    list of improvements with High/Medium/Low priorities.

    Args:
        project_path: Absolute path to the project directory
        focus_areas: Optional areas to focus on (ui, ux, code-quality, accessibility, performance)

    Returns:
        Markdown checklist with prioritized improvements
    """

    if focus_areas is None:
        focus_areas = ["ui", "ux", "code-quality", "accessibility", "performance"]

    # Analyze the project if it exists
    project_info = {"exists": False, "structure": {}}

    if Path(project_path).exists():
        try:
            # Quick analysis
            project_info["exists"] = True
            project_info["has_package_json"] = (Path(project_path) / "package.json").exists()
            project_info["has_components"] = (Path(project_path) / "components").exists() or (
                Path(project_path) / "src" / "components"
            ).exists()
        except Exception as e:
            project_info["error"] = str(e)

    context = f"""You are a senior QA engineer and design expert with 15+ years of experience.
Review this project and create a comprehensive, actionable polish checklist.

=== PROJECT INFORMATION ===
Path: {project_path}
Project exists: {project_info.get('exists')}
{json.dumps(project_info, indent=2)}

=== AGENCY STANDARDS TO VERIFY ===
{AGENCY_SKILL[:5000]}  # Include relevant parts of the skill

=== FOCUS AREAS ===
{', '.join(focus_areas)}

=== ANTI-PATTERNS TO CHECK FOR ===
- ❌ Overusing modals for non-critical actions
- ❌ Mobile view as just "shrunk desktop"
- ❌ Using emojis in production UI
- ❌ Inconsistent spacing/typography
- ❌ Missing loading/error states
- ❌ Poor contrast ratios
- ❌ No separate mobile/desktop components

=== YOUR TASK ===
Create a detailed, prioritized checklist in the following format:

# Project Polish Checklist - {Path(project_path).name}

## HIGH PRIORITY (Must Fix Before Launch)

### UI/UX Critical Issues
- [ ] **Issue description**
  - **Location**: Where to find it (file:line or component name)
  - **Why**: Why it's important
  - **Fix**: Specific steps to fix it
  - **Estimated time**: X minutes/hours

### Accessibility Violations
...

### Security Concerns
...

## MEDIUM PRIORITY (Should Fix)

### Design Inconsistencies
...

### Missing States
- [ ] Add loading states to async actions
- [ ] Implement error boundaries
...

### Code Organization
...

## LOW PRIORITY (Nice to Have)

### Animation Polish
...

### Performance Optimizations
...

### Documentation
...

## Standards Verification

### ✅ Following Standards
- Professional icons (Lucide)
- TypeScript throughout
...

### ❌ Not Following Standards
- Using modals for simple confirmations (should be inline)
- No separate mobile/desktop components
...

## Estimated Total Time
**High Priority**: X hours
**Medium Priority**: Y hours
**Low Priority**: Z hours
**TOTAL**: ~XY hours

Generate a thorough, actionable checklist now!"""

    response = get_claude_response(context, max_tokens=8000)
    return response


# ============================================================================
# Tool 3: review_ui_component
# ============================================================================


@app.tool()
async def review_ui_component(
    component_code: str, component_type: str, file_path: str = ""
) -> str:
    """
    Review a UI component against agency design standards.

    Provides specific feedback on modal vs inline patterns, icon usage,
    animations, accessibility, and mobile/desktop handling.

    Args:
        component_code: The component source code
        component_type: Type (button, form, modal, inline-action, layout, card, etc.)
        file_path: Optional file path for context

    Returns:
        Detailed review with suggestions and code examples
    """

    context = f"""You are a senior frontend developer and UI/UX expert. Review this component
against our elite agency standards.

=== COMPONENT TO REVIEW ===
**Type**: {component_type}
**File**: {file_path or 'Not provided'}

```typescript
{component_code}
```

=== AGENCY STANDARDS ===
{AGENCY_SKILL[:6000]}

=== REVIEW CHECKLIST ===

**1. Modal vs Inline Pattern:**
- Is this a modal? Should it be inline instead?
- If modal is necessary (critical confirmation, auth, complex form), is it well-designed?
- Does it follow modal design requirements (backdrop blur, animations, escape key)?

**2. Icon Usage:**
- Professional icons (Lucide React)? ✓ / ✗
- No emojis? ✓ / ✗
- Consistent sizing and colors? ✓ / ✗

**3. Interaction Design:**
- Inline feedback for actions? ✓ / ✗
- Loading states? ✓ / ✗
- Error handling? ✓ / ✗
- Success confirmation? ✓ / ✗

**4. Mobile/Desktop Handling:**
- Responsive or separate components?
- Touch targets (48×48px min)? ✓ / ✗
- Mobile-specific optimizations? ✓ / ✗

**5. Animations:**
- Smooth transitions (300ms, ease-in-out)? ✓ / ✗
- Framer Motion for complex animations? ✓ / ✗
- Not too flashy? ✓ / ✗

**6. Accessibility:**
- Semantic HTML? ✓ / ✗
- ARIA labels where needed? ✓ / ✗
- Keyboard navigation? ✓ / ✗
- Focus management? ✓ / ✗
- Color contrast (WCAG AA)? ✓ / ✗

**7. TypeScript:**
- Proper types for props? ✓ / ✗
- No `any` types? ✓ / ✗
- Return type specified? ✓ / ✗

**8. Code Quality:**
- Reusable/composable? ✓ / ✗
- Well-named variables? ✓ / ✗
- Commented complex logic? ✓ / ✗
- Follows React best practices? ✓ / ✗

=== OUTPUT FORMAT ===

# Component Review: {component_type.title()}

## ✅ Excellent Points
- [Specific things done well]
- ...

## ⚠️ Issues Found

### HIGH PRIORITY
1. **[Issue title]**
   - **Problem**: [Description]
   - **Why it matters**: [Impact]
   - **Suggested fix**:
   ```typescript
   // Better approach:
   [code example]
   ```

### MEDIUM PRIORITY
...

### LOW PRIORITY
...

## 💡 Suggestions

### Alternative Pattern
[If a better pattern exists, show it with code]

### Improvements
...

## 📝 Summary
Overall score: X/10
Main strengths: ...
Main improvements needed: ...

Provide your thorough review now!"""

    response = get_claude_response(context, max_tokens=4000)
    return response


# ============================================================================
# Tool 4: review_backend_code
# ============================================================================


@app.tool()
async def review_backend_code(code: str, code_type: str, file_path: str = "") -> str:
    """
    Review backend code against agency standards.

    Checks API design, security, error handling, code organization, and performance.

    Args:
        code: The code to review
        code_type: Type (controller, service, route, model, middleware)
        file_path: Optional file path

    Returns:
        Detailed review with security and quality suggestions
    """

    context = f"""You are a senior backend developer with expertise in security and API design.
Review this {code_type} code against our agency's backend excellence standards.

=== CODE TO REVIEW ===
**Type**: {code_type}
**File**: {file_path or 'Not provided'}

```
{code}
```

=== BACKEND STANDARDS ===
**API Design:**
- RESTful conventions (proper HTTP methods)
- Consistent response format (success: true/false, data, error)
- Proper HTTP status codes
- Clear endpoint naming

**Security:**
- Input validation (Zod, Joi, class-validator)
- SQL injection prevention (parameterized queries)
- XSS protection (sanitize outputs)
- Authentication/authorization checks
- Rate limiting considerations

**Error Handling:**
- User-friendly error messages
- Proper logging (no sensitive data in logs)
- Graceful degradation
- Centralized error handling

**Code Organization:**
- Separation of concerns (controller → service → repository)
- Single responsibility principle
- DRY (Don't Repeat Yourself)
- Clear function/variable names

**Performance:**
- Efficient database queries
- Caching where appropriate
- Pagination for list endpoints
- Async/await usage

=== REVIEW CHECKLIST ===

1. **API Design**: Is the endpoint well-designed? RESTful? Clear naming?
2. **Security**: Any security vulnerabilities? Input validation? Auth checks?
3. **Error Handling**: Proper try-catch? User-friendly errors? Logging?
4. **Code Quality**: Clean? Organized? Following patterns? TypeScript types?
5. **Performance**: Efficient queries? Caching? Pagination?

=== OUTPUT FORMAT ===

# Backend Code Review: {code_type.title()}

## Security Analysis
- ✅ / ⚠️ / ❌ [Security aspect]: [Details]

## Code Quality
- ✅ / ⚠️ / ❌ [Quality aspect]: [Details]

## Issues Found

### CRITICAL (Security/Data Loss)
[If any critical issues]

### HIGH PRIORITY
[Important issues]

### MEDIUM PRIORITY
[Improvements]

## Suggested Improvements

```typescript
// Current approach:
[problematic code snippet]

// Better approach:
[improved code example]
```

## Summary
Overall: [rating/10]
Security: [Secure / Needs work / Critical issues]
Code quality: [Excellent / Good / Needs improvement]

Provide your review now!"""

    response = get_claude_response(context, max_tokens=4000)
    return response


# ============================================================================
# Tool 5: generate_component_template
# ============================================================================


@app.tool()
async def generate_component_template(
    component_name: str, component_purpose: str, should_be_inline: bool = True
) -> str:
    """
    Generate a component template following agency standards.

    Creates production-ready components with TypeScript, accessibility,
    animations, and following inline-first philosophy.

    Args:
        component_name: Name of the component (e.g., "DeleteConfirmation", "UserCard")
        component_purpose: What the component does
        should_be_inline: Whether to use inline pattern (default: True)

    Returns:
        Complete TypeScript component code with examples and documentation
    """

    context = f"""You are a senior React developer. Generate a production-ready component
following our elite agency standards.

=== COMPONENT REQUEST ===
**Name**: {component_name}
**Purpose**: {component_purpose}
**Pattern**: {'Inline interaction' if should_be_inline else 'Modal (if absolutely necessary)'}

=== AGENCY STANDARDS ===
- Professional icons (Lucide React)
- Smooth animations (Framer Motion)
- TypeScript with proper types
- Inline interactions (no modals unless critical)
- Tailwind CSS styling
- Accessibility (ARIA, keyboard nav)
- Mobile-optimized (touch targets 48×48px)

=== REQUIREMENTS ===
Generate a COMPLETE, production-ready component with:

1. **TypeScript Interfaces**
   - Props interface
   - Any internal types

2. **Functionality**
   - {'Inline confirmation pattern' if should_be_inline else 'Well-designed modal'}
   - Loading states
   - Error handling
   - Success feedback

3. **Design**
   - Professional icons (import from lucide-react)
   - Smooth animations (Framer Motion if needed)
   - Clean Tailwind styling
   - Hover/active states

4. **Accessibility**
   - ARIA labels
   - Keyboard navigation
   - Focus management
   - Semantic HTML

5. **Mobile Optimization**
   - Touch-friendly hit targets
   - Responsive design

=== OUTPUT FORMAT ===

# {component_name} Component

## Overview
[Brief description]

## Code

```typescript
// {component_name}.tsx
import {{ useState }} from 'react';
import {{ /* relevant lucide icons */ }} from 'lucide-react';
import {{ motion }} from 'framer-motion'; // if animations needed

interface {component_name}Props {{
  // Props with JSDoc comments
}}

export function {component_name}({{ ...props }}: {component_name}Props) {{
  // Component implementation
  // Include all states, handlers, etc.

  return (
    // JSX with proper structure
  );
}}
```

## Usage Example

```typescript
// Example usage in another component
import {{ {component_name} }} from './components/{component_name}';

function ParentComponent() {{
  return (
    <{component_name}
      // ... props
    />
  );
}}
```

## Props API

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| ... | ... | ... | ... |

## Accessibility Notes
- [Keyboard shortcuts]
- [Screen reader support]
- [ARIA attributes used]

## Styling Notes
- Uses Tailwind CSS
- Responsive breakpoints: ...
- Color scheme: ...

Generate the complete, production-ready component now!"""

    response = get_claude_response(context, max_tokens=4000)
    return response


# ============================================================================
# Tool 6: get_design_guidelines
# ============================================================================


@app.tool()
async def get_design_guidelines(category: Optional[str] = None) -> str:
    """
    Get agency design and development guidelines.

    Args:
        category: Optional category to filter (ui_ux, pwa, code_quality, all)

    Returns:
        Guidelines in markdown format
    """

    if category and category != "all":
        # Extract specific section from the skill document
        section_map = {
            "ui_ux": "## UI/UX Excellence Standards",
            "pwa": "## PWA Architecture Requirements",
            "code_quality": "## Code Quality Standards",
            "anti_patterns": "## Anti-Patterns to Avoid",
        }

        if category in section_map:
            # Find and return specific section
            lines = AGENCY_SKILL.split("\n")
            start_marker = section_map[category]
            start_idx = None
            end_idx = None

            for i, line in enumerate(lines):
                if start_marker in line:
                    start_idx = i
                elif start_idx is not None and line.startswith("## ") and i > start_idx:
                    end_idx = i
                    break

            if start_idx:
                section_lines = lines[start_idx: end_idx if end_idx else len(lines)]
                return "\n".join(section_lines)

    # Return full guidelines
    return f"""# Complete Agency Design Guidelines

{AGENCY_SKILL}

---

## Knowledge Base Summary

### Projects Analyzed
{json.dumps([p.get('name') for p in KNOWLEDGE_BASE.get('projects', [])], indent=2)}

### Common Tech Stack
{json.dumps(KNOWLEDGE_BASE.get('tech_stack_summary', {}), indent=2)}

### Design Insights
{json.dumps(KNOWLEDGE_BASE.get('design_insights', {}), indent=2)}
"""


# ============================================================================
# Tool 7: analyze_modal_usage
# ============================================================================


@app.tool()
async def analyze_modal_usage(project_path: str) -> str:
    """
    Analyze modal usage in a project and suggest inline alternatives.

    Scans the project for modal/dialog components and determines if they
    should be converted to inline interactions.

    Args:
        project_path: Absolute path to the project

    Returns:
        Report on modal usage with conversion suggestions and priority
    """

    modals_found = []
    project = Path(project_path)

    if not project.exists():
        return f"❌ Project path does not exist: {project_path}"

    # Search for modal/dialog components
    for pattern in ["components", "src/components", "app/components"]:
        comp_dir = project / pattern
        if comp_dir.exists():
            for file_path in comp_dir.rglob("*.tsx"):
                try:
                    content = file_path.read_text()
                    if any(
                        term in content for term in ["Dialog", "Modal", "<dialog", "Popup"]
                    ):
                        modals_found.append(
                            {
                                "file": str(file_path.relative_to(project)),
                                "snippet": content[:800],  # First 800 chars
                            }
                        )
                except Exception:
                    continue

    if not modals_found:
        return """# ✅ Modal Usage Analysis - EXCELLENT!

No modal components found in the project. Great adherence to the inline-first approach!

## Recommendation
Continue using inline patterns for user interactions. This provides a better user experience
by keeping context and reducing interruptions.
"""

    context = f"""You are a UX expert specializing in interaction design. Analyze these modal usages
and determine if they should be inline interactions instead.

=== MODALS FOUND ===
Total modals: {len(modals_found)}

{json.dumps(modals_found, indent=2)}

=== AGENCY MODAL POLICY ===
**Modals are ONLY appropriate for:**
1. Destructive confirmations (delete, permanent removal)
2. Critical alerts requiring immediate acknowledgment
3. Authentication flows (login, signup, password reset)
4. Complex multi-step forms that would lose context

**Everything else should be inline!**

=== YOUR TASK ===
For each modal found, provide:

1. **Should it be inline?** (Yes/No/Maybe)
2. **Reasoning**: Why or why not
3. **Priority**: High/Medium/Low
4. **How to convert**: If yes, provide inline pattern example
5. **Estimated time**: Time to convert

=== OUTPUT FORMAT ===

# Modal Usage Analysis Report

## Summary
- Total modals found: {len(modals_found)}
- Should be inline: [count]
- Appropriately used: [count]
- Maybe: [count]

---

{f'''
## Modal #{1}: [filename]

**Current Usage**: [What it's used for based on code]

**Should be inline?**: Yes / No / Maybe

**Reasoning**: [Detailed explanation]

**Priority**: High / Medium / Low

**Conversion Example** (if should be inline):
```typescript
// Instead of modal, use inline confirmation:
function InlineAction() {{
  const [confirming, setConfirming] = useState(false);

  if (confirming) {{
    return (
      <div className="inline-flex items-center gap-2 px-3 py-1.5 bg-red-50 border border-red-200 rounded-lg">
        <span className="text-sm text-red-900">Confirm action?</span>
        <button onClick={{handleConfirm}} className="...">
          <Check className="w-4 h-4" />
        </button>
        <button onClick={{() => setConfirming(false)}} className="...">
          <X className="w-4 h-4" />
        </button>
      </div>
    );
  }}

  return (
    <button onClick={{() => setConfirming(true)}} className="...">
      <Trash2 className="w-4 h-4" />
    </button>
  );
}}
```

**Estimated time**: X minutes

---

[Repeat for each modal]
'''}

## Overall Recommendations

### High Priority Conversions
1. [Modal that definitely should be inline]
2. ...

### Medium Priority
...

### Appropriately Used Modals
- [Modal that's correctly used as modal]
- ...

## Estimated Total Time
Converting all high-priority items: ~X hours

Analyze all modals and provide the complete report now!"""

    response = get_claude_response(context, max_tokens=6000)
    return response


# ============================================================================
# Tool 8: check_mobile_desktop_separation
# ============================================================================


@app.tool()
async def check_mobile_desktop_separation(project_path: str) -> str:
    """
    Verify that the project has separate mobile and desktop views.

    Checks for proper PWA implementation with distinct mobile and desktop
    components, not just responsive CSS.

    Args:
        project_path: Absolute path to the project

    Returns:
        Report on mobile/desktop separation with recommendations
    """

    project = Path(project_path)

    if not project.exists():
        return f"❌ Project path does not exist: {project_path}"

    analysis = {
        "mobile_components": [],
        "desktop_components": [],
        "responsive_only": [],
        "has_bottom_nav": False,
        "has_sidebar": False,
        "uses_media_query_hook": False,
        "uses_device_detection": False,
    }

    # Scan components
    for pattern in ["components", "src/components", "app/components"]:
        comp_dir = project / pattern
        if comp_dir.exists():
            for file_path in comp_dir.rglob("*.tsx"):
                try:
                    filename = file_path.name.lower()
                    content = file_path.read_text()

                    # Check for mobile-specific components
                    if "mobile" in filename:
                        analysis["mobile_components"].append(str(file_path.relative_to(project)))

                    # Check for desktop-specific components
                    if "desktop" in filename:
                        analysis["desktop_components"].append(
                            str(file_path.relative_to(project))
                        )

                    # Check for bottom nav
                    if "bottomnav" in filename or "bottom-nav" in filename:
                        analysis["has_bottom_nav"] = True

                    # Check for sidebar
                    if "sidebar" in filename:
                        analysis["has_sidebar"] = True

                    # Check for device detection
                    if "useMediaQuery" in content or "isMobile" in content:
                        analysis["uses_device_detection"] = True

                except Exception:
                    continue

    context = f"""You are a PWA and responsive design expert. Review this project's mobile/desktop
separation and provide recommendations.

=== PROJECT ANALYSIS ===
{json.dumps(analysis, indent=2)}

=== AGENCY PWA STANDARDS ===
**Required:**
- Separate mobile and desktop components (NOT just responsive CSS)
- Mobile: Bottom navigation bar (4-5 items), single-column layouts
- Desktop: Sidebar navigation, multi-column layouts
- Use `lg` breakpoint (1024px) to switch between mobile/desktop components
- Device detection: `const isMobile = useMediaQuery('(max-width: 1023px)')`

**Anti-Pattern:**
```typescript
// ❌ BAD: Just using responsive CSS
<div className="flex-col md:flex-row">
  {{/* Same component, different layouts */}}
</div>
```

**Correct Pattern:**
```typescript
// ✅ GOOD: Separate components
{{isMobile ? <MobileView /> : <DesktopView />}}
```

=== YOUR TASK ===
Analyze the project and provide a comprehensive report.

=== OUTPUT FORMAT ===

# Mobile/Desktop Separation Report

## Current State

### ✅ Strengths
- [What's done well]

### ⚠️ Issues
- [What's missing or wrong]

## Findings

### Mobile Components Found
{f'- ' + chr(10).join(['- ' + c for c in analysis['mobile_components']]) if analysis['mobile_components'] else '❌ No mobile-specific components found'}

### Desktop Components Found
{f'- ' + chr(10).join(['- ' + c for c in analysis['desktop_components']]) if analysis['desktop_components'] else '❌ No desktop-specific components found'}

### Navigation
- Bottom Nav: {'✓' if analysis['has_bottom_nav'] else '✗'}
- Sidebar: {'✓' if analysis['has_sidebar'] else '✗'}

### Device Detection
- Uses media queries: {'✓' if analysis['uses_device_detection'] else '✗'}

## Recommendations

### HIGH PRIORITY
[Critical changes needed]

### Implementation Guide

1. **Create Device Detection Hook**
```typescript
// hooks/useMediaQuery.ts
[Example code]
```

2. **Create Mobile Bottom Nav**
```typescript
// components/layout/MobileBottomNav.tsx
[Example code]
```

3. **Create Desktop Sidebar**
```typescript
// components/layout/DesktopSidebar.tsx
[Example code]
```

4. **Update Main Layout**
```typescript
// Update to switch between mobile/desktop
[Example code]
```

## Compliance Score

- Mobile-specific components: [X/10]
- Desktop-specific components: [X/10]
- Navigation patterns: [X/10]
- Overall PWA compliance: [X/10]

## Next Steps
1. [Specific actionable step]
2. [Specific actionable step]
...

Provide your complete analysis now!"""

    response = get_claude_response(context, max_tokens=5000)
    return response


# ============================================================================
# Server Initialization
# ============================================================================

if __name__ == "__main__":
    # Run the MCP server via stdio
    app.run(transport="stdio")
