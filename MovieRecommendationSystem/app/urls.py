# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('', navbar, name='navbar'),
    path('login', login, name='login'),
    path('register', register_view, name='register'),

]
