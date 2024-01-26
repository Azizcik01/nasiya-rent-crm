from datetime import datetime as dt
from base_helper.helper import permission_checker
from core.models.cars import Arenda
from core.models.monitoring import Monitoring


def main_cp(request):
    result = {}
    key = request.path.replace("/", " ").split()
    if key:
        key = key[0]
    else:
        key = 'nothing'
    sidebar = {
        'admin-profil':'admin_active',
        'brand':'brand_active',
        'ctg':'ctg_active',
        'car':'car_active',
        'user':'user_active',
        'card':'card_active',
        'u-profil':'uprofil_active',
        'u-brend':'ubrend_active',
        'u-cars':'ucars_active',
        'u-contact':'ucontact_active',
        'monitoring':'monitoring_active',
        'arend':'arend_active',
    }.get(key, "nothing")

    result.update({sidebar:'active'})
    
    return result

@permission_checker
def notification(request):
    all_arend = Arenda.objects.all()
    arend3 = Arenda.objects.filter('-id').filter(status=False)[:2]
    coin_change = Monitoring.objects.filter('-id')[:5]
    ctx = {
        'all_arend':all_arend,
        'arend3':arend3,
        'coin':coin_change,
    }
    return ctx


# def arend_kun(request):
#     if not request.user.is_anonymous:
#         root = Arenda.objects.filter(status=True, car_status=False, user=request.user)
#         for x in root:
#             if x.date_to<dt.today().day():
#                 x.car.status = True
#                 x.save()
        



