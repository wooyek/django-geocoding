# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_geocoding.models import AbstractAddress, AbstractLocation

from django_powerbank.db.models.fields import UniqueSlugField


class NamedModel(AbstractLocation, AbstractAddress):
    name = models.CharField(max_length=150, verbose_name=_('name'))

