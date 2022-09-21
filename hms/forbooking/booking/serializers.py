from rest_framework import serializers 
from.models import * 
import datetime
from rest_framework.validators import UniqueTogetherValidator
class Bookingserializer(serializers.ModelSerializer):
   class Meta:
    model =Slot
    #model = Mooking
    fields = ['username','patientid','doctorid','doctorname','department','patientname','email','phone','gender','appoinmentdate','appoinmenttime','symptoms']

   validators = [ 
      UniqueTogetherValidator(
         queryset = Slot.objects.all(),
         fields=['doctorid','appoinmentdate','appoinmenttime']
      )
   ]
   
   def validate(self, data):
      if data['appoinmentdate'] < datetime.date.today():
         raise serializers.ValidationError("you are selecting the past date")
      return data 

   