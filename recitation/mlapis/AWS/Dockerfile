# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY main.py .

# # Set environment variables for AWS credentials (you can also use AWS IAM Roles for EC2)
# ENV AWS_ACCESS_KEY_ID=<your_access_key_id>
# ENV AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
# ENV AWS_REGION=<your_aws_region>

# Set the command to run your Python script
CMD ["python", "my_script.py"]