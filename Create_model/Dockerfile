# Use a slim version of Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container's working directory
COPY .  /app

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start the FastAPI application using Uvicorn
# Note: 'APP.main:app' refers to 'main.py' inside the 'APP' folder
CMD ["uvicorn", "APP.main:app", "--host", "0.0.0.0", "--port", "8000"]
