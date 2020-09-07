from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
first_name=''
last_name=''
about_me=''
class EditProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['first_name','last_name','about_me','image']