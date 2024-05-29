# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Python output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Expose the port your application will run on
EXPOSE 5000

# Run the application
CMD ["python", "gui.py"]
