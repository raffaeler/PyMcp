"""
Sample MCP Server.
This server demonstrates a basic MCP server template using FastMCP.
"""

import asyncio
import os
from typing import Annotated, Any

from dotenv import load_dotenv
from fastmcp import Context, FastMCP
from fastmcp.exceptions import ToolError

# pyright: reportUnusedFunction=none

mcp = FastMCP(
    name="Sample MCP Server",
    include_tags={"development", "production"},
    exclude_tags={"internal", "obsolete"},
    on_duplicate_tools="error",
    on_duplicate_resources="warn",
    on_duplicate_prompts="replace",
    include_fastmcp_meta=False,
)


@mcp.tool(
    name="echo",
    description="An echo tool for testing purposes.",
    annotations={
        "title": "Echo Tool",
        "readOnlyHint": True,
    },
    enabled=True,
    tags={"development"},
)
async def echo(
    message: Annotated[str, "The message to echo back."],
) -> Annotated[str, "The echoed message."]:
    """An echo tool for testing purposes."""
    if not message:
        raise ToolError("Message cannot be empty.")
    return message


@mcp.tool(
    name="oneLiner",
    description="Generates a one-liner summary for the provided text.",
    annotations={
        "title": "One-Liner Summary Tool",
        "readOnlyHint": True,
    },
    enabled=True,
    tags={"development"},
)
async def one_liner(
    context: Context,
    text: Annotated[str, "The text to summarize."],
) -> Annotated[str, "The one-liner summary of the text."]:
    """Generates a one-liner summary for the provided text."""
    if not text:
        raise ToolError("Text cannot be empty.")

    # include_context:
    # allows the MCP client to include the tools exposed by this server
    response: Any = await context.sample(
        system_prompt="You are an assistant writing super-short summaries.",
        messages=f"Summarize the following text in one line:\n\n{text}",
        # model_preferences="",
        include_context="thisServer",
        max_tokens=50,
        temperature=0.5,
    )

    result: str = response.text
    return result


class StringTools:
    """A collection of string manipulation tools."""

    @mcp.tool(
        name="reverse_string",
        description="Reverses a given string.",
        annotations={
            "title": "Reverse String Tool",
            "readOnlyHint": True,
        },
        enabled=True,
        tags={"development"},
    )
    @staticmethod
    async def reverse_string(
        context: Context,
        text: Annotated[str, "The string to reverse."],
    ) -> Annotated[str, "The reversed string."]:
        """Reverses a given string."""
        try:
            request = context.get_http_request()
            if request:
                print("HTTP Headers:", request.headers)
        except RuntimeError:
            pass
        return text[::-1]


if __name__ == "__main__":
    load_dotenv()
    host = os.getenv("MCP_SERVER_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_SERVER_PORT", "8000"))
    asyncio.run(mcp.run_async(transport="streamable-http", host=host, port=port))
    # mcp.run(transport="http", host=host, port=port)
