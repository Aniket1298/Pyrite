from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import *
from users.models import *
from .forms import *
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('/login')
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,initial={'username':"AADSDS"})
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            #user.backend = 'django.contrib.auth.backends.ModelBackend'
            #login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
class post():
    def __init__(self,author,title,content,avatar,posted_on):
        self.author=author
        self.title=title
        self.content=content
        self.avatar=avatar
        self.posted_on=posted_on
class post():
    def __init__(self,author,title,content,avatar,posted_on,url):
        self.author=author
        self.url=url
        self.title=title
        self.content=content
        self.avatar=avatar
        self.posted_on=posted_on
@login_required
def profile(request,id=0):
    if id==0:
        id=request.user.id
    d={}
    profile=Profile.objects.all()
    url=''
    avtar=''
    for i in profile:
        if i.user.id==id:
            avtar=i.avatar
        d.update({i.user.id:[i.user.username,i.avatar]})
    b=Post.objects.all()
    l=[]
    for i in b:
        if i.author==id:
            url='/user/profile'+str(i.author)+"/"
            t=post("      "+d[i.author][0],i.title,i.content,d[i.author][1],i.posted_on,url)
            l.append(t)
    l=l[::-1]
    p=Profile.objects.all()
    profile=''
    user=User.objects.get(pk=id)
    for i in p:
        if i.user.id==id:
            profile=i
            break
    b=Post.objects.all()
    return render(request,'users/profile.html',{'user':user,'profile':profile,'blogs':l,'avatar':avtar})
def addprofile(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES)#instance=Profile(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print (form.errors)
    else:
        form=ProfileForm()
    return render(request,'users/addprofile.html',{'form':form})

@login_required
def edit_profile(request):
    username=request.user.username
    l=Profile.objects.all()
    tid=0
    user=l[0]
    avtar=''
    for i in l:
        if i.user.username==username:
            tid=i.id
            user=i
    first_name=user.first_name
    avtar=user.avatar
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save(commit=False)
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.image=form.cleaned_data['image']
            print ("------+++++++++++------",form.cleaned_data['image'])
            print (request.FILES)
            user.avatar=form.cleaned_data['image']   
            user.about_me=form.cleaned_data['about_me']
            user.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('home')
        else:
            print ("Bihit ")
    else:
        form=EditProfileForm(instance=user)
    return render(request, "users/edit_profile.html",{'form':form,'avatar':avtar})
@login_required
def myprofile(request,id=0):
    if id==0:
        id=request.user.id
    d={}
    profile=Profile.objects.all()
    url=''
    avtar=''
    for i in profile:
        if i.user.id==id:
            avtar=i.avatar
        d.update({i.user.id:[i.user.username,i.avatar]})
    b=Post.objects.all()
    l=[]
    for i in b:
        if i.author==id:
            url='/user/profile'+str(i.author)+"/"
            t=post("      "+d[i.author][0],i.title,i.content,d[i.author][1],i.posted_on,url)
            l.append(t)
    l=l[::-1]
    p=Profile.objects.all()
    profile=''
    user=User.objects.get(pk=id)
    for i in p:
        if i.user.id==id:
            profile=i
            break
    b=Post.objects.all()
    return render(request,'users/myprofile.html',{'user':user,'profile':profile,'blogs':l,'avatar':avtar})