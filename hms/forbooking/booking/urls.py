from django.urls import path 
from .views import *

urlpatterns = [
    path('mapp',Mappoinment.as_view()),#mapp-->MAKEAPPOINMENT
    path('papp/<int:pk>',papp.as_view()),
     path('dapp/<int:pk>',dapp.as_view()),
     path('update/<int:pk>',Appupdate.as_view()),
     path('delete',Appoinmentdel.as_view())


]