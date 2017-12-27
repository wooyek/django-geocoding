# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.
import factory
from . import models


class AbstractAddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.AbstractAddress

    street = factory.Faker("street")
    street_no = factory.Faker("building_number")
    flat_no = factory.Faker("building_number")
    postal_code = factory.Faker("postcode")
    post_town = factory.Faker("city")
    city_town = factory.Faker("city")
    municipality = factory.Faker("city")
    country = factory.Faker("country")
