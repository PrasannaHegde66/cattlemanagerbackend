from . import views
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.views import obtain_auth_token 
from django.urls import include, path,re_path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from rest_framework import routers

router=routers.DefaultRouter()
router.register('user',views.UserCBV,basename='users')
router.register(r'^cattle/(?P<cattle_id>\d+)/animal',views.AnimalCBV,basename='animal')
router.register('cattle',views.CattleCBV,basename='cattle')

urlpatterns = [
    path(r'',include(router.urls)),
    path("user-login/",views.user_login,name='userlogins'),
    path("user-logout/",views.user_logout,name='userlogouts'),
    re_path(r'^cattle/(?P<cattle_id>\d+)/admin/adduser/',views.add_user,name='addusers'),
    re_path(r'^cattle/(?P<cattle_id>\d+)/showanimals/$',views.show_animals,name="showanimals"),
    re_path(r'^cattle/(?P<cattle_id>\d+)/showanimal/(?P<tag_number>\d+)/$',views.show_animal,name="showanimal"),
    re_path(r'^cattle/(?P<cattle_id>\d+)/searchanimal/$',views.search_animal,name="search-animal"),
    re_path(r'^cattle/(?P<cattle_id>\d+)/deleteanimal/(?P<tag_number>\d+)/$',views.delete_animal,name="delete-animal"),
    re_path(r'^cattle/(?P<cattle_id>\d+)/cattledetails/$',views.cattle_details,name="cattledetails"),
]