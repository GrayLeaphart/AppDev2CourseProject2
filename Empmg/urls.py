from django.urls import path
from Empmg import views

urlpatterns = [
    path('Home/', views.home, name='home'),
    path('Signin/', views.signin, name='signin'),
    path('CreateAcc/', views.createacc, name='createaccount'),
    path('UserHome/', views.userhome, name='userhome'),
    path('Updateemp/', views.updatepage, name='update'),
    path('Createemp/', views.createemp, name="createemp")
]
