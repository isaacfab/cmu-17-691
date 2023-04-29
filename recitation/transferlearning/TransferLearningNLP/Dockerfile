# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py /app
COPY requirements.txt /app

# Install any needed packages
RUN python -m pip install --upgrade pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

# Download the pre-trained model
RUN transformers-cli download t5-small

# Run the command to start the application
CMD ["python", "main.py"]