FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY api.py /app.py

CMD ["python3", "/app.py"]





