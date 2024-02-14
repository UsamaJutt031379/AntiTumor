from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup , name='signup'),
    path('index', views.index , name='index'),
    path('home', views.home , name='home'),
    path('bt', views.bt , name='bt'),
    path('mt', views.mt , name='mt'),
    path('stat', views.stat , name='stat'),
    path('publish' , views.publish , name='publish'),

    path('live_well', views.live_well, name = 'live_well' ),
    path('five_steps', views.five_steps, name = 'five_steps' ),
    path('eat_well', views.eat_well, name = 'eat_well' ),
    path('add_support', views.add_support, name = 'add_support'),
    path('calculator', views.calculator, name='calculator'),

    path('contact', views.contact, name = 'contact'),
    
    path('login_form', views.login_form , name='login_form'),
    path('logout_form', views.logout_form, name='logout_form'),

]
