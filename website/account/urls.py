from django.urls import path
from . import views

app_name = "account"   


urlpatterns = [

    path("register", views.sign_up_user, name="register"),
    path('logout/' , views.logout_user , name='logout'),
    path('login' , views.login_user , name='login')

]