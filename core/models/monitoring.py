from django.db import models
from core.models.auth import User

class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128, default='Rent Card')
    raqam = models.CharField(max_length=20) # 0000 0000 0000 0000
    mask = models.CharField(max_length=20, null= True, blank=True) # 0000. **** **** 0000
    expire = models.CharField(max_length=5) # 00/00
    token = models.CharField(max_length=256, unique=True)
    balance = models.BigIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.name


class Monitoring(models.Model):
    tr_id = models.CharField(max_length=128, unique=True) #Tranzaksiya ID
    sender = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, related_name='sender')
    reciever = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, related_name='reciever')
    amount = models.IntegerField(default=0)
    status = models.SmallIntegerField(default=1) # 1-created 2-o'tqazildi 3-Bekor qilindi

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return self.tr_id





