from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class CustuserRegistrationForm(UserCreationForm):
    class Meta:
        model=Custuser
        fields=['username','email','password1','password2']


class CustuserLoginForm(AuthenticationForm):
    pass
    

class PackagesForm(forms.ModelForm):
    expiry=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    class Meta:
        model=Packages
        fields=['title','destination','price','duration','image','description','expiry']
    

class VendorRegistrationForm(UserCreationForm):
    company_name=forms.CharField(max_length=100,required=True,label="Company Name")
    contact_no=forms.CharField(max_length=50,required=True,label="Contact Number")
    address=forms.CharField(widget=forms.Textarea,required=True,label="Address")

    class Meta:
        model=Custuser
        fields=['username','email','password1','password2']

    def save(self,commit=True):
        user=super().save(commit=False)
        user.role='vendor'
        if commit:
            user.save()
            Vendor.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                contact_no=self.cleaned_data['contact_no'],
                address=self.cleaned_data['address'],
            )
            return user