from django import forms
from .models import student,subject

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields  = ('index_no','email','first_name','last_name','phone_number')
            
        widgets = {
                'index_no': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control'}),

                
               
                
       }


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields  = ('index_no','subject_code','subject_name','marks','attendance')
            
        widgets = {
                'index_no': forms.TextInput(attrs={'class': 'form-control'}),
                'subject_code': forms.TextInput(attrs={'class': 'form-control'}),
                'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
                'marks': forms.NumberInput(attrs={'class': 'form-control'}),
                'attendance': forms.NumberInput(attrs={'class': 'form-control'}),

                
               
                
       }


