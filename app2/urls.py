app_name='two'
from django.urls import path 
from app1.views import *

urlpatterns = [
    path('virat/',virat,name='virat'),
]