from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1> Welcome to the django page ... </h1>")
def Newapp(request):
    return HttpResponse("<h1> This is a new page.. </h1>")