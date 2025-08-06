# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements (if any) and app
COPY app ./app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose port and run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]