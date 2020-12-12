from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'story9'

urlpatterns = [
    path('', views.specialPage),
    path('signup/', views.createUser),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'))
    
]