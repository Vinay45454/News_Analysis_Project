## 5. Deployment docker local environment

# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_CACHE=1

# Set the working directory
WORKDIR /app/

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install spaCy and download the model
RUN pip install --no-cache-dir spacy && \
    python -m spacy download en_core_web_sm

# Copy application code
COPY . .

# Expose port for Streamlit
EXPOSE 8501

# Run the Streamlit server
CMD ["streamlit", "run", "news_scraper.py", "--server.port=8501", "--server.enableCORS=false"]
