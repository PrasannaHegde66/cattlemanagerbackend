from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Cattle(models.Model):
    id=models.AutoField(primary_key=True)
    cattle_name=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=50,null=True)
    place=models.CharField(max_length=100,null=True)
    phone_no=models.CharField(max_length=20,null=True)

class Animal(models.Model):
    tag_number=models.CharField(primary_key=True,max_length=20)
    parent_id=models.ForeignKey("self",on_delete=models.CASCADE,null=True)
    cow_profile_pic=models.ImageField(upload_to='uploads/',null=True)
    name=models.CharField(max_length=50,null=True)
    breed=models.CharField(max_length=60,null=True)
    gender=models.CharField(max_length=10,null=True)
    date_of_birth=models.DateField(null=True)
    date_of_entry=models.DateField(null=True)
    no_of_children=models.PositiveIntegerField(null=True)
    how_cattle_obtained=models.CharField(max_length=50,null=True)
    is_alive=models.BooleanField(default=True)

class Cattle_User(models.Model):
    cattle_id=models.ForeignKey(Cattle,max_length=50,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    is_admin=models.BooleanField(default=False)
    

class Cattle_Animal(models.Model):
    cattle_id=models.ForeignKey(Cattle,on_delete=models.CASCADE)
    animal_id=models.ForeignKey(Animal,on_delete=models.CASCADE)
    added_by_id=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    Date=models.DateField(null=True)
    
        





