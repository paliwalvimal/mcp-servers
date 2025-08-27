from typing import Any

from server import mcp
from models import ShortUrlRequest
from utils import make_api_request


@mcp.tool()
async def generate_short_url(req_data: ShortUrlRequest) -> Any:
    """
    Generate a short URL for a given long URL.

    Args:
        req_data: The long URL to shorten along with additional optional parameters.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """
    api_response = await make_api_request(api_path="create", req_data=req_data.model_dump())

    return api_response
