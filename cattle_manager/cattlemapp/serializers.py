from cattlemapp.models import Animal,Cattle,Cattle_User,Cattle_Animal,Token
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class AnimalSerializer(ModelSerializer):
    class Meta:
        model=Animal
        fields='__all__'

class TokenSerializer(ModelSerializer):
    class Meta:
        model=Token
        fields='__all__'

class Cattle_userSerializer(ModelSerializer):
    class Meta:
        model=Cattle_User
        fields='__all__'