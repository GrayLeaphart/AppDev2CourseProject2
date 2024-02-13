from django.urls import path
from Empmg import views

urlpatterns = [
    path("", views.home, name="home"),
]
