from pathlib import Path
from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('submit',views.submit,name="submit")
]