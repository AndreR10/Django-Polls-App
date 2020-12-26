from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView, name="home"),
    path('record/<str:pk>', views.DetailRecordView, name="detail-record"),
    path('create_record/', views.CreateRecordView, name="create-record"),
    path('update_record/<str:pk>/',
         views.UpdateRecordView,
         name="update-record")
]
