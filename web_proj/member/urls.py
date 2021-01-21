from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'board'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
    path('board/',views.board,name='index'),
    path('answer/create/<int:postId>/',views.answer_create,name='answer_create'),
    path('board/<int:postId>/',views.detail, name='detail'),
    path('signup/', views.def, name='signup'),
]