from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
	path('register/',views.register),
	#path('myblogs/',views.myblogs),
	path('profile<int:id>/',views.profile),
	path('myprofile',views.myprofile),
	path('addprofile/',views.addprofile),
	path('edit_profile/',views.edit_profile),
	path('logout/',views.logout_view),
]