FROM python:3.13-slim

WORKDIR /app

COPY frontend frontend

RUN pip install --no-cache-dir uv 

WORKDIR /app/frontend

RUN uv sync --no-dev

CMD ["uv", "run", "streamlit", "app.py", "--server.port", "8501", "--server.adress", "0.0.0.0"]