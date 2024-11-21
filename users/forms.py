from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Username', 
            'class': 'form-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password', 
            'class': 'form-input'
        })
    )
