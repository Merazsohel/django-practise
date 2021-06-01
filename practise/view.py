from django.http import HttpResponse


def home(request):
    return HttpResponse("This is Home")


def about(request):
    return HttpResponse("This is About")
