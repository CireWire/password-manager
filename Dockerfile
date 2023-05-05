# Use Python 3.8 as the base image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the working directory
COPY . .

# Expose port 8000 for the Flask web server
EXPOSE 8000

# Start the app with the "python" command
CMD ["python", "password_manager.py"]
