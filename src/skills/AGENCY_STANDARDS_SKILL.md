# Agency Standards Skill - Elite Software Development Standards

## Overview
This skill defines the comprehensive design and development standards for a high-quality software agency specializing in modern, intuitive, professionally-designed enterprise systems and PWA web applications.

## Core Philosophy

### "Inline-First, Professional-Always"
- Minimize modal dialogs - prefer inline interactions
- Professional iconography - never emojis in production UI
- Separate mobile and desktop experiences - not just responsive CSS
- Clean, modern, slick design that users love
- Well-organized, easy-to-understand code

---

## UI/UX Excellence Standards

### Visual Quality Requirements

**Design Aesthetic:**
- ✓ Modern, slick, and professional appearance
- ✓ Clean layouts with intentional whitespace
- ✓ Consistent design system (colors, typography, spacing)
- ✓ High contrast ratios for accessibility (WCAG AA minimum)
- ✓ Professional color palettes (avoid overly saturated colors)

**Iconography:**
- ✓ Use professional icon libraries:
  - **Lucide React** (preferred)
  - **Heroicons** (acceptable)
  - **Phosphor Icons** (acceptable)
- ✗ **NEVER** use emojis in production UI
- ✓ Consistent icon sizing (typically 20px-24px for UI elements)
- ✓ Icon colors should match design system

**Animations:**
- ✓ Smooth, subtle animations (300ms duration)
- ✓ Use easing functions: `ease-in-out`, `cubic-bezier(0.4, 0, 0.2, 1)`
- ✓ Spring animations for interactive elements (Framer Motion)
- ✓ Micro-interactions for feedback (hover, tap, focus)
- ✓ Loading states with skeleton screens or spinners
- ✗ Avoid jarring or overly flashy animations

---

### Interaction Design Philosophy

**Inline-First Approach:**
```
RULE: Use inline interactions by default. Modals are the exception, not the rule.
```

**When to use INLINE patterns:**
- ✓ Simple confirmations (delete, edit, save)
- ✓ Form validation and error messages
- ✓ Success notifications
- ✓ Filter and sort controls
- ✓ Quick actions (archive, favorite, share)
- ✓ Dropdown menus and popovers
- ✓ Expandable sections and accordions

**When modals ARE appropriate:**
- Critical destructive confirmations (permanent deletion, data loss)
- Authentication flows (login, signup, password reset)
- Complex forms that would lose context if navigated away
- Critical alerts requiring user acknowledgment
- Multi-step processes with clear beginning/end

**Modal Design Requirements (when necessary):**
```typescript
// Well-designed modal checklist:
- [ ] Backdrop blur effect (backdrop-blur-sm)
- [ ] Smooth entrance/exit animations (fade + scale)
- [ ] Clear primary and secondary actions
- [ ] Escape key to close
- [ ] Click outside to close (for non-critical modals)
- [ ] Focus trap for accessibility
- [ ] Max-width constraints (max-w-lg or max-w-2xl)
- [ ] Mobile-responsive (full-screen on mobile if needed)
```

**Example: Inline Delete Confirmation**
```typescript
import { useState } from 'react';
import { Trash2, Check, X } from 'lucide-react';

function InlineDeleteButton({ itemName, onDelete }: Props) {
  const [confirming, setConfirming] = useState(false);
  const [deleting, setDeleting] = useState(false);

  if (confirming) {
    return (
      <div className="inline-flex items-center gap-2 px-3 py-1.5 bg-red-50 border border-red-200 rounded-lg">
        <span className="text-sm text-red-900">Delete "{itemName}"?</span>
        <button
          onClick={async () => {
            setDeleting(true);
            await onDelete();
          }}
          disabled={deleting}
          className="p-1 text-red-600 hover:bg-red-100 rounded transition-colors"
        >
          <Check className="w-4 h-4" />
        </button>
        <button
          onClick={() => setConfirming(false)}
          disabled={deleting}
          className="p-1 text-gray-600 hover:bg-gray-100 rounded transition-colors"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    );
  }

  return (
    <button
      onClick={() => setConfirming(true)}
      className="p-2 text-gray-600 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
    >
      <Trash2 className="w-4 h-4" />
    </button>
  );
}
```

