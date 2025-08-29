from server import mcp


@mcp.prompt()
def generate_short_url_prompt() -> str:
    """
    Prompt to use while generating a short URL.

    Returns:
        The prompt string
    """
    return """
    **Core Task:** Help user generate a short URL for the given URL

    **Instructions:**
    1. Always start with understanding the user's request and plan the steps before executing the tools.
    2. Validate all the required inputs are provided by the user. If not, prompt for the required inputs.
    3.
    """
