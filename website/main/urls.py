from django.urls import path
from . import views
app_name='main'

urlpatterns = [
   path('' , views.home_page , name='home-page'), 
   path('add/', views.add_employee , name = 'add-employee'),  
   path('show/' , views.show_all_emp , name='show-all'),
   path('show/<emplyee_id>' , views.show_assiegnd_emplyee,name='show-assigend'),
   path('add_course/<employee_id>' , views.add_course , name='add-course') ,
   path('delete/<employee_id>', views.delet_employee , name='delete'),  
   path('update_emp/<employee_id>', views.update_employee , name='update'),
   path('add_mandate/<employee_id>' , views.add_mandate , name='add-mandate'),
   path('show_activityes/<employee_id>' , views.show_courses_and_mondate , name='show-course-mandate-emp'),
   path('show_mandates/<employee_id>' , views.show_mandates , name='show_mandate'),
   path('edit/<int:activity_id>/' , views.editCourse , name='update_course'),
   path('deleteCourse/<course_id>' , views.deleteCourse , name='delete-course'),
   path('update_mandate/<mandate_id>',views.editmandate , name='edit-mandate'),
   path('deleteMandate/<mandate_id>' , views.deleteMandate , name='delete-mandate'),
   path('test/' , views.showStatisticForMandate , name='stat'),
   path('show_request_user/' , views.show_request_user_for_admin , name='show-request'),
   path('accept/<int:employee_id>' , views.accept_user_request , name='accept-user'),
   path('rejectUser/<int:employee_id>' , views.reject_user_request , name='reject'),
   path('add_activiity/<int:employee_id>' , views.add_activity , name = 'add_activity'),
   path('delete_activity/<int:activity_id>' , views.delete_activity , name = 'delete_actvity'),
   path('updateActivity/<int:activity_id>' , views.editActivity , name = 'update_activity'),
   path('transfare_activity_to_courses_compleate/<int:activity_id>' , views.moving_activity_to_courser_after_complete , name = 'transfare_activity_to_courser'),
   path('transfare_activity_to_mandate_compleate/<int:activity_id>' , views.moving_activity_to_mandate_after_complete , name = 'transfare_activity_to_mandate'),
   path('about/' , views.aboutOmc , name='about'),
   path('showAllCourses/<int:employee_id>' , views.show_courses , name='showCourses'),
   path('dashbord/' , views.dashBoradInfo , name='dashboard'), 
   path('aaa/' , views.arabic_pdf , name='report'), 
   path('ReportForEmp/<int:employee_id>' , views.assiengEmployeeReport , name='ForEmpReport'), 

   
 
   
]