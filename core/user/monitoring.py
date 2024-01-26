from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from base_helper.helper import generate_tr_id
from core.models.auth import User
from core.models.cars import Brand, Category, Car, Arenda
from core.models.monitoring import Card, Monitoring



@login_required(login_url='sign_in')
def brend_user(request, conf=None, pk=None, carpk=None):
    ctx = {}
    if conf == '1':
        cars = Car.objects.filter(brand_id=pk)
        ctx['cars'] = cars
        ctx['conf'] = True
    elif conf == '2':
        cars = Car.objects.filter(ctg_id=pk)
        ctx['cars'] = cars
        ctx['conf'] = True
    else: 
        ctx.update({'brands':Brand.objects.all()})              #[1]
        ctx.update({'ctgs':Category.objects.all()})             #[2]
    return render(request, 'user/brend_user.html', ctx)


@login_required(login_url='sign_in')
def u_index(request, status=None):
    root = User.objects.filter(id = request.user.id).first()
    card = Card.objects.filter(owner_id = root.id).first()
    ctx = {
        'root' : root,
        'card' : card
    }
    if status:
        if request.method == 'POST':
            own = Card.objects.filter(owner_id=request.user.id).first()
            karta = request.POST.get("karta_raqam")
            shaxs = Card.objects.filter(raqam=karta).first()
            ctx['karta'] = shaxs
            if shaxs and request.POST.get('summa'):
                if own.balance < int(request.POST.get('summa')):
                    ctx['error'] = 'Kartada yetarli pul yoq'
                else:
                    own.balance = own.balance - int(request.POST.get('summa'))
                    shaxs.balance = shaxs.balance + int(request.POST.get('summa'))
                    own.save()
                    shaxs.save()
                    data = Monitoring.objects.create(
                        tr_id = generate_tr_id(),
                        sender = own,
                        reciever = shaxs,
                        amount = request.POST.get('summa'),
                        status = 2
                    )
                    data.save()
                    ctx['succes'] = "Muvaffaqqiyatli o'tkazildi! "
                    return redirect('u_index')
            else:
                ctx['error'] = 'Bunday karta egasi mavjud emas!'
            
    ctx['status'] = status
    return render(request, 'user/profil_user.html', ctx)


@login_required(login_url='sign_in')
def admin_contact(request):
    buyurtma = Arenda.objects.filter(user = request.user)
    ctx = {
        'roots' : buyurtma
    }
    return render(request, 'user/contact.html', ctx)
