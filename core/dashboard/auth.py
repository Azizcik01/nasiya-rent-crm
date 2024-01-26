import random
from datetime import datetime as dt
from django.shortcuts import render, redirect
from core.models.auth import User
from django.contrib.auth import login, logout
from core.models.monitoring import Card
from django.contrib.auth.decorators import login_required
from core.form import UserForm
from base_helper.helper import permission_checker, card_musk, create_uniqe_number, generate_token

def sign_in(request):
    if request.POST:
        tel = request.POST.get('tel')
        pas = request.POST.get('pas')
        user = User.objects.filter(phone=tel).first()
        if not user:
            return render(request, 'auth/login.html', {'error':'Telefon raqam yoki parol xato!'})
        if not user.check_password(pas):
            return render(request, 'auth/login.html', {'error':'Telefon raqam yoki parol xato!'})
        if not user.is_active:
            return render(request, 'auth/login.html', {'error':'Bu foydalanuvchi qora ro\'yhatda!'})
        login(request, user)
        return redirect('home')
    return render(request, 'auth/login.html')


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect('sign_in')


@permission_checker
def Reg_user(request, pk=None, status=None):
    ctx = {
            'roots':User.objects.all()
        }
    if status == 'form':
        root = User.objects.filter(pk=pk).first()
        form = UserForm(instance=root or None)
        if request.POST:
            if not root:
                data = {
                "fio":request.POST.get('fio'),
                "username":request.POST.get('username'),
                "ps_seria":request.POST.get('ps_seria'),
                "phone":request.POST.get('phone'),
                "g_seria":request.POST.get('g_seria'),
                "g_yil_from":request.POST.get('g_yil_from'),
                "g_yil_to":request.POST.get('g_yil_to'),
                "g_ctg":request.POST.get('g_ctg'),
                "user_type":request.POST.get('user_type'),
                "password":request.POST.get('password')
                }
                user = User.objects.create_user(**data)
                user.save()
                card_raqam = create_uniqe_number()
                card_m = card_musk(number=card_raqam)
                card = Card.objects.create(
                    owner = user,
                    name = user.fio,
                    raqam = card_raqam,
                    mask = card_m,
                    expire = f'{str(dt.today().date()).replace("-", " ").split()[1]}/{str(dt.today().date().year+1)[2:]}',
                    token = generate_token(pk=user.id),
                    balance = 100
                )
                card.save()
            else:
                root.fio = request.POST.get('fio')
                root.username = request.POST.get('username')
                root.ps_seria = request.POST.get('ps_seria')
                root.phone = request.POST.get('phone')
                root.g_seria = request.POST.get('g_seria')
                root.g_yil_from = request.POST.get('g_yil_from')
                root.g_yil_to = request.POST.get('g_yil_to')
                root.g_ctg = request.POST.get('g_ctg')
                root.user_type = request.POST.get('user_type')
                root.save()
            return redirect('users')
        ctx['root'] = root
        ctx['form'] = form
        ctx['status'] = 'form'
    if status == 'del':
        root = User.objects.filter(pk=pk).first()
        try:
            root.delete()
        except:
            pass
    return render(request, 'adminpages/users.html', ctx)


@permission_checker
def change_password(request, id):
    if request.user.is_anonymous:
        return redirect('sign_in')
    user = User.objects.filter(id=id).first()
    if user:
        if request.POST:
            new = request.POST.get('pas')
            user.set_password(str(new))
            user.save()
        return redirect('users')


@permission_checker
def user_ban(request, status, pk):
    user = User.objects.filter(pk=pk).first()
    if request.user != user:
        if status == 'ban':
            user.is_active = False
            user.save()
        elif status == 'antiban':
            user.is_active = True
            user.save()
        return redirect('users')
    else:
        return redirect('users')










