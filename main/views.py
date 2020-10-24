from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Input_Form
from .models import Course


def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')

def porto(request):
    return render(request, 'main/porto.html')

def cv(request):
    return render(request, 'main/cv.html')

def idea(request):
    return render(request, 'main/addon.html')

response = {}

def sched(request):
    response = {'name' : 'PPW', 'input_form' : Input_Form}
    return render(request, 'main/addsched.html', response)

def savecourse(request):
    form = Input_Form(request.POST or None)
    if (form.is_valid and request.method=='POST'):
        form.save()
        return HttpResponseRedirect('/schedule')
    else:
        return HttpResponseRedirect('/')

def readcourse(request):
    courses = Course.objects.all()
    response['courses'] = courses

    html = 'main/schedule.html'
    return render(request, html, response)

def delcourse(request, kp):
    obj = Course.objects.get(pk=kp)
    obj.delete()
    return HttpResponseRedirect('/schedule')