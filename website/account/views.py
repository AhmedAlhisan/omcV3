from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def sign_up_user(request : HttpRequest):
   if request.method == 'POST':
         if request.POST['password'] == request.POST['password1']:
            new_user = User.objects.create_user(is_active=0 , username = request.POST['username'] , first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , password=request.POST['password'])
            new_user.save()
            messages.success(request , 'تم ارسال طلب الانضمام بنجاح ')
            return redirect('account:login')
         else:
             messages.success(request , 'كلمة المرور لابد ان تكون متطابقة')
   return render(request , 'account/register.html')
              
		

def logout_user(request : HttpRequest):

    logout(request)
    messages.success(request , 'تم تسجيل الخروج بنجاح')

    return redirect("main:home-page")


def login_user(request : HttpRequest):

    
    
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

        if user is not None and user.is_active == 1:
            #login user
            login(request, user)
            messages.success(request , f'  تم تسجيل الدخول بنجاح  {request.user.last_name} {request.user.first_name}  ')
            return redirect("main:home-page")
        elif user is not None and user.is_active == 0 :
            messages.success(request , 'لم يتم تنشيط الحساب بعد')
        else:    
            messages.success(request , 'الرقم العسكري او كلمة المرور خاطئة')

    return render(request, "account/login.html")