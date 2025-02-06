from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nom')
    last_name = forms.CharField(label='Cognom')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrassenya', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contrassenya', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }