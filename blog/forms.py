from django.forms import ModelForm
from  .models import *
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
from django import forms
class temp(forms.Form):
     title=forms.CharField(max_length=100)
     content=forms.CharField(max_length=1000)
