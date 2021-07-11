from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


from . import views
urlpatterns = [
    path("adminuser/",views.adminuser,name="adminuser"),
    path("send/", views.send, name="send"),
    path("back/", views.back, name="back"),
    path("register/",views.home,name="home"),
    path("regUser/", views.regUser, name="regUser"),
    path("",views.main, name="main"),
    path("myadmin/", views.myadmin, name="myadmin"),
    path("user/", views.user, name="user"),
    path("stock/", views.stockrdt, name="stockrdt"),
    path("stockinfo/", views.stockinfo, name="stockinfo"),
    path("supplier/", views.supp, name="supp"),
    path("supplierinfo/", views.supplierinfo, name="supplierinfo"),
    path('appointment/', views.app, name="app"),
    path('delapp/', views.delapp, name="delapp"),
    path('deleteapp/',views.deleteapp, name="deleteapp"),
    path("bookappointment/", views.bookappointment, name="bookappointment"),
    path('updapp/', views.updapp, name="updapp"),
    path('updateapp/', views.updateapp, name="updateapp"),
    path('form/', views.adminhome, name="adminhome"),
    path('front/', views.forgot),
    path('submit/', views.adminuser),
    path('viewappointments/', views.viewappointments, name='viewappointments'),
    path('viewstock/',views.viewstock, name='viewstock')
]