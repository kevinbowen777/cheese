cheese
======

.. toctree::
   :hidden:
   :maxdepth: 1

   package_index
   create_new_users

.. contents:: Table of Contents
   :local:
   :backlinks: top
   :depth: 2

- A cheese index application

cheese is a basic demonstration of Django functionality using a `Cookiecutter <https://github.com/feldroy/django-crash-starter>`_ template.

Features
--------

 * Application

   * Add cheeses with a description, firmness, & country of origin
   * User registration with email verification & social(GitHub) login using `django-allauth <https://pypi.org/project/django-allauth/>`_
   * `Bootstrap4 <https://pypi.org/project/django-bootstrap4/>`_ & `crispy-forms <https://pypi.org/project/django-crispy-forms/>`_ decorations
   * Customizable user profile pages with bio, profile pic, & `country flags <https://pypi.python.org/pypi/django-countries>`_
   * Centered account templates(login, registration, verification, etc.)
 * Dev/testing

   * Basic module testing templates
   * `Coverage <https://pypi.org/project/coverage/>`_ reports in `htmlcov` directory
   * `Debug-toolbar <https://pypi.org/project/django-debug-toolbar/>`_ available. See notes in `config/settings.py` for enabling.
   * Examples of using `Factories <https://pypi.org/project/factory-boy/>`_ & `pytest <https://pypi.org/project/pytest/>`_ fixtures in account app testing
   * `shell_plus <https://django-extensions.readthedocs.io/en/latest/shell_plus.html>`_ with `IPython <https://pypi.org/project/ipython/>`_ via `django-extensions <https://pypi.python.org/pypi/django-extensions/>`_ package
   * `Nox <https://pypi.org/project/nox/>`_ testing sessions for latest Python 3.9, 3.10, and 3.11

     * `black <https://pypi.org/project/black/>`_
     * `Sphinx <https://pypi.org/project/Sphinx/>`_ documentaion generation
     * linting
       
       * `flake8 <https://pypi.org/project/flake8/>`_
       * `flake8-bandit <https://pypi.org/project/flake8-bandit/>`_
       * `flake8-bugbear <https://pypi.org/project/flake8-bugbear/>`_
       * `flake8-import-order <https://pypi.org/project/flake8-import-order/>`_
     * `safety <https://pypi.org/project/safety/)(python package vulnerability testing>`_
     * `pytest sessions <https://docs.pytest.org/en/latest/>`_ with `pytest-cov <https://pypi.org/project/pytest-cov/>`_ & `pytest-django <https://pypi.org/project/pytest-django/>`_

Installation
------------

To install the cheese project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/cheese.git
   $ cd cheese

Local installation
------------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ createdb cheese (Requires Postgres 13)
   $ python manage.py migrate
   $ python manage.py createsuperuser
   

Docker installation
-------------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run django_start, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Application Demo
----------------
Live demonstration of application running on Heroku:

TBD

Reporting Bugs
--------------

Visit the cheese `Issues page <https://github.com/kevinbowen777/cheese/issues>`_ on GitHub.