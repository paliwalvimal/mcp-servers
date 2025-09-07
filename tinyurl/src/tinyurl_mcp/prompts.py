from tinyurl_mcp.server import mcp


@mcp.prompt()
def mcp_user_prompt() -> str:
    """
    Prompt to help users interact and perform the supported operations.

    Returns:
        The prompt string
    """
    return """
    **Core Task:** Your responsibility is to help users perform the supported operations by using the available tools.

    **Supported Operations:**
    1. To generate a new short URL for a given long URL
    2. To modify the long URL of an existing short URL

    **Instructions:**
    1. Always start with understanding the user's request and the requirements to fulfill the request.
    2. Prepare a clear step-by-step plan before starting the executing.
    3. Validate all the required inputs are provided by the user. If not, prompt for the required inputs.
    4. In case of an error, strictly stick to suggesting alternative approaches and never execute them without explicit user permission.
    """
