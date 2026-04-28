# 1. Use a lightweight Python image
FROM python:3.11-slim-bullseye

# 2. Set environment variables
# Prevents Python from writing .pyc files and keeps output unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install system dependencies
# These are required for PostgreSQL (psycopg2) and general build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
# We copy only requirements first to leverage Docker's cache layers
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Expose the port Django runs on
EXPOSE 8000

# 8. Use a script or direct command to run the server
# In production, you'd use 'gunicorn', but for development, we use manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
