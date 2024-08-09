# Use a slim version of Python based on Debian Buster
FROM python:3.9.7-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install required system packages using apt-get (since this is a Debian-based image)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Command to run the application
CMD ["python", "./main.py"]
