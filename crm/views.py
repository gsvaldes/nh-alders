from django.shortcuts import render
from django.views.generic import TemplateView



class MapView(TemplateView):
    template_name = 'crm/districts_map.html'



