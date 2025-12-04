FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

# ➜ 這行是關鍵，讓 Python 找得到 /app/src/app
ENV PYTHONPATH="/app/src"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
