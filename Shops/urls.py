# shops/urls.py
from django.urls import path
from .views import register_shop, search_shops

urlpatterns = [
    path('', register_shop, name='register_shop'),
    path('search/', search_shops, name='search_shops'),
]
