FROM python:3.8

RUN apt update

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /code
COPY . /code/
WORKDIR /code/

# RUN ["ls"]
# RUN ["chmod", "+x", "docker-entrypoint.sh"]

CMD "ls"