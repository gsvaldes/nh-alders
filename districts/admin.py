from django.contrib.gis import admin as geoadmin
from django.contrib import admin
from districts.models import AlderDistrict, Person, Organization, PostalAddress


geoadmin.site.register(AlderDistrict, geoadmin.GeoModelAdmin)

admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(PostalAddress)




