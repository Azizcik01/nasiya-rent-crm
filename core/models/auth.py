from typing import Any
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models

class UManager(UserManager):

    def create_user(self, ps_seria, phone=None, password=None, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            ps_seria = ps_seria,
            password = password,
            phone = phone,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user
    def create_superuser(self, ps_seria, phone=None, password=None, is_staff=False, is_superuser=False, **extra_fields):
        return self.create_user(
            ps_seria=ps_seria,
            phone=phone,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )   

class User(AbstractBaseUser, PermissionsMixin):
    
    #       admin
    fio = models.CharField(verbose_name='FIO:', max_length=128)
    username = models.CharField(verbose_name='Username:', max_length=50, null=True, blank=True)
    ps_seria = models.CharField(verbose_name='Passport seria:', max_length=10, unique=True)
    phone = models.CharField(verbose_name='Tel raqam:', max_length=20, unique=True)

    #       user
    g_seria = models.CharField(verbose_name='Guvohnoma seria raqami: ', max_length=15 ,null=True, blank=True)
    g_yil_from = models.CharField(verbose_name='Guvohnoma yili (Berilishi):', max_length=15, null=True, blank=True)
    g_yil_to = models.CharField(verbose_name='Guvohnoma yili (Tugashi):', max_length=15, null=True, blank=True)
    g_ctg = models.CharField(verbose_name='Guvohnoma toifasi', max_length=5 ,null=True, blank=True)

    #       umumiy
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.SmallIntegerField(choices=[
        (1, 'Admin'),
        (2, 'User'),
    ], default=2 )

    objects = UManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['ps_seria']


    def get_user_name(self):
        return f'{self.fio.split()[0] if not self.username else self.username}'
    
    












