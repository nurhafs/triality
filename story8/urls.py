from django.urls import path
from django.conf.urls import url
from .views import findbooks, olah_data

app_name = 'story8'


urlpatterns = [
    path('', findbooks),
    path('data/', olah_data)
]
