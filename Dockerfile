FROM python:3.9.7-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "python healthcheck.py & python main.py"]
EXPOSE 8080
EXPOSE 8080

