from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
       path('',views.home,name='home'),
       path('login',views.login,name='login'),
       path('sign',views.sign,name='sign'),
       path('homes',views.homes,name='homes'),
       path('con',views.con,name='con'),
       path('more',views.more,name='more'),
       path('log',views.log,name='log'),
]