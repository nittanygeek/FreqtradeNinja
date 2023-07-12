# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory to the working directory
COPY . .

# Expose the port your Flask app is running on
EXPOSE 5000

# Set the entry point command for the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
