## TinyURL MCP Server

This MCP server provides tools to interact with [tinyurl.com](https://tinyurl.com) to manage short URLs.

### Prerequisites

1. [uv](https://docs.astral.sh/uv/) from Astral
2. [Python 3.13](https://www.python.org/downloads/) or higher
3. Clone the repository

### Configuration

Use either of the below option to configure your MCP client.

**Via uv:**
```json
{
  "mcpServers": {
    "tinyurl-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "mcp-servers/tinyurl/src/tinyurl_mcp_server",
        "run",
        "main.py"
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


**Via docker:**

First step is to build the image:
```bash
docker image build -t tinyurl .
```

Then configure your MCP client:
```json
{
  "mcpServers": {
    "tinyurl-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "tinyurl"
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
