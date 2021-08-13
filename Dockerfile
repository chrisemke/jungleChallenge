FROM python:3.9.6

LABEL maintainer="chrisemke"
LABEL app="junglechallenge"

ADD . /app

EXPOSE 8000

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python"]

CMD ["/app/app/manage.py", "runserver", "0.0.0.0:8000"]
