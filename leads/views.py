from django.shortcuts import render
from .models import Clients, Services, Wallets, Transactions, Operations
from .serializers import ClientSerializer, ServiceSerializer, TransactionSerializer, OperationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import F
from aiohttp import web
import aiohttp
import asyncio
from wallet_Python import views

class ClientListCreate(generics.ListCreateAPIView, web.View):
    model = 'leads.Clients'
    async def get_queryset(self):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.all)

    async def get(self):
        queryset = await self.get_queryset()
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


async def call_api():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://api.github.com/events') as resp:
            response = await resp.read()
            print(response)

asyncio.run(call_api())
