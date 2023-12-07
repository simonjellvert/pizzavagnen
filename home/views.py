from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    """
    Template for home page
    """
    template_name = 'home/index.html'
