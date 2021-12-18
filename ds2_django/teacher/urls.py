from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    # -------------- general paths ----------
    path('home/', teacher, name='teacher_home'),
    path('group/', group, name='teacher_group'),
    path('Module/', Module, name='teacher_module'),
    path('Student/', Students, name='teacher_student'),
    path('Homework/', Homework, name='teacher_homework'),

    # --------------

    path('Student/details', Student_absence, name='teacher_student_details'),
    path('group/details/<int:id>', group_details, name='GroupDetail'),
    path(r'^deleteurl/(?P<pk>\d+)/$',DeleteGroup.as_view(), name='deletegroup'),


    path('group/modules/<int:id>' ,  groupModule ,  name= 'groupModule'),

    #-----------------
    path('Group/Addhomework/' ,  addstudenthomework , name='addstudenthomework'),
    path('Group/Addhomework/<int:id>', addGrouphomework, name='addgrouphomework'),

    path('Group/AddGroup', addGroup, name='addgroup'),
    path('Group/updateGroup/<int:id>', updateGroup, name='UpdateGroup'),
    path('Group/AddGrouphomework/<int:id>', addGrouphomework, name='addgrouphomework'),

    path('Module/AddModule', addModule, name='addModule'),


    path('student/AddStudent', addStudent, name='addstudent'),
    path('student/UpdateStudent/<int:id>', updateStudent, name='addstudent'),
    path('student/studentDetail/<int:id>', student_detail, name='studentdetail'),
    path('student/addstudentAbsencd/', student_add_absence, name='addabsence'),




    path('chart/', chart, name='chart'),


]
