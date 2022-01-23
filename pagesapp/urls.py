from django.urls import path
from .views import HomePageView, AboutPageView, ProductsPageView, NavbarPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('navbar/', NavbarPageView.as_view(), name='navbar'),
    path('products/', ProductsPageView.as_view(), name='products'),
]