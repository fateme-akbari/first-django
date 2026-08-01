from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def signin_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
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
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "sign-up successfully")
                return redirect("accounts:signin")
        return render(request, "accounts/signup.html")
    else:
        return redirect("website:index")

def forget_password(request):
    if request.user.is_authenticated:
        return redirect("website:index")

    email_form = EmailLookupForm()
    password_form = SetNewPasswordForm()
    step = 1

    if request.method == "POST":
        reset_email = request.session.get("reset_email")
        submitted_step = request.POST.get("step")

        if submitted_step == "1":
            email_form = EmailLookupForm(data=request.POST)
            if email_form.is_valid():
                request.session["reset_email"] = email_form.cleaned_data["email"]
                step = 2
            else:
                step = 1

        elif submitted_step == "2":
            password_form = SetNewPasswordForm(data=request.POST)
            if password_form.is_valid():
                password_form.save(reset_email)
                del request.session["reset_email"]
                return redirect("accounts:signin")

    return render(
        request,
        "accounts/password-reset-page.html",
        {
            "step": step,
            "password_form": password_form,
            "email_form": email_form
        }
    )