---

### Form & Validation Standards

**Form Design:**
- ✓ Inline validation (validate on blur, show errors below fields)
- ✓ Clear, helpful error messages (not technical jargon)
- ✓ Success states with checkmarks or green borders
- ✓ Loading states on submit buttons
- ✓ Disabled state styling for unavailable actions

**Error Handling:**
```typescript
// Good: Inline error message
<div>
  <input type="email" />
  {error && (
    <p className="mt-1 text-sm text-red-600 flex items-center gap-1">
      <AlertCircle className="w-4 h-4" />
      {error}
    </p>
  )}
</div>

// Bad: Modal for simple validation error
❌ <Modal isOpen={hasError}>Email is invalid</Modal>
```

---

## PWA Architecture Requirements

### Critical Rule: Separate Components for Mobile and Desktop

```
❌ BAD: Using only responsive CSS
<div className="flex-col md:flex-row">
  {/* Same component, different layouts */}
</div>

✓ GOOD: Separate components
{isMobile ? <MobileView /> : <DesktopView />}
```

### Desktop View Requirements

**Layout:**
- ✓ Sidebar navigation (fixed or collapsible)
- ✓ Multi-column layouts where appropriate
- ✓ Generous padding and spacing
- ✓ Hover states for all interactive elements
- ✓ Tooltips for additional context
- ✓ Keyboard shortcuts support
- ✓ Larger hit targets (40×40px minimum)

**Navigation:**
- ✓ Persistent sidebar with clear hierarchy
- ✓ Breadcrumbs for deep navigation
- ✓ Search functionality prominently placed
- ✓ Quick actions in header/toolbar

**Example Desktop Sidebar:**
```typescript
// components/layout/DesktopSidebar.tsx
export function DesktopSidebar() {
  return (
    <aside className="hidden lg:flex fixed left-0 top-0 bottom-0 w-64 bg-white border-r border-gray-200 flex-col">
      {/* Logo */}
      <div className="p-6">
        <Logo />
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-3">
        {navItems.map(item => (
          <Link
            key={item.id}
            href={item.href}
            className="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-gray-100 transition-colors group"
          >
            <item.icon className="w-5 h-5 text-gray-600 group-hover:text-gray-900" />
            <span>{item.label}</span>
          </Link>
        ))}
      </nav>
    </aside>
  );
}
```

---

### Mobile View Requirements

**Think "Native App", Not "Shrunk Website"**

**Layout:**
- ✓ Bottom navigation bar (4-5 items maximum)
- ✓ Single-column layouts
- ✓ Horizontal scrolling for card collections
- ✓ Touch-optimized hit targets (48×48px minimum)
- ✓ Safe area insets for devices with notches
- ✗ NO hover states (use tap/press states instead)
- ✓ Large, thumb-friendly buttons
- ✓ Pull-to-refresh pattern
- ✓ Swipe gestures (back, delete)

**Navigation:**
- ✓ Bottom tab bar with 4-5 main sections
- ✓ Icons + labels for clarity
- ✓ Active state clearly visible
- ✓ Smooth animations between tabs

**Example Mobile Bottom Nav:**
```typescript
// components/layout/MobileBottomNav.tsx
export function MobileBottomNav() {
  const pathname = usePathname();

  return (
    <motion.nav
      initial={{ y: 100 }}
      animate={{ y: 0 }}
      className="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-xl border-t border-gray-200"
    >
      <div
        className="flex items-center justify-around px-4 pt-2 pb-1"
        style={{ paddingBottom: 'max(0.25rem, env(safe-area-inset-bottom))' }}
      >
        {navItems.map(item => {
          const isActive = pathname.startsWith(item.href);
          return (
            <Link
              key={item.id}
              href={item.href}
              className="flex flex-col items-center py-1.5 px-2 min-w-0 flex-1"
            >
              <motion.div
                whileTap={{ scale: 0.88 }}
                className={`p-2 rounded-2xl transition-all ${
                  isActive
                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-600/30'
                    : 'text-gray-500'
                }`}
              >
                <item.icon className="w-5 h-5" />
              </motion.div>
              <span className="text-[10px] font-semibold mt-0.5">
                {item.label}
              </span>
            </Link>
          );
        })}
      </div>
    </motion.nav>
  );
}
```

