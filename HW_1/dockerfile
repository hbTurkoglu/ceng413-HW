FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create an unprivileged user and a data folder it may write to.
RUN useradd --create-home --uid 10001 appuser && mkdir -p /data && chown appuser:appuser /data
USER appuser

ENV DATA_DIR=/data GREETING="Hello from CENG413 HW1!"
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]