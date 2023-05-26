app_name='one'

from django.urls import path 
from app1.views import *

urlpatterns=[
    path('msd/',msd,name='msd'),
    
]