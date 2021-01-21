from django.urls import path
from . import views

app_name = 'dust_checker'

urlpatterns = [
    path('', views.index, name='index'),
    path('/detail/<str:itemCode>/', views.detail, name='detail'),
    path('/robot/', views.robot,name='robot'),
    path('/robot/getserver.php/', views.server)
]