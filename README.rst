===========================
Django geocoding for models
===========================


.. image:: https://img.shields.io/pypi/v/django-geocoding.svg
        :target: https://pypi.python.org/pypi/django-geocoding

.. image:: https://img.shields.io/travis/wooyek/django-geocoding.svg
        :target: https://travis-ci.org/wooyek/django-geocoding

.. image:: https://readthedocs.org/projects/django-geocoding/badge/?version=latest
        :target: https://django-geocoding.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/wooyek/django-geocoding/badge.svg?branch=develop
        :target: https://coveralls.io/github/wooyek/django-geocoding?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/wooyek/django-geocoding/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/wooyek/django-geocoding
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/wooyek/django-geocoding/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/wooyek/django-geocoding.svg
        :target: https://github.com/wooyek/django-geocoding/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/wooyek/django-geocoding.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/wooyek/django-geocoding
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/wooyek

Abstract base models and mixins to store address and GPS coordinates info

* Free software: MIT license
* Documentation: https://django-geocoding.readthedocs.io.

Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

Install Django geocoding for models::

    pip install django-geocoding

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_geocoding.apps.DjangoGeocodingConfig',
        ...
    )

Add Django geocoding for models's URL patterns:

.. code-block:: python

    from django_geocoding import urls as django_geocoding_urls


    urlpatterns = [
        ...
        url(r'^', include(django_geocoding_urls)),
        ...
    ]


Running Tests
-------------

Does the code actually work?

::
    $ pipenv install --dev
    $ pipenv shell
    $ tox


We recommend using pipenv_ but a legacy approach to creating virtualenv and installing requirements should also work.
Please install `requirements/development.txt` to setup virtual env for testing and development.


Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install#fancy-installation-of-pipenv
