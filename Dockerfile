FROM python:3.11-slim

WORKDIR /app

COPY ./app ./app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV MONGO_URI="<YOUR_MONGODB_ATLAS_CONNECTION_STRING>"
ENV SECRET_KEY="your_secret_key"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
