from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class AddRegistrationForm(forms.ModelForm):
#     class Meta:
#         #model = Users
#         fields = '__all__'

    # creds = forms.CharField(max_length=255, label="Your Full Name")
    # email = forms.EmailField(max_length=50) 
    # nickname = forms.CharField(max_length=50)
    # password = forms.PasswordInput()
    # team = forms.ModelChoiceField(queryset=Teams.objects.all(), label="Ваша команда", required=True)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')