FROM python:3.9-slim as builder

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv 

#Install deps exactly as locked, no dev deps
RUN uv sync --frozen --no-dev

FROM python:3.9-slim as runtime

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv

COPY app ./app 
COPY static ./static
#activate the virtual environment
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]