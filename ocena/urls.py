from django.urls import path

from . import views

urlpatterns = [
    path("main/", views.main, name='main'),
    path("final/", views.final, name='final'),
]
