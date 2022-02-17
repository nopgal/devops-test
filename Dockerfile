FROM python:latest

ADD updateString.py .

ENTRYPOINT ["python", "./updateString.py"]
