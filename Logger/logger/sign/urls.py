from django.urls import path
from . import views

urlpattern = [
    path('login/', views.Login, name="in"),
]
