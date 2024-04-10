
FROM python:3.12.0-bullseye


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

ENV PYTHONUNBUFFERED 1

RUN pip install  -r /app/requirements.txt


COPY . .


EXPOSE 8000