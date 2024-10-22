from django.urls import path
from .views import *
urlpatterns = [
    path('',views.hello, name='hello'),
]

