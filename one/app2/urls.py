from django.urls import path
from app2 import views

urlpatterns=[
    path('',views.home,name='homepage'),    
    path('login',views.logins,name='loginpage'),
    path('profile',views.profile,name='profilepage'),
    path('navbor',views.navbor,name='navborpage'),
    path('display',views.display,name='displaypage'),
    path('create',views.create,name='createpage'),
    path('register',views.register,name='registerpage'),
    path('logout',views.logouts,name='logoutpage'),
    
]