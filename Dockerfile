FROM python:3.11.8-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8081 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8081"]
