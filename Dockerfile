FROM python:latest


# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["updateString.py"]
