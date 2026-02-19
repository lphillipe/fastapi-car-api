FROM python:3.13.11-alpine3.22

SHELL ["/bin/sh", "-o", "pipefail", "-c"]
ARG POETRY_VERSION=2.3.2

RUN apk add curl && \
    curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY . .
RUN poetry install --without dev

CMD ["poetry", "run", "fastapi", "dev", "car_api/app.py", "--host", "0.0.0.0"]