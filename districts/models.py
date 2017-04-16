from django.contrib.gis.db import models


class AlderDistrict(models.Model):
    shape_area = models.IntegerField()
    wards_desc = models.CharField(max_length=50)
    alder = models.CharField(max_length=100)
    lci_ward_g = models.CharField(max_length=50)
    shape_length = models.IntegerField()
    wards = models.IntegerField()
    wards_txt = models.CharField(max_length=2)

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.wards_desc


