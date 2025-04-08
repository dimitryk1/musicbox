# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /rockapp

# Copy requirements file (creating this first)
RUN echo "flask==2.0.1\nwerkzeug==2.0.3\naws-xray-sdk==2.10.0" > requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API code
COPY rockapp.py .

# Expose port 9003
EXPOSE 9003

# Run the API
CMD ["python", "rockapp.py"]