**Card Layouts on Mobile:**
```typescript
// Horizontal scrolling for card collections
<div className="overflow-x-auto -mx-4">
  <div className="flex gap-4 px-4 pb-4">
    {items.map(item => (
      <Card key={item.id} className="flex-shrink-0 w-72">
        {/* Card content */}
      </Card>
    ))}
  </div>
</div>
```

**Responsive Breakpoints:**
```typescript
// tailwind.config.ts
export default {
  theme: {
    screens: {
      'sm': '640px',   // Small phones landscape
      'md': '768px',   // Tablets
      'lg': '1024px',  // Desktop (use this for mobile/desktop split)
      'xl': '1280px',  // Large desktop
      '2xl': '1536px', // Extra large
    }
  }
}

// Usage: Switch components at 'lg' breakpoint
{isMobile ? <MobileBottomNav /> : <DesktopSidebar />}
```

---

## Code Quality Standards

### Frontend Architecture

**Component Organization:**
```
src/
├── components/
│   ├── ui/              # Reusable UI primitives
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   └── ...
│   ├── layout/          # Layout components
│   │   ├── DesktopSidebar.tsx
│   │   ├── MobileBottomNav.tsx
│   │   ├── Header.tsx
│   │   └── ...
│   ├── features/        # Feature-specific components
│   │   ├── auth/
│   │   ├── dashboard/
│   │   └── ...
│   └── shared/          # Shared business components
│       ├── UserAvatar.tsx
│       ├── StatCard.tsx
│       └── ...
├── hooks/               # Custom React hooks
├── lib/                 # Utilities and helpers
├── stores/              # State management (Zustand)
├── types/               # TypeScript types
└── app/                 # Next.js app router (or pages/)
```

**TypeScript Requirements:**
- ✓ Strict mode enabled
- ✓ No `any` types (use `unknown` if truly needed)
- ✓ Interfaces for all component props
- ✓ Type all function parameters and returns
- ✓ Use discriminated unions for variants

**Component Best Practices:**
```typescript
// Good component structure
import { ComponentType } from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  disabled = false,
  children,
  onClick
}: ButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={disabled || isLoading}
      className={clsx(
        'inline-flex items-center justify-center rounded-lg font-medium transition-colors',
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-gray-200 text-gray-900 hover:bg-gray-300': variant === 'secondary',
          'border border-gray-300 bg-white hover:bg-gray-50': variant === 'outline',
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-4 py-2 text-base': size === 'md',
          'px-6 py-3 text-lg': size === 'lg',
          'opacity-50 cursor-not-allowed': disabled,
        }
      )}
    >
      {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
      {children}
    </button>
  );
}
```

**Accessibility Requirements:**
- ✓ Semantic HTML (`<button>`, `<nav>`, `<main>`, etc.)
- ✓ ARIA labels where needed
- ✓ Keyboard navigation support
- ✓ Focus indicators (visible focus rings)
- ✓ Color contrast ratios (WCAG AA)
- ✓ Screen reader friendly

---

### Backend Architecture

**API Structure:**
```
backend/
├── src/
│   ├── controllers/     # Request handling
│   ├── services/        # Business logic
│   ├── models/          # Data models
│   ├── routes/          # API routes
│   ├── middleware/      # Auth, validation, logging
│   ├── utils/           # Helper functions
│   └── types/           # TypeScript types
├── tests/
└── config/
```

**API Design Standards:**
- ✓ RESTful conventions (GET, POST, PUT, PATCH, DELETE)
- ✓ Consistent response format:
```typescript
// Success response
{
  success: true,
  data: {...},
  meta: { page: 1, total: 100 }
}

// Error response
{
  success: false,
  error: {
    code: 'VALIDATION_ERROR',
    message: 'User-friendly error message',
    details: [...]
  }
}
```

