from django.urls import path
from . import views

urlpatterns = [
    path('demoapp/', views.demoapp, name='demoapp'),
]
