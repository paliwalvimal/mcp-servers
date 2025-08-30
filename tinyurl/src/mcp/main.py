from server import mcp

import prompts  # noqa: F401
import tools  # noqa: F401


def main():
    print("\nStarting MCP server...")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
