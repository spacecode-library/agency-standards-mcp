# Dockerfile for Railway deployment
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY pyproject.toml ./
RUN pip install --no-cache-dir uv && \
    uv pip install --system "mcp>=1.4.0" anthropic python-dotenv fastapi uvicorn pathspec

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/logs

# Expose port for Railway
EXPOSE $PORT

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:' + __import__('os').environ.get('PORT', '8000') + '/health')" || exit 1

# Run the remote server
CMD python src/agency_mcp_remote.py
