from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('porto/', views.porto, name="portofolio"),
    path('exp/', views.cv, name="experience"),
    path('prompt/', views.idea, name="prompt"),
    path('schedule/', views.readcourse),
    path('addsched/', views.sched),
    path('savesched', views.savecourse),
    path('deletecourse/<int:kp>', views.delcourse, name="delcourse")
    
]
