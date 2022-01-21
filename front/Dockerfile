FROM python:3.7.7-slim

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py /app/
COPY requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

EXPOSE 80
WORKDIR /app

CMD ["python", "app.py", "80"]
