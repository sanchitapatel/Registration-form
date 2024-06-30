from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

def login(request):

    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        #print(email,password)
        data=Student.objects.filter(Email=email)
        if data:
            data=Student.objects.get(Email=email)
            password=data.Password
            print(password)

    #     # print(request.method)
    #     # print(request.POST)
        return render(request,'login.html') 



    # data=Student.objects.filter(Email=email)
    # if data:
    #     msg='email already exist'
    #     return render(request,'home.html',{'key':msg})
    # else:
    #     if password==cpassword:
            
    #         Student.objects.create(name='name',
    #                                contact='contact',
    #                                Email='email',
    #                                password='password')
    #         msg="registration successfully"
    #         return render(request,'home.html',{'key':msg})
    #     else:
    #         msg="password &cpassword not matched"
    #         return render(request,'home.html',{'key':msg})
        
    #     #print(name)
    #     #print(email)
    #     #Student.objects.create(Name=name,
    #                         #Email=email)
    #     #return HttpResponse('Registration successfully')'''
    return render(request,'login.html')
