from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        
        return email
    
class EmailLookupForm(forms.Form):
    email = forms.EmailField(required=True)
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account was found with this email address.")
        
        return email
    
    
class SetNewPasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
   
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            password_validation.validate_password(password1)
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            self.add_error("password2", "The two password fields didn't match.")
        return cleaned_data
    
    def save(self, email):
        password = self.cleaned_data["password1"]
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return user