from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view1(request):
    return HttpResponse("<h1>Welcome to the Home page</h1>")

def view2(request,email):
    return render(request,"sample.html",context={'email':email,'name':"Mohini"})

def view3(request,name):
    return HttpResponse(f'<h1>Hello Ms. {name} </h1>')

def if_demo(request):
    login = True
    return render(request,"if_demo.html", context={'login':login})   

def ifelse_demo(request):
    login = True
    return render(request,"ifelse_demo.html", context={'login':login, 'name':"Mohini", 'a':50, 'b':90})   

def for_demo(request):
    return render(request, "for_demo.html", context={'items':['Google', 'Microsoft', 'JPMorgan', 'Oracle'], 'profile':{'name':"Mohini", 'age':25, 'sal':30000}})

