"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 
from . import views
from .views import HomeView, AddStudentView,AddSubjectView,view_results,view_student,view_student_detail,view_attendance,view_exam_report,view_course_report #comming from views.py 

urlpatterns = [

	path('',HomeView.as_view(), name = "home"), #this is how we add the html view
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('add_subjects/', AddSubjectView.as_view(), name='add_subjects'),
    path('view_results/', view_results.as_view(), name='view_results'),
    path('students/', view_student.as_view(), name='view_student'),
    path('student/<int:pk>', view_student_detail.as_view(), name='view_student_details'),
    path('student/attendence/', view_attendance.as_view(), name='view_attendance'),
    path('student/examreport/',view_exam_report.as_view(), name='view_exam_report'),
    path('student/course_report/',view_course_report.as_view(), name='view_course_report'),
   
	
   
]   
