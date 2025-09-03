from tinyurl_mcp.server import mcp

import tinyurl_mcp.prompts  # noqa: F401
import tinyurl_mcp.tools  # noqa: F401


def main():
    print("\nStarting MCP server...")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
