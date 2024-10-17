from django.urls import path
from .views import homepage, login, register

urlpatterns = [
    path('', homepage,name='homepage'),
    path('login', login,name='login'),
    path('register', register, name='register')
]