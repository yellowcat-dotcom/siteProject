from django.urls import path
from . import views
from .views import configuration_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('configuration/', configuration_view, name='configuration'),
]