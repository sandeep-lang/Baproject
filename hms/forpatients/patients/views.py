from json import load
from urllib import response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
import requests
from .models import User

# Create your views here.
class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response(serializer.data)
        return Response("Accounted Create Succesfully")
class Login(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first() 

        if user is None:
            raise AuthenticationFailed("No User Found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password") 

        load = {
            'id':  user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        t = jwt.encode(load,'secret',algorithm='HS256')
        response = Response() 
        response.set_cookie(key='jwt',value=t,httponly=True)
        response.data = {
            'jwt':t
        }
        return response
class Pprofile(APIView):
    def get(self,request):
        t=request.COOKIES.get('jwt')

        if not t:
            raise AuthenticationFailed('Unauthenticated')
        try:
            load = jwt.decode(t,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthneticated')
        #user = User.objects.filter(id=load['id']).first() 
        #serializer = UserSerializer(user)
        #return Response(serializer.data)
        l=load['id']

        t =requests.get('http://127.0.0.1:8002/api/papp/%d'%l)#imp
        return Response(t.json())
class Profile(APIView):
    def get(self,request):
        t=request.COOKIES.get('jwt')

        if not t:
            raise AuthenticationFailed('Unauthenticated')
        try:
            load = jwt.decode(t,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthneticated')
        user = User.objects.filter(id=load['id']).first() 
        serializer = UserSerializer(user)
        return Response(serializer.data)
        #l=load['id']

        #a =request.get('http://127.0.0.1:8002/api/pview/%d'% l)
        #return Response(a.json())


class Logout(APIView):
    def post(self,request):
        response = Response() 
        response.delete_cookie('jwt') 
        response.data = {
            'message' : 'success'
        }
        return response

class Appoinmentview(APIView):
    def post(self,request):
        t=request.COOKIES.get('jwt')
        if not t:
            raise AuthenticationFailed('Unauthenticated') 
        try:
            load =jwt.decode(t,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        s=load['id']
        a={
            'username':request.data['username'],
            'patientid':s,
            'doctorid':request.data['doctorid'],
            'doctorname':request.data['doctorname'],
            'department': request.data['department'],
            'patientname':request.data['patientname'],
            'email':request.data['email'],
            'phone':request.data['phone'],
            'gender':request.data['gender'],
            'appoinmentdate':request.data['appoinmentdate'],
            'appoinmenttime':request.data['appoinmenttime'],
            'symptoms':request.data['symptoms']
        }
        t=jwt.encode(a,'secret',algorithm='HS256')
        data = {
            'jwt':t 
        }
        response = requests.post("http://127.0.0.1:8002/api/mapp",cookies=data)
        return Response(response)
class Bookupdate(APIView):
    def put(self, request):
        t = request.COOKIES.get('jwt')
        if not t:
            raise AuthenticationFailed('Unauthenticated')
        try:
            load = jwt.decode(t, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unathenticated')
        id = load['id']
        load = {
            'username':request.data['username'],
            'patientid':id,
            'doctorid':request.data['doctorid'],
            'doctorname':request.data['doctorname'],
            'department': request.data['department'],
            'patientname':request.data['patientname'],
            'email':request.data['email'],
            'phone':request.data['phone'],
            'gender':request.data['gender'],
            'appoinmentdate':request.data['appoinmentdate'],
            'appoinmenttime':request.data['appoinmenttime'],
            'symptoms':request.data['symptoms']
        }
        t = jwt.encode(load, 'secret', algorithm='HS256') 
        response = Response()
        response.data = {'jwt' : t}
        cookie = {
            'jwt' : t
        }
        new = request.data['id']
        appointment = requests.put('http://127.0.0.1:8002/api/update/%d'%new, data=cookie)
        return Response(appointment.json())
class Deleteapp(APIView):
    def delete(self,request):
        t = request.COOKIES.get('jwt')
        if not t:
            raise  AuthenticationFailed("login with correct details")
        try:
            load = jwt.decode(t,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('login again')
        id = load['id']
        load = {
            'appoinmentid': request.data['appoinmentid'],
            'userid':id,
        }
        t = jwt.encode(load,'secret',algorithm='HS256')
        response = Response()
        response.data = {
            'jwt':t 
        }
        cookie = {'jwt':t}
        b = requests.delete('http://127.0.0.1:8002/api/delete',data=cookie)
        return Response(b)