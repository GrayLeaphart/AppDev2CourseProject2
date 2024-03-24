from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def home(request):
    return render(request, 'home.html')

@login_required
def userhome(request):
    username = request.user.username
    return render(request, 'userhome.html', {'username': username})

def updatepage(request):
    return render(request, 'update.html')

def createemp(request):
    return render(request, 'createemp.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

def createacc(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin') 
    else:
        form = UserRegistrationForm()
    return render(request, 'createaccount.html', {'form': form})

#future reference for when beginning redirecting pages between one another
#def logout_view(request):
  #  logout(request)
    #return redirect('home')  