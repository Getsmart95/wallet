from rest_framework import serializers
from .models import Clients, Wallets, Transactions, Services, Operations, Histories

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'name', 'verification_code', 'password', 'email', 'created_at', 'status')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'wallet',  'name')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id', 'wallet', 'wallet_partner', 'operation_type', 'created_at', 'status', 'amount')

class WalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ('id', 'client', 'currency', 'balance', 'status', 'entity')

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('id', 'service', 'transaction', 'requisite', 'status', 'created_at')