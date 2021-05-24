from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from django.contrib.auth.models import User
from .models import Animal,Cattle,Cattle_User,Cattle_Animal
from cattlemapp.serializers import  UserSerializer,AnimalSerializer,TokenSerializer,Cattle_userSerializer
from rest_framework import viewsets
from datetime import date
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count



class UserCBV(viewsets.ViewSet):
    def create(self,request):
        x=request.data
        user=User.objects.create_user(username=x['username'],email=x['email'],password=x['password'],is_staff=x["is_staff"])
        cattle=Cattle.objects.create()
        cattle_user=Cattle_User.objects.create(user_id=user,cattle_id=cattle,is_admin=user.is_staff)
        return Response({"message":"user created","cattle_id":cattle.id})

class CattleCBV(viewsets.ViewSet):
    def update(self,request,pk=id):
        z=request.data
        x=Cattle.objects.filter(id=pk).update(cattle_name=z['cattle_name'],city=z['city'],place=z['place'],phone_no=z['phone_no'])
        return Response({"message":"successfully added"})

    def partial_update(self,request,pk=id):
        z=request.data
        m=request.user.id
        if Cattle_User.objects.filter(cattle_id_id=cattle_id,user_id_id=m): 
            try:
                cattle_object=Cattle.objects.get(id=pk)
                cattle_object.cattle_name=z.get("cattle_name",cattle_object.cattle_name)
                cattle_object.city=z.get("city",cattle_object.city)
                cattle_object.place=z.get('place',cattle_object.place)
                cattle_object.phone_no=z.get('phone_no',cattle_object.phone_no)
                cattle_object.save()
                return Response({"message":"cattle is successfully updated"})
            except:
                return Response({"message":"Invalid Cattle Id"})
        else:
            return Response({"message":"Invalid user"})
