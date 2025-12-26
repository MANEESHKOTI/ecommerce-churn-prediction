# Base image [cite: 177]
FROM python:3.9-slim

# Set working directory [cite: 178]
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage cache
COPY requirements.txt .

# Install Python dependencies [cite: 184]
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files [cite: 185]
COPY . .

# Expose Streamlit port [cite: 186]
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Default command
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]