**Security Best Practices:**
- ✓ Input validation (Zod, Joi, or class-validator)
- ✓ SQL injection prevention (parameterized queries)
- ✓ XSS protection (sanitize outputs)
- ✓ CSRF tokens for state-changing operations
- ✓ Rate limiting (express-rate-limit)
- ✓ Helmet.js for security headers
- ✓ Authentication (JWT, sessions)
- ✓ Authorization (RBAC or ABAC)

**Error Handling:**
```typescript
// Centralized error handling
class AppError extends Error {
  constructor(
    public statusCode: number,
    public message: string,
    public code?: string,
    public details?: any
  ) {
    super(message);
  }
}

// In routes/controllers
throw new AppError(400, 'Invalid email format', 'VALIDATION_ERROR');

// Error middleware
app.use((err, req, res, next) => {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      success: false,
      error: {
        code: err.code,
        message: err.message,
        details: err.details
      }
    });
  }

  // Log unexpected errors
  logger.error(err);

  res.status(500).json({
    success: false,
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred'
    }
  });
});
```

---

## Tech Stack Recommendations

### Frontend
- **Framework:** Next.js (App Router) or Vite + React
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Components:** Radix UI or Headless UI
- **Icons:** Lucide React
- **Animations:** Framer Motion
- **Forms:** React Hook Form + Zod
- **State:** Zustand
- **Data Fetching:** React Query

### Backend
- **Node.js:** Express or Fastify
- **Python:** FastAPI
- **Database:** PostgreSQL (Supabase) or MongoDB
- **ORM:** Prisma or Drizzle (Node), SQLAlchemy (Python)
- **Auth:** NextAuth, Supabase Auth, or custom JWT

---

## Anti-Patterns to Avoid

### UI/UX Anti-Patterns
- ❌ Overusing modals for non-critical actions
- ❌ Mobile view as just "shrunk desktop"
- ❌ Using emojis instead of professional icons
- ❌ Inconsistent spacing/typography
- ❌ Missing loading/error states
- ❌ Poor contrast ratios
- ❌ Buttons that don't look clickable
- ❌ Forms without validation feedback

### Code Anti-Patterns
- ❌ Mixing presentation and business logic
- ❌ Inconsistent naming conventions
- ❌ Missing error handling
- ❌ No TypeScript types
- ❌ Hardcoded values instead of constants
- ❌ God components (components that do too much)
- ❌ Prop drilling (use context or state management)
- ❌ Inline styles (use Tailwind classes)

---

## Quality Checklist

### Before Submitting Code

**UI/UX:**
- [ ] Interactions are inline (modals only when necessary)
- [ ] Professional icons used (Lucide, Heroicons)
- [ ] Smooth animations (300ms, ease-in-out)
- [ ] Mobile and desktop views are separate components
- [ ] Bottom nav on mobile, sidebar on desktop
- [ ] Touch targets are 48×48px minimum on mobile
- [ ] Loading states for all async actions
- [ ] Error states with helpful messages
- [ ] Success feedback for user actions

**Code Quality:**
- [ ] TypeScript types for everything
- [ ] No `any` types
- [ ] Components are small and focused
- [ ] Accessibility attributes (ARIA, semantic HTML)
- [ ] Keyboard navigation works
- [ ] Code is well-commented
- [ ] Consistent naming conventions
- [ ] No console.logs in production

**Performance:**
- [ ] Images optimized (WebP, lazy loading)
- [ ] Code splitting where appropriate
- [ ] Lighthouse score 90+ (performance, accessibility)
- [ ] No unnecessary re-renders

**Testing:**
- [ ] Manual testing on mobile and desktop
- [ ] Cross-browser testing (Chrome, Safari, Firefox)
- [ ] Accessibility testing (keyboard, screen reader)

---

## Success Metrics

**Generated projects should achieve:**
- ✓ 0 accessibility violations (Lighthouse)
- ✓ 90+ performance score
- ✓ Consistent design system
- ✓ Zero emojis in UI
- ✓ <3 modals in typical user flow
- ✓ Type-safe codebase (TypeScript)
- ✓ Comprehensive error handling
- ✓ Mobile + desktop specific views

---

## Version History
- **v1.0.0** - Initial comprehensive standards document
