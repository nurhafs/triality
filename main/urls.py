from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('/mainpage', views.main_page, name="main"),
    path('profile/', views.profile, name="profile"),
    path('porto/', views.porto, name="portofolio"),
    path('exp/', views.cv, name="experience"),
    path('prompt/', views.idea, name="prompt")
]
