FROM python:3.9-slim-buster

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY main.py /app/main.py

# Set environment variable for authentication
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/key/fast-nexus-381802-60ccb90fc180.json

CMD [ "python", "main.py" ]