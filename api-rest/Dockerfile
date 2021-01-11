FROM python:3-alpine

LABEL Description="Simple service to request HTTP endpoint and print result to stdout"

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY code .

ENTRYPOINT ["python","main.py"]
