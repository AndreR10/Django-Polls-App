from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView, name="home"),
    path('log/<str:pk>', views.DetailLogView, name="detail-log"),
    path('create_log/', views.CreateLogView, name="create-log"),
    path('update_log/<str:pk>/',
         views.UpdateLogView,
         name="update-log")
]
