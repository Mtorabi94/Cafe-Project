from django.urls import path
from .views import index_view, menu_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('menu/', menu_view, name='menu'),
]