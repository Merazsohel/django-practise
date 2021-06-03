from django.shortcuts import render


def home(request):
    return render(request, "employee/index.html")


def profile(request):
    return render(request, "employee/profile.html")
