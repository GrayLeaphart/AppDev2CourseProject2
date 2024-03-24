from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.fields['username'].help_text = None
     self.fields['username'].error_messages['unique'] = "Account Already Exists  "
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
