from core.form import ArendForm
from core.models.cars import Car, Arenda
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime as dt

@login_required(login_url='sign_in')
def U_Cars(request, pk=None):
    ctx = {
        'cars' : Car.objects.filter(status=True)
    }
    if pk:
        root = Car.objects.filter(pk=pk).first()
        ctx['root'] = root
    return render(request, 'user/cars_user.html', ctx)


@login_required(login_url='sign_in')
def arend_car(request, pk=None):
    ctx = {}
    car = Car.objects.filter(pk=pk, status=True ).first()
    user = request.user
    if car.status != True:
        ctx['error'] = 'Avtomobil aktiv holatda emas!'
        return redirect('cars-user')
    if not user.g_seria:
        ctx['error'] = 'Sizning guvohnomangiz mavjud emas!'
        return redirect('cars-user')
    form = ArendForm(request.POST or None)
    ctx['conf'] = True
    ctx['form'] = form
    ctx['car'] = car
    ctx['user'] = user
    if form.is_valid():
        kun = request.POST.get('kun')
        arend = Arenda.objects.create(
            user = user,
            car = car,
            pay_type = request.POST.get('pay_type'),
            date_from = dt.today(),
            date_to = dt.today().strftime(f'%Y-%m-{dt.today().day+int(kun)}'),
            summa = car.narx * int(kun),
        )
        arend.save()
        return redirect('cars-user')
    return render(request, "user/cars_user.html", ctx)

