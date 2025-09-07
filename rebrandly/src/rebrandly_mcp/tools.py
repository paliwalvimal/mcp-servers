from loguru import logger

from rebrandly_mcp.server import mcp
from rebrandly_mcp.utils import make_api_request, RequestMethod
from rebrandly_mcp.models import (
    CreateShortUrlRequest,
    ShortUrlDetails,
    ApiErrorResponse,
    DeleteShortUrlRequest,
)


@mcp.tool()
async def generate_short_url(
    req_data: CreateShortUrlRequest,
) -> ShortUrlDetails | ApiErrorResponse:
    """
    Generate a new short URL for a given long/destination URL.

    Args:
        req_data: The long/destination URL to shorten along with metadata.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """

    logger.info("Making an API request to generate a new short URL...")
    api_response = await make_api_request(
        api_path="links",
        req_method=RequestMethod.POST,
        req_data=req_data.model_dump_json(exclude_none=True),
    )

    if "status_code" in api_response:
        return ApiErrorResponse(**api_response)
    else:
        return ShortUrlDetails(**api_response)


@mcp.tool()
async def delete_short_url(
    req_data: DeleteShortUrlRequest,
) -> ShortUrlDetails | ApiErrorResponse:
    """
    Delete an existing short URL.

    Args:
        req_data: The unique identifier of the short URL.

    Returns:
        The deleted short URL and the metadata if success else error code along with the message.
    """

    logger.info("Making an API request to delete the existing short URL...")
    api_response = await make_api_request(
        api_path=f"links/{DeleteShortUrlRequest.id}", req_method=RequestMethod.DELETE
    )

    if "status_code" in api_response:
        return ApiErrorResponse(**api_response)
    else:
        return ShortUrlDetails(**api_response)
