FROM python:3.7.7-slim

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY details.py /app/
COPY requirements.txt /app/

WORKDIR /app
EXPOSE 80

CMD ["python", "details.py", "80"]
