from django.urls import path
from basic_appA import views

app_name = 'basic_appA'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]
