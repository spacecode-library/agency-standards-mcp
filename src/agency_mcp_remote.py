#!/usr/bin/env python3
"""
Agency Standards MCP Remote Server

HTTP server for remote team access with authentication and rate limiting.
"""

import os
import secrets
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load the main MCP server tools
from agency_mcp_server import (
    generate_project_starter,
    generate_polish_checklist,
    review_ui_component,
    review_backend_code,
    generate_component_template,
    get_design_guidelines,
    analyze_modal_usage,
    check_mobile_desktop_separation,
    KNOWLEDGE_BASE,
)

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Agency Standards MCP Server",
    description="Remote MCP server for agency development standards",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple API key storage (use database in production)
API_KEYS = {
    os.getenv("ADMIN_API_KEY", "admin-key-change-me"): {
        "name": "Admin",
        "role": "admin",
        "permissions": ["all"],
        "created_at": datetime.now().isoformat()
    }
}

# Rate limiting (simple in-memory, use Redis in production)
RATE_LIMITS = {}


def verify_api_key(authorization: Optional[str] = Header(None)):
    """Verify API key from Authorization header"""
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization format. Use: Bearer <api-key>"
        )

    api_key = authorization.replace("Bearer ", "")

    if api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API key")

    # Simple rate limiting
    now = datetime.now()
    if api_key in RATE_LIMITS:
        last_request, count = RATE_LIMITS[api_key]
        if (now - last_request).seconds < 60:
            if count > 100:  # 100 requests per minute
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            RATE_LIMITS[api_key] = (last_request, count + 1)
        else:
            RATE_LIMITS[api_key] = (now, 1)
    else:
        RATE_LIMITS[api_key] = (now, 1)

    return API_KEYS[api_key]


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Agency Standards MCP Server",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "tools": "/tools",
            "guidelines": "/api/guidelines",
            "generate-project": "/api/generate-project",
            "review-component": "/api/review-component",
            "admin": "/admin/*"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Agency Standards MCP Server",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/tools")
async def list_tools(user: dict = Depends(verify_api_key)):
    """List available tools"""
    return {
        "tools": [
            {
                "name": "generate_project_starter",
                "description": "Generate complete starter projects from SRS/system design",
                "parameters": ["srs_document", "system_design", "project_name", "project_type"]
            },
            {
                "name": "generate_polish_checklist",
                "description": "Generate prioritized polish checklist",
                "parameters": ["project_path", "focus_areas"]
            },
            {
                "name": "review_ui_component",
                "description": "Review UI component against standards",
                "parameters": ["component_code", "component_type", "file_path"]
            },
            {
                "name": "review_backend_code",
                "description": "Review backend code for security and quality",
                "parameters": ["code", "code_type", "file_path"]
            },
            {
                "name": "generate_component_template",
                "description": "Generate production-ready component template",
                "parameters": ["component_name", "component_purpose", "should_be_inline"]
            },
            {
                "name": "get_design_guidelines",
                "description": "Get agency design guidelines",
                "parameters": ["category"]
            },
            {
                "name": "analyze_modal_usage",
                "description": "Analyze modal usage and suggest inline alternatives",
                "parameters": ["project_path"]
            },
            {
                "name": "check_mobile_desktop_separation",
                "description": "Check PWA mobile/desktop separation",
                "parameters": ["project_path"]
            }
        ]
    }


# =============================================================================
# API Endpoints for Tools
# =============================================================================


@app.post("/api/generate-project")
async def api_generate_project(
    srs_document: str,
    system_design: str,
    project_name: str,
    project_type: str = "fullstack-pwa",
    user: dict = Depends(verify_api_key)
):
    """Generate a starter project"""
    result = await generate_project_starter(
        srs_document=srs_document,
        system_design=system_design,
        project_name=project_name,
        project_type=project_type
    )
    return {"success": True, "data": result}


@app.post("/api/polish-checklist")
async def api_polish_checklist(
    project_path: str,
    focus_areas: Optional[list] = None,
    user: dict = Depends(verify_api_key)
):
    """Generate polish checklist"""
    result = await generate_polish_checklist(
        project_path=project_path,
        focus_areas=focus_areas
    )
    return {"success": True, "data": result}


