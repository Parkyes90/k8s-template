from django.urls import include
from django.urls import path

urlpatterns = [
    path("users/", include("apis.v1.users.urls")),
]
