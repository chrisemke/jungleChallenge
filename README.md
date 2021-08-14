# <img src="https://workable-application-form.s3.amazonaws.com/advanced/production/602fa5aa3e0ec0b348d83793/54d46f43-ba92-9697-8a90-83bcec01b674" width="350" height="80"> Challenge

[![NPM](https://img.shields.io/github/license/chrisemke/jungleChallenge)](https://github.com/chrisemke/jungleChallenge/blob/main/LICENSE)

<details open>
<summary>Index:</summary>
  
+ [About](#about)
+ [Tecnologies](#tecnologies)
+ [Setup](#setup)
+ [Run](#run)
+ [Tests](#tests)
</details>

## About
### API for jungle code challenge
Biggest difficulties of this challenge: Docker (I've never used it before) and some difficulties with django itself

## Tecnologies

* [Python](https://www.python.org/downloads/release/python-396/)
* [PostgreSQL](https://www.postgresql.org/)
* [Django](https://www.djangoproject.com/)
* [Django rest framework](https://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)
* [Poetry](https://python-poetry.org/)

## Setup
> Needed for production: git and docker

> Needed for developing: git, docker, python, poetry, postgresql

## Run
1: You need to clone the repository

2: Open a terminal inside of the root directory of the project

3: Run: ```docker-compose up --build -d```

4: You can check if the containers are running ```docker-compose ps```
   The result should be something like this:
```docker
Name                Command               State                    Ports                  
--------------------------------------------------------------------------------------------
django     python /app/app/manage.py  ...   Up      0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
postgres   docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp,:::5432->5432/tcp
```

## Tests

1: You need to open a terminal on "app" directory

2: For run all tests you need to run this command: ```python manage.py test```
