from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class NavbarPageView(TemplateView):
    template_name = 'navbar.html'

class ProductsPageView(TemplateView):
    template_name = 'products.html'
