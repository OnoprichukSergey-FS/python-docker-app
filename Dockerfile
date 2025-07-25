# Base Python image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy files into the container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
