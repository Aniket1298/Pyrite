from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created")
            username=form.cleaned_data.get('username')
            return redirect('blog-home')  
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})
class post():
    def __init__(self,author,title,content,avatar,posted_on,url):
        self.author=author
        self.url=url
        self.title=title
        self.content=content
        self.avatar=avatar
        self.posted_on=posted_on
def home(request):
    d={}
    profile=Profile.objects.all()
    url=''
    for i in profile:
        d.update({i.user.id:[i.user.username,i.avatar]})
    b=Post.objects.all()
    l=[]
    for i in b:
        
        url='/user/profile'+str(i.author)+"/"
        t=post("      "+d[i.author][0],i.title,i.content,d[i.author][1],i.posted_on,url)
        l.append(t)
    l=l[::-1]
    avtar=''
    return render(request,'blog/home.html',{'blogs':l,'avatar':avtar})
def addblog(request):
    avtar=''
    id=request.user.id
    p=Profile.objects.all()
    for i in p:
        if i.user.id==id:
            avtar=i.avatar
            break
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            blog=Post(title=form.cleaned_data.get('title'),content=form.cleaned_data.get('content'),posted_on=timezone.now(),author=request.user.id)
            blog.save()
            return redirect('home')  
    else:
        form=PostForm()
    return render(request,'blog/addblog.html',{'form':form,'avatar':avtar})