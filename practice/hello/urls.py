from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("mike", views.mike, name="mike"),
    path("marvhiee", views.marvhiee, name="marvhiee")
]