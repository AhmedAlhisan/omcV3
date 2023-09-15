from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def sign_up_user(request : HttpRequest):

   if request.method == 'POST':
        if  len(request.POST.get('last_name')) < 10:
            messages.success(request , ' الرجاء كتابة الاسم كاملا ') 
           
        elif  request.POST['password'] != request.POST['password1']:
            messages.success(request , '   كلمة السر غير متطابقه ')       
        elif len( request.POST['password']) < 8  or not any(char.isupper() for char in  request.POST['password']) or not any(char in "!@#$%^&*(),.?\":{}|<>" for char in  request.POST['password']):
            messages.success(request , 'ثمانية خانات على الاقل !@#$%^&*(),.? يجب ان تحتوي كلمة السر على حروف كبيره و رموز خاصه ') 
                 
         
        else: 
            new_user = User.objects.create_user(is_active=0 , username = request.POST['username'] , first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , password=request.POST['password'])
            new_user.save()
            messages.success(request , 'تم ارسال طلب الانضمام بنجاح ')
            return redirect('account:login')
        
   return render(request , 'account/register.html' )
              
		

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