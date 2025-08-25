from server import mcp
from models import ShortUrlRequest, ShortUrlResponse


@mcp.tool()
def generate_short_url(req_data: ShortUrlRequest) -> ShortUrlResponse:
    """
    Generate a short URL for a given long URL.

    Args:
        req_data: The long URL to shorten and additional optional parameters.

    Returns:
        A short URL for the given long URL if success else error code along with the message.
    """

    return ShortUrlResponse(tiny_url="https://vim.onl/demo123")
