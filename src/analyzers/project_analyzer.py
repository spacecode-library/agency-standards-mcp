"""
Project Analyzer - Scans and extracts patterns from existing agency projects
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Set
import logging

logger = logging.getLogger(__name__)


class ProjectAnalyzer:
    """Analyzes project structure and extracts design patterns"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.project_name = self.project_path.name

    def analyze(self) -> Dict:
        """
        Comprehensive project analysis

        Returns:
            Dict containing:
            - name: project name
            - tech_stack: detected technologies
            - components: list of components with types
            - design_patterns: modal/inline patterns
            - folder_structure: organization pattern
            - design_system: colors, spacing, etc.
        """
        logger.info(f"Analyzing project: {self.project_name}")

        analysis = {
            "name": self.project_name,
            "path": str(self.project_path),
            "tech_stack": self._detect_tech_stack(),
            "components": self._analyze_components(),
            "design_patterns": self._extract_design_patterns(),
            "folder_structure": self._analyze_folder_structure(),
            "design_system": self._extract_design_system(),
            "mobile_patterns": self._detect_mobile_patterns(),
            "icon_usage": self._detect_icon_usage(),
        }

        logger.info(f"✓ Analysis complete for {self.project_name}")
        return analysis

    def _detect_tech_stack(self) -> Dict[str, any]:
        """Detect technologies used in the project"""
        tech_stack = {
            "framework": None,
            "language": None,
            "styling": [],
            "components": [],
            "state_management": [],
            "form_handling": [],
            "icons": [],
            "animations": [],
        }

        # Check package.json
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

                    # Framework detection
                    if "next" in deps:
                        tech_stack["framework"] = "Next.js"
                    elif "vite" in deps and "react" in deps:
                        tech_stack["framework"] = "Vite + React"
                    elif "react" in deps:
                        tech_stack["framework"] = "React"
                    elif "vue" in deps:
                        tech_stack["framework"] = "Vue"

                    # Language
                    if "typescript" in deps:
                        tech_stack["language"] = "TypeScript"
                    else:
                        tech_stack["language"] = "JavaScript"

                    # Styling
                    if "tailwindcss" in deps:
                        tech_stack["styling"].append("Tailwind CSS")
                    if "styled-components" in deps:
                        tech_stack["styling"].append("Styled Components")
                    if "emotion" in deps or "@emotion/react" in deps:
                        tech_stack["styling"].append("Emotion")

                    # Component libraries
                    if "@radix-ui/react-dialog" in deps or any("@radix-ui" in d for d in deps):
                        tech_stack["components"].append("Radix UI")
                    if "@headlessui/react" in deps:
                        tech_stack["components"].append("Headless UI")

                    # State management
                    if "zustand" in deps:
                        tech_stack["state_management"].append("Zustand")
                    if "redux" in deps or "@reduxjs/toolkit" in deps:
                        tech_stack["state_management"].append("Redux")
                    if "jotai" in deps:
                        tech_stack["state_management"].append("Jotai")

                    # Form handling
                    if "react-hook-form" in deps:
                        tech_stack["form_handling"].append("React Hook Form")
                    if "zod" in deps:
                        tech_stack["form_handling"].append("Zod")
                    if "yup" in deps:
                        tech_stack["form_handling"].append("Yup")

                    # Icons
                    if "lucide-react" in deps:
                        tech_stack["icons"].append("Lucide React")
                    if "@heroicons/react" in deps:
                        tech_stack["icons"].append("Heroicons")
                    if "react-icons" in deps:
                        tech_stack["icons"].append("React Icons")

                    # Animations
                    if "framer-motion" in deps:
                        tech_stack["animations"].append("Framer Motion")
                    if "react-spring" in deps:
                        tech_stack["animations"].append("React Spring")

            except Exception as e:
                logger.error(f"Error parsing package.json: {e}")

        return tech_stack

    def _analyze_components(self) -> List[Dict]:
        """Analyze React/Vue components in the project"""
        components = []

        # Find component directories
        component_dirs = []
        for pattern in ["components", "src/components", "app/components"]:
            comp_dir = self.project_path / pattern
            if comp_dir.exists():
                component_dirs.append(comp_dir)

        for comp_dir in component_dirs:
            for file_path in comp_dir.rglob("*.tsx"):
                try:
                    component_info = self._analyze_component_file(file_path)
                    if component_info:
                        components.append(component_info)
                except Exception as e:
                    logger.debug(f"Error analyzing {file_path}: {e}")

        return components

    def _analyze_component_file(self, file_path: Path) -> Optional[Dict]:
        """Analyze a single component file"""
        try:
            content = file_path.read_text()
            relative_path = file_path.relative_to(self.project_path)

            component_info = {
                "name": file_path.stem,
                "path": str(relative_path),
                "type": self._detect_component_type(content, file_path),
                "has_animations": "framer-motion" in content or "motion." in content,
                "uses_icons": any(icon in content for icon in ["lucide-react", "@heroicons", "Icon"]),
                "is_mobile_specific": "mobile" in file_path.name.lower() or "Mobile" in file_path.name,
                "is_desktop_specific": "desktop" in file_path.name.lower() or "Desktop" in file_path.name,
            }

            return component_info

        except Exception as e:
            logger.debug(f"Error reading {file_path}: {e}")
            return None

    def _detect_component_type(self, content: str, file_path: Path) -> str:
        """Detect the type/purpose of a component"""
        filename_lower = file_path.name.lower()

        # Check for modal/dialog
        if any(term in content for term in ["Dialog", "Modal", "<dialog"]):
            return "modal"

        # Check for inline patterns
        if any(term in content.lower() for term in ["inline", "confirmation"]):
            return "inline-action"

        # Layout components
        if any(term in filename_lower for term in ["nav", "sidebar", "header", "footer", "layout"]):
            return "layout"

        # Form components
        if any(term in filename_lower for term in ["form", "input", "select", "checkbox"]):
            return "form"

        # UI primitives
        if file_path.parent.name == "ui":
            return "ui-primitive"

        return "component"

    def _extract_design_patterns(self) -> Dict:
        """Extract design patterns (modal vs inline)"""
        patterns = {
            "modal_components": [],
            "inline_components": [],
            "modal_count": 0,
            "inline_count": 0,
            "modal_usage_ratio": 0.0,
        }

        component_dirs = []
        for pattern in ["components", "src/components", "app/components"]:
            comp_dir = self.project_path / pattern
            if comp_dir.exists():
                component_dirs.append(comp_dir)

        for comp_dir in component_dirs:
            for file_path in comp_dir.rglob("*.tsx"):
                try:
                    content = file_path.read_text()
                    relative_path = str(file_path.relative_to(self.project_path))

                    # Check for modals
                    if any(term in content for term in ["Dialog", "Modal", "<dialog"]):
                        patterns["modal_components"].append(relative_path)
                        patterns["modal_count"] += 1

                    # Check for inline patterns
                    if "confirming" in content.lower() or "inline" in content.lower():
                        patterns["inline_components"].append(relative_path)
                        patterns["inline_count"] += 1

                except Exception as e:
                    logger.debug(f"Error checking patterns in {file_path}: {e}")

        # Calculate ratio
        total = patterns["modal_count"] + patterns["inline_count"]
        if total > 0:
            patterns["modal_usage_ratio"] = patterns["modal_count"] / total

        return patterns

    def _analyze_folder_structure(self) -> Dict:
        """Analyze folder organization patterns"""
        structure = {
            "has_components_folder": False,
            "has_src_folder": False,
            "component_organization": [],
            "has_ui_folder": False,
            "has_layout_folder": False,
            "has_shared_folder": False,
        }

        # Check for standard folders
        structure["has_src_folder"] = (self.project_path / "src").exists()
        structure["has_components_folder"] = (
            (self.project_path / "components").exists()
            or (self.project_path / "src" / "components").exists()
        )

        # Check component organization
        component_dirs = []
        for pattern in ["components", "src/components"]:
            comp_dir = self.project_path / pattern
            if comp_dir.exists():
                component_dirs.append(comp_dir)

        for comp_dir in component_dirs:
            if (comp_dir / "ui").exists():
                structure["has_ui_folder"] = True
                structure["component_organization"].append("ui")
            if (comp_dir / "layout").exists():
                structure["has_layout_folder"] = True
                structure["component_organization"].append("layout")
            if (comp_dir / "shared").exists():
                structure["has_shared_folder"] = True
                structure["component_organization"].append("shared")

        return structure

    def _extract_design_system(self) -> Dict:
        """Extract design system patterns from Tailwind config"""
        design_system = {
            "uses_tailwind": False,
            "custom_colors": False,
            "custom_spacing": False,
            "design_tokens": {},
        }

        # Check for Tailwind config
        for config_name in [
            "tailwind.config.ts",
            "tailwind.config.js",
            "tailwind.config.mjs",
        ]:
            config_path = self.project_path / config_name
            if config_path.exists():
                design_system["uses_tailwind"] = True
                try:
                    content = config_path.read_text()
                    design_system["custom_colors"] = "colors:" in content or '"colors"' in content
                    design_system["custom_spacing"] = "spacing:" in content or '"spacing"' in content

                    # Try to extract some basic info
                    if "extend:" in content:
                        design_system["design_tokens"]["extends_default"] = True
                except Exception as e:
                    logger.debug(f"Error reading Tailwind config: {e}")
                break

        return design_system

    def _detect_mobile_patterns(self) -> Dict:
        """Detect mobile-specific patterns"""
        mobile_patterns = {
            "has_mobile_nav": False,
            "has_bottom_nav": False,
            "mobile_components": [],
            "uses_safe_area_insets": False,
            "separate_mobile_desktop": False,
        }

        # Search for mobile-specific components
        for pattern in ["components", "src/components", "app/components"]:
            comp_dir = self.project_path / pattern
            if comp_dir.exists():
                for file_path in comp_dir.rglob("*.tsx"):
                    try:
                        filename_lower = file_path.name.lower()
                        content = file_path.read_text()

                        if "mobile" in filename_lower:
                            mobile_patterns["mobile_components"].append(
                                str(file_path.relative_to(self.project_path))
                            )

                        if "bottomnav" in filename_lower or "bottom-nav" in filename_lower:
                            mobile_patterns["has_bottom_nav"] = True

                        if "mobilenav" in filename_lower or "mobile-nav" in filename_lower:
                            mobile_patterns["has_mobile_nav"] = True

                        if "safe-area-inset" in content or "env(safe-area-inset" in content:
                            mobile_patterns["uses_safe_area_insets"] = True

                        # Check for device detection
                        if "isMobile" in content or "useMediaQuery" in content:
                            mobile_patterns["separate_mobile_desktop"] = True

                    except Exception as e:
                        logger.debug(f"Error checking mobile patterns: {e}")

        return mobile_patterns

    def _detect_icon_usage(self) -> Dict:
        """Detect icon library usage"""
        icon_usage = {
            "libraries": [],
            "has_emoji_usage": False,
            "professional_icons": True,
        }

        # Check package.json for icon libraries
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

                    if "lucide-react" in deps:
                        icon_usage["libraries"].append("Lucide React")
                    if "@heroicons/react" in deps:
                        icon_usage["libraries"].append("Heroicons")
                    if "react-icons" in deps:
                        icon_usage["libraries"].append("React Icons")

            except Exception as e:
                logger.debug(f"Error checking icon usage: {e}")

        # Check for emoji usage in components
        for pattern in ["components", "src/components", "app"]:
            comp_dir = self.project_path / pattern
            if comp_dir.exists():
                for file_path in comp_dir.rglob("*.tsx"):
                    try:
                        content = file_path.read_text()
                        # Simple emoji detection (this is a basic check)
                        if any(emoji in content for emoji in ["😀", "🎉", "✨", "🚀", "💡"]):
                            icon_usage["has_emoji_usage"] = True
                            icon_usage["professional_icons"] = False
                            break
                    except Exception as e:
                        logger.debug(f"Error checking emojis: {e}")

        return icon_usage


