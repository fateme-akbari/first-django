from django.urls import path, include
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path("signin", signin_view, name="signin"),
    path("signout", signout_view, name="signout"),
    path("signup", signup_view, name="signup")
]
