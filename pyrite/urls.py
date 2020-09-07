from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',blog_views.index,name='index'),#auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('register/',user_views.register,name='register'),
    path('user/',include('users.urls')),
    path('home/',blog_views.home,name='home'),
    path('addblog/',blog_views.addblog,name='addblog'),
    path('logout/',user_views.logout_view,name='logout'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 