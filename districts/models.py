from django.contrib.gis.db import models as geomodels
from django.db import models

from django.core.validators import RegexValidator


class AlderDistrict(geomodels.Model):
    shape_area = geomodels.IntegerField()
    wards_desc = geomodels.CharField(max_length=50)
    alder = geomodels.CharField(max_length=100)  #  TODO make foreign key to alder model
    lci_ward_g = geomodels.CharField(max_length=50)
    shape_length = geomodels.IntegerField()
    wards = geomodels.IntegerField()
    wards_txt = geomodels.CharField(max_length=2)

    mpoly = geomodels.MultiPolygonField()

    class Meta:
        ordering = ('wards',)

    def __str__(self):
        return self.wards_desc


class PostalAddress(models.Model):
    address = models.CharField(
        verbose_name="Address line",
        max_length = 90,
        blank = True
    ) 
    city = models.CharField(verbose_name='City', max_length=50)
    state = models.CharField(verbose_name='State', max_length=2)
    zip_code = models.CharField(verbose_name="Zip Code", max_length = 10)


class Organization(models.Model):
    name = models.CharField(max_length=300)
    address = models.ForeignKey('PostalAddress', on_delete=models.PROTECT)


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    district = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
         message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
         )
    phone_number = models.CharField(
        # validators=[phone_regex],
        max_length=15,
        blank=True
        )
    email = models.EmailField(max_length=200, verbose_name = "Email Address")
    address = models.ForeignKey('PostalAddress', on_delete=models.PROTECT)
    ismemberof = models.ManyToManyField('Organization', verbose_name = 'Is member of', blank=True, null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

    class Meta:
        ordering = ('last_name',)


#  TODO make alder model that subclasses person




