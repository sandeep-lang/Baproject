from lib2to3.pgen2 import token
from django.shortcuts import render
from rest_framework.views import APIView
import datetime

from .models import *
from .serializers import Bookingserializer
from rest_framework.response import Response
import jwt
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

class Mappoinment(APIView):
    def post(self,request):
        t=request.COOKIES.get('jwt')
        if not t:
            raise AuthenticationFailed('Unauthenticated')
        if not t:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            a=jwt.decode(t,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        print('hello')
    
        y =Bookingserializer(data= {
            'username' :a['username'],
            'patientid':a['patientid'],
            'doctorid':a['doctorid'],
            'doctorname':a['doctorname'],
            'department':a['department'],
            'patientname':a['patientname'],
            'email':a['email'],
            'phone' :a['phone'],
            'gender':a['gender'],
            'appoinmentdate':a['appoinmentdate'],
            'appoinmenttime':a['appoinmenttime'],
            'symptoms':a['symptoms']
        })
        y.is_valid(raise_exception=True)
        y.save()
        return Response({"Thank for your appoinment with our Organization"})#success

class papp(APIView):
    def get(self,_,pk=None) :
        a = Slot.objects.filter(patientid=pk)
        #a = Mooking.objects.filter(patientid=pk)
        #d = a.filter(appoinmentdate__gte = datetime.date.today())
        serializer = Bookingserializer(a,many=True) 
        return Response(serializer.data)      
class dapp(APIView):
    def get(self,_,pk=None) :
        a = Slot.objects.filter(doctorid=pk)
        #a = Mooking.objects.filter(patientid=pk)
       # d = a.filter(appoinmentdate__gte = datetime.date.today())
        serializer = Bookingserializer(a,many=True) 
        return Response(serializer.data)  
class Appupdate (APIView):

    def put(self,request,pk = None):
        c = Slot.objects.filter(id= pk).first()
        token = request.data['jwt']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        serializer = Bookingserializer(c, data=payload)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
class Appoinmentdel(APIView):
    def delete(self,request,pk=None):
        t = request.data['jwt']
        load = jwt.decode(t,'secret',algorithms=['HS256'])
        appoinmentid = load['appoinmentid']
        appoindel = Slot.objects.get(id=appoinmentid)
        appoindel.delete()
        return Response({'Appoinment Deleted'})