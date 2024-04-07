from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

def deleteItem(request, id):
    item = get_object_or_404(Employee, id=id)
    item.delete()
    return redirect('userhome')
    

   
def home(request):
    return render(request, 'home.html')

@login_required
def userhome(request):
    username = request.user.username
    employees = Employee.objects.all()
    return render(request, 'userhome.html', {'username': username,  'employees': employees})


def redirect_to_userhome(request):
    return redirect('userhome')

def updateemployee(request, employ_id):
    employ = get_object_or_404(Employee, id=employ_id)
    if request.method == 'POST':
        employ.name = request.POST.get('name')
        employ.email = request.POST.get('email')
        employ.role = request.POST.get('role')
        employ.save()
        return redirect('userhome')
    return render(request, 'update.html', {'employ': employ})


@login_required
def createemp(request):
     if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)  # Save the form data but don't commit to the database yet
            employee.user = request.user  # Associate the employee with the current user
            employee.save()  # Now save the employee with the associated user
            return redirect('userhome')  # Redirect to a view displaying the list of employees
     else:
        form = EmployeeForm()
     return render(request, 'createemp.html', {'form': form})


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