from django.db import models
from core.models.auth import User
from datetime import datetime as dt

class Brand(models.Model):
    name = models.CharField(verbose_name='Avtomobil Brendi:', max_length=50)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='Avtomobil Turi:' ,max_length=50)
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    name = models.CharField(verbose_name='Avtomobil nomi: ',max_length=128)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    raqam = models.CharField(verbose_name='Davlat raqami: ', max_length=15)
    yil = models.IntegerField(verbose_name='Mashina yili:', default=2015)
    xk = models.TextField(null=True, blank=True)    #xarakteristika
    narx = models.IntegerField(verbose_name='Kunlik narx:',default=0)
    status = models.BooleanField(default=True) # Activ yoki Activmas

    def __str__(self) -> str:
        return self.name

class Arenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    date_from = models.DateField(auto_now_add=True)
    date_to = models.DateField(default=dt.today().strftime(f'%Y-%m-{dt.today().day+1}'))
    summa = models.BigIntegerField(default=0)
    pay_type = models.CharField(max_length=25, choices=[
        ('Naqt', 'Naqt'),
        ('Plastik', 'Plastik'),
        ('Bo\'lib to\'lash', 'Bo\'lib to\'lash')
    ])
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.phone
    