from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, DetailView
from account.models import Account
from .models import student,subject
from .forms import AddStudentForm,AddSubjectForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages



# Create your views here.

class HomeView(ListView):
	model = subject
	template_name = 'home.html'

class AddStudentView(CreateView):
	model = student
	form_class = AddStudentForm
	template_name = 'add_student.html'
	#fields = '__all__'
	#fields = ('index','name')

class AddSubjectView(CreateView):
	model = subject
	form_class = AddSubjectForm
	template_name = 'add_subjects.html'

	#fields = '__all__'


class view_results(ListView):
	model = subject
	fields = '__all__'
	template_name = 'view_result.html'


class view_student(ListView):
	model = student
	fields = '__all__'
	template_name = 'view_students.html'


class view_student_detail(DetailView):
	model = student
	fields = '__all__'
	template_name = 'view_student_details.html'

class view_attendance(ListView):
	model = subject
	fields = '__all__'
	template_name = 'view_attendence.html'

class view_exam_report(ListView):
	model = subject
	fields = '__all__'
	template_name = 'view_exam_report.html'


class view_course_report(ListView):
	model = subject
	fields = '__all__'
	template_name = 'view_course_report.html'



def stdview(request):
	try: 
		q = request.GET.get('q')
	except:
		q=None
	if q:
		sbjct = subject.objects.filter(subject_code__icontains=q) 
		
		context = {'query': q, 'sbjct': sbjct}
		template = "search.html"
	else:
		template = "search.html"
		context = {}	
	return render(request,template,context)




    




	
