from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuari {username} creat amb èxit')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    context = {'form': form }

    return render(request, 'social/register.html', context)

def profile(request):
    return render(request, 'social/profile.html')
