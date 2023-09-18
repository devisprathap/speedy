from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse


def  register(request):
    if request.method=='POST':

        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email= request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This field is required')
                return redirect('/register')

            else:

                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('/login')
        else:
            messages.info(request,'password not matching')
            return redirect('/register')
        return redirect('/')

    return render(request,"register.html")





def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/submit')
        else:
            messages.info(request,"invalid credential")
            return redirect('/login')
    return render(request,'login.html')









def form(request):
    if request.method=='POST':
        username = request.POST['username']
        DOB = request.POST['DOB']
        age= request.POST['age']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']

        user=auth.authenticate(username=username,DOB=DOB,age=age,phonenumber=phonenumber,address=address)
        # if User.objects.filter(username=username).exists():
        #     messages.info(request, 'This field is required')
        #     return redirect('/form')
        #
        # else:
        #
        #     user = User.objects.create_user(username=username)
        #
        #     user.save();
        #     return redirect('/link')

        return redirect('/link')



    return render(request, 'form.html')
#


def form1(request):
    if request.method=='POST':

        return redirect('/link')
    return render(request,"form1.html")



def logout(request):
    auth.logout(request)
    return render(request,"home.html")

def home(request):
    return render(request,"home.html")
def link(request):
    return render(request,"link.html")
    return redirect('/')

def submit(request):
    return render(request,"submit.html")