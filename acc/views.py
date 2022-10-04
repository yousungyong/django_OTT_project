from django.shortcuts import render, redirect

from acc.forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.
def no_login(request):
  return render(request, 'acc/login.html')

def logout(request):
  return 0

def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('/Main/')
  else:
      form = UserForm()
  return render(request, 'acc/signup.html', {'form': form})