from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.



def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username not available")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')