from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_page_image'] = '/static/img/333064805_760223689005819_9082627831218226945_n.jpg'
        return context
