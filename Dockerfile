FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /src/

RUN poetry install --no-root --no-dev

COPY . /src/

EXPOSE 8000

CMD ["sh", "-c", "poetry run uvicorn src.main:app --host ${SITE_HOST} --port ${SITE_PORT}"]
