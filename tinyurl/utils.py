import os
import httpx

from dotenv import load_dotenv
from typing import Any

load_dotenv()


async def make_api_request(api_path: str, req_data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the TinyURL API with proper error handling."""
    headers = {
        "User-Agent": "VimalPaliwal TinyURL MCP",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('TINY_URL_API_KEY', None)}",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"https://api.tinyurl.com/{api_path}", headers=headers, json=req_data
            )
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
