from django.urls import path
from Empmg import views

urlpatterns = [
    path('Home/', views.home, name='home'),
]
