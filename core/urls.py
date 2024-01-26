from django.urls import path
from core.dashboard.auth import sign_in, sign_out, Reg_user, change_password, user_ban
from core.dashboard.monitoing import home, ctg_brend, del_cb, notification, user_card, admin_profil, monitoring
from core.dashboard.cars import Cars, arends, chek_arend
from core.user.monitoring import admin_contact, brend_user, u_index
from core.user.cars import U_Cars, arend_car

urlpatterns = [
    #                   auth
    path('sign-in/', sign_in, name='sign_in'),
    path('sign-out/', sign_out, name='sign_out'),
    #                   monitoring
    path('', home, name='home'),
##############################[  ADMIN  ]####################################
    #                   profil
    path('admin-profil/', admin_profil, name='a_profil'),
    path('admin-profil/<status>/', admin_profil, name='change_coin'),
    #                   brand
    path('brand/', ctg_brend, name='brands'),
    path('brand/add/<int:key>/', ctg_brend, name='add-brand'),
    path('brand/edit/<int:key>/<int:pk>/', ctg_brend, name='edit-brand'),
    path('brand/delete/<int:key>/<int:pk>/', del_cb, name='del-brand'),
    #                   ctg
    path('ctg/', ctg_brend, name='ctgs'),
    path('ctg/add/<int:key>/', ctg_brend, name='add-ctg'),
    path('ctg/edit/<int:key>/<int:pk>/', ctg_brend, name='edit-ctg'),
    path('ctg/delete/<int:key>/<int:pk>/', del_cb, name='del-ctg'),
    #                   car
    path('car/', Cars, name='cars'),
    path('car/add/<status>/', Cars, name='add-car'),
    path('car/edit/<status>/<int:pk>/', Cars, name='edit-car'),
    path('car/delete/<int:pk>/', Cars, name='del-car'),
    #                   reg_user
    path('user/', Reg_user, name='users'),
    path('user/add/<status>/', Reg_user, name='add-user'),
    path('user/edit/<status>/<int:pk>/', Reg_user, name='edit-user'),
    path('user/delete/<status>/<int:pk>/', Reg_user, name='del-user'),
    path('user/chp/<int:id>/', change_password, name='chp'),
    path('user/ban/<status>/<int:pk>/', user_ban, name='user_ban'),
    #                   card
    path('card/', user_card, name='cards'),
    path('card/info/<int:pk>/', user_card, name='info_cards'),
    path('card/plus/<int:pk>/', user_card, name='plus_cards'),
    #                   monitoring
    path('monitoring/info/', monitoring, name='monitoring'),
    #                   arendalar
    path('arend/', arends, name='arends'),
    path('arend/chek/<status>/<int:pk>/', chek_arend, name='chek_arend'),
    path('notification/admin/', notification, name='notification'),
    
##############################[  USER  ]#######################################
    #                   user_profil
    path('u-profil/', u_index, name='u_index'),
    path('u-profil/coin/<status>/', u_index, name='u_change_coin'),
    #                   user_brend
    path('u-brend/', brend_user, name='brend-user'),
    path('u-brend/<conf>/<int:pk>/', brend_user, name='ubrend-car'),
    path('u-brend/<conf>/<int:pk>/', brend_user, name='uctg-car'),
    #                   arenda
    path('u-cars/arend/<int:pk>/', arend_car, name='arend_car'),
    #                   user_car
    path('u-cars/', U_Cars, name='cars-user'),
    path('u-cars/<int:pk>/', U_Cars, name='car-info-user'),
    #                   contact_admin
    path('u-contact/', admin_contact, name='contact_admin'),


]
