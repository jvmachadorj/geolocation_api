from django.contrib.gis.db.models import PolygonField
from django.db import models
from phone_field import PhoneField


class Providers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneField()
    language = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)

    def __str__(self):
        return 'Provider:{}-{}'.format(self.id, self.name)


class ServiceAreas(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    service_area = PolygonField(blank=False, null=False)
    provider = models.ForeignKey(Providers, on_delete=models.PROTECT)

    def __str__(self):
        return 'Service Area:{}-{}'.format(self.id, self.name)
