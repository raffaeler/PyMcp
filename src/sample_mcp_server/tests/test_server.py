"""Tests for the sample MCP server."""

from typing import Any
from unittest.mock import MagicMock

import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError
from fastmcp.server.context import Context

from sample_mcp_server import __version__, server
from sample_mcp_server.server import mcp


def test_server_import() -> None:
    """Test that the server module can be imported."""
    assert server is not None


def test_package_version() -> None:
    """Test that the package version is defined."""
    assert __version__ == "0.1.0"


@pytest.mark.asyncio
async def test_echo_tool() -> None:
    """Test the echo tool using fastmcp.Client."""

    async with Client(mcp) as client:
        # Test with a normal message
        result = await client.call_tool("echo", {"message": "Hello, World!"})
        assert result.data == "Hello, World!"

        # Test with another message
        result = await client.call_tool("echo", {"message": "Test message"})
        assert result.data == "Test message"


@pytest.mark.asyncio
async def test_echo_tool_empty_message() -> None:
    """Test that the echo tool raises an error for empty messages."""

    async with Client(mcp) as client:
        # Test with empty message - should raise ToolError
        with pytest.raises(ToolError, match="Message cannot be empty"):
            await client.call_tool("echo", {"message": ""})


@pytest.mark.asyncio
async def test_one_liner_tool(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test the one_liner tool using fastmcp.Client."""

    # Mock the context.sample() response
    mock_response = MagicMock()
    mock_response.text = "Python is a high-level, interpreted programming language created in 1991."

    async def mock_sample(*_args: Any, **_kwargs: Any) -> Any:
        return mock_response

    monkeypatch.setattr(Context, "sample", mock_sample)

    async with Client(mcp) as client:
        # Test with a sample text
        text = """
        Python is a high-level, interpreted programming language known for its
        simplicity and readability. It was created by Guido van Rossum and first
        released in 1991. Python emphasizes code readability with its notable use
        of significant whitespace and supports multiple programming paradigms,
        including procedural, object-oriented, and functional programming.
        """
        result = await client.call_tool("oneLiner", {"text": text})

        # Verify that we get a non-empty string response
        assert isinstance(result.data, str)
        assert len(result.data) > 0

        # The summary should be significantly shorter than the original text
        assert len(result.data) < len(text)
        assert result.data == mock_response.text


@pytest.mark.asyncio
async def test_one_liner_tool_empty_text() -> None:
    """Test that the one_liner tool raises an error for empty text."""

    async with Client(mcp) as client:
        # Test with empty text - should raise ToolError
        with pytest.raises(ToolError, match="Text cannot be empty"):
            await client.call_tool("oneLiner", {"text": ""})


@pytest.mark.asyncio
async def test_reverse_string_tool() -> None:
    """Test the reverse_string tool."""
    async with Client(mcp) as client:
        result = await client.call_tool("reverse_string", {"text": "hello"})
        assert result.data == "olleh"
