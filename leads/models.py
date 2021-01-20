from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=100)
    verification_code = models.IntegerField()
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

class Wallets(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT)
    currency = models.CharField(max_length=20)
    balance = models.IntegerField()
    status = models.CharField(max_length=50)
    entity = models.BooleanField()

class Transactions(models.Model):
    wallet = models.ForeignKey(Wallets, on_delete=models.PROTECT, related_name='transfer_from')
    wallet_partner = models.ForeignKey(Wallets, on_delete=models.PROTECT, related_name='transfer_to')
    operation_type = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()

class Services(models.Model):
    name = models.CharField(max_length=100)
    wallet = models.ForeignKey(Clients, on_delete=models.PROTECT)

class Operations(models.Model):
    service = models.ForeignKey(Services, on_delete=models.PROTECT)
    transaction = models.ForeignKey(Transactions, on_delete=models.PROTECT)
    requisite = models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Histories(models.Model):
    wallet_id = models.IntegerField()
    transaction = models.ForeignKey(Transactions, on_delete=models.PROTECT)
    operation = models.ForeignKey(Operations, on_delete=models.PROTECT)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
