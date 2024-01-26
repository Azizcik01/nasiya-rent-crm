from contextlib import closing
from django.db import connection
from django.shortcuts import redirect, render
import random
from methodism import generate_key, code_decoder
from methodism import dictfetchone

def permission_checker(funk):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('sign_in')
        if not request.user.is_staff or not request.user.is_superuser:
            return render(request, 'base.html', {'error':404})
        if request.user.user_type !=1 :
            return render(request, 'base.html', {'error':404})
        return funk(request, *args, **kwargs)
    return wrapper

def card_musk(number):
    number = number.replace(" ", "")
    return f"{number[:4]} **** **** {number[-4:]}"

def generate_number():
    return "2631 "+ " ".join(str(random.randint(1000, 9999)) for x in range(3))

def create_uniqe_number():
    number = generate_number()
    with open("base_helper/card_number.txt", 'r') as file:
        if not number in file.read().split('\n'):
            with open("base_helper/card_number.txt", 'a') as write:
                write.write(f'{number}\n')
            return number
    return create_uniqe_number()

def generate_token(pk):
    key = generate_key(10)+code_decoder(code=pk)+generate_key(10)
    with open('base_helper/token.txt', 'r') as file:
        if not key in file.read().split('\n'):
            with open('base_helper/token.txt', 'a') as write:
                write.write(f'{key}\n')
            return key
    return generate_token()


def counter():
    sql = '''
    SELECT 
    (SELECT COUNT(*) from core_car) as car,
    (SELECT COUNT(*) from core_arenda)  as arend,
    (SELECT COUNT(*) from core_user us WHERE us.user_type==1) as admin,
    (SELECT COUNT(*) from core_user us WHERE us.user_type==2) as costumer
    FROM core_user 
    limit 1
    '''
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        natija = dictfetchone(cursor)
    return natija


def generate_tr_id():
    key = random.randint(1_000_000, 9_999_999)
    with open('base_helper/tr_id.txt', 'r') as file:
        if not key in file.read().split('\n'):
            with open('base_helper/tr_id.txt', 'a') as write:
                write.write(f'{key}\n')
            return key
    return generate_tr_id()



