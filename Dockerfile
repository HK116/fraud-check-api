# Use the official Python image
FROM python:3.11.8

# Set workind directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependecies
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI server
CMD ["uviron", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]