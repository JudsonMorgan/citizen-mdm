FROM python:3.9-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


ENV DATABASE_URL=postgresql://root:root@db:5432/citizen_mdm

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
