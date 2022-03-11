from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def login_user(request):
    form = AuthenticationForm
    if request.POST:
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():

            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(password=password,username=username)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'xatolik bor qaytib urinib koring')
                print('xato')
        else:
            messages.error(request, 'xatolik bor qaytib urinib koring')
            print('xato1')

    ctx = {
        'forms':form
    }
    return render(request,'login.html',ctx)
def register_user(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,'success')
            return redirect('login')
            messages.success(request,"SUCCESS:)")
            print('ishladi')
        else:
            messages.error(request,"ERROR!!!")
            print('xato')

    ctx= {
        'forms':form
    }
    return render(request,'register.html',ctx)
def logout_user(request):
    logout(request)
    return redirect('home')