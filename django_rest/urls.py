from .api_views import *
from .views import *
from rest_framework import routers
from knox import views as knox_views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"todos", TodosView, "todos")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/registration/", RegisterAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
]
