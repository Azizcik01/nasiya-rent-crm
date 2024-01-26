from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from base_helper.helper import permission_checker, counter, generate_tr_id
from core.models.cars import Arenda, Category, Brand
from core.models.monitoring import Card, Monitoring
from core.models.auth import User
from core.form import CtgForm, BrandForm


@login_required(login_url='sign_in')
def home(request):
    if request.user.user_type == 2:
        return redirect('u_index')
    return render(request, 'adminpages/index.html', {'count':counter()})

@permission_checker
def ctg_brend(request, key=None, pk=None):
    ctx = {
        'roots':Category.objects.all(),
        'brands':Brand.objects.all()
    }
    if request.POST:
        if key==1:
            root = Category.objects.filter(pk=pk).first()
            form = CtgForm(request.POST or None, instance=root or None)
            if form:
                if form.is_valid():
                    form.save()
                    return redirect('ctgs')
            ctx["form"] = form
        if key==2:
            root = Brand.objects.filter(pk=pk).first()
            form = BrandForm(request.POST or None, instance=root or None)
            if form:
                if form.is_valid():
                    form.save()
                    return redirect('brands')
            ctx["form"] = form
    return render(request, 'adminpages/ctg_brand.html', ctx)

@permission_checker
def del_cb(request, key, pk):
    if request:
        if key == 1:
            Category.objects.get(pk=pk).delete()
            return redirect('ctgs')
        if key == 2:
            Brand.objects.get(pk=pk).delete()
            return redirect('brands')


@permission_checker
def user_card(request, pk=None):
    ctx = {
        'roots':Card.objects.all()
    }
    if pk:
        root = Card.objects.filter(pk=pk).first()
        ctx['root'] = root
    if request.POST:
        root = Card.objects.filter(pk=pk).first()
        balans = request.POST.get('balans')
        if type(balans) != int:
                ctx['error'] = 'Sonlardan iborat summa kiriting!'
        root.balance = root.balance + int(balans)
        root.save()
        return redirect('cards')
    return render(request, 'adminpages/card.html', ctx)


@permission_checker
def admin_profil(request, status=None):
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
                    return redirect('a_profil')
            else:
                ctx['error'] = 'Bunday karta egasi mavjud emas!'
            
    ctx['status'] = status
    return render(request, 'adminpages/profil.html', ctx)


def monitoring(request):
    ctx = {
        'roots':Monitoring.objects.all().order_by('-pk')
    }
    return render(request, 'adminpages/monitoring.html', ctx)

@permission_checker
def notification(request):
    all_arend = Arenda.objects.all()
    arend3 = Arenda.objects.filter('-id')[:2]
    coin_change = Monitoring.objects.filter('-id')[:2]
    ctx = {
        'all_arend':all_arend,
        'arend3':arend3,
        'coin':coin_change
    }
    return render(request, 'base.html', ctx)

