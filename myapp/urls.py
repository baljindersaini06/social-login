from django.urls import path
from . import views

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('dashboard', views.index, name='dashboard'),
    path('',views.login_user,name='login'),
    path('success',views.success,name='success'),

]