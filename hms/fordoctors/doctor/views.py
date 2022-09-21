from email import message
from json import load
from urllib import response
from rest_framework.views import APIView

#from forbooking.booking.models import Slot
from .serializers import *
from . models import*
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = Doctors.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("user not found") 
        
        if str(password)!= user.password:
            raise AuthenticationFailed("Please enter valid password")
        
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

class Dprofile(APIView):
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

        t =request.get('http://127.0.0.1:8002/api/dapp/%d'% l)
