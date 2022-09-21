from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.exceptions import ValidationError

"""
# Create your models here.
class Appoinment(AbstractUser):
    username = models.CharField(max_length=200)
    patientid = models.IntegerField()
    doctorid = models.IntegerField()
    doctorname = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    patientname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    appoinmentdate = models.DateField()
    appoinmenttime = models.CharField(max_length=200)
    symptoms = models.CharField(max_length=200)
    
    REQUIRED_FIELDS= []
    USERNAME_FIELD= 'id' #id

    def save(self,*args,**kwargs):
        if self.appoinmentdate < datetime.date.today():
            raise ValidationError("The Date Cannot be past")
            #super(Appoinment,self).save(*args,**kwargs)

    def validate(self, data):
      if data['appoinmentdate'] < datetime.date.today():
         raise serializers.ValidationError("you are selecting the past date")
      return data"""
 
class Slot(models.Model):
    username = models.CharField(max_length=200)
    patientid = models.IntegerField()
    doctorid = models.IntegerField()
    doctorname = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    patientname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    appoinmentdate = models.DateField()
    appoinmenttime = models.TimeField()
    symptoms = models.CharField(max_length=200)

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []