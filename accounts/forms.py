from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import *


class RegisterForm(forms.Form):
    # first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'}))
    phone = forms.CharField(max_length=17, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'مثال: 09123456789'}))
    passwordd = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز عبور خود را وارد نمایید'}))
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل قبلا ثبت شده است')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('این نام کاربری قبلا استفاده شده است')
        return username
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور خود را وارد کنید'}))


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد نمایید',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'رمز عبور خود را وارد نمایید',}))
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone', 'address1', 'address2', 'area', 'state', 'postal_code', 'image')

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد نمایید',}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد نمایید',}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره همراه خود را وارد نمایید',}),
            'address1' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'',}),
            'address2' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'',}),
            'area' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'',}),
            'state' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'',}),
            'postal_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'',}),
            'image': forms.FileInput()
        }
