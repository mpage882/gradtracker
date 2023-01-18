from django.urls import path, include
from .views import UserRegister


app_name = 'users'
urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserRegister.as_view(), name='login'),
    
]