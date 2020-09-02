from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    print("hello")
    return HttpResponse("ok")

def login2(request):
    print("world")
    return HttpResponse("err")