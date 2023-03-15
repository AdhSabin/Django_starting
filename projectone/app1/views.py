from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Responses")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    my_dict = {
        "Name":name,
        "Age":age
    }
    return JsonResponse(my_dict) 

def myfirstpage(request):
    return render(request, 'index.html') 

def mysecondpage(request):
    return render (request,'second.html')

def mythirdpage(request):
    var = "Hello"
    greetings = "How are you?"
    list = ['pen','book','copy','marker']
    num1, num2 = 5,7
    ans = num1 > num2
    my_dict = {
        "var" : var,
        "msg" : greetings,
        "mylist" : list,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render (request,'third.html',context=my_dict)  

def myimagepage(request):
    return render (request,'imagepage.html')

def myform(request):
    return render (request,'myform.html')   

def submitmyform(request):
    my_dict1={
        "Name":request.POST['name'],
        "Address":request.POST['add'],
        "Password":request.POST['pass'],
        "Method" : request.method

    }   
    return JsonResponse(my_dict1)  





    
    
