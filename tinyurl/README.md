## TinyURL MCP Server

This MCP server provides tools to interact with [tinyurl.com](https://tinyurl.com) to manage short URLs.

### Prerequisites

1. [uv](https://docs.astral.sh/uv/) from Astral
2. [Python 3.13](https://www.python.org/downloads/) or higher

### Configuration

Use either of the below option to configure your MCP client.

**Option 1: Via uvx**
```json
{
  "mcpServers": {
    "tinyurl-mcp": {
      "command": "uvx",
      "args": [
        "tinyurl-mcp"
      ],
      "env": {
        "TINY_URL_API_KEY": "__API_KEY__"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```


**Option 2: Via docker**

```json
{
  "mcpServers": {
    "tinyurl-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "tinyurl-mcp"
      ],
      "env": {
        "TINY_URL_API_KEY": "__API_KEY__"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### Available Tools

- `generate_short_url`: Generate a new short URL
- `update_long_url`:  Update the long URL of an existing short URL
- `delete_short_url`: Delete an existing short URL
- `list_short_urls`: Llist all the available or archived short URLs

### Basic Usage Examples

- Shorten linkedin.com/in/xxxxx for me please
- Please create a short URL for medium.com/blog/xxxxx that expires next week
- Update the long URL of tinyurl.com/xxxx to medium.com/blog/zzzzz
- Delete the short URL for tinyurl.com/xxxx for me please
- List all the archived short URLs
