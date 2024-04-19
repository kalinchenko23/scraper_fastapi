FROM python:3.9 AS base

WORKDIR /scraper_fastapi

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS final

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api_service:app", "--host", "0.0.0.0", "--port", "8000"]