from .api_views import *
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path("registration/", RegisterAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
]
