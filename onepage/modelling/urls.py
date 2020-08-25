from django.urls import path

from . import views

urlpatterns = [
    path('', views.modelling, name='modellingg')
]
