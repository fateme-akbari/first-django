from django import forms
from website.models import *

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = "__all__"