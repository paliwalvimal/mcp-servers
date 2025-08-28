import os
import httpx

from typing import Any

from server import mcp


async def make_api_request(api_path: str, req_data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the TinyURL API with proper error handling."""
    try:
        api_key = os.environ["TINY_URL_API_KEY"]
    except:
        mcp.request_context.session.send_log_message(
            level="error",
            message="TINY_URL_API_KEY not set in environment variables",
        )
        raise
    headers = {
        "User-Agent": "VimalPaliwal TinyURL MCP",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        try:
            url = f"https://api.tinyurl.com/{api_path}"
            print(f"Making request to: {url}")
            print(f"Request data: {req_data}")

            response = await client.post(url, headers=headers, json=req_data)
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.json()}")

            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"API request failed: {str(e)}")
            return None
