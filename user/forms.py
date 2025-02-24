from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class CustuserRegistrationForm(UserCreationForm):
    class Meta:
        model=Custuser
        fields=['username','email','role','password1','password2']


class CustuserLoginForm(AuthenticationForm):
    pass
    

class PackagesForm(forms.ModelForm):
    expiry=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    class Meta:
        model=Packages
        fields=['title','destination','price','duration','image','description','expiry']
    


