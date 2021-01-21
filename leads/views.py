from django.shortcuts import render
from .models import Clients, Services, Wallets, Transactions, Operations
from .serializers import ClientSerializer, ServiceSerializer, TransactionSerializer, OperationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import F

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

class ServicesListCreate(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

@api_view(['POST'])
@csrf_exempt
def payment_service(request):
    if request.method == 'POST':
        serializerTransaction = TransactionSerializer(data=request.data)

        amount = request.data.get('amount')
        wallet_id_from = request.data.get('wallet')
        wallet_id_to = request.data.get('wallet_partner')
        service_id = request.data.get('service')
        requisite = request.data.get('requisite')
        created_at = request.data.get('created_at')

        if wallet_id_from == wallet_id_to:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if serializerTransaction.is_valid():
            serializerTransaction.save()
            transaction_id = serializerTransaction.data['id']
            Wallets.objects.filter(id=wallet_id_from).update(balance = F('balance') - amount)
            Wallets.objects.filter(id=wallet_id_to).update(balance = F('balance') + amount)

            serializerOperation = Operations(service_id=service_id, transaction_id=transaction_id, requisite=requisite, status="Done", created_at=created_at)
            serializerOperation.save()
            Transactions.objects.filter(id=transaction_id).update(status="Done")

            return Response(serializerTransaction.data, status=status.HTTP_201_CREATED)
        return Response(serializerTransaction.errors, status=status.HTTP_400_BAD_REQUEST)

# def payment_status(request):
#     if request.method == 'GET':
#         queryset = Operations.objects.filter(id=re)
#         serializer_class = ServiceSerializer