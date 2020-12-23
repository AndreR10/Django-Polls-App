from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView, name="home"),
    path('create_record/', views.CreateRecordView, name="create-record")
]
