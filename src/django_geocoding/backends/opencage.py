# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.
from __future__ import absolute_import

import logging


def geocode_lat_lng(address):
    from opencage.geocoder import OpenCageGeocode
    from django.conf import settings
    api_key = settings.OPENCAGE_API_KEY
    geocoder = OpenCageGeocode(api_key)
    location = geocoder.geocode(address)

    if location:
        return location[0]['geometry']['lat'], location[0]['geometry']['lng']
    return None, None


def geocode_address(model):
    location = geocode_location(model.location)
    logging.debug("location: %s", location)
    if location:
        location = location[0]
        model.lat = location['geometry'].get('lat')
        model.lng = location['geometry'].get('lng')
        model.street = location['components'].get('road')
        model.street_no = location['components'].get('house_number')
        model.postal_code = location['components'].get('postcode')
        model.city_town = location['components'].get('city')
        model.municipality = location['components'].get('state')
        model.country = (location['components'].get('country_code') or '').upper()
    return model


def geocode_location(location):
    from opencage.geocoder import OpenCageGeocode
    from django.conf import settings
    geocoder = OpenCageGeocode(settings.OPENCAGE_API_KEY)
    location = geocoder.geocode(location)
    return location
