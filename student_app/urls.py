from django.urls import path
from django.conf.urls import url
from . import views as v
from . import hodviews as hodv


urlpatterns = [
    path('', v.loginpage, name='login'),
    path('index', v.sdemo, name='index'),
    path('bc_tabs', v.vdemo, name='bc_tabs'),
    path('admin_home', hodv.admin_home , name='admin_home'),
    path('user_login', v.dologin, name='user_login'),
    path('dologin', v.dologin, name='dologin'),
    path('user_details', v.user_details, name='user_details'),
    path('user_logout', v.logout_user, name='user_logout'),
    path('admin_home', hodv.admin_home , name='admin_home'),

    path('addstaff', hodv.addstaff , name='addstaff'),
    path('addstaff_save', hodv.addstaff_save , name='addstaff_save'),
    path('managestaff', hodv.managestaff , name='managestaff'),

    path('addcourse', hodv.addcourse , name='addcourse'),
    path('addcourse_save', hodv.addcourse_save, name='addcourse_save'),

    path('addsubject', hodv.addsubject , name='addsubject'),
    path('addsubject_save', hodv.addsubject_save, name='addsubject_save'),

    path('addstudent', hodv.addstudent, name='addstudent'),
    path('addstudent_save', hodv.addstudent_save, name='addstudent_save'),
    path('managestudent', hodv.managestudent , name='managestudent'),
]