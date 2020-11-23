from django.contrib.auth.forms import AuthenticationForm
from django import forms

from django.contrib.auth.models import User
from django.forms import fields


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        'name': 'username',
                                        'id': 'inputEmail',
                                        'class': 'form-control',
                                        'placeholder': 'Username or Email',
                                    }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Password',
                                       'id': 'inputPassword',
                                   }))