@app.post("/api/review-component")
async def api_review_component(
    component_code: str,
    component_type: str,
    file_path: str = "",
    user: dict = Depends(verify_api_key)
):
    """Review UI component"""
    result = await review_ui_component(
        component_code=component_code,
        component_type=component_type,
        file_path=file_path
    )
    return {"success": True, "data": result}


@app.post("/api/review-backend")
async def api_review_backend(
    code: str,
    code_type: str,
    file_path: str = "",
    user: dict = Depends(verify_api_key)
):
    """Review backend code"""
    result = await review_backend_code(
        code=code,
        code_type=code_type,
        file_path=file_path
    )
    return {"success": True, "data": result}


@app.post("/api/generate-component")
async def api_generate_component(
    component_name: str,
    component_purpose: str,
    should_be_inline: bool = True,
    user: dict = Depends(verify_api_key)
):
    """Generate component template"""
    result = await generate_component_template(
        component_name=component_name,
        component_purpose=component_purpose,
        should_be_inline=should_be_inline
    )
    return {"success": True, "data": result}


@app.get("/api/guidelines")
async def api_guidelines(
    category: Optional[str] = None,
    user: dict = Depends(verify_api_key)
):
    """Get design guidelines"""
    result = await get_design_guidelines(category=category)
    return {"success": True, "data": result}


@app.post("/api/analyze-modals")
async def api_analyze_modals(
    project_path: str,
    user: dict = Depends(verify_api_key)
):
    """Analyze modal usage"""
    result = await analyze_modal_usage(project_path=project_path)
    return {"success": True, "data": result}


@app.post("/api/check-mobile-desktop")
async def api_check_mobile_desktop(
    project_path: str,
    user: dict = Depends(verify_api_key)
):
    """Check mobile/desktop separation"""
    result = await check_mobile_desktop_separation(project_path=project_path)
    return {"success": True, "data": result}


# =============================================================================
# Admin Endpoints
# =============================================================================


@app.post("/admin/api-keys")
async def create_api_key(
    developer_name: str,
    role: str = "developer",
    user: dict = Depends(verify_api_key)
):
    """Create new API key for a developer (admin only)"""
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    # Generate secure API key
    new_key = f"agency_{secrets.token_urlsafe(32)}"

    API_KEYS[new_key] = {
        "name": developer_name,
        "role": role,
        "permissions": ["read", "write"] if role == "developer" else ["all"],
        "created_at": datetime.now().isoformat()
    }

    return {
        "success": True,
        "api_key": new_key,
        "developer": developer_name,
        "setup_command": f"claude mcp add agency-standards --transport http -e API_KEY={new_key} {os.getenv('SERVER_URL')}"
    }


@app.get("/admin/api-keys")
async def list_api_keys(user: dict = Depends(verify_api_key)):
    """List all API keys (admin only)"""
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {
        "success": True,
        "api_keys": [
            {
                "key": key[:20] + "...",
                "name": info["name"],
                "role": info["role"],
                "created_at": info["created_at"]
            }
            for key, info in API_KEYS.items()
        ]
    }


@app.get("/admin/stats")
async def get_stats(user: dict = Depends(verify_api_key)):
    """Get usage statistics (admin only)"""
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {
        "success": True,
        "statistics": {
            "total_api_keys": len(API_KEYS),
            "rate_limit_entries": len(RATE_LIMITS),
            "knowledge_base_projects": len(KNOWLEDGE_BASE.get("projects", [])),
        }
    }


@app.get("/admin/knowledge-base")
async def get_knowledge_base(user: dict = Depends(verify_api_key)):
    """Get knowledge base summary (admin only)"""
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return {
        "success": True,
        "knowledge_base": {
            "projects": [p.get("name") for p in KNOWLEDGE_BASE.get("projects", [])],
            "tech_stack": KNOWLEDGE_BASE.get("tech_stack_summary", {}),
            "design_insights": KNOWLEDGE_BASE.get("design_insights", {})
        }
    }


# =============================================================================
# Server Startup
# =============================================================================


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")

    print(f"🚀 Starting Agency Standards MCP Remote Server")
    print(f"📍 Listening on {host}:{port}")
    print(f"📚 Knowledge Base: {len(KNOWLEDGE_BASE.get('projects', []))} projects")
    print(f"🔑 API Keys configured: {len(API_KEYS)}")
    print(f"✅ Server ready!")

    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )
