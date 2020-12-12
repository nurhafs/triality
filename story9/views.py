from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def specialPage(request):
    response = {}
    return render(request, "spec.html", response)

def createUser(request):
    makeUser = formUser(request.POST or None)
    response= {
        'newUserForm':makeUser
    }

    if request.method=='POST':
        if makeUser.is_valid():
            user = User.objects.create_user(
				username=makeUser.cleaned_data.get('username'),
                email=makeUser.cleaned_data.get('email'),
				password=makeUser.cleaned_data.get('password')
				)
            user.save()
    return render(request, 'signup.html', response)