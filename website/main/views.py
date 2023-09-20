from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse,HttpResponseRedirect
from . models import Employee , Course , Mandate , Activity
from django.contrib import messages
from django.urls import reverse
from datetime import datetime , date
from django.contrib.auth.models import User
from hijri_converter import Hijri, Gregorian
import os
from django.core.paginator import Paginator
from django.db.models import Q



def assiengEmployeeReport(request , employee_id):
    Report_date = date.today
    git_all_activity_for_assigend_emp = Activity.objects.filter(employee_active=employee_id)
    return render(request , 'main/ReportForAssigenEmp.html',{'git_all_activity_for_assigend_emp':git_all_activity_for_assigend_emp , 'Report_date':Report_date})
def arabic_pdf_activity(request):
    all_activity = Activity.objects.all()
    for i in all_activity:
        print(i.activity_type)
    
    Report_date = date.today
   
    return render(request , 'main/aaa.html',{'all_activity':all_activity ,'Report_date':Report_date})
def arabic_pdf_courses(request):
    all_activity = Activity.objects.all()
    for i in all_activity:
        print(i.activity_type)
    
    Report_date = date.today
   
    return render(request , 'main/bbb.html',{'all_activity':all_activity ,'Report_date':Report_date})

def arabic_pdf_mandate(request):
    all_activity = Activity.objects.all()
    for i in all_activity:
        print(i.activity_type)
    
    Report_date = date.today
   
    return render(request , 'main/ccc.html',{'all_activity':all_activity ,'Report_date':Report_date})

# globalVar
check_new_request_user = User.objects.filter(is_active = 0)






def add_employee(request : HttpRequest):
    if request.user.is_authenticated:
        check_new_request_user = User.objects.filter(is_active = 0)
        if request.method =='POST':
            new_emp = Employee(name = request.POST['name'] , preRank = request.POST['preRank'], mulirty_classfication = request.POST['mulirty_classfication'], non_mulirty_classfication = request.POST['non_mulirty_classfication'],employee_number = request.POST['employee_number'] , major = request.POST['major'],certificate=request.POST['certificate'],graduted_from=request.POST['graduted_from'],job_title=request.POST['job_title'],work_place=request.POST['work_place'],writen_by=request.user)
            new_emp.save()
            messages.success(request , 'تمت اضافة الموظف بنجـاح')
            return redirect('main:show-all')


        return render(request , 'main/add-employee.html',{'check_new_request_user':check_new_request_user})
    return redirect('account:login')
def delet_employee(request : HttpRequest, employee_id):
    if request.user.is_staff:
        assigend_emp = Employee.objects.get(id = employee_id)
        if request.method == 'POST' and request.POST.get('action') == 'delete':
            # delete the band from the database
            assigend_emp.delete()
            messages.success(request , 'تم الحذف بنجاح ')
            return redirect('main:show-all')
        return render(request,
                    'main/delete.html',
                    {'assigend_emp': assigend_emp})
    return redirect('account:login')



def home_page(request : HttpRequest):
    if request.user.is_staff:
        check_new_request_user = User.objects.filter(is_active = 0)
        return render(request , 'main/home.html' , {'check_new_request_user':check_new_request_user})
    return render(request , 'main/home.html' )

def show_request_user_for_admin(request:HttpRequest):
    if request.user.is_staff:
        check_new_request_user = User.objects.filter(is_active = 0)
        return render(request , 'main/show_request_user.html' , {'check_new_request_user':check_new_request_user})
    return redirect('account:login')

def accept_user_request(request:HttpRequest , employee_id):
    if request.user.is_staff:
        assigne_user = User.objects.get(id = employee_id)
        assigne_user.is_active = 1
        assigne_user.save()
        messages.success(request , 'تمت الموافقة على طلب التسجيل')
        return redirect('main:show-request')
    return redirect('account:login')

def reject_user_request(request : HttpRequest , employee_id):
        assigne_user = User.objects.get(id = employee_id)


        assigne_user.delete()
        messages.success(request , 'تم رفض طلب التسجيل بنجاح')

        return redirect(  'main:show-request')







