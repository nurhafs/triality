from django.shortcuts import render
from django.http import JsonResponse
import requests, json

# Create your views here.
def findbooks(request):
    return render(request, 'findbk.html')

def olah_data(request):
    arg = request.GET['r']
    url = "https://www.googleapis.com/books/v1/volumes?q=" + arg
    y = requests.get(url)
    data = json.loads(y.content)
    return JsonResponse(data, safe=False)