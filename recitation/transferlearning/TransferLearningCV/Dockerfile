# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Copy the files into the container at /app
COPY main.py /app
COPY datasets.py /app

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*
# RUN pip install psutil
RUN pip install -r requirements.txt

# # Define environment variable
# ENV NAME World

# Run app.py when the container launches
RUN python -W ignore datasets.py
CMD ["python", "main.py"]