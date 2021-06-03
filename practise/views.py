from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    data = "Hey! I am about data"
    return HttpResponse(data)
