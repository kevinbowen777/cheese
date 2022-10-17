## cheese 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/cheese.svg)](https://github.com/kevinbowen777/cheese/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A cheese index application

cheese is a basic demonstration of Django functionality using a [Cookiecutter](https://github.com/feldroy/django-crash-starter) template.

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---
## Features
 - None. Two simple web pages build with Django

---

### Installation
 - `git clone https://github.com/kevinbowen777/cheese.git`
 - `cd cheese`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### Application Demo
 - TBD
 
---
### Screenshots

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/cheese/issues)
      to view currently open bug reports or open a new issue.