def show_all_emp(request : HttpRequest):
    if request.user.is_authenticated:
        my_employee = Employee.objects.all()
        number_of_employee = 0 
        for i in my_employee:
            number_of_employee = number_of_employee + 1

        check_new_request_user = User.objects.filter(is_active = 0)
        if 'search' in request.GET:
            all_emp=Employee.objects.filter(name__contains=request.GET['search'])
        elif 'searchnum' in request.GET:
            convert_var : int = request.GET['searchnum']
            all_emp=Employee.objects.filter(employee_number=convert_var)
        else:
            all_emp = Employee.objects.all()
            paginator = Paginator(all_emp, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
          

        return render(request , 'main/show-grid-employee.html' , {'number_of_employee':number_of_employee,'page_obj':page_obj,  'all_emp':all_emp , 'check_new_request_user':check_new_request_user})
    return redirect('account:login')


def show_assiegnd_emplyee (request : HttpRequest , emplyee_id):
    if request.user.is_authenticated:
        
        assigen_emp = Employee.objects.get(id=emplyee_id)
        
            
        
        labels = []
        data = []
        check_new_request_user = User.objects.filter(is_active = 0)

        assigend_emp = Employee.objects.get(id=emplyee_id)
        all_activity_for_singal_emp = Activity.objects.filter(employee_active = assigend_emp.id)
        if all_activity_for_singal_emp : 
            counter_of_activity : int = 0
            counter_of_mandate:int = 0
            counter_of_courses:int = 0
            for activity in all_activity_for_singal_emp:
                if activity.activity_type=='Type_one_active':
                    counter_of_activity = counter_of_activity+1
                elif activity.activity_type=='Type_three_mandate':
                    counter_of_mandate=counter_of_mandate+1
                else:
                    counter_of_courses=counter_of_courses+1  
            labels.append('نشاط')        
            data.append(counter_of_activity)  

            labels.append('انتداب')        
            data.append(counter_of_mandate)   

            labels.append('دورة')        
            data.append(counter_of_courses)              

        return render(request ,'main/show-single-employee.html' , {'labels':labels ,'data':data  , 'assigend_emp':assigend_emp , 'check_new_request_user':check_new_request_user} )
    return redirect('account:login')

def add_course(request :HttpRequest , employee_id):
    if request.user.is_authenticated:
        assigend_emp = Employee.objects.get(id = employee_id)

        if request.method == 'POST':

            full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
            full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
            full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
            full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
            full_start_en_date = full_start_en_date.isoformat()
            full_end_en_date = full_end_en_date.isoformat()

            new_couorse = Course(start_hijri_day = request.POST['hijridaystart'],start_hijri_month = request.POST['hijrimonthstart'],start_hijri_year = request.POST['hijriyearstart'] ,end_hijri_day = request.POST['hijridayend'] , end_hijri_month = request.POST['hijrimonthend'] ,end_hijri_year = request.POST['hijriyearend']  ,course_certficate_upload =  request.FILES['certificate_upload_pdf'],
                    starthijridate =full_start_hijri_date , endhijridate= full_end_hijri_date,writen_by = request.user , assigend_employee = assigend_emp , title = request.POST['title'],course_number = request.POST['course_number'], course_provider = request.POST['course_provider'],  course_provider_country = request.POST['course_provider_country'],where_course_has_been_provide = request.POST['where_course_has_been_provide'],degree_percent=request.POST['degree_percent'],rating_word=request.POST['rating_word'],startDate=full_start_en_date,endDate=full_end_en_date )
            if datetime.strptime(new_couorse.startDate, '%Y-%m-%d') > datetime.strptime(new_couorse.endDate,'%Y-%m-%d'):
                messages.success(request , 'عذرا يرجى ادخال التاريخ بشكل صحيح')
            else:
                new_couorse.save()

                messages.success(request , 'تمت اضافة دورة بنجاح ')
                return redirect(reverse('main:show-assigend', kwargs={"emplyee_id": employee_id}))
        return render(request , 'main/add-course.html' , {"check_new_request_user":check_new_request_user})
    return redirect('account:login')

def update_employee(request : HttpRequest , employee_id):
    if request.user.is_authenticated:
        assigend_emp = Employee.objects.get(id = employee_id)
        if request.method == 'POST':
            assigend_emp.name=request.POST['name']
            
            assigend_emp.employee_number = request.POST['employee_number']
            assigend_emp.major = request.POST['major']
            assigend_emp.certificate = request.POST['certificate']
            assigend_emp.graduted_from=request.POST['graduted_from']
            assigend_emp.job_title=request.POST['job_title']
            assigend_emp.work_place=request.POST['work_place']
            assigend_emp.writen_by=request.user
            assigend_emp.preRank=request.POST['preRank']
            assigend_emp.mulirty_classfication= request.POST['mulirty_classfication']
            assigend_emp.mulirty_classfication= request.POST['non_mulirty_classfication']
            assigend_emp.save()
            messages.success(request , 'تمـت تعديل الموظف بنجاح')
            return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':employee_id}))
        return render(request , 'main/update_employee.html' , {'assigend_emp':assigend_emp , 'check_new_request_user':check_new_request_user})
    return redirect('account:login')

def add_mandate(request : HttpRequest ,employee_id ):
    if request.user.is_authenticated:
        assigend_employee = Employee.objects.get(id = employee_id)
        if request.method == 'POST':
            full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
            full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
            full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
            full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
            full_start_en_date = full_start_en_date.isoformat()
            full_end_en_date = full_end_en_date.isoformat()
            new_mandate = Mandate(end_hijri_day = request.POST['hijridayend'] , end_hijri_month = request.POST['hijrimonthend'] , end_hijri_year = request.POST['hijriyearend'],start_hijri_day = request.POST['hijridaystart'],start_hijri_month=request.POST['hijrimonthstart'] , start_hijri_year = request.POST['hijriyearstart'] ,mandate_employee = assigend_employee , starthijridate = full_start_hijri_date , endhijridate = full_end_hijri_date  , writen_by = request.user , start_date = full_start_en_date , end_date=full_end_en_date ,mandate_place = request.POST['mandate_place'] ,mandate_type = request.POST['mandate_type'] )
            print(new_mandate)
            print(type(new_mandate.start_date))
            if datetime.strptime(new_mandate.start_date,'%Y-%m-%d') < datetime.strptime(new_mandate.end_date , '%Y-%m-%d'):
                new_mandate.save()
                messages.success(request , 'تم اضافة الانتداب بنجاح')
            else:
                messages.success(request , 'عذرا يرجى ادخال تاريخ بداية و نهاية صحيح ')
                return render(request , 'main/add_mandate.html' , {'check_new_request_user':check_new_request_user})
            return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':employee_id }))

        return render(request , 'main/add_mandate.html' , {'check_new_request_user':check_new_request_user} )
    return redirect('account:login')

def show_courses_and_mondate(request : HttpRequest , employee_id):
    if request.user.is_authenticated:
        current_time = datetime.now().strftime('%Y-%m-%d')
        assigend_emp = Employee.objects.get(id = employee_id)
        show_all_activity_all=Activity.objects.filter(employee_active = assigend_emp)

        show_all_courses = Course.objects.filter(assigend_employee = assigend_emp)
        show_all_mondate = Mandate.objects.filter(mandate_employee = assigend_emp)
        show_all_activity = Activity.objects.filter(employee_active = assigend_emp).filter(activity_type = 'Type_one_active')
        for j in show_all_activity:
            activity_date = j.activity_end_date.isoformat()
            if datetime.strptime (current_time , '%Y-%m-%d') >= datetime.strptime(activity_date , '%Y-%m-%d'):
                j.activity_tack_action = 1
                j.save()
                print('ok')
        counter : int = 0
        for i in show_all_mondate:
            counter = i.date_diff + counter
            print(counter)
            

        return render(request , 'main/show_activityes.html',{'show_all_activity_all':show_all_activity_all,'show_all_courses':show_all_courses ,'show_all_mondate':show_all_mondate ,'assigend_emp':assigend_emp , 'counter':counter , 'show_all_activity':show_all_activity , 'current_time':current_time,'check_new_request_user':check_new_request_user  })
    return redirect('account:login')

def editCourse (request : HttpRequest , activity_id : int  ):
    
    if request.user.is_authenticated:
        assigend_course =Course.objects.get(id=activity_id)
        assigend_activity=Activity.objects.get(id=assigend_course.id)
        for_emp = Employee.objects.get(id = assigend_course.assigend_employee.id)

        if request.method == 'POST':
            full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
            full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
            full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
            full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
            full_start_en_date = full_start_en_date.isoformat()
            full_end_en_date = full_end_en_date.isoformat()
            new_couorse = Course( start_hijri_day = request.POST['hijridaystart'],start_hijri_month = request.POST['hijrimonthstart'],start_hijri_year = request.POST['hijriyearstart'] ,end_hijri_day = request.POST['hijridayend'] , end_hijri_month = request.POST['hijrimonthend'] ,end_hijri_year = request.POST['hijriyearend']  ,course_certficate_upload =  request.FILES.get('course_certficate_upload'),
            starthijridate =full_start_hijri_date , endhijridate= full_end_hijri_date,writen_by = request.user , assigend_employee = assigend_course.assigend_employee , title = request.POST['title'],course_number = request.POST['course_number'], course_provider = request.POST['course_provider'],  course_provider_country = request.POST['course_provider_country'],where_course_has_been_provide = request.POST['where_course_has_been_provide'],degree_percent=request.POST['degree_percent'],rating_word=request.POST['rating_word'],startDate=full_start_en_date,endDate=full_end_en_date )           
            if datetime.strptime(full_start_en_date, '%Y-%m-%d') < datetime.strptime(full_end_en_date,'%Y-%m-%d'):
                git_all_employee_activity = Activity.objects.filter(employee_active = new_couorse.assigend_employee.id).exists()
                if git_all_employee_activity:
                    for i in Activity.objects.filter(employee_active = new_couorse.assigend_employee.id) :
                        if i.id != assigend_activity.id:
                            old_end_date=str(i.activity_end_date)
                            old_start_date=str(i.activity_st_date)
                            print(old_end_date , i)
                            print(new_couorse.startDate)
                        
                        
                            print('...............itration')
                            if (datetime.strptime(old_end_date , '%Y-%m-%d') < datetime.strptime(new_couorse.startDate , '%Y-%m-%d')and (new_couorse.endDate , '%Y-%m-%d')> (old_end_date , '%Y-%m-%d'))or (datetime.strptime(new_couorse.endDate , '%Y-%m-%d') < datetime.strptime(old_start_date , '%Y-%m-%d') ) :
                                print("cached")
                                print(new_couorse.endDate)
                                print(new_couorse.startDate)
                                print(old_end_date)
                                print(old_start_date)
                                continue
                            

                            messages.success(request , 'عذرا الموظف يوجد لديه نشاط فعال في هذه الفترة')
                            return render(request , 'main/update_course.html' ,{'assigend_course':assigend_course})
                    else:
                        assigend_course.starthijridate = new_couorse.starthijridate
                        assigend_course.endhijridate = new_couorse.endhijridate
                        assigend_course.startDate=new_couorse.startDate
                        assigend_course.endDate = new_couorse.endDate
                        assigend_course.start_hijri_day=new_couorse.start_hijri_day
                        assigend_course.start_hijri_month=new_couorse.start_hijri_month
                        assigend_course.start_hijri_year=new_couorse.start_hijri_year
                        assigend_course.end_hijri_day=new_couorse.end_hijri_day
                        assigend_course.end_hijri_month=new_couorse.end_hijri_month
                        assigend_course.end_hijri_year=new_couorse.end_hijri_year
                        assigend_course.title=new_couorse.title
                        assigend_course.course_number=new_couorse.course_number
                        assigend_course.course_provider=new_couorse.course_provider
                        assigend_course.course_provider_country=new_couorse.course_provider_country
                        assigend_course.where_course_has_been_provide=new_couorse.where_course_has_been_provide
                        assigend_course.degree_percent=new_couorse.degree_percent
                        assigend_course.rating_word=new_couorse.rating_word
                        if new_couorse.course_certficate_upload:
                            assigend_course.course_certficate_upload=new_couorse.course_certficate_upload
                        

                        assigend_activity.activityName=new_couorse.title
                        assigend_activity.activity_st_date=new_couorse.startDate
                        assigend_activity.activity_end_date=new_couorse.endDate
                        assigend_activity.start_hijri_day=new_couorse.start_hijri_day
                        assigend_activity.start_hijri_month=new_couorse.start_hijri_month
                        assigend_activity.start_hijri_year=new_couorse.start_hijri_year
                        assigend_activity.end_hijri_day=new_couorse.end_hijri_day
                        assigend_activity.end_hijri_month=new_couorse.end_hijri_month
                        assigend_activity.end_hijri_year=new_couorse.end_hijri_year
                        assigend_activity.full_end_hijri_date=new_couorse.endhijridate
                        assigend_activity.full_start_hijri_date=new_couorse.starthijridate
                        

                        assigend_course.save()
                        assigend_activity.save()
                        messages.success(request , 'تم تعديل بينات الدورة بنجاح')
                        return redirect(reverse('main:show-course-mandate-emp' , kwargs={'employee_id':for_emp.id}))


                
                
        return render(request , 'main/update_course.html' , {'assigend_course':assigend_course})
    return redirect('account:login')

def show_mandates(request:HttpRequest , employee_id):
    all_mandates_for_emp = Mandate.objects.filter(mandate_employee = employee_id)
    for_emp = Employee.objects.get(id = employee_id)
    counter : int = 0
    for i in all_mandates_for_emp:
            counter = i.date_diff + counter
            print(counter)

    return render(request , 'main/show_mandates.html', {'all_mandates_for_emp':all_mandates_for_emp ,'for_emp':for_emp , 'counter':counter , 'check_new_request_user':check_new_request_user})

def show_only_activity(request : HttpRequest , employee_id):
    for_emp = Employee.objects.get(pk = employee_id)
    all_activity_for_assigen_emp = Activity.objects.filter(employee_active = for_emp.id)
    git_all_activity_data = all_activity_for_assigen_emp.filter(activity_type= 'Type_one_active').filter(activity_tack_action = 1)

    return render(request , 'main/showActiveOnly.html' , {'git_all_activity_data':git_all_activity_data})



def show_courses(request:HttpRequest , employee_id):
    all_courses_for_emp = Course.objects.filter(assigend_employee = employee_id)
    for_emp = Employee.objects.get(id = employee_id)
    counter = 0
    for i in all_courses_for_emp:
        counter = counter + 1
        print(counter)
    return render(request , 'main/show_courses.html' , {'all_courses_for_emp':all_courses_for_emp , 'for_emp':for_emp , 'counter':counter , 'check_new_request_user':check_new_request_user} )

def deleteCourse(request : HttpRequest , course_id):
    if request.user.is_staff:
        assigend_course = Course.objects.get(id=course_id)
        for_emp=Employee.objects.get(id=assigend_course.assigend_employee.id)
        if request.method == 'POST':
            # delete the band from the database
            assigend_course.delete()
            messages.success(request , 'تم الحذف بنجاح ')
            return redirect(reverse('main:show-course-mandate-emp' , kwargs={'employee_id':for_emp.id}))

        return render(request , 'main/delete_course.html' , {'assigend_course':assigend_course  })
    return redirect('account:login')

def editmandate(request : HttpRequest , mandate_id):
    if request.user.is_authenticated:
        assigend_activity=Activity.objects.get(id=mandate_id)
        assigen_mandate =Mandate.objects.get(id = assigend_activity.id)
       
        for_emp=Employee.objects.get(id = assigen_mandate.mandate_employee.id)

        if request.method == 'POST':
                full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
                full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
                full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
                full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
                full_start_en_date = full_start_en_date.isoformat()
                full_end_en_date = full_end_en_date.isoformat()
                
                if datetime.strptime(full_start_en_date,'%Y-%m-%d') < datetime.strptime(full_end_en_date , '%Y-%m-%d'):
                    assigen_mandate.mandate_type=request.POST['mandate_type']
                    assigen_mandate.mandate_place=request.POST['mandate_place']
                    assigen_mandate.start_hijri_day=request.POST['hijridaystart']
                    assigen_mandate.start_hijri_month=request.POST['hijrimonthstart']
                    assigen_mandate.start_hijri_year=request.POST['hijriyearstart']
                    assigen_mandate.end_hijri_day=request.POST['hijridayend']
                    assigen_mandate.end_hijri_month=request.POST['hijrimonthend']
                    assigen_mandate.end_hijri_year = request.POST['hijriyearend']
                    assigen_mandate.start_date=full_start_en_date
                    assigen_mandate.end_date=full_end_en_date
                    assigen_mandate.starthijridate=full_start_hijri_date
                    assigen_mandate.endhijridate=full_end_hijri_date

                    assigen_mandate.save()
                    messages.success(request , 'تم تعديل الانتداب بنجاح')
                    return redirect(reverse('main:show-course-mandate-emp' , kwargs={'employee_id':for_emp.id}))
                else:
                    messages.success(request , 'عذرا يرجى ادخال تاريخ بداية و نهاية صحيح ')
                    return render(request , 'main/edit_mandate.html')


        return render(request , 'main/edit_mandate.html' , {'assigen_mandate':assigen_mandate , 'for_emp':for_emp})
    return redirect('account:login')


def deleteMandate(request : HttpRequest , mandate_id):

        assigen_mandate = Mandate.objects.get(id=mandate_id)
        for_emp=Employee.objects.get(id=assigen_mandate.mandate_employee.id)
        if request.method == 'POST':
            # delete the band from the database
            assigen_mandate.delete()
            messages.success(request , 'تم الحذف بنجاح ')
            return redirect(reverse('main:show_mandate' , kwargs={'employee_id':for_emp.id}))




def showStatisticForMandate(request : HttpRequest):
    labels = []
    data = []
    if request.user.is_authenticated:
        check_new_request_user = User.objects.filter(is_active = 0)

        '''year for mandate'''
        all_mandate_year = Activity.objects.filter(activity_type = 'Type_three_mandate')
     
        yearDic = {'one' : 0 ,
        'tow':0  ,
        'three' :  0,
        'four' : 0,
        'fife' :  0,
      
        }
        
        for i in all_mandate_year:
            if i.start_hijri_year == '1440':
                yearDic['one']+=1
            elif i.start_hijri_year == '1441':
                 yearDic['tow']+=1
            elif i.start_hijri_year == '1442':
                yearDic['three']+=1
            elif i.start_hijri_year == '1443':
                yearDic['four']+=1
            elif i.start_hijri_year == '1444':
                yearDic['fife']+=1
            yearList = list(yearDic.values()) 
            print(yearList)   
            


        '''for showing all activity'''
        all_emp_mandate=Activity.objects.filter(activity_type='Type_three_mandate' )
        mulitry_mandate=all_emp_mandate.filter(activity_in_out='inside')
        data_for_month_mulitry={'one' : 0 ,
        'tow':0  ,
        'three' :  0,
        'four' : 0,
        'fife' :  0,
        'six' :  0,
        'seven' : 0,
        'eight' :  0,
        'nine' :  0,
        'ten' :  0,
        'eleven' :  0,
        'tweleve' :  0
        }
        
        
        for i in mulitry_mandate:
            if i.start_hijri_month == '1' and i.start_hijri_year =='1443':
                data_for_month_mulitry['one']+=1
            elif i.start_hijri_month == '2' and i.start_hijri_year =='1443':
                data_for_month_mulitry['tow']+=1
            elif i.start_hijri_month == '3' and i.start_hijri_year =='1443':
                data_for_month_mulitry['three'] +=1
            elif i.start_hijri_month == '4' and i.start_hijri_year =='1443':
                data_for_month_mulitry['four'] += 1
            elif i.start_hijri_month == '5' and i.start_hijri_year =='1443':
                data_for_month_mulitry['fife']+=1
            elif i.start_hijri_month == '6' and i.start_hijri_year =='1443':
                data_for_month_mulitry['six']+=1
            elif i.start_hijri_month == '7' and i.start_hijri_year =='1443':
                data_for_month_mulitry['seven']+=1
            elif i.start_hijri_month == '8' and i.start_hijri_year =='1443':
                data_for_month_mulitry['eight']+=1
            elif i.start_hijri_month == '9'and i.start_hijri_year =='1443':
                data_for_month_mulitry['nine']+=1
            elif i.start_hijri_month == '10'and i.start_hijri_year =='1443':
                data_for_month_mulitry['ten']+=1
            elif i.start_hijri_month == '11'and i.start_hijri_year =='1443':
                data_for_month_mulitry['eleven']+=1
            elif i.start_hijri_month == '12' and i.start_hijri_year =='1443':
                data_for_month_mulitry['tweleve']+=1
            for key, value in data_for_month_mulitry.items():
                print(f"key{key} val {value}") 
            data_only_for_mulitry=list(data_for_month_mulitry.values())
            print(data_only_for_mulitry)
            '''for madny'''
        
        non_mulitry_mandate=all_emp_mandate.filter(activity_in_out='outside')
        data_for_month_non_mulitry={'one' : 0 ,
        'tow':0  ,
        'three' :  0,
        'four' : 0,
        'fife' :  0,
        'six' :  0,
        'seven' : 0,
        'eight' :  0,
        'nine' :  0,
        'ten' :  0,
        'eleven' :  0,
        'tweleve' :  0
        }
        
        
        for i in non_mulitry_mandate:
            if i.start_hijri_month == '1' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['one']+=1
            elif i.start_hijri_month == '2' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['tow']+=1
            elif i.start_hijri_month == '3' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['three'] +=1
            elif i.start_hijri_month == '4' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['four'] += 1
            elif i.start_hijri_month == '5' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['fife']+=1
            elif i.start_hijri_month == '6' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['six']+=1
            elif i.start_hijri_month == '7' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['seven']+=1
            elif i.start_hijri_month == '8' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['eight']+=1
            elif i.start_hijri_month == '9' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['nine']+=1
            elif i.start_hijri_month == '10' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['ten']+=1
            elif i.start_hijri_month == '11' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['eleven']+=1
            elif i.start_hijri_month == '12' and i.start_hijri_year =='1443':
                data_for_month_non_mulitry['tweleve']+=1
            for key, value in data_for_month_non_mulitry.items():
                print(f"key{key} val {value}") 
            data_only_for_non_mulitry=list(data_for_month_non_mulitry.values())
            print(data_only_for_non_mulitry)     

        
        

        '''for showing total mandate days for each employee '''
        all_emp = Employee.objects.all()
        for i in all_emp:
            x = i.id
            print(x)
            if Mandate.objects.filter(mandate_employee = x).exists():
                counter : int = 0
                all_assigen_mandate=Mandate.objects.filter(mandate_employee = x)
                for  j in all_assigen_mandate:
                    counter = counter + int(j.date_diff)
                    print(counter)
                    new_emp_field=Employee.objects.get(id = j.mandate_employee.id)
                    print(new_emp_field.id ,'h')
                    new_emp_field.number_of_mandate_days=counter
                    new_emp_field.save()
            else:
                re_assigend=Employee.objects.get(id=x)
                re_assigend.number_of_mandate_days=0
                re_assigend.save()
        all_employee=Employee.objects.all().order_by('-number_of_mandate_days')
        for n in all_employee:
            if n.number_of_mandate_days > 50 and n.number_of_mandate_days <= 100 :
                labels.append(n.name)
                data.append(n.number_of_mandate_days) 

        lower_hours_emp = Employee.objects.all().order_by('number_of_mandate_days')
        labelsLow = []
        dataLow = []
        for i in lower_hours_emp:
             if i.number_of_mandate_days < 10 and i.number_of_mandate_days > 0 :
                labelsLow.append(i.name)
                dataLow.append(i.number_of_mandate_days)

        show_zero_days_emp = Employee.objects.filter(number_of_mandate_days = 0 ) 
        paginator = Paginator(show_zero_days_emp, 2) # Show 2 items per page
        page_number = request.GET.get('page')
        page_obj_zero = paginator.get_page(page_number)

        allActivity = Activity.objects.all()
        labelsForActivityName = []
        dateForEachActivitCount = []
        
        activity_counter  = 0
        course_counter  = 0
        mandate_counter= 0
        for i in allActivity :
            if i.activity_type == 'Type_one_active':
                activity_counter = activity_counter + 1
            elif i.activity_type == 'Type_two_courses':
                course_counter = course_counter + 1
            elif i.activity_type == 'Type_three_mandate':
                mandate_counter = mandate_counter +1
        labelsForActivityName.append('نشاط')        
        dateForEachActivitCount.append(activity_counter)

        labelsForActivityName.append('دورة')
        dateForEachActivitCount.append(course_counter)

        labelsForActivityName.append('انتداب')
        dateForEachActivitCount.append(mandate_counter)
        for i in dateForEachActivitCount:
            print(i)
        for i in labelsForActivityName:
            print(i)  
               
        return render(request , 'main/test.html' , {'yearList':yearList , 'data_only_for_non_mulitry':data_only_for_non_mulitry , 'data_only_for_mulitry':data_only_for_mulitry , 'page_obj_zero':page_obj_zero,'labelsForActivityName':labelsForActivityName ,'dateForEachActivitCount':dateForEachActivitCount , 'show_zero_days_emp':show_zero_days_emp,'labelsLow':labelsLow,'dataLow':dataLow,'labels':labels , 'data':data ,'all_employee':all_employee , 'check_new_request_user':check_new_request_user}  )
    return redirect('account:login')


def add_activity(request : HttpRequest , employee_id):
    assigen_emp = Employee.objects.get(id = employee_id)
    if request.method == 'POST':
        full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
        full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
        full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
        full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
        full_start_en_date = full_start_en_date.isoformat()
        full_end_en_date = full_end_en_date.isoformat()
        new_activity = Activity(is_there_any_additional_activity = request.POST['is_there_any_additional_activity'] , the_additional_task=request.POST['the_additional_task'], activity_type=request.POST['activity_type'],activity_in_out=request.POST['activity_in_out'] , activity_location=request.POST['activity_location'], end_hijri_day=request.POST['hijridayend'] , end_hijri_month=request.POST['hijrimonthend'] , end_hijri_year = request.POST['hijriyearend'], start_hijri_day=request.POST['hijridaystart'] , start_hijri_month = request.POST['hijrimonthstart'] , start_hijri_year = request.POST['hijriyearstart'] , activityName = request.POST['activityName'] , activity_st_date = full_start_en_date , activity_end_date = full_end_en_date , full_start_hijri_date =full_start_hijri_date , full_end_hijri_date = full_end_hijri_date , employee_active = assigen_emp , writen_by_user = request.user )
        if datetime.strptime(new_activity.activity_st_date, '%Y-%m-%d')< datetime.strptime(new_activity.activity_end_date,'%Y-%m-%d'):
            git_all_employee_activity = Activity.objects.filter(employee_active = new_activity.employee_active).exists()
            if git_all_employee_activity:

                for i in Activity.objects.filter(employee_active = new_activity.employee_active) :
                    old_end_date=str(i.activity_end_date)
                    old_start_date=str(i.activity_st_date)
                    print(old_end_date , i)
                    print(new_activity.activity_st_date)
                    
                    
                    print('...............itration')
                    if (datetime.strptime(old_end_date , '%Y-%m-%d') < datetime.strptime(new_activity.activity_st_date , '%Y-%m-%d')and (new_activity.activity_end_date , '%Y-%m-%d')> (old_end_date , '%Y-%m-%d'))or (datetime.strptime(new_activity.activity_end_date , '%Y-%m-%d') < datetime.strptime(old_start_date , '%Y-%m-%d') ) :
                       print("cached")
                       print(new_activity.activity_st_date)
                       print(new_activity.activity_end_date)
                       print(old_end_date)
                       print(old_start_date)
                       continue
                    
                    
                    messages.success(request , 'عذرا الموظف يوجد لديه نشاط فعال في هذه الفترة')
                    return render(request , 'main/add_activity.html')
                
                new_activity.save()
                messages.success(request , ' تم اضافة النشاط بنجاح')
                return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':employee_id}))
            new_activity.save()
            messages.success(request , 'تم اضافة النشاط بنجاح')
            return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':employee_id}))
        messages.success(request , '   عذرا التاريخ غير صحيح ')
        return render(request , 'main/add_activity.html')
    return render(request , 'main/add_activity.html')
# Still need some issue fix
def editActivity(request : HttpRequest , activity_id):
    '''still one issue if we edit the activity after activity compleate we need to re check the date if the date is not more than or equal today keep take action as it is , if not we update the take action to 0'''
    assigen_activity = Activity.objects.get(id = activity_id)
   
    print(assigen_activity.activityName)
    print(assigen_activity.end_hijri_month)
    print(assigen_activity.activityName)
    for_emp=Employee.objects.get(id = assigen_activity.employee_active.id)


    if request.method == 'POST':
    

        full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
        full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
        full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
        full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
        full_start_en_date = full_start_en_date.isoformat()
        full_end_en_date = full_end_en_date.isoformat()
        assigen_activity.activityName=request.POST['activityName']
        assigen_activity.activity_in_out=request.POST['activity_in_out']
        assigen_activity.activity_location=request.POST['activity_location']
        assigen_activity.activity_type=request.POST['activity_type']
        
        assigen_activity.activity_st_date = full_start_en_date
        assigen_activity.activity_end_date=full_end_en_date
        assigen_activity.start_hijri_day=request.POST['hijridaystart']
        assigen_activity.start_hijri_month=request.POST['hijrimonthstart']
        assigen_activity.start_hijri_year=request.POST['hijriyearstart']
        assigen_activity.end_hijri_day=request.POST['hijridayend']
        assigen_activity.end_hijri_month=request.POST['hijrimonthend']
        assigen_activity.end_hijri_year=request.POST['hijriyearend']
        assigen_activity.full_start_hijri_date=full_start_hijri_date
        assigen_activity.full_end_hijri_date=full_end_hijri_date
        assigen_activity.writen_by_user = request.user
        if datetime.strptime(assigen_activity.activity_st_date, '%Y-%m-%d')< datetime.strptime(assigen_activity.activity_end_date,'%Y-%m-%d'):
            git_all_employee_activity = Activity.objects.filter(employee_active = assigen_activity.employee_active).exists()
            if git_all_employee_activity:

                for i in Activity.objects.filter(employee_active = assigen_activity.employee_active) :
                    if assigen_activity.id != i.id:
                        old_end_date=str(i.activity_end_date)
                        old_start_date=str(i.activity_st_date)
                        print(type(old_end_date))
                        print('...............')

                        if (datetime.strptime(old_end_date , '%Y-%m-%d') < datetime.strptime(assigen_activity.activity_st_date , '%Y-%m-%d')and (assigen_activity.activity_end_date , '%Y-%m-%d')> (old_end_date , '%Y-%m-%d'))or (datetime.strptime(assigen_activity.activity_end_date , '%Y-%m-%d') < datetime.strptime(old_start_date , '%Y-%m-%d') ) :
                            print(old_end_date)
                            print(assigen_activity.activity_end_date)
                            continue


                        messages.success(request , 'عذرا الموظف يوجد لديه نشاط فعال في هذه الفترة')
                        return render(request , 'main/edit_activity.html' , {'assigen_activity':assigen_activity })



                assigen_activity.save()
                messages.success(request , 'تم تعديل النشاط بنجاح')
                return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':for_emp.id}))
    return render(request , 'main/edit_activity.html' , {'assigen_activity':assigen_activity })

def delete_activity(request:HttpRequest, activity_id):
    assign_activity = Activity.objects.get(id=activity_id)
    if request.method=='POST':
        
        for_emp = Employee.objects.get(id = assign_activity.employee_active.id)
        print(assign_activity.id)
        
        if assign_activity.activity_type=='Type_two_courses' and assign_activity.activity_tack_action==1:
            assign_course=Course.objects.get(id=assign_activity.id)
            assign_course.delete()
            assign_activity.delete()
            messages.success(request, ' تم حذف الدورة بنجاح')
            return HttpResponseRedirect(reverse('main:show-course-mandate-emp', kwargs={"employee_id": for_emp.id}))
        elif assign_activity.activity_type=='Type_three_mandate'and assign_activity.activity_tack_action==1:
            assign_mandate=Mandate.objects.get(id=assign_activity.id)
            assign_mandate.delete()
            assign_activity.delete()
            messages.success(request, ' تم حذف الانتداب بنجاح')
            return HttpResponseRedirect(reverse('main:show-course-mandate-emp', kwargs={"employee_id": for_emp.id}))
        else:        
            assign_activity.delete()
            messages.success(request, 'تم حذف النشاط بنجاح')
            return HttpResponseRedirect(reverse('main:show-course-mandate-emp', kwargs={"employee_id": for_emp.id}))
    return render(request , 'main/delete_activity.html' , {'assign_activity':assign_activity})
        

   



def moving_activity_to_courser_after_complete(request : HttpRequest , activity_id):
    assign_activity=Activity.objects.get(id = activity_id)
    for_emp = Employee.objects.get(id = assign_activity.employee_active.id)
    if request.method=='POST':
        full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
        full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
        full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
        full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
        full_start_en_date = full_start_en_date.isoformat()
        full_end_en_date = full_end_en_date.isoformat()
        new_couorse = Course(id=assign_activity.id ,start_hijri_day = request.POST['hijridaystart'],start_hijri_month = request.POST['hijrimonthstart'],start_hijri_year = request.POST['hijriyearstart'] ,end_hijri_day = request.POST['hijridayend'] , end_hijri_month = request.POST['hijrimonthend'] ,end_hijri_year = request.POST['hijriyearend']  ,course_certficate_upload =  request.FILES.get('certificate_upload_pdf'),
        starthijridate =full_start_hijri_date , endhijridate= full_end_hijri_date,writen_by = request.user , assigend_employee = assign_activity.employee_active , title = request.POST['title'],course_number = request.POST['course_number'], course_provider = request.POST['course_provider'],  course_provider_country = request.POST['course_provider_country'],where_course_has_been_provide = request.POST['where_course_has_been_provide'],degree_percent=request.POST['degree_percent'],rating_word=request.POST['rating_word'],startDate=full_start_en_date,endDate=full_end_en_date )
        if datetime.strptime(new_couorse.startDate, '%Y-%m-%d') > datetime.strptime(new_couorse.endDate,'%Y-%m-%d'):
                messages.success(request , 'عذرا يرجى ادخال التاريخ بشكل صحيح')
        else:
            assign_activity.activity_tack_action=1
            assign_activity.save()
            new_couorse.save()
            messages.success(request , 'تمت اضافةالنشاط في قسم السجل التدريبي بنجاح ')
            return redirect(reverse('main:show-assigend', kwargs={"emplyee_id": for_emp.id}))


    return render(request , 'main/add-course.html' , {'assign_activity' : assign_activity , 'check_new_request_user':check_new_request_user})

def moving_activity_to_mandate_after_complete(request:HttpRequest , activity_id):
    assign_activity=Activity.objects.get(id = activity_id)
    for_emp = Employee.objects.get(id = assign_activity.employee_active.id)
    if request.method=='POST':

        full_start_hijri_date = f"{request.POST['hijridaystart']} / {request.POST['hijrimonthstart']} / {request.POST['hijriyearstart']}"
        full_end_hijri_date = f"{request.POST['hijridayend']} / {request.POST['hijrimonthend']} / {request.POST['hijriyearend']}"
        full_start_en_date =Hijri(int(request.POST['hijriyearstart']), int(request.POST['hijrimonthstart']),int(request.POST['hijridaystart'])).to_gregorian()
        full_end_en_date =Hijri(int(request.POST['hijriyearend']), int(request.POST['hijrimonthend']),int(request.POST['hijridayend'])).to_gregorian()
        full_start_en_date = full_start_en_date.isoformat()
        full_end_en_date = full_end_en_date.isoformat()
        new_mandate = Mandate(id=assign_activity.id,end_hijri_day = request.POST['hijridayend'] , end_hijri_month = request.POST['hijrimonthend'] , end_hijri_year = request.POST['hijriyearend'],start_hijri_day = request.POST['hijridaystart'],start_hijri_month=request.POST['hijrimonthstart'] , start_hijri_year = request.POST['hijriyearstart'] ,mandate_employee = for_emp , starthijridate = full_start_hijri_date , endhijridate = full_end_hijri_date  , writen_by = request.user , start_date = full_start_en_date , end_date=full_end_en_date ,mandate_place = request.POST['mandate_place'] ,mandate_type = assign_activity.activity_in_out )
        print(new_mandate)
        if datetime.strptime(new_mandate.start_date,'%Y-%m-%d') < datetime.strptime(new_mandate.end_date , '%Y-%m-%d'):
            assign_activity.activity_tack_action=1
            assign_activity.save()
            new_mandate.save()
            result_of_in_out = Activity.objects.get(pk = assign_activity.id)
            messages.success(request , 'تم اضافة الانتداب بنجاح')
        else:
            messages.success(request , 'عذرا يرجى ادخال تاريخ بداية و نهاية صحيح ')
            return render(request , 'main/add_mandate.html')
        return redirect(reverse('main:show-assigend' , kwargs={'emplyee_id':for_emp.id}))
    return render(request , 'main/add_mandate.html' , {'assign_activity' : assign_activity ,'check_new_request_user':check_new_request_user  } )

def aboutOmc(request:HttpRequest ):
    return render(request , 'main/about.html' ,{'check_new_request_user':check_new_request_user})

def dashBoradInfo(request : HttpRequest):
   #activity DashBoard
   all_activity_in_system = Activity.objects.filter(activity_type = 'Type_one_active')
   counter_for_all_activity_in_system : int = 0 
   for i in all_activity_in_system:
       counter_for_all_activity_in_system = counter_for_all_activity_in_system + 1
   print(counter_for_all_activity_in_system)
   all_activity_in_system_not_complete =Activity.objects.filter(activity_type = 'Type_one_active').filter(activity_tack_action = False)
   counter_for_all_activity_in_system_not_complete : int = 0 
   for j in all_activity_in_system_not_complete:
       counter_for_all_activity_in_system_not_complete = counter_for_all_activity_in_system_not_complete + 1 
   print(counter_for_all_activity_in_system_not_complete)   
   FinalResultForNotCompleteActivity = (counter_for_all_activity_in_system_not_complete / counter_for_all_activity_in_system) * 100
   print(FinalResultForNotCompleteActivity)
   print(int(FinalResultForNotCompleteActivity))
   FinalResultForNotCompleteActivity = int(FinalResultForNotCompleteActivity)
   print(type(FinalResultForNotCompleteActivity))
   #mandate Dashboard
   all_mandate_in_system = Activity.objects.filter(activity_type = 'Type_three_mandate')
   counter_for_all_mandate_inSystem : int = 0
   for i in all_mandate_in_system:
       counter_for_all_mandate_inSystem = counter_for_all_mandate_inSystem + 1
   print(counter_for_all_mandate_inSystem)
   all_mandate_not_completed = Activity.objects.filter(activity_type = 'Type_three_mandate').filter(activity_tack_action = False) 
   counter_for_all_mandate_not_complete : int = 0
   for i in all_mandate_not_completed:
       counter_for_all_mandate_not_complete = counter_for_all_mandate_not_complete +1
   finalResultForNotCompleteMandate = (counter_for_all_mandate_not_complete / counter_for_all_mandate_inSystem ) * 100
   finalResultForNotCompleteMandate = int(finalResultForNotCompleteMandate)
   #courses Dashboard
   all_courses_in_system = Activity.objects.filter(activity_type = 'Type_two_courses')
   counter_for_all_courses : int = 0
   for i in all_courses_in_system:
       counter_for_all_courses = counter_for_all_courses + 1
   all_courses_not_complete = Activity.objects.filter(activity_type = 'Type_two_courses').filter(activity_tack_action = False)
   counter_for_all_courses_not_complete : int = 0
   for j in all_courses_not_complete:
       counter_for_all_courses_not_complete = counter_for_all_courses_not_complete +1
   finalResultForCourses = (counter_for_all_courses_not_complete / counter_for_all_courses) * 100  
   finalResultForCourses = int(finalResultForCourses)
       

          

   return render(request , 'main/dashBord.html' , {'counter_for_all_courses':counter_for_all_courses , 'finalResultForCourses':finalResultForCourses ,'counter_for_all_courses_not_complete':counter_for_all_courses_not_complete ,'finalResultForNotCompleteMandate':finalResultForNotCompleteMandate, 'counter_for_all_mandate_not_complete':counter_for_all_mandate_not_complete ,'counter_for_all_mandate_inSystem':counter_for_all_mandate_inSystem ,'FinalResultForNotCompleteActivity':FinalResultForNotCompleteActivity ,'counter_for_all_activity_in_system_not_complete':counter_for_all_activity_in_system_not_complete , 'counter_for_all_activity_in_system':counter_for_all_activity_in_system })   
   



