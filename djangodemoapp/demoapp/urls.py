from django.urls import path
from . import views
from .views import predict, demoapp

urlpatterns = [
    path('predict/', predict, name='predict'),
    path('demoapp/', views.demoapp, name='demoapp'),
]
