FROM python:3.13-slim

WORKDIR /app/rag

# copies backend folder from host into /app/rag/backend in container
COPY backend backend
COPY knowledge_base knowledge_base

# this makes the package structure intact -> will see the rag folder
ENV PYTHONPATH=/app 

# install uv on the container
RUN pip install --no-cache-dir uv

WORKDIR /app/rag/backend

# this installs the dependencies specified in pyproject.toml into a .venv
RUN uv sync --no-dev

CMD [ "uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000" ]

