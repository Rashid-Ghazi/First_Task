from django.shortcuts import HttpResponse, render
from django.http import JsonResponse


def home(request):
    print(request.method, request.META)
    person = {
        "name" : "abc"
    }
    return render(request, 'home.html', person)


def about_us(request):
    return render(request, 'about_us.html', {})

def Contact_us(request):
    return render(request,'Contact_us.html',{})
