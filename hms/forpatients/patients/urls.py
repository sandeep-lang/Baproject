
from django.urls import path
from .views import *

urlpatterns = [
    path('register',Register.as_view()),
    path('login',Login.as_view()),
    path('profile',Profile.as_view()),
    path('pprofile',Pprofile.as_view()),
    path('logout',Logout.as_view()),
    path('papp',Appoinmentview.as_view()),#appoinmentview --> URL
    path('update',Bookupdate.as_view()),
     path('delete',Deleteapp.as_view())
]