class AnimalCBV(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes=(IsAuthenticated,)
    def create(self,request,cattle_id):
        cattle=Cattle.objects.get(id=cattle_id)
        input_data=request.data
        user=request.user.id
        user_object=User.objects.get(id=user)
        if Cattle_User.objects.filter(cattle_id_id=cattle_id,user_id_id=user):  
            animal1=Animal()
            animal1.cow_profile_pic=input_data['cow_profile_pic']
            animal1.tag_number=input_data['tag_number']
            animal1.name=input_data['name']
            animal1.breed=input_data['breed']
            animal1.gender=input_data['gender']
            animal1.date_of_birth=input_data['date_of_birth']
            animal1.date_of_entry=input_data['date_of_entry']
            animal1.how_cattle_obtained=input_data['how_cattle_obtained']
            if "no_of_children" in input_data:
                animal1.no_of_children=input_data['no_of_children']
            else:
                animal1.no_of_children=None
            if  Cattle_Animal.objects.filter(cattle_id_id=cattle_id,animal_id_id=animal1.tag_number):
                return Response({"message":"Animal already exist"})
            else:
                pass   
            if 'parent_id' in input_data:
                parent=input_data['parent_id']
                if Animal.objects.filter(tag_number=parent):
                    animal1.parent_id_id=parent
                else:
                    return Response({"message":"Invalid parent Id/does not exist"})
            else:
                animal1.parent_id_id=None
            try:
                animal=Animal.objects.get(tag_number=input_data['tag_number'])
                animal.is_alive=True
                animal.name=input_data["name"]
                animal.date_of_entry=input_data['date_of_entry']
                animal.how_cattle_obtained=input_data['how_cattle_obtained']
                animal.save()
            except:
                animal=Animal.objects.create(tag_number=animal1.tag_number,cow_profile_pic=animal1.cow_profile_pic,breed=animal1.breed,name=animal1.name,gender=animal1.gender,date_of_birth=animal1.date_of_birth,date_of_entry=animal1.date_of_entry,how_cattle_obtained=animal1.how_cattle_obtained,parent_id_id=animal1.parent_id_id,no_of_children=animal1.no_of_children) 
            cattle_animal_object=Cattle_Animal.objects.create(cattle_id=cattle,animal_id=animal,added_by_id=user_object,Date=date.today())
            return Response({"message":"Animal added successfully"})
        else:
            return Response({"message":"Invalid User"})
    def partial_update(self,request,cattle_id,pk=id):
        z=request.data
        m=request.user.id
        if Cattle_User.objects.filter(cattle_id_id=cattle_id,user_id_id=m):    
            if  Cattle_Animal.objects.filter(cattle_id_id=cattle_id,animal_id_id=pk):
                try:
                    animal_object=Animal.objects.get(tag_number=pk)
                    animal_object.no_of_children=z.get("no_of_children",animal_object.no_of_children)
                    animal_object.cow_profile_pic=z.get("cow_profile_pic",animal_object.cow_profile_pic)
                    animal_object.is_alive=z.get("is_alive",animal_object.is_alive)
                    animal_object.save()
                    return Response({"message":"successfully updated"})
                except:
                    return Response({"message":"Invalid tag number"})
            else:
                return  Response({"message":"Invalid credentials"})
        else:
            return Response({"message":"Invalid User"})
    def destroy(self,request,pk):
        input_data=request.data
        m=request.user.id
        if Cattle_User.objects.filter(cattle_id_id=cattle_id,user_id_id=m): 
            if  Cattle_Animal.objects.filter(cattle_id_id=cattle_id,animal_id_id=pk):
                animal=Animal.objects.get(tag_number=tag_number)
                animal.is_alive=False
                animal.save()
                Cattle_Animal.objects.delete(cattle_id=cattle_id,animal_id_id=tag_number)
                return Response({"message":"Animal deleted Successfully"})
            else:   
                return Response({"message":"Animal does not exist in that cattle"})
        else:
            return Response({"message":"Invalid User"})
@api_view(['POST'])
def user_login(request):
    m=request.data
    user=User.objects.filter(email=m["email"]).first()
    success=user.check_password(m['password'])
    print(user.id)
    cattle_user=Cattle_User.objects.filter(user_id_id=user.id).first()
    if success:
        x=Token.objects.filter(user_id=user.id).delete()
        token=Token.objects.create(user=user)
        return Response({"token":token.key,"cattle_id":cattle_user.cattle_id_id,"user_id":user.id})
    else:
        return Response({"message":"Invalid credentials"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    m=request.data
    user=User.objects.get(id=m['user_id'])
    token=Token.objects.filter(user_id=user.id).delete()
    return Response({"message":"logout success"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request,cattle_id):
    user_id=request.user.id
    user_is_admin=request.user.is_staff
    m=request.data
    if user_is_admin:
        if Cattle_User.objects.filter(cattle_id_id=cattle_id,user_id_id=user_id):
            cattle=Cattle.objects.get(id=m['cattle_id'])
            user=User.objects.create_user(username=m['user_name'],email=m['email'],password=m['password'],is_staff=m["is_staff"])
            cattle_user=Cattle_User.objects.create(user_id=user,cattle_id=cattle,is_admin=user.is_staff)
            return Response({"message":"user added successfully"})
        else:
            return Response({"message":"you are not admin"})
    else:
        return Response({"message":"You are not admin"})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def show_animals(request,cattle_id):
    m={}
    n={}
    input_data=request.data
    queryset=Cattle_Animal.objects.filter(cattle_id=cattle_id)
    animalid_list=queryset.values_list('animal_id_id',flat=True)
    for i in animalid_list:
        animal=Animal.objects.get(tag_number=i)
        serializers=AnimalSerializer(animal)
        m[i]=serializers.data
    for i in animalid_list:
        m[i]['cow_profile_pic']='http://127.0.0.1:8000'+str(m[i]['cow_profile_pic'])
    n=m
    return Response(n)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def show_animal(request,cattle_id,tag_number):
    m={}
    print(request.user.id)
    input_data=request.data
    if Cattle_Animal.objects.filter(cattle_id_id=cattle_id,animal_id_id=tag_number).exists():
        animal=Animal.objects.get(tag_number=tag_number)
    else:
        return Response({"message":"Invalid Credentials"})
    serializer=AnimalSerializer(animal)
    m=serializer.data
    m['cow_profile_pic']='http://127.0.0.1:8000'+str(m['cow_profile_pic'])
    return Response(m)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_animal(request,cattle_id):
    m={}
    input_data=request.query_params
    if Cattle_Animal.objects.filter(cattle_id_id=cattle_id,animal_id_id=input_data['animal_id']).exists():
        animal=Animal.objects.get(tag_number=input_data['animal_id'])
    else:
        return Response({"message":"Invalid Tag Number"})
    serializer=AnimalSerializer(animal)
    m=serializer.data
    m['cow_profile_pic']='http://127.0.0.1:8000'+str(m['cow_profile_pic'])
    return Response(m)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_animal(request,cattle_id,tag_number):
    input_data=request.data
    animal=Animal.objects.get(tag_number=tag_number)
    animal.is_alive=False
    animal.save()
    try:
        canimal=Cattle_Animal.objects.get(cattle_id=cattle_id,animal_id_id=tag_number)
        canimal.delete()
        return Response({"message":"Animal deleted Successfully"})
    except:
        return Response({"message":"Animal does not exist in that cattle"})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cattle_details(request,cattle_id):
    m=[]
    gender_count = Animal.objects.filter(cattle_animal__cattle_id=cattle_id).values('gender').annotate(Count('gender'))
    print(gender_count)
    for i in gender_count:
        z={}        
        z['gender']=i["gender"]
        z["count"]=i["gender__count"]
        m.append(z)    
    return Response({"message":"details sent","data":m})