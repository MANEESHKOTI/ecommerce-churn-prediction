FROM python:3.9-slim

WORKDIR /app

# Install system dependencies (from your instructions)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# --- CRITICAL FIX ---
# We use streamlit run instead of python --version
# This keeps the container ALIVE so 'docker-compose exec' works.
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]