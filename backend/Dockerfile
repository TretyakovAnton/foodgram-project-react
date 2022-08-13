FROM python:3.7-slim

WORKDIR /app



RUN python -m pip install --upgrade pip

COPY requirements.txt .
#WORKDIR /app/backend

RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]
