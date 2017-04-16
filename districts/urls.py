from django.conf.urls import url, include
from rest_framework import routers, viewsets
from districts.models import AlderDistrict
from districts.serializers import DistrictSerializer


class DistrictViewSet(viewsets.ModelViewSet): # TODO move to views.py
    queryset = AlderDistrict.objects.all()
    serializer_class = DistrictSerializer


router = routers.DefaultRouter()
router.register(r'districts', DistrictViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]







