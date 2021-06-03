from django.http import HttpResponse


def employee(request):
    data = "Hey! I am employee data"
    return HttpResponse(data)


def profile(request):
    data = "Hey! I am employee profile data"
    return HttpResponse(data)
