from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account
from ERMS.models import student

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address' )

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

 

    '''
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__()

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
'''

class StaffRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address' )

    
    class Meta:
        model = Account
        fields = ("email", "username","is_staff","is_admin","password1", "password2")


        '''
    def __init__(self, *args, **kwargs):
        super(StaffRegistrationForm,self).__init__()

        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['is_staff'].widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'''

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("invalid login")


               
                
       