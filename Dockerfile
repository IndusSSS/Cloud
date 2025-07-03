FROM python:3.12-slim
WORKDIR /app
ENV POETRY_VERSION=1.6.1
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --only main
COPY . .
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
