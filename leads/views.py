from django.shortcuts import render
from .models import Clients, Services
from .serializers import ClientSerializer, ServiceSerializer
from rest_framework import generics

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

class ServicesListCreate(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
# class WalletViewSet()