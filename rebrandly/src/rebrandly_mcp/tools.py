from loguru import logger

from rebrandly_mcp.server import mcp
from rebrandly_mcp.utils import make_api_request
from rebrandly_mcp.models import CreateShortUrlRequest, ShortUrlDetails, ApiErrorResponse


@mcp.tool()
async def generate_short_url(
    req_data: CreateShortUrlRequest,
) -> ShortUrlDetails:
    """
    Generate a new short URL for a given long/destination URL.

    Args:
        req_data: The long/destination URL to shorten along with metadata.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """

    logger.info("Making an API request to generate a new short URL...")
    api_response = await make_api_request(
        api_path="links", req_data=req_data.model_dump_json(exclude_none=True)
    )

    if api_response["code"] == 0:
        return ShortUrlDetails(**api_response)
    else:
        return ApiErrorResponse(**api_response)
