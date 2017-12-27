=====
Usage
=====

To use Django geocoding for models in a project, add it to your `INSTALLED_APPS`:

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
