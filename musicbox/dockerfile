# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file (creating this first)
RUN echo "requests\nflask==2.0.1\nwerkzeug==2.0.3\naws-xray-sdk==2.10.0" > requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API code
COPY musicbox.py .

# Expose port 9000
EXPOSE 9000

# Run the API
CMD ["python", "musicbox.py"]