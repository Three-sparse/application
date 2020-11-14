from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'user_app/signup.html', context)

def index(request):
  user = request.user
  context = {'user':user}
  return render(request, 'user_app/index.html',context)

def logged_in(request):
  if request.user:
    return True
  else:
    return False
  
  
