from django.http import HttpResponse


def home(request):
    data = "Hey! I am home data"
    return HttpResponse(data)


def about(request):
    data = "Hey! I am about data"
    return HttpResponse(data)
