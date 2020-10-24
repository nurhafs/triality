"""story URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profile/', include('main.urls')),
    path('porto/', include('main.urls')),
    path('exp/', include('main.urls')),
    path('prompt/', include('main.urls')),
    path('schedule/', include('main.urls')),
    path('addsched/', include('main.urls')),
    path('editcourse/', include('main.urls')),
    path('activity/', include('story6.urls')),
]
