from django.conf.urls import url
from django.urls import path
from .views import ObtainTokenView,ProfilesApi
#Add Our API URLS
urlpatterns = [
    path('login-api/', ObtainTokenView.as_view(),name="Login"),
    path('profiles/', ProfilesApi.as_view(),name="User Profiles"),

]
