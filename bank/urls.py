from django.urls import path

from bank import views

urlpatterns = [
    path('',views.hello, name='hello'),
]

