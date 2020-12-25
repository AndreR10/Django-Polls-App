from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView, name="home"),
    path('create_record/', views.CreateRecordView, name="create-record"),
    path('record/<str:pk>', views.DetailRecordView, name="detail-record"),
    path('update_record/', views.UpdateRecordView, name="update-record"),
]
