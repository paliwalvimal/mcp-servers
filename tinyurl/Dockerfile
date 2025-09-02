# Build stage - Use a Python image with uv pre-installed
FROM mirror.gcr.io/astral/uv:0.8-python3.13-trixie-slim AS builder

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Install the project's dependencies using the lockfile and settings
COPY uv.lock pyproject.toml .
RUN uv sync --frozen --no-install-project --no-dev --no-editable

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . .
RUN uv build && uv pip install dist/*.whl


# Production stage - Use minimal python image
FROM mirror.gcr.io/python:3.13-slim-trixie

WORKDIR /app

# Create app user
RUN groupadd -g 1000 app && useradd -u 1000 -g app -s /bin/sh app

COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Change user
USER app

# Run the MCP server by default
ENTRYPOINT [ "tinyurl-mcp-server" ]
