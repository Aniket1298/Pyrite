from PIL import Image
from django.db import models
from django.contrib.auth.models import User
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    email_id=models.EmailField(null=True)
    image=models.ImageField(default='profile.PNG',upload_to='profile_pics/',null=True)
    avatar=models.ImageField(default='avatar.PNG',upload_to='temp/')
    about_me=models.TextField(null=True)#image=models.ImageField(upload_to='temp')
    def save(self,**kwargs):
        super().save()
        img = Image.open(self.image.path)
        avt=img.copy()
        img=img.resize((300,300),Image.ANTIALIAS)    
        img.save(self.image.path)
        avt=avt.resize((40,40),Image.ANTIALIAS)
        avt.save(self.avatar.path)
    def __str__(self):
        return self.user.username