class KnowledgeBaseBuilder:
    """Builds knowledge base from multiple projects"""

    def __init__(self, project_paths: List[str]):
        self.project_paths = project_paths
        self.knowledge_base = {
            "projects": [],
            "common_patterns": {},
            "tech_stack_summary": {},
            "design_insights": {},
        }

    def build(self) -> Dict:
        """Analyze all projects and build knowledge base"""
        logger.info(f"Building knowledge base from {len(self.project_paths)} projects...")

        for path in self.project_paths:
            if not path or not Path(path).exists():
                logger.warning(f"Project path does not exist: {path}")
                continue

            analyzer = ProjectAnalyzer(path)
            analysis = analyzer.analyze()
            self.knowledge_base["projects"].append(analysis)

        # Extract common patterns
        self._extract_common_patterns()
        self._summarize_tech_stack()
        self._generate_design_insights()

        logger.info(f"✓ Knowledge base built from {len(self.knowledge_base['projects'])} projects")
        return self.knowledge_base

    def _extract_common_patterns(self):
        """Extract patterns common across projects"""
        all_frameworks = []
        all_styling = []
        all_components = []
        modal_count = 0
        inline_count = 0

        for project in self.knowledge_base["projects"]:
            tech = project.get("tech_stack", {})
            if tech.get("framework"):
                all_frameworks.append(tech["framework"])
            all_styling.extend(tech.get("styling", []))
            all_components.extend(tech.get("components", []))

            patterns = project.get("design_patterns", {})
            modal_count += patterns.get("modal_count", 0)
            inline_count += patterns.get("inline_count", 0)

        self.knowledge_base["common_patterns"] = {
            "most_common_framework": max(set(all_frameworks), key=all_frameworks.count)
            if all_frameworks
            else None,
            "common_styling": list(set(all_styling)),
            "common_components": list(set(all_components)),
            "modal_inline_ratio": modal_count / max(inline_count, 1),
        }

    def _summarize_tech_stack(self):
        """Summarize tech stack usage across projects"""
        tech_summary = {
            "frameworks": {},
            "styling": {},
            "icons": {},
            "animations": {},
        }

        for project in self.knowledge_base["projects"]:
            tech = project.get("tech_stack", {})

            # Count frameworks
            framework = tech.get("framework")
            if framework:
                tech_summary["frameworks"][framework] = (
                    tech_summary["frameworks"].get(framework, 0) + 1
                )

            # Count styling tools
            for style in tech.get("styling", []):
                tech_summary["styling"][style] = tech_summary["styling"].get(style, 0) + 1

            # Count icon libraries
            for icon in tech.get("icons", []):
                tech_summary["icons"][icon] = tech_summary["icons"].get(icon, 0) + 1

            # Count animation libraries
            for anim in tech.get("animations", []):
                tech_summary["animations"][anim] = tech_summary["animations"].get(anim, 0) + 1

        self.knowledge_base["tech_stack_summary"] = tech_summary

    def _generate_design_insights(self):
        """Generate insights about design patterns"""
        insights = {
            "pwa_adoption": 0,
            "mobile_first_count": 0,
            "uses_bottom_nav": 0,
            "separate_mobile_desktop": 0,
            "professional_icon_usage": 0,
        }

        for project in self.knowledge_base["projects"]:
            mobile = project.get("mobile_patterns", {})
            icons = project.get("icon_usage", {})

            if mobile.get("has_bottom_nav"):
                insights["uses_bottom_nav"] += 1
            if mobile.get("separate_mobile_desktop"):
                insights["separate_mobile_desktop"] += 1
            if icons.get("professional_icons"):
                insights["professional_icon_usage"] += 1

        insights["pwa_adoption_rate"] = insights["uses_bottom_nav"] / len(
            self.knowledge_base["projects"]
        )

        self.knowledge_base["design_insights"] = insights

    def save_to_file(self, output_path: str):
        """Save knowledge base to JSON file"""
        with open(output_path, "w") as f:
            json.dump(self.knowledge_base, f, indent=2)
        logger.info(f"✓ Knowledge base saved to {output_path}")


if __name__ == "__main__":
    # Test the analyzer
    import sys

    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
        analyzer = ProjectAnalyzer(project_path)
        result = analyzer.analyze()
        print(json.dumps(result, indent=2))
    else:
        print("Usage: python project_analyzer.py <project_path>")
