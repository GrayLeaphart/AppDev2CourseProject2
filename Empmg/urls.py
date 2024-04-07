from django.urls import path
from Empmg import views

urlpatterns = [
    path('Home/', views.home, name='home'),
    path('Signin/', views.signin, name='signin'),
    path('CreateAcc/', views.createacc, name='createaccount'),
    path('UserHome/', views.userhome, name='userhome'),
    path('update_employee/<int:employ_id>/', views.updateemployee, name='update_employee'),
    path('Createemp/', views.createemp, name="createemp"),
    path('delete-item/<int:id>/', views.deleteItem, name='delete-item'),
]
