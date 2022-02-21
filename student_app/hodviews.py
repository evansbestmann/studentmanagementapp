import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *


def admin_home(request):
    return render (request,"hod_templates/home_content.html")

def addstaff(request):
    return render (request,"hod_templates/addstaff.html")

def addstaff_save(request):
    if request.method!="POST":
        return HttpResponse ("Method not allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password = request.POST.get("password")
        username=request.POST.get("username")
        email=request.POST.get("email")

        address=request.POST.get("address")
        try:
           user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
           user.staff.address=address
           user.save()
           messages.success(request,"Staff added successfully")
           return HttpResponseRedirect("/addstaff")
        except:
            messages.error(request, "Failed to add staff")
            return HttpResponseRedirect("/addstaff")
def managestaff(request):
    staffs=Staff.objects.all()
    return render(request, "hod_templates/managestaff.html",{"staffs":staffs})

def addcourse(request):
    return render (request,"hod_templates/addcourse.html")

def addcourse_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        course = request.POST.get("course_name")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Course added successfully")
            return HttpResponseRedirect("/addcourse")
        except:
            messages.error(request, "Failed to add Course")
            return HttpResponseRedirect("/addcourse")

def addsubject(request):
    course=Courses.objects.all()
    #use customuser to drop down user_type 2 which staff
    staff = CustomUser.objects.filter(user_type=2)
    return render (request,"hod_templates/addsubject.html",{"course":course,"staff":staff})

def addsubject_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        subject = request.POST.get("subject_name")
        course_id= request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
        try:
            subject= Subjects(subject_name=subject,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request, "Subject added successfully")
            return HttpResponseRedirect("/addsubject")
        except:
            messages.error(request, "Failed to add Subject")
            return HttpResponseRedirect("/addsubject")

def addstudent(request):
    course=Courses.objects.all()
    return render (request,"hod_templates/addstudent.html",{"course":course})

def addstudent_save(request):
    if request.method!="POST":
        return HttpResponse ("Method not allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password = request.POST.get("password")
        username=request.POST.get("username")
        email=request.POST.get("email")
        session_start=request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id=request.POST.get("course")
        sex=request.POST.get("sex")


        address=request.POST.get("address")
        try:
           user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
           user.student.address=address
           course_obj=Courses.objects.get(id=course_id)
           user.student.course_id=course_obj
           user.student.session_starts_year=session_start
           user.student.session_ends_year=session_end
           user.student.gender=sex
           user.student.profile_pic=""
           user.save()
           messages.success(request,"Student added successfully")
           return HttpResponseRedirect("/addstudent")
        except:
            messages.error(request, "Failed to add student")
            return HttpResponseRedirect("/addstudent")
def managestudent(request):
    student=Student.objects.all()
    return render(request, "hod_templates/managestudent.html",{"student":student})