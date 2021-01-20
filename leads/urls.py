from django.urls import path
from . import views

urlpatterns = [
    path('api/addClient/', views.ClientListCreate.as_view()),
    path('api/services/', views.ServicesListCreate.as_view()),
]
