# Sample MCP Server

This is a sample MCP (Model Context Protocol) server for document ingestion, built using FastMCP.

## Features

- Document ingestion with content type support
- Document search functionality
- Docker support for easy deployment

## Local Development

### Prerequisites

- Python 3.10 or higher
- `uv` package manager

### Setup

1. Create and activate a virtual environment using `uv`:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
uv pip install -e ".[dev]"
```

3. Run the server:

```bash
python -m sample_mcp_server.server
```

## Testing

Run tests with pytest:

```bash
pytest src/sample_mcp_server/tests/
```

## Docker Deployment

Build the Docker image:

```bash
docker build -f src/sample_mcp_server/Dockerfile -t sample-mcp-server .
```

Run the container:

```bash
docker run -i sample-mcp-server
```

## Available Tools

### ingest_document

Ingest a document for processing.

**Parameters:**
- `content` (required): The document content to ingest
- `doc_type` (optional): Type of document (text, markdown, etc.)

### search_documents

Search through ingested documents.

**Parameters:**
- `query` (required): Search query string
