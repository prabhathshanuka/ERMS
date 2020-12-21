from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from account.forms import RegistrationForm,StaffRegistrationForm,AccountAuthenticationForm
from django.views.generic import ListView, CreateView, DetailView

from .models import Account

# Create your views here.
def UserRegisterView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)



def StaffRegistrationView(request):
    context = {}
    if request.POST:
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['staff_registration_form'] = form
    else:
        form = StaffRegistrationForm()
        context['staff_registration_form'] = form
    return render(request, 'registration/Staff_register.html', context)



'''class StaffRegistrationView(CreateView):
	model = Account
	form_class = StaffRegistrationForm
	template_name = 'registration/Staff_register.html'''
   
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password=password)

        if user:
            login(request, user)
            return redirect("home")
        if user.is_anonymous:
             form = AccountAuthenticationForm()

       

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')