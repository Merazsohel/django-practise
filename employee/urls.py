from django.urls import path
from employee import views

urlpatterns = [
    path('', views.home),
    path('profile', views.profile),
]
