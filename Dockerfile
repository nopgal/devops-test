FROM python:latest

ADD updateString.py .

RUN pip install requests beautifulsoup4

ENTRYPOINT ["python", "./updateString.py"]
