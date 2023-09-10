from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(
        attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'address',
                'placeholder': 'Электронная почта'
            }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password1',
                'placeholder': 'Введите пароль'
            }))
    confirm_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password1',
                'placeholder': 'Повторите пароль'
            }))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'fname',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'lname',
                'placeholder': 'Фамилия'
            }),
        }


class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'email',
            'name': 'email',
            'placeholder': 'Электронная почта'
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Введите пароль'
        }
    ))