FROM python:3.11
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "web_concurrency.wsgi", "-w", "2", "-b", "0.0.0.0:8000"]
