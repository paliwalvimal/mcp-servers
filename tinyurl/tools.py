from server import mcp
from models import ShortUrlRequest, ShortUrlResponse
from utils import make_api_request


@mcp.tool()
def generate_short_url(req_data: ShortUrlRequest) -> ShortUrlResponse:
    """
    Generate a short URL for a given long URL.

    Args:
        req_data: The long URL to shorten and additional optional parameters.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """
    api_response = await make_api_request(api_path="create", req_data=req_data.model_dump())

    return ShortUrlResponse(api_response)
