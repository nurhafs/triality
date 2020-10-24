from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'story6'


urlpatterns = [
    path('', views.act, name="kegiatan"),
    path('peserta/<int:par_id>', views.peserta, name="peserta"),
    path('delact/<int:kp>', views.delact, name="delact")
]
