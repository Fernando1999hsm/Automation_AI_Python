FROM mcr.microsoft.com/playwright/python:v1.52.0-focal

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install chromium

COPY . /app

ENV HEADLESS=true
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "pytest", "-v"]