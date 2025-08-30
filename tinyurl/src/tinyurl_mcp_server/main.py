from tinyurl_mcp_server.server import mcp

import tinyurl_mcp_server.prompts  # noqa: F401
import tinyurl_mcp_server.tools  # noqa: F401


def main():
    print("\nStarting MCP server...")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
