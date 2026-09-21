.. _`changelog`:

=========
Changelog
=========

``cheese`` issues are filed on `GitHub <https://github.com/kevinbowen777/cheese/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

cheese 0.3.7 (2026-09-21)
=========================

Contributor-facing changes
--------------------------

-  (`#512 <https://github.com/kevinbowen777/cheese/512>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#516 <https://github.com/kevinbowen777/cheese/516>`_): Update testing to Python 3.14.7, 3.13.15, and 3.12.14

-  (`#516 <https://github.com/kevinbowen777/cheese/516>`_): Update nox to 2026.8.10

-  (`#516 <https://github.com/kevinbowen777/cheese/516>`_): Update django-allauth to 65.19.1

-  (`#520 <https://github.com/kevinbowen777/cheese/520>`_): Update nox to 2026.8.17

-  (`#520 <https://github.com/kevinbowen777/cheese/520>`_): Update django-allauth to 65.19.2

-  (`#520 <https://github.com/kevinbowen777/cheese/520>`_): Update djlint to 1.45.0

-  (`#520 <https://github.com/kevinbowen777/cheese/520>`_): Update django-debug-toolbar to 8.0.0

-  (`#522 <https://github.com/kevinbowen777/cheese/522>`_): Replace master with main in static gh action

-  (`#523 <https://github.com/kevinbowen777/cheese/523>`_): Update django-allauth to 65.19.3

-  (`#523 <https://github.com/kevinbowen777/cheese/523>`_): Update django-countries to 9.1.0

-  (`#523 <https://github.com/kevinbowen777/cheese/523>`_): Update towncrier to 26.9.0

-  (`#523 <https://github.com/kevinbowen777/cheese/523>`_): Upgrade GitHub actions to latest versions

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Update djlint to 1.46.2

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Update django-allauth to 65.19.4

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Update psycopg to 3.3.6

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Add myst-parser dependency


Improved documentation
----------------------

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Add CONTRIBUTING document

-  (`#525 <https://github.com/kevinbowen777/cheese/525>`_): Link CHANGELOG to Sphinx documentation


New features
------------

-  (`#520 <https://github.com/kevinbowen777/cheese/520>`_): Upgrade to Django 6.1.1

cheese 0.3.6 (2026-08-09)
=========================

Improved documentation
----------------------

-  (`#486 <https://github.com/kevinbowen777/cheese/486>`_): Add towncrier 25.8.0.

cheese 0.3.5 (2026-07-23)
=========================

Contributor-facing changes
--------------------------

-  (`#504 <https://github.com/kevinbowen777/cheese/504>`_): Update with Python 3.14.6 & 3.13.14.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#500 <https://github.com/kevinbowen777/cheese/500>`_): Drop support for Python 3.11.


New features
------------

-  (`#472 <https://github.com/kevinbowen777/cheese/472>`_): Upgrade to Django 6.0.7

cheese 0.3.4 (2025-12-08)
=========================

Contributor-facing changes
--------------------------

-  (`#448 <https://github.com/kevinbowen777/cheese/448>`_): Update Docker with Python 3.14 & Postgres 15.15.

-  (`#458 <https://github.com/kevinbowen777/cheese/458>`_): Add Python 3.14 support.


New features
------------

-  (`#592 <https://github.com/kevinbowen777/cheese/592>`_): Upgrade Django to 5.2.8.

cheese 0.3.3 (2025-04-29)
=========================

Contributor-facing changes
--------------------------

-  (`#403 <https://github.com/kevinbowen777/cheese/403>`_): Upgrade PostgreSQL to 15.11.

-  (`#413 <https://github.com/kevinbowen777/cheese/413>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#410 <https://github.com/kevinbowen777/cheese/410>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#539 <https://github.com/kevinbowen777/cheese/539>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#352 <https://github.com/kevinbowen777/cheese/352>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#415 <https://github.com/kevinbowen777/cheese/415>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#417 <https://github.com/kevinbowen777/cheese/417>`_): Replace safety package with pip-audit.

cheese 0.3.2 (2025-01-08)
=========================

Contributor-facing changes
--------------------------

-  (`#342 <https://github.com/kevinbowen777/cheese/342>`_): Upgrade to psycopg 3.

-  (`#348 <https://github.com/kevinbowen777/cheese/348>`_): Add support for Python 3.13

-  (`#390 <https://github.com/kevinbowen777/cheese/390>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#382 <https://github.com/kevinbowen777/cheese/382>`_): Upgrade Django to 5.1.4

cheese 0.3.0 (2024-02-21)
=========================

Contributor-facing changes
--------------------------

-  (`#215 <https://github.com/kevinbowen777/cheese/215>`_): Redirect admin site to non-default URL(/resources)

-  (`#244 <https://github.com/kevinbowen777/cheese/244>`_): Upgrade Poetry to 1.7.0.

-  (`#253 <https://github.com/kevinbowen777/cheese/253>`_): Update Python to 3.12.1.

-  (`#341 <https://github.com/kevinbowen777/cheese/341>`_): Bump Safety version to 2.4.0.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#235 <https://github.com/kevinbowen777/cheese/235>`_): Drop support for Python 3.9.


New features
------------

-  (`#274 <https://github.com/kevinbowen777/cheese/274>`_): Upgrade to Django 5.0.

cheese 0.2.0 (2023-05-09)
=========================

Contributor-facing changes
--------------------------

-  (`#112 <https://github.com/kevinbowen777/cheese/112>`_): Install ruff. Drop flake8-* packages.

cheese 0.1.0 (2023-05-08)
=========================

Contributor-facing changes
--------------------------

- : Add support for Python 3.12.

- : Drop pipenv for project management. Add Poetry.

- : Implement gunicorn for testing

-  (`#41 <https://github.com/kevinbowen777/cheese/41>`_): Mirror to GitLab.

-  (`#43 <https://github.com/kevinbowen777/cheese/43>`_): Re-write for compatibility with Poetry 1.3.2.


Improved documentation
----------------------

-  (`#30 <https://github.com/kevinbowen777/cheese/30>`_): Add Sphinx for documentation


New features
------------

-  (`#96 <https://github.com/kevinbowen777/cheese/96>`_): Upgrade to Django 4.2.

cheese 0.0.1 (2022-10-17)
=========================

New features
------------

- : Build Docker support for Heroku deployment.

-  (`#40 <https://github.com/kevinbowen777/cheese/40>`_): Support Django 4.1.2.


Miscellaneous internal changes
------------------------------

- : Initial commit
