from rest_framework import serializers
from .models import Clients, Wallets, Transactions, Services, Operations, Histories

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'name', 'verification_code', 'password', 'email', 'created_at', 'status')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'name', 'wallet_id')