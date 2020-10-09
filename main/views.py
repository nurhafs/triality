from django.shortcuts import render


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