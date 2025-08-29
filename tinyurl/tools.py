from server import mcp
from models import (
    CreateShortUrlRequest,
    CreateShortUrlResponse,
    UpdateLongUrlRequest,
    UpdateLongUrlResponse,
)
from utils import make_api_request


@mcp.tool()
async def generate_short_url(req_data: CreateShortUrlRequest) -> CreateShortUrlResponse:
    """
    Generate a short URL for a given long URL.

    Args:
        req_data: The long URL to shorten along with additional optional parameters.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """
    api_response = await make_api_request(
        api_path="create", req_data=req_data.model_dump_json(exclude_none=True)
    )

    if api_response["code"] == 0:
        return CreateShortUrlResponse(
            tiny_url=api_response["data"]["tiny_url"], expires_at=api_response["data"]["expires_at"]
        )
    else:
        return CreateShortUrlResponse(code=api_response["code"], errors=api_response["errors"])


@mcp.tool()
async def update_long_url(req_data: UpdateLongUrlRequest) -> UpdateLongUrlResponse:
    """
    Update long URL associated to an existing short URL.

    Args:
        long_url: The new long URL to associate with the existing short URL.
        short_url: The existing short URL to update.

    Returns:
        The new long URL associated to the existing short URL if success else error code along with the message.
    """

    api_response = await make_api_request(api_path="change", req_data=req_data.model_dump_json())

    if api_response["code"] == 0:
        return UpdateLongUrlResponse(url=api_response["data"]["url"])
    else:
        return UpdateLongUrlResponse(code=api_response["code"], errors=api_response["errors"])
