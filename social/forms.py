from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

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

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Alguna cosa a dir?'}), required=True)

    class Meta:
        model = Post
        fields = ['content']
