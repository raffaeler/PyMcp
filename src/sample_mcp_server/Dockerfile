# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml README.md ./

# Create virtual environment and install dependencies
RUN uv venv /app/.venv && \
    . /app/.venv/bin/activate && \
    uv pip install -e .

# Copy application code
COPY src/sample_mcp_server ./src/sample_mcp_server

# Set Python path
ENV PYTHONPATH=/app
ENV PATH="/app/.venv/bin:$PATH"

# Run the MCP server
CMD ["python", "-m", "src.sample_mcp_server.server"]
