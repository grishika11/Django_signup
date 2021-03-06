from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from demo.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    contact = forms.CharField(max_length=10)
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'contact', 'address','password1', 'password2', )