from django.contrib import admin

# Register your models here.
from . models import Employee ,Course,Mandate,Activity,test

# Register your models here.

admin.site.register(test)
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Mandate)
admin.site.register(Activity)
