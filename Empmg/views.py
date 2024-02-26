from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def userhome(request):
    return render(request, 'userhome.html')

def updatepage(request):
    return render(request, 'update.html')

def createemp(request):
    return render(request, 'createemp.html')

def signin(request):
    return render(request, 'signin.html')

def createacc(request):
    return render(request, 'createaccount.html')

#future reference for when beginning redirecting pages between one another
#def logout_view(request):
  #  logout(request)
    #return redirect('home')  