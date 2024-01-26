from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.form import CarForm
from core.models.cars import Car, Arenda
from core.form import CarForm
from base_helper.helper import permission_checker
from core.models.monitoring import Card


@permission_checker
def Cars(request, status=None, pk=None):
    ctx = {
        'cars':Car.objects.all()
    }
    if status == 'form':
        root = Car.objects.filter(pk=pk).first()
        form = CarForm(request.POST or None, instance=root or None)
        if form.is_valid():
            form.save()
            return redirect('cars')
        ctx['form']=form
        ctx['status']='form'
    return render(request, 'adminpages/cars.html', ctx)

@permission_checker
def arends(request):
    buyurtma = Arenda.objects.all()
    ctx = {
        'roots' : buyurtma
    }
    return render(request, 'adminpages/arend.html', ctx)

@permission_checker
def chek_arend(request, status, pk):
    ctx = {}
    root = Arenda.objects.filter(id=pk).first()
    card = Card.objects.filter(owner=root.user).first()
    admin_card = Card.objects.filter(raqam = '2631 1111 2222 3333').first()
    if status == 'on':
        if int(root.summa) <= card.balance:
            card.balance -= int(root.summa)
            admin_card.balance += int(root.summa)
            admin_card.save()
            card.save()
            root.status = True
            root.car.status = False
            root.car.save()
            root.save()
        else:
            ctx['error'] = 'Balansda pul yetarli emas!'
        buyurtma = Arenda.objects.all()
        ctx['roots'] = buyurtma
        return render(request, 'adminpages/arend.html', ctx)
    elif status == 'off':
        if int(root.summa) <= admin_card.balance:
            admin_card.balance -= int(root.summa)
            card.balance += int(root.summa)
            admin_card.save()
            card.save()
            root.status = False
            root.car.status = True
            root.car.save()
            root.save()
        else:
            ctx['error'] = 'Balansda pul yetarli emas!'
    buyurtma = Arenda.objects.all()
    ctx['roots'] = buyurtma
    return render(request, 'adminpages/arend.html', ctx)

