import logging

import pytz
from django.contrib.gis.db.models import PointField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

# from django_tasker.decoration import queueable

COUNTRY_CHOICES = sorted(pytz.country_names.items(), key=lambda x: x[1])


class AbstractAddress(models.Model):
    street = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('street'))
    street_no = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('street no'))
    flat_no = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('flat no'))
    postal_code = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=_('postal code'))
    post_town = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('post town'))
    city_town = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('city town'))
    municipality = models.CharField(max_length=200, blank=True, null=True, help_text="State/Province", db_index=True, verbose_name=_('municipality'))
    country = models.CharField(choices=COUNTRY_CHOICES, null=True, blank=True, max_length=2, db_index=True, verbose_name=_('country'))

    class Meta:
        abstract = True

    @cached_property
    def address(self):
        data = {
            "street": self.street,
            "street_no": self.street_no,
            "postal_code": self.postal_code,
            "post_town": self.post_town,
            "municipality": self.municipality,
            "country": self.country or "",
        }
        return "{street} {street_no}, {postal_code} {post_town}, {municipality}, {country}".format(**data)


DEFAULT_SRID = 4326


class AbstractLocation(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('location'))
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="latitude ", help_text=_("Horizontal coordinate"))
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="longitude", help_text=_("Vertical coordinate"))
    point = PointField(srid=DEFAULT_SRID, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.lat and not self.lng or not self.lat and self.lng:
            raise ValidationError(_("Both lat and lng must be set or both left empty"))
        if hasattr(self, "point"):  # Poor's man feature switch
            if self.lng and self.lat:
                from django.contrib.gis.geos import Point
                self.point = Point(float(self.lng), float(self.lat), srid=4326)
            else:
                self.point = None

    @property
    def has_coordinates(self):
        return self.lat is not None and self.lng is not None

    def lazy_geocoding(self):
        logging.debug("self.location: %s", self.location)
        existing = self.__class__.objects.filter(location=self.location, lat__isnull=False, lng__isnull=False).order_by('-id').first()
        logging.debug("existing: %s", existing)
        if existing:
            self.update_address_properties(existing)
            self.save()
            return True

    def update_address_properties(self, exiting):
        logging.debug("exiting: %s %s", exiting.lat, exiting.lng)
        self.lat = exiting.lat
        self.lng = exiting.lng
        self.street = exiting.street
        self.street_no = exiting.street_no
        self.postal_code = exiting.postal_code
        self.city_town = exiting.city_town
        self.municipality = exiting.municipality
        self.country = exiting.country

    # @queueable(queue='geocoding', rate_limit=100)
    def geocode(self):
        self._geocode()

    def _geocode(self):
        logging.debug("self.location: %s", self.location)
        assert self.location
        from django_geocoding.backends.opencage import geocode_address
        geocode_address(self)
        self.save()


class DoubleLineAbstractAddress(AbstractAddress):
    address_line = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True
