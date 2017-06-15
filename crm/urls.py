from django.conf.urls import url, include
from crm import views


urlpatterns = [
    url(r'^map/$', views.MapView.as_view(), name='map'),
]