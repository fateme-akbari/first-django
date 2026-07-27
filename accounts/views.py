from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm

def signin_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                email = form.cleaned_data.get("email")
                user = authenticate(username=username, password=password, email=email)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "sign-in successfully")
                    return redirect("website:index")
        return render(request, "accounts/sign-in.html")
    else:
        return redirect("website:index")


@login_required
def signout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(request.META.get("HTTP_REFERER", "/"))
    

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "sign-up successfully")
                return redirect("accounts:signin")
        return render(request, "accounts/signup.html")
    else:
        return redirect("website:index")
