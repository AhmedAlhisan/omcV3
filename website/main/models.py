from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=512)
    rank = models.CharField(max_length=512)
    employee_number = models.IntegerField()
    major = models.CharField(max_length=512)
    certificate = models.CharField(max_length=512)
    graduted_from = models.CharField(max_length=512)
    job_title = models.CharField(max_length=512)
    number_of_mandate_days=models.IntegerField( default=0)
    number_of_courses_days=models.IntegerField( default=0)
    work_place = models.CharField(max_length=512)
    writen_by = models.ForeignKey(User , on_delete=models.CASCADE)

class Activity(models.Model):
    activityName = models.CharField(max_length=512)
    activity_st_date = models.DateField()
    activity_end_date = models.DateField()
    start_hijri_day = models.CharField(max_length=512)
    start_hijri_month = models.CharField(max_length=512)
    start_hijri_year = models.CharField(max_length=512)
    end_hijri_day = models.CharField(max_length=512)
    end_hijri_month = models.CharField(max_length=512)
    end_hijri_year = models.CharField(max_length=512)
    full_start_hijri_date = models.CharField(max_length=512)
    full_end_hijri_date = models.CharField(max_length=512)
    employee_active = models.ForeignKey(Employee,on_delete=models.CASCADE)
    writen_by_user = models.ForeignKey(User , on_delete=models.CASCADE)
    activity_location = models.CharField(max_length=512)
    activity_tack_action=models.BooleanField(default=False)
    Type_one_active = '0'
    Type_two_courses = '1'
    Type_three_mandate = '2'
    
    Activity_type_choises = [
        (Type_one_active, '0'),
        (Type_two_courses, '1'),
        (Type_three_mandate, '2'),
        
    ]
    activity_type = models.CharField(
        max_length=10,
        choices=Activity_type_choises,
        
    )

    inside = 'inside'
    outside = 'outside'
    
    activity_in_out = [
        (inside, 'inside'),
        (outside, 'outside'),
        
    ]
    activity_in_out = models.CharField(
        max_length=10,
        choices=activity_in_out,
        
    )

class Course(models.Model):
    title = models.CharField(max_length=512)
    course_number = models.CharField(max_length=512)
    course_provider = models.CharField(max_length=512)
    course_provider_country = models.CharField(max_length=512)
    where_course_has_been_provide = models.CharField(max_length=512)
    degree_percent = models.FloatField()
    rating_word = models.CharField(max_length=512)
    course_certficate_upload = models.ImageField(upload_to="static/pdfs/" , default="Certificat not avilibale")
    startDate = models.DateField()
    endDate = models.DateField()
    start_hijri_day = models.CharField(max_length=512)
    start_hijri_month = models.CharField(max_length=512)
    start_hijri_year = models.CharField(max_length=512)
    end_hijri_day = models.CharField(max_length=512)
    end_hijri_month = models.CharField(max_length=512)
    end_hijri_year = models.CharField(max_length=512)
    starthijridate = models.CharField(max_length=512 , null=True)
    endhijridate = models.CharField(max_length=512 , null=True)
    assigend_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    writen_by = models.ForeignKey(User , on_delete=models.CASCADE )

    @property
    def date_diff(self):
        return (self.endDate - self.startDate).days
    
class Mandate(models.Model):
    inside = 'inside'
    outside = 'outside'
    
    mandate_type_choises = [
        (inside, 'inside'),
        (outside, 'outside'),
        
    ]
    mandate_type = models.CharField(
        max_length=10,
        choices=mandate_type_choises,
        default=inside,
    )

    mandate_place = models.CharField(max_length=512)
    mandate_employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    writen_by = models.ForeignKey(User , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_hijri_day = models.CharField(max_length=512)
    start_hijri_month = models.CharField(max_length=512)
    start_hijri_year = models.CharField(max_length=512)
    end_hijri_day = models.CharField(max_length=512)
    end_hijri_month = models.CharField(max_length=512)
    end_hijri_year = models.CharField(max_length=512)
    starthijridate = models.CharField(max_length=512 , null=True)
    endhijridate = models.CharField(max_length=512 , null=True)
    @property
    def date_diff(self):
        return (self.end_date - self.start_date).days
    

class test(models.Model):
    a=models.CharField(max_length=512)
    b=models.CharField(max_length=512)
    c=models.BooleanField(default=False)    
    





    