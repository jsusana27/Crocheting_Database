# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# INstall Tkinter dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf \var\lib\apt\lists\*

# Make port 8080 availalbe to the world outside this container
EXPOSE 8080

# Run the application
CMD ["python", "gui.py"]
