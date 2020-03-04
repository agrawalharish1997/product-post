from django import forms
from user1.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')