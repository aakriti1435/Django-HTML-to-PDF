from django.urls import path
from . import views
# from .views import take_screenshot 

urlpatterns = [
    path('', views.canvas),
    path('/take', views.take_screenshot, name='canvas'),
]