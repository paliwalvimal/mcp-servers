import os
import httpx

from loguru import logger
from typing import Any


async def make_api_request(api_path: str, req_data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a request to the TinyURL API with proper error handling."""
    api_key = os.environ.get("TINY_URL_API_KEY", None)
    if not api_key:
        logger.error("TinyURL API key not found in environment variables.")
        return None

    headers = {
        "User-Agent": "VimalPaliwal TinyURL MCP",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    async with httpx.AsyncClient() as client:
        try:
            url = f"https://api.tinyurl.com/{api_path}"
            logger.info(f"Making request to: {url}")
            logger.info(f"Request data: {req_data}")

            response = await client.post(url, headers=headers, json=req_data)
            logger.info(f"Response status: {response.status_code}")
            logger.info(f"Response body: {response.json()}")

            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"API request failed: {str(e)}")
            return None
