from django.contrib import admin
from cattlemapp.models import Animal,Cattle_Animal,Cattle_User,User,Cattle
# Register your models here.
admin.site.register(Animal)
admin.site.register(Cattle_Animal)
admin.site.register(Cattle)
admin.site.register(Cattle_User)

