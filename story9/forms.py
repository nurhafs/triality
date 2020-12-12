from django import forms
from django.contrib.auth.forms import AuthenticationForm

class formUser(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

