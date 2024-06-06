# Use the official Python image based on Alpine
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev mariadb-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Copy the application code
COPY . /app/

# Install 'uvicorn' for running the FastAPI app with auto-reload
RUN pip install uvicorn

# Command to run the FastAPI application with auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
