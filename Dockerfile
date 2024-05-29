# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y python3-tk xvfb && \
    rm -rf /var/lib/apt/lists/*

# Install other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["xvfb-run", "--auto-servernum", "--server-args=-screen 0 640x480x24", "python", "gui.py"]
