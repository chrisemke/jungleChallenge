FROM python:3.9.6

LABEL maintainer="chrisemke"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000

RUN pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENTRYPOINT ["python"]

CMD ["jungleChallenge/manage.py", "runserver", "0.0.0.0:8000"]

ENV PATH="/py/bin:$PATH"

USER app