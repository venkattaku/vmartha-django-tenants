from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import OnUsUser


class UserCreationForm(UserCreationForm):
    class Meta:
        model = OnUsUser
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = OnUsUser
        fields = ['username', 'email']