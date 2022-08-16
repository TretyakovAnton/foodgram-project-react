FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]
