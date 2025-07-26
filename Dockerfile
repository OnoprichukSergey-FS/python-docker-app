# Start with base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements (if exists) or manually install Flask
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of your app
COPY . .

# Expose the port your app runs on (make sure it matches ECS config!)
EXPOSE 5001

# Run your app
CMD ["python", "app.py"]
