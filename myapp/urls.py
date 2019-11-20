from django.urls import path
from . import views

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('dashboard', views.index, name='dashboard'),
    path('',views.login_user,name='login'),
    path('success',views.success,name='success'),
    path('profile', views.profile, name='profile'),
    path('page_calender', views.calender, name='page_calender'),
    path('profile_account', views.profile_account, name='profile_account'),
    # path('siteupdate',views.siteupdate,name='siteupdate'),

    #path('editprofile',views.update_profile,name='editprofile'),
    #path('change_password', views.change_password, name='change_password'),
    #path('userclient',views.user_update, name='userclient'),
    path('test',views.test, name='test'),

]