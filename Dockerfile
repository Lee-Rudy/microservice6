FROM python:3.13-slim

WORKDIR /app

ENV POETRY_REQUESTS_TIMEOUT=600 \
    POETRY_NO_INTERACTION=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry


COPY project/pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction


COPY project/main.py ./main.py
COPY project/src ./src

EXPOSE 8001

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]