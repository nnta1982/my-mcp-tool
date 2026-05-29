FROM python:3.12-slim

WORKDIR /app

# Copy requirements trước để cache layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Chạy trực tiếp app FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]