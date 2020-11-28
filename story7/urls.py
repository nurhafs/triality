from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'story7'


urlpatterns = [
    path('', views.accr),
]
