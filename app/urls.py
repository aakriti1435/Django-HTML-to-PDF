from django.urls import path
from .views import GeneratePDF

urlpatterns = [
    # path('', views.home , name='home')
    path('pdf/', GeneratePDF.as_view()), 
]
