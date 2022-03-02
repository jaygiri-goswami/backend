# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /backend

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "mini_proj_flask.py" ]

